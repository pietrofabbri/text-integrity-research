"""Closed lists of number words per language, used by numeric integrity (0.6.0).

A declared simplification, not a parser of number words:

- single words are read (`venti`, `twenty`), and since 0.11.0 two-part numbers
  from 21 to 99 in Italian, English, French, German and Spanish (`ventitré`,
  `twenty-three`, `dreiundzwanzig`, `veinticuatro`); other compounds (`cento
  venti`, `soixante et onze`, Turkish `on bir`) are not;
- words for "one" are left out in every language, because they double as
  articles or pronouns (`un`, `one`, `ein`, `bir`);
- Japanese and Chinese are left out, because their numeral characters also
  form ordinary words;
- some words have other meanings (Italian `sei`, French `neuf`, Turkish `yüz`),
  and are read as numbers wherever they occur;
- inflected forms are listed only where noted.

Words that name an exact count (`decade`, `dozen`, 0.10.1) are read as that
number. Each entry maps a lower-case word to its value. MULTIPLIERS may follow a number
and multiply it (`4,8 milioni`, `tre mila`).
"""
from __future__ import annotations

from decimal import Decimal

_TENS_AND_UNITS: dict[str, tuple[str, ...]] = {
    # values 2..20, then 30, 40, ..., 90
    "it": ("due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove", "venti",
           "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"),
    "en": ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
           "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"),
    "fr": ("deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf", "vingt",
           "trente", "quarante", "cinquante", "soixante", "soixante-dix", "quatre-vingts|quatre-vingt", "quatre-vingt-dix"),
    "de": ("zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn", "zwanzig",
           "dreißig", "vierzig", "fünfzig", "sechzig", "siebzig", "achtzig", "neunzig"),
    "es": ("dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte",
           "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"),
    "pt": ("dois|duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze|quatorze", "quinze", "dezasseis|dezesseis", "dezassete|dezessete", "dezoito", "dezanove|dezenove", "vinte",
           "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"),
    "nl": ("twee", "drie", "vier", "vijf", "zes", "zeven", "acht", "negen", "tien", "elf", "twaalf", "dertien", "veertien", "vijftien", "zestien", "zeventien", "achttien", "negentien", "twintig",
           "dertig", "veertig", "vijftig", "zestig", "zeventig", "tachtig", "negentig"),
    "ru": ("два|две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать", "двадцать",
           "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"),
    "pl": ("dwa|dwie", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć", "dziesięć", "jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście", "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście", "dwadzieścia",
           "trzydzieści", "czterdzieści", "pięćdziesiąt", "sześćdziesiąt", "siedemdziesiąt", "osiemdziesiąt", "dziewięćdziesiąt"),
    "tr": ("iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz", "on", "", "", "", "", "", "", "", "", "", "yirmi",
           "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"),
    "id": ("dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan", "sepuluh", "sebelas", "", "", "", "", "", "", "", "", "",
           "", "", "", "", "", "", ""),
}
_VALUES = (*range(2, 21), 30, 40, 50, 60, 70, 80, 90)

_OTHER: dict[str, dict[str, Decimal]] = {
    "it": {"cento": Decimal(100), "mille": Decimal(1000), "metà": Decimal("0.5"), "decennio": Decimal(10), "dozzina": Decimal(12)},
    "en": {"hundred": Decimal(100), "half": Decimal("0.5"), "decade": Decimal(10), "dozen": Decimal(12)},
    "fr": {"cent": Decimal(100), "mille": Decimal(1000), "moitié": Decimal("0.5"), "décennie": Decimal(10), "douzaine": Decimal(12)},
    "de": {"hundert": Decimal(100), "hälfte": Decimal("0.5"), "jahrzehnt": Decimal(10), "dutzend": Decimal(12)},
    "es": {"cien": Decimal(100), "ciento": Decimal(100), "mitad": Decimal("0.5"), "década": Decimal(10), "docena": Decimal(12)},
    "pt": {"cem": Decimal(100), "cento": Decimal(100), "metade": Decimal("0.5"), "década": Decimal(10), "dúzia": Decimal(12)},
    "nl": {"honderd": Decimal(100), "helft": Decimal("0.5"), "decennium": Decimal(10), "dozijn": Decimal(12)},
    "ru": {"сто": Decimal(100)},
    "pl": {"sto": Decimal(100)},
    "tr": {"yüz": Decimal(100), "yarım": Decimal("0.5")},
    "id": {"seratus": Decimal(100), "seribu": Decimal(1000), "setengah": Decimal("0.5")},
}

