# Operations Map

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Operations architecture and lifecycle map
**Authority:** Operations
**Scope:** Installation, configuration, execution, resources, updates,
monitoring, recovery, maintenance and operational lifecycle

---

# 1. Purpose

This document defines how the software is installed, configured, executed,
updated, monitored and maintained.

The operational architecture must remain distinct from the development
architecture.

Development may use AI-assisted tools.

Normal software execution must not require an AI coding agent.

---

# 2. Operational Principles

The operational system follows these principles:

- local-first execution;
- explicit configuration;
- reproducibility;
- controlled external communication;
- modular components;
- reversible updates;
- explicit capability states;
- observable failures;
- preservation of scientific provenance.

---

# 3. Runtime Independence

The production runtime must be capable of executing without:

- Claude Code;
- ChatGPT;
- an AI coding agent;
- an LLM API;
- a cloud development environment.

AI-assisted development is not a runtime dependency.

---

# 4. Offline-First Principle

The core software should operate offline whenever the required local resources
are available.

Offline execution is the preferred baseline for:

- preprocessing;
- analysis;
- transformation;
- validation;
- local detection;
- local benchmarking;
- reproducibility experiments.

---

# 5. Network Use

Network access must never be assumed.

Any network-dependent functionality must be:

- explicitly identified;
- isolated;
- configurable;
- failure-tolerant;
- documented.

---

# 6. Network Boundary

The runtime should conceptually distinguish:

LOCAL
from
EXTERNAL

A component must not silently cross this boundary.

---

# 7. Optional Cloud Components

Some research or validation components may operate remotely.

Examples may include:

- external detectors;
- external validation services;
- remote research resources.

Such components are optional unless explicitly certified as required.

---

# 8. Cloud Detector Principle

A cloud-based detector may be used as an external validation instrument.

Its use must not silently modify the text being evaluated.

The detector receives an evaluation input and returns an evaluation result.

---

# 9. Evaluation Isolation

External evaluation must not modify:

- source text;
- candidate text;
- preprocessing state;
- benchmark identity.

---

# 10. Detector Result Integrity

A detector result must record:

- detector identity;
- detector version where available;
- timestamp;
- input identity;
- request configuration where relevant;
- returned result;
- availability status.

---

# 11. Detector Unavailability

If an external detector is unavailable, the software must not fabricate a
result.

The result must be represented as:

UNAVAILABLE

or another explicit non-success state.

---

# 12. Detector Changes

External detectors may change without notice.

The system must therefore distinguish:

- detector identity;
- detector version if known;
- date of evaluation.

Historical results must not be interpreted as necessarily equivalent to
future results from the same service.

---

# 13. Detector Adapter Architecture

External detectors should be accessed through adapters.

The core system should not contain detector-specific logic throughout the
pipeline.

---

# 14. Adding a Detector

A new detector should require:

- adapter;
- input/output contract;
- test fixture;
- provenance metadata;
- availability handling;
- documentation.

---

# 15. Removing a Detector

Removing a detector must not require rewriting unrelated components.

Its historical results should remain preserved.

---

# 16. Local Resources

Local resources may include:

- datasets;
- linguistic resources;
- model files;
- tokenizers;
- dictionaries;
- benchmark corpora;
- configuration;
- cached research artifacts.

---

# 17. Resource Registry

Every material resource should have a registry entry containing:

- resource ID;
- type;
- version;
- source;
- license;
- size;
- checksum where practical;
- purpose;
- dependencies.

---

# 18. Storage Constraint

The project should be designed to operate within an approximately
30 GB local storage budget unless a later decision explicitly changes this
constraint.

The storage budget includes project-controlled research resources.

---

# 19. Resource Prioritization

When storage is constrained, prioritize:

1. resources required for runtime;
2. validation datasets;
3. scientifically important reference datasets;
4. active model/resource versions;
5. reproducibility artifacts;
6. optional historical resources.

---

# 20. Resource Deduplication

Identical resources should not be stored multiple times unnecessarily.

Content-addressed or checksum-based storage may be used where useful.

---

# 21. Large Resources

Large datasets or models should be handled separately from source code where
practical.

Git repositories should not be burdened with large binary resources unless
there is a clear justification.

---

