"""CAP-VALIDATE-FACTUAL-STRUCTURED-NUMERIC: compare digit-written numbers.

Specification: docs/05-validation/NUMERIC-INTEGRITY-CAPABILITY.md
Status: EXPERIMENTAL. Compares numbers written with digits, classifying each
pair as exact, equivalent, rounding or changed (VALIDATION-MAP.md §16).
Dates are read as whole items (0.3.0). It does not read numbers written as
words, unit words, times, relative dates or what a number refers to. Inputs are never normalized (DEC-059).
"""
from __future__ import annotations

import re
import unicodedata
from collections.abc import Callable
from dataclasses import dataclass
from datetime import date
from decimal import ROUND_HALF_UP, Decimal
from functools import cache
from typing import Any

CAPABILITY_ID = "CAP-VALIDATE-FACTUAL-STRUCTURED-NUMERIC"
CAPABILITY_VERSION = "0.4.0"
FAMILY = "VALIDATE-FACTUAL-STRUCTURED"
DECIMAL_POINT = frozenset({"en", "ja", "zh"})
DECIMAL_COMMA = frozenset({"de", "es", "fr", "id", "it", "nl", "pl", "pt", "ru", "tr"})
TARGET_LANGUAGES = DECIMAL_POINT | DECIMAL_COMMA
NOT_MEASURED = ("numbers_as_words", "unit_words", "times_and_durations", "relative_dates", "abbreviated_months_not_followed_by_a_number", "two_digit_years", "what_each_number_refers_to", "ranges_and_comparisons")
SPACE_GROUP = "  "

# Letters that make a following digit part of a word (v2, H2O). Scripts written
# without spaces (kana, CJK ideographs) are excluded: digits sit directly after them.
_CJK = "\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uff66-\uff9f"
_LETTER_OR_DIGIT = rf"[^\W_{_CJK}]"
_NUMBER = re.compile(
    r"(?P<currency>[$€£¥]\s?)?"
    rf"(?P<sign>(?<!{_LETTER_OR_DIGIT})(?<![)])[-−])?"
    rf"(?<!{_LETTER_OR_DIGIT})(?P<body>\d+(?:[.,  ]\d+)*)"
    r"(?P<percent>[   ]?[%％])?"
    r"(?P<currency_after>[ \u00a0\u202f]?[$€£¥])?"
)


# Symbol -> (dimension, size in the dimension's base). Exact factors only.
UNITS: dict[str, tuple[str, Decimal]] = {
    "mg": ("mass", Decimal("0.001")), "g": ("mass", Decimal(1)), "kg": ("mass", Decimal(1000)), "t": ("mass", Decimal(1000000)),
    "mm": ("length", Decimal("0.001")), "cm": ("length", Decimal("0.01")), "m": ("length", Decimal(1)), "km": ("length", Decimal(1000)),
    "ml": ("volume", Decimal("0.001")), "cl": ("volume", Decimal("0.01")), "l": ("volume", Decimal(1)), "L": ("volume", Decimal(1)),
    "W": ("power", Decimal(1)), "kW": ("power", Decimal(1000)), "MW": ("power", Decimal(1000000)), "GW": ("power", Decimal(1000000000)),
    "Wh": ("energy", Decimal(1)), "kWh": ("energy", Decimal(1000)), "MWh": ("energy", Decimal(1000000)), "GWh": ("energy", Decimal(1000000000)),
    "ms": ("time", Decimal("0.001")), "s": ("time", Decimal(1)), "min": ("time", Decimal(60)), "h": ("time", Decimal(3600)),
    "Hz": ("frequency", Decimal(1)), "kHz": ("frequency", Decimal(1000)), "MHz": ("frequency", Decimal(1000000)), "GHz": ("frequency", Decimal(1000000000)),
    "B": ("data", Decimal(1)), "kB": ("data", Decimal(1000)), "KB": ("data", Decimal(1000)), "MB": ("data", Decimal(1000000)), "GB": ("data", Decimal(1000000000)), "TB": ("data", Decimal(1000000000000)),
    "m²": ("area", Decimal(1)), "m2": ("area", Decimal(1)), "km²": ("area", Decimal(1000000)), "km2": ("area", Decimal(1000000)), "ha": ("area", Decimal(10000)),
    "m³": ("capacity", Decimal(1)), "m3": ("capacity", Decimal(1)),
    "°C": ("celsius", Decimal(1)), "°F": ("fahrenheit", Decimal(1)),
    "km/h": ("speed_kmh", Decimal(1)), "mph": ("speed_mph", Decimal(1)),
    "EUR": ("eur", Decimal(1)), "USD": ("usd", Decimal(1)), "GBP": ("gbp", Decimal(1)), "JPY": ("jpy", Decimal(1)),
}
_UNIT = re.compile(r"[ \u00a0\u202f]?(" + "|".join(sorted(map(re.escape, UNITS), key=len, reverse=True)) + r")" + rf"(?!{_LETTER_OR_DIGIT})")
_LIST_MARKER_AFTER = re.compile(r"[.)]\s")
_LETTER_HYPHEN = re.compile(r"[^\W\d_]-$")
_HYPHEN_LETTER = re.compile(r"-[^\W\d_]")


