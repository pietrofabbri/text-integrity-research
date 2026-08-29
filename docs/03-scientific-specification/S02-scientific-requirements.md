# S02 — Scientific Requirements

**Status:** NORMATIVE  
**Version:** 0.1  
**Document type:** Scientific requirements specification  
**Parent:** `docs/03-scientific-specification/SPECIFICATION-MAP.md`  
**Depends on:** `S01-system-objectives.md`

---

# 1. Purpose

This document converts the scientific objectives defined in S01 into
explicit, testable and traceable requirements.

A requirement in this document describes a property that the scientific
system must satisfy.

Requirements must be independently verifiable whenever practical.

---

# 2. Requirement Classification

Requirements are classified as:

- `SCI` — scientific methodology;
- `DATA` — data and provenance;
- `LANG` — multilingual behaviour;
- `MEAS` — measurement;
- `STAT` — statistical evaluation;
- `REPRO` — reproducibility;
- `LIFE` — lifecycle and evolution;
- `EXT` — extensibility;
- `SEC` — scientific-data security;
- `EXTSVC` — external measurement services.

Each requirement has a unique identifier.

---

# 3. Requirement Priority

Priority levels are:

### MUST

Mandatory for scientific validity.

### SHOULD

Strongly recommended unless a documented scientific reason exists not to
implement it.

### MAY

Optional capability that must not compromise mandatory requirements.

A MUST requirement cannot be downgraded merely because implementation is
difficult.

---

# 4. Core Scientific Requirements

## REQ-SCI-001 — Controlled Experiments

**Priority:** MUST

The system shall support controlled experiments in which relevant
independent variables can be explicitly specified.

Verification shall demonstrate that experimental configuration is recorded
and reproducible.

---

## REQ-SCI-002 — Experimental Isolation

**Priority:** MUST

An experiment shall distinguish source material, experimental condition,
transformation and measurement.

The system shall not silently modify an experimental variable outside the
declared configuration.

---

## REQ-SCI-003 — Explicit Experimental Configuration

**Priority:** MUST

Every experiment shall have a machine-readable or otherwise unambiguous
configuration describing all scientifically relevant parameters.

---

## REQ-SCI-004 — Immutable Experiment Identity

**Priority:** MUST

Each completed experiment shall receive a unique identifier.

Changing a scientifically relevant parameter shall result in a distinct
experiment configuration or version.

---

# 5. Watermark Requirements

## REQ-WM-001 — Watermark Method Identification

**Priority:** MUST

Every watermark experiment shall identify the watermark methodology being
evaluated.

---

## REQ-WM-002 — Watermark Versioning

**Priority:** MUST

Where multiple versions of a watermark implementation or methodology
exist, the version shall be recorded.

---

## REQ-WM-003 — Watermark Configuration

**Priority:** MUST

Scientifically relevant watermark-generation parameters shall be recorded
when available.

---

## REQ-WM-004 — Watermark/Detector Separation

**Priority:** MUST

The system shall represent watermark generation and watermark detection as
distinct experimental components.

A detector result shall not modify the recorded watermark condition.

---

## REQ-WM-005 — Multiple Watermark Families

**Priority:** SHOULD

The framework should support multiple watermark families without requiring
changes to the scientific core.

---

## REQ-WM-006 — Historical Watermark Preservation

**Priority:** MUST

Superseded watermark methodologies shall remain identifiable in historical
experimental records.

---

# 6. Detector Requirements

## REQ-DET-001 — Detector Identity

**Priority:** MUST

Every detector measurement shall identify the detector used.

---

## REQ-DET-002 — Detector Version

**Priority:** MUST

The system shall record detector version information when available.

If the provider does not expose a version, the system shall record that
fact.

---

## REQ-DET-003 — Detector Configuration

**Priority:** MUST

Relevant detector configuration and input conditions shall be recorded.

---

## REQ-DET-004 — Detector Output Preservation

**Priority:** MUST

Raw detector output shall be preserved separately from interpreted
metrics.

---

## REQ-DET-005 — Detector Independence

**Priority:** MUST

The scientific framework shall not treat one detector as universal ground
truth.

---

## REQ-DET-006 — Detector Comparison

**Priority:** SHOULD

The framework should support comparison between multiple detectors or
detector configurations.

---

## REQ-DET-007 — Detector Temporal Tracking

**Priority:** MUST

Detector observations shall be associated with a date and identifiable
version or service state where possible.

---

# 7. AI-Generated-Text Detection Requirements

## REQ-AID-001 — AI Detector Classification

**Priority:** MUST

AI-generated-text detectors shall be represented separately from
watermark detectors.

---

## REQ-AID-002 — Detector Scope

