# Documentation and Maintenance Policy

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Development process protocol (Tranche 5 of `DEVELOPMENT-MAP.md` §202)
**Authority:** Development (documentation and maintenance workflow). Governance remains with `docs/01-governance/P00-project-governance.md`; runtime maintenance with `docs/09-operations/OPERATIONS-MAP.md`.
**Parent:** `docs/08-development/DEVELOPMENT-MAP.md` §36–45, §110–114, §133–158, §174–186
**Governance basis:** `P00-project-governance.md` §16–17, §26–27, §29, I-003, I-007
**Requirements basis:** `docs/03-scientific-specification/S02-scientific-requirements.md` `REQ-DOC-001`–`REQ-DOC-004`, `REQ-LIFE-004`
**Knowledge backlog:** `KB-004`, `KB-005` (both INCORPORATED; this document is consistent with their incorporation notes and does not reopen them)
**Research basis:** none specific; no `R-XXXX` applies
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-006, DEC-010, DEC-012, DEC-040, DEC-041, DEC-045 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes how knowledge, debt, change propagation, maintenance and historical preservation are handled during development. It sets no numeric value, schedule or metric target.

---

# 2. Recorded Contradictions — Not Resolved Here

| ID | Subject | Locations | Finding |
|---|---|---|---|
| DMP-C1 | Order of scientific change propagation | `DEVELOPMENT-MAP.md` §153; `P00` §16, §26 | §153: research → specification → architecture → implementation → validation → certification. `P00` §16 places validation before implementation and has no architecture step. `P00` §26 is a third sequence. **`P00` is higher in authority on governance, but this document does not decide whether the sequences describe the same process.** |
| DMP-C2 | Where a new idea is recorded | `DEVELOPMENT-MAP.md` §39, §137, §138; `PROJECT-MAP.md` §33 | §138 names the knowledge backlog; §137 "the appropriate project registry"; `PROJECT-MAP.md` §33 the documentation change queue. **INFERENCE:** research ideas and improvements go to the backlog, cross-document updates to the queue, per the §39 and §38 definitions. |
| DMP-C3 | Reading order for a new session | `DEVELOPMENT-MAP.md` §134; `START-HERE.md` §7 | Two different orders. §134 includes the README, which is empty (verified 2026-11-09), and omits `P00` and `NO-INVENTION-RULES.md`. **INFERENCE:** read the union, as `AGENT-WORK-MODEL.md` §2 does for lists. |
| DMP-C4 | Change queue trigger | `DEVELOPMENT-MAP.md` §37, §38 | Not a contradiction but a sequence: update in the same batch where possible (§37), otherwise queue (§38). Recorded because §37's "must not be intentionally accumulated" limits use of §38. |

---

# 3. Impact Analysis and Synchronization (§36–38, §44–45)

Before a material change, determine direct and indirect dependencies, and affected tests, documentation, benchmarks and security (§36; `P00` §17; `KB-005`). Substantive changes to scientific requirements trigger impact assessment of dependent documentation (`REQ-DOC-002`).

Architecture changes update the relevant documentation in the same batch, and documentation debt is not intentionally accumulated (§37; `DEC-006`). A documentation change is not complete until the relevant consistency checks pass (`P00` I-007).

If a complete update cannot be made at once, an entry goes in `DOCUMENTATION-CHANGE-QUEUE.md` identifying affected document, reason, required update, implementation dependency and priority (§38).

The queue is checked at the beginning and end of significant batches (§44).

**End-of-batch sweep (§45):** did the work change architecture, security, data requirements or validation; introduce a new assumption; or invalidate an existing document? If so, update or queue.

---

# 4. Project Registers (§39–43, §136)

| Content | Register | Section |
|---|---|---|
| Research ideas not yet ready for implementation | `KNOWLEDGE-BACKLOG.md` | §39 |
| Unresolved decisions (`REQ-DOC-004` for scientific questions) | `OPEN-QUESTIONS.md` | §40 |
| Material decisions | `DECISION-LOG.md` | §41 |
| Assumptions; an invalid one is updated, not silently replaced | `ASSUMPTION-REGISTRY.md` | §42 |
| External research sources and evidence, recorded before justifying normative changes (`REQ-DOC-003`) | `RESEARCH-REGISTRY.md` | §43 |

An important idea arising in development must become documentation, a decision, an assumption, an open question, a backlog item or a queue entry (§136; `DEC-010`).

---

# 5. Debt and Metrics (§110–114)

- **Metrics (§110):** useful ones include test pass rate, regression count, unresolved issues, dependency age, documentation debt, capability coverage and validation coverage. Metrics must not become targets that encourage gaming.
- **Technical debt (§111):** recorded with description, impact, reason, priority and possible resolution.
- **Documentation debt (§112):** recorded in the change queue.
- **Scientific debt (§113):** recorded separately from ordinary technical debt.
- **Security debt (§114):** not hidden in generic technical debt; it stays visible through the security process.

---

# 6. Onboarding and Context (§133–135)

- **Onboarding document (§133):** should eventually point to project map, architecture, development rules, research registry, validation, security and data. `START-HERE.md` serves a similar function. **INFERENCE:** it partly fulfils §133, and should point to this area's sub-documents.
- **Before a substantial task (§134):** README, `PROJECT-MAP.md`, relevant MAP, relevant specification, decision log, assumption registry, open questions, change queue. See DMP-C3.
- **Context (§135):** conversation history is not the sole source of requirements; repository documentation is the durable source.

---

# 7. New Ideas and Scope (§137–139)

An idea outside the immediate task is not silently implemented. Determine whether it is required, record it, and continue the approved task (§137). Improvements are recorded rather than discarded (§138). Recording an idea does not authorize implementation (§139). See DMP-C2.

