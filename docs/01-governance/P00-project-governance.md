# P00 — Project Governance & Agent Autonomy

## Status

FOUNDATIONAL / NORMATIVE

## Purpose

This document defines the governance model of the project and the
relationship between human authority, autonomous AI-assisted development,
scientific research, implementation and validation.

It is intended to allow Claude Code to perform large bounded bodies of
work autonomously while preventing uncontrolled changes to requirements,
security boundaries, scientific criteria or architectural principles.

---

# 1. Fundamental Principle

The human approves bounded work packages, not individual implementation
actions.

Claude Code is expected to operate autonomously inside an approved
boundary and to perform its own intermediate verification.

Human intervention is required only when a decision exceeds the agent's
authority.

---

# 2. Authority Hierarchy

Authority follows this order:

1. Human governance
2. Project Constitution
3. Security and safety invariants
4. Normative requirements
5. Scientific specifications
6. Architecture
7. Implementation
8. Tests and validation artifacts
9. Informative documentation

A lower-level artifact may not silently redefine a higher-level artifact.

---

# 3. Human Authority

The human retains exclusive authority over:

- constitutional principles;
- security-boundary changes;
- fundamental requirement changes;
- architectural breaking changes;
- major resource-budget changes;
- release approval;
- unresolved conflicts between fundamental objectives;
- explicit legal/licensing decisions.

---

# 4. Autonomous Agent Authority

Claude Code may autonomously:

- create and modify implementation;
- create and modify tests;
- perform refactoring;
- correct ordinary defects;
- update documentation;
- update registries;
- perform impact analysis;
- run benchmarks;
- run regression tests;
- update metadata;
- install previously authorized dependencies;
- remove obsolete internal code where removal is already authorized;
- perform rollback of its own failed work;
- produce research and engineering reports;
- identify inconsistencies;
- resolve local inconsistencies without changing higher-level requirements.

---

# 5. Human Approval Gates

Human approval is required for:

- constitutional changes;
- security-boundary changes;
- architectural breaking changes;
- new classes of external data transmission;
- unresolved requirement conflicts;
- unresolved critical scientific conflicts;
- release promotion;
- changes exceeding the approved resource budget.

---

# 6. Autonomous Verification

Before requesting human approval, Claude Code must perform, where
applicable:

1. requirement verification;
2. implementation verification;
3. test execution;
4. regression testing;
5. dependency verification;
6. security verification;
7. resource-budget verification;
8. documentation consistency verification;
9. traceability verification;
10. research-evidence verification;
11. reproducibility verification.

The agent should repair local failures before requesting intervention.

---

# 7. Stop Conditions

Claude Code must stop and report rather than improvise when encountering:

- constitutional conflict;
- security-boundary conflict;
- architectural conflict;
- unresolved critical regression;
- incompatible normative requirements;
- critical scientific ambiguity;
- resource-budget violation that cannot be resolved safely;
- licensing/legal uncertainty requiring human judgment.

---

# 8. Non-Goals of Autonomous Operation

Claude Code must not:

- weaken a requirement solely to make a test pass;
- disable validation to obtain a successful build;
- silently alter a normative definition;
- delete evidence required for reproducibility;
- conceal a regression;
- silently transmit protected input to an unauthorized external service;
- modify audit history to conceal a change;
- remove a security control because it is inconvenient;
- redefine the project objective.

---

# 9. Invariants

The following invariants are mandatory.

### I-001 — No Silent Requirement Weakening

A failed implementation must not be made successful by silently weakening
the requirement.

### I-002 — No Silent Security Relaxation

Security controls may not be weakened without the appropriate authority.

### I-003 — No Silent Evidence Destruction

Evidence required for reproducibility must not be deleted without an
explicit retention decision.

### I-004 — No Hidden External Processing

External processing of protected input must be explicit and traceable.

### I-005 — No Orphaned Capability

A newly introduced production capability must have lifecycle metadata.

### I-006 — No Untracked Dependency

New dependencies must be recorded and validated.

### I-007 — No Unverified Documentation Closure

A documentation change cannot be considered complete until the relevant
consistency checks have passed.

---

# 10. Macro-Tranche Model

The project is executed through bounded macro-tranches.

A tranche contains:

- objective;
- scope;
- authorized changes;
- expected outputs;
- Definition of Done;
- verification criteria;
- resource budget;
- stop conditions.

