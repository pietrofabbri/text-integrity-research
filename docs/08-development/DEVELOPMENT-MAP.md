# Development Map

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Development architecture and autonomous engineering process
**Authority:** Development
**Scope:** Software development, AI-assisted development, testing,
maintenance, refactoring, dependency management, change control and
autonomous work batches

---

## 1. Purpose

This document defines how the software is developed and maintained.

The project is intentionally designed so that an AI coding agent can perform
large portions of implementation and maintenance autonomously while
remaining inside a clearly defined technical, scientific and security
perimeter.

The objective is not to eliminate human oversight.

The objective is to concentrate human oversight on meaningful architectural,
scientific and security decisions rather than routine implementation.

---

# 2. Development Principle

The development process follows:

DEFINE
→ IMPLEMENT
→ VERIFY
→ INTEGRATE
→ DOCUMENT
→ REVALIDATE

No implementation should be considered complete merely because the code
runs.

---

# 3. AI-Assisted Development

The software may be developed and maintained using Claude Code or another
AI coding agent.

The coding agent is an implementation and maintenance mechanism.

It is not the final authority on:

- scientific truth;
- security policy;
- project objectives;
- empirical validity.

Those authorities remain defined by project documentation and validation
criteria.

---

# 4. Runtime Independence from AI

The production software must not require an AI coding assistant to execute.

Development may use AI.

Runtime must remain independent of the development agent.

This distinction is fundamental.

---

# 5. No Runtime AI Requirement

Unless a future capability explicitly specifies otherwise, the core runtime
must not require:

- Claude;
- ChatGPT;
- an LLM API;
- an AI coding agent;
- cloud inference.

AI may be used during development without being present during execution.

---

# 6. Local-First Development

Development should prioritize:

- local execution;
- local tests;
- deterministic tools;
- reproducible environments.

External services are optional and explicitly controlled.

---

# 7. Autonomous Work Model

Development should be organized into bounded autonomous work batches.

A batch may contain multiple logically related changes.

The goal is to avoid requiring the human operator to approve every small
operation.

---

# 8. Work Batch Definition

Each batch should define:

- objective;
- scope;
- expected files;
- dependencies;
- validation requirements;
- security classification;
- completion criteria.

---

# 9. Batch Scope

Claude Code may modify any files necessary to complete an approved batch,
provided that:

- the files are within the declared project scope;
- the change remains consistent with project architecture;
- security boundaries are preserved;
- scientific assumptions are not silently changed.

---

# 10. Batch Autonomy

Within a LOW-risk batch, Claude Code may:

- inspect files;
- create files;
- modify code;
- refactor;
- create tests;
- run tests;
- update documentation;
- update manifests;
- update dependency metadata.

It should not stop for approval after every individual operation.

---

# 11. Batch Completion

A batch is complete only when:

1. implementation exists;
2. tests have been executed;
3. relevant validation passes;
4. documentation is synchronized;
5. dependency changes are recorded;
6. security-sensitive changes are identified;
7. unresolved issues are reported.

---

# 12. Automatic Stop Conditions

Claude Code should stop the current batch when it encounters:

- a CRITICAL security change;
- an undocumented architectural conflict;
- destructive data loss risk;
- an unresolved scientific assumption;
- an unexpected external service requirement;
- incompatible licensing;
- inability to validate a critical requirement.

The stop should be precise and actionable.

---

# 13. Avoiding Approval Fatigue

The development process should minimize unnecessary human interruption.

Claude Code should prefer:

- grouping compatible work;
- running validation automatically;
- resolving routine implementation details independently;
- recording uncertainty rather than repeatedly asking questions;
- stopping only at predefined decision boundaries.

---

# 14. Decision Boundaries

Human input is normally required when a change affects:

- project objectives;
- core scientific acceptance criteria;
- security trust boundaries;
- privacy policy;
- external data transmission;
- fundamental architecture;
- licensing assumptions;
- irreversible destruction of scientific evidence.

---

# 15. Routine Engineering Decisions

Claude Code may make routine engineering decisions autonomously when they:

- do not change project objectives;
- do not weaken security;
- do not invalidate scientific assumptions;
- are reversible;
- are tested.

Examples:

- function organization;
- internal naming;
- non-functional refactoring;
- test structure;
- local caching implementation;
- internal helper extraction.

---

# 16. Change Classification