# 22. GitHub and External Storage

External repositories or release storage may be used for:

- source code;
- documentation;
- manifests;
- small fixtures;
- reproducibility metadata.

Large resources may instead be downloaded or stored through a documented
resource mechanism.

---

# 23. Resource Reproducibility

A resource referenced by an experiment should be identifiable even if the
resource itself is not stored inside the repository.

---

# 24. Resource Checksums

Checksums should be used for important downloadable resources.

This protects against accidental corruption or silent replacement.

---

# 25. Resource Download

Downloads must be explicit.

The runtime must not silently download arbitrary resources merely because a
file is missing.

---

# 26. First-Run Behavior

First-run setup should clearly identify:

- required resources;
- optional resources;
- expected storage;
- network requirements;
- installation time.

---

# 27. Installation Modes

The project should support conceptually:

OFFLINE INSTALL
ONLINE RESOURCE SETUP
DEVELOPMENT INSTALL
VALIDATION INSTALL

The exact implementation is defined elsewhere.

---

# 28. Offline Installation

Offline installation should work when all required packages and resources are
already available locally.

---

# 29. Online Resource Setup

Online setup may retrieve declared resources.

It must not retrieve arbitrary dependencies without explicit documentation.

---

# 30. Dependency Locking

Runtime dependencies should be version-pinned or otherwise reproducibly
resolved.

---

# 31. Environment Capture

The operational environment should identify:

- operating system;
- runtime version;
- package versions;
- relevant hardware;
- configuration profile.

---

# 32. Configuration Profiles

The system should support profiles such as:

DEFAULT
OFFLINE
RESEARCH
VALIDATION
DEVELOPMENT
RELEASE

Only profiles relevant to the actual implementation need to exist.

---

# 33. Configuration Validation

Configuration should be validated before processing begins.

Invalid configuration must fail clearly.

---

# 34. Safe Defaults

Default configuration must prioritize:

- data integrity;
- reproducibility;
- privacy;
- explicit failure;
- minimal external communication.

---

# 35. No Hidden Configuration

Behavior must not depend on undocumented local environment variables,
developer-specific files or hidden settings.

---

# 36. Input Handling

The runtime should treat user input as untrusted data.

Input validation should occur before processing.

---

# 37. Text Input

Text input should preserve:

- Unicode;
- language-relevant characters;
- line structure where relevant;
- encoding;
- meaningful whitespace where required.

---

# 38. Input Provenance

For experiments, the system should be able to associate an input with an
experiment identifier without necessarily storing sensitive content.

---

# 39. Sensitive Content

The runtime should avoid transmitting input externally unless the user has
explicitly enabled the relevant external functionality.

---

# 40. External Transmission

Any component transmitting text externally must make that behavior explicit.

---

# 41. Cloud Privacy Boundary

Cloud evaluation should be treated as a separate privacy boundary.

Users should know when their text leaves the local environment.

---

# 42. Cloud Failure

If cloud evaluation fails, the local processing pipeline should remain
usable unless the external evaluation is explicitly required for the selected
workflow.

---

# 43. Processing Pipeline

The runtime should conceptually follow:

INPUT
→ VALIDATION
→ ANALYSIS
→ PROCESSING
→ OUTPUT VALIDATION
→ RESULT

Optional external evaluation should remain an isolated branch.

---

# 44. No Silent Mutation

Operational infrastructure must not silently mutate the input or output.

---

# 45. Output Integrity

The output should retain its declared provenance.

The runtime should record which processing components were applied.

---

# 46. Output Status

Each processing operation should produce an explicit status.

Suggested states:

SUCCESS
PARTIAL
FAILED
INVALID_INPUT
UNSUPPORTED
UNAVAILABLE

---

# 47. Unsupported Language

If the selected capability does not support the input language adequately,
the runtime should report an explicit unsupported or degraded status.

---

# 48. Language Detection

If automatic language detection is used, its result should be considered a
classification signal rather than unquestionable truth.

Where ambiguity is important, the runtime should expose it.

---

# 49. Manual Language Selection

The user should be able to explicitly specify a language where supported.

---

# 50. Language Profiles

Language-specific resources and capabilities should be represented through
versioned profiles.

---

# 51. Capability Registry

