#!/usr/bin/env python3
"""Collaudo of the experimental capabilities on this repository's own documents.

Read-only; recorded in docs/05-validation/TRIAL-GIT-HISTORY.md. Not a benchmark:
the texts are English project documentation and the edits are mostly additions.

Usage: python3 tools/trial_on_history.py [repository_root]
"""
from __future__ import annotations

import collections
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
sys.path.insert(0, str(ROOT / "src"))

from text_integrity import measure_minimality as minimality
from text_integrity import validate_numeric as numeric
from text_integrity import validate_structural as structural

FENCE = re.compile(r"^ {0,3}(```|~~~)")
ATX = re.compile(r"^ {0,3}#{1,6}\s")
WORD = re.compile(r"\bshall\b|\bmust\b|\bshould\b")
SWAP = {"shall": "must", "must": "shall", "should": "ought"}


def git(*args: str) -> str:
    done = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, errors="replace", check=True)
    return done.stdout


def struct(a: str, b: str) -> dict:
    return structural.validate(a, b, language="en", constraint_type="HARD")


def num(a: str, b: str) -> dict:
    return numeric.validate(a, b, language="en", constraint_type="HARD")


def history() -> dict:
    commits = git("log", "--format=%H", "--reverse").split()
    outcomes: collections.Counter = collections.Counter()
    slowest, errors, characters, pairs = 0.0, 0, 0, 0
    for commit in commits[1:]:
        for line in git("diff-tree", "--no-commit-id", "--name-status", "-r", f"{commit}^", commit).splitlines():
            status, *paths = line.split("\t")
            if status != "M" or not paths[0].endswith(".md") or "_to_delete" in paths[0]:
                continue
            before, after = git("show", f"{commit}^:{paths[0]}"), git("show", f"{commit}:{paths[0]}")
            pairs += 1
            characters += len(before)
            try:
                outcomes["structural", struct(before, after)["outcome"]] += 1
                outcomes["numeric", num(before, after)["outcome"]] += 1
                start = time.perf_counter()
                outcomes["minimality", minimality.measure(before, after, language="en")["outcome"]] += 1
                slowest = max(slowest, time.perf_counter() - start)
            except (ArithmeticError, LookupError, TypeError, ValueError, RecursionError):
                errors += 1
    return {"pairs": pairs, "characters": characters, "errors": errors, "minimality_slowest_seconds": round(slowest, 1), "outcomes": {f"{k[0]}:{k[1]}": v for k, v in sorted(outcomes.items())}}


def outside_fences(text: str) -> list[str]:
    inside, lines = False, []
    for line in re.split(r"\r\n|\n|\r", text):
        if FENCE.match(line):
            inside = not inside
        elif not inside:
            lines.append(line)
    return lines


def reword(text: str) -> str:
    """Swap modal verbs outside code; structure and numbers must not change."""
    inside, out = False, []
    for line in text.split("\n"):
        if FENCE.match(line):
            inside = not inside
        out.append(line if inside or "`" in line else WORD.sub(lambda m: SWAP[m.group()], line))
    return "\n".join(out)


def metamorphic() -> dict:
    files = [p for p in sorted((ROOT / "docs").rglob("*.md")) if "_to_delete" not in p.parts]
    tally: collections.Counter = collections.Counter()
    problems: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        tally["files"] += 1
        for label, outcome in (("reword_structural", struct(text, reword(text))["outcome"]), ("reword_numeric", num(text, reword(text))["outcome"])):
            tally[f"{label}:{outcome}"] += 1
            if outcome != "PASS":
                problems.append(f"{label} {path.name}")
        expected = sum(bool(ATX.match(line)) for line in outside_fences(text))
        found = len(structural.profile_markdown(text).headings)
        tally["heading_count_" + ("equal" if found == expected else "above_simple_count" if found > expected else "below_simple_count")] += 1
        if found < expected:
            problems.append(f"headings {path.name}: {found} of {expected}")
        outside = set(outside_fences(text))
        lines = text.split("\n")
        target = next((i for i, line in enumerate(lines) if ATX.match(line) and line in outside and lines.count(line) == 1), None)
        if target is not None:
            del lines[target]
            result = struct(text, "\n".join(lines))
            tally[f"delete_heading:{result['outcome']}"] += 1
            if result["outcome"] != "FAIL" or "headings" not in result["differences"]:
                problems.append(f"delete_heading {path.name}")
    return {"tally": dict(sorted(tally.items())), "problems": problems[:25], "problem_count": len(problems)}


if __name__ == "__main__":
    print(json.dumps({"history": history(), "metamorphic": metamorphic()}, ensure_ascii=False, indent=1))