# Month names per language (lower case; "|" separates accepted forms of one month).
MONTHS: dict[str, tuple[str, ...]] = {
    "en": ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"),
    "it": ("gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"),
    "es": ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre|setiembre", "octubre", "noviembre", "diciembre"),
    "fr": ("janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"),
    "de": ("januar|jänner", "februar", "märz", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "dezember"),
    "pt": ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"),
    "nl": ("januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"),
    "id": ("januari", "februari", "maret", "april", "mei", "juni", "juli", "agustus", "september", "oktober", "november", "desember"),
    "tr": ("ocak", "şubat", "mart", "nisan", "mayıs", "haziran", "temmuz", "ağustos", "eylül", "ekim", "kasım", "aralık"),
    "pl": ("styczeń|stycznia", "luty|lutego", "marzec|marca", "kwiecień|kwietnia", "maj|maja", "czerwiec|czerwca", "lipiec|lipca", "sierpień|sierpnia", "wrzesień|września", "październik|października", "listopad|listopada", "grudzień|grudnia"),
    "ru": ("январь|января", "февраль|февраля", "март|марта", "апрель|апреля", "май|мая", "июнь|июня", "июль|июля", "август|августа", "сентябрь|сентября", "октябрь|октября", "ноябрь|ноября", "декабрь|декабря"),
}
# Abbreviations are read only before a number; "" means no abbreviation is read.
MONTH_ABBREVIATIONS: dict[str, tuple[str, ...]] = {
    "en": ("jan", "feb", "mar", "apr", "", "jun", "jul", "aug", "sep|sept", "oct", "nov", "dec"),
    "it": ("gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"),
    "es": ("ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep|sept", "oct", "nov", "dic"),
    "fr": ("janv|jan", "févr|fév", "", "avr", "", "", "juil", "", "sept", "oct", "nov", "déc"),
    "de": ("jan", "feb", "mär", "apr", "", "jun", "jul", "aug", "sep|sept", "okt", "nov", "dez"),
    "pt": ("jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"),
    "nl": ("jan", "feb", "mrt", "apr", "", "jun", "jul", "aug", "sep|sept", "okt", "nov", "dec"),
    "id": ("jan", "feb", "mar", "apr", "", "jun", "jul", "agu|ags", "sep", "okt", "nov", "des"),
    "tr": ("oca", "şub", "mar", "nis", "may", "haz", "tem", "ağu", "eyl", "eki", "kas", "ara"),
    "pl": ("sty", "lut", "mar", "kwi", "", "cze", "lip", "sie", "wrz", "paź", "lis", "gru"),
    "ru": ("янв", "фев", "мар", "апр", "", "июн", "июл", "авг", "сен|сент", "окт", "ноя", "дек"),
}
ISO_CURRENCY_SYMBOL = {"EUR": "€", "USD": "$", "GBP": "£", "JPY": "¥"}
_START = rf"(?<!{_LETTER_OR_DIGIT})(?<![.,/\-])"
_END = rf"(?!{_LETTER_OR_DIGIT})(?![-/.]\d)"
_DAY_MARK = r"(?:\.|er|º|°|st|nd|rd|th)?"
_YEAR_AFTER_MONTH = rf"[\s,]+(?:del?\s+)?(?P<year>\d{{4}}){_END}"
_YMD = re.compile(rf"{_START}(?P<year>\d{{4}})(?P<sep>[-/.])(?P<month>\d{{1,2}})(?P=sep)(?P<day>\d{{1,2}}){_END}")
_XYY = re.compile(rf"{_START}(?P<first>\d{{1,2}})(?P<sep>[-/.])(?P<second>\d{{1,2}})(?P=sep)(?P<year>\d{{4}}){_END}")
_CJK_DATES = (
    re.compile(r"(?<!\d)(?P<year>\d{4})年(?P<month>\d{1,2})月(?:(?P<day>\d{1,2})[日号])?"),
    re.compile(r"(?<!\d)(?P<month>\d{1,2})月(?P<day>\d{1,2})[日号]"),
)


