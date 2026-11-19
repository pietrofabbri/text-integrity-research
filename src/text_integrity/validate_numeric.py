"""CAP-VALIDATE-FACTUAL-STRUCTURED-NUMERIC: compare digit-written numbers.

Specification: docs/05-validation/NUMERIC-INTEGRITY-CAPABILITY.md
Status: EXPERIMENTAL. Compares numbers written with digits, classifying each
pair as exact, equivalent, rounding or changed (VALIDATION-MAP.md §16).
Dates are read as whole items (0.3.0); single number words and codes such
as v2.3 are read (0.6.0). It does not read compound number words, unit words,
times, relative dates or what a number refers to. Inputs are never normalized (DEC-059).
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

from text_integrity import number_words, unit_words

CAPABILITY_ID = "CAP-VALIDATE-FACTUAL-STRUCTURED-NUMERIC"
CAPABILITY_VERSION = "0.8.0"
FAMILY = "VALIDATE-FACTUAL-STRUCTURED"
DECIMAL_POINT = frozenset({"en", "ja", "zh"})
DECIMAL_COMMA = frozenset({"de", "es", "fr", "id", "it", "nl", "pl", "pt", "ru", "tr"})
TARGET_LANGUAGES = DECIMAL_POINT | DECIMAL_COMMA
NOT_MEASURED = ("compound_number_words", "number_words_in_ja_zh", "unit_words_outside_seven_languages", "times_and_durations", "relative_dates", "abbreviated_months_not_followed_by_a_number", "two_digit_years", "what_each_number_refers_to", "ranges_and_comparisons")
SPACE_GROUP = "  "

# Letters that make a following digit part of a word (v2, H2O). Scripts written
# without spaces (kana, CJK ideographs) are excluded: digits sit directly after them.
_CJK = "\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uff66-\uff9f"
_LETTER_OR_DIGIT = rf"[^\W_{_CJK}]"
_NUMBER = re.compile(
    r"(?P<currency>[$€£¥][ \u00a0\u202f]?|(?<![^\W_])(?:EUR|USD|GBP|JPY)[ \u00a0\u202f])?"
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
    "°C": ("temperature", Decimal(1)), "°F": ("temperature", Decimal(1)),  # °F is converted by _to_base
    "km/h": ("speed", Decimal(1)), "mph": ("speed", Decimal("1.609344")),
    # Units outside the metric system, with their exact definitions (0.7.0)
    "mi": ("length", Decimal("1609.344")), "ft": ("length", Decimal("0.3048")), "yd": ("length", Decimal("0.9144")),
    "lb": ("mass", Decimal("453.59237")), "oz": ("mass", Decimal("28.349523125")),
    "EUR": ("eur", Decimal(1)), "USD": ("usd", Decimal(1)), "GBP": ("gbp", Decimal(1)), "JPY": ("jpy", Decimal(1)),
}
WORD_ONLY_UNITS = frozenset({"mi"})  # read only from words such as "miles": "mi" is also a pronoun
_UNIT = re.compile(r"[ \u00a0\u202f]?(" + "|".join(sorted(map(re.escape, set(UNITS) - WORD_ONLY_UNITS), key=len, reverse=True)) + r")" + rf"(?!{_LETTER_OR_DIGIT})")


@cache
def _unit_word_pattern(language: str) -> re.Pattern[str] | None:
    words = unit_words.unit_words(language)
    if not words:
        return None
    alternatives = "|".join(re.escape(w).replace("\\ ", "[ \u00a0]") for w in sorted(words, key=len, reverse=True))
    return re.compile(rf"[ \u00a0\u202f]?({alternatives})(?![\w-])", re.IGNORECASE)


# Percent written as words after a number (0.8.0): 25 per cento, 25 pour cent
PERCENT_WORDS: dict[str, tuple[str, ...]] = {
    "it": ("per cento", "percento"), "en": ("per cent", "percent"), "fr": ("pour cent", "pour-cent"),
    "de": ("Prozent",), "es": ("por ciento",), "pt": ("por cento",), "nl": ("procent",),
    "ru": ("процентов", "процента", "процент"), "pl": ("procent", "procentów", "procenty"), "id": ("persen",),
}


@cache
def _percent_word_pattern(language: str) -> re.Pattern[str] | None:
    words = PERCENT_WORDS.get(language)
    if not words:
        return None
    alternatives = "|".join(re.escape(w).replace("\\ ", "[ \u00a0]") for w in sorted(words, key=len, reverse=True))
    return re.compile(rf"[ \u00a0\u202f]({alternatives})(?![\w-])", re.IGNORECASE)


def _to_base(value: Decimal, unit: str) -> Decimal:
    if unit == "°F":
        return (value - 32) * 5 / 9
    return value * UNITS[unit][1]


def _from_base(value: Decimal, unit: str) -> Decimal:
    if unit == "°F":
        return value * 9 / 5 + 32
    return value / UNITS[unit][1]
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
    unit_text: str = ""

    def kind(self) -> tuple[Decimal | None, bool, str]:
        return (self.value, self.percent, self.currency)

    def base_value(self) -> tuple[str, Decimal] | None:
        """Return dimension and value in that dimension's base, if a unit is known."""
        if self.value is None or self.unit not in UNITS:
            return None
        return UNITS[self.unit][0], _to_base(self.value, self.unit)


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


