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

    def test_compound_number_words_pass_but_limit_is_declared(self):
        result = run("twenty-three men", "twenty-four men")
        self.assertEqual(result["outcome"], "PASS")
        self.assertIn("compound_number_words", result["not_measured"])

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
        result = run("513 kg", "513 quintali", language="it")
        self.assertEqual(result["outcome"], "partially measured")
        self.assertEqual(len(result["comparison"]["unit_uncertain"]), 1)

    def test_unit_needs_a_boundary(self):
        self.assertEqual(v.extract("5 metropolitane", "it")[0].unit, "")
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


class CurrencyAfterNumber(unittest.TestCase):
    def outcome(self, a, b, language="it"):
        return run(a, b, language=language)["outcome"]

    def test_changed_symbol_fails(self):
        self.assertEqual(self.outcome("Costa 500 €", "Costa 500 $"), "FAIL")
        self.assertEqual(self.outcome("Costa 1.200,50 €", "Costa 1.200,50 £"), "FAIL")
        self.assertEqual(self.outcome("Coûte 500\u00a0€", "Coûte 500\u00a0$", "fr"), "FAIL")
        self.assertEqual(self.outcome("Costa 500 EUR", "Costa 500 USD"), "FAIL")

    def test_same_currency_in_another_position_passes(self):
        self.assertEqual(self.outcome("€ 1.200,00", "1.200,00 €"), "PASS")
        self.assertEqual(self.outcome("500 EUR", "500 €"), "PASS")
        self.assertEqual(self.outcome("500 €", "500\u00a0€"), "PASS")

    def test_changed_amount_fails(self):
        self.assertEqual(self.outcome("Costa 500 €", "Costa 600 €"), "FAIL")

    def test_next_number_is_not_taken(self):
        self.assertEqual(values("5 € e 300 persone", "it"), [Decimal(5), Decimal(300)])


class AbbreviatedMonths(unittest.TestCase):
    def outcome(self, a, b, language="it"):
        return run(a, b, language=language)["outcome"]

    def test_changed_month_fails(self):
        self.assertEqual(self.outcome("il 15 mar. 2024", "il 15 apr. 2024"), "FAIL")
        self.assertEqual(self.outcome("On Mar 5, 2024", "On Apr 5, 2024", "en"), "FAIL")
        self.assertEqual(self.outcome("am 15. Okt. 2024", "am 15. Nov. 2024", "de"), "FAIL")

    def test_same_date_passes(self):
        self.assertEqual(self.outcome("il 15 mar. 2024", "il 15 marzo 2024"), "PASS")
        self.assertEqual(self.outcome("Sept. 2024", "September 2024", "en"), "PASS")

    def test_read_only_before_a_number(self):
        self.assertEqual(v.find_dates("il 15 mar e il 16 set", "it"), [])
        self.assertEqual(v.find_dates("Dec is here", "en"), [])
        self.assertEqual(v.find_dates("the mar 5", "en"), [])


class CurrencyCodeBeforeNumber(unittest.TestCase):
    def test_same_currency(self):
        for a, b in (("EUR 350", "350 €"), ("EUR 1.200,00", "€ 1.200,00"), ("USD 5", "$5")):
            self.assertEqual(run(a, b, language="it")["outcome"], "PASS", (a, b))

    def test_changed_currency(self):
        self.assertEqual(run("EUR 350", "USD 350", language="it")["outcome"], "FAIL")
        self.assertEqual(run("EUR 350", "350 $", language="it")["outcome"], "FAIL")

    def test_code_inside_a_word_is_not_a_currency(self):
        self.assertEqual(v.extract("XEUR 350", "it")[0].currency, "")


class PositionalPairing(unittest.TestCase):
    """A changed item is paired with the one in its position, not with an identical one elsewhere."""

    def test_changed_date_next_to_rewritten_date(self):
        a = "il 15 marzo 2024 e poi il 2024-03-15"
        b = "il 16 marzo 2024 e poi il 15 marzo 2024"
        dates = run(a, b, language="it")["comparison"]["dates"]
        self.assertEqual(dates["changed"], [{"original": "15 marzo 2024", "candidate": "16 marzo 2024"}])
        self.assertEqual([(e["original"], e["candidate"]) for e in dates["equivalent"]], [("2024-03-15", "15 marzo 2024")])

    def test_changed_number_is_reported_as_a_pair(self):
        result = run("1, 2, 3, 4", "1, 2, 5, 4")
        self.assertEqual(result["comparison"]["changed"], [{"original": "3", "candidate": "5"}])

    def test_swapped_identical_dates_keep_order(self):
        a, b = "On March 5, 2024 and on 5 March 2024", "On 5 March 2024 and on March 5, 2024"
        result = run(a, b)
        self.assertEqual(result["outcome"], "PASS")
        self.assertTrue(result["order_preserved"])

    def test_moved_number_is_paired_and_flagged(self):
        result = run("10 then 20 then 30", "30 then 10 then 20")
        self.assertEqual(result["outcome"], "partially measured")
        self.assertFalse(result["order_preserved"])


if __name__ == "__main__":
    unittest.main()


