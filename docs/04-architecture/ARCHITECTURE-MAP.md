# Architecture Map

**Status:** ACTIVE
**Version:** 0.1
**Document type:** System architecture map
**Authority:** Architectural
**Scope:** Offline text analysis, controlled text transformation, integrity
validation, research evaluation and capability lifecycle

---

## 1. Purpose

This document defines the architectural structure of the project.

The architecture must provide a stable foundation for:

- multilingual text analysis;
- scientific research;
- watermark analysis;
- AI-generated-text assessment;
- provenance analysis;
- controlled text transformation;
- semantic and factual integrity validation;
- minimality measurement;
- reproducible experimentation;
- offline execution;
- optional external research integrations;
- capability versioning;
- capability activation and retirement;
- continuous maintenance.

The architecture must remain useful even when individual research
hypotheses, detectors, models or algorithms become obsolete.

---

# 2. Architectural Principle

The system must separate:

1. text preservation;
2. analysis;
3. transformation;
4. validation;
5. evaluation;
6. external integrations;
7. configuration;
8. capability lifecycle;
9. reporting.

No single algorithm should define the architecture.

Algorithms are replaceable components.

---

# 3. High-Level Architecture

The conceptual pipeline is:

INPUT
→ PRESERVATION SNAPSHOT
→ NORMALIZATION / REPRESENTATION
→ ANALYSIS
→ OPTIONAL CONTROLLED TRANSFORMATION
→ INTEGRITY VALIDATION
→ EVALUATION
→ OUTPUT + REPORT

The pipeline must preserve the original input independently of all
intermediate representations.

---

# 4. Architectural Layers

The system should be divided into the following conceptual layers:

1. Interface Layer
2. Orchestration Layer
3. Text Representation Layer
4. Analysis Layer
5. Transformation Layer
6. Validation Layer
7. Evaluation Layer
8. Capability Layer
9. Data / Model Layer
10. External Integration Layer
11. Persistence Layer
12. Reporting Layer
13. Configuration Layer

Each layer should have a clearly defined responsibility.

---

# 5. Interface Layer

Responsibilities:

- accept input text;
- accept configuration;
- select evaluation profiles;
- select supported language;
- request analysis;
- request controlled transformation;
- display results;
- export reports.

The interface must not contain scientific logic.

The interface may be:

- command line;
- local graphical interface;
- library/API;
- batch interface.

The architecture must permit multiple interfaces over the same core.

---

# 6. Orchestration Layer

The orchestration layer coordinates execution.

Responsibilities include:

- pipeline construction;
- capability selection;
- dependency resolution;
- configuration validation;
- execution ordering;
- failure handling;
- cancellation;
- resource limits;
- result aggregation.

The orchestrator must not contain detector-specific or
language-specific algorithms.

---

# 7. Text Representation Layer

The system must maintain multiple representations where necessary.

At minimum:

1. canonical original text;
2. analysis representation;
3. transformation representation;
4. final output.

The canonical original must remain immutable.

---

# 8. Preservation Snapshot

Immediately after input, the system should create a preservation snapshot.

The snapshot may contain:

- original text;
- encoding;
- Unicode normalization state;
- hashes;
- structural representation;
- paragraph boundaries;
- sentence boundaries;
- tokenization;
- detected language;
- metadata required for validation.

The snapshot provides the baseline against which subsequent changes are
measured.

---

# 9. Analysis Layer

The analysis layer contains independent analytical capabilities.

Potential capability families include:

- language identification;
- segmentation;
- token analysis;
- linguistic analysis;
- stylometric analysis;
- watermark signal analysis;
- provenance analysis;
- AI-generation assessment;
- statistical analysis;
- structural analysis;
- semantic analysis.

Analysis components must be independently versioned.

---

# 10. Watermark Analysis

Watermark-related components are analytical components.

They may investigate:

- statistical signals;
- token-level signals;
- semantic signals;
- syntactic signals;
- contextual signals;
- known watermark families;
- experimental watermark hypotheses.

Each analyzer must document:

- required input;
- assumptions;
- supported languages;
- algorithm/version;
- confidence;
- limitations;
- reproducibility;
- scientific source.

The architecture must not assume that one watermark detector represents all
possible watermark mechanisms.

---

# 11. AI-Generated-Text Assessment

AI-generation assessment must be represented as an analytical capability.

Potential implementations include:

- local classifiers;
- statistical measurements;
- linguistic measurements;
- stylometric measurements;
- externally supplied detector results.

Each result must retain:

- analyzer identity;
- version;
- configuration;
- language;
- text length;
- score;
- confidence;
- threshold;
- timestamp where relevant.

Results must not be silently converted into universal truth.

---

# 12. Provenance Analysis

Provenance analysis may inspect:

- embedded metadata;
- cryptographic signatures;
- content credentials;
- provenance records;
- document history where available.

Provenance analysis is distinct from watermark analysis.

A missing provenance signal does not prove that content has no provenance.

---

# 13. Transformation Layer

The transformation layer is responsible for controlled modifications of text.

Its architectural purpose is to support legitimate operations such as:

- grammar correction;
- spelling correction;
- formatting normalization;
- terminology normalization;
- clarity improvement;
- consistency correction;
- style normalization;
- accessibility-oriented rewriting;
- user-requested paraphrasing;
- translation;
- controlled summarization.

Every transformation must declare:

- purpose;
- scope;
- expected effects;
- language support;
- dependencies;
- validation requirements.

The transformation layer must not directly determine whether an external
detector will classify the resulting text as human-generated.

