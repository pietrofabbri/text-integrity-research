# S05 — Transformation Requirements

**Status:** NORMATIVE
**Version:** 0.1
**Document type:** Scientific specification
**Parent:** `docs/03-scientific-specification/SPECIFICATION-MAP.md`
**Related:** `docs/03-scientific-specification/S01-system-objectives.md`
**Related:** `docs/03-scientific-specification/S04-fidelity-requirements.md`
**Research basis:** `docs/02-research/RESEARCH-MAP.md`
**Identifier history:** Originally drafted as
`S03-transformation-requirements.md` under status `NORMATIVE / DRAFT FOR
CONSOLIDATION`. Renumbered to `S05` on 2026-08-22 to resolve a
duplicate-identifier collision with `S03-experimental-model.md` — see
`DEC-011` in `docs/00-project/DECISION-LOG.md` and DCQ-005 in
`docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md`. No requirement content
was changed as part of this renumbering.

---

# 1. Purpose

This document defines the scientific requirements governing textual
transformation.

It specifies what a transformation system must guarantee about its behavior
without prescribing a particular implementation, algorithm, model, language,
framework or software architecture.

The transformation layer exists to produce a candidate output from a source
text under explicitly defined experimental constraints.

The transformation layer does not determine whether its own output is
scientifically acceptable.

Acceptance is determined by the independent validation layer.

---

# 2. Fundamental Transformation Principle

A transformation must be treated as an experimental intervention.

The system must be able to establish:

- what the source was;
- what transformation was applied;
- which parameters were used;
- what output was produced;
- what changed;
- what remained unchanged;
- what evidence supports acceptance or rejection.

The transformation must therefore be observable, reproducible and
independently evaluable.

---

# 3. Transformation Objective

The primary transformation objective is:

> Produce the smallest justified modification of the source capable of
> satisfying the explicitly defined experimental objective while respecting
> all mandatory preservation requirements.

The experimental objective must be represented independently from the
transformation implementation.

A transformation must not infer its objective from the result of a detector.

---

# 4. Separation from Evaluation

Transformation and evaluation are separate system responsibilities.

The transformation component:

- receives an input;
- applies an explicitly configured method;
- produces an output;
- records transformation metadata.

The evaluation component:

- evaluates fidelity;
- evaluates experimental outcomes;
- evaluates relevant detectors;
- evaluates uncertainty;
- determines acceptance.

The transformation component must not be the sole authority for declaring
its own success.

---

# 5. Transformation Requirement TRN-001 — Source Preservation

The original source must remain unchanged and independently retrievable.

The transformation process must operate on a representation of the source
without modifying the authoritative source artifact.

The source must remain available for:

- comparison;
- reproduction;
- validation;
- audit;
- rollback;
- future re-evaluation.

---

# 6. Transformation Requirement TRN-002 — Output Independence

The output must be stored as a distinct artifact.

The system must never overwrite the authoritative source as part of normal
transformation.

The relationship between source and output must be explicit.

---

# 7. Transformation Requirement TRN-003 — Transformation Identity

Every transformation method must have a stable identifier.

The identifier must remain stable across compatible revisions.

A materially different method must receive a new version or identifier according
to the project's lifecycle rules.

---

# 8. Transformation Requirement TRN-004 — Transformation Versioning

Every transformation result must identify the exact transformation version
that produced it.

Version information must be sufficient to distinguish materially different
behavior.

Historical results must not silently acquire a new transformation version.

---

# 9. Transformation Requirement TRN-005 — Parameter Recording

Parameters that can materially affect transformation behavior must be recorded.

This includes, where applicable:

- thresholds;
- configuration;
- selected strategy;
- language;
- domain;
- preprocessing;
- postprocessing;
- randomness configuration;
- resource limits.

Unrecorded parameters that materially affect output are considered a
reproducibility risk.

---

# 10. Transformation Requirement TRN-006 — Explicit Configuration

Transformation behavior must be explicitly configurable.

Implicit behavior based on undocumented defaults must be minimized.

Defaults may exist, but their values and semantics must be documented.

---

# 11. Transformation Requirement TRN-007 — Minimal Intervention

The transformation should modify no more of the source than necessary for the
experimental objective.

Minimal intervention must be measured independently from experimental success.

A method must not be considered superior merely because it changes fewer
characters or tokens.

---

# 12. Transformation Requirement TRN-008 — Preservation Priority

Mandatory fidelity requirements have priority over transformation objectives.

The conceptual priority order is:

1. preserve mandatory source properties;
2. maintain linguistic validity;
3. minimize unnecessary modification;
4. optimize the experimental objective;
5. optimize secondary preferences.