def _month_key(name: str) -> str:
    return name.casefold().replace("ı", "i")


@cache
def _month_patterns(language: str) -> tuple[dict[str, int], tuple[re.Pattern[str], ...]]:
    """Return the month index and the name-based date patterns, most specific first."""
    if language not in MONTHS:
        return {}, ()
    def alternatives(months: tuple[str, ...]) -> list[str]:
        return sorted((form for forms in months for form in forms.split("|") if form), key=len, reverse=True)

    index = {_month_key(form): number for months in (MONTHS[language], MONTH_ABBREVIATIONS[language]) for number, forms in enumerate(months, 1) for form in forms.split("|") if form}
    forms = alternatives(MONTHS[language])
    # English month names are capitalized; this keeps the verb "may" and "to march" out.
    flags = 0 if language == "en" else re.IGNORECASE
    names = "|".join(re.escape(form.capitalize() if language == "en" else form) for form in forms)
    name = rf"(?P<name>{names})(?!{_LETTER_OR_DIGIT})"
    patterns = [re.compile(rf"{_START}(?P<day>\d{{1,2}}){_DAY_MARK}\s+(?:(?:of|de)\s+)?{name}(?:{_YEAR_AFTER_MONTH})?", flags)]
    if language == "en":
        patterns.append(re.compile(rf"{_START}{name}\s+(?P<day>\d{{1,2}})(?:st|nd|rd|th)?(?!{_LETTER_OR_DIGIT})(?:,?\s+(?P<year>\d{{4}}){_END})?", flags))
    patterns.append(re.compile(rf"{_START}{name}{_YEAR_AFTER_MONTH}", flags))
    short = "|".join(re.escape(form.capitalize() if language == "en" else form) for form in alternatives(MONTH_ABBREVIATIONS[language]))
    abbreviated = rf"(?P<name>{short})(?:\.|(?!{_LETTER_OR_DIGIT}))"
    patterns.append(re.compile(rf"{_START}(?P<day>\d{{1,2}}){_DAY_MARK}\s+(?:(?:of|de)\s+)?{abbreviated}{_YEAR_AFTER_MONTH}", flags))
    if language == "en":
        patterns.append(re.compile(rf"{_START}{abbreviated}\s+(?P<day>\d{{1,2}})(?:st|nd|rd|th)?(?!{_LETTER_OR_DIGIT})(?:,?\s+(?P<year>\d{{4}}){_END})?", flags))
    patterns.append(re.compile(rf"{_START}{abbreviated}{_YEAR_AFTER_MONTH}", flags))
    return index, tuple(patterns)


@dataclass(frozen=True)
class DateMention:
    raw: str
    readings: frozenset[tuple[int | None, int, int | None]]  # (year, month, day)
    relies_on_convention: bool = False


def _valid_date(year: int | None, month: int, day: int | None) -> bool:
    try:
        date(2000 if year is None else year, month, 1 if day is None else day)
    except ValueError:
        return False
    return True


