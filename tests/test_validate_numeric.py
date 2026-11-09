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

    def test_different_units_fail(self):
        result = run("circa 513 kg di rifiuti", "circa 513 g di rifiuti", language="it")
        self.assertEqual(result["outcome"], "FAIL")

    def test_same_unit_passes(self):
        self.assertEqual(run("513 kg", "513kg")["outcome"], "PASS")

    def test_unit_conversion_is_recognised(self):
        result = run("1,5 km", "1500 m", language="it")
        self.assertEqual(len(result["comparison"]["unit_conversion"]), 1)
        self.assertEqual(result["comparison"]["removed"], [])

    def test_wrong_conversion_fails(self):
        self.assertEqual(run("1 km", "100 m")["outcome"], "FAIL")

    def test_different_dimensions_fail(self):
        self.assertEqual(run("1000 g", "1 km")["outcome"], "FAIL")

    def test_unit_lost_is_uncertain_not_pass(self):
        result = run("513 kg", "513 chilogrammi", language="it")
        self.assertEqual(result["outcome"], "partially measured")
        self.assertEqual(len(result["comparison"]["unit_uncertain"]), 1)

    def test_unit_needs_a_boundary(self):
        self.assertEqual(v.extract("5 metri", "it")[0].unit, "")
        self.assertEqual(v.extract("5 gatti", "it")[0].unit, "")

    def test_list_markers_are_not_numbers(self):
        self.assertEqual(values("1. Primo\n2) Secondo\n", "it"), [])

    def test_year_at_line_start_is_a_number(self):
        self.assertEqual(values("2022. Nel corso", "it"), [Decimal(2022)])

    def test_renumbering_does_not_fail(self):
        self.assertEqual(run("1. uno\n2. due\n", "1. uno\n3. due\n")["outcome"], "PASS")

    def test_json_serializable(self):
        json.dumps(run("1.5", "1.50"))

    def test_german_real_case(self):
        self.assertEqual(run("Preis: 1.234,50 EUR", "Es kostet 1.234,50 EUR", language="de")["outcome"], "PASS")

    def test_digit_block_performance(self):
        text = "12.34 " * 3000
        self.assertEqual(run(text, text)["outcome"], "PASS")


class Dates(unittest.TestCase):
    def outcome(self, a, b, language):
        return run(a, b, language=language)["outcome"]

    def test_month_name_change_fails(self):
        for language, a, b in (
            ("it", "Il 15 marzo 2024", "Il 15 aprile 2024"),
            ("en", "On March 15, 2024", "On April 15, 2024"),
            ("de", "Am 15. März 2024", "Am 15. April 2024"),
            ("ru", "1 марта 2024 года", "1 апреля 2024 года"),
            ("es", "el 5 de mayo de 2021", "el 5 de junio de 2021"),
            ("tr", "15 Ocak 2024", "15 Şubat 2024"),
        ):
            self.assertEqual(self.outcome(a, b, language), "FAIL", language)

    def test_same_date_in_another_form_passes_and_stays_visible(self):
        for language, a, b in (
            ("it", "Il 15/03/2024", "Il 15 marzo 2024"),
            ("en", "On March 15, 2024", "On 15 March 2024"),
            ("de", "am 15. März 2024", "am 15.03.2024"),
            ("es", "el 5 de mayo de 2021", "el 05/05/2021"),
            ("zh", "2024年3月15日", "2024-03-15"),
        ):
            result = run(a, b, language=language)
            self.assertEqual(result["outcome"], "PASS", language)
            self.assertEqual(len(result["comparison"]["dates"]["equivalent"]), 1, language)

    def test_day_month_swap(self):
        self.assertEqual(self.outcome("Il 03/05/2024", "Il 05/03/2024", "it"), "FAIL")
        result = run("On 03/05/2024", "On 05/03/2024", language="en")
        self.assertEqual(result["outcome"], "partially measured")
        self.assertTrue(result["relies_on_language_convention"])

    def test_dropping_month_or_year_fails(self):
        self.assertEqual(self.outcome("Nel marzo 2024", "Nel 2024", "it"), "FAIL")
        self.assertEqual(self.outcome("Il 15 marzo 2024", "Il 15 marzo", "it"), "FAIL")

    def test_date_parts_are_not_numbers(self):
        result = run("Il 15/03/2024 e 513 kg", "Il 15/03/2024 e 513 kg", language="it")
        self.assertEqual(result["counts"]["original"], 1)
        self.assertEqual(result["counts"]["original_dates"], 1)

    def test_not_dates(self):
        self.assertEqual(v.find_dates("You may 5 and march 3", "en"), [])
        self.assertEqual(v.find_dates("31/02/2024", "it"), [])
        self.assertEqual(v.find_dates("v1.2.2024", "it"), [])
        self.assertEqual(v.find_dates("1.2.3", "it"), [])

    def test_reordered_dates_are_only_partially_measured(self):
        a, b = "Dal 1 marzo 2024 al 2 aprile 2024", "Al 2 aprile 2024 dal 1 marzo 2024"
        self.assertEqual(self.outcome(a, b, "it"), "partially measured")


class TextsWithoutSpaces(unittest.TestCase):
    def test_digits_after_cjk_are_numbers(self):
        self.assertEqual(values("共有300人，增加到45.5%。", "zh"), [Decimal(300), Decimal("45.5")])
        self.assertEqual(values("人口は300人です", "ja"), [Decimal(300)])

    def test_change_after_cjk_fails(self):
        self.assertEqual(run("共有300人", "共有310人", language="zh")["outcome"], "FAIL")
        self.assertEqual(run("人口は300人です", "人口は301人です", language="ja")["outcome"], "FAIL")

    def test_latin_letter_still_blocks(self):
        self.assertEqual(values("v2 and H2O"), [])


if __name__ == "__main__":
    unittest.main()
