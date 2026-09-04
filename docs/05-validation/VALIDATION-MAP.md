# Validation Map

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Validation architecture and scientific evaluation map
**Authority:** Validation
**Scope:** Experimental validation, software validation, multilingual
validation, integrity validation, detector/watermark measurement and
regression

---

## 1. Purpose

This document defines how the project determines whether a capability,
transformation, experiment or release satisfies its declared requirements.

Validation must distinguish between:

- scientific evidence;
- software correctness;
- measurement correctness;
- transformation integrity;
- detector observations;
- research hypotheses;
- operational readiness.

No single metric or external detector constitutes universal ground truth.

---

# 2. Fundamental Validation Principle

A result is valid only relative to:

- a defined objective;
- a defined population or corpus;
- a defined language;
- a defined methodology;
- a defined measurement;
- a defined version;
- a defined acceptance criterion.

Therefore:

VALIDATED

does not mean:

UNIVERSALLY TRUE

It means:

VALIDATED UNDER THE DECLARED CONDITIONS.

---

# 3. Validation Domains

The project uses several independent validation domains:

1. software validation;
2. input/output integrity;
3. semantic preservation;
4. factual preservation;
5. structural preservation;
6. linguistic quality;
7. minimality;
8. multilingual behavior;
9. watermark analysis;
10. AI-generation assessment;
11. robustness;
12. reproducibility;
13. resource behavior;
14. regression;
15. release certification.

---

# 4. Validation Hierarchy

Validation should proceed from lower-level guarantees to higher-level
scientific conclusions.

Recommended hierarchy:

SOFTWARE CORRECTNESS
→ DATA CORRECTNESS
→ COMPONENT CORRECTNESS
→ PIPELINE CORRECTNESS
→ INTEGRITY VALIDATION
→ SCIENTIFIC EVALUATION
→ RELEASE CERTIFICATION

A failure at a lower level invalidates conclusions dependent on it.

---

# 5. Software Correctness

Software correctness tests include:

- unit tests;
- integration tests;
- schema tests;
- serialization tests;
- configuration tests;
- dependency tests;
- error-handling tests;
- deterministic behavior tests where applicable.

Software correctness does not establish scientific effectiveness.

---

# 6. Data Correctness

Datasets must be validated for:

- encoding;
- corruption;
- duplicates;
- missing data;
- language labels;
- metadata consistency;
- licensing;
- provenance;
- version integrity.

Dataset changes must be detectable.

---

# 7. Dataset Versioning

Every benchmark dataset must have:

- unique identifier;
- version;
- source;
- acquisition date;
- license;
- language distribution;
- domain distribution;
- text-length distribution;
- preprocessing description;
- checksum where appropriate.

A scientific result must identify the dataset version used.

---

# 8. Train/Test Separation

Where machine-learning components are involved, evaluation data must be
appropriately separated from development or training data.

Potential leakage must be investigated.

A detector or transformation system must not be evaluated on data that has
directly influenced its development without explicit disclosure.

---

# 9. Test Corpus Design

Evaluation corpora should cover relevant variation in:

- language;
- domain;
- author style;
- document length;
- register;
- complexity;
- formatting;
- punctuation;
- vocabulary;
- technical terminology.

A single homogeneous corpus is insufficient for broad claims.

---

# 10. Multilingual Validation

Each target language must be evaluated independently.

Initial target languages:

1. English
2. Spanish
3. German
4. Japanese
5. French
6. Portuguese
7. Russian
8. Italian
9. Dutch
10. Polish
11. Turkish
12. Chinese
13. Indonesian

Results must not be aggregated in a way that hides poor performance in an
individual language.

---

# 11. Language Capability Matrix

Validation should maintain a matrix similar to:

| Language | Analysis | Transformation | Integrity | Watermark Analysis | AI Assessment | Status |
|----------|----------|-----------------|-----------|--------------------|---------------|--------|

Each cell should have its own evidence.

---

# 12. Input/Output Integrity

For every transformation experiment, the system must preserve:

- original input;
- output;
- structured diff;
- transformation metadata;
- validation results.

The original input must never be reconstructed from the output.

---

# 13. Semantic Preservation

Semantic preservation must be evaluated independently from surface similarity.

Possible measurements include:

- textual entailment;
- contradiction detection;
- semantic similarity;
- structured fact comparison;
- human evaluation where scientifically justified.

Multiple complementary metrics are preferable to one universal metric.

