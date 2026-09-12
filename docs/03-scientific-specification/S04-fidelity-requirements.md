# S04 — Fidelity Requirements

**Status:** NORMATIVE
**Version:** 0.2 (2026-09-12: DCQ-008 propagation note added to FID-002,
per DECISION-LOG.md DEC-016)
**Document type:** Scientific specification
**Parent:** `docs/03-scientific-specification/SPECIFICATION-MAP.md`
**Related:** `docs/03-scientific-specification/S01-system-objectives.md`
**Research basis:** `docs/02-research/RESEARCH-MAP.md`
**Identifier history:** Originally drafted as `S02-fidelity-requirements.md`
under status `NORMATIVE / DRAFT FOR CONSOLIDATION`. Renumbered to `S04` on
2026-08-22 to resolve a duplicate-identifier collision with
`S02-scientific-requirements.md` — see `DEC-011` in
`docs/00-project/DECISION-LOG.md` and DCQ-005 in
`docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md`. No requirement content
was changed as part of this renumbering.

---

# 1. Purpose

This document defines the scientific requirements for preserving the input
text during a transformation.

The purpose is to ensure that transformation quality is evaluated independently
from the particular detector, watermark methodology or transformation
algorithm being investigated.

The central principle is:

> A transformation is acceptable only when the required properties of the
> source text remain within the experimentally defined preservation limits.

The document therefore defines fidelity as a multidimensional property.

---

# 2. Fidelity Model

Textual fidelity is not represented by a single universal score.

The minimum fidelity model consists of:

1. semantic fidelity;
2. factual fidelity;
3. informational fidelity;
4. linguistic fidelity;
5. structural fidelity;
6. stylistic fidelity;
7. formatting fidelity where applicable;
8. transformation magnitude.

These dimensions must remain separately observable.

A composite score may be introduced for a specific experiment, but it must not
replace the underlying dimensions.

---

# 3. Source and Output

Every transformation experiment has at least two primary textual artifacts:

- SOURCE — the original input text;
- OUTPUT — the transformed text.

The system must preserve an unmodified representation of SOURCE for the entire
experiment.

OUTPUT must be associated unambiguously with:

- the source identifier;
- the transformation method;
- the transformation version;
- the transformation parameters;
- the experiment identifier.

The source must never be reconstructed from the output.

---

# 4. Fidelity Requirement FID-001 — Semantic Preservation

The output must preserve the intended meaning of the source within the
acceptance limits defined by the applicable validation specification.

Semantic preservation must consider, where applicable:

- propositions;
- claims;
- relationships;
- negations;
- modality;
- temporal relationships;
- causal relationships;
- logical relationships;
- scope;
- discourse relations;
- references between statements.

A high lexical similarity must not be treated as sufficient evidence of
semantic equivalence.

---

# 5. Fidelity Requirement FID-002 — Claim Preservation

Material claims present in the source must not be silently:

- removed;
- contradicted;
- materially weakened;
- materially strengthened;
- changed in scope;
- changed in attribution.

Where claim extraction is possible, source and output claims should be
compared explicitly.

A transformation that changes a claim must be classified as a potential
fidelity failure unless the change is explicitly permitted by the experiment.

**Note (2026-09-12, DCQ-008, per DECISION-LOG.md DEC-016):** This is the
holistic, claim/proposition-level scope that `DECISION-LOG.md` DEC-015
identified as where `KNOWLEDGE-BACKLOG.md` KB-013's evidence gap actually
applies: no evidence-backed multilingual factual/claim-consistency option
currently exists (`RESEARCH-REGISTRY.md` R-0109-R-0112). For English,
MiniCheck (R-0109) is a well-evidenced candidate; for the other 12 target
languages, no candidate currently qualifies as validated (see
`docs/04-architecture/VALIDATION-ARCHITECTURE.md` §6 for the resulting
`VALIDATE-FACTUAL-CLAIM` architectural treatment, including the FID-043
requirement that an unvalidated language/capability pair be reported as
`not measurable`/`unsupported` rather than silently passed). This is
distinct from FID-003 below, whose scope is narrower and does not carry
this evidence gap.

---

# 6. Fidelity Requirement FID-003 — Factual Preservation

The output must preserve factual information contained in the source.

The evaluation framework should detect changes to:

- names;
- entities;
- dates;
- times;
- quantities;
- percentages;
- measurements;
- currencies;
- units;
- locations;
- identifiers;
- citations;
- references;
- technical parameters.

