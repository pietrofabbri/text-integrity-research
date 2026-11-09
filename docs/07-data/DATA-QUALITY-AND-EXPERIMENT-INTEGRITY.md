# Data Quality and Experiment Integrity

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Data governance protocol (Tranche 4 of `DATA-MAP.md` §126)
**Authority:** Data. Validation methodology remains with `docs/05-validation/`.
**Parent:** `docs/07-data/DATA-MAP.md` §50–66, §83–86, §88–89, §112–113, §116–117
**Requirements basis:** `docs/03-scientific-specification/S02-scientific-requirements.md` `REQ-LANG-003`
**Research basis:** `docs/02-research/R08-benchmark-dataset-research.md` §31–40, §69.3–69.4; `R07` §80.2 (`R-0087`–`R-0089`)
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-012, DEC-051, DEC-055 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes how data enters the project, how its quality is judged, and which gates apply before it is relied on. It sets no quality threshold, duplicate rate or split ratio. Software test rules are in `TEST-AND-VERIFICATION-POLICY.md` §6.

---

# 2. Recorded Contradictions and Ambiguities — Not Resolved Here

| ID | Subject | Locations | Finding |
|---|---|---|---|
| DQI-C1 | Translation as augmentation | `DATA-MAP.md` §64–66 | §66 lists translation and paraphrase as augmentation; §64–65 treat translated and back-translated data as distinct conditions. **INFERENCE:** compatible; translated data meets §64–65 and is also versioned under §66. |
| DQI-C2 | Quality flags and lifecycle | `DATA-MAP.md` §69, §86 | `DEPRECATED` appears as a flag and in lifecycle discussion. Whether a flag can differ from a lifecycle state is not stated; deferred per `DEC-012`. |
| DQI-C3 | Release gates | `DATA-MAP.md` §117; `ENGINEERING-STANDARDS.md` ENG-C1 | One of four separate checklists, kept separate per `DEC-012`. |

---

# 3. Ingestion and Independence (§50–55)

**Ingestion (§50), a controlled operation:** (1) source verification; (2) license check; (3) file validation; (4) checksum calculation; (5) metadata registration; (6) optional preprocessing; (7) validation.

**Duplicates (§51):** duplicate or near-duplicate data can distort evaluations. Analysis is supported where appropriate; deduplication is versioned.

**Contamination (§52):** investigated where relevant: benchmark text in training data, reused during development, benchmark-derived tuning, accidental leakage between datasets.

**Leakage (§53):** documented. A benchmark is not treated as independent if its contents influenced the evaluated capability.

**Splits (§54–55):** development, validation and test where applicable, with strategy depending on the task. Temporal splits may be useful; temporal assumptions are documented.

**Research context (`R08` §69.3–69.4; `R07` §80.2):** no formal near-duplicate detection was found in RAID, MGTBench, M4 or DetectRL, and no n-gram or embedding-overlap contamination detection applied to named AI-detection benchmarks, as also recorded in `DETECTOR-VALIDATION-PROTOCOL.md`. `R-0087` documents benchmark-artifact contamination. Therefore a published benchmark must not be assumed free of duplicates or contamination (**INFERENCE**).

---

# 4. Representation and Quality (§56–60)

- **Multilingual balance (§56; `REQ-LANG-003`):** aggregated results must not conceal severe differences between languages. Reports include per-language results.
- **Representation (§57):** monitor whether the distribution reflects the intended research population. The language list is a scope decision, not evidence of real-world representation.
- **Quality (§58):** correctness, completeness, duplication, language accuracy, labeling quality, domain diversity, length distribution, provenance.
- **Labels (§59):** label source, annotation procedure, confidence where available, disagreements, unknown cases.
- **Unknown labels (§60):** remain explicit. Documents are not forced into a binary category to simplify processing.

---

# 5. Controls and Altered Text (§61–66)

- **Synthetic (§61):** clearly distinguished from naturally occurring data.
- **Human (§62):** provenance documented as accurately as possible; claims of human authorship must not exceed the available evidence.
- **Generated (§63):** generation metadata recorded; model families remain distinguishable.
- **Translated (§64):** labeled as translated. Translation can change lexical distributions, syntax, punctuation, discourse structure, detector behavior and watermark-related measurements.
- **Back-translated (§65):** a distinct experimental condition, not equivalent to the original text.
- **Augmentation (§66):** versioned; the distinction between original and augmented data is preserved.

---

# 6. Gates and Flags (§83–86, §116–117)

| Gate | Conditions | Section |
|---|---|---|
| Dataset becomes `ACTIVE` | Provenance known; licensing recorded; integrity verified; metadata exists; language information available where relevant; preprocessing documented; storage location known | §83 |
| Benchmark becomes `ACTIVE` | Contents versioned; evaluation methodology defined; leakage risks considered; licensing permits intended use; baseline results available where appropriate | §84 |
| Model becomes `ACTIVE` | Provenance known; format verified; license known; compatibility documented; loading behavior tested; security implications assessed | §85 |
| Relying on a dataset for a major claim | Provenance, licensing, integrity, language, domain, sample characteristics, contamination risk, preprocessing, version | §116 |
| Before a release | Required datasets and models available; manifests validate; checksums correct; licenses recorded; optional resources correctly marked; storage requirements known | §117 |

**Flags (§86):** `VERIFIED`, `PARTIALLY_VERIFIED`, `LANGUAGE_UNCERTAIN`, `LICENSE_UNCERTAIN`, `DUPLICATES_PRESENT`, `CONTAMINATION_RISK`, `EXTERNAL_TRANSFER_RESTRICTED`, `DEPRECATED`.

---

# 7. Automation and Drift (§88–89, §113)

**Automatic checks (§88), where practical:** checksums, file counts, size checks, encoding checks, language validation, duplicate detection, manifest validation, license metadata presence.

**Regression (§89):** for important corpora, compare document count, language distribution, length distribution, duplicate rate and metadata distribution after an update.

**Drift (§113):** for external or periodically updated datasets, monitor version, distribution, label, language and licensing changes. An update may require benchmark revalidation.

---

# 8. Claims (§112)

A dataset's limitations propagate into scientific claims. A result obtained only on short texts, one domain, synthetic data or one language must not automatically be generalized beyond those conditions.

---

# 9. Gaps

| ID | Gap | Would normally belong in |
|---|---|---|
| DQI-G1 | "Near-duplicate" and acceptable duplicate rates are undefined | Per-benchmark validation |
| DQI-G2 | The "intended research population" (§57) is undefined | `02-research` / owner |
| DQI-G3 | Language validation method (§88) is unselected | Implementation tranche |
| DQI-G4 | Train/test separation for detector benchmarks lacks research grounding (`TEST-AND-VERIFICATION-POLICY.md` TVP-G5) | `R08` |

No value has been supplied for any of these.

---

# 10. Coverage of the Parent Sections

| Parent sections | Covered in |
|---|---|
| §50–55 | §3 |
| §56–60 | §4 |
| §61–66 | §5 |
| §83–86, §116–117 | §6 |
| §88–89, §113 | §7 |
| §112 | §8 |