**Priority:** MUST

The system shall record the intended scope and supported languages of an
AI-generated-text detector when known.

---

## REQ-AID-003 — Detector Output Semantics

**Priority:** MUST

The system shall document what a detector output represents before using
that output in statistical analysis.

---

## REQ-AID-004 — Detector Uncertainty

**Priority:** MUST

Where detector uncertainty or calibration information is available, it
shall be preserved.

---

# 8. Multilingual Requirements

## REQ-LANG-001 — Language Metadata

**Priority:** MUST

Every text sample shall have explicit language metadata.

---

## REQ-LANG-002 — Language-Specific Evaluation

**Priority:** MUST

Results shall be analyzable separately by language.

---

## REQ-LANG-003 — No Silent Cross-Language Aggregation

**Priority:** MUST

The system shall not combine results from different languages into a
single aggregate metric without explicitly identifying the aggregation.

---

## REQ-LANG-004 — Initial Language Set

**Priority:** MUST

The initial scientific framework shall support experimentation involving:

- English;
- Spanish;
- German;
- Japanese;
- French;
- Portuguese;
- Russian;
- Italian;
- Dutch;
- Polish;
- Turkish;
- Chinese;
- Indonesian.

---

## REQ-LANG-005 — Language Extensibility

**Priority:** MUST

Adding a language shall not require redesigning unrelated scientific
components.

---

## REQ-LANG-006 — Language Qualification

**Priority:** SHOULD

A language should have an explicit evidence record describing known
linguistic, dataset and detector limitations.

---

# 9. Transformation Requirements

## REQ-TRANS-001 — Transformation Identity

**Priority:** MUST

Every transformation shall have an explicit identifier.

---

## REQ-TRANS-002 — Transformation Version

**Priority:** MUST

Scientifically relevant transformation changes shall produce a new
version.

---

## REQ-TRANS-003 — Transformation Configuration

**Priority:** MUST

Relevant transformation parameters shall be recorded.

---

## REQ-TRANS-004 — Source Preservation

**Priority:** MUST

The original experimental source shall remain separately identifiable.

---

## REQ-TRANS-005 — Transformation Chain

**Priority:** MUST

When multiple transformations are applied sequentially, their order and
configuration shall be recorded.

---

## REQ-TRANS-006 — Minimal-Change Measurement

**Priority:** SHOULD

The system should quantify the magnitude of textual change produced by a
transformation using multiple measurable dimensions.

---

# 10. Preservation Requirements

## REQ-PRES-001 — Semantic Preservation

**Priority:** MUST

Experiments involving transformation shall include a measurable assessment
of semantic preservation.

---

## REQ-PRES-002 — Factual Preservation

**Priority:** SHOULD

Where applicable, experiments should evaluate whether factual content has
changed.

---

## REQ-PRES-003 — Structural Preservation

**Priority:** MUST

Structural changes shall be measurable.

Relevant structures may include:

- paragraphs;
- sentences;
- headings;
- lists;
- quotations;
- formatting metadata.

---

## REQ-PRES-004 — Stylistic Preservation

**Priority:** SHOULD

Stylistic changes should be evaluated independently from semantic
similarity.

---

## REQ-PRES-005 — Linguistic Preservation

**Priority:** SHOULD

Relevant linguistic characteristics should be measured separately from
semantic similarity.

---

## REQ-PRES-006 — Multi-Metric Evaluation

**Priority:** MUST

No single similarity metric shall be treated as sufficient evidence of
overall preservation.

---

# 11. Statistical Requirements

## REQ-STAT-001 — Raw Observation Preservation

**Priority:** MUST

Raw experimental observations shall be retained separately from derived
statistics.

---

## REQ-STAT-002 — Statistical Method Identification

**Priority:** MUST

Every reported statistical result shall identify the statistical method
used.

---

## REQ-STAT-003 — Sample Size

**Priority:** MUST

The relevant sample size shall be recorded for reported aggregate results.

---

## REQ-STAT-004 — Uncertainty

**Priority:** MUST

Meaningful uncertainty shall be reported where applicable.

---

## REQ-STAT-005 — Multiple Comparisons

**Priority:** SHOULD

Where multiple statistical comparisons are performed, the methodology
shall account for multiple-comparison effects where scientifically
appropriate.

---

## REQ-STAT-006 — Exploratory/Confirmatory Separation

**Priority:** MUST

Exploratory findings shall be distinguishable from confirmatory findings.

---

## REQ-STAT-007 — Negative Results

**Priority:** MUST

Negative and inconclusive results shall be retained.

---

# 12. Dataset Requirements

## REQ-DATA-001 — Dataset Identity

