import json
import random
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from text_integrity import measure_minimality as m


def reference(a, b):
    row = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        new = [i]
        for j, y in enumerate(b, 1):
            new.append(min(row[j] + 1, new[j - 1] + 1, row[j - 1] + (x != y)))
        row = new
    return row[-1]


class Distance(unittest.TestCase):
    def test_known(self):
        self.assertEqual(m.character_edit_distance("kitten", "sitting"), 3)
        self.assertEqual(m.character_edit_distance("", "abc"), 3)
        self.assertEqual(m.character_edit_distance("abc", "abc"), 0)

    def test_matches_reference_on_random_strings(self):
        rng = random.Random(1234)
        for _ in range(500):
            a = "".join(rng.choice("abcé語") for _ in range(rng.randint(0, 80)))
            b = "".join(rng.choice("abcé語") for _ in range(rng.randint(0, 80)))
            self.assertEqual(m.character_edit_distance(a, b), reference(a, b), (a, b))

    def test_no_unicode_normalization(self):
        self.assertEqual(m.character_edit_distance("é", "é"), 2)

    def test_long_input_is_fast_enough(self):
        self.assertEqual(m.character_edit_distance("a" * 20000, "a" * 19999 + "b"), 1)


class Tokens(unittest.TestCase):
    def test_counts(self):
        ops = m.token_operations(["a", "b", "c", "d"], ["a", "x", "c", "d", "e"])
        self.assertEqual(ops, {"distance": 2, "insertions": 1, "deletions": 0, "substitutions": 1})

    def test_distance_matches_reference(self):
        rng = random.Random(99)
        for _ in range(300):
            a = [rng.choice("abcd") for _ in range(rng.randint(0, 30))]
            b = [rng.choice("abcd") for _ in range(rng.randint(0, 30))]
            ops = m.token_operations(a, b)
            self.assertEqual(ops["distance"], reference(a, b))
            self.assertEqual(ops["distance"], ops["insertions"] + ops["deletions"] + ops["substitutions"])


class Measure(unittest.TestCase):
    def test_ratios(self):
        metrics = m.measure("one two three four", "one 2 three four five", language="en")["metrics"]
        self.assertEqual(metrics["token_edit_distance"]["value"], 2)
        self.assertEqual(metrics["changed_token_ratio"]["value"], 0.5)
        self.assertEqual(metrics["inserted_token_ratio"]["value"], 0.25)
        self.assertEqual(metrics["lexical_substitution_rate"]["value"], 0.25)

    def test_no_pass_fail_and_no_combined_score(self):
        result = m.measure("a", "a", language="en")
        self.assertEqual(result["outcome"], "partially measured")
        self.assertNotIn("score", result)
        json.dumps(result)

    def test_unmeasured_are_explicit(self):
        metrics = m.measure("a", "b", language="en")["metrics"]
        self.assertEqual(metrics["changed_sentence_ratio"]["state"], "not measurable")
        self.assertEqual(metrics["semantic_deviation"]["state"], "not measurable")

    def test_japanese_tokens_not_measurable_but_characters_are(self):
        metrics = m.measure("本文です", "本文だ", language="ja")["metrics"]
        self.assertEqual(metrics["character_edit_distance"]["state"], "measured")
        self.assertEqual(metrics["token_edit_distance"]["state"], "not measurable")

    def test_empty_original_ratio_not_applicable(self):
        metrics = m.measure("", "new", language="en")["metrics"]
        self.assertEqual(metrics["changed_token_ratio"]["state"], "not applicable")
        self.assertEqual(metrics["token_edit_distance"]["value"], 1)

    def test_structural_rate(self):
        metric = m.measure("# A\n\ntext", "## A\n\ntext", language="it")["metrics"]["structural_change_rate"]
        self.assertEqual(metric["changed_elements"], ["headings"])

    def test_structural_unsupported_format_stays_explicit(self):
        metric = m.measure("a", "a", language="en", input_format="html")["metrics"]["structural_change_rate"]
        self.assertEqual(metric["state"], "unsupported")

    def test_unsupported_language_and_limit(self):
        self.assertEqual(m.measure("a", "a", language="xx")["outcome"], "unsupported")
        self.assertEqual(m.measure("abc", "abc", language="en", max_chars=1)["outcome"], "not measurable")

    def test_type_error(self):
        with self.assertRaises(TypeError):
            m.measure(None, "a", language="en")


if __name__ == "__main__":
    unittest.main()
