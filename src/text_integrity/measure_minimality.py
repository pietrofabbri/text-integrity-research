"""CAP-VALIDATE-MINIMALITY-LEXICAL: measure how much a candidate text changed.

Specification: docs/05-validation/MINIMALITY-MEASUREMENT-CAPABILITY.md
Status: EXPERIMENTAL. Reports measurements side by side, with no combined
score and no PASS/FAIL. Fewer changes do not make a text better (FID-057,
TRN-007). Inputs are never normalized (DEC-059).
"""
from __future__ import annotations

import re
from collections import Counter
from typing import Any

from text_integrity import validate_structural as structural

CAPABILITY_ID = "CAP-VALIDATE-MINIMALITY-LEXICAL"
CAPABILITY_VERSION = "0.3.0"
FAMILY = "VALIDATE-MINIMALITY"
TOKENIZER = "whitespace-v1"
SENTENCE_SPLITTER = "punctuation-v1"
_SENTENCE = re.compile(r"(?<=[.!?…])\s+|(?<=[。！？])")
WHITESPACE_DELIMITED = frozenset({"en", "es", "de", "fr", "pt", "ru", "it", "nl", "pl", "tr", "id"})
NOT_SEGMENTED_BY_SPACES = frozenset({"ja", "zh"})
TARGET_LANGUAGES = WHITESPACE_DELIMITED | NOT_SEGMENTED_BY_SPACES


def character_edit_distance(a: str, b: str) -> int:
    """Levenshtein distance over code points (Myers/Hyyro bit-parallel)."""
    if a == b:
        return 0
    if not a or not b:
        return max(len(a), len(b))
    if len(a) < len(b):
        a, b = b, a
    masks: dict[str, int] = {}
    for i, ch in enumerate(b):
        masks[ch] = masks.get(ch, 0) | (1 << i)
    full = (1 << len(b)) - 1
    high = 1 << (len(b) - 1)
    positive, negative, score = full, 0, len(b)
    for ch in a:
        match = masks.get(ch, 0)
        d0 = ((((match & positive) + positive) & full) ^ positive) | match | negative
        hp = negative | (~(d0 | positive) & full)
        hn = positive & d0
        if hp & high:
            score += 1
        elif hn & high:
            score -= 1
        hp = ((hp << 1) | 1) & full
        hn = (hn << 1) & full
        positive = hn | (~(d0 | hp) & full)
        negative = hp & d0
    return score


def token_operations(first: list[str], second: list[str]) -> dict[str, int]:
    """Minimal edit counts over tokens; ties prefer substitution, then deletion."""
    start = 0
    while start < min(len(first), len(second)) and first[start] == second[start]:
        start += 1
    end = 0
    while end < min(len(first), len(second)) - start and first[-1 - end] == second[-1 - end]:
        end += 1
    ids: dict[str, int] = {}
    a = [ids.setdefault(token, len(ids)) for token in first[start: len(first) - end]]
    b = [ids.setdefault(token, len(ids)) for token in second[start: len(second) - end]]
    # Exact banded alignment: widen until the distance fits inside the band. A cell
    # with cost <= band never depends on a cell outside it, so results (tie-breaks
    # included) equal the full table's.
    longest = max(len(a), len(b))
    band = max(abs(len(a) - len(b)), 32)
    while True:
        packed, bits = _aligned(a, b, band)
        cost = packed >> (2 * bits)
        if cost <= band or band >= longest:
            break
        band *= 2
    mask = (1 << bits) - 1
    insertions, deletions = (packed >> bits) & mask, packed & mask
    return {"distance": cost, "insertions": insertions, "deletions": deletions, "substitutions": cost - insertions - deletions}


def _aligned(a: list[int], b: list[int], band: int) -> tuple[int, int]:
    """Edit table restricted to |i - j| <= band. Cells pack cost, insertions, deletions."""
    bits = max(len(a), len(b)).bit_length() + 1
    cost_shift = 2 * bits
    one_substitution, one_deletion, one_insertion = 1 << cost_shift, (1 << cost_shift) | 1, (1 << cost_shift) | (1 << bits)
    unreachable = (len(a) + len(b) + 2) << cost_shift
    row = [unreachable] * (len(b) + 1)
    for j in range(min(len(b), band) + 1):
        row[j] = j * one_insertion
    for i, token in enumerate(a, 1):
        low, high = max(1, i - band), min(len(b), i + band)
        diagonal = row[low - 1]
        row[low - 1] = i * one_deletion if low == 1 else unreachable
        left = row[low - 1]
        for j in range(low, high + 1):
            up = row[j]
            if token == b[j - 1]:
                current = diagonal
            else:  # ties prefer substitution, then deletion
                current = diagonal + one_substitution
                if (up + one_deletion) >> cost_shift < current >> cost_shift:
                    current = up + one_deletion
                if (left + one_insertion) >> cost_shift < current >> cost_shift:
                    current = left + one_insertion
            row[j] = current
            diagonal, left = up, current
    return row[-1], bits


