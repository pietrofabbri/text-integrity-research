# Capability Specification: Numeric Integrity of Digit-Written Numbers

**Status:** ACTIVE (specification). The capability it specifies is `EXPERIMENTAL`.
**Version:** 0.1
**Document type:** Capability specification (`DEVELOPMENT-MAP.md` §22) and capability record (`CAPABILITY-ARCHITECTURE.md` §4)
**Implementation:** `src/text_integrity/validate_numeric.py`; tests in `tests/test_validate_numeric.py`
**Requirements basis:** `S04-fidelity-requirements.md` `FID-003`, `FID-008`, `FID-041`, `FID-043`, `FID-046`
**Protocol basis:** `FIDELITY-VALIDATION-PROTOCOL.md` §4.1, §5; `VALIDATION-MAP.md` §16
**Architectural basis:** `VALIDATION-ARCHITECTURE.md` §6, §8
**Research basis:** `R-0079` and `R-0041` show that the failure mode exists; per `FIDELITY-VALIDATION-PROTOCOL.md` §5 this evidence is anecdotal and does not support any claim about the check itself
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-015, DEC-057, DEC-059, DEC-062 (this capability)

---

# 1. Purpose

Compare the numbers written with digits in an original and a candidate text, and classify each as `exact`, `equivalent`, `rounding` or changed (`removed` / `added`), as `VALIDATION-MAP.md` §16 requires, and recognize exact conversions between metric units.

**A `PASS` covers digit-written numbers only.** It is a deterministic extraction result under declared conditions (`FIDELITY-VALIDATION-PROTOCOL.md` §5), not a finding that facts were preserved.

# 2. Capability Record

| Field | Value |
|---|---|
| `id` | `CAP-VALIDATE-FACTUAL-STRUCTURED-NUMERIC` |
| `name` | Numeric integrity of digit-written numbers |
| `category` | `VALIDATE-FACTUAL-STRUCTURED` |
| `version` | 0.10.0 |
| `status` | `EXPERIMENTAL` |
| `languages` | `EXPERIMENTAL` for the 13 target languages; `unsupported` otherwise |
| `dependencies` | None |
| `input_requirements` | Two strings, a language code, a declared constraint type |
| `output_schema` | `VALIDATION-ARCHITECTURE.md` §8, with the full comparison |
| `validation_requirements` | Not yet defined |
| `scientific_sources` | `R-0079` and `R-0041` for the failure mode only |
| `known_limitations` | §5 |
| `resource_requirements` | No resources beyond the running interpreter |

# 3. Number Reading

**Decimal convention by language (a declared simplification):** point for `en`, `ja`, `zh`; comma for `de`, `es`, `fr`, `id`, `it`, `nl`, `pl`, `pt`, `ru`, `tr`. Regional variants that differ, such as Mexican Spanish, are read incorrectly.

**Ambiguity:** a form with one separator followed by three digits (`1.000`, `1,000`) has opposite meanings under the two conventions. The number is read by the language's convention and flagged. If a pairing depends on such a reading, the outcome can be at best `partially measured`.

**Identifier-like numbers:** numbers joined to letters by a hyphen (`DEC-058`, `10-year`) count normally, since a real quantity may look the same, and changes to them are also reported in `identifier_like_changes`.

**Codes (0.6.0):** a token where a letter of a script written with spaces stands directly before a digit (`v2.3`, `H2O`, `A4`, `CO2`) is a code. Codes are compared literally, as whole items, in `comparison.codes`; a changed, removed or added code fails. Unit symbols such as `m2` are not codes, and digits inside a code are not also read as numbers. Before 0.6.0, `v2.3` to `v3.3` was not detected.

**Not numbers:** digits inside a code. Since 0.3.0, digits after kana or CJK ideographs are numbers: Japanese and Chinese have no space before them, and earlier versions silently read almost none of them. Forms that fit no pattern (`1.2.3`) are kept literally and match only identically. Digits in any Unicode script are read by value.