An optimization objective must never silently override a hard preservation
constraint.

---

# 13. Transformation Requirement TRN-009 — Hard Constraints

A transformation must support explicit hard constraints.

Examples may include:

- no factual changes;
- no numerical changes;
- no entity changes;
- no unsupported additions;
- no semantic degradation beyond a defined threshold;
- no language change.

Hard constraints must be experiment-specific and versioned.

---

# 14. Transformation Requirement TRN-010 — Soft Objectives

The system should support secondary optimization objectives.

Examples include:

- minimizing edit distance;
- preserving sentence structure;
- preserving terminology;
- preserving style;
- minimizing generated material.

Soft objectives must never override hard constraints.

---

# 15. Transformation Requirement TRN-011 — Transformation Budget

A transformation may operate under an explicit transformation budget.

Potential budget dimensions include:

- maximum changed-token ratio;
- maximum inserted-token ratio;
- maximum deleted-token ratio;
- maximum changed-sentence ratio;
- maximum semantic distance;
- maximum structural deviation.

The budget must be configurable.

A budget must not be interpreted as proof of fidelity.

---

# 16. Transformation Requirement TRN-012 — Local Modification

Where technically and scientifically appropriate, the system should prefer
localized modifications.

The system should be capable of identifying:

- unchanged spans;
- modified spans;
- inserted spans;
- deleted spans;
- substituted spans.

Locality improves interpretability and facilitates scientific analysis.

---

# 17. Transformation Requirement TRN-013 — No Unnecessary Generation

The system should avoid generating content that is not required by the
experimental objective.

Where a local transformation can satisfy the objective while preserving the
same required properties, unnecessary generation should be disfavored.

---

# 18. Transformation Requirement TRN-014 — No Unsupported Content

A transformation must not introduce unsupported factual or substantive content
unless the experimental configuration explicitly permits it.

Generated additions must be distinguishable from preserved material where
practical.

---

# 19. Transformation Requirement TRN-015 — No Silent Deletion

The transformation must not silently remove substantive source information.

Any substantive deletion must be observable in the transformation record and
subject to fidelity evaluation.

---

# 20. Transformation Requirement TRN-016 — No Silent Reordering

Reordering of substantive content must be observable.

The system must distinguish:

- harmless structural reordering;
- stylistic reordering;
- meaning-preserving reordering;
- meaning-changing reordering.

The classification belongs to evaluation rather than the transformation
component itself.

---

# 21. Transformation Requirement TRN-017 — Language Preservation

Unless explicitly configured otherwise, the transformation must preserve the
source language.

The transformation must not silently translate the source.

Unintended language switching or mixed-language output must be detectable.

---

# 22. Transformation Requirement TRN-018 — Language-Aware Processing

Transformation behavior may vary by language.

Language-specific strategies may be introduced where research demonstrates that
a generic method is inadequate.

Such strategies must be separately identifiable and evaluable.

---

# 23. Transformation Requirement TRN-019 — Language-Specific Constraints

Language-specific transformation constraints may include:

- morphology;
- syntax;
- word order;
- agreement;
- orthography;
- script;
- idiomaticity;
- punctuation;
- register.

Each language-specific constraint must have a documented scientific rationale.

---

# 24. Transformation Requirement TRN-020 — Unsupported Languages

When a language is outside validated coverage, the system must not silently
treat it as fully supported.

The system must be capable of returning an explicit unsupported or
insufficient-evidence state.

---

# 25. Transformation Requirement TRN-021 — Content-Type Awareness

The transformation must identify or respect distinct content types where
relevant.

Potential content types include:

- natural language;
- headings;
- quotations;
- tables;
- references;
- formulas;
- code;
- structured data;
- metadata.

A generic natural-language transformation must not blindly modify machine-
readable content.

---

# 26. Transformation Requirement TRN-022 — Structured Content Protection

Where structured content is protected by the experiment, the transformation
must preserve its machine-readable semantics.

This includes, where applicable:

- JSON-like structures;
- XML-like structures;
- configuration;
- code;
- formulas;
- identifiers.

Protected structured content should be excluded from ordinary linguistic
transformation.

---

# 27. Transformation Requirement TRN-023 — Boundary Awareness

Transformations must respect content boundaries.

A transformation should not unintentionally cross:

- document sections;
- quotations;
- tables;
- code blocks;
- formulas;
- metadata boundaries.

Boundary rules must be explicit.

---

# 28. Transformation Requirement TRN-024 — Unicode Safety

