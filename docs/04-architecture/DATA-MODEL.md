# Data Model (Architecture Layer)

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Architecture sub-document (Tranche 1)
**Authority:** Architectural
**Parent:** `docs/04-architecture/ARCHITECTURE-MAP.md` §32-33 (Data and
Model Layer, Resource Management)
**Scope:** How the Data/Model architectural layer is invoked by the rest
of the pipeline, and how it enforces the storage budget at runtime. Not a
data-governance document — see §2.

---

# 1. Purpose

This document formalizes `ARCHITECTURE-MAP.md` §32-33 into a concrete
architectural interface. It exists because §58 of that document lists
`DATA-MODEL.md` as a candidate document, and `ARCHITECTURE-MAP.md` §64
(2026-09-12) judged this document "structurally ready now," directly
supported by `docs/07-data/DATA-MAP.md` §7-9's existing governance
methodology and by R09's concrete, verified disk-size findings for
specific candidate resources (`RESEARCH-REGISTRY.md` R-0102-R-0121).

---

# 2. Relationship to `docs/07-data/DATA-MAP.md` — Read This First

`docs/07-data/DATA-MAP.md` is the authoritative document for data and
model **governance**: identifiers (§12), manifests (§80-81), licensing
(§38-40), lifecycle (§69), activation gates (§83-85), and storage-budget
allocation policy (§43-46, §102). This document does **not** restate,
duplicate, or override any of that. `DATA-MODEL.md` is authoritative only
for a narrower, different question: how the rest of the software
architecture (the Orchestration, Analysis, Transformation and Validation
layers named in `ARCHITECTURE-MAP.md` §4) actually obtains and uses a
dataset or model resource at run time, and where in the pipeline the
storage/resource budget is actually enforced.

If any statement in this document appears to conflict with `DATA-MAP.md`,
`DATA-MAP.md` governs, and this document should be corrected.

---

# 3. Layer Responsibility

Restating `ARCHITECTURE-MAP.md` §32: the Data/Model Layer manages
datasets, corpora, benchmark sets, model files, tokenizer resources,
language resources, detector configurations, and experiment artifacts.
Architecturally, this layer sits between the `DATA-MAP.md`-governed
artifacts on disk and the layers that consume them (Analysis,
Transformation, Validation — `ARCHITECTURE-MAP.md` §4). No other layer
should read a dataset or model file directly; all access goes through
this layer, so that governance rules (versioning, licensing, integrity)
have one enforcement point rather than being re-implemented per consumer.

---

# 4. Interface Contract (Conceptual, Not a Literal API)

The layer exposes, conceptually:

- **resolve(resource_id)** — given a `DATA-MAP.md`-registered dataset or
  model identifier, return a handle to the concrete artifact, or an
  explicit unavailable state (§8) if it cannot.
- **manifest(resource_id)** — return the governance metadata
  (`DATA-MAP.md` §80-81) without loading the artifact itself.
- **budget_status()** — return current usage against the storage budget
  (§7), per category (`DATA-MAP.md` §44).
- **release(resource_id)** — signal that a resource may be unloaded from
  active memory/cache (not deleted from disk — deletion is a
  `DATA-MAP.md`-governed operation, §70-71 of that document).

This is a conceptual contract, not a fixed function signature or chosen
programming-language interface — the exact implementation is a
Development-phase decision (§12).

---

# 5. Resource Resolution Flow

A capability (per `docs/04-architecture/CAPABILITY-ARCHITECTURE.md` §4)
declares its dependencies as `DATA-MAP.md`-registered identifiers. At run
time:

```
CAPABILITY REQUEST
  → CAPABILITY REGISTRY (confirms capability is ACTIVE/VALIDATED for the
     requested language, per CAPABILITY-ARCHITECTURE.md §6/§10)
  → DATA/MODEL LAYER . resolve(resource_id)
      → checks DATA-MAP.md manifest (§80-81): version, checksum, license
      → checks activation gate state (DATA-MAP.md §84-85)
      → returns handle, or an explicit unavailable state (§8)
  → CONSUMING LAYER (Analysis/Transformation/Validation) uses the handle
```

This flow is the architectural realization of `DATA-MAP.md` §95's
conceptual dependency graph (`DATASET → PREPROCESSOR → RESOURCE →
CAPABILITY → EXPERIMENT → RESULT`) — this document places that graph
inside the pipeline described in `ARCHITECTURE-MAP.md` §3.

---

# 6. Lazy Loading and Caching

