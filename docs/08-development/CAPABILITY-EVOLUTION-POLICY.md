# Capability Evolution Policy

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Development process protocol (Tranche 4 of `DEVELOPMENT-MAP.md` §202)
**Authority:** Development (how capabilities are built, changed and replaced). The capability model itself remains with `docs/04-architecture/CAPABILITY-ARCHITECTURE.md`; validation gates with `docs/05-validation/VALIDATION-GATES.md`.
**Parent:** `docs/08-development/DEVELOPMENT-MAP.md` §25–35, §83–103
**Governance basis:** `P00-project-governance.md` §14, §15, §22, I-005
**Requirements basis:** `docs/03-scientific-specification/S02-scientific-requirements.md` `REQ-LIFE-003`, `REQ-LIFE-004`, `REQ-LIFE-005`, `REQ-LANG-005`
**Architectural basis:** `CAPABILITY-ARCHITECTURE.md` §4, §6–8, §10, §13; `LANGUAGE-ARCHITECTURE.md` §7; `CONFIGURATION-ARCHITECTURE.md` §6–7; `REPORTING-ARCHITECTURE.md` §5
**Research basis:** no new finding; `CAPABILITY-ARCHITECTURE.md` §10 records the evidence (KB-008, KB-010, `R09` §10.3–10.4) for language-scoped state
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-003, DEC-009, DEC-012, DEC-029, DEC-030, DEC-035, DEC-040, DEC-041, DEC-044 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes the development practice for capabilities: isolation, contracts, languages, configuration, registry, replacement, migration, compatibility and refactoring. It does not change the capability model or decide any gate. It sets no numeric value and selects no storage format or versioning scheme.

---

# 2. Recorded Contradictions — Not Resolved Here

**CEP-C1, lifecycle vocabulary.** Three enumerations describe what appears to be the same concept:

- `DEVELOPMENT-MAP.md` §27: `DRAFT → EXPERIMENTAL → VALIDATED → ACTIVE → MONITORED → DEPRECATED → RETIRED`.
- `CAPABILITY-ARCHITECTURE.md` §6: `DISCOVERED → EXPERIMENTAL → VALIDATED → ACTIVE → DEPRECATED → RETIRED`, with a `DEGRADED` branch.
- `P00-project-governance.md` §15: `DISCOVERED → EXPERIMENTAL → VALIDATED → ACTIVE → DEPRECATED → RETIRED → REMOVED`.

These are instances of the un-itemized set of "8–10" enumerations in `CLAUDE-CONSOLIDATION-REPORT.md` SECOND PASS §5S. `DEC-012`'s trigger for reconciliation is not met. Following the precedent of `VALIDATION-GATES.md` §2, this document writes in its Parent's vocabulary. That is a choice of which vocabulary to write in, not a finding of authority.

| ID | Subject | Locations | Finding |
|---|---|---|---|
| CEP-C2 | Activation | `DEVELOPMENT-MAP.md` §29; `CAPABILITY-ARCHITECTURE.md` §7 | §29 ties `ACTIVE` to "validation criteria". §7 places its Activation Gate at `VALIDATED` and treats `VALIDATED → ACTIVE` as a separate later step that may need a recorded decision. **INFERENCE:** both must be satisfied. |
| CEP-C3 | Registry fields | `DEVELOPMENT-MAP.md` §91; `CAPABILITY-ARCHITECTURE.md` §4 | §91 lists replacement and deprecation state, absent as named fields from the §4 schema. §4 has further fields. **INFERENCE:** a registry entry carries the fields of both. |
| CEP-C4 | Absent-support states | `DEVELOPMENT-MAP.md` §85; `REPORTING-ARCHITECTURE.md` §5; `LANGUAGE-ARCHITECTURE.md` §7 | §85: "unsupported/degraded". Reporting: `not measurable, unsupported, not applicable`. Language: `NOT_SUPPORTED`. Different layers; correspondence is not established. |
| CEP-C5 | Adding a language | `DEVELOPMENT-MAP.md` §86; `LANGUAGE-ARCHITECTURE.md` §7 | §86 requires resources, tests, validation, documentation and performance assessment. §7 allows an entry with most fields `NOT_SUPPORTED`. **INFERENCE:** an entry alone is not a capability expansion; §86 applies when support is claimed. |

---

# 3. Capability Structure (§25–26, §33–35)

- **Composition (§25):** prefer small composable capabilities to one monolithic algorithm. `P00` §14 sets an additive-by-default preference.
- **Isolation (§26):** each major capability has defined input, output, version, dependencies, tests, status and documentation. Lifecycle metadata is mandatory for production capabilities (`P00` I-005).
- **Modularity (§33):** interfaces allow replacement without rewriting unrelated parts.
- **Stable interfaces (§34):** stable where practical. A breaking change is documented, dependents are updated, regression tests run and architecture documentation updated. A breaking architectural change needs human approval (`P00` §5).
- **Dependency graph (§35):** dependencies among code, datasets, models, linguistic resources, detectors, validators and documentation are recognized. A change to one node may require validating dependent nodes.