**Priority:** MUST

Every dataset used in an experiment shall have an identifiable dataset
record.

---

## REQ-DATA-002 — Dataset Version

**Priority:** MUST

Dataset versions shall be recorded when available.

---

## REQ-DATA-003 — Dataset Provenance

**Priority:** MUST

The provenance of experimental datasets shall be documented.

---

## REQ-DATA-004 — Dataset Integrity

**Priority:** MUST

Changes to locally stored datasets or derived datasets shall be
detectable.

---

## REQ-DATA-005 — Dataset Limitations

**Priority:** MUST

Known limitations, biases and applicability constraints shall be recorded.

---

# 13. Reproducibility Requirements

## REQ-REPRO-001 — Configuration Reproducibility

**Priority:** MUST

A completed experiment shall preserve sufficient configuration information
to reproduce the experiment.

---

## REQ-REPRO-002 — Software Version

**Priority:** MUST

The software version used for an experiment shall be recorded.

---

## REQ-REPRO-003 — Dependency Version

**Priority:** MUST

Scientifically relevant dependency versions shall be recorded.

---

## REQ-REPRO-004 — Randomness

**Priority:** MUST

Random seeds or equivalent reproducibility controls shall be recorded
where applicable.

---

## REQ-REPRO-005 — External-Service Limitation

**Priority:** MUST

Experiments depending on mutable external services shall explicitly record
that exact historical reproduction may be impossible.

---

# 14. Provenance Requirements

## REQ-PROV-001 — End-to-End Provenance

**Priority:** MUST

A reported result shall be traceable to its source material, experimental
configuration and measurement process.

---

## REQ-PROV-002 — Immutable Raw Evidence

**Priority:** MUST

Raw evidence shall be preserved separately from derived or interpreted
results.

---

## REQ-PROV-003 — Evidence Chain

**Priority:** MUST

Derived results shall identify the raw observations from which they were
calculated.

---

# 15. External Service Requirements

## REQ-EXTSVC-001 — Explicit External Processing

**Priority:** MUST

Any external service receiving experimental text shall be explicitly
identified in the experiment configuration.

---

## REQ-EXTSVC-002 — External Service Metadata

**Priority:** MUST

The system shall record, where available:

- provider;
- service;
- endpoint or interface identifier;
- date/time;
- service version;
- relevant configuration.

---

## REQ-EXTSVC-003 — Failure Isolation

**Priority:** MUST

Failure or unavailability of an external measurement service shall not
corrupt local experimental state.

---

## REQ-EXTSVC-004 — Offline Core Independence

**Priority:** MUST

The core scientific pipeline shall remain executable without mandatory
access to external AI services.

---

# 16. Lifecycle Requirements

## REQ-LIFE-001 — Capability Identity

**Priority:** MUST

Each major scientific capability shall have an identifier.

---

## REQ-LIFE-002 — Capability Versioning

**Priority:** MUST

Major capability changes shall be versioned.

---

## REQ-LIFE-003 — Deprecation

**Priority:** MUST

Obsolete scientific capabilities shall support explicit deprecation.

---

## REQ-LIFE-004 — Historical Preservation

**Priority:** MUST

Deprecating or removing an active capability shall not delete historical
experimental evidence.

---

## REQ-LIFE-005 — Supersession

**Priority:** MUST

When a methodology supersedes another methodology, the relationship shall
be explicitly recorded.

---

# 17. Extensibility Requirements

## REQ-EXT-001 — Detector Extensibility

**Priority:** MUST

New detector integrations shall be addable without redesigning unrelated
scientific components.

---

## REQ-EXT-002 — Watermark Extensibility

**Priority:** MUST

New watermark methodologies shall be addable through defined interfaces
or equivalent isolation mechanisms.

---

## REQ-EXT-003 — Language Extensibility

**Priority:** MUST

New languages shall be addable without redesigning the scientific core.

---

## REQ-EXT-004 — Metric Extensibility

**Priority:** MUST

New evaluation metrics shall be addable without modifying historical
results.

---

## REQ-EXT-005 — Methodology Retirement

**Priority:** MUST

An obsolete methodology shall be disableable or removable from active
execution without deleting historical evidence.

---

# 18. Security and Scientific Integrity

## REQ-SEC-001 — Input Integrity

**Priority:** MUST

Experimental source material shall remain identifiable and protected from
silent modification.

---

## REQ-SEC-002 — Provenance Integrity

**Priority:** MUST

The system shall provide mechanisms for detecting unauthorized alteration
of scientific evidence.

---

## REQ-SEC-003 — External Boundary Visibility

**Priority:** MUST

External data transmission shall be explicit and auditable.

---