Numbers and structured factual information require particular attention because
small textual changes may produce large semantic differences.

---

# 7. Fidelity Requirement FID-004 — No Unsupported Factual Generation

The transformation must not introduce new factual assertions unless the
experimental specification explicitly permits them.

The system should distinguish:

- stylistic additions;
- explanatory additions;
- factual additions;
- unsupported assertions.

An output containing unsupported factual material must be flagged independently
from ordinary textual variation.

---

# 8. Fidelity Requirement FID-005 — Information Preservation

The information content of the source must be preserved to the extent required
by the experiment.

The evaluation should consider:

- facts;
- qualifications;
- conditions;
- exceptions;
- examples;
- constraints;
- references;
- uncertainty statements;
- attribution;
- contextual information.

A shorter output is not necessarily less faithful, and a longer output is not
necessarily more faithful.

Information preservation must therefore be evaluated semantically rather than
only through length or token count.

---

# 9. Fidelity Requirement FID-006 — Negation Preservation

Negation is a high-risk semantic property.

The transformation must preserve, where applicable:

- explicit negation;
- implicit negation;
- scope of negation;
- negative quantification;
- contrastive negation;
- negation involving modality.

Any change in negation must be treated as a potentially material semantic
change.

---

# 10. Fidelity Requirement FID-007 — Modality Preservation

The transformation must preserve modality and epistemic qualification.

Particular attention should be given to changes involving:

- certainty;
- probability;
- possibility;
- obligation;
- permission;
- recommendation;
- speculation;
- attribution of uncertainty.

For example, a statement expressing possibility must not silently become a
statement expressing certainty.

---

# 11. Fidelity Requirement FID-008 — Quantitative Preservation

Quantitative information must be preserved accurately.

This includes:

- numbers;
- ranges;
- ratios;
- percentages;
- mathematical expressions;
- units;
- comparisons;
- ordering;
- magnitudes.

Where possible, quantitative information should be extracted and compared
independently from general semantic similarity.

---

# 12. Fidelity Requirement FID-009 — Temporal Preservation

Temporal information must be preserved.

The evaluation should consider:

- dates;
- durations;
- sequences;
- relative temporal expressions;
- deadlines;
- historical references;
- before/after relationships.

Changes that alter the temporal interpretation of a statement constitute
potential semantic failures.

---

# 13. Fidelity Requirement FID-010 — Entity Preservation

Named and referenced entities must be preserved.

This includes, where applicable:

- persons;
- organizations;
- locations;
- products;
- works;
- scientific entities;
- technical entities;
- identifiers.

Entity substitutions must not be considered harmless lexical variation without
evaluation.

---

# 14. Fidelity Requirement FID-011 — Attribution Preservation

The output must preserve attribution.

The transformation must not silently change:

- who made a statement;
- who performed an action;
- who is responsible for a claim;
- whether a statement is quoted;
- whether information is attributed to a source.

Attribution errors may create factual or semantic errors even when the overall
text remains highly similar.

---

# 15. Fidelity Requirement FID-012 — Citation and Reference Preservation

Where the input contains citations, references or source markers, their
meaning must be preserved.

The transformation must not silently:

- remove important citations;
- invent citations;
- change cited sources;
- alter citation targets;
- change bibliographic facts;
- attribute a claim to a different source.

Citation handling may be configured differently for experiments that explicitly
exclude citation material.

---

# 16. Fidelity Requirement FID-013 — Linguistic Correctness

The output must remain linguistically valid in the target language.

Evaluation should consider:

- grammar;
- syntax;
- morphology;
- agreement;
- lexical choice;
- orthography;
- punctuation;
- idiomaticity;
- coherence.

A detector-related outcome must never be treated as evidence of linguistic
quality.

---

# 17. Fidelity Requirement FID-014 — Register Preservation

Where preservation of style is required, the output should preserve the
source register.

Relevant dimensions include:

- formal versus informal language;
- technical versus general language;
- academic register;
- journalistic register;
- conversational register;
- professional register;
- rhetorical level.

Register preservation may be relaxed only when explicitly authorized by the
experiment.

---

# 18. Fidelity Requirement FID-015 — Stylistic Preservation

Where style preservation is part of the experiment, the transformation should
minimize unnecessary stylistic change.

Potential dimensions include:

- sentence rhythm;
- lexical preference;
- phraseology;
- rhetorical structure;
- paragraph organization;
- degree of formality;
- use of passive or active constructions;
- discourse markers.

