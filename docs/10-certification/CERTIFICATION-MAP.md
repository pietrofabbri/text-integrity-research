# Certification Map

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Scientific and operational certification framework
**Authority:** Certification
**Scope:** Evidence, validation, certification, recertification,
deprecation, reproducibility and release eligibility

---

# 1. Purpose

This document defines how the project determines whether a software
capability is sufficiently validated for a defined purpose.

The project explicitly separates:

- technical correctness;
- operational readiness;
- experimental validity;
- scientific validity;
- certification.

A capability may satisfy one level without satisfying the others.

---

# 2. Fundamental Principle

"Software execution succeeded" does not mean:

"the scientific objective has been demonstrated."

Certification is therefore an evidence-based process.

---

# 3. Certification Levels

The project should distinguish at least:

UNTESTED
EXPERIMENTAL
VALIDATED
CERTIFIED
DEPRECATED
RETIRED

---

# 4. UNTESTED

The capability exists but has not yet undergone meaningful validation.

It must not be represented as scientifically validated.

---

# 5. EXPERIMENTAL

The capability has undergone preliminary testing but evidence remains
insufficient for certification.

Experimental results are research results.

---

# 6. VALIDATED

The capability satisfies the predefined technical and scientific validation
criteria for a defined scope.

Validation does not imply universal validity.

---

# 7. CERTIFIED

A capability is CERTIFIED only when the project has sufficient evidence that
it satisfies its declared acceptance criteria for a clearly defined scope.

---

# 8. DEPRECATED

A previously active capability should become DEPRECATED when:

- superior methodology exists;
- scientific evidence has changed;
- maintenance is no longer justified;
- compatibility is problematic;
- security concerns exist;
- validation criteria have materially changed.

---

# 9. RETIRED

A capability is RETIRED when it is no longer used for normal execution.

Historical evidence may continue to reference it.

---

# 10. Certification Scope

Certification must always specify scope.

Scope may include:

- language;
- text type;
- input conditions;
- resource versions;
- capability version;
- detector set;
- validation environment;
- operational mode.

---

# 11. No Universal Certification

A capability certified for one scope is not automatically certified for all
languages, document types, datasets or environments.

---

# 12. Language Certification

Multilingual capabilities must be evaluated by language.

A system may be certified for one language while remaining experimental or
unsupported for another.

---

# 13. Language Families

Where scientifically justified, related languages may be grouped for
experimentation.

However, family-level evidence must not automatically replace language-level
evidence.

---

# 14. Language Expansion

Adding a new language requires new evidence.

Existing certification does not automatically transfer.

---

# 15. Language Regression

If a new update degrades a previously certified language, the affected
certification must be reviewed.

---

# 16. Certification Object

The fundamental certification object is:

CAPABILITY
+ VERSION
+ SCOPE
+ EVIDENCE
+ VALIDATION CRITERIA
+ ENVIRONMENT

---

# 17. Evidence

Certification evidence may include:

- scientific literature;
- controlled experiments;
- benchmark results;
- independent replication;
- regression tests;
- robustness analysis;
- adversarial evaluation;
- detector evaluation;
- reproducibility evidence.

---

# 18. Evidence Hierarchy

Evidence should be classified by strength.

Suggested hierarchy:

E0 — no evidence
E1 — implementation evidence
E2 — controlled internal experiment
E3 — benchmark evidence
E4 — independent or external evidence
E5 — replicated evidence across relevant conditions

The exact hierarchy may evolve.

---

# 19. Literature Evidence

Scientific literature should inform:

- hypotheses;
- methodology;
- validation criteria;
- limitations;
- future research.

Literature should not automatically be treated as proof that a particular
implementation works.

---

# 20. Literature Registry

Relevant scientific sources must be registered in:

docs/00-project/RESEARCH-REGISTRY.md

---

# 21. Evidence Provenance

Every important certification claim should identify its evidence source.

---

# 22. Evidence Versioning

Evidence should be associated with:

- source;
- date;
- experiment version;
- software version;
- relevant resources.

---

# 23. Evidence Expiration

Scientific evidence may become obsolete.

Certification must therefore be considered temporally bounded.

---

# 24. Certification Date

Every certification should record the date on which it was granted.