**Cross-reference:** the requirement-ID-level definition of this dimension
is `S04-fidelity-requirements.md` § 4, FID-001 — Semantic Preservation.
Added 2026-08-29 per the Q001 cross-area audit
(`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §4S).

---

# 14. Semantic Acceptance

A candidate should not be accepted merely because a similarity score exceeds
a threshold.

Acceptance should consider:

- meaning preservation;
- contradictions;
- changed claims;
- changed modality;
- changed negation;
- changed conditions;
- changed causal relationships.

High lexical similarity does not guarantee semantic equivalence.

---

# 15. Factual Preservation

Validation must explicitly compare factual elements.

At minimum, where applicable:

- numbers;
- dates;
- times;
- units;
- percentages;
- names;
- organizations;
- locations;
- references;
- identifiers;
- URLs.

Unexpected factual modifications must be flagged.

**Cross-reference:** the requirement-ID-level definition of this dimension
is `S04-fidelity-requirements.md` § 6, FID-003 — Factual Preservation.
Added 2026-08-29 per the Q001 cross-area audit
(`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §4S).

---

# 16. Numerical Integrity

Numerical values require special treatment.

Validation should distinguish:

- exact equality;
- mathematically equivalent representation;
- unit conversion;
- rounding;
- changed value.

A transformation must not silently convert a factual change into a formatting
difference.

---

# 17. Entity Integrity

Named entities should be compared where reliably extractable.

Relevant entity classes include:

- people;
- organizations;
- places;
- products;
- institutions;
- events.

Entity substitutions require explicit handling.

---

# 18. Structural Integrity

Validation must compare document structure.

Potential elements:

- paragraph count;
- headings;
- list structure;
- table structure;
- quotation boundaries;
- references;
- markup;
- formulas;
- code blocks.

Structural changes must be intentional and measurable.

**Cross-reference:** the requirement-ID-level definition of this dimension
is `S04-fidelity-requirements.md` § 19, FID-016 — Structural Preservation.
Added 2026-08-29 per the Q001 cross-area audit
(`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §4S).

---

# 19. Linguistic Quality

Linguistic validation may assess:

- grammar;
- spelling;
- fluency;
- coherence;
- register;
- terminology;
- punctuation;
- language-specific conventions.

Quality metrics must be language-aware.

---

# 20. Minimality

Minimality must be measured independently.

Possible metrics:

- character edit distance;
- token edit distance;
- changed-token ratio;
- changed-sentence ratio;
- lexical substitution rate;
- structural change rate;
- semantic deviation.

No single metric should define minimality universally.

**Cross-reference:** the requirement-ID-level definition of this dimension
is `S04-fidelity-requirements.md` § 24, FID-021 — Minimality, and
`S05-transformation-requirements.md` § 11, TRN-007 — Minimal Intervention.
Added 2026-08-29 per the Q001 cross-area audit
(`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §4S).

---

# 21. Transformation Budget

Where applicable, experiments may define a transformation budget.

Possible dimensions:

- maximum changed tokens;
- maximum changed sentences;
- maximum structural changes;
- maximum semantic deviation.

Budgets must be versioned.

---

# 22. Watermark Measurement

Watermark-related experiments should measure the behavior of known watermark
mechanisms or detectors under explicitly defined conditions.

An experiment must record:

- watermark family;
- implementation;
- version;
- configuration;
- language;
- corpus;
- text length;
- transformation;
- measurement;
- uncertainty.

The measurement is an observation, not a universal truth.

---

# 23. Watermark Families

The research registry should classify watermark mechanisms by relevant
properties.

Potential dimensions include:

- generation-time vs post-generation;
- token-level vs semantic;
- statistical vs cryptographic;
- model-dependent vs model-independent;
- visible vs latent;
- local vs contextual;
- robust vs fragile under transformation.

The classification must be updated when research identifies new categories.

---

# 24. Detector Registry

Every detector used for research must have a registry entry.

Minimum fields:

- detector ID;
- provider;
- version;
- interface;
- language coverage;
- input constraints;
- output format;
- score interpretation;
- threshold;
- limitations;
- date tested;
- reproducibility status.

---

# 25. Detector Independence

Where multiple detectors are used, results must remain separate.

The system should not automatically convert:

Detector A = positive
Detector B = negative

into:

overall = uncertain

without recording the original observations.

Aggregation logic must be explicit and versioned.

---

# 26. Cloud Detector Validation

External detector services may be used as measurement instruments.

For every request, record where possible:

- service;
- endpoint or product;
- version;
- request configuration;
- timestamp;
- language;
- text length;
- returned score;
- returned classification;
- errors.

