# Capability Specification: Lexical Minimality Measurement

**Status:** ACTIVE (specification). The capability it specifies is `EXPERIMENTAL`.
**Version:** 0.1
**Document type:** Capability specification (`DEVELOPMENT-MAP.md` §22) and capability record (`CAPABILITY-ARCHITECTURE.md` §4)
**Implementation:** `src/text_integrity/measure_minimality.py`; tests in `tests/test_measure_minimality.py`
**Requirements basis:** `S04-fidelity-requirements.md` `FID-021`, `FID-022`, `FID-037`, `FID-038`, `FID-043`, `FID-057`; `S05-transformation-requirements.md` `TRN-007`, `TRN-011`
**Protocol basis:** `FIDELITY-VALIDATION-PROTOCOL.md` §8.2; `VALIDATION-MAP.md` §20
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-057, DEC-059, DEC-060, DEC-061 (this capability)

---

# 1. Purpose

Report how much a candidate text differs from its original, as separate measurements.

**It is not a quality measure.** It gives no combined score and no `PASS` or `FAIL`. Fewer changes do not make a transformation better (`TRN-007`), and minimality is subordinate to preservation (`FID-057`). Comparing methods requires the multi-objective presentation of `FIDELITY-VALIDATION-PROTOCOL.md` §8.4, which this capability does not produce.

# 2. Capability Record

| Field | Value |
|---|---|
| `id` | `CAP-VALIDATE-MINIMALITY-LEXICAL` |
| `name` | Lexical minimality measurement |
| `category` | `VALIDATE-MINIMALITY` |
| `version` | 0.3.0 |
| `status` | `EXPERIMENTAL` |
| `languages` | Character metrics: 13 target languages. Token metrics: the 11 written with spaces between words; `not measurable` for Japanese and Chinese, which have no registered tokenizer |
| `dependencies` | `CAP-VALIDATE-STRUCTURAL-MARKDOWN` for `structural_change_rate`; no external dependency |
| `input_requirements` | Two strings, a language code, optional input format and `max_chars` |
| `output_schema` | `VALIDATION-ARCHITECTURE.md` §8, with `outcome` `partially measured` and a metrics table; `constraint_type` is always `SOFT` (`FID-057`) |
| `validation_requirements` | Not yet defined |
| `scientific_sources` | None. No `R-XXXX` validates these metrics for this purpose, so the Activation Gate condition on sources is not met |
| `known_limitations` | §5 |
| `resource_requirements` | No resources beyond the running interpreter |

# 3. Metrics

Definitions of the ratios are this capability's own, because no project document defines them (`FID-038`). The denominator is the number of tokens in the original.

| Metric | Definition | State |
|---|---|---|
| `character_edit_distance` | Levenshtein over Unicode code points, no normalization (`DEC-059`) | measured |
| `token_edit_distance` | Levenshtein over tokens | measured where tokenized |
| `changed_token_ratio` | Token edit distance ÷ original tokens; may exceed 1 | same |
| `inserted_token_ratio`, `deleted_token_ratio` | Insertions or deletions ÷ original tokens | same |
| `lexical_substitution_rate` | Substitutions ÷ original tokens | same |
| `structural_change_rate` | Differing elements ÷ the elements compared by the structural capability, of the input format, with the elements listed | measured for Markdown and plain text |
| `changed_sentence_ratio` | Original sentences without an exact match in the candidate ÷ original sentences (`punctuation-v1`) | measured |
| `semantic_deviation` | No semantic validator exists | `not measurable` |

**Tokenizer `whitespace-v1`:** splits on whitespace, case-sensitive, punctuation stays attached to words. It is a declared simplification, not a linguistic tokenizer.

**Splitter `punctuation-v1`:** splits after `.`, `!`, `?` or `…` followed by whitespace, and after `。`, `！`, `？`. It is a declared simplification: abbreviations split too, and any small edit marks the whole sentence as changed.

# 4. Failure Behavior

Non-string input raises an error. An unknown language returns `unsupported`; input above `max_chars` returns `not measurable`. Missing metrics are stated, never omitted (`FID-043`). Risk classification: MEDIUM, C2. Review under `AGENT-SECURITY-BOUNDARY.md` §7: none of the listed behaviors.

# 5. Known Limitations

- Attached punctuation counts: `word` and `word,` are different tokens, inflating token metrics.
- Token counts are not comparable across languages. Agglutinative languages such as Turkish pack more into a whitespace token (`LANGUAGE-ARCHITECTURE.md` §6).
- Since 0.3.0 token alignment is banded and exact, with results identical to the full table, tie-breaks included (checked by unit tests). Time grows with text length times the number of changes, so long texts with few changes are fast. Very long, heavily rewritten texts stay slow, about 8 seconds on a synthetic 5,000-token text with 1,641 token edits; this is one machine and not a benchmark. `max_chars` has no default value (`RESILIENCE-AND-SECURITY-ASSURANCE.md` RSA-G1).
- When several minimal alignments exist, the split between insertions, deletions and substitutions depends on a fixed tie-break. The total distance does not.
- The structural rate weights all elements equally. This is a convention without scientific basis.

# 6. Open Items

- `FIDELITY-VALIDATION-PROTOCOL.md` §2 says its §8 defines the minimum content of a structured diff. §8 defines metrics but no diff format, and this capability produces no span-level diff.
- Budget checks (`TRN-011`, `FID-022`) are not implemented; any limit must be set and versioned by an experiment.
- No experiment or benchmark has been run, and no performance is claimed.