---

# 25. Certification Review Date

Where appropriate, certification should specify a review trigger or review
interval.

A fixed calendar interval is not mandatory if scientific-change triggers are
more appropriate.

---

# 26. Recertification

Recertification is required when evidence changes materially.

Possible triggers include:

- new detector methodologies;
- new watermark methodologies;
- new scientific findings;
- new benchmark results;
- significant algorithm changes;
- significant model changes;
- major dataset changes;
- language-resource changes.

---

# 27. Scientific Change Trigger

A new scientific result that challenges a core assumption should trigger an
impact assessment.

---

# 28. Detector Change Trigger

A new detection methodology may invalidate assumptions about the performance
of a capability.

The project must therefore be able to add new detector evaluations without
rewriting the certification system.

---

# 29. Watermark Research Trigger

New watermark research may require new experiments.

The existence of a new watermark methodology does not automatically imply
that existing conclusions are invalid, but it must trigger evaluation when
relevant.

---

# 30. AI-Detection Research Trigger

New AI-detection methodologies may similarly trigger new validation
experiments.

---

# 31. No Fixed Definition of "Effective"

Scientific effectiveness must remain an evolving concept.

The project should not encode one immutable detector, metric or benchmark as
the permanent definition of success.

---

# 32. Evaluation Portfolio

Certification should rely on a portfolio of relevant evaluations rather
than one single external test.

---

# 33. External Detector Principle

An external detector can provide evidence.

It should not automatically define scientific truth.

---

# 34. Detector Independence

Where possible, evaluations should use multiple independent detection
approaches.

---

# 35. Detector Diversity

The evaluation portfolio should seek methodological diversity rather than
simply collecting many implementations of the same underlying technique.

---

# 36. Detector Versioning

Each external detector evaluation should record:

- detector identity;
- version where available;
- date;
- configuration;
- input identity;
- result.

---

# 37. Detector Availability

An unavailable detector cannot produce evidence.

The project must not convert absence of evidence into a successful result.

---

# 38. Detector Contradiction

If different detectors produce contradictory results, the result should be
represented as contradictory or uncertain.

The system must not select the favorable result merely because it is
convenient.

---

# 39. Evaluation Independence

The system should distinguish:

- development data;
- tuning data;
- validation data;
- holdout data.

---

# 40. Holdout Protection

Holdout datasets should not be used repeatedly for optimization.

Repeated use can invalidate their status as independent evaluation data.

---

# 41. Benchmark Versioning

Benchmarks must be versioned.

Changing benchmark contents creates a new benchmark version.

---

# 42. Benchmark Integrity

Benchmark data must not be silently altered to improve apparent performance.

---

# 43. Benchmark Provenance

Each benchmark should identify:

- source;
- version;
- license;
- language;
- document types;
- intended purpose.

---

# 44. Reproducibility

A certification claim should be reproducible to the extent technically
possible.

---

# 45. Reproducibility Levels

Suggested levels:

R0 — not reproducible
R1 — reproducible internally
R2 — reproducible from repository and declared resources
R3 — independently reproducible

---

# 46. Environment Reproduction

Important experiments should record:

- software version;
- dependency versions;
- model versions;
- dataset versions;
- configuration;
- random seeds where relevant.

---

# 47. Scientific Reproduction

Reproducing the software execution does not necessarily reproduce a
scientific conclusion.

The scientific interpretation must also be documented.

---

# 48. Statistical Evidence

Where statistical methods are applicable, certification should use
appropriate statistical analysis.

The exact statistical method depends on the experiment.

---

# 49. Confidence

Results should distinguish:

- point estimate;
- uncertainty;
- confidence interval where applicable;
- sample size;
- experimental conditions.

---

# 50. Effect Size

Where applicable, report effect size rather than relying only on statistical
significance.

---

# 51. Multiple Comparisons

Where many evaluations are performed, appropriate consideration should be
given to multiple-comparison effects.

---

# 52. Dataset Diversity

Certification should consider diversity of:

- languages;
- authors;
- domains;
- document lengths;
- genres;
- formatting;
- writing styles.

---

# 53. Distribution Shift

Performance measured on one distribution must not automatically be assumed
to transfer to another.

---

