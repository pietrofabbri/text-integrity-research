import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import verify_docs as v

LOG = "# Initial Decisions\n\n## DEC-001 — A\n\n### Status\n\nACCEPTED\n\n"


def repo(tmp, log=LOG, questions="## Q-001 — A\n", doc=None):
    root = Path(tmp)
    for d in ("docs/00-project", "docs/03-scientific-specification", "docs/08-development"):
        (root / d).mkdir(parents=True)
    (root / "docs/00-project/DECISION-LOG.md").write_text(log, encoding="utf-8")
    (root / "docs/00-project/OPEN-QUESTIONS.md").write_text(questions, encoding="utf-8")
    (root / "docs/00-project/RESEARCH-REGISTRY.md").write_text("## R-0001 — A\n", encoding="utf-8")
    (root / "docs/03-scientific-specification/S02.md").write_text("REQ-SEC-001\n", encoding="utf-8")
    if doc:
        (root / "docs/08-development/X.md").write_text(doc, encoding="utf-8")
    return root


def protocol(parent="§2–3", table="§2–3", extra=""):
    return f"**Parent:** `MAP` {parent}\n{extra}\n# Coverage of the Parent Sections\n| A | B |\n|---|---|\n| {table} | §1 |\n"


class Tests(unittest.TestCase):
    def blocking(self, root):
        return [f for f in v.audit(root) if f.severity == "BLOCKING"]

    def test_expand(self):
        self.assertEqual(v.expand("§2–4, §9"), [2, 3, 4, 9])

    def test_clean_repository_passes(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertEqual(v.audit(repo(t, doc=protocol())), [])

    def test_missing_decision_number(self):
        with tempfile.TemporaryDirectory() as t:
            log = LOG + LOG.split("\n\n", 1)[1].replace("001", "003")
            self.assertTrue(any("missing 002" in f.message for f in self.blocking(repo(t, log=log))))

    def test_invalid_status(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertTrue(self.blocking(repo(t, log=LOG.replace("ACCEPTED", "MAYBE"))))

    def test_uncovered_section(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertTrue(self.blocking(repo(t, doc=protocol(table="§2"))))

    def test_doubly_covered_section(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertTrue(self.blocking(repo(t, doc=protocol(parent="§2", table="§2, §2"))))

    def test_unknown_research_id(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertTrue(self.blocking(repo(t, doc=protocol(extra="R-9999"))))

    def test_unknown_requirement(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertTrue(self.blocking(repo(t, doc=protocol(extra="REQ-SEC-999"))))

    def test_missing_file_blocks_only_protocols(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertTrue(self.blocking(repo(t, doc=protocol(extra="`NOPE.md`"))))
        with tempfile.TemporaryDirectory() as t:
            found = v.audit(repo(t, doc="`NOPE.md`"))
            self.assertEqual([f.severity for f in found], ["WARNING"])

    def test_secret_detected(self):
        with tempfile.TemporaryDirectory() as t:
            root = repo(t, doc="ghp_" + "a" * 36)
            self.assertTrue(any(f.check == "secrets" for f in self.blocking(root)))


if __name__ == "__main__":
    unittest.main()
