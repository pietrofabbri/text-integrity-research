"""CAP-VALIDATE-STRUCTURAL-MARKDOWN: compare the structure of two Markdown texts.

Specification: docs/05-validation/VALIDATE-STRUCTURAL-CAPABILITY.md
Status: EXPERIMENTAL. A PASS is a deterministic observation under declared
conditions (FID-090). It says nothing about meaning, facts or quality.

Inputs are never modified or normalized (DEC-059). No network, file or
subprocess use.
"""
from __future__ import annotations

import hashlib
import re
import unicodedata
from dataclasses import asdict, dataclass, field
from typing import Any

CAPABILITY_ID = "CAP-VALIDATE-STRUCTURAL-MARKDOWN"
CAPABILITY_VERSION = "0.2.0"
FAMILY = "VALIDATE-STRUCTURAL"
TARGET_LANGUAGES = frozenset({"en", "es", "de", "ja", "fr", "pt", "ru", "it", "nl", "pl", "tr", "zh", "id"})
SUPPORTED_FORMATS = frozenset({"markdown", "plaintext"})

MEASURED = (
    "paragraphs", "headings", "lists", "tables", "block_quotes", "code_blocks",
    "inline_code", "links", "footnotes", "block_formulas", "block_order",
)
NOT_MEASURED = ("inline_quotations", "inline_formulas", "emphasis", "whitespace", "punctuation", "capitalization", "homoglyphs")

MEASURED_PLAINTEXT = ("paragraphs", "lines", "title_like_lines", "lists", "block_order")
NOT_MEASURED_PLAINTEXT = (
    "headings", "tables", "block_quotes", "code_blocks", "inline_code", "links", "footnotes", "block_formulas",
) + NOT_MEASURED
_SENTENCE_END = ".!?:;…,。！？、"