# 54. Robustness

Validation should examine robustness where relevant.

Potential dimensions include:

- text length;
- formatting;
- language;
- domain;
- writing style;
- encoding;
- controlled perturbations.

---

# 55. Boundary Conditions

Every certified capability should document known boundary conditions.

---

# 56. Failure Conditions

Certification should identify situations in which the capability should
return:

- unsupported;
- degraded;
- uncertain;
- unavailable;
- failed.

---

# 57. No Forced Success

The system must not be designed to always produce a positive or successful
classification merely because a user requested one.

---

# 58. Scientific Honesty

Certification documentation must distinguish:

OBSERVED
from
INFERRED
from
HYPOTHESIZED

---

# 59. Negative Results

Negative results are valid scientific evidence.

They should be preserved.

---

# 60. Failed Experiments

Failed experiments should not be deleted merely because they are
unfavorable.

They may provide important evidence for future methodology.

---

# 61. Regression Evidence

When a new version performs worse than an established baseline, the
regression should be recorded.

---

# 62. Baseline

Every major certification experiment should have a clearly identified
baseline where meaningful.

---

# 63. Candidate

The candidate is the implementation being evaluated.

---

# 64. Comparative Evaluation

Candidate and baseline should use identical evaluation conditions wherever
the experiment requires direct comparison.

---

# 65. Ablation

Where useful, ablation studies should determine which components contribute
to observed effects.

---

# 66. Component Attribution

Certification should avoid attributing an effect to a component without
adequate evidence.

---

# 67. Confounding

Experiments should identify plausible confounding factors.

---

# 68. Control Conditions

Where possible, include control conditions.

---

# 69. Experimental Isolation

Changes should be isolated sufficiently to determine what caused observed
effects.

---

# 70. Version Isolation

A result should identify all relevant version changes.

---

# 71. Certification Package

A certification package should contain:

- capability identity;
- version;
- scope;
- acceptance criteria;
- experiment definitions;
- datasets;
- resource versions;
- detector/evaluation portfolio;
- results;
- limitations;
- reproducibility information;
- decision.

---

# 72. Acceptance Criteria

Acceptance criteria must be defined before interpreting final results where
practical.

---

# 73. Pre-Registration Principle

For important experiments, define:

- hypothesis;
- methodology;
- primary metrics;
- acceptance criteria;

before inspecting final results where practical.

---

# 74. Avoiding Post-Hoc Criteria

Changing the acceptance criteria after observing results must be explicitly
identified.

---

# 75. Exploratory Research

Exploratory analysis is permitted.

Exploratory findings should be clearly distinguished from confirmatory
validation.

---

# 76. Confirmatory Validation

Confirmatory validation should use predefined criteria wherever practical.

---

# 77. Certification Decision

A certification decision should be:

CERTIFIED
NOT CERTIFIED
CONDITIONALLY CERTIFIED
REQUIRES REVIEW

---

# 78. Certified

All mandatory criteria are satisfied for the defined scope.

---

# 79. Not Certified

Evidence is insufficient or one or more mandatory criteria fail.

---

# 80. Conditionally Certified

The capability is acceptable under explicitly documented restrictions.

---

# 81. Requires Review

Existing certification may no longer be assumed valid because new evidence or
changes require reassessment.

---

# 82. Conditional Certification

Conditions must be explicit.

Examples:

- specific language;
- specific resource version;
- restricted text domain;
- specific operational mode;
- restricted evaluation scope.

---

# 83. Certification Revocation

Certification may be revoked when:

- critical evidence invalidates it;
- implementation changes materially;
- security issues compromise validity;
- benchmark contamination is discovered;
- reproducibility failure is significant;
- relevant scientific assumptions fail.

---

# 84. Partial Revocation

Where possible, revoke only the affected scope.

A problem in one language should not automatically invalidate unrelated
languages without evidence.

---

# 85. Certification History

Certification decisions should be preserved historically.

Do not overwrite the previous certification state without recording the
transition.

---

# 86. Certification Ledger

The project should eventually maintain a machine-readable certification
ledger.

Suggested fields:

- capability ID;
- version;
- language;
- scope;
- status;
- certification date;
- evidence version;
- validation package;
- review triggers;
- superseding version.

