# Capability Specification: Negation, Modality and Listed Opposites

**Status:** ACTIVE (specification). The capability it specifies is `EXPERIMENTAL`.
**Version:** 0.1
**Document type:** Capability specification (`DEVELOPMENT-MAP.md` §22) and capability record (`CAPABILITY-ARCHITECTURE.md` §4)
**Implementation:** `src/text_integrity/validate_polarity.py`; tests in `tests/test_validate_polarity.py`
**Requirements basis:** `S04-fidelity-requirements.md` `FID-006` (Negation), `FID-007` (Modality), `FID-043`, `FID-046`
**Protocol basis:** `FIDELITY-VALIDATION-PROTOCOL.md` §3.2
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-015, DEC-075, DEC-080 (this capability)

---

# 1. Purpose

Detect, in sentences that correspond between an original and a candidate text, a change in the number of negation markers, in the classes of modal verbs, or in a closed list of opposite words. These are the meaning changes that passed every other capability in the owner's test kit and in the trials of §17, §22 and §23 of `TRIAL-GIT-HISTORY.md`: `non garantisce` → `garantisce`, `può` → `deve`, `n'entraîne aucune` → `entraîne une`, `aumento` → `diminuzione`.

**It is not a semantic validator.** It reads listed words, not meaning. `FIDELITY-VALIDATION-PROTOCOL.md` §3.2 and `DEC-015` leave semantic and claim-level validation without a validated method in 12 of the 13 languages; this capability does not change that, and a `PASS` is not evidence that meaning was preserved.

# 2. Capability Record

| Field | Value |
|---|---|
| `id` | `CAP-VALIDATE-SEMANTIC-POLARITY` |
| `name` | Negation, modality and listed opposites |
| `category` | `VALIDATE-SEMANTIC` |
| `version` | 0.1.0 |
| `status` | `EXPERIMENTAL` |
| `languages` | `it`, `en`, `fr`, `de`, `es`, `pt`, `nl`, `ru`, `pl` for all three checks; `tr`, `id` for negation only; `ja`, `zh` `unsupported` |
| `dependencies` | None; Python standard library only |
| `input_requirements` | Two strings, a language code, a declared constraint type |
| `output_schema` | `VALIDATION-ARCHITECTURE.md` §8, with `changes`, sentence counts and `not_measured` |
| `validation_requirements` | As for the other capabilities (`ACCEPTANCE-CRITERIA-OPTIONS.md` §5); no threshold |
| `scientific_sources` | None. The marker lists are the agent's and are not checked by native speakers |
| `known_limitations` | §5 |
| `resource_requirements` | No resources beyond the running interpreter |

# 3. Method

1. **Sentences** are split after `.`, `!`, `?`, `…`, `;` and `:` followed by space, and at blank lines (`polarity-v1`).
2. **Alignment:** sentences are paired in order, maximizing the sum of token similarity (`difflib` ratio over lower-cased tokens). A pair needs a similarity above 0.5; this value is an engineering parameter of the alignment, chosen by the agent, not a fidelity threshold. Unpaired sentences are counted and not compared.
3. **Markers**, compared for each pair:
   - **negation:** the number of listed negation words (`non`, `né`, `senza`; `not`, `no`, `never`, `n't`; `ne`, `pas`, `aucun`; `nicht`, `kein`; and so on). Different counts are a change;
   - **modality:** counts of verbs of possibility (`può`, `can`, `peut`, `kann`, `puede`) and of obligation (`deve`, `must`, `doit`, `muss`, `debe`). Different counts per class are a change;
   - **opposites:** a closed list of pairs per language (`prima`/`dopo`, `before`/`after`, `aumento`/`diminuzione`, `increase`/`decrease`, `massimo`/`minimo`). A different count of either side is a change.
4. **Outcome:** `FAIL` (severity `MAJOR`, `FID-046`) if any aligned pair shows a change; otherwise `partially measured` if some sentences could not be aligned, else `PASS`. The severity and the outcome rule are the agent's proposal under `DEC-080`, awaiting the owner's confirmation (`DEC-004`).

# 4. Outcomes

| Outcome | When |
|---|---|
| `FAIL` (`MAJOR`) | A listed marker changed in an aligned pair; every change is listed with both sentences |
| `partially measured` | No change in aligned pairs, but some sentences are unaligned |
| `PASS` | All sentences aligned and no listed marker changed |
| `unsupported`, `not measurable` | Unlisted language, or input above `max_chars` |

# 5. Known Limitations

- **Meaning in general is not assessed.** Antonyms outside the list (`evitando` → `provocando`, `garantendo` → `escludendo`), verbs and adjectives of negative meaning (`manca`, `lacks`, `impossible`), negation by prefix (`unable`, `inefficace`), and implicit negation are not read.
- **The scope of negation is not analysed.** Moving a negation within a sentence, or replacing `non ... mai` with `mai`, may pass or fail regardless of meaning. Restrictive `ne ... que` in French counts as negation.
- **A rephrasing that keeps meaning can fail**: `non garantisce` → `manca di garantire`, or `must not` → `may not`. No such false alarm has been measured yet.
- **Overlap with numeric qualifiers:** `non più di 30` → `almeno 30` is reported by both capabilities.
- Conditional mood, tense, certainty adverbs (`probabilmente`, `certainly`) and evidentiality are not read.
- Sentences changed too much to align are not compared; a heavy rewrite can therefore pass with changes inside it.
- Word lists are closed, cover nine languages for modality and opposites, and are not checked by native speakers.

# 6. Evidence

Unit tests only, written by the same agent. The marker lists were written after the agent had seen the meaning changes in the test kit and in the reserve series (R01–R14), so **none of those texts can serve as held-out evidence for this capability**; a new reserve is needed (`ACCEPTANCE-CRITERIA-OPTIONS.md` D5). On R01–R14 as development data, see `TRIAL-GIT-HISTORY.md` §24.
