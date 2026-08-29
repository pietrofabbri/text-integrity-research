# R08 — Benchmark and Dataset Research

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Scientific research domain
**Parent:** docs/02-research/RESEARCH-MAP.md
**Methodology:** docs/02-research/R01-literature-research-methodology.md

---

# 1. Purpose

This document defines research requirements for selecting, constructing,
evaluating and maintaining datasets and benchmarks.

---

# 2. Fundamental Principle

A benchmark is a measurement instrument.

Its existence does not guarantee that it measures the intended scientific
property correctly.

---

# 3. Dataset Categories

Potential datasets include:

- human-written text;
- generated text;
- human-edited generated text;
- mixed-origin text;
- watermarked text;
- non-watermarked generated text;
- transformed text;
- translated text;
- adversarially modified text.

---

# 4. Dataset Provenance

Record:

- source;
- creator;
- publication;
- collection methodology;
- date;
- licensing;
- transformations;
- known limitations.

---

# 5. Dataset Version

Every important dataset must have a version identifier.

---

# 6. Integrity

Where feasible, maintain:

- checksums;
- manifests;
- file counts;
- metadata validation.

---

# 7. Licensing

Every external dataset must have its permitted-use status assessed.

---

# 8. Data Minimization

The project should avoid storing unnecessary copies of large datasets.

---

# 9. Local Storage Constraint

The complete local project data environment should target a maximum of
approximately 30 GB.

This is an engineering constraint and may be revised through the project
decision process.

---

# 10. External Resources

Large public resources may be referenced through:

- manifests;
- download instructions;
- checksums;
- reproducible acquisition procedures.

---

# 11. GitHub Resources

GitHub repositories may be used as research resources where appropriate.

Repository availability does not guarantee scientific validity or permanence.

---

# 12. Benchmark Purpose

Every benchmark must have an explicit purpose.

Examples:

- watermark detection;
- AI detection;
- semantic preservation;
- linguistic preservation;
- robustness;
- multilingual evaluation.

---

# 13. Benchmark Population

Define the population represented by the benchmark.

---

# 14. Language Coverage

Record:

- languages;
- proportions;
- scripts;
- language-generation methodology.

---

# 15. Domain Coverage

Record relevant domains and genres.

---

# 16. Length Distribution

Record document-length distribution.

---

# 17. Author Distribution

Where relevant, record author diversity.

---

# 18. Model Distribution

For generated text, record generation models and versions.

---

# 19. Prompt Distribution

Where relevant, record prompt methodology.

---

# 20. Generation Parameters

Record generation parameters where available.

---

# 21. Human Editing

Record whether generated documents were edited by humans.

---

# 22. Annotation

Record:

- annotation methodology;
- annotator population;
- agreement;
- quality control.

---

# 23. Ground Truth

Ground truth must be explicitly defined.

---

# 24. Ground Truth Uncertainty

Ambiguous documents should not be silently assigned a definitive label.

---

# 25. Class Balance

Record class distributions.

---

# 26. Sampling

Document sampling methodology.

---

# 27. Selection Bias

Investigate whether dataset construction introduces selection bias.

---

# 28. Publication Bias

Where the benchmark is derived from published material, consider publication
bias.

---

# 29. Contamination

Investigate possible overlap with:

- model training;
- detector training;
- benchmark tuning;
- public benchmark releases.

---

# 30. Deduplication

Duplicate or near-duplicate documents should be identified.

---

# 31. Train/Validation/Test Separation

Maintain clear separation where applicable.

---

# 32. Test Set Protection

The final test set should not be repeatedly used for optimization.

---

# 33. Holdout

Where practical maintain a genuinely held-out evaluation set.

---

# 34. Temporal Splits

Temporal splits may be useful for evaluating distribution shift.

---

# 35. Domain Splits

Domain-specific holdouts may be useful for generalization testing.

---

# 36. Language Splits

Language-specific holdouts may be useful where data permits.

---

# 37. Author Splits

Author-disjoint splits may be necessary for some research questions.

---

# 38. Prompt Splits

For generated text, prompt-disjoint evaluation may be useful.

---

# 39. Model Splits

Testing on models not used during development can measure generalization.

---

# 40. Benchmark Leakage

Benchmark leakage must be treated as a scientific validity risk.

---

# 41. Benchmark Aging

Benchmarks can become obsolete.

Reasons include:

- new generation models;
- new detectors;
- new watermark methodologies;
- changed linguistic distributions.

---

# 42. Benchmark Refresh

A benchmark may require periodic refresh.

---

# 43. Benchmark Versioning

A refreshed benchmark should receive a new version.

Historical results must remain associated with the old version.

---

# 44. Benchmark Comparability

Results across benchmark versions must not automatically be treated as
directly comparable.

---

# 45. Benchmark Metrics

Every benchmark should define:

- primary metrics;
- secondary metrics;
- aggregation;
- uncertainty;
- acceptance criteria where applicable.

---

# 46. Multilingual Benchmark