Runtime capability availability should come from a registry rather than
hard-coded assumptions.

Each capability should expose:

- ID;
- version;
- status;
- dependencies;
- supported languages;
- resource requirements.

---

# 52. Capability States

Supported states include:

ACTIVE
EXPERIMENTAL
DEGRADED
DISABLED
DEPRECATED
RETIRED
UNAVAILABLE

---

# 53. Active Capability

An ACTIVE capability may be used by normal workflows.

---

# 54. Experimental Capability

An EXPERIMENTAL capability may require explicit research configuration.

It must not silently replace an active certified component.

---

# 55. Degraded Capability

A DEGRADED capability may operate with known limitations.

Those limitations must be visible to the caller.

---

# 56. Disabled Capability

A DISABLED capability is installed but intentionally unavailable.

---

# 57. Deprecated Capability

A DEPRECATED capability remains available for compatibility or research but
should not normally be selected for new workflows.

---

# 58. Retired Capability

A RETIRED capability is no longer executable in the normal runtime.

Historical artifacts may still reference it.

---

# 59. Unavailable Capability

An UNAVAILABLE capability cannot currently run because a dependency or
resource is missing.

---

# 60. Capability Selection

Where multiple implementations exist, selection should be explicit and
traceable.

---

# 61. Capability Versioning

Changing a capability in a way that can affect scientific output requires a
new capability version or equivalent identity.

---

# 62. Runtime Provenance

A result should be traceable to:

- software version;
- capability versions;
- resource versions;
- configuration;
- optional external evaluations.

---

# 63. Experiment Identity

Important research executions should receive an experiment identifier.

---

# 64. Experiment Manifest

An experiment manifest should contain, where relevant:

- experiment ID;
- timestamp;
- software revision;
- capability versions;
- datasets;
- models/resources;
- configuration;
- input identifier;
- output identifier;
- validation status.

---

# 65. Reproducibility

A future user should be able to reconstruct the environment of an important
experiment from its manifest and referenced resources.

---

# 66. Randomness

Stochastic processing should record:

- random seed;
- relevant generation parameters;
- stochastic component version.

---

# 67. Deterministic Mode

Where technically feasible, provide a deterministic mode for validation and
reproducibility.

---

# 68. Runtime Logging

Logs should be useful for diagnostics without unnecessarily exposing text
content.

---

# 69. Privacy-Preserving Logging

By default, logs should prefer:

- identifiers;
- hashes;
- metadata;
- status;

rather than complete user documents.

---

# 70. Debug Logging

Detailed content logging should require explicit debug configuration.

---

# 71. Log Levels

Suggested levels:

ERROR
WARN
INFO
DEBUG
TRACE

Only levels necessary for the implementation need to be exposed.

---

# 72. Error Reporting

Operational errors should state:

- what failed;
- where it failed;
- why it failed where known;
- whether output is trustworthy;
- whether retry is appropriate.

---

# 73. Retry Policy

Retries should only be automatic when failure is plausibly transient.

Examples:

- temporary network failure;
- transient external service error.

Do not repeatedly retry deterministic failures.

---

# 74. Retry Limits

Automatic retries must be bounded.

---

# 75. External Service Timeouts

Cloud services must have explicit timeouts.

---

# 76. External Service Rate Limits

Adapters should respect declared rate limits.

---

# 77. External Service Costs

The project's operational design assumes zero-cost external services where
possible.

Any service that introduces mandatory monetary cost must be explicitly
identified before becoming a required dependency.

---

# 78. Free-Tier Assumption

Free external services may change their policies.

The runtime must not assume that a free service will remain free forever.

---

# 79. Service Replacement

External service dependencies must be replaceable through adapters.

---

# 80. No Vendor Lock-In

The core architecture should not depend on one detector or one external
provider.

---

# 81. External Provider Registry

External services should be registered with:

- provider;
- service;
- purpose;
- endpoint;
- version where applicable;
- data transmitted;
- cost status;
- fallback;
- dependency status.

---

# 82. Provider Failure

A provider failure should not silently change the scientific interpretation
of an experiment.

---

# 83. Provider Version Drift

If an external provider changes behavior, future results should be
distinguished from historical results where possible.

---

# 84. Operational Updates

Updates may affect:

- code;
- dependencies;
- models;
- datasets;
- language resources;
- external service adapters.

Each class requires appropriate validation.

---

# 85. Update Classes

Classify updates as:

PATCH
MINOR
MAJOR
RESOURCE
SCIENTIFIC
SECURITY

---

# 86. Patch Update

A patch should normally preserve expected behavior.

---

# 87. Minor Update

A minor update may add functionality without intentionally breaking existing
interfaces.

---

# 88. Major Update

A major update may change interfaces or scientific behavior.

---

# 89. Resource Update

A resource update changes a dataset, model, dictionary or similar artifact.

---

# 90. Scientific Update

A scientific update changes an algorithm, methodology or interpretation.

---

# 91. Security Update

A security update addresses a vulnerability or security boundary.

---

# 92. Update Preconditions

Before a significant update:

- verify backup/recovery;
- record current version;
- run baseline tests;
- identify affected capabilities.

---

# 93. Update Validation

After updating:

- run regression tests;
- run relevant scientific validation;
- inspect resource integrity;
- inspect documentation;
- inspect security impact.

---

# 94. Update Rollback

Every material update should have a rollback strategy.

---

# 95. Rollback Principle

If an update causes unacceptable regression, restore the last known valid
configuration rather than improvising a partial rollback.

---

# 96. Database and State Migration

If persistent state is introduced, migrations must be:

- versioned;
- reversible where practical;
- tested;
- documented.

---

# 97. No Destructive Update

Updates must not silently destroy historical experiment metadata.

---

# 98. Historical Results

Historical results should retain their original software/resource identity.

---

# 99. Re-evaluation

When a new capability becomes available, historical inputs may be
re-evaluated as new experiments.

The original result must not be overwritten.

---

# 100. Result Comparison

Comparisons between versions should identify all meaningful environmental
differences.

---

# 101. Operational Validation

Operational validation should verify:

- installation;
- startup;
- input processing;
- output generation;
- resource loading;
- failure handling;
- offline behavior;
- external adapter behavior where applicable.

---

# 102. Health Check

The runtime should eventually provide a health-check capability.

A health check should distinguish:

READY
DEGRADED
MISSING_RESOURCE
MISCONFIGURED
UNAVAILABLE

---

# 103. Resource Health

Health checks should verify the presence and integrity of required local
resources.

---

# 104. Dependency Health

Health checks should detect missing or incompatible runtime dependencies.

---

# 105. External Health

External services should be checked only when their use is relevant.

The application should not require continuous connectivity merely to start.

---

# 106. Startup Failure

Startup should fail clearly when mandatory configuration or resources are
missing.

---

# 107. Partial Availability

If optional resources are missing, the system may start in DEGRADED mode.

The unavailable capabilities must be clearly reported.

---

# 108. No False Readiness

The system must not report READY if a required capability is unavailable.

---

# 109. Resource Installation

Resource installation should be repeatable and idempotent where practical.

---

# 110. Resource Cleanup

Unused resources may be removed only when their scientific or operational
importance has been evaluated.

---

# 111. Storage Monitoring

The project should monitor storage usage of:

- datasets;
- models;
- caches;
- logs;
- experiment artifacts.

---

# 112. Cache Policy

Caches should be distinguishable from authoritative resources.

Caches may be deleted and regenerated where practical.

---

# 113. Cache Integrity

Corrupt caches must not be treated as authoritative.

---

# 114. Cache Rebuild

The runtime should be able to rebuild disposable caches.

---

# 115. Backup

Important:

- configuration;
- manifests;
- experiment metadata;
- validation evidence;

should be backed up or reproducibly reconstructable.

---

# 116. Backup Scope

Backups should prioritize metadata and scientifically important artifacts
rather than indiscriminately copying all temporary data.

---

# 117. Recovery

Recovery procedures should identify:

- required files;
- required resources;
- installation steps;
- validation steps.

---

# 118. Disaster Recovery

The project should eventually document recovery from:

- corrupted installation;
- deleted cache;
- missing resource;
- dependency failure;
- broken update.

---

# 119. Recovery Validation

After recovery, run the relevant verification profile.

---

# 120. Operational Security

Operations must preserve the security constraints defined in the security
documentation.

---

