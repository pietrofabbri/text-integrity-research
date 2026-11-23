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
lists: Italian, English, French, German, Spanish, Portuguese, Dutch, and since
0.11.0 Polish and Russian.
"""
from __future__ import annotations

APPROX, LOWER, UPPER = "approx", "lower", "upper"

_PHRASES: dict[str, dict[str, str]] = {
    "it": {
        APPROX: "circa|all'incirca|approssimativamente|intorno a|intorno ai|attorno a|attorno ai|nell'ordine di",
        LOWER: "almeno|oltre|più di|sopra|superiore a|superiori a|superiore al|superiori al|superiore ai|superiori ai|non meno di|ben oltre|al di sopra di",
        UPPER: "fino a|fino ad|meno di|non più di|al massimo|massimo|quasi|inferiore a|inferiori a|inferiore al|inferiori al|inferiore ai|inferiori ai|sotto|entro|al di sotto di",
    },
    "en": {
        APPROX: "about|around|approximately|roughly|some|circa|an estimated",
        LOWER: "at least|more than|over|above|in excess of|upwards of|no fewer than|no less than|greater than|higher than",
        UPPER: "up to|less than|fewer than|under|below|at most|no more than|nearly|almost|just under|lower than",
    },
    "fr": {
        APPROX: "environ|près de|quelque|approximativement|autour de|aux alentours de",
        LOWER: "au moins|plus de|au-delà de|plus d'|pas moins de|supérieur à|supérieure à|supérieurs à|supérieures à|supérieur au|supérieure au|au-dessus de",
        UPPER: "jusqu'à|moins de|au plus|au maximum|presque|pas plus de|moins d'|inférieur à|inférieure à|inférieurs à|inférieures à|inférieur au|inférieure au|en dessous de|au-dessous de",
    },
    "de": {
        APPROX: "etwa|rund|ungefähr|circa|ca.|zirka",
        LOWER: "mindestens|mehr als|über|wenigstens|oberhalb von|höher als",
        UPPER: "bis zu|weniger als|höchstens|fast|knapp|unter|maximal|unterhalb von|niedriger als",
    },
    "es": {
        APPROX: "aproximadamente|alrededor de|cerca de|unos|unas|en torno a",
        LOWER: "al menos|más de|por lo menos|como mínimo|superior a|superiores a|superior al|superiores al|por encima de",
        UPPER: "hasta|menos de|como máximo|casi|no más de|inferior a|inferiores a|inferior al|inferiores al|por debajo de",
    },
    "pt": {
        APPROX: "aproximadamente|cerca de|por volta de|em torno de|uns|umas",
        LOWER: "pelo menos|mais de|no mínimo|acima de|superior a|superiores a|superior ao|superiores aos",
        UPPER: "até|menos de|no máximo|quase|abaixo de|inferior a|inferiores a|inferior ao|inferiores aos",
    },
    "nl": {
        APPROX: "ongeveer|circa|zo'n|rond|ca.",
        LOWER: "minstens|ten minste|meer dan|ruim|minimaal|boven|hoger dan|op zijn minst|op z'n minst",
        UPPER: "tot|minder dan|hoogstens|bijna|maximaal|tot wel|onder|lager dan|ten hoogste|op zijn hoogst|op z'n hoogst",
    },
    # 0.11.0
    "pl": {
        APPROX: "około|ok.|mniej więcej|rzędu",
        LOWER: "co najmniej|przynajmniej|ponad|powyżej|więcej niż|nie mniej niż|minimum",
        UPPER: "co najwyżej|maksymalnie|poniżej|mniej niż|nie więcej niż|prawie|niemal|do",
    },
    "ru": {
        APPROX: "около|примерно|приблизительно|порядка",
        LOWER: "не менее|не менее чем|не менее чем на|более|более чем|более чем на|свыше|по меньшей мере|как минимум|больше",
        UPPER: "не более|не более чем|не более чем на|менее|менее чем|менее чем на|максимум|почти|не больше|до",
    },
}


def qualifiers(language: str) -> dict[str, str]:
    """Return a map from lower-case qualifier phrase to its class."""
    return {phrase: cls for cls, phrases in _PHRASES.get(language, {}).items() for phrase in phrases.split("|")}