---

# 14. Transformation Constraints

Transformations must operate under explicit constraints.

Possible constraints include:

- preserve factual content;
- preserve entities;
- preserve numerical values;
- preserve citations;
- preserve URLs;
- preserve document structure;
- preserve requested terminology;
- minimize unnecessary changes;
- respect user-defined style;
- respect language-specific rules.

Constraints must be machine-testable whenever practical.

**Cross-reference:** the requirement-ID-level definitions underlying these
constraints are the FID-xxx preservation family in
`S04-fidelity-requirements.md` and TRN-007 (Minimal Intervention) in
`S05-transformation-requirements.md`. Added 2026-08-29 per the Q001
cross-area audit (`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND
PASS, §4S).

---

# 15. Transformation Candidate Model

A transformation should be treated as a candidate until validated.

Conceptually:

ORIGINAL
→ CANDIDATE
→ ANALYSIS
→ VALIDATION
→ ACCEPTED / REJECTED

The original must never be overwritten during candidate generation.

Multiple candidates may be evaluated independently.

---

# 16. Validation Layer

The validation layer determines whether a candidate transformation satisfies
its declared constraints.

Validation families may include:

- semantic validation;
- factual validation;
- structural validation;
- numerical validation;
- entity validation;
- linguistic validation;
- minimality validation;
- regression validation.

Validation must be independent from the component that generated the
candidate whenever practical.

---

# 17. Semantic Validation

Semantic validation may combine:

- deterministic comparisons;
- linguistic analysis;
- entailment analysis;
- contradiction detection;
- semantic similarity;
- structured information comparison.

No single semantic metric should automatically define correctness.

**Cross-reference:** the requirement-ID-level definition of this dimension
is `S04-fidelity-requirements.md` § 4, FID-001 — Semantic Preservation.
Added 2026-08-29 per the Q001 cross-area audit
(`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §4S).

---

# 18. Factual Validation

Factual validation should prioritize deterministic checks where possible.

Examples include:

- numbers;
- dates;
- names;
- organizations;
- places;
- units;
- percentages;
- references;
- URLs;
- identifiers.

Unexpected factual changes should normally cause candidate rejection or
explicit review.

**Cross-reference:** the requirement-ID-level definition of this dimension
is `S04-fidelity-requirements.md` § 6, FID-003 — Factual Preservation.
Added 2026-08-29 per the Q001 cross-area audit
(`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §4S).

---

# 19. Structural Validation

Structural validation compares:

- paragraphs;
- headings;
- lists;
- tables;
- quotations;
- references;
- markup;
- code;
- formulas;
- document ordering.

The exact validation method depends on the input format.

**Cross-reference:** the requirement-ID-level definition of this dimension
is `S04-fidelity-requirements.md` § 19, FID-016 — Structural Preservation.
Added 2026-08-29 per the Q001 cross-area audit
(`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §4S).

---

# 20. Minimality Measurement

The system must measure how much a candidate differs from its source.

Potential measurements include:

- character-level distance;
- token-level distance;
- lexical substitution;
- sentence modification;
- structural modification;
- semantic deviation.

Minimality is an evaluation dimension, not merely an implementation detail.