def _numeric_date(raw: str, first: int, second: int, year: int, language: str) -> DateMention | None:
    """Read d/m/y or m/d/y. English keeps both readings; other languages read day first."""
    day_first, month_first = (year, second, first), (year, first, second)
    valid = [reading for reading in (day_first, month_first) if _valid_date(*reading)]
    if not valid:
        return None
    if len(valid) == 1 or first == second:
        return DateMention(raw, frozenset(valid[:1]))
    return DateMention(raw, frozenset(valid if language == "en" else [day_first]), True)


def _mention_from(match: re.Match[str], language: str, month_index: dict[str, int]) -> DateMention | None:
    groups = match.groupdict()
    year = int(_ascii_digits(groups["year"])) if groups.get("year") else None
    if groups.get("first"):
        return None if year is None else _numeric_date(match.group(0), int(_ascii_digits(groups["first"])), int(_ascii_digits(groups["second"])), year, language)
    month = month_index.get(_month_key(groups["name"])) if groups.get("name") else int(_ascii_digits(groups["month"]))
    day = int(_ascii_digits(groups["day"])) if groups.get("day") else None
    if month is None or not _valid_date(year, month, day):
        return None
    return DateMention(match.group(0), frozenset({(year, month, day)}))


def find_dates(text: str, language: str) -> list[tuple[int, int, DateMention]]:
    """Return non-overlapping dates as (start, end, mention), in textual order."""
    month_index, named = _month_patterns(language)
    patterns: tuple[re.Pattern[str], ...] = (_YMD, _XYY, *(_CJK_DATES if language in {"ja", "zh"} else ()), *named)
    found: list[tuple[int, int, DateMention]] = []
    for pattern in patterns:
        for match in pattern.finditer(text):
            if any(match.start() < end and start < match.end() for start, end, _ in found):
                continue
            mention = _mention_from(match, language, month_index)
            if mention is not None:
                found.append((match.start(), match.end(), mention))
    return sorted(found, key=lambda item: item[0])


@dataclass(frozen=True)
class Number:
    raw: str
    value: Decimal | None
    decimals: int
    percent: bool
    currency: str
    relies_on_convention: bool
    identifier_like: bool = False
    unit: str = ""

    def kind(self) -> tuple[Decimal | None, bool, str]:
        return (self.value, self.percent, self.currency)

    def base_value(self) -> tuple[str, Decimal] | None:
        """Return dimension and value in that dimension's base, if a unit is known."""
        if self.value is None or self.unit not in UNITS:
            return None
        dimension, size = UNITS[self.unit]
        return dimension, self.value * size


def _ascii_digits(text: str) -> str:
    return "".join(str(unicodedata.digit(c)) if c.isdigit() else c for c in text)


def _valid_groups(parts: list[str]) -> bool:
    return 1 <= len(parts[0]) <= 3 and all(len(p) == 3 for p in parts[1:])


def _parse(body: str, decimal: str) -> tuple[Decimal | None, int, bool]:
    """Return value, decimals and whether the reading depends on the language."""
    text = _ascii_digits(body)
    group = "," if decimal == "." else "."
    separators = [c for c in text if c in ".," + SPACE_GROUP]
    if not separators:
        return Decimal(text), 0, False
    for space in SPACE_GROUP:
        text = text.replace(space, group)
    tail = text.rsplit(decimal, 1) if decimal in text else [text]
    if len(tail) == 2 and decimal in tail[0]:
        return None, 0, False
    whole, fraction = tail[0], tail[1] if len(tail) == 2 else ""
    groups = whole.split(group)
    if len(groups) > 1 and not _valid_groups(groups):
        return None, 0, False
    single = len(separators) == 1 and separators[0] in ".,"
    number = "".join(groups)
    if fraction:
        ambiguous = single and len(fraction) == 3 and not number.startswith("0")
        return Decimal(f"{number}.{fraction}"), len(fraction), ambiguous
    ambiguous = single and len(groups[-1]) == 3 and not number.startswith("0")
    return Decimal(number), 0, ambiguous