---

# 87. Capability Matrix

The certification system should eventually expose a matrix showing:

CAPABILITY
×
LANGUAGE
×
VERSION
×
STATUS

---

# 88. Resource Matrix

Where relevant, certification should also identify resource dependencies.

---

# 89. Detector Matrix

Where external evaluation is relevant, maintain a matrix of:

CAPABILITY
×
DETECTOR
×
VERSION
×
DATE
×
RESULT

---

# 90. Evaluation Coverage

Certification should make gaps visible.

A missing detector evaluation is a coverage gap, not evidence of success.

---

# 91. Coverage Status

Possible states:

COVERED
PARTIALLY_COVERED
NOT_COVERED
NOT_APPLICABLE

---

# 92. Scientific Confidence

Certification may include an evidence-confidence descriptor.

Suggested levels:

LOW
MODERATE
HIGH

The descriptor must be justified by the evidence portfolio.

---

# 93. Confidence Is Not Certainty

No scientific certification should be interpreted as proof of universal
success.

---

# 94. Generalization

Generalization claims must be proportional to the evaluated scope.

---

# 95. External Validation

Independent external evaluation is valuable where available.

It should be distinguished from internal testing.

---

# 96. Independent Reproduction

Independent reproduction strengthens evidence but is not always possible.

The certification record should explicitly state whether it occurred.

---

# 97. Reproducibility Failure

If a previously reproducible result cannot be reproduced, investigate whether
the cause is:

- software;
- environment;
- resource;
- randomness;
- external service;
- documentation;
- original experimental error.

---

# 98. Scientific Audit

A certification audit should inspect:

- evidence;
- methodology;
- data provenance;
- benchmark integrity;
- statistical analysis;
- implementation identity;
- reproducibility.

---

# 99. Automated Certification Checks

Some checks should eventually be automated.

Examples:

- manifest completeness;
- checksum verification;
- version consistency;
- test status;
- benchmark identity;
- required evaluation coverage.

---

# 100. Human Scientific Review

Automated checks cannot replace scientific interpretation.

A human or appropriately designated scientific review process must interpret
material evidence where required.

---

# 101. AI-Assisted Certification

AI tools may assist with:

- literature organization;
- experiment generation;
- analysis;
- documentation;
- consistency checks.

They must not silently determine certification status without the project's
defined evidence process.

---

# 102. Certification Independence

The implementation agent should not be the sole authority determining that
its own implementation is scientifically certified.

---

# 103. Separation of Roles

Where practical, separate:

- implementation;
- validation;
- certification decision.

---

# 104. Automated Validation Agent

Claude Code may execute validation procedures automatically.

It may report whether predefined criteria passed.

---

# 105. Certification Authority

The project documentation defines the criteria.

The certification process determines whether those criteria have been met.

---

# 106. Scientific Change Management

When new research appears:

1. register source;
2. identify affected assumptions;
3. perform impact assessment;
4. create required experiments;
5. update validation;
6. revise certification if necessary.

---

# 107. Watermark Methodology Updates

A newly published watermark technique should enter the same process.

It should not automatically be ignored because the existing evaluation suite
does not contain it.

---

# 108. Detection Methodology Updates

A newly published AI-detection technique should likewise trigger an
evaluation-impact assessment when relevant.

---

# 109. New Threat Model

When a new evaluation method exposes a previously unknown weakness, the
capability may move from:

CERTIFIED

to:

REQUIRES REVIEW

until the evidence is assessed.

---

# 110. No Permanent Certification

Certification is not a lifetime guarantee.

---

# 111. Certification Renewal

Renewal may be triggered by:

- major scientific changes;
- capability changes;
- resource changes;
- relevant external evaluation changes.

---

# 112. Version Promotion

A new version does not inherit certification automatically.

It may inherit evidence only where equivalence has been demonstrated and
documented.

---

# 113. Minor Version Changes

Even minor changes must be evaluated for scientific impact.

A version number alone cannot determine equivalence.

---

# 114. Model Updates

Changing a model may materially change scientific behavior.

Model updates therefore require appropriate revalidation.

---

# 115. Dataset Updates

Dataset changes require reassessment when they affect training, tuning or
evaluation.

---

