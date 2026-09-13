# External Integration Architecture

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Architecture sub-document (Tranche 4)
**Authority:** Architectural
**Parent:** `docs/04-architecture/ARCHITECTURE-MAP.md` §29-31 (External
Integration Layer, External Data Boundary, Cloud Detector Integration)
**Scope:** How an external service, dataset, or model download is
isolated behind an adapter, made explicit to the user before any data
leaves the local system, and prevented from silently becoming a hidden
dependency of the deterministic local pipeline.

---

# 1. Purpose

This document formalizes `ARCHITECTURE-MAP.md` §29-31 into a concrete
adapter and boundary model. It exists because §58 of that document lists
`EXTERNAL-INTEGRATION-ARCHITECTURE.md` as a candidate; §64.4 originally
left it, and five other candidates, unevaluated, "recommended to revisit
after Tranches 1-2." `DECISION-LOG.md` DEC-021 (Tranche 4) assessed it as
"likely ready but not drafted in this pass — scoped as a candidate next
step." This document is that next step, per the owner's confirmation to
proceed.

Like `CORE-ARCHITECTURE.md`, this document's readiness does not depend on
per-language or per-model research evidence — §29-31 describe a boundary
and isolation mechanism, not a decision about which external provider,
detector, or dataset is scientifically adequate. It is directly grounded
in two decisions already made: `DECISION-LOG.md` DEC-001 (the production
runtime must not require a remote generative-AI service) and DEC-002
(external detection services may be integrated through explicit adapters
but are not part of the mandatory offline core). This document formalizes
*how* those two decisions are architecturally enforced, not whether they
hold — they were already decided.

Like every prior tranche document, this document selects no specific
external provider, protocol, or data format. It defines the mechanism any
of them would need to plug into.

---

# 2. Relationship to Other Documents

- `ARCHITECTURE-MAP.md` §29-31 is the authoritative parent; this document
  elaborates, it does not supersede.
- `docs/00-project/DECISION-LOG.md` DEC-001 and DEC-002 are the
  governing decisions this document operationalizes architecturally.
- `docs/04-architecture/CORE-ARCHITECTURE.md` §4 already lists the
  External Integration Layer as "not yet formalized beyond
  `ARCHITECTURE-MAP.md` §29-31 (a candidate document, per §10 below)" —
  this document is that formalization. `CORE-ARCHITECTURE.md` §6's
  Orchestration Layer dispatch flow is unchanged by this document: an
  external integration is invoked the same way as any other capability,
  through the adapter boundary this document defines, and is subject to
  the same failure-isolation and eligibility reporting `CORE-ARCHITECTURE.md`
  §9 already requires — this document does not duplicate that reporting
  taxonomy, it extends it with one additional case (§7 below).
- `docs/04-architecture/CAPABILITY-ARCHITECTURE.md` governs whether a
  capability that happens to be backed by an external integration is
  eligible for a given language and at what lifecycle state (§10 of that
  document); this document governs the boundary the integration itself
  must sit behind, independent of which capability uses it.
- `docs/04-architecture/DATA-MODEL.md` already covers model/dataset
  provenance, versioning and resource-budget enforcement for artifacts
  once they are local (its §5 Resource Resolution Flow, §7 budget
  enforcement); this document covers the boundary crossing itself — the
  act of a model download, dataset fetch, or cloud call happening at
  all — which is logically prior to and distinct from what `DATA-MODEL.md`
  does with the artifact afterward.
- `ARCHITECTURE-MAP.md` §49 (Security Boundaries) and §50 (Supply-Chain
  Integrity) are the authoritative documents for trust and provenance
  requirements on external artifacts generally; this document restates
  only the parts directly relevant to the adapter boundary (§6 below) and
  does not attempt a full security architecture, which remains its own
  area (`docs/06-security/`, per §61).
- `ARCHITECTURE-MAP.md` §36 (Configuration Layer) and §38 (Reporting
  Layer) are cross-referenced (§5, §7 below) but not formalized by this
  document — both remain their own candidate documents per DEC-021's
  triage.

---

# 3. Adapter Isolation Principle

