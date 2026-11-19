"""Words that qualify a number, grouped by meaning (numeric integrity 0.10.0).

A declared simplification, chosen by the agent on the owner's delegation
(DEC-076). A qualifier is a phrase directly before a number. Each phrase
belongs to one class:

- APPROX: about the number (`circa`, `about`, `environ`, `etwa`);
- LOWER: the number or more (`almeno`, `oltre`, `più di`, `at least`);
- UPPER: the number or less (`fino a`, `meno di`, `quasi`, `up to`).

A change of class fails; a change within a class (`fino a` and `meno di`) is
not reported as a change; a qualifier present on one side only lowers the
outcome. Strict and non-strict bounds share a class. Seven languages have
lists: Italian, English, French, German, Spanish, Portuguese, Dutch.
"""
from __future__ import annotations

APPROX, LOWER, UPPER = "approx", "lower", "upper"

_PHRASES: dict[str, dict[str, str]] = {
    "it": {
        APPROX: "circa|all'incirca|approssimativamente|intorno a|intorno ai|attorno a|attorno ai|nell'ordine di",
        LOWER: "almeno|oltre|più di|sopra|superiore a|superiori a|non meno di|ben oltre",
        UPPER: "fino a|fino ad|meno di|non più di|al massimo|massimo|quasi|inferiore a|inferiori a|sotto|entro",
    },
    "en": {
        APPROX: "about|around|approximately|roughly|some|circa|an estimated",
        LOWER: "at least|more than|over|above|in excess of|upwards of|no fewer than|no less than",
        UPPER: "up to|less than|fewer than|under|below|at most|no more than|nearly|almost|just under",
    },
    "fr": {
        APPROX: "environ|près de|quelque|approximativement|autour de|aux alentours de",
        LOWER: "au moins|plus de|au-delà de|plus d'|pas moins de",
        UPPER: "jusqu'à|moins de|au plus|au maximum|presque|pas plus de|moins d'",
    },
    "de": {
        APPROX: "etwa|rund|ungefähr|circa|ca.|zirka",
        LOWER: "mindestens|mehr als|über|wenigstens",
        UPPER: "bis zu|weniger als|höchstens|fast|knapp|unter|maximal",
    },
    "es": {
        APPROX: "aproximadamente|alrededor de|cerca de|unos|unas|en torno a",
        LOWER: "al menos|más de|por lo menos|como mínimo",
        UPPER: "hasta|menos de|como máximo|casi|no más de",
    },
    "pt": {
        APPROX: "aproximadamente|cerca de|por volta de|em torno de|uns|umas",
        LOWER: "pelo menos|mais de|no mínimo|acima de",
        UPPER: "até|menos de|no máximo|quase|abaixo de",
    },
    "nl": {
        APPROX: "ongeveer|circa|zo'n|rond|ca.",
        LOWER: "minstens|ten minste|meer dan|ruim|minimaal",
        UPPER: "tot|minder dan|hoogstens|bijna|maximaal|tot wel",
    },
}


def qualifiers(language: str) -> dict[str, str]:
    """Return a map from lower-case qualifier phrase to its class."""
    return {phrase: cls for cls, phrases in _PHRASES.get(language, {}).items() for phrase in phrases.split("|")}