Cloud results should be treated as observations from a changing external
system.

---

# 27. Detector Drift

External detectors may change without notice.

The project should periodically evaluate:

- score distribution;
- threshold behavior;
- language behavior;
- response format;
- API behavior.

A detector update may invalidate direct comparisons with earlier results.

---

# 28. Watermark/Detector Experiment Design

Experiments should use controlled comparisons.

Example structure:

BASELINE
→ CONTROLLED TRANSFORMATION
→ MEASURE

rather than uncontrolled modification.

Where multiple transformations are compared, the experimental design should
control for:

- text;
- language;
- length;
- domain;
- transformation magnitude.

---

# 29. Paired Evaluation

Whenever possible, compare the same source text before and after a
controlled transformation.

This reduces variance caused by corpus differences.

Paired measurements should retain the source/output relationship.

---

# 30. Control Groups

Research experiments should use appropriate controls.

Possible controls include:

- unchanged text;
- naturally human-edited text;
- independently generated text;
- standardized transformations;
- randomly selected corpus controls.

The exact control design depends on the research question.

---

# 31. Confounding Factors

Experiments must consider possible confounders such as:

- text length;
- language;
- domain;
- formatting;
- translation;
- spelling quality;
- punctuation;
- author style;
- topic;
- model family;
- detector version.

A detector result cannot automatically be attributed to the transformation
being studied.

---

# 32. Statistical Validation

Where sample size permits, report:

- sample size;
- central tendency;
- variance;
- confidence intervals where appropriate;
- effect size;
- statistical test;
- assumptions;
- missing observations.

Statistical significance must not be confused with practical significance.

---

# 33. Repeated Experiments

Stochastic components should be evaluated over multiple runs when relevant.

Record:

- seed;
- number of runs;
- configuration;
- model version;
- aggregation method.

Single-run results must be identified as such.

---

# 34. Human Evaluation

Human evaluation may be used for properties that automated metrics cannot
adequately capture.

Potential criteria:

- semantic equivalence;
- grammaticality;
- naturalness;
- coherence;
- stylistic consistency.

Human evaluation must specify:

- evaluator population;
- instructions;
- sample size;
- scoring scheme;
- blinding;
- aggregation.

---

# 35. Blind Evaluation

Where practical, evaluators should not know which experimental condition
produced a text.

This reduces confirmation bias.

---

# 36. Evaluation Against AI Detectors

AI detector results may be included as research measurements.

They must not be treated as definitive evidence of authorship.

A detector classification should therefore be represented as:

OBSERVATION

rather than:

GROUND TRUTH.

---

# 37. Negative Results

Negative results are first-class scientific results.

The system must retain experiments that show:

- no effect;
- inconsistent effect;
- detector disagreement;
- language degradation;
- unexpected semantic changes;
- insufficient robustness.

Negative findings must not be automatically discarded.

---

# 38. Failed Experiments

A failed experiment should record:

- hypothesis;
- configuration;
- expected outcome;
- actual outcome;
- failure reason;
- affected components;
- reproducibility information.

Failed experiments may prevent incorrect future assumptions.

---

# 39. Regression Testing

Every validated capability requires regression tests.

Regression tests must detect:

- functional regressions;
- semantic regressions;
- factual regressions;
- language regressions;
- structural regressions;
- performance regressions;
- resource regressions.

---

# 40. Scientific Regression

Scientific regression is distinct from software regression.

A software update can pass every unit test while changing scientific behavior.

Therefore benchmark results must be compared across relevant releases.

---

# 41. Baseline Management

Every major capability should have a baseline.

A baseline consists of:

- software version;
- capability versions;
- dataset;
- configuration;
- metrics;
- results.

New results should be compared against the appropriate baseline.

---

# 42. Reproducibility

An experiment should be reproducible from its recorded metadata.

At minimum:

- experiment ID;
- software version;
- configuration;
- dataset version;
- language;
- capability versions;
- model versions;
- random seed where applicable;
- detector version where applicable.

---

# 43. Reproducibility Classes

Experiments may be classified as:

- FULLY_REPRODUCIBLE
- LOCALLY_REPRODUCIBLE
- CONDITIONALLY_REPRODUCIBLE
- EXTERNALLY_DEPENDENT
- NON_REPRODUCIBLE

External services may make exact reproduction impossible.

This limitation must be explicit.

---

# 44. Acceptance Thresholds

Thresholds must be justified by:

- research evidence;
- benchmark distributions;
- domain requirements;
- error costs;
- statistical analysis.