THOUSAND, MILLION, BILLION = Decimal(1000), Decimal(1000000), Decimal(1000000000)
MULTIPLIERS: dict[str, dict[str, Decimal]] = {
    "it": {"mila": THOUSAND, "milione": MILLION, "milioni": MILLION, "miliardo": BILLION, "miliardi": BILLION},
    "en": {"thousand": THOUSAND, "million": MILLION, "millions": MILLION, "billion": BILLION, "billions": BILLION},
    "fr": {"million": MILLION, "millions": MILLION, "milliard": BILLION, "milliards": BILLION},
    "de": {"tausend": THOUSAND, "million": MILLION, "millionen": MILLION, "milliarde": BILLION, "milliarden": BILLION},
    "es": {"mil": THOUSAND, "millón": MILLION, "millones": MILLION},
    "pt": {"mil": THOUSAND, "milhão": MILLION, "milhões": MILLION},
    "nl": {"duizend": THOUSAND, "miljoen": MILLION, "miljoenen": MILLION, "miljard": BILLION, "miljarden": BILLION},
    "ru": {"тысяча": THOUSAND, "тысячи": THOUSAND, "тысяч": THOUSAND, "миллион": MILLION, "миллиона": MILLION, "миллионов": MILLION, "миллиард": BILLION, "миллиарда": BILLION, "миллиардов": BILLION},
    "pl": {"tysiąc": THOUSAND, "tysiące": THOUSAND, "tysięcy": THOUSAND, "milion": MILLION, "miliony": MILLION, "milionów": MILLION, "miliard": BILLION, "miliardy": BILLION, "miliardów": BILLION},
    "tr": {"bin": THOUSAND, "milyon": MILLION, "milyar": BILLION},
    "id": {"ribu": THOUSAND, "juta": MILLION, "miliar": BILLION},
}


_UNITS_FOR_COMPOUNDS = {
    "it": ("uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove"),
    "en": ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine"),
    "fr": ("", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"),
    "de": ("ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"),
}
_SPANISH_TWENTIES = ("veintiuno", "veintidós", "veintitrés", "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve")


def _compounds(language: str) -> dict[str, Decimal]:
    """Two-part numbers from 21 to 99 (0.11.0): ventiquattro, twenty-four, vingt-quatre, vierundzwanzig, veinticuatro."""
    out: dict[str, Decimal] = {}
    forms = _TENS_AND_UNITS.get(language)
    units = _UNITS_FOR_COMPOUNDS.get(language)
    if forms and units:
        tens = {value: forms[i].split("|")[0] for i, value in enumerate(_VALUES) if value >= 20 and value % 10 == 0}
        for ten_value, ten in tens.items():
            if language == "fr" and ten_value in {70, 90}:
                continue
            if language == "fr" and ten_value == 80:
                ten = "quatre-vingt"
            for unit_value, unit in enumerate(units, 1):
                if not unit:
                    continue
                if language == "it":
                    stem = ten[:-1] if unit[0] in "uo" else ten
                    out[stem + unit] = Decimal(ten_value + unit_value)
                    if unit == "tre":
                        out[stem + "tré"] = Decimal(ten_value + 3)
                elif language in {"en", "fr"}:
                    out[f"{ten}-{unit}"] = Decimal(ten_value + unit_value)
                elif language == "de":
                    out[f"{unit}und{ten}"] = Decimal(ten_value + unit_value)
    if language == "es":
        out.update({word: Decimal(21 + i) for i, word in enumerate(_SPANISH_TWENTIES)})
    return out


def lexicon(language: str) -> dict[str, Decimal]:
    """Return every number word of a language with its value, multipliers included."""
    words: dict[str, Decimal] = dict(_compounds(language))
    for value, forms in zip(_VALUES, _TENS_AND_UNITS.get(language, ("",) * len(_VALUES)), strict=True):
        for form in forms.split("|"):
            if form:
                words[form] = Decimal(value)
    words.update(_OTHER.get(language, {}))
    words.update(MULTIPLIERS.get(language, {}))
    return words