Every significant development change should be classified:

LOW
MEDIUM
HIGH
CRITICAL

The security map defines the corresponding security implications.

---

# 17. Low-Risk Changes

Examples:

- documentation corrections;
- test additions;
- internal refactoring;
- formatting;
- deterministic bug fixes with existing tests.

These may normally be completed autonomously.

---

# 18. Medium-Risk Changes

Examples:

- new capability;
- dependency update;
- data pipeline change;
- API change;
- new internal abstraction.

These require stronger automated validation.

---

# 19. High-Risk Changes

Examples:

- network integration;
- new external service;
- model loading mechanism;
- major architecture change;
- significant data handling change.

These must be clearly reported and isolated.

---

# 20. Critical Changes

Examples:

- arbitrary code execution;
- security boundary modification;
- credential architecture;
- uncontrolled external transmission;
- destructive migration.

These require explicit human approval.

---

# 21. Development Phases

Development should conceptually proceed through:

PHASE 0 — documentation and research
PHASE 1 — architecture
PHASE 2 — infrastructure
PHASE 3 — core implementation
PHASE 4 — capability implementation
PHASE 5 — validation
PHASE 6 — certification
PHASE 7 — maintenance

The project may iterate between phases.

---

# 22. Documentation Before Implementation

A major capability should not be implemented without an adequate
specification.

The specification does not need to predict every implementation detail.

It must define:

- purpose;
- inputs;
- outputs;
- constraints;
- dependencies;
- validation;
- failure behavior.

---

# 23. Research Before Capability

Where a capability depends on scientific claims, implementation should follow
research review.

The project must distinguish:

KNOWN
SUPPORTED
PLAUSIBLE
EXPERIMENTAL
UNKNOWN

---

# 24. Scientific Uncertainty

Claude Code must not convert an unresolved research question into an
apparently settled implementation rule without documenting the assumption.

---

# 25. Implementation Strategy

Prefer small composable capabilities rather than one monolithic algorithm.

This makes it easier to:

- add new research methods;
- compare alternatives;
- disable obsolete methods;
- replace dependencies;
- test individual components.

---

# 26. Capability Isolation

Each major capability should have:

- defined input;
- defined output;
- version;
- dependencies;
- tests;
- status;
- documentation.

---

# 27. Capability Lifecycle

Capabilities should support:

DRAFT
→ EXPERIMENTAL
→ VALIDATED
→ ACTIVE
→ MONITORED
→ DEPRECATED
→ RETIRED

---

# 28. Experimental Capability

An experimental capability may be used in research but must not automatically
be treated as part of the certified production pipeline.

---

# 29. Activation

A capability becomes ACTIVE only after satisfying its validation criteria.

---

# 30. Deprecation

A capability should be deprecated rather than immediately deleted when:

- a better method replaces it;
- a dependency becomes obsolete;
- evidence shows poor performance;
- maintenance cost becomes excessive;
- a new methodology supersedes it.

---

# 31. Retirement

Retirement means the capability is no longer used by the active system.

Historical evidence and metadata should remain available.

---

# 32. Replacement

A retired capability should identify its replacement where one exists.

The replacement must independently satisfy validation requirements.

---

# 33. Modularity

The architecture should favor interfaces that allow components to be
replaced without rewriting unrelated parts of the system.

---

# 34. Stable Interfaces

Internal interfaces should remain stable where practical.

When breaking changes are necessary:

- document them;
- update dependents;
- run regression tests;
- update architecture documentation.

---

# 35. Dependency Graph

The development process must recognize dependencies between:

- code;
- datasets;
- models;
- linguistic resources;
- detectors;
- validators;
- documentation.

A change to one node may require validation of dependent nodes.

---

# 36. Impact Analysis

Before a material change, determine:

- direct dependencies;
- indirect dependencies;
- tests affected;
- documentation affected;
- benchmark effects;
- security effects.

---

# 37. Documentation Synchronization

When implementation changes architecture, update the relevant documentation
in the same development batch.

Documentation debt must not be intentionally accumulated.

---

# 38. Documentation Change Queue

If a complete documentation update cannot be performed immediately, create an
entry in:

docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md

The entry must identify:

- affected document;
- reason;
- required update;
- implementation dependency;
- priority.

---

# 39. Knowledge Backlog

Research ideas that are relevant but not yet ready for implementation should
go into:

docs/00-project/KNOWLEDGE-BACKLOG.md

They should not be lost inside chat history or temporary notes.

---

# 40. Open Questions

Unresolved decisions should be recorded in:

docs/00-project/OPEN-QUESTIONS.md

The purpose is to prevent uncertainty from disappearing between development
sessions.

---

# 41. Decision Log

Material decisions should be recorded in:

docs/00-project/DECISION-LOG.md

This provides historical context for future maintenance.

---

# 42. Assumption Registry

Assumptions should be recorded in:

docs/00-project/ASSUMPTION-REGISTRY.md

An assumption that becomes invalid should be updated rather than silently
replaced.

---

# 43. Research Registry

External research sources and scientific evidence should be registered in:

docs/00-project/RESEARCH-REGISTRY.md

This prevents rediscovery and loss of provenance.

---

# 44. Change Queue Discipline

Claude Code should check the documentation change queue at the beginning and
end of significant work batches.

---

# 45. End-of-Batch Documentation Sweep

Before completing a batch, Claude Code should ask internally:

- Did implementation change architecture?
- Did implementation change security?
- Did implementation change data requirements?
- Did implementation change validation?
- Did implementation introduce a new assumption?
- Did implementation invalidate an existing document?

If yes, update the relevant documentation or create a queue entry.

---

# 46. Test-First Preference

Where practical, tests should be written before or alongside implementation.

The project should not depend exclusively on manual inspection.

---

# 47. Test Categories

The project should distinguish:

- unit tests;
- integration tests;
- regression tests;
- security tests;
- data validation tests;
- scientific validation tests;
- performance tests;
- reproducibility tests.

---

# 48. Unit Tests

Unit tests verify isolated behavior.

They should be deterministic wherever possible.

---

# 49. Integration Tests

Integration tests verify interactions between capabilities.

Examples:

- preprocessing → transformation;
- transformation → validation;
- dataset → experiment;
- detector adapter → result normalization.

---

# 50. Regression Tests

Every important discovered failure should become a regression test when
practical.

---

# 51. Security Tests

Security tests should cover the boundaries defined in the security map.

---

# 52. Data Tests

Data tests should verify:

- manifests;
- checksums;
- expected schemas;
- encodings;
- resource availability.

---

# 53. Scientific Tests

Scientific tests should verify properties relevant to the research
hypothesis.

They are distinct from ordinary software correctness tests.

---

# 54. Performance Tests

Performance tests should measure:

- execution time;
- memory;
- storage;
- throughput;
- scalability.

Performance should not be optimized at the expense of scientific validity
without explicit justification.

---

# 55. Reproducibility Tests

Where practical, repeat an experiment using the same:

- input;
- dataset;
- configuration;
- software version;
- resource versions.

The expected result should be reproducible within defined tolerances.

---

# 56. Determinism

The system should distinguish:

DETERMINISTIC
from
STOCHASTIC

For stochastic components, record:

- seed;
- sampling parameters;
- model version;
- relevant environment.

---

# 57. Random Seeds

Tests should use fixed seeds when deterministic behavior is required.

Production experimentation may intentionally use multiple seeds.

---

# 58. Numerical Tolerances

Floating-point comparisons should use defined tolerances rather than exact
equality where appropriate.

---

# 59. Test Isolation

Tests should not depend on:

- previous test execution;
- undeclared local files;
- network availability;
- developer-specific configuration.

---

# 60. Offline Test Suite

The project should provide a test mode that runs without network access.

---

# 61. Network Regression

Changes must not introduce hidden network access.

Network-dependent tests must be clearly identified.

---

# 62. External Service Tests

External services should use:

- mocks;
- fixtures;
- recorded responses;
- controlled integration tests;

where practical.

The complete test suite must not depend on a third-party service being
available.

---

# 63. Test Fixtures

Fixtures should be:

- versioned;
- small;
- deterministic;
- representative.

Sensitive real-world documents should not be used unnecessarily.

---

# 64. Benchmark Integrity

Benchmarks must not be modified merely to make a new implementation perform
better.

Changes to benchmark data require explicit versioning.

---

# 65. Scientific Holdout

Where a holdout set is defined, development must not silently optimize
against it.

---

# 66. Test Contamination

Tests should not accidentally become training or tuning data for capabilities
being evaluated.

---

# 67. Code Quality