**Number words (0.6.0):** single number words are read from closed lists per language in `src/text_integrity/number_words.py` (11 languages; Japanese and Chinese have none). A number word and the same value in digits are `equivalent` (`tre` and `3`). A multiplier word right after a number joins it (`4,8 milioni` = 4,800,000; `120 mila`). Declared simplifications: compound words (`ventitré`, `twenty-three`) are not read; words for "one" are left out, because they double as articles or pronouns; inflected forms are listed only for Russian and Polish multipliers and a few others; words with another meaning (Italian `sei`, French `neuf`, Turkish `yüz`) are read as numbers wherever they occur.

**Qualifiers (0.10.0):** a phrase directly before a number that bounds or approximates it is read from closed lists for seven languages (`src/text_integrity/number_qualifiers.py`) and assigned one of three classes: about (`circa`, `about`), the number or more (`almeno`, `oltre`, `più di`, `at least`) and the number or less (`fino a`, `meno di`, `quasi`, `up to`). For paired numbers, a change of class fails and is listed in `qualifier_changed`; a qualifier on one side only gives at best `partially measured` and is listed in `qualifier_uncertain`; a change within a class is not reported. Strict and non-strict bounds share a class, so `fino a` and `meno di` are not distinguished. Verbs that qualify a number (`atteindre`, `dépasser`) are not read. The rule is the agent's, on the owner's delegation (`DEC-076`).

**Percent words (0.8.0):** `per cento`, `percent`, `pour cent`, `Prozent`, `por ciento`, `por cento`, `procent`, `процент`, `persen` and their listed forms, directly after a number, mark it as a percentage, so `25 pour cent` and `25 %` are `equivalent`. The words are not also read as number words. Turkish, where `yüzde` precedes the number, Japanese and Chinese are not covered.

**Units (0.2.0):** a closed list of symbols directly after a number (`kg`, `g`, `km`, `m`, `l`, `kWh`, `GB`, `°C`, `EUR` and others, in `UNITS` in the code). Unit words (`chilogrammi`) are not read. Two different known units fail unless they are an exact metric conversion (`1,5 km` and `1500 m`, class `unit_conversion`). If only one side has a known unit, the pair is listed in `unit_uncertain` and the outcome is at best `partially measured`.

**Unit words (0.7.0):** directly after a number, unit words from closed lists for English, Italian, French, German, Spanish, Portuguese and Dutch (`src/text_integrity/unit_words.py`) are read as the matching symbol: `3 kilometres` is `3 km`, and `5 chilogrammi` to `5 grammi` fails. Reports show the unit as written. Words with another common meaning are left out (English `pound`, Italian `gradi` alone).

**Units outside the metric system (0.7.0):** miles (only as a word), feet, yards, pounds (`lb`), ounces, `mph` and `°F` are converted by their exact definitions. An exact match is a `unit_conversion`. A match after rounding to the digits shown by the rounder side (`5 miles` and `8 km`, `70 °F` and `21 °C`) is an `approximate_conversion`: it does not fail, and the outcome is at best `partially measured`. **This tolerance rule was proposed in `DEC-070` and confirmed by the owner in `DEC-071`.**

**List markers (0.2.0):** a number of up to three digits at the start of a line, followed by `.` or `)` and a space, is treated as a list marker and not compared.

**Dates (0.3.0):** dates are read as whole items and compared as dates, in support of `FID-009`; their digits are not also counted as numbers. Forms read: `YYYY-MM-DD` and `D/M/YYYY` with `-`, `/` or `.` as separator; full month names of the 11 languages written with spaces (`15 marzo 2024`, `March 15, 2024`, `5 de mayo de 2021`, `15. März 2024`, with or without day or year); `2024年3月15日` and its shorter forms in Japanese and Chinese. The same date in another form is class `equivalent` in `comparison.dates` and does not fail. A changed, removed or added date, including a dropped month or year, fails.

