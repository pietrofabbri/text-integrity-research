# Scientific Specification Map

**Status:** ACTIVE
**Version:** 0.2 (2026-09-12: DCQ-006/007/008 propagation notes added to
§17, §20-23, §25-26, per DECISION-LOG.md DEC-016)
**Document type:** Scientific and functional specification architecture
**Authority:** Normative within the project
**Scope:** Definition of measurable system objectives, requirements,
constraints, evaluation dimensions and capability boundaries

---

## 1. Purpose

This document defines the structure of the scientific specification of the
project.

The scientific specification translates validated research knowledge into
explicit, measurable and testable requirements.

It does not prescribe implementation details unless an implementation
constraint is itself scientifically necessary.

The specification must answer:

- what the system is expected to accomplish;
- what properties the output must preserve;
- how much modification is acceptable;
- how effectiveness is measured;
- how uncertainty is represented;
- how multilingual differences are handled;
- how new scientific knowledge can modify requirements;
- when a capability is considered valid, obsolete or insufficient.

---

# 2. Fundamental Objective

The system is intended to transform an input text while preserving the
maximum possible fidelity to that input and satisfying the project's
validated text-integrity objectives.

The fundamental optimization principle is:

> Achieve the required validated objective with the minimum necessary
> transformation of the input text.

The system must not optimize transformation magnitude independently of
content preservation.

A smaller change that introduces a factual or semantic error is worse than a
larger change that is demonstrably necessary to preserve correctness.

---

# 3. Scientific Specification Boundaries

The specification is divided into:

1. functional requirements;
2. content-preservation requirements;
3. transformation-minimality requirements;
4. linguistic-quality requirements;
5. analytical/evaluation requirements;
6. multilingual requirements;
7. robustness requirements;
8. reproducibility requirements;
9. extensibility requirements;
10. uncertainty requirements;
11. lifecycle requirements.

---

# 4. Requirement Classification

Every requirement should have a unique identifier.

Recommended identifiers:

- `FR` — Functional Requirement
- `SEM` — Semantic Preservation Requirement
- `FACT` — Factual Preservation Requirement
- `STR` — Structural Preservation Requirement
- `MIN` — Minimality Requirement
- `LING` — Linguistic Quality Requirement
- `MULTI` — Multilingual Requirement
- `ROB` — Robustness Requirement
- `EVAL` — Evaluation Requirement
- `DATA` — Data Requirement
- `SEC` — Security-related Scientific Requirement
- `EXT` — Extensibility Requirement
- `LIFE` — Lifecycle Requirement

Each requirement should additionally record:

- priority;
- source;
- rationale;
- validation method;
- dependencies;
- current status;
- affected languages;
- affected capabilities.

---

# 5. Requirement Status

Recommended statuses:

- PROPOSED
- UNDER_REVIEW
- ACCEPTED
- VALIDATED
- CONDITIONAL
- DEPRECATED
- RETIRED
- REJECTED

A requirement must not silently change status.

Status changes should be traceable through the project decision system.

