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

Potential future documents include:

- `CORE-ARCHITECTURE.md`
- `PIPELINE-ARCHITECTURE.md`
- `CAPABILITY-ARCHITECTURE.md`
- `LANGUAGE-ARCHITECTURE.md`
- `ANALYSIS-ARCHITECTURE.md`
- `TRANSFORMATION-ARCHITECTURE.md`
- `VALIDATION-ARCHITECTURE.md`
- `EXTERNAL-INTEGRATION-ARCHITECTURE.md`
- `DATA-MODEL.md`
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