**Abbreviated months (0.4.0):** the abbreviations in `MONTH_ABBREVIATIONS` are read only when a number follows (`15 mar. 2024`, `Mar 2024`, English `Mar 5`), because alone they collide with ordinary words.

**Date convention (a declared simplification):** an all-digit date that is valid both as day-first and month-first is read day-first, except in English, where both readings are kept because both are in use. A pairing that depends on this cannot give more than `partially measured`.

**Pairing (0.5.0):** numbers, and separately dates, are paired by an order-preserving alignment. A pair costs its class (exact, then equivalent, unit conversion, rounding); an unpaired or substituted item costs more than any pair. A changed item is therefore paired with the item in the same position, and reported in `changed` as original and candidate, instead of being paired with an identical item elsewhere. Items left over that equal an item elsewhere are paired as moved, and the outcome is then at best `partially measured`. Runs of identical items at both ends are paired directly; the rest takes time proportional to the product of the two lengths, about 3 seconds for 1,400 numbers against 1,400 (one machine, not a benchmark).

# 4. Outcomes

| Outcome | When |
|---|---|
| `FAIL` (severity `CRITICAL`, per `FID-046`) | Any number removed or added, or a rounding not permitted |
| `partially measured` | No change found, but a pairing depends on the convention, matched numbers changed order, or a unit is known on one side only; the same for dates |
| `PASS` | All numbers paired, in order, without relying on the convention |
| `unsupported`, `not measurable` | Unknown language, or input above `max_chars` |

`equivalent` values (`0.50` and `0.5`) do not fail, and remain visible. Rounding fails unless the experiment sets `permit_rounding`. Percent and currency symbol form part of a number's identity. Since 0.4.0 the symbol may stand before or after the number, and `EUR`, `USD`, `GBP` and `JPY` count as the same currency as their symbols, before the number too since 0.5.0; currency words (`euro`) are not read. `constraint_type` has no default (`FID-041`). Inputs are unaltered (`DEC-059`). Risk: MEDIUM, C2. Review under `AGENT-SECURITY-BOUNDARY.md` §7: none of the listed behaviors.

# 5. Known Limitations

- **Compound number words and Japanese or Chinese numerals are not read** (`twenty-three`, `三百`). Changing `twenty-three` to `twenty-four` is not detected. The result lists this in `not_measured`. Single number words are read since 0.6.0.
- Qualifiers outside the seven listed languages, and verbs or clauses that qualify a number, are not read.
- **What a number refers to is not known.** Swapped values are only signalled by a change of order, and a legitimate reordering gives the same signal.
- Unit words are read in seven languages only. Single-letter units can be misread, as in `Room 5 B`. Currencies are never converted. US and UK gallons, inches and other units outside the list are not read.
- Times, durations and relative expressions (`14:30`, `three days later`, `last week`) are not read (`FID-009`); times are still treated as separate numbers.
- Abbreviated month names with no number after them (`15 mar.`), inflected forms not listed in `MONTHS` (Russian and Polish have nominative, genitive and, since 0.9.0, prepositional or locative forms such as `в марте` and `w marcu`; other cases are not listed) and two-digit years are not read as dates. Their digits are compared as numbers, and a changed month name is then not detected.
- A number after an English month name is read as a day, so `In May 30 people came` gives a date. Date order is checked among dates only, not against the surrounding numbers.
- Ranges, comparisons, magnitudes in words (`3 million`) and expressions (`FID-008`) are not interpreted.
- A plain space is not treated as digit grouping, because it could separate two numbers.
- Pairing is deterministic and favours position. When the same value occurs several times and items are both changed and moved, it may still differ from a human's pairing.

# 6. Open Items

Per `VALIDATION-ARCHITECTURE.md` §6.1, whether extraction is adequately evidenced per language is an open question, to be raised as a knowledge-backlog item when activation is proposed. No experiment has been run and no performance is claimed.