Per `ARCHITECTURE-MAP.md` §27 (Dependency Isolation), the layer should
load a resource only when a request actually needs it, not eagerly at
startup — large or optional resources (§8) should not be loaded merely
because they exist in the registry. Caching of loaded resources follows
`DATA-MAP.md` §47 (Cache Policy: caches must be distinguishable from
canonical data, and may be deleted and regenerated) — this document adds
only that the *layer*, not each consuming component individually, is
responsible for cache lifetime, so that two capabilities depending on the
same model do not each hold their own redundant copy in memory.

---

# 7. Resource Budget Enforcement Point

`ARCHITECTURE-MAP.md` §33 states the architecture must distinguish
mandatory, optional, temporary, cached, benchmark and archival assets and
that large resources should be loadable/removable independently.
`DATA-MAP.md` §43-46 defines the ~30GB budget and its alert states
(NORMAL/WARNING/CRITICAL). This document places the actual enforcement of
those states at the Data/Model Layer's `resolve()` and `budget_status()`
operations (§4): a request that would push total *loaded* (not merely
on-disk) resource usage into CRITICAL should be rejected or require
explicit confirmation, rather than silently degrading behavior elsewhere
in the pipeline — consistent with `ARCHITECTURE-MAP.md` §45 (Failure
Isolation: "silent fallback is prohibited when it could change scientific
interpretation").

---

# 8. Optional Resource Handling at the Architecture Level

`DATA-MAP.md` §92 defines resource states `AVAILABLE / OPTIONAL / MISSING
/ INCOMPATIBLE / DEPRECATED`. This document requires that `resolve()`
(§4) return one of these states explicitly rather than throwing an
undifferentiated error, so that a consuming layer can distinguish "this
capability cannot run at all" from "this capability's optional resource
is simply not installed" — directly implementing `ARCHITECTURE-MAP.md`
§28 (Offline Core: the core must remain operational when optional
capabilities are unavailable) and §45 (Failure Isolation).

---

# 9. Quantization as an Architectural Concern

R09 §10.5 found that a model's effective quality, not only its disk size,
can depend on its quantization level, and that this interaction with the
project's multilingual requirement is explicitly unstudied. This document
therefore requires that a resolved model handle (§4) expose which
precision/quantization variant is active as part of its manifest
metadata (`DATA-MAP.md` §81's `format` field), not only its identifier —
so that a capability record's `known_limitations`
(`CAPABILITY-ARCHITECTURE.md` §4) can distinguish "validated at F16" from
"validated at Q4_K_M" once such validation work is done. This document
does not itself validate any quantization level for any model — that is
future Research/Validation work.

---

# 10. Multi-Candidate Resource Slots

Per `CAPABILITY-ARCHITECTURE.md` §13, more than one capability record may
exist in the same category with different underlying resources. This
document requires that the Data/Model Layer's interface (§4) address
resources by their `DATA-MAP.md` identifier, never by a hardcoded
assumption of "the" model for a category — this is what makes
`ARCHITECTURE-MAP.md` §2's "algorithms are replaceable components"
principle actually enforceable rather than aspirational.

---

# 11. Illustrative Example (Non-Binding)

Using `RESEARCH-REGISTRY.md` entries already on file, purely to make the
resolution flow (§5) concrete — not a decision to adopt these specific
resources:

```
resolve("DATA-MODEL-E5-LARGE-INSTRUCT")
  → manifest: {source: intfloat/multilingual-e5-large-instruct,
               format: fp16, size: ~1.14GB, license: open (R-0103)}
  → activation gate: NOT YET EVALUATED (no DATA-MAP.md manifest entry
    exists yet — this is illustrative, not a live registration)
  → returns: MISSING (per §8), since no such manifest is actually
    registered in DATA-MAP.md as of this document's writing
```

This illustrates that even a well-evidenced R09 candidate is not
automatically "available" merely because R09 discusses it — it becomes
available only once formally registered in `DATA-MAP.md`, a separate,
later step.

---

# 12. What This Document Does Not Decide

This document does not: select any specific model, dataset or
quantization level as the project's default for any capability; fix a
literal programming-language interface or function signature for §4's
contract; choose a concrete storage/serialization technology for
manifests or caches; or resolve any of DCQ-006, DCQ-007 or DCQ-008. All
of these remain separate, later decisions, consistent with DEC-009 and
`ARCHITECTURE-MAP.md` §64.5.

---

# 13. Final Principle

The Data/Model Layer's value is that every other layer can ask for a
capability's resource by identifier and receive either a working handle
or an honest, specific reason it cannot — never a silent substitution and
never a silent failure. This document exists to make that guarantee an
architectural property, not an incidental behavior of whichever component
happens to load a file first.
