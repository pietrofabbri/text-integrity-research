# Data Lifecycle and Change

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Data governance protocol (Tranche 5 of `DATA-MAP.md` §126)
**Authority:** Data (primary for data lifecycle).
**Parent:** `docs/07-data/DATA-MAP.md` §67–72, §87, §90, §94–99, §107–109, §122–123
**Governance basis:** `P00-project-governance.md` I-003
**Requirements basis:** `docs/03-scientific-specification/S02-scientific-requirements.md` `REQ-LIFE-004`
**Research basis:** none specific; no `R-XXXX` applies
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-012, DEC-051, DEC-056 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes how data artifacts age, change, are replaced and are retired while keeping scientific results interpretable. It sets no review interval.

---

# 2. Recorded Contradictions and Ambiguities — Not Resolved Here

| ID | Subject | Locations | Finding |
|---|---|---|---|
| DLC-C1 | Data lifecycle vocabulary | `DATA-MAP.md` §69; `CAPABILITY-EVOLUTION-POLICY.md` CEP-C1 | `DISCOVERED → ACQUIRED → VERIFIED → REGISTERED → PROCESSED → VALIDATED → ACTIVE → ARCHIVED → RETIRED` is a further enumeration, for data rather than capabilities. Deferred per `DEC-012`. |
| DLC-C2 | Removal for storage reasons | `DATA-MAP.md` §70, §102; `P00` I-003 | §70 allows retirement when storage constraints require removal. §102 forbids deleting canonical evidence for the target without documenting impact, and I-003 requires an explicit retention decision for evidence needed for reproducibility. **INFERENCE:** §70 is subject to both. |
| DLC-C3 | Dependency graphs | `DATA-MAP.md` §95; `DEVELOPMENT-MAP.md` §35 | Two compatible descriptions with different nodes (`CAPABILITY-EVOLUTION-POLICY.md` §3). |
| DLC-C4 | Automation limits | `DATA-MAP.md` §107; `DEVELOPMENT-MAP.md` §176 | §107 allows reversible, deterministic, documented, tested maintenance. §176 forbids automatically replacing benchmark datasets or deleting historical results. Both apply. |

---

# 3. Artifacts and Retention (§67–68)

**Experiment artifacts (§67):** input and output identifiers, diffs, measurements, logs, reports. Large redundant artifacts should not consume storage unnecessarily.

**Retention (§68; `REQ-LIFE-004`):** important results remain accessible after a capability is deprecated. Retirement does not automatically justify deleting historical evidence.

---

# 4. Lifecycle, Retirement and Deletion (§69–72, §122)

**Lifecycle (§69):** see DLC-C1.

**Retirement (§70):** when a license expires, source disappears, replacement is superior, benchmark is invalidated, storage constraints require removal (DLC-C2) or security concerns arise. Metadata about the former artifact is preserved.

**Deletion (§71):** documented for important scientific data: what, why, when, who or what authorized it, and whether results are affected.

**Migration (§72):** to a new format preserves identifiers, versions, provenance, checksums where meaningful and semantic interpretation.

**Review (§122):** large resources are periodically reviewed for continued scientific value, replacement availability, storage cost, license changes, security issues and reproducibility value.

---

# 5. Change and Dependencies (§87, §90, §94–95, §98–99)

**Impact (§87):** when a dataset changes, determine effects on benchmarks, baselines, experiments, scientific claims, certification, storage and licensing.

**Reproducibility (§90):** a new environment can reconstruct required public datasets from manifests where the source remains available. If impossible, the limitation is recorded.

**Registry (§94):** every capability depending on a dataset or model declares it, so the project can determine what breaks on removal, what needs retesting after an update and which capabilities depend on a deprecated resource.

**Graph (§95):** dataset → preprocessor → resource → capability → experiment → result. Changes propagate through it during validation.

**Change queue (§98):** material data changes enter the documentation change queue: new benchmark, changed corpus, new model, changed license, changed preprocessing, retired dataset.

**Research registry (§99):** references all major datasets, preventing duplicate acquisition of substantially identical resources without scientific justification.

---

# 6. Obsolescence and Replacement (§96–97)

A resource may become obsolete because better data exists, its source disappears, licensing or methodology changes, language coverage improves or security concerns emerge. Obsolete resources are deprecated before retirement when practical (§96).

A deprecated resource identifies a replacement where one exists, and the replacement does not automatically inherit the old resource's version or scientific properties (§97).

---

# 7. Maintenance and Preservation (§107–109, §123)

**Automation (§107):** when reversible, deterministic, documented and tested, for example regenerating caches, validating manifests, checking checksums and producing storage reports. See DLC-C4.

**After a maintenance batch (§108):** expected files exist; unexpected files are absent; checksums correct; manifests valid; storage within limits; dependent tests pass.

**Preservation (§109):** when a capability is retired, preserve at least dataset identifier and version, experiment identifier, software version and result metadata.

**Lifecycle automation (§123), where practical:** manifest checks, storage accounting, checksum checks, stale-cache detection, dependency impact detection.

---

# 8. Gaps

| ID | Gap | Would normally belong in |
|---|---|---|
| DLC-G1 | Review intervals (§122) are undefined | Implementation tranche |
| DLC-G2 | Who may authorize deletion of important data (§71) is not named | Owner decision |
| DLC-G3 | Which results are "important" (§68, §71) has no stated criterion | `DATA-MAP.md`, by decision |

No value has been supplied for any of these.

---

# 9. Coverage of the Parent Sections

| Parent sections | Covered in |
|---|---|
| §67–68 | §3 |
| §69–72, §122 | §4 |
| §87, §90, §94–95, §98–99 | §5 |
| §96–97 | §6 |
| §107–109, §123 | §7 |