The transformation must handle Unicode correctly.

It must not unintentionally corrupt:

- characters;
- combining marks;
- normalization;
- scripts;
- punctuation;
- encoding.

Unicode behavior must be tested across the supported language set.

---

# 29. Transformation Requirement TRN-025 — Formatting Policy

Formatting behavior must be explicitly configured.

The transformation may:

- preserve formatting;
- normalize formatting;
- ignore formatting;
- modify formatting.

The selected behavior must be recorded.

Formatting changes must not be mistaken for linguistic transformation.

---

# 30. Transformation Requirement TRN-026 — Determinism

Where deterministic execution is possible, the transformation should support
deterministic operation.

If stochastic execution is used, the system must record sufficient information
to reproduce or statistically characterize the result.

---

# 31. Transformation Requirement TRN-027 — Randomness Control

If randomness is involved, the system should support:

- explicit random seed;
- recorded random configuration;
- reproducible execution where technically possible;
- repeated trials where necessary.

A stochastic result must not be represented as a deterministic result.

---

# 32. Transformation Requirement TRN-028 — Failure Before Output

If mandatory preconditions cannot be satisfied, the transformation should fail
explicitly rather than silently producing an output outside the configured
conditions.

Examples include:

- unsupported language;
- invalid input;
- unavailable required component;
- violated resource limit;
- malformed structured content.

---

# 33. Transformation Requirement TRN-029 — Failure Transparency

Transformation failures must be classified.

Potential classes include:

- unsupported language;
- invalid input;
- preprocessing failure;
- transformation failure;
- resource exhaustion;
- configuration error;
- dependency failure;
- safety-boundary violation;
- insufficient evidence;
- internal error.

The original source must remain available after failure.

---

# 34. Transformation Requirement TRN-030 — No Partial Success Misclassification

A partially transformed output must not be presented as a completed
transformation unless the experiment explicitly defines partial transformation
as valid.

Partial execution must be identifiable.

---

# 35. Transformation Requirement TRN-031 — Atomicity

A completed transformation should produce a coherent result.

If a transformation fails partway through, the system should avoid leaving an
ambiguous artifact that could be mistaken for a valid final output.

Temporary artifacts should be distinguishable from validated outputs.

---

# 36. Transformation Requirement TRN-032 — Provenance

Every output must have transformation provenance.

At minimum:

- source identifier;
- transformation identifier;
- transformation version;
- configuration identifier;
- execution timestamp;
- language;
- relevant environment information.

---

# 37. Transformation Requirement TRN-033 — Provenance Integrity

Transformation metadata must not be modifiable in a way that obscures how an
output was produced.

Changes to metadata must be traceable.

---

# 38. Transformation Requirement TRN-034 — No Hidden Preprocessing

Preprocessing that materially affects transformation must be explicit.

Examples include:

- Unicode normalization;
- whitespace normalization;
- segmentation;
- language identification;
- markup processing;
- tokenization.

---

# 39. Transformation Requirement TRN-035 — No Hidden Postprocessing

Postprocessing that materially modifies output must be explicit.

Examples include:

- punctuation normalization;
- whitespace changes;
- sentence reconstruction;
- formatting;
- filtering;
- content removal.

---

# 40. Transformation Requirement TRN-036 — Transformation Pipeline Transparency

Where multiple transformation stages are used, the system should record the
ordered stages.

Each material stage should have:

- identifier;
- version;
- configuration;
- input/output relationship.

This enables attribution of observed changes.

---

# 41. Transformation Requirement TRN-037 — Stage Isolation

Where practical, transformation stages should be independently testable.

A failure in one stage should be distinguishable from a failure in another.

This requirement supports maintainability and future replacement.

---

# 42. Transformation Requirement TRN-038 — Component Replaceability

Transformation components should be replaceable without requiring unrelated
components to be rewritten.

The architecture must support:

- adding a new transformation method;
- replacing an existing method;
- deprecating a method;
- retaining an old method for historical reproduction.

---

# 43. Transformation Requirement TRN-039 — Capability Lifecycle

Every major transformation capability must have a lifecycle state.

Recommended states:

DISCOVERED
→ EXPERIMENTAL
→ VALIDATED
→ ACTIVE
→ DEPRECATED
→ RETIRED
→ REMOVED

Lifecycle state must be explicit.

---

# 44. Transformation Requirement TRN-040 — Experimental Methods

Experimental transformation methods may be integrated into the research
environment without being considered production-ready.

Experimental methods must not silently become active capabilities.

---

# 45. Transformation Requirement TRN-041 — Validation Before Activation