Style must be treated separately from semantic equivalence.

A semantically equivalent output may still represent a substantial stylistic
change.

---

# 19. Fidelity Requirement FID-016 — Structural Preservation

The transformation should preserve document structure unless structural
modification is explicitly permitted.

Structural elements may include:

- paragraphs;
- headings;
- lists;
- tables;
- quotations;
- sections;
- footnotes;
- references;
- ordering of content.

Structural comparison must account for the format of the input.

---

# 20. Fidelity Requirement FID-017 — Formatting Preservation

Where formatting is considered part of the input, the transformation should
preserve it.

Potential formatting elements include:

- whitespace;
- punctuation;
- quotation marks;
- capitalization;
- emphasis;
- markup;
- line breaks;
- list markers.

Formatting may be excluded from an experiment when it is not scientifically
relevant, but that exclusion must be explicit.

---

# 21. Fidelity Requirement FID-018 — Language Identity

The output must remain in the intended target language unless the experiment
explicitly permits language conversion.

Unintentional:

- translation;
- code-switching;
- language mixing;
- transliteration;

must be detected where practical.

---

# 22. Fidelity Requirement FID-019 — Script Preservation

For languages with multiple writing systems, the experiment must explicitly
define whether script preservation is required.

Examples include:

- Japanese scripts;
- Chinese character variants;
- Cyrillic versus Latin transliteration;
- Arabic-derived scripts;
- mixed-script documents.

A script change must not automatically be classified as semantic failure, but
must be recorded as a transformation property.

---

# 23. Fidelity Requirement FID-020 — Transformation Magnitude

The system must measure how much the output differs from the source.

At minimum, the evaluation framework should be capable of measuring multiple
levels of change.

Potential measurements include:

- character edit distance;
- token edit distance;
- word substitution rate;
- insertion rate;
- deletion rate;
- sentence modification rate;
- paragraph modification rate;
- syntactic change;
- semantic distance.

No single distance metric is considered universally authoritative.

---

# 24. Fidelity Requirement FID-021 — Minimality

Where multiple transformations satisfy the same experimental objective, the
preferred transformation is the one that introduces the least unnecessary
change while satisfying all mandatory preservation requirements.

Minimality must not override fidelity.

A smaller textual change that introduces a factual or semantic error is worse
than a larger change that preserves the source correctly.

---

# 25. Fidelity Requirement FID-022 — Generation Budget

The evaluation framework should support explicit limits on generated material.

Potential controls include:

- changed-token ratio;
- inserted-token ratio;
- changed-sentence ratio;
- generated-content estimate;
- semantic-distance threshold.

A generation budget is an experimental constraint rather than a universal
scientific constant.

---

# 26. Fidelity Requirement FID-023 — Locality of Modification

Where feasible, transformations should be localized.

The system should identify:

- unchanged regions;
- modified regions;
- inserted regions;
- deleted regions;
- substituted regions.

Localized modification is desirable because it improves interpretability and
facilitates causal analysis.

---

# 27. Fidelity Requirement FID-024 — No Hidden Content Modification

All material modifications must be observable in the experiment record.

The system must not silently modify:

- source text;
- metadata used for evaluation;
- evaluation configuration;
- detector configuration;
- language identification;
- preprocessing rules.

Preprocessing changes must be explicitly recorded.

---

# 28. Fidelity Requirement FID-025 — Preprocessing Transparency

Any preprocessing applied before fidelity evaluation must be documented.

Examples include:

- normalization;
- whitespace normalization;
- Unicode normalization;
- tokenization;
- sentence segmentation;
- markup removal;
- case normalization.

Preprocessing must not be used to conceal meaningful changes.

---

# 29. Fidelity Requirement FID-026 — Unicode Awareness

Unicode normalization and encoding differences must be handled explicitly.

The system should distinguish:

- byte-level differences;
- code-point differences;
- grapheme differences;
- visually equivalent representations.

This is particularly important for multilingual evaluation.

---

# 30. Fidelity Requirement FID-027 — Multilingual Fidelity

Fidelity evaluation must account for language-specific characteristics.

A metric validated for one language must not automatically be assumed to be
equally valid for another.

The project must record language-specific limitations for fidelity metrics.

---

# 31. Fidelity Requirement FID-028 — Morphological Fidelity

For morphologically rich languages, evaluation should account for changes in:

- case;
- number;
- gender;
- tense;
- aspect;
- mood;
- person;
- agreement;
- derivational morphology.

A morphologically small textual change may produce a significant semantic or
grammatical effect.

---

# 32. Fidelity Requirement FID-029 — Word-Order Fidelity

The evaluation must account for language-specific word-order properties.

A change in word order may be:

- stylistically harmless;
- grammatically necessary;
- semantically meaningful.

The classification must therefore depend on the target language.

---

# 33. Fidelity Requirement FID-030 — Discourse Fidelity

The transformation should preserve discourse-level relationships.

Relevant properties include:

- topic continuity;
- coherence;
- reference resolution;
- discourse markers;
- contrast;
- causality;
- sequence;
- conclusion relationships.

Sentence-by-sentence similarity is insufficient for full discourse evaluation.

---

# 34. Fidelity Requirement FID-031 — Long-Range Dependency Preservation

Where relevant, the evaluation should identify changes involving dependencies
across distant portions of the document.

Examples include:

- pronoun references;
- terminology consistency;
- entity references;
- definitions;
- repeated claims;
- section-level conclusions.

A locally acceptable sentence may still create a document-level inconsistency.

---

# 35. Fidelity Requirement FID-032 — Terminology Preservation

Technical or domain-specific terminology should be preserved where it carries
meaning.

The system should identify:

- domain terms;
- abbreviations;
- acronyms;
- defined terms;
- specialized nomenclature.

Unnecessary terminology substitutions should be penalized when terminology
preservation is required.

---

# 36. Fidelity Requirement FID-033 — Formula and Symbol Preservation

Where text contains mathematical, scientific or technical notation, the
transformation must preserve its meaning.

This includes:

- formulas;
- symbols;
- variables;
- units;
- equations;
- chemical notation;
- code-like fragments where applicable.

Such content may require specialized validation rather than ordinary language
metrics.

---

# 37. Fidelity Requirement FID-034 — Code and Structured Text

When the input contains code, configuration, structured data or other
machine-readable material, the system must explicitly classify it.

The transformation must not alter executable or structured semantics unless
the experiment explicitly permits it.

Natural-language fidelity metrics must not be applied blindly to such content.

---

# 38. Fidelity Requirement FID-035 — Mixed-Content Documents

Documents may contain multiple content types.

The system should support segmentation into, where applicable:

- natural language;
- headings;
- quotations;
- tables;
- references;
- code;
- formulas;
- metadata;
- structured data.

Each segment may require different fidelity criteria.

---

# 39. Fidelity Requirement FID-036 — Human Evaluation

Where automated metrics cannot adequately establish fidelity, human evaluation
may be used.

Human evaluation protocols should define:

- evaluator population;
- instructions;
- rating scale;
- sampling;
- blinding;
- inter-rater agreement;
- adjudication;
- statistical treatment.

Human evaluation must be reproducible to the extent practical.

---

# 40. Fidelity Requirement FID-037 — Metric Diversity

Important fidelity claims should not depend exclusively on a single metric.

Where feasible, evaluation should combine complementary measurements.

Examples include:

- lexical metrics;
- semantic metrics;
- factual consistency checks;
- structural comparison;
- linguistic evaluation;
- human evaluation.

Metrics that measure substantially the same property should not be treated as
independent evidence without justification.

---

# 41. Fidelity Requirement FID-038 — Metric Validity

Every metric used as an acceptance criterion must have a documented rationale.

The documentation should identify:

- what the metric measures;
- what it does not measure;
- language coverage;
- known biases;
- known failure modes;
- validation evidence;
- version;
- implementation.

A metric must not be used merely because it is convenient.

---

# 42. Fidelity Requirement FID-039 — Threshold Validity

Acceptance thresholds must be scientifically justified.

Thresholds may originate from:

- published research;
- benchmark distributions;
- human evaluation;
- controlled experiments;
- project-specific empirical calibration.

Thresholds must be versioned.

A threshold must not be changed merely to make a method pass.

---

# 43. Fidelity Requirement FID-040 — Pareto Evaluation

Where multiple fidelity dimensions conflict, the system should support
multi-objective evaluation rather than immediately collapsing them into a
single score.

For example:

- lower edit distance may conflict with better linguistic quality;
- greater stylistic preservation may conflict with another experimental
  objective;
- semantic preservation may remain high while structural similarity falls.

The system must make such trade-offs visible.

---