Once a tranche is approved, Claude Code may operate autonomously within
that boundary.

---

# 11. Tranche Completion

A tranche may be presented for approval only when:

- all mandatory objectives are complete;
- tests pass;
- regressions are resolved;
- documentation is synchronized;
- required evidence is recorded;
- dependencies are consistent;
- no unauthorized changes remain;
- the Definition of Done is satisfied.

If the criteria cannot be satisfied, the agent must report BLOCKED rather
than redefining the criteria.

---

# 12. Change Impact Levels

Changes should be classified as:

### C0 — Informational

Metadata or non-substantive documentation changes.

### C1 — Local

Local implementation or documentation changes with no architectural
impact.

### C2 — Component

Changes affecting a bounded component or interface-compatible capability.

### C3 — Architectural

Changes affecting architecture, major interfaces or system boundaries.

### C4 — Constitutional

Changes affecting fundamental project principles, security invariants or
normative objectives.

C0-C2 may normally be handled autonomously within an approved tranche.

C3 normally requires an approval gate.

C4 always requires human authority.

---

# 13. Maintainability Requirement

Maintainability is an architectural requirement.

The system must be designed so that:

- new capabilities can be added;
- obsolete capabilities can be deprecated;
- retired capabilities can be removed;
- dependencies can be replaced;
- research-derived components can evolve;
- interfaces remain understandable;
- configuration remains explicit;
- documentation remains synchronized.

---

# 14. Additive-by-Default Principle

When introducing a new capability, the default architectural preference is
to add a component, adapter, plugin or registry entry rather than modify
unrelated core functionality.

This principle may be overridden when research or architectural analysis
demonstrates that a core change is necessary.

---

# 15. Capability Lifecycle

Production capabilities should follow:

DISCOVERED
→ EXPERIMENTAL
→ VALIDATED
→ ACTIVE
→ DEPRECATED
→ RETIRED
→ REMOVED

Each major capability must have:

- identifier;
- version;
- owner/maintainer role;
- dependencies;
- validation status;
- documentation;
- retirement path.

---

# 16. Scientific Evolution

New research does not automatically modify production behavior.

A new finding must pass through:

Research Registry
→ Impact Assessment
→ Specification Decision
→ Validation
→ Implementation
→ Certification

A finding may also be recorded as having no production impact.

---

# 17. Documentation Governance

The project documentation is a connected knowledge system.

Important knowledge must be represented in one or more of:

- Project Map;
- Knowledge Backlog;
- Research Registry;
- Decision Log;
- Open Questions;
- Assumption Registry;
- Documentation Change Queue;
- normative specification.

Claude Code must perform cross-document impact analysis when making
substantive changes.

---

# 18. Final Repository Certification

Final review is delegated to Claude Code because the agent has access to
the complete repository and can inspect:

- documentation;
- source;
- tests;
- registries;
- dependencies;
- Git history;
- configuration;
- validation artifacts.

Certification must include:

- documentation completeness;
- cross-reference integrity;
- requirement traceability;
- test coverage;
- dependency consistency;
- lifecycle consistency;
- security invariants;
- research traceability;
- reproducibility.

The agent must not certify unresolved failures as successful.

---

# 19. Human Review Philosophy

Human review should focus on decisions rather than line-by-line
implementation.

The desired operating model is:

Human:
    approves bounded objective

Claude Code:
    executes
    verifies
    repairs
    documents
    tests
    reports

Human:
    approves next bounded objective

---

# 20. Governing Principle

The project must remain:

- understandable;
- auditable;
- reversible;
- reproducible;
- extensible;
- maintainable;
- scientifically updateable.

Autonomy must increase execution efficiency without reducing governance,
traceability or scientific integrity.

---

# 21. Scientific Neutrality and Experimental Boundary

The project distinguishes scientific experimentation from production
behavior.

Experimental components may be used to investigate:

- watermark behavior;
- watermark detectability;
- AI-generated-text detection;
- detector robustness;
- false positives and false negatives;
- multilingual effects;
- linguistic variation;
- text transformations;
- semantic preservation;
- stylistic preservation;
- statistical properties;
- reproducibility;
- interactions between detectors and transformations.

Experimental results must be reported without assuming that a detector,
watermark or transformation is inherently correct or incorrect.

The system must preserve the distinction between:

