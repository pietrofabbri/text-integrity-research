# Configuration Architecture

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Architecture sub-document (Tranche 4)
**Authority:** Architectural
**Parent:** `docs/04-architecture/ARCHITECTURE-MAP.md` §36 (Configuration
Layer)
**Scope:** What a single request/run's configuration governs, how it
relates to — without duplicating — an Evaluation Profile (§37), and the
discipline that keeps scientific behavior discoverable from configuration
rather than hidden in undocumented defaults.

---

# 1. Purpose

This document formalizes `ARCHITECTURE-MAP.md` §36 into a concrete
configuration model. It exists because §58 of that document lists
`CONFIGURATION-ARCHITECTURE.md` as a candidate; §64.4 originally left it,
and five other candidates, unevaluated. `DECISION-LOG.md` DEC-023 (Tranche
4, continued) found it blocked — not for the evidence-based reasons that
blocked `TRANSFORMATION-ARCHITECTURE.md`, but because this document's own
scope overlaps, in its field list, with §37 (Evaluation Profiles), and
`ARCHITECTURE-MAP.md` did not state how the two relate. `DECISION-LOG.md`
DEC-025 resolves that overlap — Configuration and Evaluation Profile are
distinct, composable concepts, not the same object under two names — and
this document is drafted on that resolved basis.

Like every prior tranche document, this document selects no specific
configuration file format, schema language, or storage mechanism. It
defines what a request's configuration must be able to express and how it
relates to the other layers that consume it, not the concrete syntax.

---

# 2. Relationship to Other Documents

- `ARCHITECTURE-MAP.md` §36 is the authoritative parent; §2.7 (Architectural
  Principle: configuration as one of the system's nine separated
  concerns), §4.13 (Configuration Layer as its own architectural layer),
  §57 (No Hidden Scientific State: "all scientifically relevant state must
  be discoverable from configuration"), §40-41 (Reproducibility and
  Deterministic Core, both listing configuration), and §46-47 (Update
  Architecture / Compatibility: configuration schemas must be
  independently versionable, breaking changes explicit) are the other
  sections this document elaborates.
- `ARCHITECTURE-MAP.md` §37 (Evaluation Profiles) and
  `docs/03-scientific-specification/SPECIFICATION-MAP.md` §27-28 (No
  Universal Success Claim; Effectiveness Profiles) govern the distinct,
  evidentiary concept of an Evaluation Profile. Per `DECISION-LOG.md`
  DEC-025, this document's Configuration is not a rewording of that
  concept: a Configuration *selects* which Evaluation Profile (by name and
  version) governs a run's effectiveness framing (§4 below); it does not
  itself define what that profile contains. This document does not
  formalize §37 or `SPECIFICATION-MAP.md` §27-28 — they remain governed
  where they already are.
- `docs/04-architecture/CORE-ARCHITECTURE.md` §5-6 already restate that
  the Interface Layer accepts configuration (alongside language and
  evaluation-profile selection, listed separately) and that the
  Orchestration Layer's responsibilities include "configuration
  validation." This document does not redefine either responsibility; it
  defines what the configuration being accepted and validated actually
  contains.
- `docs/04-architecture/CAPABILITY-ARCHITECTURE.md` §10 (per-language
  capability state) and `docs/04-architecture/LANGUAGE-ARCHITECTURE.md`
  §4 govern which capabilities are eligible for a language independent of
  any run's configuration; a Configuration's "enabled capabilities" field
  (§3 below) can only narrow that eligible set, never widen it beyond what
  those documents already permit.
- `docs/04-architecture/EXTERNAL-INTEGRATION-ARCHITECTURE.md` §5 already
  states that "`ARCHITECTURE-MAP.md` §36 governs where [external-service]
  configuration itself lives, once a Configuration Layer document
  formalizes it" — this document is that formalization for the
  "external services" field (§3 below); it does not restate
  `EXTERNAL-INTEGRATION-ARCHITECTURE.md`'s own opt-in, logging, or
  adapter-isolation requirements.
- `docs/04-architecture/REPORTING-ARCHITECTURE.md` §2 already notes it
  "requires a report be able to record whatever configuration and
  evaluation-profile information exists" without depending on how the two
  relate; this document's resolution (§4 below) is what that dependency
  now resolves to, but `REPORTING-ARCHITECTURE.md`'s own schema is not
  restated here.