# 121. Least Privilege

The runtime should operate with the minimum filesystem and network
permissions required.

---

# 122. Filesystem Scope

The software should not require unrestricted access to the user's filesystem
unless explicitly justified.

---

# 123. Network Scope

The software should not require unrestricted network access.

---

# 124. Subprocesses

Subprocess execution should be minimized and explicitly controlled.

---

# 125. Executable Resources

Downloaded executable content should not be executed automatically without
validation.

---

# 126. Resource Provenance

Externally obtained resources should have identifiable provenance.

---

# 127. Integrity Verification

Where practical, verify downloaded artifacts using:

- checksums;
- signatures;
- trusted release metadata.

---

# 128. Configuration Secrets

Secrets should never be stored in source code.

---

# 129. Credential Isolation

Credentials required for optional external services should remain separate
from ordinary configuration.

---

# 130. Credential Failure

Missing credentials should produce a clear unavailable state rather than
silently falling back to insecure behavior.

---

# 131. No Credential Leakage

Credentials must not appear in:

- logs;
- experiment manifests;
- error messages;
- source control.

---

# 132. Data Retention

The runtime should retain only the information required for:

- execution;
- reproducibility;
- validation;
- diagnostics.

---

# 133. Temporary Data

Temporary files should be deleted or made disposable after use when practical.

---

# 134. Cloud Data Retention

If an external service retains submitted text, that behavior must be
documented.

---

# 135. User Consent Boundary

External transmission of user-provided text should be an explicit operational
choice.

---

# 136. Operational Modes

The software should conceptually support:

LOCAL_ONLY
LOCAL_WITH_EXTERNAL_VALIDATION
RESEARCH
DIAGNOSTIC

The exact names may change during implementation.