Per `ARCHITECTURE-MAP.md` §29, every external integration must be
isolated behind an adapter, and the rest of the system must depend on the
adapter interface rather than on the provider implementation. This
document requires that the adapter boundary specifically be the *only*
place provider-specific code, request formats, authentication, or
response parsing may live. No orchestration, analysis, transformation, or
validation code (`CORE-ARCHITECTURE.md` §6; `ANALYSIS-ARCHITECTURE.md`;
`VALIDATION-ARCHITECTURE.md`) may reference a specific external provider
by name or format — it may only invoke the adapter interface and receive
back a result already normalized into this project's own schemas
(`ARCHITECTURE-MAP.md` §56, Schema-First Principle).

This is the same isolation discipline `ARCHITECTURE-MAP.md` §27
(Dependency Isolation) already requires of external detector
integrations, optional language models, and GPU-specific components
generally; this document narrows it specifically to the boundary where
data or a request actually crosses outside the local system.

---

# 4. External Integration Categories

Per `ARCHITECTURE-MAP.md` §29, an external integration may provide:
detector measurements, research data, benchmark data, model downloads, or
optional validation services. This document distinguishes two
architecturally different kinds of crossing, because they carry different
obligations under §5-6 below:

- **Outbound** — user-provided or in-progress text leaves the local
  system to be processed elsewhere (e.g. a cloud detector call, an
  optional external validation service). This is the case §30's opt-in
  and data-transfer-logging requirements govern most directly, and the
  one this document treats with the most caution.
- **Inbound-only** — an artifact (a model file, a dataset, a benchmark
  set) is fetched from an external source but no user text is sent
  outward. This still crosses the security and supply-chain boundary
  (`ARCHITECTURE-MAP.md` §49-50) but does not implicate §30's
  data-transfer-logging requirement in the same way, since nothing of the
  user's is transmitted.

A single integration may do both (e.g. a hosted service that must first
download a client library). The adapter (§3) must make explicit, per
integration, which of the two — or both — it performs, so that the
distinction is a declared property of the adapter rather than something a
reader has to infer from its behavior.

---

# 5. External Data Boundary

Per `ARCHITECTURE-MAP.md` §30, before any text is sent externally, the
system must make the operation explicit, and external processing must
never happen implicitly. This document requires that this explicitness be
enforced at the adapter boundary (§3) itself — not left to interface-layer
convention (`CORE-ARCHITECTURE.md` §5) — so that no interface built on
this core can accidentally trigger outbound (§4) transfer without the
user-visible confirmation §30 requires. Concretely, the adapter boundary
must support, per §30's own list:

- **opt-in external processing** — an outbound integration must default
  to disabled and require an explicit enabling action, never an
  opt-out default;
- **provider identification** — which external service or source is
  involved must be surfaced, not abstracted away as "external";
- **configuration visibility** — what will be sent, and under what
  configuration, must be inspectable before the call is made
  (`ARCHITECTURE-MAP.md` §36 governs where that configuration itself
  lives, once a Configuration Layer document formalizes it);
- **data-transfer logging** — that a transfer happened, to which
  provider, and what category of data (§4) must be recorded, feeding the
  Reporting Layer (`ARCHITECTURE-MAP.md` §38) once formalized;
- **failure handling** — an unreachable or erroring external service must
  surface as an explicit failure state (§7 below), never as a silent
  empty result;
- **local fallback where available** — if a local-only path exists for
  the same capability, its availability must be surfaced alongside the
  external option, not hidden behind it.

---

# 6. Cloud Detector Integration

Per `ARCHITECTURE-MAP.md` §31, a cloud detector may be used as a research
measurement instrument; its result must remain an external observation
and must never become a hidden part of the local transformation pipeline;
a cloud service becoming unavailable must not alter the deterministic
local processing path. This document makes explicit what "remains an
external observation" means architecturally: a cloud detector's result
is written into the same observation schema `ANALYSIS-ARCHITECTURE.md`
§7 (Output Category Tagging) already requires for every analysis
result — it is tagged by its source and evidence character, exactly as
`SPECIFICATION-MAP.md` §22's evidence discipline requires of a research
finding, and it is never permitted to silently substitute for, override,
or gate a local capability's own result. If a cloud detector and a local
capability disagree, both observations must be reported side by side
(`CORE-ARCHITECTURE.md` §6, aggregation must not collapse per-capability
results into a single value) — this document does not decide, and no
document yet decides, how a report should present a disagreement to a
reader; that is a Reporting Layer concern (§38, not yet formalized).

---

# 7. Failure and Availability as an Explicit Case