def extract(text: str, language: str) -> list[Number]:
    """Extract digit-written numbers in textual order, leaving out those inside dates."""
    decimal = "." if language in DECIMAL_POINT else ","
    date_spans = [(start, end) for start, end, _ in find_dates(text, language)]
    numbers = []
    for match in _NUMBER.finditer(text):
        if any(match.start() < end and start < match.end() for start, end in date_spans):
            continue
        line_start = text.rfind("\n", 0, match.start()) + 1
        if (
            not text[line_start:match.start()].strip()
            and not match["currency"] and not match["currency_after"] and not match["sign"] and not match["percent"]
            and len(match["body"]) <= 3 and match["body"].isdigit()
            and _LIST_MARKER_AFTER.match(text, match.end())
        ):
            continue
        value, decimals, relies = _parse(match["body"], decimal)
        if value is not None and match["sign"]:
            value = -value
        before, after = text[max(0, match.start() - 2):match.start()], text[match.end():match.end() + 2]
        identifier_like = bool(_LETTER_HYPHEN.search(before) or _HYPHEN_LETTER.match(after))
        unit_match = None if match["percent"] or match["currency_after"] else _UNIT.match(text, match.end())
        unit = unit_match.group(1) if unit_match else ""
        raw = match.group(0).strip()
        currency = (match["currency"] or match["currency_after"] or "").strip()
        if unit in ISO_CURRENCY_SYMBOL and not currency:  # 500 EUR and 500 € are one currency
            raw, currency, unit = f"{raw} {unit}", ISO_CURRENCY_SYMBOL[unit], ""
        numbers.append(Number(raw, value, decimals, bool(match["percent"]), currency, relies, identifier_like, unit))
    return numbers


def _units_compatible(source: Number, target: Number) -> bool:
    return source.unit == target.unit or not source.unit or not target.unit


def _is_conversion(source: Number, target: Number) -> bool:
    if not source.unit or not target.unit or source.unit == target.unit:
        return False
    first, second = source.base_value(), target.base_value()
    return first is not None and first == second and (source.percent, source.currency) == (target.percent, target.currency)


def _is_rounding(source: Number, target: Number) -> bool:
    if not _units_compatible(source, target):
        return False
    if source.value is None or target.value is None or (source.percent, source.currency) != (target.percent, target.currency):
        return False
    if target.decimals >= source.decimals:
        return False
    step = Decimal(1).scaleb(-target.decimals)
    return source.value.quantize(step, rounding=ROUND_HALF_UP) == target.value


def _same_kind(source: Number, target: Number) -> bool:
    return source.value is not None and source.kind() == target.kind() and _units_compatible(source, target)


def _same_text_and_unit(source: Number, target: Number) -> bool:
    return source.raw == target.raw and source.unit == target.unit


def _same_text(source: Number, target: Number) -> bool:
    return source.raw == target.raw and _units_compatible(source, target)


def _pair[T: (Number, DateMention)](first: list[T], second: list[T], free: set[int], used: dict[int, int], test: Callable[[T, T], bool]) -> list[tuple[int, int]]:
    """Pair each unmatched source number with the first free target passing test."""
    found = []
    for i, source in enumerate(first):
        if i in used:
            continue
        for j in sorted(free):
            if test(source, second[j]):
                free.remove(j)
                used[i] = j
                found.append((i, j))
                break
    return found


def compare(first: list[Number], second: list[Number]) -> dict[str, Any]:
    """Pair numbers: exact first, then equivalent, then rounding; the rest changed."""
    free = set(range(len(second)))
    used: dict[int, int] = {}
    paired = _pair(first, second, free, used, _same_text_and_unit) + _pair(first, second, free, used, _same_text)
    out: dict[str, Any] = {"exact": [first[i].raw for i, _ in paired]}
    for label, test in (("equivalent", _same_kind), ("unit_conversion", _is_conversion), ("rounding", _is_rounding)):
        out[label] = [
            {
                "original": first[i].raw,
                "candidate": second[j].raw,
                "relies_on_language_convention": first[i].relies_on_convention or second[j].relies_on_convention,
            }
            for i, j in _pair(first, second, free, used, test)
        ]
    out["removed"] = [n.raw for i, n in enumerate(first) if i not in used]
    out["added"] = [second[j].raw for j in sorted(free)]
    out["identifier_like_changes"] = sum(n.identifier_like for i, n in enumerate(first) if i not in used) + sum(second[j].identifier_like for j in free)
    out["unit_uncertain"] = [
        {"original": f"{first[i].raw} {first[i].unit}".strip(), "candidate": f"{second[j].raw} {second[j].unit}".strip()}
        for i, j in sorted(used.items())
        if first[i].unit != second[j].unit and not (first[i].unit and second[j].unit)
    ]
    targets = [used[i] for i in sorted(used)]
    out["pairs_in_order"] = targets == sorted(targets)
    return out