Arbitrary thresholds must not be presented as scientific facts.

---

# 45. Threshold Versioning

Every threshold must have:

- identifier;
- version;
- rationale;
- source;
- date;
- affected capabilities;
- affected languages;
- replacement history.

Changing a threshold may change certification status.

---

# 46. Confidence

Validation results should distinguish:

- pass;
- fail;
- inconclusive;
- unavailable.

Where a probability or confidence score exists, its meaning must be
documented.

---

# 47. Uncertainty Propagation

Where possible, uncertainty should propagate through the evaluation pipeline.

A highly uncertain analytical result should not become a definitive
downstream conclusion merely because the system converts it to a Boolean.

---

# 48. Robustness Testing

Robustness experiments may test controlled changes such as:

- punctuation;
- spelling;
- formatting;
- sentence boundaries;
- translation;
- back-translation;
- editing;
- length changes.

The transformation under study must be clearly defined.

---

# 49. Distribution Shift

Validation should consider whether results generalize across:

- domains;
- authors;
- text lengths;
- languages;
- topics;
- document types.

A result obtained on one narrow corpus must not automatically generalize
to all text.

---

# 50. Longitudinal Validation

Important capabilities should be evaluated over time where practical.

This is particularly relevant for:

- external detectors;
- watermark implementations;
- language models;
- cloud services;
- changing datasets.

Historical measurements should remain available.

---

# 51. External Service Failure

If an external detector is unavailable:

- local experiments must continue where possible;
- the missing measurement must be marked unavailable;
- results must not be fabricated;
- certification profiles requiring that detector must fail or become
  conditional according to their declared rules.

---

# 52. Offline Validation

The project must maintain an offline validation suite for core behavior.

Offline validation should cover:

- integrity;
- structural comparison;
- semantic validation where locally supported;
- deterministic checks;
- regression;
- configuration;
- resource limits.

---

# 53. Resource Validation

The validation system should measure:

- disk usage;
- memory;
- CPU;
- GPU usage where applicable;
- execution time;
- cache growth.

The project target is to remain within the defined storage budget unless
explicitly revised.

---

# 54. Security Validation

Security validation should cover:

- untrusted input;
- malformed files;
- dependency integrity;
- downloaded artifacts;
- external-service boundaries;
- temporary-file handling;
- sensitive logging.

Security validation is documented in greater detail in the security
documentation.

---

# 55. Capability Validation Gate

A capability may progress from EXPERIMENTAL to VALIDATED only when:

1. its objective is defined;
2. its inputs and outputs are defined;
3. its evidence is documented;
4. its benchmark is defined;
5. its metrics are defined;
6. its limitations are known;
7. its regression tests exist;
8. its dependencies are documented;
9. its reproducibility status is known.