- `ARCHITECTURE-MAP.md` §43 (Development/Runtime Separation) reserves the
  concrete configuration format/schema for Development; this document
  does not fix one.

---

# 3. Configuration Content (Restated)

Per `ARCHITECTURE-MAP.md` §36, a request's configuration may define:
language, pipeline, enabled capabilities, transformation constraints,
validation profile, external services, resource limits, output format,
and logging level. "Which profile(s) apply" below covers both §36's own
literal "validation profile" field (still undefined — §5) and the
Evaluation Profile reference `DECISION-LOG.md` DEC-025 established as a
second, distinct profile a configuration selects; §36's own text predates
DEC-025 and names only the former. This document requires that every
field populated in a configuration be traceable to the document that
actually governs its meaning — a configuration is a set of *selections*,
not a place where new semantics are defined:

- `language` — selects among the languages `LANGUAGE-ARCHITECTURE.md` §4
  registers; does not itself add or define a language.
- `pipeline` — selects which stages of `CORE-ARCHITECTURE.md` §3's
  high-level pipeline run for this request (e.g. analysis-only versus
  analysis-plus-transformation); does not redefine the pipeline's stages.
- `enabled capabilities` — narrows, for this request, which of the
  capabilities `CAPABILITY-ARCHITECTURE.md` §10 already marks eligible for
  the selected language are actually invoked; per §2 above, this field
  can only narrow eligibility, never grant it.
- `transformation constraints` — selects specific constraint values within
  the bounds `ARCHITECTURE-MAP.md` §14 already defines; does not redefine
  what a constraint is.
- `evaluation profile` (§37) and, separately, `validation profile` — see
  §4 and §5 below.
- `external services` — selects which external integrations
  (`EXTERNAL-INTEGRATION-ARCHITECTURE.md` §3-4) are enabled for this
  request, including the opt-in state that document's §5 requires default
  to disabled.
- `resource limits` — sets request-level bounds distinct from, and
  composed with, the resource-budget enforcement `DATA-MODEL.md` §7
  already places at the Data/Model Layer's `resolve()` operation
  (`CORE-ARCHITECTURE.md` §6 already draws this distinction for
  orchestration-level limits generally).
- `output format` and `logging level` — govern presentation and
  diagnostic verbosity; `ARCHITECTURE-MAP.md` §39 (Observability) and
  `REPORTING-ARCHITECTURE.md` §3 remain authoritative for what
  observability and report content actually consist of.

---

# 4. Configuration's Relationship to an Evaluation Profile

Per `DECISION-LOG.md` DEC-025: an Evaluation Profile (§37,
`SPECIFICATION-MAP.md` §27-28) is a versioned, named bundle — techniques,
detectors, languages, datasets, transformations, metrics, thresholds,
date, evidence baseline — that scopes a scientific effectiveness claim
(`SPECIFICATION-MAP.md` §27: "effectiveness is evaluated against a
versioned, explicitly defined evaluation profile," never claimed
universally). This document requires that a Configuration's
`evaluation_profile` field hold only a reference — a name and version —
to one of the profiles `SPECIFICATION-MAP.md` §28 already enumerates
(baseline, conservative, multilingual, research, regression, release
certification) or a future one registered the same way. A Configuration
must never embed a full profile definition inline as if it were
request-local, ad hoc data: doing so would let a single run silently
originate an unversioned, unregistered effectiveness scope, exactly what
`SPECIFICATION-MAP.md` §27's "No Universal Success Claim" principle
exists to prevent.

This is a one-way reference, not a merge: the Evaluation Profile's own
content is defined and versioned wherever `SPECIFICATION-MAP.md` §27-28
and `ARCHITECTURE-MAP.md` §37 place it, never re-derived from, or
overridden by, a request's Configuration.

---

# 5. The Undefined "Validation Profile" Field

