"""CAP-VALIDATE-SEMANTIC-POLARITY: negation and modality in aligned sentences.

Specification: docs/05-validation/POLARITY-MODALITY-CAPABILITY.md
Status: EXPERIMENTAL. A deterministic, rule-based check, not a semantic
validator: it compares closed lists of markers sentence by sentence.

- Negation: the number of negation markers (`non`, `not`, `nicht`, `kein`...).
- Modality: the classes of modal verbs (possibility `può`, `can`; obligation
  `deve`, `must`).
- Order: a closed list of opposite pairs (`prima`/`dopo`, `before`/`after`,
  `aumento`/`diminuzione`, `increase`/`decrease`).

A PASS says only that no listed marker changed in aligned sentences; it is not
a finding that meaning was preserved (FID-090). Inputs are never normalized
(DEC-059).
"""
from __future__ import annotations

import re
from collections import Counter
from difflib import SequenceMatcher
from typing import Any

CAPABILITY_ID = "CAP-VALIDATE-SEMANTIC-POLARITY"
CAPABILITY_VERSION = "0.1.0"
FAMILY = "VALIDATE-SEMANTIC"
NOT_MEASURED = (
    "meaning_in_general", "antonyms_outside_the_list", "negation_by_prefix_or_affix",
    "implicit_negation", "verbs_and_adjectives_of_negative_meaning", "conditional_and_mood",
    "scope_of_negation", "sentences_that_cannot_be_aligned",
)

NEGATION: dict[str, str] = {
    "it": "non|né|nessun|nessuno|nessuna|niente|nulla|mai|senza",
    "en": "not|no|never|none|nor|neither|without|cannot|n't",
    "fr": "ne|n'|pas|aucun|aucune|jamais|rien|sans|ni",
    "de": "nicht|kein|keine|keinen|keinem|keiner|keines|nie|niemals|ohne|weder",
    "es": "no|ni|ningún|ninguna|ninguno|nunca|jamás|sin|nada",
    "pt": "não|nem|nenhum|nenhuma|nunca|jamais|sem|nada",
    "nl": "niet|geen|nooit|zonder|noch",
    "ru": "не|нет|ни|никогда|без",
    "pl": "nie|bez|nigdy|żaden|żadna|żadne",
    "tr": "değil|yok",
    "id": "tidak|bukan|tanpa|belum",
}
POSSIBILITY, OBLIGATION = "possibility", "obligation"
MODALS: dict[str, dict[str, str]] = {
    "it": {POSSIBILITY: "può|possono|potrà|potranno|possa|possano|potere", OBLIGATION: "deve|devono|dovrà|dovranno|debba|debbano|dovere|occorre|bisogna"},
    "en": {POSSIBILITY: "can|may|might|could", OBLIGATION: "must|shall|should|required"},
    "fr": {POSSIBILITY: "peut|peuvent|pourra|pourront|puisse|puissent", OBLIGATION: "doit|doivent|devra|devront|doive|doivent|faut"},
    "de": {POSSIBILITY: "kann|können|darf|dürfen|könnte|könnten", OBLIGATION: "muss|müssen|soll|sollen|müsste|müssten"},
    "es": {POSSIBILITY: "puede|pueden|podrá|podrán|pueda|puedan", OBLIGATION: "debe|deben|deberá|deberán|deba|deban"},
    "pt": {POSSIBILITY: "pode|podem|poderá|poderão|possa|possam", OBLIGATION: "deve|devem|deverá|deverão|deva|devam"},
    "nl": {POSSIBILITY: "kan|kunnen|mag|mogen", OBLIGATION: "moet|moeten|dient|dienen"},
    "ru": {POSSIBILITY: "может|могут|можно", OBLIGATION: "должен|должна|должно|должны|необходимо|нужно"},
    "pl": {POSSIBILITY: "może|mogą|można", OBLIGATION: "musi|muszą|należy|powinien|powinna|powinno|powinni"},
}
# Opposite pairs: each word maps to (pair id, side).
OPPOSITES: dict[str, tuple[tuple[str, str], ...]] = {
    "it": (("prima", "dopo"), ("aumento", "diminuzione"), ("aumenta", "diminuisce"), ("aumentare", "diminuire"), ("incremento", "riduzione"), ("massimo", "minimo")),
    "en": (("before", "after"), ("increase", "decrease"), ("increases", "decreases"), ("increased", "decreased"), ("rise", "fall"), ("maximum", "minimum")),
    "fr": (("avant", "après"), ("augmentation", "diminution"), ("augmenter", "diminuer"), ("hausse", "baisse"), ("maximum", "minimum")),
    "de": (("vor", "nach"), ("erhöhung", "senkung"), ("anstieg", "rückgang"), ("zunahme", "abnahme"), ("maximal", "minimal")),
    "es": (("antes", "después"), ("aumento", "disminución"), ("aumentar", "disminuir"), ("máximo", "mínimo")),
    "pt": (("antes", "depois"), ("aumento", "diminuição"), ("aumentar", "diminuir"), ("máximo", "mínimo")),
    "nl": (("voor", "na"), ("toename", "afname"), ("stijging", "daling"), ("maximaal", "minimaal")),
    "ru": (("до", "после"), ("увеличение", "уменьшение"), ("рост", "снижение"), ("максимальный", "минимальный")),
    "pl": (("przed", "po"), ("wzrost", "spadek"), ("zwiększenie", "zmniejszenie"), ("maksymalny", "minimalny")),
}
TARGET_LANGUAGES = frozenset(NEGATION)