The project should use automated checks for:

- syntax;
- formatting;
- linting;
- type consistency where applicable;
- dependency integrity;
- tests.

---

# 68. Static Analysis

Static analysis should be used where it materially improves reliability.

Security-sensitive code should receive stronger static inspection.

---

# 69. Type Safety

Where the chosen language supports it, explicit types should be preferred
for important interfaces.

---

# 70. Error Handling

Errors should be:

- explicit;
- categorized;
- actionable;
- non-destructive.

Silent failure is discouraged.

---

# 71. Fail-Safe Principle

When the system cannot establish that an operation is safe or valid, it
should prefer:

- explicit failure;
- degraded capability;
- unavailable result;

rather than fabricating success.

---

# 72. Result Status

Important operations should distinguish:

SUCCESS
PARTIAL
FAILED
UNAVAILABLE
INVALID
NOT_EVALUATED

---

# 73. No Fabricated Scientific Results

The software must never infer a successful scientific result merely because
a processing pipeline completed technically.

---

# 74. Logging

Development and runtime logs should provide enough information for
diagnostics while respecting the security and privacy maps.

---

# 75. Reproducible Builds

Where practical, builds should be reproducible from:

- source;
- dependency versions;
- configuration;
- declared artifacts.

---

# 76. Environment Declaration

The project should declare required:

- runtime versions;
- operating system assumptions;
- system dependencies;
- package dependencies.

---

# 77. Dependency Management

Every dependency should have:

- purpose;
- version;
- license;
- source;
- compatibility information.

---

# 78. Dependency Minimization

Avoid adding dependencies for functionality that can be safely implemented
with existing components.

Every dependency adds:

- maintenance cost;
- security surface;
- compatibility risk;
- storage cost.

---

# 79. Dependency Updates

Dependency updates should be performed deliberately.

After an update:

- run tests;
- inspect changelog where available;
- inspect security implications;
- verify scientific regressions where relevant.

---

# 80. Dependency Retirement

Unused dependencies should be removed.

A dependency should not remain merely because it was once useful.

---

# 81. Model Dependencies

Models are dependencies and must be versioned like software dependencies.

A model update may change scientific behavior even if the software code is
unchanged.

---

# 82. Dataset Dependencies

Dataset changes may also change software results.

Dataset version must therefore be part of experiment identity.

---

# 83. Interface Contracts

Components should expose explicit contracts for:

- inputs;
- outputs;
- errors;
- configuration;
- supported languages;
- resource requirements.

---

# 84. Language Capability Contracts

A multilingual component must explicitly declare which languages it supports.

"Multilingual" must not be interpreted as "equally capable in every
language."

---

# 85. Unsupported Languages

If a capability does not support a language adequately, it must return an
explicit unsupported/degraded state rather than silently producing a result
that appears equivalent.

---

# 86. Language Expansion

Adding a language should be treated as a capability expansion.

It requires:

- language resources;
- tests;
- validation;
- documentation;
- performance assessment.

---

# 87. Language Retirement

A language may be temporarily or permanently disabled if:

- required resources disappear;
- performance is inadequate;
- security issues arise;
- maintenance becomes unsustainable.

Historical results remain identified by the previous capability state.

---

# 88. Configuration

Configuration should be:

- explicit;
- validated;
- versionable;
- documented.

Avoid hidden environment-dependent behavior.

---

# 89. Configuration Defaults

Defaults must be safe and conservative.

A developer's local configuration must not silently become a production
requirement.

---

# 90. Feature Flags

Feature flags may be used to:

- activate experimental capabilities;
- disable obsolete components;
- compare implementations;
- roll back risky changes.

---

# 91. Capability Registry

The project should maintain a registry containing at least:

- capability ID;
- version;
- status;
- dependencies;
- supported languages;
- validation state;
- replacement;
- deprecation state.

---

# 92. Dynamic Capability Selection

Where practical, capabilities should be selected through explicit registry
configuration rather than hard-coded branching.

This simplifies future replacement.

---

# 93. Algorithm Replacement

A new algorithm should be installable alongside the old one during validation.

Do not immediately destroy the old implementation merely because a new
candidate exists.

---

# 94. Comparative Evaluation

Competing implementations should be evaluated under the same:

- dataset;
- input;
- language;
- configuration;
- validation criteria.

---

# 95. Champion/Challenger Model