class NumberWords(unittest.TestCase):
    def outcome(self, a, b, language="it"):
        return run(a, b, language=language)["outcome"]

    def test_changed_word_fails(self):
        self.assertEqual(self.outcome("tre archivisti", "quattro archivisti"), "FAIL")
        self.assertEqual(self.outcome("la metà del materiale", "un terzo del materiale"), "FAIL")
        self.assertEqual(self.outcome("three men", "four men", "en"), "FAIL")
        self.assertEqual(self.outcome("drei Tage", "vier Tage", "de"), "FAIL")

    def test_word_and_digits_are_equivalent(self):
        result = run("tre archivisti", "3 archivisti", language="it")
        self.assertEqual(result["outcome"], "PASS")
        self.assertEqual(result["comparison"]["equivalent"][0]["original"], "tre")

    def test_capitalized_word(self):
        self.assertEqual(self.outcome("Dodici persone", "Tredici persone"), "FAIL")

    def test_words_for_one_are_not_read(self):
        self.assertEqual(values("un libro e una casa", "it"), [])
        self.assertEqual(values("the one I saw", "en"), [])

    def test_multiplier_joins_the_number(self):
        self.assertEqual(values("4,8 milioni di euro", "it"), [Decimal(4800000)])
        self.assertEqual(values("tre milioni", "it"), [Decimal(3000000)])
        self.assertEqual(self.outcome("4,8 milioni", "4.800.000"), "PASS")
        self.assertEqual(self.outcome("120 mila euro", "120.000 euro"), "partially measured")
        self.assertEqual(self.outcome("4,8 milioni", "4,8 miliardi"), "FAIL")

    def test_word_inside_another_word_is_not_read(self):
        self.assertEqual(values("dieciottesimo e treno", "it"), [])
        self.assertEqual(values("dix-sept", "fr"), [Decimal(17)])

    def test_no_words_in_japanese(self):
        self.assertEqual(values("三人", "ja"), [])


class Codes(unittest.TestCase):
    def test_changed_code_fails(self):
        result = run("release v2.3 ready", "release v3.3 ready", language="it")
        self.assertEqual(result["outcome"], "FAIL")
        self.assertEqual(result["comparison"]["codes"]["changed"], [{"original": "v2.3", "candidate": "v3.3"}])

    def test_codes_are_not_numbers(self):
        self.assertEqual(values("v2.3, H2O, formato A4", "it"), [])
        self.assertEqual([c for _, _, c in v.find_codes("v2.3, H2O, formato A4.")], ["v2.3", "H2O", "A4"])

    def test_unit_symbols_and_hyphen_codes_are_not_codes(self):
        self.assertEqual(v.find_codes("80 m2 e DPR-445 e 3D"), [])

    def test_cjk_is_not_a_code(self):
        self.assertEqual(v.find_codes("第3章"), [])
        self.assertEqual(run("第3章", "第4章", language="zh")["outcome"], "FAIL")


class ReportedLabels(unittest.TestCase):
    def test_changed_unit_is_shown(self):
        result = run("peso di 500 kg", "peso di 500 g", language="it")
        self.assertEqual(result["comparison"]["changed"], [{"original": "500 kg", "candidate": "500 g"}])


class UnitWords(unittest.TestCase):
    def test_changed_unit_word_fails(self):
        self.assertEqual(run("a strip of 3 kilometres", "a strip of 3 metres")["outcome"], "FAIL")
        self.assertEqual(run("pesa 5 chilogrammi", "pesa 5 grammi", language="it")["outcome"], "FAIL")

    def test_word_and_symbol_are_the_same_unit(self):
        self.assertEqual(run("3 kilometres", "3 km")["outcome"], "PASS")
        self.assertEqual(run("a 20 gradi Celsius", "a 20 °C", language="it")["outcome"], "PASS")

    def test_word_conversion_is_exact(self):
        self.assertEqual(run("dura 90 minuti", "dura 1,5 ore", language="it")["outcome"], "PASS")

    def test_changed_word_shown_as_written(self):
        result = run("500 grams", "500 kilograms")
        self.assertEqual(result["comparison"]["changed"], [{"original": "500 grams", "candidate": "500 kilograms"}])


class ConversionsBetweenSystems(unittest.TestCase):
    def test_exact_definitions(self):
        self.assertEqual(run("at 50 °F", "at 10 °C")["outcome"], "PASS")
        self.assertEqual(run("1 mile", "1.609344 km")["outcome"], "PASS")

    def test_rounded_conversion_is_partial_and_visible(self):
        for a, b in (("5 miles", "8 km"), ("70 °F", "21 °C"), ("60 mph", "97 km/h"), ("10 lb", "4.5 kg")):
            result = run(a, b)
            self.assertEqual(result["outcome"], "partially measured", (a, b))
            self.assertEqual(len(result["comparison"]["approximate_conversion"]), 1, (a, b))

    def test_wrong_conversion_fails(self):
        self.assertEqual(run("5 miles", "9 km")["outcome"], "FAIL")
        self.assertEqual(run("70 °F", "25 °C")["outcome"], "FAIL")

    def test_mi_alone_is_not_a_unit(self):
        self.assertEqual(v.extract("ne ho 5 mi pare", "it")[0].unit, "")