**Cross-reference:** `docs/06-security/SECURITY-MAP.md` § 14 "Network
Modes" defines a related but non-identical enumeration (`OFFLINE,
LOCAL_ONLY, EXTERNAL_ANALYSIS_ALLOWED, RESEARCH_NETWORK_MODE`) for what
appears to be the same underlying concept. Only `LOCAL_ONLY` is shared
verbatim between the two lists. Neither has been reconciled with the
other; which one is authoritative (or whether the security-boundary and
operations-boundary concepts are genuinely distinct) is a HUMAN DECISION
REQUIRED item — see `docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`,
SECOND PASS, §5S/§13S. Added 2026-08-29.

---

# 137. LOCAL_ONLY

No external text transmission.

---

# 138. LOCAL_WITH_EXTERNAL_VALIDATION

Local processing remains primary while explicitly enabled external evaluation
is available.

---

# 139. RESEARCH

May expose experimental capabilities and additional diagnostics.

Research results must remain clearly distinguished from certified results.

---

# 140. DIAGNOSTIC

Provides additional diagnostic information for troubleshooting.

It should not silently alter scientific processing.

---

# 141. Production Safety

Experimental or diagnostic modes must not accidentally become the default
production mode.

---

# 142. Configuration Migration

When configuration format changes:

- detect old versions;
- migrate safely where possible;
- preserve user intent;
- validate the result.

---

# 143. Configuration Versioning

Configuration schemas should be versioned when material changes occur.

---

# 144. Operational Documentation

Operational procedures must be documented sufficiently for another person or
agent to reproduce them.

---

# 145. Installation Documentation

Installation documentation must identify:

- prerequisites;
- installation;
- resources;
- validation;
- troubleshooting.

---

# 146. Runtime Documentation

Runtime documentation must identify:

- input;
- output;
- configuration;
- supported modes;
- limitations.

---

# 147. Troubleshooting

Troubleshooting should be organized around observable symptoms rather than
implementation internals alone.

---

# 148. Incident Classification

Operational incidents should be classified as:

INFO
MINOR
MAJOR
CRITICAL

---

# 149. Incident Evidence

Preserve enough evidence to reproduce or diagnose significant incidents.

---

# 150. Incident Recovery

After an incident:

1. restore safe operation;
2. preserve evidence;
3. identify cause;
4. assess scientific impact;
5. document corrective action.

---

# 151. Scientific Incident

An operational failure that may alter scientific results must be treated as
a scientific incident as well as a technical incident.

---

# 152. Result Invalidation

If an operational problem could have corrupted results, those results should
be marked as potentially invalid rather than silently retained as valid.

---

# 153. Operational Change Control

Material operational changes should be recorded in the decision log or
appropriate change documentation.

---

# 154. Maintenance Windows

Planned maintenance should be performed in a way that minimizes disruption
to active research.

---

# 155. Maintenance Verification

After maintenance:

- run health checks;
- run relevant tests;
- verify resources;
- verify representative execution.

---

# 156. Capability Retirement Operations

Retiring a capability requires:

- disablement;
- migration plan where needed;
- historical compatibility decision;
- documentation update;
- cleanup of obsolete dependencies.

---

# 157. Obsolete Resource Cleanup

A resource may be removed only after confirming:

- no active capability requires it;
- no reproducibility requirement depends on it;
- historical metadata remains sufficient.

---

# 158. Obsolete External Service

If an external service disappears:

- mark it unavailable;
- preserve historical results;
- identify replacement;
- validate replacement independently.

---

# 159. New Detector Operations

Adding a new detector should not alter existing local processing.

It should enter as an independent operational capability.

---

# 160. Detector Retirement

Detector retirement should preserve historical detector metadata.

---

# 161. Operational Version Matrix

The project should eventually maintain a matrix covering:

- software version;
- capability version;
- resource version;
- detector version;
- validation status.

---

# 162. Compatibility Matrix

Where multiple combinations are supported, compatibility should be explicit.

---

# 163. Unsupported Combinations

Unsupported combinations must fail clearly.

---

# 164. No Silent Fallback

The runtime should not silently substitute a different algorithm, model,
language resource or detector merely because the requested one is
unavailable.

Any fallback must be explicit.

---

# 165. Controlled Fallback

Where a fallback is scientifically acceptable, it must be:

- declared;
- versioned;
- logged;
- represented in experiment metadata.

---

# 166. Operational Reproducibility

A reproducible operation requires knowledge of:

- software;
- configuration;
- resources;
- capabilities;
- external services.

---

# 167. External Reproducibility Limitation

Results depending on an external service may not be perfectly reproducible if
the provider changes its system.

The system must record this limitation rather than conceal it.

---

# 168. Research Snapshot

Important experiments should be capable of producing a snapshot containing
the metadata necessary for future interpretation.

---

# 169. Snapshot Integrity

Snapshots should identify their source versions and checksums where practical.

---

# 170. Runtime Upgrade Principle

The system should evolve incrementally.

Avoid upgrades that simultaneously change:

- operating environment;
- core algorithms;
- datasets;
- external detectors;

unless the change itself is the subject of an explicit experiment.

---

# 171. Controlled Change

Changes should be isolated where possible so that regressions can be
attributed.

---

# 172. Experimental Comparison

When testing a new implementation operationally, preserve the previous
configuration as a baseline.

---

# 173. Baseline

A baseline is a known valid configuration against which a candidate is
compared.

---

# 174. Candidate

A candidate is a new implementation or configuration not yet certified.

---

# 175. Promotion

A candidate may be promoted only after passing relevant validation.

---

# 176. Demotion

An active capability may be demoted when new evidence shows unacceptable
behavior.

---

# 177. Emergency Disablement

A capability with a critical defect must be disableable without removing the
entire software installation.

---

# 178. Emergency Rollback

The system should allow restoration of the last known valid capability
configuration.

---

# 179. Maintenance Autonomy

Routine maintenance may be performed by Claude Code under the development
rules.

Operational changes affecting runtime security or scientific validity remain
subject to the defined approval boundary.

---

# 180. Operational Agent Boundary

Claude Code may inspect and modify operational configuration within its
approved development scope.

It must not silently:

- expose user data;
- enable unrestricted networking;
- delete historical evidence;
- weaken security controls.

---

# 181. Automated Operational Checks

The project should eventually automate checks for:

- missing resources;
- broken manifests;
- incompatible dependencies;
- stale configuration;
- invalid capability states;
- documentation inconsistencies.

---

# 182. Operational Audit

An operational audit should produce:

PASS
WARNING
BLOCKING

results.

---

# 183. Operational Readiness

A release is operationally ready when:

- installation works;
- required resources are available;
- health checks pass;
- core execution works;
- failure behavior is understood;
- relevant validation passes.

**Cross-reference:** three other release-readiness checklists exist
elsewhere in the corpus, none cross-referenced with this one:
`docs/07-data/DATA-MAP.md` § 117 "Data Quality Gate for Release",
`docs/08-development/DEVELOPMENT-MAP.md` § 108 "Release Candidate", and
`docs/10-certification/CERTIFICATION-MAP.md` § 149 "Combined Release
Eligibility". Whether these should be consolidated or remain separate,
area-specific checklists is a REVIEW REQUIRED item — see
`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §4S/§12S.
Added 2026-08-29.