# A code: letters and digits joined, with a letter directly before a digit
# (v2.3, H2O, A4, CO2). Compared literally, as one item (0.6.0).
_CODE_TOKEN = re.compile(rf"(?:[^\W{_CJK}]|[.\-/])+")
_LETTER_THEN_DIGIT = re.compile(rf"[^\W\d_{_CJK}]\d")


def find_codes(text: str) -> list[tuple[int, int, str]]:
    """Return codes as (start, end, text), in textual order. Unit symbols such as m2 are not codes."""
    found = []
    for match in _CODE_TOKEN.finditer(text):
        token = match.group(0)
        lead, trail = len(token) - len(token.lstrip(".-/")), len(token) - len(token.rstrip(".-/"))
        core = token[lead:len(token) - trail]
        if core and _LETTER_THEN_DIGIT.search(core) and core not in UNITS:
            found.append((match.start() + lead, match.end() - trail, core))
    return found


@cache
def _word_pattern(language: str) -> re.Pattern[str] | None:
    words = number_words.lexicon(language)
    if not words:
        return None
    alternatives = "|".join(map(re.escape, sorted(words, key=len, reverse=True)))
    return re.compile(rf"(?<![\w-])(?:{alternatives})(?![\w-])", re.IGNORECASE)


def _word_numbers(text: str, language: str, taken: list[tuple[int, int]]) -> list[tuple[int, int, Number]]:
    pattern = _word_pattern(language)
    if pattern is None:
        return []
    words = number_words.lexicon(language)
    found = []
    for match in pattern.finditer(text):
        if any(match.start() < end and start < match.end() for start, end in taken):
            continue
        value = words[match.group(0).lower()]
        found.append((match.start(), match.end(), Number(match.group(0), value, 0, False, "", False)))
    return found


def _merge_multipliers(items: list[tuple[int, int, Number]], text: str, language: str) -> list[tuple[int, int, Number]]:
    """Join a number and the multiplier word after it: 4,8 milioni = 4800000."""
    multipliers = number_words.MULTIPLIERS.get(language, {})
    merged: list[tuple[int, int, Number]] = []
    for start, end, number in items:
        if merged and number.raw.lower() in multipliers and number.value is not None:
            first_start, first_end, first = merged[-1]
            if first.value is not None and not first.unit and not text[first_end:start].strip() and "\n" not in text[first_end:start]:
                raw = text[first_start:end]
                merged[-1] = (first_start, end, Number(raw, first.value * number.value, 0, first.percent, first.currency, first.relies_on_convention, first.identifier_like))
                continue
        merged.append((start, end, number))
    return merged