**Cross-reference:** `S02-scientific-requirements.md` § 24 "Requirement
Lifecycle" defines a related but non-identical sequence for the same
underlying concept (`PROPOSED → REVIEWED → ACCEPTED → VERIFIED → ACTIVE →
SUPERSEDED → RETIRED` vs. this section's `PROPOSED, UNDER_REVIEW, ACCEPTED,
VALIDATED, CONDITIONAL, DEPRECATED, RETIRED, REJECTED`). Neither
vocabulary has been reconciled with the other; which one is authoritative
is a HUMAN DECISION REQUIRED item — see
`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §5S/§13S.
Note also that § 33 "Capability Lifecycle" in this document is a distinct
vocabulary for *capability*-level (not *requirement*-level) lifecycle and
may be the more apt comparandum if what you intend to reconcile is
capability state rather than requirement state. Added 2026-08-29.

---

# 6. Functional Specification

The system must conceptually support the following workflow:

Input
→ Analysis
→ Candidate transformation
→ Validation
→ Acceptance / rejection
→ Output

The architecture may implement additional intermediate stages.

The specification does not require a specific algorithm.

---

# 7. Input Integrity

The system must preserve the original input exactly for comparison.

The original text must remain available throughout the processing lifecycle.

The system should preserve, where relevant:

- Unicode content;
- whitespace information;
- punctuation;
- capitalization;
- paragraph boundaries;
- sentence boundaries;
- headings;
- lists;
- numerical values;
- units;
- references;
- citations;
- links;
- markup.

Where normalization is required internally, the normalized representation
must not replace the canonical original representation.

---

# 8. Output Integrity

The output must be represented as a distinct artifact.

The system must be able to determine:

- what changed;
- where it changed;
- how much it changed;
- why the change occurred;
- which validation criteria were affected.

The final output must not contain accidental modifications introduced by
formatting, encoding or serialization.

---

# 9. Semantic Preservation

Semantic preservation is a primary requirement.

The output should preserve the meaning of the input to the maximum extent
supported by the validated methodology.

Evaluation should consider:

- sentence meaning;
- paragraph meaning;
- discourse relations;
- causal relations;
- temporal relations;
- logical relations;
- modality;
- negation;
- conditions;
- scope;
- implications.

A generic similarity score is insufficient as the sole semantic acceptance
criterion.

**Cross-reference:** the requirement-ID-level definition of this dimension
is `S04-fidelity-requirements.md` § 4, FID-001 — Semantic Preservation.
Added 2026-08-29 per the Q001 cross-area audit
(`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §4S).

---

# 10. Factual Preservation

The system must preserve factual information unless an explicit,
user-authorized transformation objective states otherwise.

Special attention must be given to:

- names;
- people;
- organizations;
- places;
- dates;
- times;
- numbers;
- measurements;
- currencies;
- units;
- percentages;
- technical terminology;
- references;
- citations;
- URLs;
- identifiers.

Numerical and entity changes should be subject to deterministic or
high-confidence validation whenever technically possible.

**Cross-reference:** the requirement-ID-level definition of this dimension
is `S04-fidelity-requirements.md` § 6, FID-003 — Factual Preservation.
Added 2026-08-29 per the Q001 cross-area audit
(`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §4S).

---

# 11. Structural Preservation

The system should preserve document structure unless a transformation is
strictly necessary.

Relevant structures include:

- paragraphs;
- headings;
- lists;
- tables;
- quotations;
- footnotes;
- references;
- markup;
- inline formatting;
- code;
- formulas.

Structural equivalence is separate from semantic equivalence.

**Cross-reference:** the requirement-ID-level definition of this dimension
is `S04-fidelity-requirements.md` § 19, FID-016 — Structural Preservation.
Added 2026-08-29 per the Q001 cross-area audit
(`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §4S).

---

# 12. Minimality

Minimality is a first-class objective.

The system should minimize unnecessary modifications across multiple levels:

- character;
- token;
- lexical;
- syntactic;
- sentence;
- paragraph;
- structural;
- semantic.

No single distance metric should be treated as a universal definition of
minimality.

**Cross-reference:** the requirement-ID-level definition of this dimension
is `S04-fidelity-requirements.md` § 24, FID-021 — Minimality, and
`S05-transformation-requirements.md` § 11, TRN-007 — Minimal Intervention.
Added 2026-08-29 per the Q001 cross-area audit
(`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §4S).

---

# 13. Transformation Budget

The project should support a concept of transformation budget.

A transformation budget may constrain:

- maximum percentage of changed tokens;
- maximum number of changed sentences;
- maximum structural modifications;
- maximum semantic deviation;
- maximum factual risk.

The actual thresholds must be determined empirically through validation.

Thresholds must therefore remain configurable and versioned.

---

# 14. No-Unnecessary-Generation Principle

The system should prefer deterministic or minimally generative operations
when these can satisfy the validated objective without reducing quality.

Where generation is required, it should be constrained by:

- source context;
- preservation rules;
- transformation budget;
- validation;
- rollback capability.

The system should not generate additional content merely to make the output
appear different.

---

# 15. Human-Likeness and Linguistic Quality

"Linguistic naturalness" must be treated as a measurable research
hypothesis, not as a binary property.

Evaluation may include:

- grammaticality;
- fluency;
- coherence;
- lexical appropriateness;
- stylistic consistency;
- register consistency;
- discourse naturalness;
- language-specific norms.

The project must not equate:

human-like
=
not AI-generated
=
watermark-free
=
linguistically natural.

These are distinct properties.

**Cross-reference:** the requirement-ID-level definition of the linguistic
dimension is `S04-fidelity-requirements.md` § 16, FID-013 — Linguistic
Correctness. Added 2026-08-29 per the Q001 cross-area audit
(`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §4S).

---

# 16. Watermark-Related Requirements

The scientific specification may define requirements concerning the
behavior of known watermark mechanisms.

However, requirements must be derived from validated scientific evidence.

The project must distinguish:

- known watermark families;
- known detector behavior;
- experimentally observed signals;
- theoretical vulnerabilities;
- unsupported assumptions.

A future watermark must not be considered covered merely because it belongs
to the same broad category as a previously studied mechanism.

---

# 17. AI-Detection-Related Requirements

The specification must not treat any individual AI detector as universal
ground truth.

Where detector measurements are used for validation, the specification
should preserve:

- detector identity;
- detector version;
- date;
- configuration;
- language;
- text length;
- result;
- confidence;
- threshold;
- relevant API or service conditions.

Detector measurements must be reproducible where the external system allows
it.

**Note (2026-09-12, DCQ-007, per DECISION-LOG.md DEC-016):** Detector
reliability is not uniform across writer populations —
`RESEARCH-REGISTRY.md` R-0022 (RESEARCH EVIDENCE) documents a
well-confirmed non-native-writer detection bias (elevated false-positive
rates for non-native writers on evaluated classifiers). Any use of
detector output for a specification-level decision should treat
writer-population bias as a known, evidenced confounder rather than an
unmodeled residual error. This note records the finding; it does not
itself define a bias-correction mechanism.

---

# 18. Multi-Detector Evaluation

Where scientifically justified, evaluation should use multiple independent
measurement systems.

The system should preserve individual detector results rather than reducing
them immediately to a single binary verdict.

A disagreement between detectors is itself a measurable result.

---

# 19. Watermark and Detector Coverage

Coverage must be represented as a versioned capability matrix.

At minimum:

| Technique / Detector | Languages | Version | Evidence | Validation | Status |
|----------------------|-----------|---------|----------|------------|--------|

A capability marked ACTIVE must have a documented validation basis.

---

# 20. Multilingual Specification

Initial target languages are:

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

This list is a project priority, not a claim that all languages have equal
scientific support.

**Note (2026-09-12, DCQ-006, per DECISION-LOG.md DEC-016):** Per
`KNOWLEDGE-BACKLOG.md` KB-008 (Correction, 2026-08-24), AI-text-detection
literature evidence exists for all 13 languages listed above, though depth
varies by language; watermarking literature evidence is comparatively
thin and does not yet cover all 13 languages at the same depth (see
`docs/02-research/R05-multilingual-linguistic-research.md` §47.1,
R-0046-R-0073). This is the specific evidence behind the "not a claim of
equal scientific support" statement above.

---

# 21. Language-Specific Requirements

Each language must be evaluated independently for:

- tokenization;
- segmentation;
- morphology;
- syntax;
- writing system;
- punctuation;
- linguistic naturalness;
- semantic preservation;
- factual preservation;
- detector behavior;
- watermark behavior;
- benchmark availability.

A multilingual component must not be considered validated for all supported
languages merely because it passes tests in one language.

**Note (2026-09-12, DCQ-008, per DECISION-LOG.md DEC-016):** For "factual
preservation" specifically, no evidence-backed multilingual factual/claim
-consistency option currently exists (`KNOWLEDGE-BACKLOG.md` KB-013;
`RESEARCH-REGISTRY.md` R-0109-R-0112) — see
`docs/04-architecture/VALIDATION-ARCHITECTURE.md` §6 for the architectural
consequence (`DECISION-LOG.md` DEC-015's `VALIDATE-FACTUAL-CLAIM`
category). For "detector behavior," local AI-text detection is currently
bounded by accuracy and cross-lingual robustness rather than storage, with
near-chance accuracy observed for several target languages among
presently available local options (KB-014; R-0113-R-0118). See also §17's
note on non-native-writer bias (R-0022, DCQ-007) — a related but distinct
confounder.

---

# 22. Language Capability States

Each language should have a capability state:

- NOT_SUPPORTED
- RESEARCH_ONLY
- EXPERIMENTAL
- VALIDATED
- ACTIVE
- DEGRADED
- DEPRECATED
- RETIRED

A language may have different states for different capabilities.

For example:

- semantic preservation: VALIDATED;
- watermark analysis: RESEARCH_ONLY;
- external detector integration: NOT_SUPPORTED.

**Note (2026-09-12, DCQ-006/DCQ-008, per DECISION-LOG.md DEC-016):**
These per-capability-per-language states must be assigned individually
rather than defaulted uniformly. Current research evidence (not itself a
capability-state assignment — that remains separate implementation/
validation work) points toward: AI-text-detection capability states
varying by language and generally ahead of watermark-analysis states
(KB-008 correction, R-0046-R-0073); no language currently qualifying for a
VALIDATED multilingual factual/claim-consistency state (KB-013,
R-0109-R-0112); and local-detector capability states that should not be
set to VALIDATED or ACTIVE for a language beyond what its evidenced
accuracy and cross-lingual robustness supports (KB-014, R-0113-R-0118).
This note records the evidence; it does not assign any state.

---

# 23. Robustness Specification

The system must evaluate relevant behavior under controlled text changes.

Potential conditions include:

- proofreading;
- human editing;
- punctuation changes;
- spelling correction;
- translation;
- back-translation;
- paraphrasing;
- sentence restructuring;
- formatting;
- text-length changes.

Robustness claims must identify the exact transformation conditions.

**Note (2026-09-12, DCQ-006, per DECISION-LOG.md DEC-016):** No
requirement in this specification should be read as assuming
watermark-based or classifier-based detection remains reliable after
paraphrasing or translation. Evidence on file shows detection degrading
sharply under both: detection rate below 0.3 after a single paraphrase
pass, across all evaluated schemes (`RESEARCH-REGISTRY.md` R-0039), and
AUC/F1 dropping to 0.55-0.82 after translation, depending on scheme and
language pair (R-0065, R-0066, R-0068, R-0069; see
`docs/00-project/KNOWLEDGE-BACKLOG.md` KB-011). A robustness claim under
this section must therefore not extrapolate a technique's untested
performance under paraphrasing or translation from its performance under
other conditions.

---

# 24. Uncertainty

The system must represent uncertainty explicitly.

It must be possible to distinguish:

- validated;
- likely;
- uncertain;
- unsupported;
- unknown.

The absence of evidence must not be represented as evidence of absence.

---

# 25. Acceptance Criteria

A transformation must not be accepted solely because it satisfies one
measurement.

Acceptance should consider the relevant combination of:

- objective completion;
- semantic preservation;
- factual preservation;
- structural preservation;
- linguistic quality;
- minimality;
- robustness;
- known detector/watermark coverage;
- uncertainty;
- regression status.

The exact acceptance policy must be versioned.

**Note (2026-09-12, DCQ-007, per DECISION-LOG.md DEC-016):** Where
acceptance criteria rely on a detector's false-positive rate (FPR) as part
of "known detector/watermark coverage," FPR alone is not sufficient to
judge real-world acceptability without an accompanying prevalence
estimate for the population being evaluated — `RESEARCH-REGISTRY.md`
R-0086 (RESEARCH EVIDENCE); see `docs/00-project/OPEN-QUESTIONS.md` Q-003.
This document does not yet define a prevalence-aware acceptance policy; it
records that any future one must account for this argument rather than
treating a bare FPR threshold as sufficient.

---

# 26. Failure and Rejection

A candidate transformation should be rejected when:

- factual information is altered unexpectedly;
- semantic deviation exceeds the applicable threshold;
- structural integrity is violated;
- linguistic quality falls below the applicable threshold;
- transformation exceeds its allowed budget;
- required validation fails;
- the measurement is inconclusive where certainty is required;
- a regression is detected;
- the capability is not valid for the applicable language.

Failure must be observable and diagnosable.

**Note (2026-09-12, DCQ-007, per DECISION-LOG.md DEC-016):** A rejection
or acceptance decision driven by a detector's reported false-positive rate
should be interpreted alongside a prevalence estimate for the relevant
population (R-0086; see §25's note) and should not be confused with the
population-level base rate of the condition being detected. Separately,
non-native-writer status is a documented confounder for false-positive
behavior specifically (R-0022; see §17's note) and should not be silently
absorbed into a single undifferentiated FPR figure.

---

# 27. No Universal Success Claim

The system must not claim universal success against all possible future
watermarking or detection mechanisms.

The correct scientific representation is:

> effectiveness is evaluated against a versioned, explicitly defined
> evaluation profile.

An evaluation profile contains:

- techniques;
- detectors;
- versions;
- languages;
- datasets;
- transformations;
- metrics;
- thresholds;
- date;
- evidence baseline.

---

# 28. Effectiveness Profiles

The project should support multiple profiles.

Examples:

- baseline;
- conservative;
- multilingual;
- research;
- regression;
- release certification.

Profiles must be versioned.

A new scientific discovery may require creation or modification of a
profile.

---

# 29. Evolution of Effectiveness

Effectiveness is not a permanent property.

When new evidence appears, the project must determine whether it changes:

- evaluation coverage;
- acceptance criteria;
- supported languages;
- transformation methods;
- validation thresholds;
- architecture;
- certification status.

A release may therefore remain historically valid while becoming
scientifically outdated.

---

# 30. Reproducibility

A scientific result must be reproducible to the maximum extent allowed by
its dependencies.

Each evaluation should record:

- software version;
- configuration;
- dataset version;
- model version;
- detector version;
- language;
- test corpus;
- metrics;
- thresholds;
- date;
- environment where relevant.

---

# 31. Regression Requirements

Every accepted capability must have regression tests.

Regression testing must verify at least the relevant:

- semantic properties;
- factual properties;
- structural properties;
- language properties;
- minimality properties;
- detector/watermark evaluation properties.

Removing or modifying a capability must also update its regression suite.

---

# 32. Extensibility Requirements

The scientific specification must not encode today's techniques as permanent
architectural assumptions.

New techniques should be addable through modular capability definitions.

Each capability should be independently:

- identifiable;
- configurable;
- measurable;
- testable;
- activatable;
- deactivatable;
- deprecated;
- retired.

---

# 33. Capability Lifecycle

The scientific state of a capability follows:

DISCOVERED
→ RESEARCHED
→ EXPERIMENTAL
→ VALIDATED
→ ACTIVE
→ DEGRADED / DEPRECATED
→ RETIRED

A capability must not be activated solely because an implementation exists.

---

# 34. Scientific Dependencies

Each important requirement should identify its dependencies.

Examples:

Research finding
→ requirement
→ metric
→ benchmark
→ implementation
→ validation

If a dependency becomes obsolete, affected requirements must be reviewed.

---

# 35. External Services

External detectors or analytical services may be used as optional validation
evidence.

They must not silently become required runtime dependencies.

Where an external service is used, the project must document:

- service identity;
- API/version;
- terms;
- privacy implications;
- data transmission;
- reproducibility limitations;
- fallback behavior.

---

# 36. Offline Core Requirement

The core system must remain executable without access to external AI
services.

Optional external evaluation must be architecturally isolated from the
offline core.

Loss of an external service must not corrupt the local processing pipeline.

---

# 37. Zero-Cost Runtime Principle

The project should prefer freely available software and research resources
for the runtime and validation stack.

This does not prohibit paid development or maintenance labor.

Licensing and redistribution conditions remain mandatory constraints.

---

# 38. Resource Constraints

The project has an approximate storage budget of 30 GB for the overall
research/software environment.

Scientific requirements must therefore distinguish between:

- essential assets;
- optional assets;
- downloadable assets;
- generated temporary assets;
- archival assets.

Resource-intensive approaches must justify their value.

---

# 39. Security-Related Scientific Constraints

The specification must distinguish between:

- defensive evaluation;
- measurement;
- research;
- production transformation.

A scientific finding describing a potential weakness does not automatically
authorize operational use of that weakness.

Security boundaries are defined in the security documentation.

---

# 40. Documentation Traceability

Every major requirement must eventually be traceable to:

- research evidence;
- decision or rationale;
- architecture;
- implementation;
- validation;
- certification.

Requirements without a clear origin must be marked as assumptions or open
questions until resolved.

---

# 41. Specification Change Process

A specification change must identify:

1. what changed;
2. why it changed;
3. evidence supporting the change;
4. affected requirements;
5. affected architecture;
6. affected tests;
7. affected datasets;
8. affected certification criteria;
9. whether backward compatibility is required.

Changes must be recorded through the project's documentation governance
system.

---

# 42. Obsolescence

A requirement may become obsolete because:

- scientific evidence changed;
- a technique disappeared;
- a detector became unavailable;
- a benchmark became invalid;
- a language capability changed;
- a better methodology replaced it;
- a security concern emerged.

Obsolete requirements must be deprecated before retirement unless immediate
removal is required by a safety or integrity condition.

Historical traceability must be preserved.

---

# 43. Scientific Quality Gates

Before a requirement is marked VALIDATED, the project should demonstrate:

1. a defined measurement;
2. a defined acceptance criterion;
3. an appropriate dataset;
4. a reproducible evaluation procedure;
5. relevant language coverage;
6. known limitations;
7. regression coverage;
8. traceability to scientific evidence.

---

# 44. Required Detailed Specification Documents

The following are candidate future documents.

They should only be created when the corresponding area has enough
substance to justify a separate maintenance boundary.

Potential documents include:

- `CORE-REQUIREMENTS.md`
- `SEMANTIC-FIDELITY-SPEC.md`
- `FACTUAL-PRESERVATION-SPEC.md`
- `MINIMALITY-SPEC.md`
- `LINGUISTIC-QUALITY-SPEC.md`
- `MULTILINGUAL-SPEC.md`
- `WATERMARK-COVERAGE-SPEC.md`
- `DETECTOR-EVALUATION-SPEC.md`
- `ROBUSTNESS-SPEC.md`
- `EFFECTIVENESS-PROFILES.md`
- `CAPABILITY-LIFECYCLE-SPEC.md`
- `REPRODUCIBILITY-SPEC.md`

These are not yet mandatory.

## 44.1 Existing Specification Documents (Index)

Unlike the candidate documents above, the following already exist in
`docs/03-scientific-specification`:

| ID | File | Status | Scope |
|---|---|---|---|
| S01 | `S01-system-objectives.md` | NORMATIVE / FOUNDATIONAL | System-level scientific objectives |
| S02 | `S02-scientific-requirements.md` | NORMATIVE | S01 objectives converted into testable requirements |
| S03 | `S03-experimental-model.md` | NORMATIVE / SCIENTIFIC | Abstract experimental model and measurement framework |
| S04 | `S04-fidelity-requirements.md` | NORMATIVE | Content-preservation (fidelity) requirements |
| S05 | `S05-transformation-requirements.md` | NORMATIVE | Transformation-minimality requirements |

S04 and S05 were originally drafted as `S02-fidelity-requirements.md` and
`S03-transformation-requirements.md` respectively, colliding with the IDs
above. They were renumbered on 2026-08-22 rather than merged, because
their scope (content-preservation, transformation-minimality) is distinct
from S02/S03's scope and matches boundary categories already listed in
§3. See `DEC-011` in `docs/00-project/DECISION-LOG.md`.

This index should be updated whenever a document in this range is added,
renumbered, retired, or promoted from the candidate list above.

---

# 45. Relationship With Other Project Areas

## Research

Provides scientific evidence and identifies phenomena requiring
measurement.

## Architecture

Implements the specification while preserving modularity.

## Validation

Determines whether requirements are actually satisfied.

## Security

Defines security boundaries around sensitive or potentially adversarial
capabilities.

## Data

Provides datasets and benchmark assets required for validation.

## Development

Defines how requirements become implementation changes.

## Operations

Defines how validated capabilities are deployed, updated and retired.

## Certification

Determines whether a specific release satisfies its declared scientific
profile.

---

# 46. Current Specification State

The scientific specification is currently in the structural-definition
phase.

Detailed thresholds and algorithms must not be invented prematurely.

Where empirical evidence is required, the requirement should initially be
expressed as a measurable objective whose threshold is determined through
research and validation.

---

# 47. Governing Principle

The specification must define what "good" means without prematurely deciding
how "good" must be achieved.

Scientific requirements must be:

- measurable;
- testable;
- traceable;
- versioned;
- language-aware;
- uncertainty-aware;
- updateable;
- removable when obsolete.

The system is not considered scientifically complete merely because it
produces output.

It is complete only when its output can be evaluated against an explicit,
reproducible and continuously maintainable specification.