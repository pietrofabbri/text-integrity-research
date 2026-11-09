# Data Governance and Licensing

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Data governance protocol (Tranche 2 of `DATA-MAP.md` §126)
**Authority:** Data. Security boundaries remain with `docs/06-security/SECURITY-MAP.md`.
**Parent:** `docs/07-data/DATA-MAP.md` §34–40, §100, §105–106, §110–111, §115, §118–121, §124–125
**Research basis:** `Q-007` and its evidence (`R08` §69.1; `R-0016`, `R-0020`, `R-0049`, `R-0088`, `R-0099`), summarized in §5
**Related questions:** `Q-007`, `Q-019`
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-012, DEC-051, DEC-053 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes how data is classified for privacy and transfer, how licenses are recorded, and how data is acquired and documented.

**It gives no legal advice and draws no legal conclusion.** `DATA-MAP.md` §34 says the exact legal classification depends on the applicable jurisdiction and dataset license. Whether a given dataset may lawfully be used or distributed remains a matter for `Q-007` and appropriate legal judgment. Licensing uncertainty requiring human judgment is a stop condition (`P00-project-governance.md` §7).

---

# 2. Recorded Contradictions and Ambiguities — Not Resolved Here

| ID | Subject | Locations | Finding |
|---|---|---|---|
| DGL-C1 | Overlapping transfer terms | `DATA-MAP.md` §34, §35 | `PROHIBITED_FOR_EXTERNAL_TRANSFER` is a privacy class and `PROHIBITED` a transfer state. How a dataset's class determines its state is not stated. |
| DGL-C2 | Data-card states | `DATA-MAP.md` §111; `CAPABILITY-EVOLUTION-POLICY.md` CEP-C1 | `DRAFT → REVIEWED → ACTIVE → DEPRECATED → RETIRED` is a further lifecycle enumeration. Whether it is the same concept is not established; deferred per `DEC-012`. |
| DGL-C3 | Datasets and user text | `DATA-MAP.md` §35; `Q-019` | Transfer eligibility is declared for datasets only (`TRUST-AND-DATA-BOUNDARIES.md` TDB-C4). |

---

# 3. Privacy and Transfer (§34–37)

**Classes (§34, recommended):** `PUBLIC`, `RESEARCH_RESTRICTED`, `PRIVATE`, `SENSITIVE`, `PROHIBITED_FOR_EXTERNAL_TRANSFER`.

**Transfer eligibility (§35):** every dataset declares `ALLOWED`, `CONDITIONALLY_ALLOWED`, `LOCAL_ONLY`, `PROHIBITED` or `UNKNOWN`. `UNKNOWN` is treated conservatively.

**Personal information (§36):** minimized and handled according to applicable law and license restrictions; not collected when not scientifically necessary.

**Sensitive text (§37):** not placed in Git repositories, public benchmark packages, issue trackers, ordinary logs or public documentation.

---

# 4. Licensing (§38–40)

**States (§38):** every externally sourced dataset has a recorded license or usage status: `OPEN`, `RESEARCH_ONLY`, `COMMERCIAL_RESTRICTED`, `ATTRIBUTION_REQUIRED`, `DERIVATIVE_RESTRICTIONS`, `UNKNOWN` or `PROHIBITED`.

**Evidence (§39):** where possible, license name, source URL, source version, acquisition date, license text or reference, relevant restrictions.

**Uncertainty (§40):** unknown status is never silently interpreted as permission. The dataset stays restricted until clarified.

---

# 5. Current Evidence on Dataset Licensing (from `Q-007`)

Recorded in `OPEN-QUESTIONS.md` Q-007 as of 2026-08-24. It does not resolve the question.

| Dataset | As recorded | Caveat recorded in Q-007 |
|---|---|---|
| RAID | MIT | Pending a legal read of source-corpus chains |
| MULTITuDE, MULTITuDE v2 | CC-BY-4.0 | Same |
| HC3 | CC-BY-SA-4.0 | Inherits the stricter of its own license or any source dataset's license |
| ARB | Apache-2.0 | Disclaims responsibility for its source corpora's terms, some undeclared |
| M4, DetectRL | No license stated anywhere checked | Under §40, restricted until clarified |
| TOEFL-essay corpus (ETS/LDC2014T06) | Gated behind a paid LDC license | Not freely redistributable |

Principle recorded there: a benchmark's own top-line license is not sufficient evidence of distributability without checking its source-corpus chain.

---

# 6. Boundaries (§105–106)

Data permissions follow the security map. The data layer must not independently grant network access, arbitrary code execution or unrestricted filesystem access (§105).

The agent may modify data manifests, ingestion scripts and data documentation, but must not silently replace datasets, alter benchmark membership, change labels, delete scientific evidence or bypass licensing checks. Such changes need explicit documentation and appropriate validation (§106).

---

# 7. Documentation and Citation (§110–111, §115)

**Data card (§110):** every major dataset eventually has one, or equivalent: purpose, provenance, license, composition, languages, preprocessing, known limitations, storage requirements, scientific uses. States are in §111 (see DGL-C2).

**Citation (§115):** scientific use of external datasets retains attribution and citation information, in the manifest where practical.

---

# 8. Acquisition (§100, §118–121)

**Current state (§118):** the project has a data architecture and no requirement that all datasets be acquired before the software architecture is final. Acquisition proceeds incrementally.

**Priority (§100):** scientific relevance; provenance quality; licensing clarity; multilingual coverage; reproducibility; storage efficiency; maintenance burden.

**Strategy (§119):** resources answering the highest-value scientific questions first. Large datasets are not downloaded merely because they are available.

**For every proposed large dataset (§120):** research question, expected benefit, estimated storage, licensing status, processing cost, alternatives.

**No hoarding (§121):** every large resource has an owner within the research architecture: a capability, benchmark or research question.

---

# 9. Governing Principles (§124–125)

Data decisions are explicit, reversible where possible and scientifically traceable (§124). Data is treated as versioned scientific dependencies: traceable data → reproducible experiments → interpretable results → maintainable software. A dataset that cannot be identified, reproduced, licensed, validated or properly interpreted must not silently become foundational (§125).

---

# 10. Gaps

| ID | Gap | Would normally belong in |
|---|---|---|
| DGL-G1 | Distributability of each dataset, including the source-corpus chains (`Q-007`) | Human and legal judgment |
| DGL-G2 | The applicable jurisdiction (§34) is not stated | Owner decision |
| DGL-G3 | How privacy classes map to transfer states (DGL-C1) | `DATA-MAP.md`, by decision |
| DGL-G4 | What makes a dataset "large" or "major" (§110, §120–121) has no stated criterion | `DATA-MAP.md`, by decision |

No value has been supplied for any of these.

---

# 11. Coverage of the Parent Sections

| Parent sections | Covered in |
|---|---|
| §34–37 | §3 |
| §38–40 | §4 |
| §105–106 | §6 |
| §110–111, §115 | §7 |
| §100, §118–121 | §8 |
| §124–125 | §9 |