Where useful, the active capability can be compared against one or more
challenger implementations.

This is especially useful when scientific knowledge evolves rapidly.

---

# 96. Obsolete Method Detection

A capability should be considered for deprecation when evidence shows:

- consistently inferior performance;
- incompatibility;
- security problems;
- excessive maintenance cost;
- scientific invalidation.

---

# 97. No Premature Deletion

Deprecated code should not be immediately deleted if it is still needed for:

- historical reproduction;
- comparison;
- migration;
- scientific auditing.

---

# 98. Migration

When replacing a capability:

1. implement replacement;
2. run parallel validation;
3. compare results;
4. document differences;
5. activate replacement;
6. deprecate old capability;
7. retire old capability when safe.

---

# 99. Backward Compatibility

Maintain backward compatibility where it provides meaningful scientific or
operational value.

Do not preserve obsolete interfaces indefinitely without reason.

---

# 100. API Stability

Public interfaces should follow semantic versioning or another documented
versioning strategy.

---

# 101. Internal Interfaces

Internal interfaces may evolve more quickly but must still maintain clear
contracts.

---

# 102. Refactoring

Refactoring should preserve externally observable behavior unless the change
is explicitly intended.

Refactoring should be accompanied by tests.

---

# 103. Large Refactors

Large refactors should be divided into independently verifiable steps.

Avoid mixing:

- architecture migration;
- scientific changes;
- unrelated cleanup;

in one opaque change.

---

# 104. Commit Discipline

Changes should be logically grouped.

A commit should ideally represent one coherent engineering purpose.

---

# 105. Commit Messages

Commit messages should describe the purpose rather than merely listing files.

---

# 106. Revertability

Important changes should be reversible.

Before risky changes, ensure the previous state can be reconstructed.

---

# 107. Rollback

Rollback mechanisms should exist for:

- capability activation;
- dependency updates;
- configuration changes;
- migrations.

---

# 108. Release Candidate

Before a release:

- tests pass;
- security checks pass;
- data manifests validate;
- documentation is synchronized;
- dependencies are recorded;
- certification status is known.

---

# 109. Release Artifact

A release should identify:

- software version;
- source revision;
- dependency versions;
- dataset versions;
- model versions;
- configuration;
- validation status.

---

# 110. Development Metrics

Useful development metrics include:

- test pass rate;
- regression count;
- unresolved issues;
- dependency age;
- documentation debt;
- capability coverage;
- validation coverage.

Metrics must not become targets that encourage gaming.

---

# 111. Technical Debt

Technical debt should be recorded rather than forgotten.

Each significant debt item should have:

- description;
- impact;
- reason;
- priority;
- possible resolution.

---

# 112. Documentation Debt

Documentation debt should be recorded in the documentation change queue.

---

# 113. Scientific Debt

Scientific uncertainties should be recorded separately from ordinary
technical debt.

---

# 114. Security Debt

Security weaknesses must not be hidden inside generic technical debt.

They should remain visible through the security process.

---

# 115. Autonomous Consistency Review

At the end of every substantial batch, Claude Code should perform a
repository-wide consistency check.

At minimum inspect:

- project map;
- affected architecture documents;
- affected specifications;
- security map;
- data map;
- validation map;
- development documentation;
- decision log;
- assumption registry;
- documentation change queue.

---

# 116. Dependency Consistency Review

The agent should verify:

- imports;
- declared dependencies;
- manifests;
- configuration;
- capability registry;
- dataset/model dependencies.

---

# 117. Interface Consistency Review

The agent should verify that changed interfaces remain consistent across:

- callers;
- implementations;
- tests;
- documentation.

---

# 118. Documentation Consistency Review

The agent should search for:

- obsolete names;
- old paths;
- removed capabilities;
- stale versions;
- contradictory requirements;
- references to nonexistent files.

---

# 119. Security Consistency Review

The agent should check whether changes introduced:

- network calls;
- new permissions;
- subprocesses;
- dynamic loading;
- credential handling;
- external transmission.

---

# 120. Scientific Consistency Review

The agent should check whether changes alter:

- experimental assumptions;
- benchmark definitions;
- acceptance criteria;
- language scope;
- interpretation of results.

---

# 121. Data Consistency Review

The agent should check:

- dataset identifiers;
- versions;
- manifests;
- checksums;
- declared dependencies;
- storage requirements.