- observation;
- hypothesis;
- measured result;
- interpretation;
- engineering requirement.

A measured detector response is evidence, not automatically a ground-truth
label.

---

# 22. Separation of Evaluation and Production Behavior

An experimental transformation must not automatically become a production
capability.

Before a transformation or algorithm can be incorporated into an approved
production workflow, the project must establish:

- its scientific purpose;
- its measurable behavior;
- its preservation characteristics;
- its limitations;
- its validation methodology;
- its security implications;
- its reproducibility;
- its effect on other project requirements.

Experimental capability and production capability must therefore have
distinct lifecycle states.

---

# 23. Detector and Watermark Evaluation Boundary

The project may evaluate detectors and watermarking systems scientifically.

Evaluation may include:

- sensitivity;
- specificity;
- false-positive rate;
- false-negative rate;
- calibration;
- robustness;
- language dependence;
- domain dependence;
- text-length dependence;
- paraphrase sensitivity;
- formatting sensitivity;
- model dependence;
- reproducibility;
- temporal stability.

Detector outputs must be treated as measurements with documented provenance.

A detector result must never be silently converted into an unquestioned
ground-truth label.

Watermark experiments must likewise document:

- watermark family;
- implementation or reference;
- configuration;
- generation conditions;
- detector conditions;
- language;
- text length;
- sampling or generation parameters where relevant;
- statistical test;
- confidence or uncertainty;
- experimental version.

---

# 24. No Detector-Driven Objective Substitution

A detector result must not silently become the optimization objective of
an experimental transformation.

If an experiment studies the relationship between a transformation and a
detector, the experiment must explicitly define:

- the hypothesis;
- the independent variables;
- the dependent variables;
- preservation metrics;
- detector metrics;
- stopping criteria;
- statistical methodology.

Changing the experimental objective requires an explicit scientific
decision and appropriate documentation.

---

# 25. Reproducibility of Negative Results

Negative, inconclusive and failed experiments are first-class scientific
results.

The project must preserve sufficient information to reproduce them when
practical.

An unsuccessful experiment must not be silently removed because it produces
unfavorable results.

Where an experiment cannot be reproduced, the reason must be recorded.

---

# 26. Scientific Change Trigger

New literature, watermark methodologies, detector methodologies, languages,
datasets or evaluation techniques may trigger a scientific reassessment.

The normal process is:

NEW EVIDENCE
→ RESEARCH REGISTRY
→ IMPACT ASSESSMENT
→ DOCUMENTATION CHANGE QUEUE
→ AFFECTED SPECIFICATIONS
→ AFFECTED EXPERIMENTS
→ VALIDATION

The existence of a new detector or watermark does not by itself require a
change to production behavior.

The project must first determine its scientific relevance.

---

# 27. Evidence Over Assumption

When experimental evidence conflicts with an existing assumption, the
conflict must be recorded.

The project must not preserve an assumption merely because it is already
embedded in architecture or implementation.

The appropriate response is:

OBSERVATION
→ EVIDENCE REVIEW
→ ASSUMPTION UPDATE
→ DECISION
→ IMPACT ANALYSIS
→ VALIDATION

---

# 28. Scientific Integrity of Autonomous Development

Claude Code may implement experiments and analysis pipelines autonomously
within an approved tranche.

It must not:

- fabricate scientific evidence;
- alter experimental data to obtain a desired result;
- omit unfavorable results from a required report;
- silently change statistical methodology;
- change evaluation criteria after observing results;
- represent an experimental observation as an established scientific fact.

If scientific methodology is ambiguous in a material way, the agent must
record the ambiguity and use the project's approved research methodology
rather than inventing a conclusion.

---

# 29. Research-to-Engineering Separation

Research findings and engineering requirements must remain distinguishable.

A research result may produce:

- a new requirement;
- a new validation criterion;
- a new architecture requirement;
- a new experiment;
- a documented limitation;
- no engineering change.

The project must explicitly record which of these outcomes occurred.

---

# 30. Governance Extension Rule

Future governance requirements must be added rather than silently replacing
existing principles.

When a new governance rule conflicts with an existing rule, Claude Code must:

1. identify the conflict;
2. record it;
3. identify affected documents;
4. determine the applicable authority level;
5. stop if human authority is required;
6. otherwise apply the higher-level rule.

Governance documents are normative and must therefore be treated as
versioned project artifacts.