**Cross-reference:** the requirement-ID-level definition of this dimension
is `S04-fidelity-requirements.md` § 24, FID-021 — Minimality, and
`S05-transformation-requirements.md` § 11, TRN-007 — Minimal Intervention.
Added 2026-08-29 per the Q001 cross-area audit
(`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §4S).

---

# 21. Evaluation Layer

The evaluation layer combines measurements into reproducible experiment
results.

It must support:

- benchmark execution;
- detector comparison;
- transformation comparison;
- language comparison;
- regression analysis;
- robustness experiments;
- statistical analysis;
- report generation.

Evaluation must preserve raw measurements.

Derived scores must never replace the underlying observations.

---

# 22. Experimental Matrix

The architecture should support experiments across multiple dimensions:

- language;
- input corpus;
- text length;
- domain;
- analyzer;
- detector;
- model;
- transformation;
- configuration;
- version.

An experiment should be reproducible from its recorded configuration.

---

# 23. Capability Registry

Every significant analytical or transformation component should have a
capability identifier.

A capability record should contain:

- unique ID;
- name;
- category;
- version;
- status;
- languages;
- dependencies;
- input requirements;
- output schema;
- validation requirements;
- scientific sources;
- known limitations;
- resource requirements.

The registry is the architectural mechanism that permits modular evolution.

---

# 24. Capability Lifecycle

Capabilities follow:

DISCOVERED
→ EXPERIMENTAL
→ VALIDATED
→ ACTIVE
→ DEPRECATED
→ RETIRED

A capability may also enter:

DEGRADED

when its scientific or operational quality declines but immediate retirement
is not justified.

---

# 25. Capability Activation

A capability must not become active merely because it is implemented.

Activation should require:

- defined specification;
- validation;
- dependency verification;
- regression tests;
- documentation;
- compatibility checks;
- licensing checks where applicable.

---

# 26. Capability Retirement

Retirement must be supported as a first-class operation.

A capability may be retired because of:

- scientific obsolescence;
- superior replacement;
- unavailable dependency;
- licensing change;
- security issue;
- insufficient validation;
- excessive resource requirements;
- loss of maintenance viability.

Retirement must preserve historical records.

---

# 27. Dependency Isolation

Optional capabilities should not unnecessarily contaminate the core.

Examples include:

- external detector integrations;
- optional language models;
- large research datasets;
- experimental analyzers;
- GPU-specific components.

The core must remain operational when optional capabilities are unavailable.

---

# 28. Offline Core

The core runtime must not require external AI services.

The offline core must provide the fundamental processing and validation
pipeline.

External research integrations are optional architectural extensions.

---

# 29. External Integration Layer

External integrations may provide:

- detector measurements;
- research data;
- benchmark data;
- model downloads;
- optional validation services.

Every external integration must be isolated behind an adapter.

The rest of the system must depend on the adapter interface rather than on
the provider implementation.

---

# 30. External Data Boundary

Before any text is sent externally, the system must make the operation
explicit.

The architecture must support:

- opt-in external processing;
- provider identification;
- configuration visibility;
- data-transfer logging;
- failure handling;
- local fallback where available.

External processing must never happen implicitly.

---

# 31. Cloud Detector Integration

A cloud detector may be used as a research measurement instrument.

Its result must remain an external observation.

The architecture must not make a cloud detector a hidden part of the local
transformation pipeline.

A cloud service becoming unavailable must not alter the deterministic local
processing path.

---

# 32. Data and Model Layer

The data/model layer manages:

- datasets;
- corpora;
- benchmark sets;
- model files;
- tokenizer resources;
- language resources;
- detector configurations;
- experiment artifacts.

Every significant artifact should have:

- version;
- provenance;
- license;
- checksum/hash where appropriate;
- size;
- intended use.

---

# 33. Resource Management

The project has an approximate 30 GB storage budget.

The architecture must distinguish:

- mandatory assets;
- optional assets;
- temporary assets;
- cached assets;
- benchmark assets;
- archival assets.

Large resources should be loadable or removable independently where
practical.

---

# 34. Language Architecture

Language support should be modular.

The core must not assume that all languages share identical:

- tokenization;
- segmentation;
- morphology;
- syntax;
- punctuation;
- normalization;
- detector behavior.

Language-specific resources should therefore be isolated behind stable
interfaces.

---

# 35. Language Capability Registry

Each language capability should identify:

- language code;
- display name;
- supported operations;
- tokenizer;
- linguistic resources;
- analyzers;
- validators;
- known limitations;
- validation status.

A language can be active for one capability and research-only for another.

---

# 36. Configuration Layer

Configuration must be explicit and versioned.

Configuration may define:

- language;
- pipeline;
- enabled capabilities;
- transformation constraints;
- validation profile;
- external services;
- resource limits;
- output format;
- logging level.

Scientific behavior must not depend on undocumented environment variables
or hidden defaults.

---

# 37. Evaluation Profiles

The architecture must support versioned evaluation profiles.

A profile may specify:

- analyzers;
- detectors;
- transformations;
- languages;
- datasets;
- metrics;
- thresholds;
- external integrations;
- required validation.

Profiles must be reproducible.

---

# 38. Reporting Layer

Every significant execution should be able to produce a structured report.

The report may contain:

- input identifier/hash;
- language;
- enabled capabilities;
- versions;
- transformations;
- changes;
- validation results;
- detector observations;
- watermark-analysis observations;
- uncertainty;
- warnings;
- errors;
- final status.

The report should be machine-readable.

Human-readable summaries may be generated from the same underlying data.

---

# 39. Observability

The architecture must support diagnostics without requiring external
telemetry.

Relevant information includes:

- execution stage;
- capability;
- duration;
- resource use;
- validation result;
- failure reason;
- dependency status.

Sensitive text should not be unnecessarily written to logs.

---

# 40. Reproducibility

An experiment should be reproducible from:

- software version;
- configuration;
- dataset version;
- model version;
- capability versions;
- language;
- evaluation profile;
- external-service metadata where applicable.

Randomized components must support recorded seeds or equivalent
reproducibility controls where technically possible.

---

# 41. Deterministic Core

Where deterministic processing is practical, the architecture should prefer
it for:

- structural comparison;
- numerical comparison;
- entity preservation;
- hashing;
- serialization;
- configuration;
- validation rules.

Probabilistic components should expose their uncertainty.

---

# 42. AI Independence of Runtime

The project may be developed and maintained with AI-assisted development
tools.

The production runtime must not depend on an AI coding assistant.

Runtime behavior must be fully defined by the software, its declared
dependencies and its configured resources.

---

# 43. Development/Runtime Separation

Development tools and runtime components must be clearly separated.

Development-only dependencies must not silently become production
dependencies.

Research-only tools must not silently become runtime requirements.

---

# 44. Testing Architecture

Testing should be layered:

- unit tests;
- component tests;
- integration tests;
- pipeline tests;
- multilingual tests;
- regression tests;
- benchmark tests;
- reproducibility tests;
- resource tests.

Scientific validation belongs alongside, but must remain conceptually
distinct from, ordinary software testing.

---

# 45. Failure Isolation

A failure in one optional capability should not corrupt unrelated results.

The architecture should support:

- capability-level failure;
- graceful degradation;
- explicit unavailable status;
- partial-result reporting;
- rollback of failed transformations.

Silent fallback is prohibited when it could change scientific interpretation.

---

# 46. Update Architecture

Updates may affect:

- software;
- datasets;
- models;
- tokenizers;
- detectors;
- evaluation profiles;
- language resources;
- capability definitions.

Each update must be independently versionable where practical.

---

# 47. Compatibility

Capability updates should specify compatibility with:

- input formats;
- output formats;
- configuration schemas;
- datasets;
- other capabilities.

Breaking changes must be explicit.

---

# 48. Deprecation

A component should be deprecated before removal when practical.

Deprecation should record:

- reason;
- replacement if available;
- affected capabilities;
- affected experiments;
- migration requirements;
- intended removal release.

---

# 49. Security Boundaries

Security-sensitive functions must be isolated.

The architecture must distinguish:

- local trusted processing;
- user-provided input;
- external data;
- external services;
- downloaded artifacts;
- experimental components.

Downloaded models and datasets must not automatically gain arbitrary
execution privileges.

---

# 50. Supply-Chain Integrity

Dependencies and external artifacts should be tracked.

Where practical, record:

- source;
- version;
- checksum;
- license;
- acquisition date;
- dependency relationship.

Unverified binaries should not be silently promoted into the trusted core.

---

# 51. Storage Architecture

The architecture should distinguish:

- source datasets;
- derived datasets;
- benchmark datasets;
- models;
- caches;
- experiment outputs;
- reports;
- archives.

Temporary artifacts should have explicit cleanup policies.

---

# 52. Research Sandbox

Experimental components should be executable in a controlled research
environment before activation in the main pipeline.

The research sandbox provides:

- isolated dependencies;
- experimental configurations;
- benchmark execution;
- reproducible experiment records;
- controlled promotion to validated capability.

---

# 53. Promotion Path

The architectural promotion path is:

Research Component
→ Experimental Capability
→ Validation
→ Capability Registry
→ Active Capability

Promotion requires explicit evidence.

Implementation alone is insufficient.

---

# 54. Removal Path

The retirement path is:

Active Capability
→ Deprecation
→ Validation of Replacement / Impact
→ Retirement
→ Optional Removal

Historical experiment results must remain interpretable after removal.

---

# 55. Interface Stability

Core interfaces should remain stable even when implementations change.

The architecture should favor interfaces around:

- text;
- analysis results;
- transformation candidates;
- validation results;
- experiment results;
- capability metadata.

---

# 56. Schema-First Principle

Structured results should use explicit schemas.

Schemas should exist for:

- analysis results;
- detector results;
- watermark-analysis results;
- transformation candidates;
- validation results;
- experiment metadata;
- capability metadata;
- reports.

Schema changes must be versioned.

---

# 57. No Hidden Scientific State

Scientific behavior must not depend on:

- undocumented heuristics;
- hidden detector calls;
- undocumented thresholds;
- mutable global state;
- undeclared external services;
- unversioned model files.

All scientifically relevant state must be discoverable from configuration,
metadata or versioned resources.

---

# 58. Architecture Documentation

Detailed architectural documents should be created only when the associated
component has sufficient complexity to justify its own maintenance boundary.

**Status update (2026-09-12):** per §64's Tranche 1 and Tranche 2, three
of the documents below now exist: `docs/04-architecture/
CAPABILITY-ARCHITECTURE.md` (formalizes §23-26),
`docs/04-architecture/DATA-MODEL.md` (formalizes §32-33), and
`docs/04-architecture/VALIDATION-ARCHITECTURE.md` (formalizes §16-20,
unblocked by `DECISION-LOG.md` DEC-015).

**Status update (2026-09-13):** per §64.4.2's second reassessment and
`DECISION-LOG.md` DEC-020, two more now exist: `docs/04-architecture/
ANALYSIS-ARCHITECTURE.md` (formalizes §9-12) and `docs/04-architecture/
LANGUAGE-ARCHITECTURE.md` (formalizes §34-35), both unblocked by
`SPECIFICATION-MAP.md` §22.1's per-language capability-state assignment
(DEC-018). `TRANSFORMATION-ARCHITECTURE.md` remains not created — §64.4.2
found its blocker is a different, deeper dependency (actually-`VALIDATED`
capabilities, not documented per-language defaults) that this round did
not resolve.

**Status update (2026-09-13, later):** per §64.6 (Tranche 4) and
`DECISION-LOG.md` DEC-021, `docs/04-architecture/CORE-ARCHITECTURE.md`
now also exists (formalizes §3-8), evaluated as evidence-independent and
therefore ready without waiting on any per-language record.
`EXTERNAL-INTEGRATION-ARCHITECTURE.md` and `CONFIGURATION-ARCHITECTURE.md`/
`REPORTING-ARCHITECTURE.md` are assessed but not drafted in this pass;
`PIPELINE-ARCHITECTURE.md` and `PLUGIN-ARCHITECTURE.md` remain unresolved
scoping questions (§64.6). The remaining candidates below are otherwise
unchanged — still potential future documents, not yet created; §64 gives
the proposed order.

**Status update (2026-09-13, later still):** per `DECISION-LOG.md`
DEC-022, `docs/04-architecture/EXTERNAL-INTEGRATION-ARCHITECTURE.md` now
also exists (formalizes §29-31), executing the candidate DEC-021
identified as "likely ready but not drafted." `CONFIGURATION-ARCHITECTURE.md`
and `REPORTING-ARCHITECTURE.md` remain the next candidates, still pending
the deeper evaluation DEC-021 deferred for both; `PIPELINE-ARCHITECTURE.md`
and `PLUGIN-ARCHITECTURE.md` remain unresolved scoping questions.

Potential future documents include:

- `CORE-ARCHITECTURE.md` — **created**, see above
- `PIPELINE-ARCHITECTURE.md`
- `CAPABILITY-ARCHITECTURE.md` — **created**, see above
- `LANGUAGE-ARCHITECTURE.md` — **created**, see above
- `ANALYSIS-ARCHITECTURE.md` — **created**, see above
- `TRANSFORMATION-ARCHITECTURE.md`
- `VALIDATION-ARCHITECTURE.md` — **created**, see above
- `EXTERNAL-INTEGRATION-ARCHITECTURE.md` — **created**, see above
- `DATA-MODEL.md` — **created**, see above
- `CONFIGURATION-ARCHITECTURE.md`
- `REPORTING-ARCHITECTURE.md`
- `PLUGIN-ARCHITECTURE.md`

These are candidates rather than immediate mandatory files.

---

# 59. Architecture Change Process

An architectural change must identify:

1. affected requirements;
2. affected capabilities;
3. affected interfaces;
4. affected dependencies;
5. affected tests;
6. affected data;
7. compatibility implications;
8. migration requirements;
9. rollback strategy;
10. documentation updates.

The change must be propagated through the documentation change queue.

---

# 60. Architectural Quality Gates

Before an architectural component becomes part of the validated system, it
should satisfy:

- defined responsibility;
- stable interface;
- documented dependencies;
- test coverage;
- resource characterization;
- failure behavior;
- security review where relevant;
- reproducibility requirements;
- documentation;
- lifecycle state.

---

# 61. Relationship With Other Project Areas

## Research

Defines scientific phenomena and candidate capabilities.

## Scientific Specification

Defines measurable requirements.

## Validation

Determines whether architecture and capabilities satisfy requirements.

## Security

Defines trust boundaries and security controls.

## Data

Defines datasets and model resources.

## Development

Defines implementation and change procedures.

## Operations

Defines installation, execution and update procedures.

## Certification

Determines whether the complete architecture and release satisfy the
declared certification profile.

---

# 62. Current Architectural State

The project is currently in the architectural-definition phase.

The architecture deliberately does not select final algorithms before the
research and validation phases establish their suitability.

The architecture therefore prioritizes:

- modularity;
- replaceability;
- reproducibility;
- offline execution;
- scientific traceability;
- multilingual extensibility;
- capability lifecycle management.

**Update (2026-09-12):** per §64 Tranche 1 and `DECISION-LOG.md` DEC-014,
this area is no longer a single MAP document — `CAPABILITY-ARCHITECTURE.md`
and `DATA-MODEL.md` now exist. This does not mean the definition phase has
ended: both new documents formalize generic mechanisms only and
deliberately still select no specific detector, watermark scheme, model
or algorithm, consistent with the principle stated above. Areas outside
04-architecture that describe "04-architecture through 10-certification"
as uniformly single-MAP-document (e.g. `docs/00-project/START-HERE.md`)
should be read with this update in mind.

**Update (2026-09-13):** per §64.4.2 (Tranche 3a) and `DECISION-LOG.md`
DEC-020, `ANALYSIS-ARCHITECTURE.md` and `LANGUAGE-ARCHITECTURE.md` now
also exist, both formalizing generic mechanisms only, per the same
principle. `TRANSFORMATION-ARCHITECTURE.md` (the remaining Tranche 3
candidate) is not yet drafted: §64.4.2 found it depends on capabilities
actually reaching `VALIDATED` status
(`CAPABILITY-ARCHITECTURE.md` §6-7), not merely on a documented
per-language default — a dependency this update does not resolve.

**Update (2026-09-13, later):** per §64.6 (Tranche 4) and
`DECISION-LOG.md` DEC-021, `CORE-ARCHITECTURE.md` now also exists,
formalizing §3-8's execution backbone. This document's readiness did not
depend on research evidence at all, unlike every prior tranche document —
it was deferred only for pacing, per §64.4's original "revisit after
Tranches 1-2" note. The definition phase, in substance, therefore
continues even as the document count grows: no specific detector,
watermark scheme, model, tokenizer, interface technology or algorithm has
been selected by any of the six sub-documents now in 04-architecture.

**Update (2026-09-13, later still):** per `DECISION-LOG.md` DEC-022,
`EXTERNAL-INTEGRATION-ARCHITECTURE.md` now also exists, formalizing
§29-31's adapter and external-data-boundary mechanics — the seventh
sub-document in 04-architecture, and, like `CORE-ARCHITECTURE.md`,
evidence-independent rather than blocked on per-language or per-model
research. It selects no specific external provider, protocol, data
format, or security-control mechanism, so the definition phase remains
unaffected in substance by this addition as well.

---

# 63. Governing Principle

The architecture must survive changes in scientific knowledge.

A detector can disappear.

A watermark can become obsolete.

A language module can be replaced.

A model can be deprecated.

A benchmark can be invalidated.

A new analytical method can emerge.

None of these events should require redesigning the entire system.

The architecture is therefore considered successful when scientific and
technical evolution can occur through bounded, versioned and testable
capability changes rather than uncontrolled changes to the core.

---

# 64. Proposed Path to Exit Definition Phase (2026-09-12) — Awaiting Owner Decision

This section proposes a prioritized, tranche-based plan for drafting the
candidate documents listed in §58, using what is now known from
`03-scientific-specification` (S02/S04/S05) and the research layer
(R01-R09, in particular R09's local-deployment findings and KB-008/
KB-010/KB-013/KB-014's capability-evidence gaps). It is a proposal, not a
decision: per `docs/00-project/DECISION-LOG.md` DEC-004 ("human approval
is required at macro-tranche boundaries") and this project's consistent
practice of not silently resolving structural questions (DEC-012, DEC-013
precedent), no drafting begins under this plan without owner confirmation
of the tranche order below — or a different order the owner prefers.

## 64.1 Readiness Signal Used

A candidate document from §58 is judged "ready to draft" when the
requirements and research it would formalize are already established
(not merely anticipated) elsewhere in the corpus, and judged "premature"
when drafting it now would require inventing capability-specific choices
(which detector, which language coverage, which model) that the evidence
does not yet support — which §25 (Capability Activation) and DEC-005
(requirements must not be weakened to obtain a result) both argue against
doing prematurely.

## 64.2 Tranche 1 — Structurally Ready Now

- **`CAPABILITY-ARCHITECTURE.md`**: formalizes §23-26 (Capability
  Registry, Lifecycle, Activation, Retirement), which are generic
  mechanisms independent of which specific detector, watermark scheme or
  model is eventually registered. Nothing in R01-R09 or S02/S04/S05
  changes this mechanism's shape.
- **`DATA-MODEL.md`**: formalizes §32-33 (Data/Model Layer, Resource
  Management), directly informed by R08 §7-9 (dataset provenance/
  licensing/storage methodology) and R09's concrete verified-size findings
  for specific candidate models (R-0102-R-0121). This is the architecture
  document R09's evidence most directly and completely supports drafting
  today.

## 64.3 Tranche 2 — Executed (2026-09-12)

- **`VALIDATION-ARCHITECTURE.md`**: formalizes §16-20 (Validation Layer,
  Semantic/Factual/Structural Validation, Minimality), cross-referencing
  concrete `FID-xxx`/`TRN-xxx` requirements already in S04/S05. The
  scoping decision this tranche was waiting on is resolved by
  `DECISION-LOG.md` DEC-015: factual validation splits into a
  deterministic category (`VALIDATE-FACTUAL-STRUCTURED`, not blocked by
  KB-013) and a claim/proposition-level category
  (`VALIDATE-FACTUAL-CLAIM`, where KB-013's gap actually applies and
  where non-English capabilities may register only `EXPERIMENTAL`
  candidates). Q-001 (semantic-equivalence metric) remains genuinely
  open — the document defines where such a metric plugs in, not what it
  is.

## 64.4 Tranche 3 — Premature Without Further Upstream Resolution

- **`ANALYSIS-ARCHITECTURE.md`** (covers §9-12, including Watermark
  Analysis and AI-Generated-Text Assessment): KB-008/KB-010/KB-014 all
  show detector/watermark capability-state evidence is language- and
  capability-dependent in ways not yet resolved by DCQ-006/007/008 (all
  still `PENDING`). Drafting this now risks assuming a capability state
  (e.g. which languages get a validated AI-detection capability) ahead of
  the evidence.
- **`LANGUAGE-ARCHITECTURE.md`** (§34-35): depends on the same
  per-language capability-state resolution as above.
- **`TRANSFORMATION-ARCHITECTURE.md`** (§13-15): the mechanism (§13-15)
  is stable, but meaningful content depends on which transformation
  families are prioritized, which in turn depends on which validation
  families (now defined in `VALIDATION-ARCHITECTURE.md`, Tranche 2) have
  `VALIDATED` capabilities to check against — still premature until
  Tranche 3's own blockers (DCQ-006/007/008) resolve.
- **`EXTERNAL-INTEGRATION-ARCHITECTURE.md`, `CONFIGURATION-ARCHITECTURE.md`,
  `REPORTING-ARCHITECTURE.md`, `PLUGIN-ARCHITECTURE.md`, `CORE-ARCHITECTURE.md`,
  `PIPELINE-ARCHITECTURE.md`**: not evaluated in depth in this pass: none
  of R01-R09's findings bear on them directly, and doing so would extend
  this proposal beyond what the current research/specification base can
  actually support. Recommended to revisit after Tranches 1-2.

### 64.4.1 Reassessment (2026-09-12, per DECISION-LOG.md DEC-017)

The owner asked that this Tranche 3 blocker be revisited after DCQ-006/
007/008's `03-scientific-specification` portions were executed
(`DECISION-LOG.md` DEC-016; `SPECIFICATION-MAP.md` §17, §20-23, §25-26;
`S02-scientific-requirements.md`; `S04-fidelity-requirements.md` FID-002).
That execution added evidence-cited cross-reference notes — it
deliberately did not assign any actual per-language, per-capability state
(each added note says so explicitly, e.g. `SPECIFICATION-MAP.md` §22's
note: "this note records the evidence; it does not assign any state").

The readiness signal in §64.1 requires that "the requirements and
research it would formalize are already established... elsewhere in the
corpus" before a candidate document is drafted. For
`ANALYSIS-ARCHITECTURE.md` and `LANGUAGE-ARCHITECTURE.md`, what would need
to be established is not the underlying research evidence (already
registered as R-0022, R-0046-R-0073, R-0086, R-0109-R-0121) but the actual
per-language/per-capability state assignments (`SPECIFICATION-MAP.md` §22)
that `03-scientific-specification` itself has not yet performed — only
generic illustrative examples exist there. `TRANSFORMATION-ARCHITECTURE.md`
has the same dependency, one level removed (it needs to know which
validation families have `VALIDATED` capabilities, which in turn needs
those same state assignments). This propagation pass therefore does not
change the readiness conclusion: **Tranche 3 remains premature**, for the
same underlying reason as before, now stated more precisely.

The concrete, currently-unblocked next step toward eventually satisfying
this readiness signal is not drafting a Tranche 3 document, but populating
real per-language, per-capability state values in
`SPECIFICATION-MAP.md` §22 (and the corresponding `S02-scientific-
requirements.md` REQ-LANG-006 evidence record), grounded in the evidence
this pass just cited. That is itself a substantive `03-scientific-
specification` content decision — which capabilities to state for which
of the 13 languages, and what evidence threshold justifies each state —
and is proposed here as a candidate follow-up, not begun unilaterally.

### 64.4.2 Second Reassessment (2026-09-13, per DECISION-LOG.md DEC-019)

The owner approved §64.4.1's candidate follow-up; `SPECIFICATION-MAP.md`
§22.1 now assigns real per-language states for AI-generated-text
detection, watermarking, and factual/claim-consistency validation
(`DECISION-LOG.md` DEC-018). This section re-runs the §64.1 readiness
test against that new state, per document:

- **`ANALYSIS-ARCHITECTURE.md`**: §64.4's blocker was specifically the
  absence of per-language/per-capability state assignments for
  detection and watermarking. `SPECIFICATION-MAP.md` §22.1.1/§22.1.2 now
  supply exactly that (13 languages, `RESEARCH_ONLY`/`NOT_SUPPORTED`,
  each cell cited to a specific `R-XXXX`). A document formalizing the
  generic watermark-analysis/AI-detection-assessment mechanism — how a
  capability record queries and respects these per-language states,
  mirroring `VALIDATION-ARCHITECTURE.md`'s treatment of the factual-
  validation split — no longer requires inventing anything §22.1 does
  not already supply. **Reassessed as structurally ready.**
- **`LANGUAGE-ARCHITECTURE.md`**: depended on the identical resolution.
  **Reassessed as structurally ready**, on the same basis.
- **`TRANSFORMATION-ARCHITECTURE.md`**: §64.4's blocker was different in
  kind, not merely in degree — it needs to know which validation
  families have *`VALIDATED`* capabilities to check transformations
  against, not merely which have a documented default state. Every cell
  in `SPECIFICATION-MAP.md` §22.1 is `RESEARCH_ONLY` or `NOT_SUPPORTED`
  by design (§22.1's own Method note: no capability in this project has
  yet been implemented or passed `CAPABILITY-ARCHITECTURE.md`'s
  Activation Gate). No documentation update can manufacture a `VALIDATED`
  capability — that requires actual implementation and evaluation work
  that has not started. **Remains premature**, for a reason DEC-018 could
  not and did not resolve.

Consistent with `DECISION-LOG.md` DEC-004 (human approval required at
macro-tranche boundaries) and this proposal's own practice for Tranches
1-2, drafting `ANALYSIS-ARCHITECTURE.md` and `LANGUAGE-ARCHITECTURE.md`
does not begin under this reassessment alone — it requires the owner's
explicit confirmation, given separately from the reassessment itself.

### 64.4.3 Tranche 3a Executed (2026-09-13, per DECISION-LOG.md DEC-020)

The owner gave the confirmation §64.4.2 required. `ANALYSIS-ARCHITECTURE.md`
(formalizing §9-12) and `LANGUAGE-ARCHITECTURE.md` (formalizing §34-35)
are now drafted, both selecting no specific detector, watermark scheme,
tokenizer or model, consistent with §64.1's readiness signal and every
prior tranche document's practice. `TRANSFORMATION-ARCHITECTURE.md`
remains not drafted, per §64.4.2's finding that its blocker is
unresolved.

## 64.5 What This Proposal Does Not Decide

Consistent with DEC-009 (a research finding does not automatically become
a system requirement): neither this proposal nor the documents it
produced (`CAPABILITY-ARCHITECTURE.md`, `DATA-MODEL.md`,
`VALIDATION-ARCHITECTURE.md`, `ANALYSIS-ARCHITECTURE.md`,
`LANGUAGE-ARCHITECTURE.md`, `CORE-ARCHITECTURE.md`,
`EXTERNAL-INTEGRATION-ARCHITECTURE.md`) select an actual
semantic-similarity model, factual-consistency approach, detector,
watermark scheme, tokenizer, interface technology, external provider,
integration protocol, or security-control mechanism. Specific technical
choices remain a separate, later decision, to be made when each
document's mechanism is actually implemented and to be recorded in
`docs/00-project/DECISION-LOG.md` at that time.

## 64.6 Tranche 4 (2026-09-13, per DECISION-LOG.md DEC-021)

§64.4's six unevaluated candidates (`CORE-ARCHITECTURE.md`,
`PIPELINE-ARCHITECTURE.md`, `EXTERNAL-INTEGRATION-ARCHITECTURE.md`,
`CONFIGURATION-ARCHITECTURE.md`, `REPORTING-ARCHITECTURE.md`,
`PLUGIN-ARCHITECTURE.md`) were deliberately left unassessed, "recommended
to revisit after Tranches 1-2." With Tranches 1, 2 and 3a complete, this
section performs that revisit for the first of them.

Unlike §64.1's readiness signal (evidence sufficiency per language/
capability), these six candidates' readiness turns on a different
question: whether `ARCHITECTURE-MAP.md` already contains enough
conceptual definition, independent of any research evidence, to
formalize without inventing new software-architecture concepts. On that
test:

- **`CORE-ARCHITECTURE.md`** (§3-8): well-specified, evidence-independent,
  and foundational — every capability document drafted so far assumes an
  orchestration/preservation-snapshot layer exists. **Reassessed as
  structurally ready**, and drafted (see `docs/04-architecture/
  CORE-ARCHITECTURE.md`).
- **`EXTERNAL-INTEGRATION-ARCHITECTURE.md`** (§29-31): similarly
  well-specified and evidence-independent, directly grounded in DEC-001
  (offline core). Assessed as likely ready but not drafted in this pass —
  scoped as a candidate next step, not begun unilaterally. **Update
  (2026-09-13, per `DECISION-LOG.md` DEC-022):** drafted, following the
  owner's confirmation to proceed with this candidate. See
  `docs/04-architecture/EXTERNAL-INTEGRATION-ARCHITECTURE.md`.
- **`CONFIGURATION-ARCHITECTURE.md`** (§36) and
  **`REPORTING-ARCHITECTURE.md`** (§38): reasonably specified but lower
  priority; not evaluated to the same depth in this pass. **Update
  (2026-09-13, per `DECISION-LOG.md` DEC-023):** now evaluated to the same
  depth — see §64.7 below. `REPORTING-ARCHITECTURE.md` assessed
  structurally ready; `CONFIGURATION-ARCHITECTURE.md` found to have an
  unresolved scoping overlap with §37 (Evaluation Profiles), recorded
  rather than drafted around.
- **`PIPELINE-ARCHITECTURE.md`**: has no clearly distinct parent section —
  its likely content overlaps substantially with §6 (Orchestration
  Layer), which `CORE-ARCHITECTURE.md` §6 now formalizes.
  `CORE-ARCHITECTURE.md` §10 explicitly leaves open whether this should
  remain a separate document or whether §6's treatment already covers it,
  rather than silently deciding either way.
- **`PLUGIN-ARCHITECTURE.md`**: no parent section in `ARCHITECTURE-MAP.md`
  addresses a plugin mechanism at all. Drafting it now would mean
  inventing a concept the corpus has not yet defined, contrary to
  `NO-INVENTION-RULES.md`. **Remains unevaluated** — a scoping decision
  (what a "plugin" would mean in this architecture) would need to come
  first, as its own proposal.

## 64.7 Tranche 4, Continued: Evaluating REPORTING-ARCHITECTURE.md and CONFIGURATION-ARCHITECTURE.md (2026-09-13, per DECISION-LOG.md DEC-023)

Following DEC-021's deferral of these two candidates to "not evaluated to
the same depth," this section applies §64.6's readiness test (conceptual
definition already present, independent of research evidence) to each in
turn.

**`REPORTING-ARCHITECTURE.md` (§38) — assessed structurally ready.**
Unlike `CORE-ARCHITECTURE.md` and `EXTERNAL-INTEGRATION-ARCHITECTURE.md`,
which formalized a section range that no other document yet touched,
Reporting's obligations are already scattered, concretely, across every
sub-document drafted so far: `CORE-ARCHITECTURE.md` §9 (the four-state
failure/eligibility taxonomy a report must represent),
`ANALYSIS-ARCHITECTURE.md` §7 (Output Category Tagging — every analysis
result carries a tag a report must preserve, never collapse),
`VALIDATION-ARCHITECTURE.md` §9 (Missing-Evidence Reporting, which
already cites this section directly), and
`EXTERNAL-INTEGRATION-ARCHITECTURE.md` §5-7 (data-transfer logging and
the "external boundary unreachable" state). §38 itself already specifies
a full content list (input identifier/hash, language, enabled
capabilities, versions, transformations, changes, validation results,
detector and watermark-analysis observations, uncertainty, warnings,
errors, final status) and requires the report be machine-readable with
human-readable summaries derived from the same underlying data — directly
reinforced by §21 (Evaluation Layer: "derived scores must never replace
the underlying observations"), §51 (reports as a distinct storage
category), and §56 (Schema-First Principle: reports need an explicit,
versioned schema). A `REPORTING-ARCHITECTURE.md` document's task is
therefore real but bounded: unify these already-scattered obligations
into one coherent schema and document, without inventing any new
reporting concept the corpus does not already require.

**`CONFIGURATION-ARCHITECTURE.md` (§36) — found not yet ready, for a
reason distinct from any prior tranche document's blocker.** §36 is
directly grounded (Configuration is one of the Architectural Principle's
nine separated concerns, §2.7, and its own layer, §4.13) and reinforced
by §57 (No Hidden Scientific State: "all scientifically relevant state
must be discoverable from configuration"), §40-41 (Reproducibility and
Deterministic Core both list configuration), and §46-47 (configuration
schemas must be independently versionable, breaking changes explicit).
However, this evaluation surfaced a genuine, previously unrecorded
overlap: §36's content list (language, pipeline, enabled capabilities,
transformation constraints, validation profile, external services,
resource limits, output format, logging level) substantially overlaps
§37's Evaluation Profile content list (analyzers, detectors,
transformations, languages, datasets, metrics, thresholds, external
integrations, required validation) — `ARCHITECTURE-MAP.md` nowhere states
whether an Evaluation Profile is a specialization of Configuration, a
separate parallel concept, or the same thing under two names. Per
`docs/99-backlog/POST-INVENTORY-QUEUE.md`'s Governing Rule (a
contradiction or gap found during an audit is *recorded*, not silently
reconciled) and `NO-INVENTION-RULES.md`, this document does not resolve
that relationship by drafting around it — doing so would mean silently
inventing a scoping decision (in either direction) that the corpus has
not made. This is the same discipline `CORE-ARCHITECTURE.md` §10 already
applied to the `PIPELINE-ARCHITECTURE.md`/§6 overlap: recorded as an open
scoping question, not answered by omission.

`CONFIGURATION-ARCHITECTURE.md` therefore remains **not drafted**, pending
a scoping decision — to be proposed and recorded in `DECISION-LOG.md` in
its own right — on the Configuration/Evaluation-Profile relationship.