import json
import sys
import unittest
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from text_integrity import validate_numeric as v


def run(a, b, **k):
    k.setdefault("language", "en")
    k.setdefault("constraint_type", "HARD")
    return v.validate(a, b, **k)


def values(text, language="en"):
    return [n.value for n in v.extract(text, language)]


class Extract(unittest.TestCase):
    def test_conventions(self):
        self.assertEqual(values("1,234.5"), [Decimal("1234.5")])
        self.assertEqual(values("1.234,5", "de"), [Decimal("1234.5")])
        self.assertEqual(values("1,000,000"), [Decimal(1000000)])
        self.assertEqual(values("1.000", "de"), [Decimal(1000)])
        self.assertEqual(values("1.000"), [Decimal("1.000")])

    def test_spaces_as_groups(self):
        self.assertEqual(values("1 000,5", "fr"), [Decimal("1000.5")])

    def test_ambiguity_flag(self):
        self.assertTrue(v.extract("1,000", "en")[0].relies_on_convention)
        self.assertFalse(v.extract("1,000,000", "en")[0].relies_on_convention)
        self.assertFalse(v.extract("0.125", "en")[0].relies_on_convention)

    def test_unparseable_kept_literal(self):
        self.assertEqual(values("1.2.3"), [None])

    def test_not_part_of_identifiers(self):
        self.assertEqual(values("v2 H2O x12"), [])

    def test_range_is_not_negative(self):
        self.assertEqual(values("10-20"), [Decimal(10), Decimal(20)])

    def test_negative(self):
        self.assertEqual(values("was -5 and −3"), [Decimal(-5), Decimal(-3)])

    def test_sentence_end_not_decimal(self):
        self.assertEqual(values("It was 10."), [Decimal(10)])

    def test_fullwidth_and_percent(self):
        number = v.extract("５０％", "ja")[0]
        self.assertEqual(number.value, Decimal(50))
        self.assertTrue(number.percent)


class Validate(unittest.TestCase):
    def test_same_numbers_pass(self):
        self.assertEqual(run("Cost 12.5 and 3", "It cost 12.5, plus 3")["outcome"], "PASS")

    def test_changed_value_fails_critical(self):
        result = run("Cost $1.1218", "Cost $1.1219")
        self.assertEqual((result["outcome"], result["severity"]), ("FAIL", "CRITICAL"))
        self.assertEqual(result["comparison"]["removed"], ["$1.1218"])

    def test_equivalent(self):
        result = run("0.50 of it", "0.5 of it")
        self.assertEqual(result["outcome"], "PASS")
        self.assertEqual(len(result["comparison"]["equivalent"]), 1)

    def test_grouping_depends_on_convention(self):
        result = run("1,000 people", "1000 people")
        self.assertEqual(result["outcome"], "partially measured")
        self.assertTrue(result["relies_on_language_convention"])

    def test_rounding_fails_unless_permitted(self):
        self.assertEqual(run("1.1218", "1.12")["outcome"], "FAIL")
        result = run("1.1218", "1.12", permit_rounding=True)
        self.assertEqual(result["outcome"], "PASS")
        self.assertEqual(len(result["comparison"]["rounding"]), 1)

    def test_wrong_rounding_is_change(self):
        self.assertEqual(run("1.1218", "1.13", permit_rounding=True)["comparison"]["removed"], ["1.1218"])

    def test_percent_and_currency_matter(self):
        self.assertEqual(run("50%", "50")["outcome"], "FAIL")
        self.assertEqual(run("$5", "€5")["outcome"], "FAIL")

    def test_sign_matters(self):
        self.assertEqual(run("is -5", "is 5")["outcome"], "FAIL")

    def test_added_and_removed(self):
        self.assertEqual(run("one 1", "one 1 and 2")["comparison"]["added"], ["2"])
        self.assertEqual(run("1 and 2", "1")["comparison"]["removed"], ["2"])

    def test_swap_is_never_a_clean_pass(self):
        result = run("10 men, 20 women", "20 men, 10 women")
        self.assertEqual(result["outcome"], "partially measured")
        self.assertFalse(result["order_preserved"])

    def test_no_numbers_passes_but_declares_limits(self):
        result = run("three men", "four men")
        self.assertEqual(result["outcome"], "PASS")
        self.assertIn("numbers_as_words", result["not_measured"])

    def test_missing_evidence_states(self):
        self.assertEqual(run("1", "1", language="xx")["outcome"], "unsupported")
        self.assertEqual(run("123", "123", max_chars=1)["outcome"], "not measurable")

    def test_arguments(self):
        with self.assertRaises(ValueError):
            run("1", "1", constraint_type="NO")
        with self.assertRaises(TypeError):
            run(1, "1")

    def test_identifier_like_changes_still_fail_but_are_counted(self):
        result = run("see DEC-041", "see DEC-042")
        self.assertEqual(result["outcome"], "FAIL")
        self.assertEqual(result["comparison"]["identifier_like_changes"], 2)

    def test_hyphenated_quantity_is_not_hidden(self):
        result = run("a 10-year study", "a 20-year study")
        self.assertEqual(result["outcome"], "FAIL")

    def test_json_serializable(self):
        json.dumps(run("1.5", "1.50"))

    def test_german_real_case(self):
        self.assertEqual(run("Preis: 1.234,50 EUR", "Es kostet 1.234,50 EUR", language="de")["outcome"], "PASS")

    def test_digit_block_performance(self):
        text = "12.34 " * 3000
        self.assertEqual(run(text, text)["outcome"], "PASS")


if __name__ == "__main__":
    unittest.main()