`ARCHITECTURE-MAP.md` §36 also lists "validation profile" as a
Configuration field, distinct from "evaluation profile" (§37) by name.
This document's evaluation found that no other document —
`VALIDATION-ARCHITECTURE.md` included — defines what a "validation
profile" actually is. Per `NO-INVENTION-RULES.md`, this document does not
invent a definition for it. It records the field's existence (because §36
already lists it) and requires that, if and when a "validation profile"
concept is defined, it be defined in `VALIDATION-ARCHITECTURE.md` (the
document already authoritative for validation-family scope, per that
document's §4) and referenced from here by name only — the same
one-way-reference discipline §4 above applies to Evaluation Profile. This
document does not resolve what "validation profile" means; that remains a
separate, later gap, distinct from the Configuration/Evaluation-Profile
overlap DEC-025 resolved, and should not be conflated with it.

---

# 6. Discoverability and No Hidden Scientific State

Per `ARCHITECTURE-MAP.md` §57, "all scientifically relevant state must be
discoverable from configuration, metadata or versioned resources." This
document requires that this hold specifically at the configuration
boundary: any behavior that could change a scientific result — which
capabilities ran, which profile scoped the effectiveness claim, which
external services were consulted — must be reconstructable by reading the
configuration a request actually used, never inferred from an
undocumented environment variable, a hardcoded default the configuration
schema does not expose, or a value silently substituted when a field was
left unset. Per §41 (Deterministic Core), configuration handling itself
should be deterministic: the same configuration, applied to the same
input and capability versions, must select the same behavior every time.

---

# 7. Versioning and Compatibility

Per `ARCHITECTURE-MAP.md` §56 (Schema-First Principle) and §46-47 (Update
Architecture, Compatibility), the configuration schema itself must be
explicit and versioned, independently of the software version, and a
breaking change to it must be explicit rather than silently tolerated by
older configurations continuing to parse with different effective
meaning. This document requires that a configuration schema version be
itself one of the fields `REPORTING-ARCHITECTURE.md` §3's observation
tier can record — per that document's §9 (Schema Stability and
Versioning), a report must remain interpretable even after the
configuration schema it was produced under has since changed.

---

# 8. Illustrative Example (Non-Binding)

Purely to make §3-5's relationship concrete — not a decision to adopt any
specific field syntax, capability, or profile as final:

```
configuration for: one request, Italian text
language: it
enabled capabilities: [subset of CAPABILITY-ARCHITECTURE.md §10's
  eligible-for-it set, narrowed for this request only]
evaluation_profile: reference only — name="multilingual", version="v1"
  (SPECIFICATION-MAP.md §28) — NOT an inline copy of that profile's
  techniques/detectors/thresholds/evidence-baseline
validation_profile: [field exists per ARCHITECTURE-MAP.md §36; its
  meaning is not yet defined by any document — recorded, not invented]
external_services: cloud AI-detector = disabled (default, per
  EXTERNAL-INTEGRATION-ARCHITECTURE.md §5's opt-in requirement)
resource_limits: [request-level; independent of DATA-MODEL.md §7's
  resolve()-level budget enforcement]
output_format / logging_level: [Development-phase decision, not fixed
  here]
```

The `evaluation_profile` field's value is small and stable (a name and a
version) precisely because the profile it points to is defined and
versioned elsewhere — the configuration does not grow every time a new
technique is added to that profile.

---

# 9. What This Document Does Not Decide

This document does not: select any specific configuration file format,
schema language, or storage mechanism (`ARCHITECTURE-MAP.md` §43 reserves
this for Development); define what "validation profile" means (§5 — a
separate gap for `VALIDATION-ARCHITECTURE.md` or a later decision to
resolve); define the content or governance of any specific Evaluation
Profile (`SPECIFICATION-MAP.md` §27-28 and `ARCHITECTURE-MAP.md` §37
remain authoritative for that); change the resource-budget enforcement
`DATA-MODEL.md` §7 already places at the Data/Model Layer; or resolve
DCQ-006, DCQ-007, or DCQ-008.

---

# 10. Final Principle

A configuration earns its place in this architecture only if reading it
tells the whole truth about what a run will do — which capabilities,
which languages, which external services, and against which named,
versioned basis any effectiveness claim it produces should be understood.
The moment a configuration starts embedding definitions that belong
elsewhere — a whole evaluation profile copied inline, a validation
concept invented on the spot because no document defines it yet — it
stops being a set of selections and starts being an undocumented second
source of truth, exactly what `ARCHITECTURE-MAP.md` §57 exists to
prevent. This document's discipline is to keep configuration small,
referential, and honest about what it does not itself define.
