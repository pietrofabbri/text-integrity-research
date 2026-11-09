# Data Identity and Metadata

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Data governance protocol (Tranche 1 of `DATA-MAP.md` §126)
**Authority:** Data (primary for data architecture, provenance and lifecycle, per `docs/99-backlog/DOCUMENT-AUTHORITY-MATRIX.md`). Runtime access to resources is in `docs/04-architecture/DATA-MODEL.md`.
**Parent:** `docs/07-data/DATA-MAP.md` §2–33, §73–78, §80–82
**Requirements basis:** `docs/03-scientific-specification/S02-scientific-requirements.md` `REQ-PROV-001`–`003`, `REQ-LANG-001`, `REQ-LANG-004`
**Research basis:** none specific to this tranche; no `R-XXXX` is needed for identification rules
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-009, DEC-012, DEC-051, DEC-052 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes how data is categorized, identified, versioned, traced and described. It selects no storage format, hash algorithm or Unicode normalization form, and sets no numeric value. No dataset manifest exists yet: everything here applies to data as it is acquired (§118).

---

# 2. Recorded Contradictions and Ambiguities — Not Resolved Here

| ID | Subject | Locations | Finding |
|---|---|---|---|
| DIM-C1 | Identifier categories | `DATA-MAP.md` §3, §12 | §12's structure is `DATA-[CATEGORY]-[SHORT-NAME]`, but its example `DATA-CORPUS-EN-001` uses `CORPUS`, which is not among §3's ten categories, and has an extra segment. §12 says the convention may evolve. |
| DIM-C2 | Retaining detector responses | `DATA-MAP.md` §32; `SECURITY-MAP.md` §12, §54 | §32 retains raw responses where legally permissible; the security map minimizes persistence. Recorded with `TRUST-AND-DATA-BOUNDARIES.md` TDB-C3, which is the same tension. |
| DIM-C3 | Unicode behavior | `DATA-MAP.md` §73–75; `SECURITY-MAP.md` §7 | §74 requires behavior to be explicitly defined for each listed case and no document defines it. §75 forbids silent discarding where interpretation could be affected. Until defined, no normalization may be treated as neutral (**INFERENCE**). |

---

# 3. Principle and Categories (§2–10)

**Principle (§2):** a result without identifiable data provenance is not fully reproducible. Every important result is traceable: data → version → preprocessing → experiment → result (`REQ-PROV-001`).

| Category (§3) | Rule | Section |
|---|---|---|
| `SOURCE_DATA` | Obtained externally, kept in original form where legally and technically possible; not silently modified. Raw evidence is kept separately from derived results (`REQ-PROV-002`) | §4 |
| `DERIVED_DATA` | Produced by a documented operation; identifies its parent dataset. Derived results identify their raw observations (`REQ-PROV-003`) | §5 |
| `BENCHMARK_DATA` | Membership is versioned; must not silently change between two evaluations | §6 |
| `TEST_DATA` | Synthetic, public, reduced, adversarial or regression fixtures; sensitive user data is not ordinary test data | §7 |
| `EXPERIMENT_DATA` | Inputs, controlled outputs, useful intermediates, detector observations, measurements, metadata; linked to its experiment identifier | §8 |
| `MODEL_ARTIFACT` | Local, tokenizer, embedding, language, classification and auxiliary models; each with provenance and version metadata | §9 |
| `LINGUISTIC_RESOURCE` | Dictionaries, frequency lists, morphological and segmentation resources, tokenizers, language identification, parsers, multilingual embeddings; specifies supported languages | §10 |
| `METADATA`, `RESULT_ARTIFACT`, `EXTERNAL_REFERENCE` | Named in §3; §11 covers metadata | §3, §11 |

---

# 4. Identity, Versions and Integrity (§11–15)

**Metadata (§11):** kept separately from large binaries where practical: identifier, version, source, license, language, domain, size, checksum, acquisition date, preprocessing, parent dataset, intended use, restrictions.

**Identifier (§12):** every important dataset or artifact has a stable identifier (see DIM-C1).

**Version (§13):** every dataset has an explicit version, changed whenever a change can affect scientific results: new or removed documents; changed labels, preprocessing, deduplication or language classification.

**Immutability (§14):** once used for a certified experiment a version is treated as immutable. Corrections create a new version, and historical results keep referencing the original.

**Checksums (§15):** where practical, cryptographic hashes for important datasets, archives, model files, benchmark packages and generated release artifacts.

---

# 5. Provenance and Preprocessing (§16–20)