## REQ-SEC-004 — Auditability

**Priority:** MUST

Substantive changes to experimental configuration, methodology or evidence
shall be traceable.

---

# 19. Temporal Requirements

## REQ-TEMP-001 — Observation Timestamp

**Priority:** MUST

Experimental observations shall include a timestamp.

---

## REQ-TEMP-002 — Methodology Temporal Context

**Priority:** MUST

Results shall be interpretable in the context of the methodology versions
available at the time of measurement.

---

## REQ-TEMP-003 — Historical Stability

**Priority:** MUST

New methodology versions shall not silently rewrite historical results.

---

# 20. Emerging-Method Requirements

## REQ-EMERGE-001 — New Method Intake

**Priority:** MUST

The research framework shall provide a defined mechanism for introducing
newly discovered watermark, detector or evaluation methodologies.

---

## REQ-EMERGE-002 — Evidence Before Activation

**Priority:** MUST

A newly discovered methodology shall be evaluated before being treated as
an active scientific instrument.

---

## REQ-EMERGE-003 — Compatibility Assessment

**Priority:** MUST

New methodologies shall undergo compatibility assessment before integration
into established experiment workflows.

---

# 21. Validation Requirements

## REQ-VAL-001 — Requirement Verification

**Priority:** MUST

Every MUST requirement shall have a corresponding verification method.

---

## REQ-VAL-002 — Requirement Traceability

**Priority:** MUST

Requirements shall be traceable to specifications, implementation and
validation evidence.

---

## REQ-VAL-003 — Regression Protection

**Priority:** MUST

Changes shall not invalidate previously accepted scientific behaviour
without detection.

---

# 22. Resource Requirements

## REQ-RES-001 — Storage Budget

**Priority:** MUST

The local project shall be designed around an approximately 30 GB storage
budget unless explicitly changed through project governance.

---

## REQ-RES-002 — Resource Accounting

**Priority:** SHOULD

Major datasets and computational artifacts should have documented storage
and computational cost.

---

## REQ-RES-003 — Efficient Retention

**Priority:** SHOULD

The project should retain scientifically valuable evidence while avoiding
unnecessary duplication.

---

# 23. Documentation Requirements

## REQ-DOC-001 — Scientific Traceability

**Priority:** MUST

Every normative scientific requirement shall be traceable to its source
objective or research evidence.

---

## REQ-DOC-002 — Change Propagation

**Priority:** MUST

Substantive changes to scientific requirements shall trigger impact
assessment of dependent documentation.

---

## REQ-DOC-003 — Research Integration

**Priority:** MUST

Relevant new scientific findings shall be recorded before they are used
to justify normative changes.

---

## REQ-DOC-004 — Open Questions

**Priority:** MUST

Unresolved scientific questions affecting requirements shall be recorded
explicitly.

---

# 24. Requirement Lifecycle

A requirement shall progress through:

PROPOSED
→ REVIEWED
→ ACCEPTED
→ VERIFIED
→ ACTIVE
→ SUPERSEDED
→ RETIRED

A requirement shall never disappear silently.

---

# 25. Requirement Change Rules

A requirement may change only when:

1. new evidence is identified;
2. the impact is assessed;
3. dependent requirements are identified;
4. the relevant specification is updated;
5. validation consequences are identified;
6. the decision is recorded.

Historical requirement versions shall remain recoverable.

---

# 26. Requirement Conflict

When two requirements conflict:

1. identify the conflict explicitly;
2. determine their authority and priority;
3. consult the relevant research evidence;
4. record possible resolutions;
5. escalate when the conflict exceeds autonomous authority.

Claude Code must not silently resolve a C3 or C4 conflict.

---

# 27. Scientific Ground-Truth Rule

The system shall distinguish among:

- known ground truth;
- experimentally established observation;
- detector output;
- inferred classification;
- hypothesis;
- assumption;
- unknown.

These categories shall never be silently conflated.

---

# 28. Completion Criteria

S02 is complete when:

- all major S01 objectives have downstream requirements;
- every MUST requirement has a verification concept;
- requirements have unique identifiers;
- multilingual requirements are explicit;
- watermark and detector requirements are separated;
- transformation and preservation requirements are explicit;
- provenance and reproducibility are explicit;
- lifecycle and extensibility are explicit;
- external-service behaviour is specified;
- temporal evolution is addressed;
- requirement conflicts and changes have defined procedures.

---

# 29. Final Principle

Scientific requirements must be precise enough to test, flexible enough to
evolve, and traceable enough to audit.

The purpose of requirements is not to freeze scientific knowledge.

The purpose is to create a stable framework in which new evidence can
change the system deliberately, visibly and reproducibly.