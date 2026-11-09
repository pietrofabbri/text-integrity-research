#!/usr/bin/env python3
"""Repository consistency audit (DEC-058).

Partial implementation of DEVELOPMENT-MAP.md §118, §122 and §159.
Uses the severity levels of §123: PASS, WARNING, BLOCKING.
Standard library only. Reads files; never writes or uses the network.

Usage: python3 tools/verify_docs.py [repository_root]
Exit status: 0 when nothing is BLOCKING, 1 otherwise.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

SECTION_RANGE = re.compile(r"§(\d+)(?:–(\d+))?")
MD_REF = re.compile(r"`(?:[\w./-]*/)?([\w-]+\.md)`")
DECISION_HEADING = re.compile(r"^## DEC-(\d{3}) ", re.MULTILINE)
DECISION_STATUS = re.compile(r"^## DEC-(\d{3}) .*?^### Status\s+(\w+)", re.MULTILINE | re.DOTALL)
QUESTION_HEADING = re.compile(r"^## Q-(\d{3}) ", re.MULTILINE)
ALLOWED_STATUS = {"PROPOSED", "ACCEPTED", "SUPERSEDED", "REJECTED"}
RESEARCH_ID = re.compile(r"\bR-\d{4}\b")
REQUIREMENT_ID = re.compile(r"\bREQ-[A-Z]+-\d{3}\b")
SECRET_PATTERNS = (
    re.compile(r"\bghp_[A-Za-z0-9]{30,}"),
    re.compile(r"\bsk-[A-Za-z0-9-]{30,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
)


@dataclass(frozen=True)
class Finding:
    severity: str
    check: str
    message: str


def expand(text: str) -> list[int]:
    """Return every section number named by a text such as '§2–4, §9'."""
    out: list[int] = []
    for start, end in SECTION_RANGE.findall(text):
        out.extend(range(int(start), int(end or start) + 1))
    return out


def sequence_gaps(numbers: list[int]) -> list[str]:
    """Describe duplicates and holes in a list that should run 1..n."""
    problems = sorted({f"duplicate {n:03d}" for n in numbers if numbers.count(n) > 1})
    if numbers:
        missing = set(range(1, max(numbers) + 1)) - set(numbers)
        problems += [f"missing {n:03d}" for n in sorted(missing)]
    return problems


def check_registers(docs: Path) -> list[Finding]:
    findings: list[Finding] = []
    log = (docs / "00-project/DECISION-LOG.md").read_text(encoding="utf-8")
    body = log.split("# Initial Decisions", 1)[-1]
    for problem in sequence_gaps([int(n) for n in DECISION_HEADING.findall(body)]):
        findings.append(Finding("BLOCKING", "decision-log", problem))
    for number, status in DECISION_STATUS.findall(body):
        if status not in ALLOWED_STATUS:
            findings.append(Finding("BLOCKING", "decision-log", f"DEC-{number}: status {status}"))
    questions = (docs / "00-project/OPEN-QUESTIONS.md").read_text(encoding="utf-8")
    for problem in sequence_gaps([int(n) for n in QUESTION_HEADING.findall(questions)]):
        findings.append(Finding("BLOCKING", "open-questions", problem))
    return findings


def check_coverage(path: Path) -> list[Finding]:
    """A sub-document's coverage table must equal its declared Parent sections."""
    text = path.read_text(encoding="utf-8")
    if "Coverage of the Parent" not in text:
        return []
    parent = re.search(r"^\*\*Parent:\*\*(.*)$", text, re.MULTILINE)
    if parent is None:
        return [Finding("BLOCKING", "coverage", f"{path.name}: no Parent line")]
    declared = expand(parent.group(1))
    covered: list[int] = []
    for line in text.split("Coverage of the Parent", 1)[1].splitlines():
        cells = line.split("|")
        if len(cells) > 2:
            covered.extend(expand(cells[1]))
    findings = []
    if sorted(covered) != sorted(declared):
        difference = sorted(set(declared) ^ set(covered))
        findings.append(Finding("BLOCKING", "coverage", f"{path.name}: differs at {difference}"))
    if len(covered) != len(set(covered)):
        findings.append(Finding("BLOCKING", "coverage", f"{path.name}: section covered twice"))
    return findings


def check_references(docs: Path, files: list[Path]) -> list[Finding]:
    """Report references to absent files and to unregistered identifiers."""
    names = {p.name for p in files}
    corpus = "\n".join(p.read_text(encoding="utf-8") for p in sorted((docs / "03-scientific-specification").glob("*.md")))
    registry = (docs / "00-project/RESEARCH-REGISTRY.md").read_text(encoding="utf-8")
    findings: list[Finding] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        protocol = "Coverage of the Parent" in text
        for name in sorted(set(MD_REF.findall(text)) - names):
            severity = "BLOCKING" if protocol else "WARNING"
            findings.append(Finding(severity, "reference", f"{path.name}: {name} not found"))
        if protocol:
            for rid in sorted(set(RESEARCH_ID.findall(text))):
                if f"## {rid} " not in registry:
                    findings.append(Finding("BLOCKING", "research-id", f"{path.name}: {rid}"))
            for req in sorted(set(REQUIREMENT_ID.findall(text))):
                if req not in corpus:
                    findings.append(Finding("BLOCKING", "requirement-id", f"{path.name}: {req}"))
    return findings


def check_secrets(root: Path) -> list[Finding]:
    """SECURITY-MAP.md §36: credentials must never be committed."""
    findings = []
    for path in root.rglob("*"):
        if ".git" in path.parts or not path.is_file() or path.suffix not in {".md", ".py", ".toml", ".yml", ".yaml", ".json"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if path.name != "test_verify_docs.py" and any(p.search(text) for p in SECRET_PATTERNS):
            findings.append(Finding("BLOCKING", "secrets", str(path.relative_to(root))))
    return findings


def audit(root: Path) -> list[Finding]:
    docs = root / "docs"
    files = sorted(p for p in docs.rglob("*.md") if "_to_delete" not in p.parts)
    findings = check_registers(docs) + check_references(docs, files) + check_secrets(root)
    for path in files:
        findings += check_coverage(path)
    return findings


def main(argv: list[str]) -> int:
    root = Path(argv[1] if len(argv) > 1 else ".").resolve()
    findings = audit(root)
    for finding in findings:
        print(f"{finding.severity:9} {finding.check:16} {finding.message}")
    blocking = sum(f.severity == "BLOCKING" for f in findings)
    warnings = sum(f.severity == "WARNING" for f in findings)
    print(f"RESULT: {'BLOCKING' if blocking else 'WARNING' if warnings else 'PASS'} ({blocking} blocking, {warnings} warnings)")
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
