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
| `version` | 0.3.0 |
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

**Not numbers:** digits directly after a letter of a script written with spaces (`v2`, `H2O`). Since 0.3.0, digits after kana or CJK ideographs are numbers: Japanese and Chinese have no space before them, and earlier versions silently read almost none of them. Forms that fit no pattern (`1.2.3`) are kept literally and match only identically. Digits in any Unicode script are read by value.

**Units (0.2.0):** a closed list of symbols directly after a number (`kg`, `g`, `km`, `m`, `l`, `kWh`, `GB`, `°C`, `EUR` and others, in `UNITS` in the code). Unit words (`chilogrammi`) are not read. Two different known units fail unless they are an exact metric conversion (`1,5 km` and `1500 m`, class `unit_conversion`). If only one side has a known unit, the pair is listed in `unit_uncertain` and the outcome is at best `partially measured`.

**List markers (0.2.0):** a number of up to three digits at the start of a line, followed by `.` or `)` and a space, is treated as a list marker and not compared.

**Dates (0.3.0):** dates are read as whole items and compared as dates, in support of `FID-009`; their digits are not also counted as numbers. Forms read: `YYYY-MM-DD` and `D/M/YYYY` with `-`, `/` or `.` as separator; full month names of the 11 languages written with spaces (`15 marzo 2024`, `March 15, 2024`, `5 de mayo de 2021`, `15. März 2024`, with or without day or year); `2024年3月15日` and its shorter forms in Japanese and Chinese. The same date in another form is class `equivalent` in `comparison.dates` and does not fail. A changed, removed or added date, including a dropped month or year, fails.

**Date convention (a declared simplification):** an all-digit date that is valid both as day-first and month-first is read day-first, except in English, where both readings are kept because both are in use. A pairing that depends on this cannot give more than `partially measured`.

# 4. Outcomes

| Outcome | When |
|---|---|
| `FAIL` (severity `CRITICAL`, per `FID-046`) | Any number removed or added, or a rounding not permitted |
| `partially measured` | No change found, but a pairing depends on the convention, matched numbers changed order, or a unit is known on one side only; the same for dates |
| `PASS` | All numbers paired, in order, without relying on the convention |
| `unsupported`, `not measurable` | Unknown language, or input above `max_chars` |

`equivalent` values (`0.50` and `0.5`) do not fail, and remain visible. Rounding fails unless the experiment sets `permit_rounding`. Percent and currency symbol form part of a number's identity. `constraint_type` has no default (`FID-041`). Inputs are unaltered (`DEC-059`). Risk: MEDIUM, C2. Review under `AGENT-SECURITY-BOUNDARY.md` §7: none of the listed behaviors.

# 5. Known Limitations

- **Numbers written as words are not read** (`three`, `三百`). Changing `three` to `four` is not detected, and a text with no digits returns `PASS`. The result always lists this in `not_measured`.
- **What a number refers to is not known.** Swapped values are only signalled by a change of order, and a legitimate reordering gives the same signal.
- Conversions are exact and metric only: `5 km` and `3.1 miles` are reported as changed. Single-letter units can be misread, as in `Room 5 B`. Temperature scales and currencies are never converted.
- Times, durations and relative expressions (`14:30`, `three days later`, `last week`) are not read (`FID-009`); times are still treated as separate numbers.
- Abbreviated month names (`Jan`, `gen.`), inflected forms not listed in `MONTHS` (Russian `в марте`, for example) and two-digit years are not read as dates. Their digits are compared as numbers, and a changed month name is then not detected.
- A number after an English month name is read as a day, so `In May 30 people came` gives a date. Date order is checked among dates only, not against the surrounding numbers.
- Ranges, comparisons, magnitudes in words (`3 million`) and expressions (`FID-008`) are not interpreted.
- A plain space is not treated as digit grouping, because it could separate two numbers.
- Pairing is greedy and deterministic, and may differ from a human's pairing when many similar numbers occur.

# 6. Open Items

Per `VALIDATION-ARCHITECTURE.md` §6.1, whether extraction is adequately evidenced per language is an open question, to be raised as a knowledge-backlog item when activation is proposed. No experiment has been run and no performance is claimed.