def extract(text: str, language: str) -> list[Number]:
    """Extract numbers in textual order: digits and number words, leaving out dates and codes."""
    decimal = "." if language in DECIMAL_POINT else ","
    taken = [(start, end) for start, end, _ in find_dates(text, language)] + [(start, end) for start, end, _ in find_codes(text)]
    items: list[tuple[int, int, Number]] = []
    word_spans: list[tuple[int, int]] = []
    for match in _NUMBER.finditer(text):
        if any(match.start() < end and start < match.end() for start, end in taken):
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
        percent = bool(match["percent"])
        percent_word = None if percent or match["currency_after"] else (_percent_word_pattern(language) or re.compile(r"(?!)")).match(text, match.end())
        if percent_word:
            percent = True
            word_spans.append((match.end(), percent_word.end()))
        unit_match = None if percent or match["currency_after"] else _UNIT.match(text, match.end())
        unit = unit_match.group(1) if unit_match else ""
        unit_text = unit
        word_pattern = _unit_word_pattern(language)
        if not unit and word_pattern and not percent and not match["currency_after"]:
            word_match = word_pattern.match(text, match.end())
            if word_match:
                unit_text = word_match.group(1)
                unit = unit_words.unit_words(language)[" ".join(unit_text.split()).lower()]
        raw = match.group(0).strip()
        currency = (match["currency"] or match["currency_after"] or "").strip()
        currency = ISO_CURRENCY_SYMBOL.get(currency, currency)  # EUR 350 and € 350 are one currency
        if unit in ISO_CURRENCY_SYMBOL and not currency:  # 500 EUR and 500 € are one currency
            raw, currency, unit, unit_text = f"{raw} {unit}", ISO_CURRENCY_SYMBOL[unit], "", ""
        if percent_word:
            raw = text[match.start():percent_word.end()].strip()
        items.append((match.start(), match.end(), Number(raw, value, decimals, percent, currency, relies, identifier_like, unit, unit_text)))
    items = sorted(items + _word_numbers(text, language, taken + word_spans), key=lambda item: item[0])
    return [number for _, _, number in _merge_multipliers(items, text, language)]


def _units_compatible(source: Number, target: Number) -> bool:
    return source.unit == target.unit or not source.unit or not target.unit


def _is_conversion(source: Number, target: Number) -> bool:
    if not source.unit or not target.unit or source.unit == target.unit:
        return False
    first, second = source.base_value(), target.base_value()
    return first is not None and first == second and (source.percent, source.currency) == (target.percent, target.currency)


def _is_approximate_conversion(source: Number, target: Number) -> bool:
    """A conversion that matches once rounded to the digits the rounder side shows (0.7.0)."""
    if not source.unit or not target.unit or source.unit == target.unit or source.value is None or target.value is None:
        return False
    if UNITS[source.unit][0] != UNITS[target.unit][0] or (source.percent, source.currency) != (target.percent, target.currency):
        return False
    for given, shown in ((source, target), (target, source)):
        assert given.value is not None and shown.value is not None
        converted = _from_base(_to_base(given.value, given.unit), shown.unit)
        if converted.quantize(Decimal(1).scaleb(-shown.decimals), rounding=ROUND_HALF_UP) == shown.value:
            return True
    return False


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


_GAP = 100  # cost of an unpaired item; any pairing class costs less (its rank)