A multilingual benchmark should preserve language-level results.

A single aggregate score is insufficient.

---

# 47. Worst-Case Language

Where appropriate report worst-case language performance.

---

# 48. Macro and Micro Aggregation

Consider both macro-averaged and micro-averaged results.

---

# 49. Human Controls

Human controls must be representative of the intended population.

---

# 50. AI Controls

Generated controls must be produced under documented conditions.

---

# 51. Watermarked Controls

Watermarked controls must record watermark methodology and relevant
generation conditions.

---

# 52. Transformation Controls

Transformed datasets must preserve the identity of their source material.

---

# 53. Pairing

Where input/output comparisons are required, preserve exact pairing.

---

# 54. Provenance Chain

A transformed document should be traceable:

SOURCE
→ TRANSFORMATION
→ OUTPUT
→ EVALUATION

---

# 55. Immutable Source

Original source material should be preserved when legally and technically
possible.

---

# 56. Transformation Manifest

Record transformation operations applied to derived datasets.

---

# 57. Dataset Reproducibility

Where practical, derived datasets should be reconstructible from source data
and transformation manifests.

---

# 58. Dataset Quality Checks

Automated checks should detect:

- missing files;
- duplicate IDs;
- malformed text;
- invalid encodings;
- missing labels;
- inconsistent metadata;
- broken provenance.

---

# 59. Unicode Validation

Multilingual datasets require Unicode integrity checks.

---

# 60. Encoding Validation

Encoding problems must be detected before scientific evaluation.

---

# 61. Language Validation

Dataset language labels should be checked where practical.

---

# 62. Length Validation

Unexpected document-length distributions should trigger review.

---

# 63. Metadata Integrity

Metadata must remain synchronized with dataset content.

---

# 64. Dataset Change Control

Material dataset changes require a new version or explicit change record.

---

# 65. Dataset Retirement

Obsolete datasets may be retired.

Historical results remain preserved.

---

# 66. Benchmark Retirement

A benchmark may be retired when it no longer provides meaningful evidence.

---

# 67. Research Outputs

This area should produce:

- dataset registry;
- benchmark registry;
- provenance methodology;
- contamination methodology;
- benchmark validity assessments;
- dataset quality standards.

---

# 68. Final Principle

A benchmark is only as useful as the validity of the measurement it enables.

---

# 69. Literature Findings (2026-08-24)

Populates §3-§67 above, concentrated on dataset/benchmark ENGINEERING AND
GOVERNANCE practice specifically — licensing, storage footprint,
deduplication, contamination-detection methodology, and lifecycle
practice — rather than re-cataloging which benchmarks exist (already
covered across R02-R07). Every claim is registered in
`docs/00-project/RESEARCH-REGISTRY.md` under the cited `R-XXXX`
identifier. Confidence markers follow the R04 §39 convention. This is a
first literature pass, not a claim of research completeness.

## 69.1 Licensing and Legal Distributability — Populated, Directly Answers Part of Q-007

Addresses §7 (Licensing) and Q-007 (OPEN-QUESTIONS.md, "which datasets
can be legally distributed within the project"):

- Confirmed licenses: RAID MIT (R-0020), HC3 CC-BY-SA-4.0 with a
  source-inheritance clause (R-0016), MULTITuDE/v2 CC-BY-4.0 (R-0049),
  ARB Apache-2.0 (R-0088).
- **Not found / not stated**: M4 and DetectRL do not state a license
  anywhere checked in this pass — this is recorded as "no evidence
  found," not as "unlicensed."
- **The clearest documented governance pattern**: a benchmark's own
  stated license often does not settle distributability, because the
  benchmark's *source corpora* may carry stricter or unstated terms.
  ARB's own paper explicitly discloses this per-source (XSum undeclared,
  WritingPrompts MIT, OpenWebText CC0) and disclaims responsibility for
  downstream redistribution of those inputs even while stating its own
  Apache-2.0 license. HC3's license explicitly inherits the *stricter* of
  its own license or any source dataset's license. **This project should
  not treat a benchmark's top-line license as sufficient evidence of
  distributability without checking its source-corpus chain.**
- **A concrete non-open case**: the ETS Corpus of Non-Native Written
  English (LDC2014T06, R-0099) — the officially licensed TOEFL-essay
  corpus — is gated behind LDC membership/fee, not freely redistributable.

## 69.2 Storage Footprint — Populated, Inconsistently Published

Addresses §9 (Local Storage Constraint, ~30GB target, KB-007): RAID
16.7GB (R-0020), HC3 147MB (R-0016), MULTITuDE 44.7GB (v1) / 29.8GB (v2)
(R-0049, AUTHOR-REPORTED and unusually large for text data — flagged, not
verified). MGTBench, M4, DetectRL, WaterBench do not publish GB figures
in any surface checked. **This is itself a finding**: exact storage
footprint is inconsistently documented across the field, not merely
something this pass failed to locate — worth noting for §67 (Research
Outputs, dataset quality standards) as a documentation gap the project
should not repeat in its own registry.