# 44. Fidelity Requirement FID-041 — Hard Constraints

Some fidelity properties may be designated hard constraints.

Examples include:

- no factual changes;
- no numerical changes;
- no entity changes;
- no unsupported claims;
- no language change.

Violation of a hard constraint may invalidate the transformation regardless of
performance on other metrics.

Hard constraints must be explicitly defined by the relevant experiment.

---

# 45. Fidelity Requirement FID-042 — Soft Objectives

Other properties may be treated as optimization objectives rather than absolute
constraints.

Examples include:

- stylistic similarity;
- lexical similarity;
- edit distance;
- sentence structure;
- formatting similarity.

Soft objectives must never override hard constraints.

---

# 46. Fidelity Requirement FID-043 — Missing Evidence

When a fidelity dimension cannot be reliably measured, the system must record
the dimension as:

- measured;
- partially measured;
- not measurable;
- unsupported;
- not applicable.

It must not silently interpret missing measurement as success.

---

# 47. Fidelity Requirement FID-044 — Confidence

Where evaluation methods provide confidence information, it must be retained.

Confidence must not be confused with correctness.

A detector or metric reporting high confidence does not automatically imply
high scientific reliability.

---

# 48. Fidelity Requirement FID-045 — Error Taxonomy

Fidelity failures should be classified.

At minimum, the system should distinguish:

- semantic error;
- factual error;
- informational omission;
- unsupported addition;
- linguistic error;
- structural error;
- stylistic deviation;
- formatting deviation;
- language error;
- terminology error;
- numerical error;
- attribution error;
- citation error.

This taxonomy should be extensible.

---

# 49. Fidelity Requirement FID-046 — Severity

Fidelity failures should support severity classification.

A recommended initial classification is:

- CRITICAL;
- MAJOR;
- MODERATE;
- MINOR;
- INFORMATIONAL.

Severity must be defined relative to the experimental objective.

For example, a changed number may be critical in one document and irrelevant
in another if the number belongs to intentionally excluded metadata.

---

# 50. Fidelity Requirement FID-047 — Aggregation

Aggregated fidelity scores may be used for analysis, but the underlying
component results must remain accessible.

An aggregate score must document:

- included dimensions;
- weighting;
- normalization;
- missing-value treatment;
- threshold;
- version.

No aggregate score may conceal a hard-constraint violation.

---

# 51. Fidelity Requirement FID-048 — Baseline

Every transformation experiment should have an appropriate baseline.

Possible baselines include:

- unchanged source;
- random or control transformation;
- alternative transformation;
- reference paraphrase;
- language-specific baseline.

The baseline must be appropriate to the scientific question.

---

# 52. Fidelity Requirement FID-049 — Control Experiments

Where causal interpretation is important, control experiments should be used.

Controls may test:

- detector behavior without transformation;
- metric behavior without transformation;
- language effects;
- preprocessing effects;
- random perturbation effects;
- alternative transformation effects.

Control experiments should be recorded as first-class experimental artifacts.

---

# 53. Fidelity Requirement FID-050 — Evaluation Leakage

The evaluation framework must identify possible leakage between:

- transformation optimization;
- benchmark data;
- detector training data;
- evaluation metrics;
- validation datasets.

A transformation must not be considered independently validated if it was
optimized directly against the evaluation set without appropriate controls.

---

# 54. Fidelity Requirement FID-051 — Dataset Independence

Where feasible, validation should include data not used during transformation
development or parameter tuning.

Development, calibration and final evaluation datasets should be separated
when scientifically justified.

---

# 55. Fidelity Requirement FID-052 — Robustness

Fidelity conclusions should be evaluated for robustness across relevant
conditions.

Potential dimensions include:

- document length;
- domain;
- language;
- register;
- source quality;
- text complexity;
- formatting;
- detector;
- transformation configuration.

A method that works only under a narrow condition must be characterized as
such.

---

# 56. Fidelity Requirement FID-053 — Distribution Shift

The system must recognize that fidelity metrics may behave differently under
distribution shift.

Potential shifts include:

- domain shift;
- language shift;
- temporal shift;
- genre shift;
- document-length shift;
- model-generation shift.

Results must not automatically be generalized beyond the tested population.

---

# 57. Fidelity Requirement FID-054 — Versioned Evaluation

Fidelity results must be associated with the versions of all material evaluation
components.

A change to a metric implementation, tokenizer, preprocessing pipeline or
dataset may invalidate direct comparison with historical results.

