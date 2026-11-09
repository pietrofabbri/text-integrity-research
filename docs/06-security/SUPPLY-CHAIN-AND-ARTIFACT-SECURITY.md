# Supply-Chain and Artifact Security

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Security protocol (Tranche 3 of `SECURITY-MAP.md` §92)
**Authority:** Security. Dependency workflow remains in `docs/08-development/ENGINEERING-STANDARDS.md`; data and model provenance in `docs/07-data/DATA-MAP.md`.
**Parent:** `docs/06-security/SECURITY-MAP.md` §25–33, §51–53, §57–62
**Governance basis:** `P00-project-governance.md` I-003, I-006
**Requirements basis:** `docs/03-scientific-specification/S02-scientific-requirements.md` `REQ-SEC-002`, `REQ-REPRO-003`
**Architectural basis:** `docs/04-architecture/ARCHITECTURE-MAP.md` §49; `EXTERNAL-INTEGRATION-ARCHITECTURE.md` §8; `CAPABILITY-ARCHITECTURE.md` §4
**Research basis:** none specific; no `R-XXXX` applies
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-012, DEC-034, DEC-043, DEC-046, DEC-049 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes how third-party and generated artifacts are treated, and how the repository and its history are protected. It selects no tool, hash algorithm, format or branching model. These are requirements, not guarantees: nothing is implemented (`TRUST-AND-DATA-BOUNDARIES.md` §1).

---

# 2. Recorded Contradictions and Ambiguities — Not Resolved Here

| ID | Subject | Locations | Finding |
|---|---|---|---|
| SCS-C1 | Dependency metadata and pinning | `SECURITY-MAP.md` §25–27; `DEVELOPMENT-MAP.md` §77, §79; `OPERATIONS-MAP.md` §30 | Overlapping, compatible lists (`ENGINEERING-STANDARDS.md` ENG-C3, ENG-C4). Read cumulatively. |
| SCS-C2 | Meaning of "plugin" | `SECURITY-MAP.md` §51–52; `DEC-034` | `DEC-034` scoped "plugin" as a generic extensibility synonym and rejected a distinct plugin mechanism document. §52's rules were written for plugins as separate trust boundaries. **INFERENCE:** §52 applies to any extension that receives permissions of its own, such as an adapter; it does not create a plugin mechanism. |
| SCS-C3 | Capability permissions | `SECURITY-MAP.md` §53, §86; `CAPABILITY-ARCHITECTURE.md` §4 | §86 requires permissions to be defined before `ACTIVE`; the capability record schema has no permissions field. |
| SCS-C4 | Repository content | `SECURITY-MAP.md` §57; `DEC-012` | `_to_delete/` holds two superseded text files kept per `DEC-012`. The repository's other tracked files are Markdown and two Python scripts (verified 2026-11-09). No §57 conflict found. |

---

# 3. Dependencies and Supply Chain (§25–28)

**Every runtime dependency has (§25):** name, version, source, license, purpose, dependency relationship and security status where known. Unnecessary dependencies are avoided.

**Pinning (§26):** important runtime dependencies are version-pinned or constrained according to the project's reproducibility policy, which is not located as a named document (`ENGINEERING-STANDARDS.md` ENG-G2). Uncontrolled floating dependencies are discouraged.

**Updates (§27):** distinguish patch, minor, major and security updates, and trigger appropriate regression testing.

**Supply chain (§28):** downloaded packages, models, datasets, binaries and scripts are untrusted until provenance and intended use have been evaluated. Adding high-risk dependencies normally requires approval (§19).

---

# 4. Artifacts (§29–33)

- **Executable artifacts (§29):** research datasets and model files must not automatically be executable. A trusted source does not grant execution authority.
- **Datasets (§30):** inspected for unexpected file types, malicious payloads, path traversal, decompression bombs, oversized files and unexpected executable content.
- **Models (§31):** models and tokenizer resources are external artifacts. Where possible, prefer formats that do not require arbitrary code execution during loading. Inbound artifacts cross only through the adapter (`EXTERNAL-INTEGRATION-ARCHITECTURE.md` §8).
- **Archives (§32):** processed defensively against path traversal, decompression bombs, unexpected symlinks, excessive extraction size and executable payloads.
- **Temporary files (§33):** controlled directories, predictable lifecycle, cleaned where appropriate, no unnecessary exposure of sensitive text.

---

# 5. Code Execution and Permissions (§51–53)

**Dynamic code (§51):** avoid unnecessary arbitrary eval, dynamic script execution, untrusted plugin execution and runtime code generation. If technically necessary, the capability requires explicit security documentation. Arbitrary code execution is CRITICAL (§21).

**Plugins (§52; see SCS-C2):** treated as separate trust boundaries, declaring permissions, dependencies, filesystem access, network access, data access and lifecycle state.

**Capability permissions (§53; see SCS-C3):** supported where practical, for example `READ_TEXT`, `WRITE_OUTPUT`, `READ_DATASET`, `NETWORK_ACCESS`, `EXTERNAL_SERVICE_ACCESS`, `MODEL_LOAD`, `TEMPORARY_FILES`. Capabilities receive only what they need.

---

# 6. Repository, History and Recovery (§57–62)

- **Repository (§57):** contains no credentials, private documents, confidential text, unnecessary binaries or unverified executable artifacts.
- **Git safety (§58):** version control preserves source and documentation history, configuration changes and scientific decisions. Destructive history rewriting is avoided unless explicitly required. `AGENT-WORK-MODEL.md` §12 records the agent's practice; audit history must not be altered to conceal a change (`P00` §8).
- **Branches (§59):** experimental work is separable from stable work. The branching model "may be defined in development documentation" and is not (SCS-G2).
- **Backup (§60):** recoverable copies of documentation, experiment metadata, benchmark definitions, capability registry and decision records.
- **Hashes (§61):** where practical, for datasets, model files, experiment inputs and outputs, and release artifacts. `REQ-SEC-002` requires mechanisms for detecting unauthorized alteration of scientific evidence.
- **Environment (§62):** operating system assumptions and runtime, dependency, model and dataset versions are documented.

---

# 7. Gaps

| ID | Gap | Would normally belong in |
|---|---|---|
| SCS-G1 | Permissions are absent from the capability record (SCS-C3) | `CAPABILITY-ARCHITECTURE.md`, by decision |
| SCS-G2 | No branching model. Current practice is direct push to `main`. Update: `DEC-057` set the model, and the owner enabled protection of `main` on 2026-11-09 (verified) | Owner decision before implementation |
| SCS-G3 | The backup location is not defined; GitHub is the only remote copy known from the repository | Owner decision |
| SCS-G4 | Hash algorithm and allowed model formats are not selected | Implementation tranche |
| SCS-G5 | What makes a dependency "high-risk" (§19) has no stated criterion beyond "security-sensitive dependency" (§21) | `SECURITY-MAP.md`, by decision |

No value has been supplied for any of these. **Update 2026-11-09:** the branching part of SCS-G2 (protection and SCS-G3 stay open) are decided by `DEC-057`; see `OPEN-QUESTIONS.md`.

---

# 8. Coverage of the Parent Sections

| Parent sections | Covered in |
|---|---|
| §25–28 | §3 |
| §29–33 | §4 |
| §51–53 | §5 |
| §57–62 | §6 |