class PercentWords(unittest.TestCase):
    def test_percent_word_equals_sign(self):
        for language, a, b in (("fr", "reculé de 25 pour cent", "reculé de 25 %"), ("it", "il 12 per cento", "il 12 %"), ("en", "a 5 percent rise", "a 5% rise"), ("de", "um 7 Prozent", "um 7 %")):
            result = run(a, b, language=language)
            self.assertEqual(result["outcome"], "PASS", (language, a, b))

    def test_percent_word_is_not_a_number_word(self):
        self.assertEqual(values("25 pour cent", "fr"), [Decimal(25)])
        self.assertEqual(values("cent euros", "fr"), [Decimal(100)])

    def test_changed_percent_fails(self):
        self.assertEqual(run("il 12 per cento", "il 15 per cento", language="it")["outcome"], "FAIL")

    def test_percent_and_plain_number_differ(self):
        self.assertEqual(run("il 12 per cento", "il 12", language="it")["outcome"], "FAIL")

    def test_currency_code_label_once(self):
        result = run("1.490,00 €", "1.490 EUR", language="it")
        self.assertEqual(result["comparison"]["equivalent"][0]["candidate"], "1.490 EUR")


class InflectedMonths(unittest.TestCase):
    def test_russian_prepositional(self):
        self.assertEqual(run("в марте 2024 года", "в апреле 2024 года", language="ru")["outcome"], "FAIL")
        self.assertEqual(run("в марте 2024 года", "в марте 2024 года", language="ru")["outcome"], "PASS")

    def test_polish_locative(self):
        self.assertEqual(run("w marcu 2024 roku", "w kwietniu 2024 roku", language="pl")["outcome"], "FAIL")
        self.assertEqual(run("w marcu 2024", "marzec 2024", language="pl")["outcome"], "PASS")


class Qualifiers(unittest.TestCase):
    def outcome(self, a, b, language="it"):
        return run(a, b, language=language)["outcome"]

    def test_change_of_class_fails(self):
        for a, b in (("circa 420", "oltre 420"), ("almeno 18", "fino a 18"), ("quasi 85", "più di 85"), ("meno di 12 mila", "più di 12 mila"), ("non più di 30", "almeno 30")):
            self.assertEqual(self.outcome(a, b), "FAIL", (a, b))
        self.assertEqual(self.outcome("at least 5 days", "up to 5 days", "en"), "FAIL")

    def test_change_within_class_passes(self):
        self.assertEqual(self.outcome("fino a 650 giorni", "meno di 650 giorni"), "PASS")
        self.assertEqual(self.outcome("près de 75 %", "environ 75 %", "fr"), "PASS")

    def test_qualifier_on_one_side_is_partial(self):
        result = run("circa 420 persone", "420 persone", language="it")
        self.assertEqual(result["outcome"], "partially measured")
        self.assertEqual(result["comparison"]["qualifier_uncertain"], [{"original": "circa 420", "candidate": "420"}])

    def test_qualifier_must_stand_before_the_number(self):
        self.assertEqual(v.extract("il circa e 420", "it")[0].qualifier, "")
        self.assertEqual(v.extract("persone oltre 420", "it")[0].qualifier, "lower")

    def test_verbs_are_not_read(self):
        self.assertEqual(self.outcome("pourrait atteindre 80 %", "pourrait dépasser 80 %", "fr"), "PASS")
        self.assertIn("verbs_qualifying_a_number", run("1", "1")["not_measured"])


class NumberWordsWithHyphens(unittest.TestCase):
    def test_word_before_hyphen_is_read(self):
        self.assertEqual(values("at six-hour intervals", "en"), [Decimal(6)])
        self.assertEqual(run("every six hours", "at six-hour intervals")["outcome"], "PASS")

    def test_fold(self):
        self.assertEqual(values("a twentyfold rise and a two-fold drop", "en"), [Decimal(20), Decimal(2)])

    def test_compounds_still_not_read(self):
        self.assertEqual(values("twenty-three men", "en"), [])
        self.assertEqual(values("dix-sept", "fr"), [Decimal(17)])

    def test_decade_equals_ten(self):
        self.assertEqual(run("his first decade of fieldwork", "his initial ten-year campaign")["outcome"], "PASS")
        self.assertEqual(values("a multi-decade record", "en"), [])


class ComparativeQualifiers(unittest.TestCase):
    def test_superior_inferior(self):
        for language, a, b in (
            ("es", "en cotas superiores a 1.500 metros", "en cotas inferiores a 1.500 metros"),
            ("fr", "une valeur supérieure à 65 décibels", "une valeur inférieure à 65 décibels"),
            ("pt", "valores superiores a 30", "valores inferiores a 30"),
            ("it", "un valore superiore al 40 %", "un valore inferiore al 40 %"),
            ("en", "greater than 5 units", "lower than 5 units"),
        ):
            self.assertEqual(run(a, b, language=language)["outcome"], "FAIL", (language, a, b))

    def test_same_class_passes(self):
        self.assertEqual(run("más de 30", "superior a 30", language="es")["outcome"], "PASS")