A transformation method must satisfy its applicable validation criteria before
being classified as active.

Implementation existence alone is insufficient.

---

# 46. Transformation Requirement TRN-042 — Deprecation

A transformation method may be deprecated when:

- better evidence exists;
- a better method supersedes it;
- dependencies become obsolete;
- reproducibility becomes impossible;
- scientific assumptions become invalid.

Deprecation must not erase historical experiment records.

---

# 47. Transformation Requirement TRN-043 — Retirement

Retired methods may remain available for historical reproduction.

Removal is permitted only when:

- retention requirements are satisfied;
- historical evidence remains interpretable;
- dependencies can safely be removed;
- the removal is documented.

---

# 48. Transformation Requirement TRN-044 — No Detector-Specific Coupling

The transformation framework must not be architecturally dependent on a single
detector.

A detector may be used for research or validation without becoming the
definition of transformation behavior.

---

# 49. Transformation Requirement TRN-045 — Evaluator Independence

Transformation methods should remain independent from the evaluation
implementation.

This reduces the risk of optimizing directly against a particular evaluator.

---

# 50. Transformation Requirement TRN-046 — Evaluator Diversity

The transformation framework must permit evaluation against multiple
independent evaluators.

The set of evaluators may change over time without requiring transformation
logic to be rewritten.

---

# 51. Transformation Requirement TRN-047 — Future Method Support

The system must support future transformation methods whose characteristics
are not known at initial implementation.

New methods should be introduced through explicit capability metadata.

---

# 52. Transformation Requirement TRN-048 — Obsolete Method Support

The system must support retirement of obsolete transformation methods without
breaking unrelated active methods.

Historical reproducibility must be considered before removal.

---

# 53. Transformation Requirement TRN-049 — Configuration Compatibility

Configuration schemas should be versioned when changes can alter transformation
behavior.

A historical configuration must remain identifiable.

---

# 54. Transformation Requirement TRN-050 — No Silent Default Changes

Changing a default parameter that materially affects output constitutes a
behavioral change.

Such changes must be versioned or explicitly documented.

---

# 55. Transformation Requirement TRN-051 — Resource Awareness

Transformation must operate within the resource constraints defined by the
project.

Relevant constraints may include:

- memory;
- storage;
- execution time;
- CPU;
- optional external-service usage.

Resource limitations must produce explicit states rather than silently
degrading output quality.

---

# 56. Transformation Requirement TRN-052 — Offline Execution

The production transformation path must be executable without requiring
generative AI inference.

Any research-only external service must remain explicitly separated from the
production transformation path.

---

# 57. Transformation Requirement TRN-053 — No Implicit Cloud Dependency

An external cloud service must not become an implicit dependency of offline
production transformation.

If an external service is intentionally supported, its use must be explicit
and configurable.

---

# 58. Transformation Requirement TRN-054 — External Service Isolation

Where external services are used for research or optional evaluation, the
system must isolate them from the core transformation path.

External service responses must not silently alter experimental conditions.

---

# 59. Transformation Requirement TRN-055 — External Service Provenance

External transformation or research services must record, where available:

- provider;
- service identifier;
- service version;
- request configuration;
- date;
- relevant limitations.

---

# 60. Transformation Requirement TRN-056 — No Uncontrolled Transmission

Protected input must not be transmitted externally without explicit
authorization and configuration.

The default production behavior should avoid external transmission.

---

# 61. Transformation Requirement TRN-057 — Input Integrity

The system must validate the input before transformation.

Validation may include:

- encoding;
- format;
- language;
- content type;
- structural integrity.

Invalid input must not silently enter the normal transformation path.

---

# 62. Transformation Requirement TRN-058 — Input Size

The system must define supported input-size ranges.

Inputs outside validated limits must be explicitly classified.

---

# 63. Transformation Requirement TRN-059 — Long Documents

Long documents must be handled according to explicit segmentation or whole-
document rules.

Segmentation must not introduce unintended semantic or structural changes.

---

# 64. Transformation Requirement TRN-060 — Short Documents

Very short texts may not provide sufficient context for some transformation
methods.

The system must support an explicit insufficient-context state.

---

# 65. Transformation Requirement TRN-061 — Context Preservation

Where a transformation operates on segments, sufficient surrounding context
must be considered to avoid:

- terminology inconsistency;
- pronoun errors;
- discourse errors;
- inconsistent register;
- contradictory local transformations.

---

# 66. Transformation Requirement TRN-062 — Segment Recombination

When transformed segments are recombined, the resulting document must be
treated as a new artifact and evaluated as a whole.

