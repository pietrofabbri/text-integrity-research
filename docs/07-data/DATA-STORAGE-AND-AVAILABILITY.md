# Data Storage and Availability

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Data governance protocol (Tranche 3 of `DATA-MAP.md` §126)
**Authority:** Data (storage-budget policy). Run-time enforcement is in `docs/04-architecture/DATA-MODEL.md` §6–8.
**Parent:** `docs/07-data/DATA-MAP.md` §41–49, §79, §91–93, §101–104, §114
**Knowledge backlog:** `KB-007` (local storage constraint)
**Research basis:** `R09` addresses local deployment feasibility within this budget; this document does not restate its findings
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-012, DEC-051, DEC-054 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes where data lives, how the storage budget is managed, and what happens when resources are absent. It sets no percentage or alert threshold: `DATA-MAP.md` §44 and §46 defer those. The repository holds no datasets (verified 2026-11-09); storage outside it is not known from the repository.

---

# 2. Recorded Contradictions and Ambiguities — Not Resolved Here

| ID | Subject | Locations | Finding |
|---|---|---|---|
| DSA-C1 | Nature of the 30 GB figure | `DATA-MAP.md` §43, §102; `KB-007` | §43: "target maximum of approximately" 30 GB, an engineering constraint. §102 calls it a "ceiling". `KB-007` is titled a "hard constraint". The figure is approximate in all three. |
| DSA-C2 | What the budget measures | `DATA-MAP.md` §43; `DATA-MODEL.md` §7 | §43 covers the complete local environment. `DATA-MODEL.md` §7 enforces alert states on *loaded*, "not merely on-disk", usage. Whether a single budget covers both is not established. |
| DSA-C3 | Resource states | `DATA-MAP.md` §92; `CAPABILITY-EVOLUTION-POLICY.md` CEP-C4 | `AVAILABLE, OPTIONAL, MISSING, INCOMPATIBLE, DEPRECATED` is a further list. `DATA-MODEL.md` §8 uses it; relation to the other absent-support states is not established. |

---

# 3. Where Data Lives (§41–42, §79)

**GitHub (§41):** source code, documentation, lightweight metadata, small public fixtures, benchmark definitions, scripts and manifests. Large datasets are not automatically committed.

**Large artifacts (§42):** may live outside the repository. The repository then holds identifier, version, checksum, acquisition instructions, provenance, license and expected size.

**Access layers (§79):** raw, normalized, benchmark and experiment access are distinguished, reducing accidental mixing of incompatible representations.

---

# 4. Storage Budget (§43–46, §101–102)

**Budget (§43):** approximately 30 GB for the complete local research/data environment (see DSA-C1, DSA-C2).

**Allocation (§44):** conceptually datasets, models, linguistic resources, caches, experiment artifacts, build artifacts and backups. Exact percentages only after actual requirements are measured.

**Monitoring (§45):** total usage, usage by category, largest artifacts, obsolete artifacts, cache usage, recoverable storage.

**Alerts (§46):** warn before exhaustion; suggested states `NORMAL`, `WARNING`, `CRITICAL`; thresholds configurable.

**Efficiency (§101):** compressed formats where safe, deduplicated and shared resources, manifests instead of duplicates, derived-on-demand artifacts where practical. Reproducibility is not sacrificed solely to minimize storage.

**Approaching the ceiling (§102), in order:** (1) remove regenerable caches; (2) remove duplicate derived artifacts; (3) compress eligible resources; (4) archive rarely used resources; (5) move eligible large public resources outside the local environment; (6) reconsider optional resources. Canonical research evidence is not deleted merely to satisfy the target without documenting the scientific impact.

---

# 5. Cache, Downloads (§47–49)

**Cache (§47):** distinguishable from canonical data, deletable and regenerable. Canonical datasets must not depend on undocumented cache state.

**Downloads (§48):** preferably through reproducible manifests identifying source, version, checksum, expected size and license.

**Verification (§49):** expected type and size, checksum where available, archive safety, provenance. See `SUPPLY-CHAIN-AND-ARTIFACT-SECURITY.md` §4.

---

# 6. Availability (§91–93, §114)

**Offline (§91):** core offline functionality relies only on resources declared locally available. The software must not silently attempt to download missing data.

**Optional resources (§92):** absence produces an explicit state (see DSA-C3).

**Discovery (§93):** the system exposes what is installed and usable, so "supported" is not confused with "currently available".

**Disappearing datasets (§114):** preserve acquisition metadata, citation, version, checksum and historical results. Redistribution still respects the original license.

---

# 7. Backup and Integrity (§103–104)

**Backup (§103):** important metadata and experiment records are backed up separately from large regenerable datasets. The location is undecided (`Q-018`).

**Monitoring (§104):** important artifacts are periodically checked against recorded checksums where practical. Unexpected changes are investigated.

---

# 8. Gaps

| ID | Gap | Would normally belong in |
|---|---|---|
| DSA-G1 | Percentages and alert thresholds (§44, §46) await measurement | After resources are measured |
| DSA-G2 | Location of large artifacts (§42) is undefined | Owner decision |
| DSA-G3 | Whether disk and loaded usage share a budget (DSA-C2) | `DATA-MAP.md` / `DATA-MODEL.md`, by decision |
| DSA-G4 | Monitoring intervals (§45, §104) are undefined | Implementation tranche |

No value has been supplied for any of these.

---

# 9. Coverage of the Parent Sections

| Parent sections | Covered in |
|---|---|
| §41–42, §79 | §3 |
| §43–46, §101–102 | §4 |
| §47–49 | §5 |
| §91–93, §114 | §6 |
| §103–104 | §7 |