Historical results must remain reproducible or explicitly marked as
non-reproducible.

---

# 58. Fidelity Requirement FID-055 — Historical Comparability

When evaluation methodology changes, the project should distinguish:

- directly comparable results;
- approximately comparable results;
- non-comparable historical results.

Historical results must not be silently recomputed and substituted for the
original evidence.

---

# 59. Fidelity Requirement FID-056 — Failure Preservation

Failed transformations must be retained as scientific evidence when required
for reproducibility.

The system must not retain only successful examples when that would bias
evaluation.

---

# 60. Fidelity Requirement FID-057 — Minimality versus Fidelity

Minimal textual change is subordinate to preservation of mandatory properties.

The optimization hierarchy is therefore:

1. satisfy hard preservation constraints;
2. avoid unacceptable linguistic or structural degradation;
3. minimize unnecessary transformation;
4. optimize secondary experimental objectives.

A transformation that changes fewer tokens but damages meaning is not preferred.

---

# 61. Fidelity Requirement FID-058 — Experimental Flexibility

The fidelity framework must allow experiments to define different mandatory
dimensions.

For example:

- semantic preservation may be mandatory;
- formatting preservation may be irrelevant;
- stylistic preservation may be a secondary objective;
- numerical preservation may be an absolute constraint.

Such configurations must be explicit and versioned.

---

# 62. Fidelity Requirement FID-059 — Language-Specific Criteria

Language-specific fidelity criteria may be introduced where general criteria
are inadequate.

Such criteria must record:

- language;
- linguistic phenomenon;
- rationale;
- metric;
- threshold;
- evidence;
- limitations.

Language-specific criteria must not silently alter the global definition of
fidelity.

---

# 63. Fidelity Requirement FID-060 — Unknown Cases

The system must support an explicit UNKNOWN or INDETERMINATE outcome.

This outcome is required when:

- evidence is insufficient;
- metrics disagree materially;
- the text is outside supported conditions;
- the evaluation method is unavailable;
- detector or metric output is inconclusive.

UNKNOWN must not be converted into PASS or FAIL without an explicit rule.

---

# 64. Fidelity Requirement FID-061 — Reproducibility of Fidelity Results

A fidelity result must be reproducible from:

- source;
- output;
- evaluation configuration;
- metric versions;
- preprocessing versions;
- datasets;
- parameters;
- environment information where relevant.

The project must preserve sufficient metadata to reconstruct the result.

---

# 65. Fidelity Requirement FID-062 — Auditability

Every acceptance or rejection decision must be explainable.

The project should be able to identify:

- which requirement was evaluated;
- which metric or method was used;
- which threshold applied;
- which evidence supported the result;
- which version was used;
- what uncertainty existed.

---

# 66. Fidelity Requirement FID-063 — No Detector-Driven Fidelity

A transformation must never be declared faithful solely because a detector
reports a desired classification.

Detector outcomes are separate evaluation dimensions.

Fidelity must be independently established.

---

# 67. Fidelity Requirement FID-064 — No Single-Metric Optimization

The production transformation objective must not be defined exclusively as
optimization of a single detector or metric.

This protects the system from overfitting to a particular evaluator.

---

# 68. Fidelity Requirement FID-065 — Evaluator Diversity

Where practical, validation should include evaluators with materially
different methodologies.

This may include:

- statistical methods;
- classifier-based methods;
- linguistic methods;
- watermark-specific methods;
- human evaluation;
- structural methods.

The exact evaluator set is determined by the research and validation layers.

---

# 69. Fidelity Requirement FID-066 — Future Evaluators

The fidelity framework must support adding future evaluators without changing
the definition of existing historical results.

Each evaluator should have:

- stable identifier;
- version;
- methodology;
- input requirements;
- output schema;
- known limitations;
- lifecycle state.

---

# 70. Fidelity Requirement FID-067 — Evaluator Retirement

An evaluator may become obsolete.

Retirement must not erase historical results.

Historical results must remain associated with the evaluator version that
produced them.

---

# 71. Fidelity Requirement FID-068 — Reassessment

Fidelity requirements must be reassessed when new scientific evidence shows
that:

- an existing metric is unreliable;
- a threshold is inappropriate;
- a linguistic phenomenon was overlooked;
- a new error class is important;
- a new evaluation methodology materially changes the evidence.

Reassessment must be documented.

---

# 72. Fidelity Requirement FID-069 — No Silent Requirement Drift

