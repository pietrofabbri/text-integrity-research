# Capability Specification: Structural Validation of Markdown and Plain Text

**Status:** ACTIVE (specification). The capability it specifies is `EXPERIMENTAL`.
**Version:** 0.1
**Document type:** Capability specification (`DEVELOPMENT-MAP.md` §22) and capability record (`CAPABILITY-ARCHITECTURE.md` §4)
**Implementation:** `src/text_integrity/validate_structural.py`; tests in `tests/test_validate_structural.py`
**Requirements basis:** `S04-fidelity-requirements.md` `FID-016`, `FID-034`, `FID-035`, `FID-041`, `FID-043`, `FID-090`; `S05-transformation-requirements.md` `TRN-022`, `TRN-023`
**Protocol basis:** `FIDELITY-VALIDATION-PROTOCOL.md` §6; `VALIDATION-MAP.md` §18
**Architectural basis:** `VALIDATION-ARCHITECTURE.md` §4, §5, §7–9
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-057, DEC-059, DEC-060 (this capability)

---

# 1. Purpose

Report whether a candidate text keeps the document structure of an original text. This is the first capability because it needs no model, dataset or dependency, and its behavior can be fully tested without scientific assumptions.

**It says nothing about meaning, factual accuracy, linguistic quality or detectability.** A `PASS` is a deterministic observation under declared conditions (`FID-090`), never evidence of fidelity overall (`FIDELITY-VALIDATION-PROTOCOL.md` §6, §8.3).

# 2. Capability Record

| Field | Value |
|---|---|
| `id` | `CAP-VALIDATE-STRUCTURAL-MARKDOWN` |
| `name` | Structural validation of Markdown |
| `category` | `VALIDATE-STRUCTURAL` |
| `version` | 0.2.0 |
| `status` | `EXPERIMENTAL` (has not passed the Activation Gate of `CAPABILITY-ARCHITECTURE.md` §7) |
| `languages` | `EXPERIMENTAL` for the 13 target languages of `DATA-MAP.md` §22; `unsupported` for any other. The rules read Markdown syntax, not language content; tests run on English, Japanese, Chinese, Russian and Turkish only |
| `dependencies` | None |
| `input_requirements` | Two strings, a language code, a declared constraint type, input format `markdown` or `plaintext` |
| `output_schema` | `VALIDATION-ARCHITECTURE.md` §8, with raw observations |
| `validation_requirements` | Not yet defined; needed before `VALIDATED` (see §7) |
| `scientific_sources` | None. No `R-XXXX` addresses structural comparison, so the Activation Gate condition on sources is not met |
| `known_limitations` | §6 |
| `resource_requirements` | No resources beyond the running interpreter |

# 3. Inputs

`original`, `candidate`, `language`, `constraint_type` (`HARD` or `SOFT`, no default, per `FID-041`), `input_format`, `permitted` (elements the experiment explicitly allows to change, per `FID-016`), `max_chars` (optional; no default value is set).

Inputs are never altered (`DEC-059`). Only line-break style is treated as equivalent, for splitting into lines.

# 4. Outputs

`outcome` is `PASS`, `FAIL`, `unsupported` or `not measurable` (`FID-043`). The result always carries both raw profiles, the differences, the permitted differences, and the lists of what was and was not measured. `confidence` is `null`, since none is provided and none may be inferred (`FID-044`).

| Measured | How |
|---|---|
| `paragraphs` | Count |
| `headings` | Ordered levels |
| `lists` | Ordered items with depth and ordered/unordered kind |
| `tables` | Rows and columns of each table |
| `block_quotes` | Lines per block |
| `code_blocks` | SHA-256 of exact content (`FID-034`) |
| `inline_code` | Exact content |
| `links` | Ordered targets |
| `footnotes` | References and definitions |
| `block_formulas` | SHA-256 of exact content of `$$` blocks |
| `block_order` | Ordered kinds of block |

**Reported, never measured:** `inline_quotations`, `inline_formulas` (a `$` is ambiguous with currency), `emphasis`, `whitespace`, `punctuation`, `capitalization`, `homoglyphs`. `FID-017` formatting is therefore not validated.

**Observation only:** the count of Unicode format characters (category `Cf`, such as zero-width characters) in each text. A difference does not cause `FAIL`, but stays visible (`FID-024`).

**Plain text (`plaintext`, 0.2.0):** blank-line blocks (`paragraphs`), non-list `lines`, `lists`, `title_like_lines` and `block_order`. A title-like line has letters and no final punctuation. This is a declared heuristic: it misses titles ending in punctuation and counts unpunctuated lines that are not titles. The other elements are reported as not measured.

# 5. Constraints and Failure Behavior

Read-only; no network, file or subprocess use. Invalid arguments raise an error. Unsupported format or language, or input above `max_chars`, returns a missing-evidence state and never `PASS` (`FID-043`). Whether the dimension is hard or soft is declared by the caller.

Classification under `AGENT-WORK-MODEL.md` §5: MEDIUM risk, C2 impact. `AGENT-SECURITY-BOUNDARY.md` §7 review: no dependency, network, filesystem, subprocess, credential, serialization, evaluation or dynamic-loading use.

# 6. Known Limitations

- Handles a common Markdown subset, with a line-based scanner rather than a complete parser. The two texts are scanned the same way, but unusual Markdown may be mis-categorized.
- A table immediately after a paragraph, with no blank line, is counted as part of the paragraph.
- Indented code blocks are read as paragraphs; indented continuation lines inside a list end the list.
- HTML blocks are not recognized, nor are reference-style links.
- Table cell text is not compared, only shape. Section-level boundary crossing (`TRN-023`) is not detected beyond `block_order`.
- HTML and other formats are `unsupported`, although `FID-016` requires comparison to account for the format of the input.

# 7. Evidence and Open Items

Tested by unit tests only. No experiment or benchmark has been run, and no performance is claimed. Moving to `VALIDATED` needs declared `validation_requirements` and the other conditions of `CAPABILITY-ARCHITECTURE.md` §7, which are owner-level decisions.