---

# 184. Scientific Readiness

Operational readiness does not imply scientific certification.

These are separate states.

---

# 185. Certification Boundary

Only the certification process can declare a capability scientifically
certified.

---

# 186. Runtime Transparency

The software should make clear:

- what it executed;
- which capabilities were used;
- which resources were used;
- which external services were contacted;
- what was unavailable.

---

# 187. User-Facing Status

Important limitations should be visible without requiring inspection of
debug logs.

---

# 188. No Misleading Success

A technically completed operation must not be represented as scientifically
successful when validation was unavailable or failed.

---

# 189. Operational State Machine

The overall runtime may conceptually transition through:

INITIALIZING
→ VALIDATING
→ READY
→ PROCESSING
→ VALIDATING_OUTPUT
→ COMPLETE

Failure states may branch to:

FAILED
DEGRADED
UNAVAILABLE

---

# 190. Initialization

Initialization verifies configuration and resources.

---

# 191. Validation

Validation verifies that required runtime prerequisites are satisfied.

---

# 192. Processing

Processing executes the selected capability chain.

---

# 193. Output Validation

Output validation verifies structural and declared operational constraints.

---

# 194. Completion

Completion records the relevant provenance and status.

---

# 195. Failure Recovery

Recoverable failures should return to a safe state.

---

# 196. Persistent Failure

Persistent failures should remain explicit until resolved.

---

# 197. Operational Logs and Research Evidence

Operational logs and scientific evidence are distinct.

A log saying that a program completed does not constitute evidence that a
scientific hypothesis was validated.

---

# 198. Monitoring

Monitoring should prioritize meaningful changes:

- capability failures;
- resource failures;
- detector availability;
- dependency problems;
- storage exhaustion;
- repeated validation failures.

---

# 199. Alerting

Alerts should avoid excessive noise.

Only actionable conditions should generate high-priority alerts.

---

# 200. Operational Cost

The design should minimize recurring operational cost.

The baseline target is:

NO MANDATORY PAID SERVICE

unless explicitly approved in a future decision.

---

# 201. External Service Substitution

If a free external service becomes paid or unavailable, the system should
support:

- replacement;
- local alternative;
- degraded operation;
- disabled capability.

---

# 202. No Permanent External Dependency

The core scientific workflow should not become permanently dependent on a
single external commercial service unless explicitly decided.

---

# 203. Future-Proof Operations

The operational design must tolerate:

- new detectors;
- new research methods;
- new languages;
- new datasets;
- new models;
- provider changes;
- obsolete components.

---

# 204. Update Discovery

Future maintenance may periodically discover:

- new scientific literature;
- new detector methodologies;
- new watermark methodologies;
- new language resources;
- new vulnerabilities.

These discoveries should enter the appropriate research or maintenance
workflow.

---

# 205. Research-to-Operations Transition

A research capability should move toward operational use only after:

- reproducible implementation;
- adequate testing;
- resource definition;
- operational documentation;
- scientific validation.

---

# 206. Operations-to-Research Feedback

Operational failures and real-world observations may generate new research
questions.

These should enter the research registry or knowledge backlog.

---

# 207. Continuous Evolution

The operational system is designed as a living system.

Its capabilities may change over time while historical results remain
traceable.

---

# 208. Final Operational Principle

The software must remain:

LOCAL-FIRST
REPRODUCIBLE
MODULAR
OBSERVABLE
REVERSIBLE
UPDATABLE
SCIENTIFICALLY TRACEABLE

while keeping external services optional and explicitly bounded.

Operational success must never be confused with scientific success.