---

# 8. Documentation Structure and Revision (§140–142)

- **Layering (§140):** project map → macro map → detailed specification → implementation → validation.
- **Conflicts (§141):** identified and recorded, never settled by a convenient interpretation. `DOCUMENT-AUTHORITY-MATRIX.md` gives the procedure.
- **Revision (§142):** material revisions preserve history and rationale.
- **Traceability:** every normative scientific requirement is traceable to its source objective or research evidence (`REQ-DOC-001`).

---

# 9. Designing for Change (§143–148)

- **Future research (§143):** a new paper may invalidate an algorithm, assumption, detector model, language strategy or validation criterion, and the architecture must allow replacement.
- **New detectors (§144):** added as new capabilities or adapters, not a rewrite of the core.
- **New watermark research (§145):** new analytical modules without invalidating unrelated infrastructure.
- **Languages (§146):** through modular resources and capability definitions (`CAPABILITY-EVOLUTION-POLICY.md` §5).
- **Feature removal (§147):** dependency analysis, regression testing, documentation updates, migration where required.
- **Flags (§148):** must not become permanent technical debt; retired flags are eventually removed.

New evidence does not by itself change production behavior (`P00` §16, §26).

---

# 10. Maintenance (§149–152, §174–179)

Maintenance is continuous engineering (§149).

**Triggers (§150):** new research, detector or watermark methodology; dependency vulnerability; dataset change; language performance change; operating-system change; security incident.

**Updates (§151):** isolated changes, compatibility testing, rollback, explicit versioning, automatic regression checks.

**Obsolete knowledge (§152):** identify affected components; update the assumption registry; identify affected experiments; update documentation; implement replacement; revalidate.

**Delegation (§174):** routine maintenance may be delegated to the agent when the rule is documented, validation is automated, rollback is possible and no major architectural decision is required. **INFERENCE:** automated validation does not exist yet (`TEST-AND-VERIFICATION-POLICY.md` TVP-G3), so this delegation is not yet available for software. `OPERATIONS-MAP.md` §179 keeps operational changes affecting runtime security or scientific validity under the approval boundary.

**Scheduled inspection (§175):** future automation may inspect dependency updates, security advisories, obsolete capabilities, documentation inconsistencies, storage usage and broken external resources.

**Limits (§176):** automated maintenance must not automatically change scientific acceptance criteria, delete historical results, replace benchmark datasets, enable network access or remove security controls.

**Major upgrades (§177):** a compatibility branch or equivalent, regression tests, inspection of changed behavior, evaluation of scientific impact.

**Failed updates (§178):** (1) identify affected component; (2) restore previous version; (3) preserve failure evidence; (4) create an issue or backlog entry; (5) investigate replacement.

**After maintenance (§179):** previous scientific results are not silently invalidated. If behavior changes, the software version distinguishes it.

---

# 11. Change Propagation (§153–158)

| Change | Chain | Section |
|---|---|---|
| Scientific | Research → Specification → Architecture → Implementation → Validation → Certification (see DMP-C1) | §153 |
| Architecture | Architecture → Implementation → Tests → Security → Operations → Documentation | §154 |
| Data | Data → Capability → Experiment → Validation → Certification | §155 |
| Security | Security → Architecture → Implementation → Tests → Operations → Documentation | §156 |
| Validation criteria | Validation → Tests → Capabilities → Certification → Reporting | §157 |

The process must not update only the code (§153). No major implementation is complete until its relevant dependency chain has been checked (§158).

---

# 12. Reproducibility, Archives and Release Notes (§180–186)

- **Experiment identity (§180):** at least software version, capability versions, dataset versions, model/resource versions and configuration. `STATISTICAL-VALIDATION-METHODOLOGY.md` §7 defines the Minimum Experiment Record.
- **Reproduction (§181):** the software environment of important historical experiments can be reconstructed.
- **Historical compatibility (§182):** a compatibility path when practical.
- **Preservation (§183):** historical implementations are archived rather than casually erased (`P00` I-003; `REQ-LIFE-004`; `DATA-MAP.md` §68).
- **Code archive (§184):** version, reason for retirement, replacement, compatibility status.
- **Documentation archive (§185):** retired capabilities retain relevant documentation.
- **Release notes (§186):** new, changed, deprecated and retired capabilities; dependency, validation and security changes.

---

# 13. Gaps

| ID | Gap | Would normally belong in |
|---|---|---|
| DMP-G1 | The repeatable documentation review of `PROJECT-MAP.md` §32 was to be "defined later in the development and governance documentation". No mechanism is defined yet; this document defines none | Implementation tranche (with `AGENT-WORK-MODEL.md` AWM-G3) |
| DMP-G2 | No technical-debt register exists (§111) | Decision when implementation begins |
| DMP-G3 | The README is empty, though §134 lists it first | Owner decision |
| DMP-G4 | Which experiments are "important" (§181) and when compatibility is "practical" (§182) have no stated criterion | Per-capability specification |
| DMP-G5 | Schedules for §175 are not defined | Future automation |

No value has been supplied for any of these. **Update 2026-11-09:** DMP-G3 are decided by `DEC-057`; see `OPEN-QUESTIONS.md`.

---

# 14. Coverage of the Parent Sections

| Parent sections | Covered in |
|---|---|
| §36–38, §44–45 | §3 |
| §39–43, §136 | §4 |
| §110–114 | §5 |
| §133–135 | §6 |
| §137–139 | §7 |
| §140–142 | §8 |
| §143–148 | §9 |
| §149–152, §174–179 | §10 |
| §153–158 | §11 |
| §180–186 | §12 |