**Each dataset documents (§16):** where it came from, who published it, how, when, which version and how it was processed.

**Chain (§17):** derived data forms a traceable chain, each step identifiable, for example source → cleaned → language-filtered → deduplicated → benchmark → experiment.

**Preprocessing (§18):** documented and versioned because it can influence results: Unicode and whitespace normalization, sentence segmentation, tokenization, language filtering, deduplication, HTML removal, markup normalization.

**Raw and processed (§19):** conceptually separate; a processed corpus is never implied to be identical to its source.

**Reversibility (§20):** where practical, keep enough metadata to understand what changed. Lossy processing is explicitly identified.

---

# 6. Language, Text and Authorship Metadata (§21–27)

- **Language (§21; `REQ-LANG-001`):** primary language, confidence if available, multilingual status, language distribution.
- **Target languages (§22; `REQ-LANG-004`):** English, Spanish, German, Japanese, French, Portuguese, Russian, Italian, Dutch, Polish, Turkish, Chinese, Indonesian. This does not assume equivalent quality in all languages.
- **Variants (§23):** distinguish language, script, regional variant, writing system and orthographic convention where relevant.
- **Length (§24):** distributions in characters, tokens, sentences, paragraphs and documents. Length is an experimental variable.
- **Domain (§25):** where feasible; not presented as objective if the labels are uncertain.
- **Author (§26):** where legally and scientifically appropriate, known human, synthetic, unknown or mixed. Sensitive personal information is not unnecessarily retained.
- **Authorship labels (§27):** research metadata, not universal ground truth. A label such as `HUMAN` or `AI_GENERATED` includes how it was established.

---

# 7. Generation, Transformation and Detector Metadata (§28–33)

- **Synthetic text (§28):** model family and version, generation configuration, date, prompt provenance where appropriate, generation procedure. Missing metadata is marked unknown, not guessed.
- **Transformations (§29):** identifier, version, configuration, input and output datasets, language, timestamp, validation results. The original source remains identifiable.
- **Watermark data (§30):** family, implementation, generation model, configuration, text source, language, length, status if known, detector methodology, version. Experimentally embedded or suspected watermarks are distinguished from independently verified status.
- **Detector data (§31):** identifier, provider, version, interface, date, language, input characteristics, result, threshold, configuration. External results are observations, not universal authorship truth.
- **Detector results (§32):** where legally permissible, raw response, normalized result, request metadata and error information. Otherwise enough metadata to interpret the normalized result (see DIM-C2).
- **External services (§33):** service, purpose, timestamp, configuration, data category and returned result. Text is never transmitted silently.

---

# 8. Text Handling (§73–78)

- **Formats (§73):** open and well-supported where practical; textual data uses explicit encoding; Unicode handling is deterministic and documented.
- **Unicode (§74):** behavior is explicitly defined for normalization, combining characters, invisible characters, bidirectional controls, homoglyphs and zero-width characters (see DIM-C3).
- **Unicode security (§75):** invisible or control characters are not silently discarded if doing so could affect scientific interpretation; any removal or change is documented.
- **Scripts (§76):** distinguished where relevant, such as Latin, Cyrillic, Han, Kana, mixed-script.
- **Encoding errors (§77):** reported. Silent replacement is discouraged.
- **Canonicalization (§78):** a transformation, not an invisible detail; its version is recorded when it can affect evaluation.

---

# 9. Manifests and Compatibility (§80–82)

**Dataset manifest (§80):** dataset ID, version, source, license, languages, size, checksum, preprocessing, storage location, status.

**Model manifest (§81):** model ID, version, source, license, format, size, checksum, supported languages, intended use, status.

**Compatibility (§82):** runtime version, tokenizer version, language and model family where relevant. Incompatible resources fail clearly.

---

# 10. Gaps

| ID | Gap | Would normally belong in |
|---|---|---|
| DIM-G1 | The identifier convention needs settling (DIM-C1) | `DATA-MAP.md`, by decision |
| DIM-G2 | Unicode behaviors of §74 are undefined | Specification before ingestion |
| DIM-G3 | No manifests or data cards exist | Implementation tranche |
| DIM-G4 | The manifest format is not selected | Implementation tranche |

No value has been supplied for any of these.

---

# 11. Coverage of the Parent Sections

| Parent sections | Covered in |
|---|---|
| §2–10 | §3 |
| §11–15 | §4 |
| §16–20 | §5 |
| §21–27 | §6 |
| §28–33 | §7 |
| §73–78 | §8 |
| §80–82 | §9 |