## 69.3 Deduplication Methodology — Confirmed Gap

Addresses §30 (Deduplication): **no evidence found** of formal
MinHash/LSH-style near-duplicate detection in any named AI-detection
benchmark paper (RAID, MGTBench, M4, DetectRL). The only concrete data
point found is ARB's (R-0088) 0.01% exact-duplicate rate, explicitly
retained rather than removed. General-purpose tooling exists and is
directly applicable (`text-dedup`, R-0101) but no evidence was found that
any named benchmark actually used it — in contrast to general LLM
pretraining-corpus practice, where such deduplication is now standard.

## 69.4 Contamination Detection — Populated

Addresses §29 (Contamination): a general LLM-contamination-detection
taxonomy exists (R-0098: n-gram overlap, membership inference, embedding/
perplexity comparison) but is explicitly scoped to general LLM eval, not
AI-detection benchmarks specifically. The one AI-detection-benchmark-
specific contamination study found (R-0087, updated this pass with
methodology detail: regex/pattern-matching plus SHAP explainability plus
adversarial spoofing) addresses artifact/shortcut contamination
(detectors learning generation boilerplate as a signal), a different
failure mode from classic n-gram/embedding train-test overlap. **No
evidence found** of n-gram or embedding-overlap contamination detection
having actually been applied to any named AI-detection benchmark.

## 69.5 Benchmark Versioning and Refresh — One Real Example Found

Addresses §41-44 (Benchmark Aging, Refresh, Versioning, Comparability):
MULTITuDE → MULTITuDEv2 (R-0049, updated) is a real, dated (2023-10 →
2024-09-27) benchmark refresh with a stated rationale (adding 10
authorship-obfuscation methods). RAID's `raid-bench` package has frequent
releases, but these are confirmed to be software/tooling releases, not
dataset content refreshes — do not conflate the two (a distinction worth
preserving carefully, since §43 requires historical results to remain
associated with the correct version). RAID's paper states an *intent* to
release updated versions but no evidence was found that a new-generator
dataset refresh has shipped. M4's lineage into M4GT-Bench/SemEval-2024
Task 8 functions as a new benchmark built on the original's methodology
rather than an in-place refresh.

## 69.6 Dataset Quality-Check Tooling and Documentation Standards — Populated

Addresses §58-63 (Dataset Quality Checks, Unicode/Encoding/Language/
Length/Metadata Validation): no AI-detection-specific automated QA tool
was found. Two established, adoptable governance templates exist —
Datasheets for Datasets and Data Statements for NLP (R-0100) — directly
relevant as a format the project's own R08 §4/§22 provenance
documentation could follow rather than invent from scratch. `ftfy`
(encoding-repair tool) and `text-dedup` (R-0101) are general-purpose
candidates for §59-60 (Unicode/Encoding Validation) and §30
(Deduplication) respectively. ARB's (R-0088) practice of flagging and
*retaining* (rather than silently dropping) 0.67% of problematic
generated texts is a concrete, citable example of the transparency-over-
silent-curation principle this project should itself follow.

## 69.7 Human-Subject and Ethics Considerations — Populated, Governance Gap Found

Addresses §22 (Annotation) and the human-text-provenance concern
underlying §49 (Human Controls): the field's most-cited detector-bias
study (R-0022, Liang et al., updated this pass) used TOEFL essays scraped
from a Chinese educational forum rather than the officially licensed
ETS/LDC corpus (R-0099), with no ethics/IRB/consent statement found in
the paper. **No evidence found** of any reviewed AI-detection benchmark
paper (RAID, MGTBench, M4, HC3, MULTITuDE, DetectRL, ARB) including a
formal IRB approval or consent statement for its human-written-text
components, beyond citing a source corpus's own license. This is recorded
as a documented governance gap in the field's own practice, not a
challenge to any finding's validity — but it directly informs how this
project should document (and better document than the field average) its
own human-text sources under R08 §4/§22.

## 69.8 Items Requiring Follow-Up Before Being Treated as Established

1. MULTITuDE's stated GB figures (44.7GB v1 / 29.8GB v2) are unusually
   large for text corpora and have not been cross-checked against the
   paper's own document/token counts.
2. MGTBench's license (reported as MIT per the GitHub repo page) could
   not be independently confirmed against the actual LICENSE file text
   in this pass (a direct raw-file fetch returned 404) — treat as
   UNVERIFIED pending direct confirmation.
3. A general survey potentially relevant to §69.1 ("A large-scale audit
   of dataset licensing and attribution in AI," Nature Machine
   Intelligence, 2024) was identified but not read in this pass — its
   relevance and specific claims are unconfirmed.
4. R-0087's exact relationship to any future DetectRL-contamination
   source should be checked before registering further sources on this
   topic, to avoid duplicate registry entries — this pass already merged
   what would have been a duplicate into R-0087's existing entry rather
   than creating a new one.