Changes to fidelity requirements must not occur implicitly through:

- code changes;
- metric changes;
- dataset changes;
- detector changes;
- preprocessing changes.

Scientific requirement changes must be explicitly documented.

---

# 73. Fidelity Requirement FID-070 — Traceability

Each fidelity requirement must be traceable to:

- scientific evidence;
- specification;
- validation method;
- implementation capability;
- validation result.

The traceability chain should support both forward and backward navigation.

---

# 74. Fidelity Requirement FID-071 — Scientific Limitations

Known limitations of fidelity evaluation must be explicitly documented.

Limitations may include:

- language coverage;
- domain coverage;
- metric validity;
- human-evaluation limitations;
- dataset limitations;
- detector dependence;
- preprocessing dependence;
- computational constraints.

---

# 75. Fidelity Requirement FID-072 — No Universal Fidelity Claim

The project must not claim universal fidelity based on a finite evaluation
population.

A valid conclusion must specify the conditions under which fidelity was
demonstrated.

---

# 76. Fidelity Requirement FID-073 — Resource Awareness

Fidelity evaluation must respect project resource constraints.

Where a high-cost metric or dataset provides insufficient incremental
scientific value, a documented alternative may be used.

Resource optimization must not silently remove critical validation.

---

# 77. Fidelity Requirement FID-074 — Offline Compatibility

The core fidelity evaluation required for production operation should be
implementable without dependence on generative AI inference.

Research-only evaluators may use external services when explicitly documented.

External evaluation must not silently modify the production output.

---

# 78. Fidelity Requirement FID-075 — Separation of Transformation and Evaluation

Transformation and evaluation must remain logically separate.

The transformation system must not be able to declare its own output valid
without passing through the applicable evaluation framework.

This separation is required to reduce circular validation.

---

# 79. Fidelity Requirement FID-076 — Immutable Experiment Inputs

Once an experiment begins, the source and relevant configuration must be
immutable.

If an input changes, the experiment must receive a new identifier or version.

---

# 80. Fidelity Requirement FID-077 — Experiment Repetition

Important findings should be tested across repeated experiments when
stochasticity or sampling variability may materially affect the result.

Single-run results must be identified when repetition is not performed.

---

# 81. Fidelity Requirement FID-078 — Statistical Reporting

Where quantitative evaluation is used, reports should include sufficient
statistics to understand the result.

Depending on the experiment, this may include:

- sample size;
- mean;
- median;
- dispersion;
- confidence interval;
- effect size;
- distribution;
- failure rate.

---

# 82. Fidelity Requirement FID-079 — Per-Language Reporting

Multilingual results must support per-language reporting.

Aggregated multilingual scores must not conceal substantial language-specific
failures.

The minimum report should permit identification of:

- language;
- sample count;
- metrics;
- thresholds;
- failures;
- confidence or uncertainty;
- unsupported conditions.

---

# 83. Fidelity Requirement FID-080 — Per-Domain Reporting

Where domain variation is relevant, results should also be reported by domain.

Examples include:

- news;
- academic;
- technical;
- conversational;
- legal;
- creative;
- business.

Domain-specific results must not automatically be generalized.

---

# 84. Fidelity Requirement FID-081 — Length Effects

The evaluation must consider document length where length can affect metrics or
detector behavior.

The project should support analysis across length bands.

---

# 85. Fidelity Requirement FID-082 — Short-Text Caution

Short texts may produce unreliable semantic, statistical or detector results.

The system must identify conditions under which the available evidence is
insufficient for short inputs.

---

# 86. Fidelity Requirement FID-083 — Long-Text Caution

Long documents may contain heterogeneous content and may exhibit local failures
that are hidden by document-level averages.

The system should support both aggregate and localized analysis.

---

# 87. Fidelity Requirement FID-084 — Segment-Level Evaluation

Where appropriate, evaluation should operate at multiple levels:

- character;
- token;
- sentence;
- paragraph;
- section;
- document.

The appropriate level depends on the scientific property being measured.

---

# 88. Fidelity Requirement FID-085 — Worst-Case Visibility

Aggregate metrics must not completely conceal severe local failures.

The validation framework should support reporting of:

- worst segment;
- highest-severity error;
- maximum deviation;
- number of critical failures.

---

# 89. Fidelity Requirement FID-086 — Preservation Priority

When experimental objectives conflict, mandatory preservation properties take
priority over secondary optimization objectives.