# 116. Detector Updates

Detector changes require new metadata and potentially new evidence.

---

# 117. Language Resource Updates

Tokenizer, dictionary or linguistic-resource changes may require language
revalidation.

---

# 118. Certification Dependency Graph

Certification should represent dependencies between:

CAPABILITY
→ RESOURCES
→ EXPERIMENTS
→ EVIDENCE
→ CERTIFICATION

---

# 119. Dependency Invalidation

If a critical dependency becomes invalid, dependent certification enters
REQUIRES REVIEW.

---

# 120. Cascading Review

A material scientific change may affect multiple capabilities.

The project should support impact analysis rather than requiring complete
revalidation blindly.

---

# 121. Review Prioritization

Prioritize review according to:

- severity;
- scope;
- scientific relevance;
- likelihood of invalidation;
- operational importance.

---

# 122. Emergency Review

Critical evidence may trigger immediate review.

---

# 123. Certification Freeze

When certification is under review, the affected capability may be frozen
from new certified releases while research continues.

---

# 124. Historical Execution

Previously certified results should retain their historical certification
context.

A later revocation does not rewrite history.

---

# 125. Historical Interpretation

Historical results may need a warning if later evidence changes their
interpretation.

---

# 126. Scientific Versioning

Scientific methodology should be versioned independently from ordinary
software versioning when necessary.

---

# 127. Methodology Identity

A methodology identity should describe the scientific procedure used for a
certification experiment.

---

# 128. Experimental Protocol

Important certification experiments should have explicit protocols.

Protocols should specify:

- input;
- preprocessing;
- method;
- parameters;
- evaluation;
- metrics;
- acceptance criteria.

---

# 129. Protocol Versioning

Changing a protocol creates a new protocol version.

---

# 130. Protocol Reuse

Protocols should be reusable across capability versions where scientifically
appropriate.

---

# 131. Certification Dataset Protection

Certification datasets should be protected from accidental modification.

---

# 132. Certification Data Access

Access should be controlled according to the security and data
documentation.

---

# 133. Blind Evaluation

Where practical, evaluation should be performed without exposing expected
results to the evaluator.

---

# 134. Double-Check Principle

Important certification results should be independently checked where
practical.

---

# 135. Result Integrity

Raw evaluation results should be preserved when feasible.

Derived metrics should be reproducible from raw results.

---

# 136. Analysis Scripts

Analysis scripts used for certification should be versioned.

---

# 137. No Manual Result Editing

Certification results should not be manually altered without an audit trail.

---

# 138. Result Corrections

If an error is discovered:

- preserve original result;
- record correction;
- identify cause;
- regenerate derived results.

---

# 139. Certification Artifact

The final certification artifact should reference all material evidence.

---

# 140. Certification Report

A certification report should summarize:

- what was evaluated;
- how it was evaluated;
- against what;
- under which conditions;
- results;
- limitations;
- decision.

---

# 141. Limitations

Every certification should explicitly document known limitations.

---

# 142. Unknowns

Important unknowns should not be hidden.

---

# 143. Negative Space

Certification should identify what was NOT evaluated when that omission could
materially affect interpretation.

---

# 144. Scientific Scope Statement

Every certified capability should have a concise scope statement.

---

# 145. Example Scope Structure

A scope may be expressed as:

Capability X
Version Y
Language Z
Resource set R
Evaluation portfolio E
Environment V

CERTIFIED

---

# 146. Operational vs Scientific Certification

Operational readiness answers:

"Can the system execute reliably?"

Scientific certification answers:

"Is there sufficient evidence that this capability satisfies the defined
scientific acceptance criteria for this scope?"

These questions must remain separate.

---

# 147. Security vs Scientific Certification

Security certification and scientific certification are also distinct.

A scientifically effective capability may still be operationally unsafe.

---

# 148. Privacy Certification

Where external services are involved, privacy requirements must be evaluated
separately.

---

# 149. Combined Release Eligibility

A production release should require all relevant gates:

TECHNICAL
+
OPERATIONAL
+
SECURITY
+
SCIENTIFIC
+
DOCUMENTATION

---

# 150. Gate Failure

Failure of one required gate prevents full release certification.

---

# 151. Partial Release

