# Core Architecture

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Architecture sub-document (Tranche 4)
**Authority:** Architectural
**Parent:** `docs/04-architecture/ARCHITECTURE-MAP.md` §3-8 (High-Level
Architecture, Architectural Layers, Interface Layer, Orchestration Layer,
Text Representation Layer, Preservation Snapshot)
**Scope:** How a request actually flows end-to-end — input, preservation
snapshot, representation, orchestrated dispatch to analysis/transformation/
validation, output and report — without selecting any specific detector,
model, or algorithm.

---

# 1. Purpose

This document formalizes `ARCHITECTURE-MAP.md` §3-8 into a concrete
execution model: the deterministic backbone every capability formalized so
far (`CAPABILITY-ARCHITECTURE.md`, `DATA-MODEL.md`,
`VALIDATION-ARCHITECTURE.md`, `ANALYSIS-ARCHITECTURE.md`,
`LANGUAGE-ARCHITECTURE.md`) assumes exists but none of them define. It
exists because §58 of that document lists `CORE-ARCHITECTURE.md` as a
candidate; §64.4 originally left it, and five other candidates,
unevaluated, "recommended to revisit after Tranches 1-2." Having now
completed Tranches 1, 2 and 3a, this document is the first of that
revisit.

Unlike the Tranche 1-3a documents, this document's readiness does not
depend on any per-language or per-model research evidence at all — §3-8
describe pure execution mechanics (how a request moves through the
system), not a decision about which detector, watermark scheme, or model
is scientifically adequate for which language. In that sense it is less
blocked than any prior tranche document, not more: the only readiness
question was whether formalizing it was in scope for this pass, which the
owner's confirmation resolves.

Like every prior tranche document, this document selects no specific
technology, algorithm, or model. It defines the mechanism that any of
them would need to plug into.

---

# 2. Relationship to Other Documents

- `ARCHITECTURE-MAP.md` §3-8 is the authoritative parent; this document
  elaborates, it does not supersede.