Segment-level success is not sufficient to establish document-level success.

---

# 67. Transformation Requirement TRN-063 — Semantic Guardrails

Where automated semantic checks are available, they should be used as
guardrails rather than as sole proof of equivalence.

A semantic metric cannot replace broader fidelity evaluation.

---

# 68. Transformation Requirement TRN-064 — Factual Guardrails

Where automated factual consistency checks are available, they should be used
to detect likely errors.

A successful factual check does not prove complete factual preservation.

---

# 69. Transformation Requirement TRN-065 — Numerical Guardrails

Numerical and structured factual information should be protected by dedicated
checks where practical.

Changes should be surfaced explicitly.

---

# 70. Transformation Requirement TRN-066 — Protected Spans

The system should support explicitly protected spans.

Protected spans may include:

- numbers;
- names;
- identifiers;
- citations;
- formulas;
- code;
- URLs;
- domain terminology.

Protection rules must be configurable and versioned.

---

# 71. Transformation Requirement TRN-067 — Protection Failure

If a protected span cannot be preserved according to its rule, the system
should fail explicitly rather than silently modifying it.

---

# 72. Transformation Requirement TRN-068 — Constraint Composition

Multiple constraints must be composable.

For example:

- semantic preservation;
- numerical preservation;
- language preservation;
- maximum modification budget.

The system must be able to determine when configured constraints are
incompatible.

---

# 73. Transformation Requirement TRN-069 — Constraint Conflict

When constraints conflict, the system must not silently prioritize one unless
the priority has been explicitly defined.

Unresolvable conflicts should produce an explicit failure or indeterminate
state.

---

# 74. Transformation Requirement TRN-070 — Constraint Versioning

Constraint definitions must be versioned.

Historical experiments must remain associated with the constraint set under
which they were executed.

---

# 75. Transformation Requirement TRN-071 — No Self-Validation

The transformation component must not determine that its output is valid
solely from internal heuristics.

Internal guardrails may reject obviously invalid outputs, but final scientific
acceptance belongs to validation.

---

# 76. Transformation Requirement TRN-072 — Retry Policy

If a transformation fails, retries must be explicit.

The system should record:

- number of attempts;
- configuration changes;
- random seeds where applicable;
- reason for retry;
- final outcome.

Retries must not silently alter experimental conditions.

---

# 77. Transformation Requirement TRN-073 — Candidate Outputs

Where multiple candidate outputs are generated, each candidate must remain
identifiable.

The system must not silently select a candidate according to an undocumented
criterion.

Candidate selection must use an explicit policy.

---

# 78. Transformation Requirement TRN-074 — Candidate Ranking

If candidates are ranked, the ranking criteria must be documented.

Ranking may consider:

- fidelity;
- transformation magnitude;
- linguistic quality;
- experimental objective.

The ranking system must not secretly encode the final acceptance decision.

---

# 79. Transformation Requirement TRN-075 — Early Rejection

Clearly invalid candidates may be rejected before expensive evaluation.

Early rejection criteria must be documented.

Early rejection must not conceal the reason for rejection.

---

# 80. Transformation Requirement TRN-076 — Evaluation Escalation

The system should support escalating evaluation effort.

For example:

1. inexpensive structural checks;
2. inexpensive linguistic checks;
3. semantic/factual checks;
4. expensive evaluation;
5. external research evaluation where explicitly configured.

Escalation must not alter the source or candidate.

---

# 81. Transformation Requirement TRN-077 — Cost-Aware Evaluation

Evaluation effort should be proportional to scientific value and resource
constraints.

Cheap checks should reject clearly invalid candidates before expensive checks
where this does not compromise scientific validity.

---

# 82. Transformation Requirement TRN-078 — No False Certainty

If the transformation framework cannot determine whether a candidate satisfies
a required condition, it must return an indeterminate state rather than
inventing certainty.

---

# 83. Transformation Requirement TRN-079 — Transformation Logs

Material transformation events should be logged.

Logs should support:

- debugging;
- reproducibility;
- audit;
- scientific analysis.

Sensitive input content should not be logged unnecessarily.

---

# 84. Transformation Requirement TRN-080 — Sensitive Data Minimization

The system should minimize retention and exposure of input text.

Logs should prefer identifiers and metadata over complete source content unless
full content retention is scientifically required.

---

# 85. Transformation Requirement TRN-081 — Reproducible Environment

Where environment differences can materially affect output, the system should
record:

- operating environment;
- dependency versions;
- relevant runtime versions;
- configuration;
- transformation version.

---

# 86. Transformation Requirement TRN-082 — Reproducible Output