def compare_dates(first: list[DateMention], second: list[DateMention]) -> dict[str, Any]:
    """Pair dates: same text first, then same date in another form; the rest changed."""
    free = set(range(len(second)))
    used: dict[int, int] = {}
    exact = _pair(first, second, free, used, lambda a, b: a.raw == b.raw)
    equivalent = _pair(first, second, free, used, lambda a, b: bool(a.readings & b.readings))
    targets = [used[i] for i in sorted(used)]
    return {
        "exact": [first[i].raw for i, _ in exact],
        "equivalent": [
            {"original": first[i].raw, "candidate": second[j].raw, "relies_on_language_convention": first[i].relies_on_convention or second[j].relies_on_convention}
            for i, j in equivalent
        ],
        "removed": [d.raw for i, d in enumerate(first) if i not in used],
        "added": [second[j].raw for j in sorted(free)],
        "in_order": targets == sorted(targets),
    }


def _base(language: str, constraint_type: str) -> dict[str, Any]:
    return {
        "family": FAMILY, "capability_id": CAPABILITY_ID, "capability_version": CAPABILITY_VERSION,
        "lifecycle_status": "EXPERIMENTAL", "constraint_type": constraint_type, "confidence": None,
        "evidence_basis": [], "language": language, "not_measured": list(NOT_MEASURED),
    }


def validate(
    original: str,
    candidate: str,
    *,
    language: str,
    constraint_type: str,
    permit_rounding: bool = False,
    max_chars: int | None = None,
) -> dict[str, Any]:
    """Compare digit-written numbers; result follows VALIDATION-ARCHITECTURE.md §8."""
    if not isinstance(original, str) or not isinstance(candidate, str):
        raise TypeError("original and candidate must be str")
    if constraint_type not in {"HARD", "SOFT"}:
        raise ValueError("constraint_type must be HARD or SOFT")
    base = _base(language, constraint_type)
    if language not in TARGET_LANGUAGES:
        return base | {"outcome": "unsupported", "reason": f"language {language!r}"}
    if max_chars is not None and max(len(original), len(candidate)) > max_chars:
        return base | {"outcome": "not measurable", "reason": "input exceeds max_chars"}
    first, second = extract(original, language), extract(candidate, language)
    comparison = compare(first, second)
    first_dates = [mention for _, _, mention in find_dates(original, language)]
    second_dates = [mention for _, _, mention in find_dates(candidate, language)]
    dates = compare_dates(first_dates, second_dates)
    dates_in_order = bool(dates.pop("in_order"))
    comparison["dates"] = dates
    changed = bool(comparison["removed"] or comparison["added"] or dates["removed"] or dates["added"])
    rounding_fails = bool(comparison["rounding"]) and not permit_rounding
    convention = any(e["relies_on_language_convention"] for e in comparison["equivalent"] + comparison["unit_conversion"] + comparison["rounding"] + dates["equivalent"])
    order_kept = bool(comparison.pop("pairs_in_order")) and dates_in_order
    if changed or rounding_fails:
        outcome, severity = "FAIL", "CRITICAL"
    else:
        outcome, severity = ("partially measured" if convention or not order_kept or comparison["unit_uncertain"] else "PASS"), None
    return base | {
        "outcome": outcome, "severity": severity, "comparison": comparison,
        "order_preserved": order_kept, "relies_on_language_convention": convention,
        "decimal_convention": "point" if language in DECIMAL_POINT else "comma",
        "counts": {"original": len(first), "candidate": len(second), "original_dates": len(first_dates), "candidate_dates": len(second_dates)},
    }