`CORE-ARCHITECTURE.md` §9 already requires that a request-level report
distinguish four states for any capability: ran and produced a result;
eligible but not invoked; not eligible for the request's language; and
invoked and failed. This document adds the state that is specific to an
external integration and does not arise for a purely local capability:

- **eligible and invoked, but the external boundary itself was
  unreachable or unavailable** (network failure, provider outage,
  authentication failure, rate limiting) — distinct from a capability
  *failing after* it ran (`CORE-ARCHITECTURE.md` §9's fourth state)
  because here the capability's own logic never had the opportunity to
  run at all.

This distinction matters because `ARCHITECTURE-MAP.md` §31 requires that
a cloud service's unavailability "must not alter the deterministic local
processing path" — the local pipeline must continue exactly as if the
external integration had not been configured, modulo the explicit,
visible gap this state records. Conflating "the provider was unreachable"
with "the capability found nothing" would violate the same
missing-evidence discipline `VALIDATION-ARCHITECTURE.md` §9 and
`CORE-ARCHITECTURE.md` §9 already require elsewhere.

---

# 8. Security and Trust Boundary for External Artifacts

Per `ARCHITECTURE-MAP.md` §49 (Security Boundaries), the architecture
must distinguish local trusted processing, user-provided input, external
data, external services, downloaded artifacts, and experimental
components — and downloaded models and datasets must not automatically
gain arbitrary execution privileges. This document requires that the
adapter boundary (§3) be the enforcement point for that distinction
specifically for inbound artifacts (§4): a downloaded model or dataset
crosses into `DATA-MODEL.md`'s provenance tracking (version, provenance,
license, checksum) only through the adapter, never by a capability
fetching and loading an artifact directly. This document does not
itself define the security controls §49 requires (sandboxing,
permission scoping, checksum verification mechanics) — those remain
`docs/06-security/`'s authoritative territory (§61) — it only requires
that whatever those controls turn out to be, they attach at this single
crossing point rather than being reimplemented per capability.

---

# 9. Illustrative Example (Non-Binding)

Purely to make §3-7's mechanism concrete — not a decision to adopt any
specific provider, protocol, or data format:

```
integration: (unnamed) cloud AI-generated-text detector
category (§4): outbound (user text sent for measurement)
adapter boundary: normalizes provider-specific request/response into
  this project's own observation schema (§6); no other layer references
  the provider's API directly
opt-in state: disabled by default; user must explicitly enable per §5
on invocation:
  - provider identified to the user before the call (§5)
  - data-transfer logged: category=outbound, provider=<identified>,
    text-hash=<preservation-snapshot hash, CORE-ARCHITECTURE.md §8>
  - result tagged as external observation (§6), reported alongside any
    local AI-generated-text capability's own result, never substituted
    for it
on provider unavailability:
  - reported as "eligible and invoked, external boundary unreachable"
    (§7) — distinct from "capability found nothing"
  - local pipeline continues unaffected (§6, per ARCHITECTURE-MAP.md §31)
```

---

# 10. What This Document Does Not Decide

This document does not: select, name, or evaluate any specific external
provider, cloud detector, dataset source, or model repository; fix a
concrete protocol, request/response format, or authentication mechanism
for the adapter boundary (`ARCHITECTURE-MAP.md` §43 reserves this for
Development); define the security controls `ARCHITECTURE-MAP.md` §49-50
require beyond naming the single crossing point they must attach to
(§8); decide whether local fallback is *mandatory* for any specific
capability that has an external variant — that remains a
`CAPABILITY-ARCHITECTURE.md`-level, per-capability decision; formalize
the Configuration Layer (§36) or Reporting Layer (§38) beyond the
cross-references in §5-6; or resolve DCQ-006, DCQ-007, or DCQ-008.

---

# 11. Final Principle

An external integration earns no exception from this project's core
discipline merely because it happens outside the local system — if
anything it needs more scaffolding, not less: explicit consent before
data leaves, a named provider instead of an anonymous "external" label,
a result that is reported as what it is (an outside observation) rather
than laundered into the appearance of a local finding, and a failure mode
that never quietly degrades into "no result" when what actually happened
was "unreachable." This document's adapter boundary exists so that
crossing outside the system is always a visible, deliberate act, never an
incidental side effect of using a capability that happens to be
implemented that way.