---

# 122. Automated Repository Audit

The project should eventually provide a command that performs the above
checks automatically.

The command should produce:

PASS
WARN
FAIL

results.

---

# 123. Audit Severity

Suggested levels:

PASS
WARNING
BLOCKING

A WARNING may be reported without stopping a batch.

A BLOCKING issue prevents completion.

---

# 124. Autonomous Batch Report

At the end of a batch, Claude Code should produce a concise report containing:

- objective;
- files changed;
- tests run;
- tests passed;
- tests failed;
- dependencies changed;
- security impact;
- documentation impact;
- unresolved questions;
- recommended next batch.

---

# 125. No Hidden Changes

Claude Code must not intentionally modify unrelated files merely to make a
batch pass.

Unrelated changes should be separated or explicitly documented.

---

# 126. Generated Files

Generated files must be distinguishable from authoritative source files.

The project should document which files are generated.

---

# 127. Source of Truth

For every important artifact, identify its source of truth.

Examples:

- specification → documentation;
- generated configuration → source template;
- benchmark manifest → benchmark definition;
- compiled artifact → source code.

---

# 128. Regeneration

Generated artifacts should be reproducible from their source of truth where
practical.

---

# 129. Build Artifacts

Build outputs should not normally be treated as authoritative source.

---

# 130. Temporary Development Artifacts

Temporary files must not silently become project dependencies.

---

# 131. Repository Cleanliness

Before completing a batch, remove unnecessary:

- temporary files;
- debug outputs;
- caches;
- generated artifacts not required for reproducibility.

---

# 132. Development Environment Reproducibility

Another developer or agent should be able to understand:

- how to install;
- how to test;
- how to run offline;
- how to validate;
- how to reproduce a result.

---

# 133. Onboarding

The project should eventually provide a concise onboarding document.

It should point to:

- project map;
- architecture;
- development rules;
- research registry;
- validation;
- security;
- data.

---

# 134. Claude Code Onboarding

When Claude Code starts a substantial task, it should first inspect:

1. README;
2. PROJECT-MAP;
3. relevant MAP file;
4. relevant specification;
5. decision log;
6. assumption registry;
7. open questions;
8. documentation change queue.

This establishes context before modification.

---

# 135. Avoiding Context Loss

The agent should not rely on conversation history as the sole source of
project requirements.

The repository documentation is the durable source of project context.

---

# 136. Documentation Over Chat Memory

If an important idea appears during development, it must eventually become
one of:

- documentation;
- decision;
- assumption;
- open question;
- backlog item;
- change queue entry.

---

# 137. New Ideas During Implementation

If Claude Code discovers an idea outside the immediate task:

- do not silently implement it;
- determine whether it is required;
- record it in the appropriate project registry;
- continue the approved task.

---

# 138. Preventing Idea Loss

Potential improvements should be recorded in the knowledge backlog rather
than discarded merely because they fall outside the current batch.

---

# 139. Preventing Scope Explosion

Recording an idea does not authorize implementation.

The backlog is deliberately separated from active scope.

---

# 140. Documentation Layering

The documentation architecture follows:

PROJECT MAP
→ MACRO MAP
→ DETAILED SPECIFICATION
→ IMPLEMENTATION
→ VALIDATION

This allows individual documents to evolve without losing the global model.

---

# 141. Documentation Authority

If documents conflict, Claude Code must identify the conflict rather than
silently choosing a convenient interpretation.

The conflict should be recorded in the appropriate registry.

---

# 142. Documentation Revision

Documentation may be revised as research evolves.

Material revisions should preserve history and rationale.

---

# 143. Future Research Changes

The software must be designed to accommodate future discoveries.

A new scientific paper may invalidate:

- an algorithm;
- an assumption;
- a detector model;
- a language strategy;
- a validation criterion.

The architecture must allow such components to be replaced.

---

# 144. Future Detector Changes

If new detector methodologies emerge, they should be implemented as new
capabilities or adapters rather than requiring a rewrite of the core.

---

# 145. Future Watermark Research

If new watermark research emerges, the system should allow new analytical
modules to be added without invalidating unrelated infrastructure.

---

# 146. Future Language Expansion

Additional languages should be addable through modular language resources
and capability definitions.

---

# 147. Feature Removal

The architecture must support removing obsolete features.

Removal should include:

- dependency analysis;
- regression testing;
- documentation updates;
- migration where required.

---

# 148. Feature Flags and Retirement

Feature flags should not become permanent technical debt.

Retired flags should eventually be removed.

---

# 149. Maintenance Principle

Maintenance should be treated as continuous engineering.

The system is not considered finished merely because an initial version
works.

---

# 150. Maintenance Triggers

Maintenance may be triggered by:

- new research;
- new detector;
- new watermark methodology;
- dependency vulnerability;
- dataset change;
- language performance change;
- operating-system change;
- security incident.

---

# 151. Update Strategy

Updates should prefer:

- isolated changes;
- compatibility testing;
- rollback;
- explicit versioning;
- automatic regression checks.

---

# 152. Obsolete Knowledge

When research disproves a previous assumption, the project should:

1. identify affected components;
2. update the assumption registry;
3. identify affected experiments;
4. update documentation;
5. implement replacement;
6. revalidate.

---

# 153. Scientific Change Propagation

Scientific changes must propagate through:

RESEARCH
→ SPECIFICATION
→ ARCHITECTURE
→ IMPLEMENTATION
→ VALIDATION
→ CERTIFICATION

The development process must not update only the code.

---

# 154. Architecture Change Propagation

Architecture changes must propagate through:

ARCHITECTURE
→ IMPLEMENTATION
→ TESTS
→ SECURITY
→ OPERATIONS
→ DOCUMENTATION

---

# 155. Data Change Propagation

Data changes must propagate through:

DATA
→ CAPABILITY
→ EXPERIMENT
→ VALIDATION
→ CERTIFICATION

---

# 156. Security Change Propagation

Security changes must propagate through:

SECURITY
→ ARCHITECTURE
→ IMPLEMENTATION
→ TESTS
→ OPERATIONS
→ DOCUMENTATION

---

# 157. Validation Change Propagation

Validation criteria changes must propagate through:

VALIDATION
→ TESTS
→ CAPABILITIES
→ CERTIFICATION
→ REPORTING

---

# 158. Development Gate

No major implementation should be considered complete until its relevant
dependency chain has been checked.

---

# 159. Continuous Verification

The project should eventually provide a single command capable of performing
the majority of:

- tests;
- linting;
- type checks;
- security checks;
- documentation checks;
- data manifest checks;
- dependency checks.

---

# 160. Verification Profiles

Verification should support profiles such as:

FAST
FULL
OFFLINE
SECURITY
SCIENTIFIC
RELEASE

---

# 161. Fast Verification

FAST should provide rapid feedback during development.

---

# 162. Full Verification

FULL should run the broad project validation suite.

---

# 163. Offline Verification

OFFLINE must run without network access.

---

# 164. Security Verification

SECURITY should emphasize:

- dependency security;
- network isolation;
- filesystem boundaries;
- unsafe execution;
- data handling.

---

# 165. Scientific Verification

SCIENTIFIC should emphasize:

- benchmark integrity;
- reproducibility;
- language coverage;
- experimental validity;
- result consistency.

---

# 166. Release Verification

RELEASE should combine all relevant checks.

---

# 167. Failure Policy

A failed blocking check prevents release or capability activation.

A non-blocking warning should remain visible.

---

# 168. No Greenwashing

A system must not report "PASS" merely because software execution succeeded.

Scientific and security checks must retain their own status.

---

# 169. Verification Evidence

Important validation should produce machine-readable or otherwise
persistable evidence where practical.

---

# 170. Development Audit Trail

Material development actions should be recoverable from:

- version control;
- decision log;
- change queue;
- experiment metadata;
- release metadata.

---

# 171. Agent Auditability

The project should make it possible to determine what Claude Code changed
during an autonomous batch.

---

# 172. Human Review

Human review should focus on:

- architecture;
- scientific interpretation;
- security boundaries;
- major changes.

It should not be necessary to manually inspect every routine implementation
detail.

---

# 173. Review Efficiency

Review material should be prepared automatically.

A review package should contain:

- summary;
- changed files;
- tests;
- risk classification;
- documentation changes;
- unresolved questions.

---

# 174. Autonomous Maintenance

Routine maintenance may be delegated to Claude Code when:

- the maintenance rule is documented;
- validation is automated;
- rollback is possible;
- no major architectural decision is required.

---

# 175. Scheduled Maintenance