_TOKEN = re.compile(r"\w+(?:'\w+)?|n't|n'|\S", re.UNICODE)
_SENTENCE = re.compile(r"(?<=[.!?…;:])\s+|\n\s*\n")


def _tokens(sentence: str) -> list[str]:
    return [t.lower() for t in _TOKEN.findall(sentence)]


def split_sentences(text: str) -> list[str]:
    """Split on final punctuation, semicolons, colons and blank lines (polarity-v1)."""
    return [part.strip() for part in _SENTENCE.split(text) if part.strip()]


def markers(sentence: str, language: str) -> dict[str, Any]:
    """Return negation count, modality classes and opposite-pair sides found in one sentence."""
    tokens = _tokens(sentence)
    negation = set(NEGATION[language].split("|"))
    found_negations = [t for t in tokens if t in negation]
    if language in {"en"}:
        found_negations += [t for t in tokens if t.endswith("n't") and t != "n't"]
    modality: Counter[str] = Counter()
    for cls, words in MODALS.get(language, {}).items():
        listed = set(words.split("|"))
        modality[cls] += sum(t in listed for t in tokens)
    sides: Counter[tuple[str, str]] = Counter()
    for pair in OPPOSITES.get(language, ()):
        for side, word in zip(("a", "b"), pair, strict=True):
            sides[(pair[0], side)] += tokens.count(word)
    return {"negations": found_negations, "modality": +modality, "opposites": +sides}


def align_sentences(first: list[str], second: list[str]) -> list[tuple[int, int]]:
    """Order-preserving alignment maximizing token similarity; unrelated sentences stay unpaired."""
    a, b = [_tokens(s) for s in first], [_tokens(s) for s in second]
    n, m = len(a), len(b)
    score = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            similarity = SequenceMatcher(None, a[i], b[j], autojunk=False).ratio()
            pair = score[i + 1][j + 1] + similarity if similarity > 0.5 else -1.0
            score[i][j] = max(pair, score[i + 1][j], score[i][j + 1])
    pairs, i, j = [], 0, 0
    while i < n and j < m:
        similarity = SequenceMatcher(None, a[i], b[j], autojunk=False).ratio()
        if similarity > 0.5 and score[i][j] == score[i + 1][j + 1] + similarity:
            pairs.append((i, j))
            i, j = i + 1, j + 1
        elif score[i][j] == score[i + 1][j]:
            i += 1
        else:
            j += 1
    return pairs


def validate(original: str, candidate: str, *, language: str, constraint_type: str, max_chars: int | None = None) -> dict[str, Any]:
    """Compare negation, modality and listed opposites in aligned sentences."""
    if not isinstance(original, str) or not isinstance(candidate, str):
        raise TypeError("original and candidate must be str")
    if constraint_type not in {"HARD", "SOFT"}:
        raise ValueError("constraint_type must be HARD or SOFT")
    base: dict[str, Any] = {
        "family": FAMILY, "capability_id": CAPABILITY_ID, "capability_version": CAPABILITY_VERSION,
        "lifecycle_status": "EXPERIMENTAL", "constraint_type": constraint_type, "confidence": None,
        "evidence_basis": [], "language": language, "not_measured": list(NOT_MEASURED),
    }
    if language not in TARGET_LANGUAGES:
        return base | {"outcome": "unsupported", "reason": f"language {language!r}"}
    if max_chars is not None and max(len(original), len(candidate)) > max_chars:
        return base | {"outcome": "not measurable", "reason": "input exceeds max_chars"}
    first, second = split_sentences(original), split_sentences(candidate)
    pairs = align_sentences(first, second)
    changes: dict[str, list[dict[str, Any]]] = {"negation": [], "modality": [], "opposites": []}
    for i, j in pairs:
        before, after = markers(first[i], language), markers(second[j], language)
        where = {"original": first[i], "candidate": second[j]}
        if len(before["negations"]) != len(after["negations"]):
            changes["negation"].append(where | {"original_markers": before["negations"], "candidate_markers": after["negations"]})
        if before["modality"] != after["modality"]:
            changes["modality"].append(where | {"original_classes": dict(before["modality"]), "candidate_classes": dict(after["modality"])})
        if before["opposites"] != after["opposites"]:
            changes["opposites"].append(where | {"original_words": sorted(f"{p}:{s}" for p, s in before["opposites"]), "candidate_words": sorted(f"{p}:{s}" for p, s in after["opposites"])})
    unaligned = {"original": len(first) - len(pairs), "candidate": len(second) - len(pairs)}
    if any(changes.values()):
        outcome, severity = "FAIL", "MAJOR"
    else:
        outcome, severity = ("partially measured" if unaligned["original"] or unaligned["candidate"] else "PASS"), None
    return base | {
        "outcome": outcome, "severity": severity, "changes": changes,
        "sentences": {"original": len(first), "candidate": len(second), "aligned": len(pairs), "unaligned": unaligned},
        "interpretation_limit": "Only listed markers are compared. A PASS is not evidence that meaning was preserved.",
    }
