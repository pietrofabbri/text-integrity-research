import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from text_integrity import validate_structural as v

DOC = """# Title

First paragraph with `code` and a [link](http://a.example).

- one
  - nested
- two

1. first

> quoted
> more

| a | b |
|---|---|
| 1 | 2 |

```python
x = 1
```

$$
E = mc^2
$$

Note[^1].

[^1]: A footnote.

Setext
------
"""


def run(a, b, **k):
    k.setdefault("language", "en")
    k.setdefault("constraint_type", "HARD")
    return v.validate(a, b, **k)


class Profile(unittest.TestCase):
    def test_elements(self):
        p = v.profile_markdown(DOC)
        self.assertEqual(p.headings, [1, 2])
        self.assertEqual(p.lists, [[[0, False], [1, False], [0, False]], [[0, True]]])
        self.assertEqual(p.tables, [[2, 2]])
        self.assertEqual(p.block_quotes, [2])
        self.assertEqual(len(p.code_blocks), 1)
        self.assertEqual(len(p.block_formulas), 1)
        self.assertEqual(p.inline_code, ["code"])
        self.assertEqual(p.links, ["http://a.example"])
        self.assertEqual(p.footnotes, ["ref:1", "def:1"])
        self.assertEqual(p.paragraphs, 2)

    def test_syntax_inside_code_is_ignored(self):
        p = v.profile_markdown("```\n# not a heading\n- not a list\n```\n")
        self.assertEqual((p.headings, p.lists), ([], []))

    def test_unclosed_fence_terminates(self):
        self.assertEqual(len(v.profile_markdown("```\ncode").code_blocks), 1)

    def test_format_characters_counted(self):
        self.assertEqual(v.profile_markdown("a\u200bb").format_characters, 1)

    def test_line_endings_equivalent(self):
        self.assertEqual(run("a\r\n\r\nb", "a\n\nb")["outcome"], "PASS")


class Validate(unittest.TestCase):
    def test_reworded_text_passes(self):
        changed = DOC.replace("First paragraph", "Opening paragraph").replace("quoted", "cited")
        self.assertEqual(run(DOC, changed)["outcome"], "PASS")

    def test_each_structural_change_fails(self):
        cases = {
            "headings": DOC.replace("# Title", "## Title"),
            "lists": DOC.replace("- two\n", ""),
            "tables": DOC.replace("| 1 | 2 |\n", ""),
            "block_quotes": DOC.replace("> more\n", ""),
            "code_blocks": DOC.replace("x = 1", "x = 2"),
            "inline_code": DOC.replace("`code`", "`other`"),
            "links": DOC.replace("http://a.example", "http://b.example"),
            "footnotes": DOC.replace("[^1]: A footnote.\n", ""),
            "block_formulas": DOC.replace("mc^2", "mc^3"),
        }
        for element, changed in cases.items():
            with self.subTest(element):
                result = run(DOC, changed)
                self.assertEqual(result["outcome"], "FAIL")
                self.assertIn(element, result["differences"])

    def test_reordering_fails(self):
        result = run("# A\n\ntext\n", "text\n\n# A\n")
        self.assertIn("block_order", result["differences"])

    def test_permitted_change_stays_visible(self):
        result = run("a\n\nb", "a b", permitted=frozenset({"paragraphs", "block_order"}))
        self.assertEqual(result["outcome"], "PASS")
        self.assertIn("paragraphs", result["permitted_differences"])

    def test_constraint_type_required_and_checked(self):
        with self.assertRaises(TypeError):
            v.validate("a", "a", language="en")
        with self.assertRaises(ValueError):
            run("a", "a", constraint_type="MAYBE")

    def test_unknown_permitted_rejected(self):
        with self.assertRaises(ValueError):
            run("a", "a", permitted=frozenset({"nope"}))

    def test_unsupported_states_are_not_pass(self):
        self.assertEqual(run("a", "a", input_format="html")["outcome"], "unsupported")
        self.assertEqual(run("a", "a", language="xx")["outcome"], "unsupported")
        self.assertEqual(run("abc", "abc", max_chars=1)["outcome"], "not measurable")

    def test_result_schema_and_honesty(self):
        result = run(DOC, DOC)
        for key in ("family", "capability_id", "outcome", "constraint_type", "confidence", "evidence_basis", "language"):
            self.assertIn(key, result)
        self.assertIsNone(result["confidence"])
        self.assertEqual(result["lifecycle_status"], "EXPERIMENTAL")
        self.assertIn("homoglyphs", result["not_measured"])
        json.dumps(result)

    def test_inputs_not_normalized(self):
        # composed and decomposed forms of the same letter stay distinct in code
        self.assertEqual(run("`é`", "`é`")["outcome"], "FAIL")

    def test_all_target_languages_on_shared_structure(self):
        samples = {"ja": "# 見出し\n\n本文です。\n", "zh": "# 标题\n\n正文。\n", "ru": "# Заголовок\n\nТекст.\n", "tr": "# Başlık\n\nMetin.\n"}
        for language, text in samples.items():
            with self.subTest(language):
                self.assertEqual(run(text, text, language=language)["outcome"], "PASS")

    def test_large_input_is_linear_enough(self):
        text = ("word [x](y) `z` | a\n\n" * 20000)
        self.assertEqual(run(text, text)["outcome"], "PASS")


if __name__ == "__main__":
    unittest.main()