**Cross-reference:** `docs/10-certification/CERTIFICATION-MAP.md` § 3
"Certification Levels" defines a related but non-identical vocabulary
(`UNTESTED, EXPERIMENTAL, VALIDATED, CERTIFIED, DEPRECATED, RETIRED`) for
what appears to be the same underlying concept as this section's
`NOT_EVALUATED, EXPERIMENTAL, CONDITIONALLY_VALIDATED, VALIDATED,
DEGRADED, DEPRECATED, RETIRED`. Shared: `EXPERIMENTAL`, `VALIDATED`,
`DEPRECATED`, `RETIRED`. Divergent: `NOT_EVALUATED` vs. `UNTESTED`;
`CONDITIONALLY_VALIDATED`/`DEGRADED` (validation-only); `CERTIFIED`
(certification-only). Neither has been reconciled with the other; which
one is authoritative is a HUMAN DECISION REQUIRED item — see
`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §5S/§13S.
Added 2026-08-29.

---

# 56. Release Validation

A release should be validated against a declared evaluation profile.

The profile specifies:

- required capabilities;
- supported languages;
- datasets;
- benchmarks;
- thresholds;
- detector versions where applicable;
- mandatory regression tests;
- resource constraints.

---

# 57. Release Status

Recommended release states:

- NOT_EVALUATED
- EXPERIMENTAL
- CONDITIONALLY_VALIDATED
- VALIDATED
- DEGRADED
- DEPRECATED
- RETIRED

---

# 58. Certification Boundary

Validation determines evidence.

Certification determines whether the evidence satisfies a declared release
profile.

These must remain separate.

---

# 59. Evidence Package

A certification evidence package should contain:

- software version;
- capability registry snapshot;
- dataset versions;
- model versions;
- evaluation profiles;
- benchmark results;
- regression results;
- known failures;
- known limitations;
- external-service observations;
- reproducibility information.

---

# 60. Scientific Claim Registry

Major claims should have traceable identifiers.

For each claim record:

- claim;
- evidence;
- dataset;
- methodology;
- date;
- confidence;
- limitations;
- status.

Claims should be updated when new evidence contradicts or weakens them.

---

# 61. Claim Lifecycle

Claims may move through:

PROPOSED
→ INVESTIGATED
→ SUPPORTED
→ VALIDATED
→ CHALLENGED
→ REVISED
→ RETIRED

Scientific claims must not become permanent simply because they once passed
a benchmark.

---

# 62. New Research Integration

When new research identifies:

- a new watermark;
- a new detector;
- a new language phenomenon;
- a new evaluation methodology;
- a new failure mode;

the validation system must be able to add a corresponding experiment without
redesigning the entire validation framework.

---

# 63. Obsolete Methodologies

A validation method may be deprecated when:

- better methodology becomes available;
- detector becomes unavailable;
- benchmark becomes invalid;
- assumptions are disproven;
- reproducibility becomes impossible.

Historical results must remain identifiable as having used the old method.

---

# 64. Validation Change Process

A validation change must record:

1. reason;
2. scientific evidence;
3. affected requirements;
4. affected benchmarks;
5. affected thresholds;
6. affected capabilities;
7. compatibility impact;
8. certification impact.

---

# 65. Validation Reports

Reports should distinguish:

- raw measurements;
- derived metrics;
- acceptance decisions;
- scientific interpretation.

The system must not hide raw measurements behind a single summary score.

---

# 66. Minimum Experiment Record

Every formal experiment should have:

- experiment ID;
- hypothesis;
- objective;
- input corpus;
- language;
- control;
- experimental condition;
- software version;
- capability versions;
- configuration;
- metrics;
- results;
- uncertainty;
- conclusion;
- limitations.

---

# 67. Minimum Transformation Record

Every controlled transformation should record:

- source identifier;
- transformation identifier;
- transformation version;
- configuration;
- language;
- candidate output;
- changed regions;
- integrity results;
- minimality results;
- linguistic results;
- evaluation observations.

---

# 68. No Silent Scientific Changes

A software update must not silently alter:

- thresholds;
- detector configurations;
- preprocessing;
- tokenization;
- benchmark membership;
- language mappings;
- evaluation methodology.

Changes must be versioned.

---

# 69. Validation Automation

As much validation as reasonably possible should be automated.

Automation should cover:

- schema validation;
- deterministic integrity checks;
- regression;
- benchmark execution;
- result comparison;
- configuration validation;
- dependency validation;
- report generation.

Human review remains appropriate for scientific interpretation where
automation is insufficient.

---

# 70. Validation Independence

Whenever practical, the component generating a result should not be the sole
judge of that result.

Examples:

- transformation generator vs integrity validator;
- detector adapter vs experiment evaluator;
- model output vs structural checker.

This reduces circular validation.

---

# 71. Rejection of Circular Evidence

The following is insufficient:

A capability declares itself successful
→ capability produces its own score
→ same capability declares pass.

Independent validation is required for important claims.

---

# 72. Experimental Transparency

Where a research result is surprising, the project should retain enough
information to reproduce or investigate it.

This includes:

- input sample;
- output sample;
- configuration;
- versions;
- metrics;
- errors;
- relevant logs.

Sensitive text must be protected appropriately.

---

# 73. Validation Quality Gate

Before publishing or relying on a major scientific conclusion, verify:

- correct dataset;
- correct language;
- correct versions;
- no obvious leakage;
- appropriate controls;
- appropriate sample size;
- appropriate metrics;
- uncertainty reported;
- limitations reported;
- competing explanations considered.

---

# 74. Current Validation State

The project is currently defining the validation framework.

Final thresholds, benchmarks and statistical methodologies should not be
invented before the research phase establishes their suitability.

The validation architecture therefore emphasizes:

- reproducibility;
- independence;
- raw measurements;
- multilingual evaluation;
- versioning;
- uncertainty;
- regression;
- continuous scientific updating.

---

# 75. Governing Principle

The purpose of validation is not to prove that the system always works.

The purpose is to determine, as rigorously as practical:

- when it works;
- where it works;
- how well it works;
- under which conditions it fails;
- how certain the conclusion is;
- whether the conclusion remains valid as the underlying ecosystem changes.

A scientifically valuable system must make failure measurable rather than
hide it.