A release may expose only the capabilities that satisfy their individual
requirements.

---

# 152. Capability-Level Release

Certification should operate at capability level where practical rather than
forcing the entire software system into one binary state.

---

# 153. Continuous Evolution

The certification framework itself must be maintainable.

New evaluation methodologies should be addable without redesigning the
entire framework.

---

# 154. New Metrics

New metrics should be addable as independent evaluation components.

---

# 155. New Detectors

New detectors should be addable through the evaluation portfolio.

---

# 156. New Watermark Evaluations

New watermark evaluations should be addable without invalidating historical
evaluation records.

---

# 157. New Languages

New languages should enter certification independently.

---

# 158. Retiring Metrics

Obsolete metrics may be deprecated.

Historical results using them remain identifiable.

---

# 159. Retiring Detectors

Obsolete detectors may be retired while preserving historical evidence.

---

# 160. Retiring Protocols

Obsolete protocols may be retired after documenting their replacement.

---

# 161. Certification Backlog

Unresolved certification needs should enter the project backlog rather than
remain informal.

---

# 162. Research Backlog Integration

Certification gaps that require new scientific research should be linked to
the research backlog.

---

# 163. Validation Backlog Integration

Certification gaps that require additional testing should be linked to the
validation backlog.

---

# 164. Documentation Integration

Certification changes should update relevant maps and detailed
documentation.

---

# 165. Certification Change Queue

Material certification changes that cannot be completed immediately should be
recorded in:

docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md

---

# 166. Certification Decision Log

Material certification decisions should be recorded in:

docs/00-project/DECISION-LOG.md

---

# 167. Assumption Changes

If certification exposes an invalid assumption, update:

docs/00-project/ASSUMPTION-REGISTRY.md

---

# 168. Open Scientific Questions

Unresolved scientific questions should be recorded in:

docs/00-project/OPEN-QUESTIONS.md

---

# 169. Final Certification State

A capability should always have an explicit current state.

No capability should rely on an ambiguous concept such as:

"probably works."

---

# 170. Certification Transparency

Certification status should be discoverable from project documentation and
machine-readable metadata where practical.

---

# 171. Certification Audit Trail

The project should preserve:

- decision;
- evidence;
- protocol;
- versions;
- date;
- scope;
- reviewer or decision process;
- subsequent changes.

---

# 172. Certification Integrity

Certification records must not be silently overwritten.

---

# 173. Certification Reversal

A certification reversal should itself be versioned and documented.

---

# 174. No Self-Certification by Implementation

An implementation agent may execute validation but must not silently declare
its own implementation scientifically successful without the defined
certification process.

---

# 175. Automated Pre-Certification

Automation may determine:

- required files present;
- tests passing;
- evidence complete;
- manifests consistent.

The final scientific interpretation remains governed by the certification
process.

---

# 176. Certification Quality Gate

Before certification, verify:

- scope defined;
- acceptance criteria defined;
- datasets identified;
- resources identified;
- methodology versioned;
- evaluation performed;
- results preserved;
- limitations documented.

---

# 177. Certification Failure Gate

Certification must fail or remain pending when:

- required evidence is missing;
- evaluation is irreproducible;
- acceptance criteria fail;
- scope is undefined;
- benchmark integrity is uncertain;
- critical dependencies are unknown.

---

# 178. Certification Warning

Warnings may coexist with certification only when explicitly classified as
non-blocking and compatible with the certified scope.

---

# 179. Certification vs Universal Guarantee

Certification is never a universal guarantee against all future conditions.

---

# 180. Future-Proof Certification

The certification framework must remain capable of evaluating methodologies
that do not yet exist.

This is achieved through modular evaluation components rather than a fixed
list of tests.

---

# 181. Scientific Evolution

When scientific knowledge changes, the project changes with it.

The objective is not to preserve an old certification indefinitely.

The objective is to preserve scientific traceability while updating the
current state of knowledge.

---

# 182. Final Principle

The project should always be able to answer five questions:

1. What exactly was evaluated?
2. Under which conditions?
3. Against which evidence?
4. What did the evaluation actually demonstrate?
5. Why is the current certification still justified?

If any of these questions cannot be answered, the certification status must
be reconsidered.