def _align[T: (Number, DateMention, "Code")](first: list[T], second: list[T], tests: list[Callable[[T, T], bool]]) -> tuple[dict[int, tuple[int, int]], list[tuple[int, int]]]:
    """Order-preserving alignment (0.5.0). Returns pairs {i: (j, class rank)} and substitutions.

    A pair costs its class rank, a substitution or an unpaired item costs _GAP, so
    a changed item is paired with the item in the same position rather than with
    an identical item elsewhere. Ties prefer pairing, then substitution, then deletion.
    """
    def rank(i: int, j: int) -> int | None:
        return next((r for r, test in enumerate(tests) if test(first[i], second[j])), None)

    start = 0
    while start < min(len(first), len(second)) and rank(start, start) == 0:
        start += 1
    end = 0
    while end < min(len(first), len(second)) - start and rank(len(first) - 1 - end, len(second) - 1 - end) == 0:
        end += 1
    if start or end:  # identical runs at both ends are paired directly; only the middle is aligned
        inner_first, inner_second = first[start:len(first) - end], second[start:len(second) - end]
        inner_pairs, inner_substitutions = _align(inner_first, inner_second, tests) if inner_first or inner_second else ({}, [])
        joined = {k: (k, 0) for k in range(start)}
        joined |= {start + i: (start + j, r) for i, (j, r) in inner_pairs.items()}
        joined |= {len(first) - 1 - k: (len(second) - 1 - k, 0) for k in range(end)}
        return joined, [(start + i, start + j) for i, j in inner_substitutions]
    n, m = len(first), len(second)
    cost = [[0] * (m + 1) for _ in range(n + 1)]
    move = [[""] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        cost[i][0], move[i][0] = i * _GAP, "d"
    for j in range(1, m + 1):
        cost[0][j], move[0][j] = j * _GAP, "i"
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            r = rank(i - 1, j - 1)
            options = [] if r is None else [(cost[i - 1][j - 1] + r, "p")]
            options += [(cost[i - 1][j - 1] + _GAP, "s"), (cost[i - 1][j] + _GAP, "d"), (cost[i][j - 1] + _GAP, "i")]
            cost[i][j], move[i][j] = min(options, key=lambda option: option[0])
    pairs: dict[int, tuple[int, int]] = {}
    substitutions: list[tuple[int, int]] = []
    i, j = n, m
    while i or j:
        step = move[i][j]
        if step == "p":
            pairs[i - 1] = (j - 1, rank(i - 1, j - 1) or 0)
        elif step == "s":
            substitutions.append((i - 1, j - 1))
        i, j = (i - 1, j - 1) if step in "ps" else (i - 1, j) if step == "d" else (i, j - 1)
    return pairs, substitutions[::-1]


def _match[T: (Number, DateMention, "Code")](first: list[T], second: list[T], tests: list[Callable[[T, T], bool]]) -> tuple[dict[int, tuple[int, int]], list[tuple[int, int]], bool]:
    """Align, then pair leftovers that moved. Returns pairs, substitutions left, and order kept."""
    pairs, substitutions = _align(first, second, tests)
    taken = {j for j, _ in pairs.values()}
    left_first = [i for i in range(len(first)) if i not in pairs]
    left_second = [j for j in range(len(second)) if j not in taken]
    moved = False
    for r, test in enumerate(tests):  # moved items: same value, another position
        for i in left_first:
            if i in pairs:
                continue
            j = next((j for j in left_second if j not in taken and test(first[i], second[j])), None)
            if j is not None:
                pairs[i] = (j, r)
                taken.add(j)
                moved = True
    remaining = [(i, j) for i, j in substitutions if i not in pairs and j not in taken]
    return pairs, remaining, not moved


def _label(item: Any) -> str:
    unit = getattr(item, "unit_text", "") or getattr(item, "unit", "")
    return f"{item.raw} {unit}" if unit else str(item.raw)


def _equal_entry(first: list[Any], second: list[Any], i: int, j: int) -> dict[str, Any]:
    return {"original": _label(first[i]), "candidate": _label(second[j]), "relies_on_language_convention": first[i].relies_on_convention or second[j].relies_on_convention}


def compare(first: list[Number], second: list[Number]) -> dict[str, Any]:
    """Pair numbers by class (exact, equivalent, unit conversion, rounding); the rest changed."""
    labels = ("exact", "exact", "equivalent", "unit_conversion", "approximate_conversion", "rounding")
    pairs, substitutions, in_order = _match(first, second, [_same_text_and_unit, _same_text, _same_kind, _is_conversion, _is_approximate_conversion, _is_rounding])
    used = {i: j for i, (j, _) in pairs.items()}
    out: dict[str, Any] = {label: [] for label in labels}
    for i in sorted(pairs):
        j, r = pairs[i]
        out[labels[r]].append(first[i].raw if labels[r] == "exact" else _equal_entry(first, second, i, j))
    free = [j for j in range(len(second)) if j not in used.values()]
    out["removed"] = [_label(n) for i, n in enumerate(first) if i not in used]
    out["added"] = [_label(second[j]) for j in free]
    out["changed"] = [{"original": _label(first[i]), "candidate": _label(second[j])} for i, j in substitutions]
    out["identifier_like_changes"] = sum(n.identifier_like for i, n in enumerate(first) if i not in used) + sum(second[j].identifier_like for j in free)
    out["unit_uncertain"] = [
        {"original": f"{first[i].raw} {first[i].unit}".strip(), "candidate": f"{second[j].raw} {second[j].unit}".strip()}
        for i, j in sorted(used.items())
        if first[i].unit != second[j].unit and not (first[i].unit and second[j].unit)
    ]
    out["pairs_in_order"] = in_order
    return out


def compare_dates(first: list[DateMention], second: list[DateMention]) -> dict[str, Any]:
    """Pair dates: same text, then same date in another form; the rest changed."""
    pairs, substitutions, in_order = _match(first, second, [lambda a, b: a.raw == b.raw, lambda a, b: bool(a.readings & b.readings)])
    taken = {j for j, _ in pairs.values()}
    return {
        "exact": [first[i].raw for i in sorted(pairs) if pairs[i][1] == 0],
        "equivalent": [_equal_entry(first, second, i, pairs[i][0]) for i in sorted(pairs) if pairs[i][1] == 1],
        "removed": [d.raw for i, d in enumerate(first) if i not in pairs],
        "added": [second[j].raw for j in range(len(second)) if j not in taken],
        "changed": [{"original": first[i].raw, "candidate": second[j].raw} for i, j in substitutions],
        "in_order": in_order,
    }


@dataclass(frozen=True)
class Code:
    raw: str
    relies_on_convention: bool = False


def compare_codes(first_raw: list[str], second_raw: list[str]) -> dict[str, Any]:
    """Pair codes by identical text only; the rest changed."""
    first, second = [Code(raw) for raw in first_raw], [Code(raw) for raw in second_raw]
    pairs, substitutions, in_order = _match(first, second, [lambda a, b: a.raw == b.raw])
    taken = {j for j, _ in pairs.values()}
    return {
        "exact": [first[i].raw for i in sorted(pairs)],
        "removed": [c.raw for i, c in enumerate(first) if i not in pairs],
        "added": [second[j].raw for j in range(len(second)) if j not in taken],
        "changed": [{"original": first[i].raw, "candidate": second[j].raw} for i, j in substitutions],
        "in_order": in_order,
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
    codes = compare_codes([raw for _, _, raw in find_codes(original)], [raw for _, _, raw in find_codes(candidate)])
    codes_in_order = bool(codes.pop("in_order"))
    comparison["codes"] = codes
    changed = bool(comparison["removed"] or comparison["added"] or dates["removed"] or dates["added"] or codes["removed"] or codes["added"])
    rounding_fails = bool(comparison["rounding"]) and not permit_rounding
    convention = any(e["relies_on_language_convention"] for e in comparison["equivalent"] + comparison["unit_conversion"] + comparison["rounding"] + dates["equivalent"])
    order_kept = bool(comparison.pop("pairs_in_order")) and dates_in_order and codes_in_order
    if changed or rounding_fails:
        outcome, severity = "FAIL", "CRITICAL"
    else:
        approximate = bool(comparison["approximate_conversion"])
        outcome, severity = ("partially measured" if convention or approximate or not order_kept or comparison["unit_uncertain"] else "PASS"), None
    return base | {
        "outcome": outcome, "severity": severity, "comparison": comparison,
        "order_preserved": order_kept, "relies_on_language_convention": convention,
        "decimal_convention": "point" if language in DECIMAL_POINT else "comma",
        "counts": {"original": len(first), "candidate": len(second), "original_dates": len(first_dates), "candidate_dates": len(second_dates), "original_codes": len(codes["exact"]) + len(codes["removed"]), "candidate_codes": len(codes["exact"]) + len(codes["added"])},
    }
