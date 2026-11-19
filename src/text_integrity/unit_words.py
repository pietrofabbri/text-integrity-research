"""Unit words per language, mapped to unit symbols (numeric integrity 0.7.0).

A declared simplification: a closed list for seven languages, read only
directly after a number (`3 kilometres`, `5 chilogrammi`). Russian, Polish,
Turkish, Indonesian, Japanese and Chinese have no list. Words with another
common meaning are left out: English `pound` (also a currency), Italian
`gradi` (any degree), French `mille` and `milles` (thousand, mile).
"""
from __future__ import annotations

_WORDS: dict[str, dict[str, str]] = {
    "en": {
        "km": "kilometre|kilometres|kilometer|kilometers", "m": "metre|metres|meter|meters",
        "cm": "centimetre|centimetres|centimeter|centimeters", "mm": "millimetre|millimetres|millimeter|millimeters",
        "kg": "kilogram|kilograms|kilogramme|kilogrammes|kilo|kilos", "g": "gram|grams|gramme|grammes",
        "t": "tonne|tonnes", "l": "litre|litres|liter|liters", "ml": "millilitre|millilitres|milliliter|milliliters",
        "h": "hour|hours", "min": "minute|minutes", "s": "second|seconds",
        "mi": "mile|miles", "ft": "foot|feet", "yd": "yard|yards", "lb": "lbs", "oz": "ounce|ounces",
        "W": "watt|watts", "kW": "kilowatt|kilowatts", "kWh": "kilowatt-hour|kilowatt-hours",
        "°C": "degrees Celsius|degree Celsius", "°F": "degrees Fahrenheit|degree Fahrenheit",
    },
    "it": {
        "km": "chilometro|chilometri", "m": "metro|metri", "cm": "centimetro|centimetri", "mm": "millimetro|millimetri",
        "kg": "chilogrammo|chilogrammi|chilo|chili", "g": "grammo|grammi", "t": "tonnellata|tonnellate",
        "l": "litro|litri", "ml": "millilitro|millilitri", "h": "ora|ore", "min": "minuto|minuti", "s": "secondo|secondi",
        "mi": "miglio|miglia", "ft": "piede|piedi", "lb": "libbra|libbre",
        "W": "watt", "kW": "kilowatt|chilowatt", "kWh": "chilowattora|kilowattora",
        "°C": "gradi Celsius|grado Celsius|gradi centigradi", "°F": "gradi Fahrenheit|grado Fahrenheit",
    },
    "fr": {
        "km": "kilomètre|kilomètres", "m": "mètre|mètres", "cm": "centimètre|centimètres", "mm": "millimètre|millimètres",
        "kg": "kilogramme|kilogrammes|kilo|kilos", "g": "gramme|grammes", "t": "tonne|tonnes",
        "l": "litre|litres", "ml": "millilitre|millilitres", "h": "heure|heures", "min": "minute|minutes", "s": "seconde|secondes",
        "W": "watt|watts", "kW": "kilowatt|kilowatts", "°C": "degrés Celsius|degré Celsius",
    },
    "de": {
        "km": "Kilometer", "m": "Meter", "cm": "Zentimeter", "mm": "Millimeter", "kg": "Kilogramm|Kilo",
        "g": "Gramm", "t": "Tonne|Tonnen", "l": "Liter", "ml": "Milliliter", "h": "Stunde|Stunden",
        "min": "Minute|Minuten", "s": "Sekunde|Sekunden", "mi": "Meile|Meilen", "W": "Watt", "kW": "Kilowatt",
        "°C": "Grad Celsius",
    },
    "es": {
        "km": "kilómetro|kilómetros", "m": "metro|metros", "cm": "centímetro|centímetros", "mm": "milímetro|milímetros",
        "kg": "kilogramo|kilogramos|kilo|kilos", "g": "gramo|gramos", "t": "tonelada|toneladas",
        "l": "litro|litros", "ml": "mililitro|mililitros", "h": "hora|horas", "min": "minuto|minutos", "s": "segundo|segundos",
        "mi": "milla|millas", "W": "vatio|vatios", "°C": "grados Celsius|grado Celsius",
    },
    "pt": {
        "km": "quilómetro|quilómetros|quilômetro|quilômetros", "m": "metro|metros", "cm": "centímetro|centímetros",
        "mm": "milímetro|milímetros", "kg": "quilograma|quilogramas|quilo|quilos", "g": "grama|gramas",
        "t": "tonelada|toneladas", "l": "litro|litros", "ml": "mililitro|mililitros", "h": "hora|horas",
        "min": "minuto|minutos", "s": "segundo|segundos", "mi": "milha|milhas", "°C": "graus Celsius|grau Celsius",
    },
    "nl": {
        "km": "kilometer", "m": "meter", "cm": "centimeter", "mm": "millimeter", "kg": "kilogram|kilo",
        "g": "gram", "t": "ton", "l": "liter", "ml": "milliliter", "h": "uur", "min": "minuut|minuten",
        "s": "seconde|seconden", "mi": "mijl", "°C": "graden Celsius",
    },
}


def unit_words(language: str) -> dict[str, str]:
    """Return a map from lower-case unit word to unit symbol."""
    return {form.lower(): symbol for symbol, forms in _WORDS.get(language, {}).items() for form in forms.split("|")}