Future automation may periodically inspect:

- dependency updates;
- security advisories;
- obsolete capabilities;
- documentation inconsistencies;
- storage usage;
- broken external resources.

---

# 176. Maintenance Safety

Automated maintenance must not automatically:

- change scientific acceptance criteria;
- delete historical results;
- replace benchmark datasets;
- enable network access;
- remove security controls.

---

# 177. Upgrade Compatibility

Before upgrading a major dependency:

- create a compatibility branch or equivalent;
- run regression tests;
- inspect changed behavior;
- evaluate scientific impact.

---

# 178. Rollback After Failed Update

If an update causes regression:

1. identify affected component;
2. restore previous version;
3. preserve failure evidence;
4. create issue/backlog entry;
5. investigate replacement.

---

# 179. Reproducibility After Maintenance

Routine maintenance should not silently invalidate previous scientific
results.

If behavior changes, the software version must distinguish the new behavior.

---

# 180. Version Identity

A meaningful experiment identity should include at least:

- software version;
- capability versions;
- dataset versions;
- model/resource versions;
- configuration.

---

# 181. Research Reproduction

The development system should make it possible to reconstruct the software
environment required by important historical experiments.

---

# 182. Historical Compatibility

When practical, maintain a compatibility path for historically important
experiments.

---

# 183. Research Preservation

Research code may become obsolete while remaining scientifically valuable.

Historical implementations should be archived rather than casually erased.

---

# 184. Code Archive

Retired implementations should have:

- version;
- reason for retirement;
- replacement;
- compatibility status.

---

# 185. Documentation Archive

Retired capabilities should retain relevant documentation.

---

# 186. Release Notes

Material releases should document:

- new capabilities;
- changed capabilities;
- deprecated capabilities;
- retired capabilities;
- dependency changes;
- validation changes;
- security changes.

---

# 187. Development Quality Gate

A development batch is considered successful only if:

- scope is satisfied;
- tests pass;
- security is preserved;
- documentation is synchronized;
- no blocking inconsistency remains.

---

# 188. Autonomous Quality Gate

Claude Code should run the quality gate before reporting completion.

The agent should not rely on the user to discover routine inconsistencies.

---

# 189. Final Batch State

Each batch should finish in one of:

COMPLETE
COMPLETE_WITH_WARNINGS
BLOCKED
FAILED

---

# 190. Complete

All required checks pass.

---

# 191. Complete With Warnings

Required checks pass, but non-blocking warnings remain documented.

---

# 192. Blocked

A decision or dependency outside the autonomous boundary prevents progress.

---

# 193. Failed

Implementation or validation failed.

Failure evidence must remain available.

---

# 194. Next-Batch Planning

At completion, Claude Code should identify the next logical batch where
useful.

It should not automatically expand scope merely because additional work is
obvious.

---

# 195. Tranche Principle

The project should be developed through a limited number of meaningful
tranches rather than an unlimited sequence of micro-approvals.

A tranche may contain multiple internal autonomous batches.

---

# 196. Tranche Definition

A tranche should have:

- objective;
- expected deliverables;
- allowed scope;
- completion criteria;
- verification profile;
- expected risk.

---

# 197. Tranche Approval

The human operator approves the tranche boundary.

Claude Code may then execute internal batches within that boundary.

---

# 198. Tranche Completion

A tranche ends when:

- all planned deliverables are complete;
- validation passes;
- documentation is synchronized;
- deviations are reported;
- unresolved issues are recorded.

---

# 199. Tranche Deviation

If Claude Code discovers a necessary change outside the approved tranche:

- implement only if it is clearly LOW-risk and within existing architecture;
- otherwise record it and stop at the appropriate boundary.

---

# 200. Tranche Efficiency

The goal is to make each human approval meaningful.

A tranche should contain enough work to justify a review but remain bounded
enough to control risk.

---

# 201. Final Development Principle

The development system must support the following operating model:

HUMAN
defines objectives and approves meaningful boundaries.

CLAUDE CODE
implements, tests, audits and maintains within those boundaries.

AUTOMATED VALIDATION
checks consistency, correctness, security and reproducibility.

DOCUMENTATION
preserves the durable project context.

SCIENTIFIC VALIDATION
determines whether the resulting capability is scientifically supported.

This separation allows the project to evolve rapidly without allowing the
development agent to silently redefine the project itself.