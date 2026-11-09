"""CAP-VALIDATE-FACTUAL-STRUCTURED-NUMERIC: compare digit-written numbers.

Specification: docs/05-validation/NUMERIC-INTEGRITY-CAPABILITY.md
Status: EXPERIMENTAL. Compares numbers written with digits, classifying each
pair as exact, equivalent, rounding or changed (VALIDATION-MAP.md §16).
It does not read numbers written as words, units, dates or what a number
refers to. Inputs are never normalized (DEC-059).
"""
from __future__ import annotations

import re
import unicodedata
from collections.abc import Callable
from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal
from typing import Any

CAPABILITY_ID = "CAP-VALIDATE-FACTUAL-STRUCTURED-NUMERIC"
CAPABILITY_VERSION = "0.2.0"
FAMILY = "VALIDATE-FACTUAL-STRUCTURED"
DECIMAL_POINT = frozenset({"en", "ja", "zh"})
DECIMAL_COMMA = frozenset({"de", "es", "fr", "id", "it", "nl", "pl", "pt", "ru", "tr"})
TARGET_LANGUAGES = DECIMAL_POINT | DECIMAL_COMMA
NOT_MEASURED = ("numbers_as_words", "unit_words", "date_and_time_meaning", "what_each_number_refers_to", "ranges_and_comparisons")
SPACE_GROUP = "  "

_NUMBER = re.compile(
    r"(?P<currency>[$€£¥]\s?)?"
    r"(?P<sign>(?<![^\W_])(?<![)])[-−])?"
    r"(?<![^\W_])(?P<body>\d+(?:[.,  ]\d+)*)"
    r"(?P<percent>[   ]?[%％])?"
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
_UNIT = re.compile(r"[ \u00a0\u202f]?(" + "|".join(sorted(map(re.escape, UNITS), key=len, reverse=True)) + r")(?![^\W_])")
_LIST_MARKER_AFTER = re.compile(r"[.)]\s")
_LETTER_HYPHEN = re.compile(r"[^\W\d_]-$")
_HYPHEN_LETTER = re.compile(r"-[^\W\d_]")


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
    """Extract digit-written numbers in textual order."""
    decimal = "." if language in DECIMAL_POINT else ","
    numbers = []
    for match in _NUMBER.finditer(text):
        line_start = text.rfind("\n", 0, match.start()) + 1
        if (
            not text[line_start:match.start()].strip()
            and not match["currency"] and not match["sign"] and not match["percent"]
            and len(match["body"]) <= 3 and match["body"].isdigit()
            and _LIST_MARKER_AFTER.match(text, match.end())
        ):
            continue
        value, decimals, relies = _parse(match["body"], decimal)
        if value is not None and match["sign"]:
            value = -value
        before, after = text[max(0, match.start() - 2):match.start()], text[match.end():match.end() + 2]
        identifier_like = bool(_LETTER_HYPHEN.search(before) or _HYPHEN_LETTER.match(after))
        unit_match = None if match["percent"] else _UNIT.match(text, match.end())
        unit = unit_match.group(1) if unit_match else ""
        numbers.append(Number(match.group(0).strip(), value, decimals, bool(match["percent"]), (match["currency"] or "").strip(), relies, identifier_like, unit))
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


def _pair(first: list[Number], second: list[Number], free: set[int], used: dict[int, int], test: Callable[[Number, Number], bool]) -> list[tuple[int, int]]:
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
    changed = bool(comparison["removed"] or comparison["added"])
    rounding_fails = bool(comparison["rounding"]) and not permit_rounding
    convention = any(e["relies_on_language_convention"] for e in comparison["equivalent"] + comparison["unit_conversion"] + comparison["rounding"])
    order_kept = bool(comparison.pop("pairs_in_order"))
    if changed or rounding_fails:
        outcome, severity = "FAIL", "CRITICAL"
    else:
        outcome, severity = ("partially measured" if convention or not order_kept or comparison["unit_uncertain"] else "PASS"), None
    return base | {
        "outcome": outcome, "severity": severity, "comparison": comparison,
        "order_preserved": order_kept, "relies_on_language_convention": convention,
        "decimal_convention": "point" if language in DECIMAL_POINT else "comma",
        "counts": {"original": len(first), "candidate": len(second)},
    }
