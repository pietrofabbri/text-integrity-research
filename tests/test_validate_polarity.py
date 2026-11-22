import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from text_integrity import validate_polarity as p


def run(a, b, language="it"):
    return p.validate(a, b, language=language, constraint_type="HARD")


class Negation(unittest.TestCase):
    def test_removed_negation_fails(self):
        for language, a, b in (
            ("it", "Il regolamento non garantisce condizioni adeguate.", "Il regolamento garantisce condizioni adeguate."),
            ("fr", "Le dispositif n'entraîne aucune interruption de la desserte.", "Le dispositif entraîne une interruption de la desserte."),
            ("de", "Es trat keine Versorgungsunterbrechung auf.", "Es trat eine Versorgungsunterbrechung auf."),
            ("en", "The draft does not exceed the limit.", "The draft exceeds the limit."),
            ("en", "The gate doesn't open at night.", "The gate opens at night."),
        ):
            result = run(a, b, language)
            self.assertEqual(result["outcome"], "FAIL", (language, a))
            self.assertEqual(len(result["changes"]["negation"]), 1)

    def test_same_negation_passes(self):
        self.assertEqual(run("Il piano non prevede costi.", "Il programma non prevede spese.")["outcome"], "PASS")


class Modality(unittest.TestCase):
    def test_possibility_to_obligation_fails(self):
        for language, a, b in (
            ("it", "Il transito può essere autorizzato ai residenti.", "Il transito deve essere autorizzato ai residenti."),
            ("es", "Las comunidades pueden programar sus turnos.", "Las comunidades deben programar sus turnos."),
            ("de", "Großabnehmer können ihre Speicher einbinden.", "Großabnehmer müssen ihre Speicher einbinden."),
            ("fr", "Les sous-stations peuvent être raccordées au réseau.", "Les sous-stations doivent être raccordées au réseau."),
        ):
            self.assertEqual(run(a, b, language)["changes"]["modality"] != [], True, (language, a))

    def test_same_class_passes(self):
        self.assertEqual(run("Il comune può presentare due domande.", "Il comune può inoltrare due domande.")["outcome"], "PASS")


class Opposites(unittest.TestCase):
    def test_listed_opposite_fails(self):
        self.assertEqual(run("Si teme un possibile aumento della congestione.", "Si teme un possibile diminuzione della congestione.")["outcome"], "FAIL")

    def test_unlisted_antonym_passes_and_is_declared(self):
        result = run("Le presas absorbieron la crecida, evitando cualquier desbordamiento.", "Le presas absorbieron la crecida, provocando cualquier desbordamiento.", "es")
        self.assertEqual(result["outcome"], "PASS")
        self.assertIn("antonyms_outside_the_list", result["not_measured"])


class Alignment(unittest.TestCase):
    def test_sentences_are_aligned_not_positional(self):
        a = "Prima frase senza importanza. Il sistema non funziona di notte. Ultima frase."
        b = "Una frase nuova aggiunta qui. Prima frase senza importanza. Il sistema non funziona di notte. Ultima frase."
        result = run(a, b)
        self.assertEqual(result["outcome"], "partially measured")
        self.assertEqual(result["sentences"]["unaligned"], {"original": 0, "candidate": 1})

    def test_reworded_sentence_keeps_its_markers(self):
        a = "Il cantiere non potrà iniziare prima di marzo."
        b = "Il cantiere non potrà partire prima di marzo."
        self.assertEqual(run(a, b)["outcome"], "PASS")

    def test_unsupported_language(self):
        self.assertEqual(run("a", "b", "ja")["outcome"], "unsupported")


if __name__ == "__main__":
    unittest.main()