_LINE_BREAK = re.compile(r"\r\n|\n|\r")
_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
_ATX = re.compile(r"^ {0,3}(#{1,6})(?:\s|$)")
_SETEXT = re.compile(r"^ {0,3}(=+|-+)\s*$")
_LIST_ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+")
_QUOTE = re.compile(r"^ {0,3}>")
_TABLE_RULE = re.compile(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")
_FOOTNOTE_DEF = re.compile(r"^\[\^([^\]]+)\]:")
_FOOTNOTE_REF = re.compile(r"\[\^([^\]]+)\]")
_LINK = re.compile(r"\[[^\]\n]*\]\(([^)\s]*)")
_INLINE_CODE = re.compile(r"`([^`\n]+)`")


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


@dataclass
class Profile:
    """Raw structural observations of one text."""

    paragraphs: int = 0
    headings: list[int] = field(default_factory=list)
    lists: list[list[Any]] = field(default_factory=list)
    tables: list[list[int]] = field(default_factory=list)
    block_quotes: list[int] = field(default_factory=list)
    code_blocks: list[str] = field(default_factory=list)
    inline_code: list[str] = field(default_factory=list)
    links: list[str] = field(default_factory=list)
    footnotes: list[str] = field(default_factory=list)
    block_formulas: list[str] = field(default_factory=list)
    block_order: list[str] = field(default_factory=list)
    format_characters: int = 0
    lines: int = 0
    title_like_lines: int = 0


def _columns(row: str) -> int:
    return len(row.strip().strip("|").split("|"))


def _scan_inline(profile: Profile, line: str) -> None:
    profile.inline_code += _INLINE_CODE.findall(line)
    without_code = _INLINE_CODE.sub("", line)
    profile.links += _LINK.findall(without_code)
    profile.footnotes += [f"ref:{m}" for m in _FOOTNOTE_REF.findall(without_code)]


def _collect_fence(lines: list[str], i: int, marker: str) -> tuple[str, int]:
    """Return a fenced block's digest source and the index after it."""
    body: list[str] = []
    i += 1
    while i < len(lines):
        match = _FENCE.match(lines[i])
        if match and match.group(1)[0] == marker[0] and len(match.group(1)) >= len(marker) and not lines[i].strip(" `~"):
            return "\n".join(body), i + 1
        body.append(lines[i])
        i += 1
    return "\n".join(body), i


def profile_markdown(text: str) -> Profile:
    """Scan a text line by line. The text itself is not altered."""
    p = Profile(format_characters=sum(unicodedata.category(c) == "Cf" for c in text))
    lines = _LINE_BREAK.split(text)
    i, n = 0, len(lines)
    current_list: list[list[Any]] = []

    def close_list() -> None:
        nonlocal current_list
        if current_list:
            p.lists.append(current_list)
            p.block_order.append("list")
            current_list = []

    while i < n:
        line = lines[i]
        if not line.strip():
            close_list()
            i += 1
            continue
        item = _LIST_ITEM.match(line)
        if item:
            current_list.append([len(item.group(1)) // 2, item.group(2)[0].isdigit()])
            _scan_inline(p, line)
            i += 1
            continue
        close_list()
        fence = _FENCE.match(line)
        if fence:
            body, i = _collect_fence(lines, i, fence.group(1))
            p.code_blocks.append(_digest(body))
            p.block_order.append("code")
        elif line.strip() == "$$":
            j = i + 1
            while j < n and lines[j].strip() != "$$":
                j += 1
            p.block_formulas.append(_digest("\n".join(lines[i + 1:j])))
            p.block_order.append("formula")
            i = j + 1
        elif heading := _ATX.match(line):
            p.headings.append(len(heading.group(1)))
            p.block_order.append("heading")
            _scan_inline(p, line)
            i += 1
        elif _QUOTE.match(line):
            start = i
            while i < n and _QUOTE.match(lines[i]):
                _scan_inline(p, lines[i])
                i += 1
            p.block_quotes.append(i - start)
            p.block_order.append("quote")
        elif "|" in line and i + 1 < n and "-" in lines[i + 1] and _TABLE_RULE.match(lines[i + 1]):
            columns = _columns(line)
            start = i
            i += 2
            while i < n and "|" in lines[i] and lines[i].strip():
                i += 1
            p.tables.append([i - start - 1, columns])
            p.block_order.append("table")
        elif definition := _FOOTNOTE_DEF.match(line):
            p.footnotes.append(f"def:{definition.group(1)}")
            p.block_order.append("footnote")
            _scan_inline(p, line[definition.end():])
            i += 1
        else:
            i = _paragraph(p, lines, i)
    close_list()
    return p


def _paragraph(p: Profile, lines: list[str], i: int) -> int:
    """Consume a paragraph or a setext heading, returning the next index."""
    n = len(lines)
    start = i
    while i < n and lines[i].strip():
        if i > start:
            setext = _SETEXT.match(lines[i])
            if setext:
                p.headings.append(1 if setext.group(1)[0] == "=" else 2)
                p.block_order.append("heading")
                return i + 1
            if _ATX.match(lines[i]) or _FENCE.match(lines[i]) or _QUOTE.match(lines[i]) or _LIST_ITEM.match(lines[i]):
                break
        _scan_inline(p, lines[i])
        i += 1
    p.paragraphs += 1
    p.block_order.append("paragraph")
    return i


def profile_plaintext(text: str) -> Profile:
    """Scan text without markup: blank-line blocks, lines, list markers, title-like lines.

    A title-like line is a line with letters and no final punctuation: a
    declared heuristic, not a detection of real titles.
    """
    p = Profile(format_characters=sum(unicodedata.category(c) == "Cf" for c in text))
    in_block = False
    current_list: list[list[Any]] = []

    def close_list() -> None:
        nonlocal current_list
        if current_list:
            p.lists.append(current_list)
            p.block_order.append("list")
            current_list = []

    for line in _LINE_BREAK.split(text):
        stripped = line.strip()
        if not stripped:
            close_list()
            in_block = False
            continue
        if not in_block:
            p.paragraphs += 1
            in_block = True
        item = _LIST_ITEM.match(line)
        if item:
            current_list.append([len(item.group(1)) // 2, item.group(2)[0].isdigit()])
            continue
        close_list()
        p.lines += 1
        if stripped[-1] not in _SENTENCE_END and any(c.isalpha() for c in stripped):
            p.title_like_lines += 1
            p.block_order.append("title_like")
        else:
            p.block_order.append("line")
    close_list()
    return p


def _missing(state: str, reason: str, language: str, constraint_type: str) -> dict[str, Any]:
    return {
        "family": FAMILY, "capability_id": CAPABILITY_ID, "capability_version": CAPABILITY_VERSION,
        "lifecycle_status": "EXPERIMENTAL", "outcome": state, "constraint_type": constraint_type,
        "confidence": None, "evidence_basis": [], "language": language, "reason": reason,
    }


def validate(
    original: str,
    candidate: str,
    *,
    language: str,
    constraint_type: str,
    input_format: str = "markdown",
    permitted: frozenset[str] = frozenset(),
    max_chars: int | None = None,
) -> dict[str, Any]:
    """Compare structure; return the result schema of VALIDATION-ARCHITECTURE.md §8.

    constraint_type has no default because FID-041 requires it to be declared.
    `permitted` names structural elements the experiment explicitly allows to
    change (FID-016); their differences stay in the result.
    """
    if not isinstance(original, str) or not isinstance(candidate, str):
        raise TypeError("original and candidate must be str")
    if constraint_type not in {"HARD", "SOFT"}:
        raise ValueError("constraint_type must be HARD or SOFT")
    measured = MEASURED_PLAINTEXT if input_format == "plaintext" else MEASURED
    unknown = set(permitted) - set(measured)
    if unknown:
        raise ValueError(f"unknown structural elements: {sorted(unknown)}")
    if input_format not in SUPPORTED_FORMATS:
        return _missing("unsupported", f"input format {input_format!r}", language, constraint_type)
    if language not in TARGET_LANGUAGES:
        return _missing("unsupported", f"language {language!r}", language, constraint_type)
    if max_chars is not None and max(len(original), len(candidate)) > max_chars:
        return _missing("not measurable", "input exceeds max_chars", language, constraint_type)

    profile = profile_plaintext if input_format == "plaintext" else profile_markdown
    before, after = profile(original), profile(candidate)
    first, second = asdict(before), asdict(after)
    differences = [e for e in measured if first[e] != second[e]]
    blocking = [e for e in differences if e not in permitted]
    return {
        "family": FAMILY, "capability_id": CAPABILITY_ID, "capability_version": CAPABILITY_VERSION,
        "lifecycle_status": "EXPERIMENTAL", "outcome": "FAIL" if blocking else "PASS",
        "constraint_type": constraint_type, "confidence": None, "evidence_basis": [],
        "language": language, "input_format": input_format,
        "differences": blocking, "permitted_differences": [e for e in differences if e in permitted],
        "measured": list(measured), "not_measured": list(NOT_MEASURED_PLAINTEXT if input_format == "plaintext" else NOT_MEASURED),
        "observations": {"original": first, "candidate": second},
    }