Given the same:

- source;
- transformation version;
- configuration;
- environment;
- random state where applicable;

the system should reproduce the same output where deterministic reproduction
is technically possible.

---

# 87. Transformation Requirement TRN-083 — Scientific Repetition

Where transformation behavior is stochastic, important findings should be
evaluated across repeated runs.

A single successful output must not establish robust behavior if stochastic
variability is material.

---

# 88. Transformation Requirement TRN-084 — Batch Consistency

When transforming multiple documents under the same configuration, the system
should apply equivalent rules.

Batch-specific differences must be attributable to explicit conditions.

---

# 89. Transformation Requirement TRN-085 — No Cross-Input Contamination

Transformation of one input must not unintentionally modify the behavior or
content of another input.

State must be isolated unless shared state is explicitly part of the
experiment.

---

# 90. Transformation Requirement TRN-086 — Cache Transparency

If caching is used, cached results must be associated with the relevant:

- source identifier;
- transformation version;
- configuration;
- environment.

A stale cache must not silently produce an invalid result.

---

# 91. Transformation Requirement TRN-087 — Cache Invalidation

Material changes to transformation behavior must invalidate incompatible
cached results.

Historical cached results may be retained for reproducibility.

---

# 92. Transformation Requirement TRN-088 — Failure Reproducibility

Where possible, failures must be reproducible from their recorded conditions.

A transient infrastructure failure must be distinguishable from a scientific
transformation failure.

---

# 93. Transformation Requirement TRN-089 — Error Classification

Errors should distinguish:

- scientific failure;
- transformation failure;
- infrastructure failure;
- configuration failure;
- resource failure;
- unsupported condition.

This distinction is required for correct diagnosis.

---

# 94. Transformation Requirement TRN-090 — Scientific Failure versus Technical Failure

A transformation that cannot execute is not equivalent to a transformation
that executes but violates fidelity.

The system must distinguish:

TECHNICAL FAILURE
from
SCIENTIFIC FAILURE.

---

# 95. Transformation Requirement TRN-091 — Output Status

Every transformation attempt should result in an explicit status.

Recommended states include:

- SUCCESS;
- FAILED;
- REJECTED;
- INDETERMINATE;
- UNSUPPORTED;
- CANCELLED.

The meaning of each state must be documented.

---

# 96. Transformation Requirement TRN-092 — Candidate Acceptance

A candidate must not be labeled scientifically accepted merely because
transformation execution succeeded.

Execution status and scientific acceptance are separate states.

---

# 97. Transformation Requirement TRN-093 — Provenance Chain

The complete chain should be reconstructable:

SOURCE
→ PREPROCESSING
→ TRANSFORMATION STAGES
→ POSTPROCESSING
→ OUTPUT
→ EVALUATION

Any omitted stage that can materially affect the result must be identified.

---

# 98. Transformation Requirement TRN-094 — Change Attribution

Where possible, the system should support attribution of output changes to
specific transformation stages.

This facilitates:

- debugging;
- scientific analysis;
- regression diagnosis;
- component replacement.

---

# 99. Transformation Requirement TRN-095 — Regression Detection

Changes to a transformation method must be tested against representative
historical inputs.

Regression testing should consider:

- output changes;
- fidelity;
- resource consumption;
- language coverage;
- failure behavior.

---

# 100. Transformation Requirement TRN-096 — Historical Compatibility

When a transformation method is updated, the project must distinguish:

- behavior-compatible revisions;
- behavior-changing revisions.

Behavior-changing revisions must not silently replace historical results.

---

# 101. Transformation Requirement TRN-097 — Backward Reproduction

Where scientifically necessary, historical transformation versions should
remain reproducible.

The project may retain:

- old implementation;
- containerized environment;
- frozen dependency set;
- archived metadata;
- representative artifacts.

---

# 102. Transformation Requirement TRN-098 — Resource Budget Transparency

If a transformation cannot satisfy configured resource limits, the system
must report the resource condition explicitly.

It must not silently reduce scientific quality to fit the budget.

---

# 103. Transformation Requirement TRN-099 — Extensibility

The transformation framework must be extensible to:

- new methods;
- new languages;
- new constraints;
- new preprocessing stages;
- new postprocessing stages;
- new evaluation interfaces.

Extensibility must not require redesign of unrelated scientific definitions.

---

# 104. Transformation Requirement TRN-100 — Maintainability

Transformation components must remain understandable and maintainable.

Each major component should have:

- purpose;
- inputs;
- outputs;
- configuration;
- dependencies;
- lifecycle;
- validation status;
- known limitations.