def _state(state: str, reason: str) -> dict[str, str]:
    return {"state": state, "reason": reason}


def _value(value: float) -> dict[str, Any]:
    return {"state": "measured", "value": value}


def _token_metrics(original: str, candidate: str, language: str) -> dict[str, dict[str, Any]]:
    names = ("token_edit_distance", "changed_token_ratio", "inserted_token_ratio", "deleted_token_ratio", "lexical_substitution_rate")
    if language in NOT_SEGMENTED_BY_SPACES:
        return {n: _state("not measurable", f"no tokenizer registered for {language}") for n in names}
    first, second = original.split(), candidate.split()
    ops = token_operations(first, second)
    metrics: dict[str, dict[str, Any]] = {"token_edit_distance": _value(ops["distance"])}
    if not first:
        metrics.update({n: _state("not applicable", "original has no tokens") for n in names[1:]})
        return metrics
    total = len(first)
    metrics["changed_token_ratio"] = _value(ops["distance"] / total)
    metrics["inserted_token_ratio"] = _value(ops["insertions"] / total)
    metrics["deleted_token_ratio"] = _value(ops["deletions"] / total)
    metrics["lexical_substitution_rate"] = _value(ops["substitutions"] / total)
    return metrics


def split_sentences(text: str) -> list[str]:
    """Split on final punctuation. A declared simplification: abbreviations split too."""
    return [part.strip() for part in _SENTENCE.split(text) if part.strip()]


def _sentence_metric(original: str, candidate: str) -> dict[str, Any]:
    first = split_sentences(original)
    if not first:
        return _state("not applicable", "original has no sentences")
    unchanged = sum((Counter(first) & Counter(split_sentences(candidate))).values())
    return {"state": "measured", "value": (len(first) - unchanged) / len(first), "splitter": SENTENCE_SPLITTER}


def _structural_metric(original: str, candidate: str, language: str, input_format: str) -> dict[str, Any]:
    result = structural.validate(original, candidate, language=language, constraint_type="SOFT", input_format=input_format)
    if result["outcome"] not in {"PASS", "FAIL"}:
        return _state(str(result["outcome"]), str(result.get("reason", "")))
    changed = len(result["differences"])
    return {"state": "measured", "value": changed / len(result["measured"]), "changed_elements": result["differences"]}


def measure(original: str, candidate: str, *, language: str, input_format: str = "markdown", max_chars: int | None = None) -> dict[str, Any]:
    """Return separately reported minimality measurements."""
    if not isinstance(original, str) or not isinstance(candidate, str):
        raise TypeError("original and candidate must be str")
    base: dict[str, Any] = {
        "family": FAMILY, "capability_id": CAPABILITY_ID, "capability_version": CAPABILITY_VERSION,
        "lifecycle_status": "EXPERIMENTAL", "constraint_type": "SOFT", "confidence": None,
        "evidence_basis": [], "language": language,
    }
    if language not in TARGET_LANGUAGES:
        return base | {"outcome": "unsupported", "reason": f"language {language!r}"}
    if max_chars is not None and max(len(original), len(candidate)) > max_chars:
        return base | {"outcome": "not measurable", "reason": "input exceeds max_chars"}
    metrics: dict[str, dict[str, Any]] = {
        "character_edit_distance": _value(character_edit_distance(original, candidate)),
        **_token_metrics(original, candidate, language),
        "changed_sentence_ratio": _sentence_metric(original, candidate),
        "structural_change_rate": _structural_metric(original, candidate, language, input_format),
        "semantic_deviation": _state("not measurable", "requires a semantic validator; none exists"),
    }
    return base | {
        "outcome": "partially measured", "tokenizer": TOKENIZER,
        "lengths": {"original_chars": len(original), "candidate_chars": len(candidate)},
        "metrics": metrics,
        "interpretation_limit": "Not a quality score. Minimality is subordinate to preservation (FID-057).",
    }