---

# 4. Lifecycle in Development Practice (§27–32)

- **Lifecycle (§27):** see CEP-C1.
- **Experimental (§28):** may be used in research but is not automatically part of the certified production pipeline. `P00` §22 requires distinct lifecycle states.
- **Activation (§29):** see CEP-C2 and `VALIDATION-GATES.md` §4.
- **Deprecation (§30):** preferred to immediate deletion when a better method replaces the capability, a dependency becomes obsolete, evidence shows poor performance, maintenance cost becomes excessive, or a new methodology supersedes it. `REQ-LIFE-003` requires explicit deprecation.
- **Retirement (§31):** no longer used by the active system; historical evidence and metadata remain available (`REQ-LIFE-004`). `CAPABILITY-ARCHITECTURE.md` §8 sets the gate.
- **Replacement (§32):** a retired capability identifies its replacement where one exists; the replacement independently satisfies validation. Supersession is recorded (`REQ-LIFE-005`).

---

# 5. Contracts and Languages (§83–87)

- **Contracts (§83):** components expose explicit contracts for inputs, outputs, errors, configuration, supported languages and resource requirements.
- **Language contracts (§84):** a multilingual component declares its languages. "Multilingual" does not mean equally capable in every language. State is per language (`CAPABILITY-ARCHITECTURE.md` §10).
- **Unsupported languages (§85):** an explicit unsupported or degraded state, never a silent result that appears equivalent (see CEP-C4).
- **Expansion (§86):** a capability expansion (see CEP-C5).
- **Retirement of a language (§87):** when required resources disappear, performance is inadequate, security issues arise or maintenance becomes unsustainable. Historical results remain identified by the previous capability state.

---

# 6. Configuration and Selection (§88–92)

- **Configuration (§88):** explicit, validated, versionable, documented; no hidden environment-dependent behavior. `CONFIGURATION-ARCHITECTURE.md` §6–7 applies.
- **Defaults (§89):** safe and conservative. A developer's local configuration must not silently become a production requirement.
- **Feature flags (§90):** to activate experimental capabilities, disable obsolete components, compare implementations or roll back risky changes.
- **Registry (§91):** see CEP-C3.
- **Selection (§92):** through explicit registry configuration rather than hard-coded branching, where practical.

---

# 7. Replacement and Migration (§93–98)

- **Coexistence (§93):** a new algorithm is installable alongside the old one during validation. `CAPABILITY-ARCHITECTURE.md` §13 expects several candidates per category.
- **Comparison (§94):** under the same dataset, input, language, configuration and validation criteria.
- **Champion/challenger (§95):** the active capability compared against challengers where useful.
- **Obsolescence (§96):** considered when evidence shows consistently inferior performance, incompatibility, security problems, excessive maintenance cost or scientific invalidation.
- **No premature deletion (§97):** deprecated code is kept while needed for historical reproduction, comparison, migration or scientific auditing.
- **Migration (§98):** (1) implement replacement; (2) run parallel validation; (3) compare results; (4) document differences; (5) activate replacement; (6) deprecate old capability; (7) retire it when safe.

---

# 8. Compatibility and Refactoring (§99–103)

- **Backward compatibility (§99):** where it provides meaningful scientific or operational value; obsolete interfaces are not kept indefinitely without reason.
- **Public interfaces (§100):** semantic versioning or another documented strategy.
- **Internal interfaces (§101):** may evolve faster but keep clear contracts.
- **Refactoring (§102):** preserves externally observable behavior unless a change is explicitly intended, and is accompanied by tests.
- **Large refactors (§103):** divided into independently verifiable steps, without mixing architecture migration, scientific changes and unrelated cleanup in one opaque change.

---

# 9. Gaps

| ID | Gap | Would normally belong in |
|---|---|---|
| CEP-G1 | The capability registry does not exist and its storage format is undecided (`CAPABILITY-ARCHITECTURE.md` §4 defers this to development) | Implementation tranche |
| CEP-G2 | The versioning strategy for public interfaces (§100) is not selected | Decision before public interfaces exist |
| CEP-G3 | Criteria for "poor", "inferior", "excessive", "inadequate" (§30, §87, §96) are undefined. Any threshold must follow `VALIDATION-GATES.md` §3 | Per-capability validation |
| CEP-G4 | The role of `MONITORED` (§27) and `REMOVED` (`P00` §15) is undefined by the other two enumerations | Reconciliation under `DEC-012` |

No value has been supplied for any of these.

---

# 10. Coverage of the Parent Sections

| Parent sections | Covered in |
|---|---|
| §25–26, §33–35 | §3 |
| §27–32 | §4 |
| §83–87 | §5 |
| §88–92 | §6 |
| §93–98 | §7 |
| §99–103 | §8 |