---

# 105. Transformation Requirement TRN-101 — Documentation Synchronization

Changes to transformation behavior must trigger documentation impact analysis.

Relevant documentation may include:

- scientific specification;
- architecture;
- validation;
- research registry;
- decision log;
- capability registry;
- change queue.

---

# 106. Transformation Requirement TRN-102 — Research Traceability

Every major transformation capability should be traceable to its scientific
basis.

The system must identify whether a capability is based on:

- published evidence;
- project experiment;
- engineering heuristic;
- empirical calibration;
- unresolved hypothesis.

---

# 107. Transformation Requirement TRN-103 — Evidence Status

Scientific assumptions behind a transformation must have an evidence status.

Recommended states include:

- ESTABLISHED;
- SUPPORTED;
- PRELIMINARY;
- UNCERTAIN;
- CONTRADICTED;
- OBSOLETE.

---

# 108. Transformation Requirement TRN-104 — Research Updates

When new evidence materially changes the validity of a transformation method,
the capability must be reassessed.

Possible outcomes include:

- unchanged;
- recalibrated;
- restricted;
- experimental;
- deprecated;
- retired.

---

# 109. Transformation Requirement TRN-105 — Future Evaluator Independence

Future detectors, watermark methodologies or other evaluators must be
integrable without requiring transformation logic to know their internal
implementation.

The transformation layer should expose stable output artifacts and metadata.

---

# 110. Transformation Requirement TRN-106 — No Hard-Coded Scientific Assumptions

Scientific assumptions that may change with future research must not be
hard-coded into low-level transformation logic where avoidable.

Such assumptions should be represented as configuration, policy or versioned
scientific specifications.

---

# 111. Transformation Requirement TRN-107 — Policy Evolution

When a future scientific policy changes the interpretation of acceptable
transformation behavior, the system must permit the policy to evolve without
rewriting unrelated components.

Historical policy versions must remain identifiable.

---

# 112. Transformation Requirement TRN-108 — Capability Registry

Major transformation capabilities should be discoverable through a registry
containing at least:

- identifier;
- version;
- lifecycle state;
- languages;
- dependencies;
- validation state;
- research basis;
- known limitations.

---

# 113. Transformation Requirement TRN-109 — Safe Removal

Removing an obsolete transformation capability must not silently invalidate
historical scientific evidence.

Before removal, the project must determine whether the capability is required
for:

- reproduction;
- comparison;
- certification;
- audit.

---

# 114. Transformation Requirement TRN-110 — No Automatic Promotion

A newly implemented transformation method must not automatically become the
default production method.

Promotion requires the applicable validation and governance conditions.

---

# 115. Transformation Requirement TRN-111 — Default Method Stability

Changing the default transformation method is a material behavioral change.

It must be versioned and documented.

Existing experiments must remain associated with the method originally used.

---

# 116. Transformation Requirement TRN-112 — Explicit Experimental Objective

Every transformation run must identify the experimental objective against
which its output will be evaluated.

An unspecified objective must not be inferred from a detector result.

---

# 117. Transformation Requirement TRN-113 — Objective/Method Separation

Multiple transformation methods must be capable of being evaluated against the
same experimental objective.

This permits scientifically meaningful comparison between methods.

---

# 118. Transformation Requirement TRN-114 — Method/Language Separation

Where possible, language support should be represented independently from
transformation-method identity.

This permits:

- one method supporting multiple languages;
- multiple methods supporting the same language;
- language-specific specialization;
- gradual expansion of language coverage.

---

# 119. Transformation Requirement TRN-115 — Experimental Matrix

The project should support an explicit experimental matrix crossing relevant
dimensions such as:

- transformation method;
- language;
- domain;
- text length;
- source type;
- evaluation configuration;
- detector configuration.

This prevents accidental generalization from a narrow experiment.

---

# 120. Transformation Requirement TRN-116 — Controlled Comparison

Two transformation methods should be compared under equivalent experimental
conditions whenever the scientific question requires direct comparison.

Differences in:

- corpus;
- language;
- preprocessing;
- evaluation;
- thresholds;

must be recorded.

---

# 121. Transformation Requirement TRN-117 — No Cherry-Picking

The project must not select only favorable outputs or documents when reporting
aggregate transformation performance.

Selection criteria must be defined before final evaluation where practical.

---

# 122. Transformation Requirement TRN-118 — Failed Candidates

Failed candidate outputs should be retained when required for scientific
analysis.

Failure examples are scientifically valuable for understanding limitations.

---

# 123. Transformation Requirement TRN-119 — Distribution Reporting