- `docs/04-architecture/CAPABILITY-ARCHITECTURE.md` governs what the
  Orchestration Layer (§6 below) actually dispatches to — a capability
  record (that document's §4) — and how it decides whether a capability
  is eligible to run for a given language (that document's §10). This
  document does not redefine capability selection rules; it defines where
  in the execution flow selection happens.
- `docs/04-architecture/ANALYSIS-ARCHITECTURE.md` and
  `VALIDATION-ARCHITECTURE.md` are two of the capability families the
  Orchestration Layer dispatches to; this document does not restate their
  internal behavior.
- `docs/04-architecture/DATA-MODEL.md` §5 (Resource Resolution Flow)
  already describes how a capability resolves its dataset/model
  dependency once dispatched; this document's Orchestration Layer (§6)
  is what triggers that resolution, not a duplicate of it.
- `ARCHITECTURE-MAP.md` §13-15 (Transformation Layer) is not itself
  formalized by this document — the deterministic backbone described
  here applies equally to a run that includes a transformation and one
  that only analyzes, but the transformation-specific candidate model
  (`VALIDATION-ARCHITECTURE.md` §3) is already restated there and is not
  duplicated here.
- Whether a separate `PIPELINE-ARCHITECTURE.md` document is needed beyond
  §6 below is explicitly not decided by this document — see §10.

---

# 3. High-Level Pipeline (Restated)

Per `ARCHITECTURE-MAP.md` §3:

```
INPUT
  → PRESERVATION SNAPSHOT
  → NORMALIZATION / REPRESENTATION
  → ANALYSIS
  → OPTIONAL CONTROLLED TRANSFORMATION
  → INTEGRITY VALIDATION
  → EVALUATION
  → OUTPUT + REPORT
```

The pipeline must preserve the original input independently of all
intermediate representations (§3; formalized as §7-8 below). This
document formalizes every stage up to and including dispatch into
ANALYSIS/TRANSFORMATION/VALIDATION (§4-8); the internal behavior of those
three stages is formalized by their own documents
(`ANALYSIS-ARCHITECTURE.md`, `VALIDATION-ARCHITECTURE.md`, and the
not-yet-drafted `TRANSFORMATION-ARCHITECTURE.md`), and EVALUATION/OUTPUT
+ REPORT are touched only where §6's result-aggregation responsibility
requires it — a full Evaluation/Reporting architecture remains a
candidate document in its own right (§58 of `ARCHITECTURE-MAP.md`,
`REPORTING-ARCHITECTURE.md`).

---

# 4. Architectural Layers (Restated, With Current Formalization Status)

Per `ARCHITECTURE-MAP.md` §4, restated here with which sub-document
currently formalizes each layer, so a reader does not need to
cross-reference §58 separately:

1. Interface Layer — §5 below.
2. Orchestration Layer — §6 below.
3. Text Representation Layer — §7 below.
4. Analysis Layer — `ANALYSIS-ARCHITECTURE.md`.
5. Transformation Layer — not yet formalized beyond `ARCHITECTURE-MAP.md`
   §13-15 (`TRANSFORMATION-ARCHITECTURE.md` remains premature, per
   `DECISION-LOG.md` DEC-019).
6. Validation Layer — `VALIDATION-ARCHITECTURE.md`.
7. Evaluation Layer — not yet formalized beyond `ARCHITECTURE-MAP.md`
   §21-22, §37.
8. Capability Layer — `CAPABILITY-ARCHITECTURE.md`.
9. Data / Model Layer — `DATA-MODEL.md`.
10. External Integration Layer — `EXTERNAL-INTEGRATION-ARCHITECTURE.md`
    (formalizes §29-31, drafted 2026-09-13 per `DECISION-LOG.md` DEC-022,
    after this document was written).
11. Persistence Layer — not yet formalized; not named among §58's
    candidate documents either, and this document does not add it as one.
12. Reporting Layer — `REPORTING-ARCHITECTURE.md` (formalizes §38,
    drafted 2026-09-13 per `DECISION-LOG.md` DEC-024, after this document
    was written).
13. Configuration Layer — `CONFIGURATION-ARCHITECTURE.md` (formalizes
    §36, drafted 2026-09-13 per `DECISION-LOG.md` DEC-025 after resolving
    its scoping overlap with §37, both after this document was written).

Layer 3 (Text Representation) also covers the Language Architecture's
concerns from a different angle: `LANGUAGE-ARCHITECTURE.md` governs which
language-specific resources exist and at what state; this document's §7
governs how a specific piece of text is represented once a language has
been identified and its resources resolved.

---

# 5. Interface Layer

Per `ARCHITECTURE-MAP.md` §5, the interface accepts input text,
configuration, evaluation-profile and language selection, requests
analysis or controlled transformation, and displays results or exports
reports. The interface must not contain scientific logic — every
decision about whether a transformation is acceptable, a detector result
is reliable, or a language is supported belongs to the layers behind it
(`CAPABILITY-ARCHITECTURE.md`, `ANALYSIS-ARCHITECTURE.md`,
`VALIDATION-ARCHITECTURE.md`, `LANGUAGE-ARCHITECTURE.md`), never to the
interface itself.

The architecture must permit multiple interfaces (command line, local
graphical interface, library/API, batch interface) over the same core.
This document's contribution beyond restating §5 is making explicit what
"the same core" means: a single Orchestration Layer entry point (§6)
that every interface calls identically, so that no interface can bypass
the dispatch, preservation, or reporting behavior another interface
relies on.

---

# 6. Orchestration Layer

Per `ARCHITECTURE-MAP.md` §6, the orchestration layer coordinates
execution: pipeline construction, capability selection, dependency
resolution, configuration validation, execution ordering, failure
handling, cancellation, resource limits, and result aggregation. The
orchestrator must not contain detector-specific or language-specific
algorithms — those live in the capabilities it dispatches to.

Concretely, for a single request, the orchestrator:

1. accepts the request from the Interface Layer (§5), including selected
   language, evaluation profile, and configuration;
2. triggers the Preservation Snapshot (§8) before any other processing;
3. resolves, for the request's declared language, which capabilities
   (`CAPABILITY-ARCHITECTURE.md` §4) are eligible to run — consulting
   that document's §10 per-language state map, not inventing its own
   eligibility logic;
4. for each eligible capability, triggers dependency resolution through
   `DATA-MODEL.md` §5's resolution flow before invoking it;
5. dispatches to Analysis (`ANALYSIS-ARCHITECTURE.md`), optionally
   Transformation, and Validation (`VALIDATION-ARCHITECTURE.md`), in the
   order `ARCHITECTURE-MAP.md` §3's pipeline specifies;
6. aggregates results using the schemas each layer defines
   (`ARCHITECTURE-MAP.md` §56, Schema-First Principle) — aggregation
   must not collapse per-capability, per-language results into a single
   value, per `CAPABILITY-ARCHITECTURE.md` §10 and
   `VALIDATION-ARCHITECTURE.md` §8's own requirements;
7. handles failure of any one capability per `ARCHITECTURE-MAP.md` §45
   (Failure Isolation) — one capability's failure must not corrupt
   results already produced by another, and must be reported explicitly
   (§9 below), never silently absorbed.

Resource limits (`ARCHITECTURE-MAP.md` §6) at the orchestration level are
distinct from, and sit above, the resource-budget enforcement
`DATA-MODEL.md` §7 already places at the Data/Model Layer's `resolve()`
operation — the orchestrator is responsible for cancellation and
overall request-level limits, not for re-implementing that budget check.

---

# 7. Text Representation Layer

Per `ARCHITECTURE-MAP.md` §7, the system must maintain, at minimum: the
canonical original text, an analysis representation, a transformation
representation, and the final output. The canonical original must remain
immutable — no capability, including a transformation capability, may
overwrite it.

This document requires that every representation beyond the canonical
original carry an explicit reference back to it (directly, or through a
chain of representations that terminates at it), so that
`ARCHITECTURE-MAP.md` §57's "No Hidden Scientific State" principle holds
for representations specifically: it must always be possible to trace any
intermediate or final representation to the immutable original without
relying on implementation-specific memory layout or undocumented
convention.

---

# 8. Preservation Snapshot

Per `ARCHITECTURE-MAP.md` §8, immediately after input and before any
other processing (§6, step 2), the orchestrator creates a preservation
snapshot. The snapshot may contain: original text, encoding, Unicode
normalization state, hashes, structural representation, paragraph/
sentence boundaries, tokenization, detected language, and metadata
required for validation. The snapshot provides the baseline against which
every subsequent change is measured.

This document requires that the snapshot's language-detection result
(if language was not explicitly supplied by the interface, per §5) be
recorded as its own field distinct from any user-supplied language
selection — a mismatch between detected and selected language is itself
a reportable condition (§9), not something to silently resolve by
preferring one over the other.

---

# 9. Failure and Uncertainty Reporting at the Core Level

Extending `ARCHITECTURE-MAP.md` §45 (Failure Isolation) and §57 (No
Hidden Scientific State) to the orchestration flow specifically: a
request-level report (ultimately the responsibility of a Reporting Layer
document, §10) must be able to distinguish, for the request as a whole:

- a capability that ran and produced a result (§6, step 5-6);
- a capability that was eligible but not invoked (e.g. cancelled, or
  skipped due to a resource limit, §6);
- a capability that was not eligible for the request's language at all
  (`CAPABILITY-ARCHITECTURE.md` §10's `NOT_SUPPORTED` state);
- a capability that was invoked and failed (§6, step 7).

These four states must never be conflated into a single "no result"
outcome — doing so would violate the same missing-evidence discipline
`VALIDATION-ARCHITECTURE.md` §9 already requires for validation results
specifically, extended here to the orchestration level generally.

---

# 10. What This Document Does Not Decide

This document does not: select any specific interface technology
(CLI, GUI, API framework); fix a concrete data structure or
serialization format for the preservation snapshot or intermediate
representations (`ARCHITECTURE-MAP.md` §43 reserves this for
Development); decide whether `PIPELINE-ARCHITECTURE.md` is a distinct
document from this one or whether §6's Orchestration Layer treatment
already covers what it would contain — that scoping question is left
open rather than answered by omission; or resolve DCQ-006, DCQ-007 or
DCQ-008 (the External Integration, Reporting, and Configuration Layers —
§29-31, §38, §36 — are now formalized separately by
`EXTERNAL-INTEGRATION-ARCHITECTURE.md`, `REPORTING-ARCHITECTURE.md`, and
`CONFIGURATION-ARCHITECTURE.md`, all drafted after this document).

---

# 11. Final Principle

Every capability this project formalizes — a detector, a validator, a
language resource — is only as trustworthy as the backbone that invokes
it consistently and reports honestly when something did not run, was not
eligible, or failed. This document's role is to make that backbone
explicit rather than assumed: so that "the system produced no result for
this dimension" always has one of a small number of honest, distinguishable
reasons (§9), never a silent gap indistinguishable from success.