No detector-related objective may override an explicitly defined hard fidelity
constraint.

---

# 90. Fidelity Requirement FID-087 — Experimental Configuration

Every fidelity experiment must define its configuration explicitly.

At minimum:

- mandatory dimensions;
- optional dimensions;
- thresholds;
- metrics;
- datasets;
- language;
- domain;
- preprocessing;
- evaluation versions.

---

# 91. Fidelity Requirement FID-088 — Configuration Versioning

Changes to fidelity configuration must create a new version.

Historical experiment results must remain associated with the configuration
under which they were produced.

---

# 92. Fidelity Requirement FID-089 — Reproducible Comparison

Comparisons between transformations must use equivalent evaluation conditions.

A comparison is invalid if materially different:

- datasets;
- preprocessing;
- thresholds;
- metrics;
- detector versions;
- language conditions;

are used without explicit adjustment.

---

# 93. Fidelity Requirement FID-090 — Scientific Interpretation

A fidelity result must be interpreted within the limits of the evidence.

The system should distinguish:

- observed result;
- statistically supported result;
- replicated result;
- generalized result;
- unresolved result.

These are not equivalent states.

---

# 94. Fidelity Requirement FID-091 — Evidence Hierarchy

When conflicting evidence exists, the project should consider:

1. independently replicated evidence;
2. controlled experimental evidence;
3. validated benchmark evidence;
4. peer-reviewed evidence;
5. preliminary experimental evidence;
6. unvalidated observations.

The exact evidence hierarchy may be refined by the research governance layer.

---

# 95. Fidelity Requirement FID-092 — Conflicting Metrics

When metrics disagree materially, the system must expose the disagreement.

It must not automatically select whichever metric produces the preferred
result.

The disagreement should be investigated or recorded as uncertainty.

---

# 96. Fidelity Requirement FID-093 — Conflicting Human Judgments

Where human evaluation is used, disagreement between evaluators must be
quantified where practical.

Low agreement may indicate:

- ambiguous instructions;
- inherently subjective criteria;
- inadequate evaluator expertise;
- difficult source material.

Such disagreement must not be hidden by averaging alone.

---

# 97. Fidelity Requirement FID-094 — Preservation Before Optimization

The system must establish that mandatory preservation requirements are
satisfied before evaluating secondary optimization objectives.

This establishes the following conceptual order:

PRESERVE
→ VERIFY
→ MEASURE CHANGE
→ EVALUATE EXPERIMENTAL OBJECTIVE
→ REPORT

---

# 98. Fidelity Requirement FID-095 — Transparent Failure

When a transformation fails, the system must report why it failed whenever the
available evidence permits classification.

Failure reports should identify:

- violated requirement;
- severity;
- evidence;
- metric;
- threshold;
- uncertainty.

---

# 99. Fidelity Requirement FID-096 — Transparent Success

A successful result must also identify:

- applicable conditions;
- evaluation population;
- metrics;
- thresholds;
- evidence;
- uncertainty;
- limitations.

"PASS" without context is insufficient scientific reporting.

---

# 100. Fidelity Requirement FID-097 — No Post-Hoc Metric Selection

Metrics and acceptance criteria should be defined before evaluating the final
experimental result whenever practical.

Post-hoc selection of favorable metrics must be identified as such.

---

# 101. Fidelity Requirement FID-098 — No Post-Hoc Threshold Selection

Thresholds must not be selected after observing the final result merely to
obtain acceptance.

Calibration experiments must be separated from final validation where
scientifically appropriate.

---

# 102. Fidelity Requirement FID-099 — Reassessment Trigger

The fidelity framework must trigger reassessment when:

- a major new metric becomes available;
- an existing metric is shown to be unreliable;
- a new language is added;
- a new document domain is introduced;
- a new transformation class is introduced;
- significant benchmark evidence changes;
- major detector or watermark methodologies change.

---

# 103. Fidelity Requirement FID-100 — Final Fidelity Principle

The objective of fidelity evaluation is not to prove that a transformation is
good.

The objective is to determine, with the strongest available evidence, whether
the transformation preserves the required properties of the source under the
specified experimental conditions.

The system must therefore remain:

- multidimensional;
- measurable;
- falsifiable;
- language-aware;
- statistically grounded;
- reproducible;
- auditable;
- extensible;
- temporally maintainable;
- open to negative results.

No transformation should be considered scientifically successful merely
because it achieves a desired detector outcome.