Transformation results should be reported as distributions where appropriate,
not only as best-case examples.

Relevant statistics may include:

- success rate;
- failure rate;
- transformation magnitude;
- fidelity distribution;
- language-specific distribution.

---

# 124. Transformation Requirement TRN-120 — Worst-Case Analysis

Important evaluations should include worst-case analysis.

The project should identify:

- severe fidelity failures;
- maximum transformation;
- language-specific failures;
- domain-specific failures;
- pathological inputs.

---

# 125. Transformation Requirement TRN-121 — Boundary Conditions

The validated operating boundary of a transformation must be explicit.

Potential boundaries include:

- supported languages;
- minimum text length;
- maximum text length;
- supported domains;
- supported formats;
- resource limits;
- required preprocessing.

---

# 126. Transformation Requirement TRN-122 — Boundary Enforcement

When input falls outside a validated boundary, the system must not silently
report normal success.

It must report the applicable boundary condition.

---

# 127. Transformation Requirement TRN-123 — Scientific Uncertainty

Transformation performance may be uncertain.

The system must support reporting:

- measured;
- estimated;
- insufficient evidence;
- indeterminate.

Uncertainty must not be converted into certainty.

---

# 128. Transformation Requirement TRN-124 — No Absolute Claims

The transformation system must not claim universal success based on finite
experiments.

All claims must remain bounded by:

- language;
- corpus;
- domain;
- evaluator;
- version;
- experimental conditions.

---

# 129. Transformation Requirement TRN-125 — Reassessment Triggers

The transformation specification must be reassessed when:

- new scientific evidence appears;
- a new transformation family is introduced;
- a detector methodology materially changes;
- a watermark methodology materially changes;
- a new language is added;
- a major metric is replaced;
- a major failure mode is discovered;
- an existing assumption is contradicted.

---

# 130. Transformation Requirement TRN-126 — No Silent Scientific Drift

Implementation changes must not silently alter:

- the definition of fidelity;
- transformation objectives;
- hard constraints;
- acceptance criteria;
- supported conditions.

Such changes require specification-level documentation.

---

# 131. Transformation Requirement TRN-127 — Auditability

A transformation result must be explainable from its recorded artifacts.

An auditor should be able to determine:

- what was transformed;
- by what method;
- with which version;
- under which configuration;
- with what intermediate stages;
- producing what output.

---

# 132. Transformation Requirement TRN-128 — Reversible Development

Transformation development must permit rollback.

Changes should be made in a manner that permits recovery of the previous
validated behavior.

---

# 133. Transformation Requirement TRN-129 — Controlled Rollout

A materially new transformation method should be capable of being evaluated
experimentally before becoming the default.

Possible rollout states include:

- experimental;
- shadow;
- candidate;
- active.

---

# 134. Transformation Requirement TRN-130 — Shadow Evaluation

Where practical, a new transformation method may be evaluated against the
same inputs as the active method without replacing the active method.

This enables comparison before promotion.

---

# 135. Transformation Requirement TRN-131 — Rollback

If a newly promoted transformation method introduces unacceptable regressions,
the system must support rollback to the previous validated method.

Rollback must preserve evidence of the failed release.

---

# 136. Transformation Requirement TRN-132 — Release Evidence

Promotion of a transformation method must be supported by evidence including,
as applicable:

- validation results;
- regression results;
- supported-language results;
- resource measurements;
- known limitations;
- configuration;
- version;
- research basis.

---

# 137. Transformation Requirement TRN-133 — Scientific Certification

A transformation capability may be certified only when the applicable
validation requirements have been satisfied.

Certification is a separate lifecycle state from implementation completion.

---

# 138. Transformation Requirement TRN-134 — Certification Expiration

Certification may become invalid when:

- requirements change;
- major scientific evidence changes;
- evaluator methodology changes materially;
- dependencies change materially;
- the transformation implementation changes.

The project must support reassessment.

---

# 139. Transformation Requirement TRN-135 — Continuous Scientific Review

The transformation framework must remain open to periodic reassessment.

It must not be considered scientifically complete merely because the initial
implementation passes its initial test suite.

---

# 140. Transformation Requirement TRN-136 — Final Principle

A transformation is not successful because it produces an output.

It is successful only when the output can be independently evaluated and
shown to satisfy the applicable scientific requirements under the defined
conditions.

The transformation layer must therefore remain:

- minimal where possible;
- preservation-first;
- explicit;
- reproducible;
- language-aware;
- modular;
- independently evaluable;
- auditable;
- extensible;
- replaceable;
- scientifically revisable.