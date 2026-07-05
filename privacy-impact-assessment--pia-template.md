# PIA / DPIA Document Template

Populate each section from the seven-phase workflow. Sections marked **[REQUIRED]** must be completed before the assessment is considered final. Sections marked **[IF APPLICABLE]** are completed when the relevant condition is met.

Delete instructional text (italics) before submitting to a regulator or storing as a compliance record.

> **Source of truth:** statutory anchors in this template (GDPR Arts. 6/9/35, Law 25 Art. 63.5, PIPL Art. 55; HIPAA/AI Act as sectoral overlays) derive from `regulatory-taxonomy.md` records, axis A12. Reconciled 2026-07-04; log: `.fable/reconciliation-log.md`. On conflict, the record wins (see `privacy-impact-assessment.md` §Regulatory Source of Truth).

---

# PRIVACY IMPACT ASSESSMENT

| Field | Value |
|---|---|
| **Assessment title** | [System / feature / processing activity name] |
| **Version** | [1.0 / date] |
| **Status** | ☐ Draft  ☐ Under review  ☐ Approved  ☐ Requires DPA consultation |
| **Controller** | [Organisation legal name] |
| **DPO / Privacy lead** | [Name, role — or "Not appointed: [basis]"] |
| **Assessment author** | [Name, role, date] |
| **Primary regulatory basis** | ☐ GDPR Art. 35  ☐ Quebec Law 25 Art. 63.5  ☐ HIPAA § 164.308(a)(1)  ☐ PIPL Art. 55  ☐ EU AI Act Art. 9  ☐ Voluntary |

---

## Executive Summary **[REQUIRED]**

*3–5 sentences: what is being assessed, what data is involved, key risks found, overall residual risk level after mitigations, and key mitigations adopted. Written for a non-technical reader.*

[Executive summary text]

**Overall residual risk level:** ☐ CRITICAL  ☐ HIGH  ☐ MEDIUM  ☐ LOW

---

## 1. Scope and Context **[REQUIRED]**

### 1.1 Processing activity description

*Describe what the system, feature, or process does. What personal data does it touch? Who does it affect?*

[Description]

### 1.2 Stated purpose

*Why does this processing activity exist? What legitimate objective does it serve? Be specific — vague purposes ("improving user experience") fail the necessity test.*

[Purpose statement]

### 1.3 Legal basis for processing **[REQUIRED]**

*Select the applicable lawful basis and provide specifics.*

**GDPR Art. 6 lawful basis (if applicable):**
- ☐ 6(1)(a) — Consent: [describe consent mechanism]
- ☐ 6(1)(b) — Contract performance: [describe contractual necessity]
- ☐ 6(1)(c) — Legal obligation: [cite specific legal obligation]
- ☐ 6(1)(d) — Vital interests
- ☐ 6(1)(e) — Public task
- ☐ 6(1)(f) — Legitimate interests: [complete LIA]

**Special categories (GDPR Art. 9) — if applicable:**
- ☐ Art. 9(2)(a) — Explicit consent
- ☐ Art. 9(2)(b) — Employment / social protection law
- ☐ Art. 9(2)(h) — Health care / treatment
- ☐ Art. 9(2)(j) — Scientific / statistical research
- ☐ Other: [specify]

**HIPAA (if applicable):** ☐ Treatment  ☐ Payment  ☐ Operations  ☐ Other: [specify]

**PIPEDA (if applicable):** ☐ Consent (Clause 4.3)  ☐ Other: [specify]

### 1.4 Necessity determination **[REQUIRED]**

*Confirm whether a DPIA is mandatory or voluntary. Complete the trigger checklist from `references/dpia-triggers.md`.*

| Trigger | Applies? | Basis |
|---|---|---|
| GDPR Art. 35(3)(a) — Systematic automated profiling | ☐ Y / ☐ N | |
| GDPR Art. 35(3)(b) — Large-scale special category data | ☐ Y / ☐ N | |
| GDPR Art. 35(3)(c) — Systematic public monitoring | ☐ Y / ☐ N | |
| EDPB 9 criteria — count met | [_] of 9 | Threshold: ≥2 |
| Quebec Law 25 Art. 63.5 | ☐ Y / ☐ N | |
| HIPAA § 164.308(a)(1) risk analysis | ☐ Y / ☐ N | |
| PIPL Art. 55 | ☐ Y / ☐ N | |
| EU AI Act Art. 9 (high-risk AI) | ☐ Y / ☐ N | |

**Conclusion:** DPIA is ☐ MANDATORY / ☐ STRONGLY ADVISED / ☐ VOLUNTARY

**Statutory basis for conclusion:** [cite specific provision]

### 1.5 Scope boundary

*Define explicitly what is IN scope and OUT of scope for this assessment.*

**In scope:** [list systems, features, data flows, geographies]

**Out of scope:** [list what this assessment does NOT cover, and why]

### 1.6 Stakeholders

| Role | Name / Team | Involvement |
|---|---|---|
| Controller | | Decision authority |
| Processor(s) | | [list all processors and sub-processors] |
| Data subjects | | [categories of affected individuals] |
| DPO | | Review and advice |
| Legal | | Legal basis confirmation |
| Technical lead | | Implementation review |
| Security | | Security control confirmation |

---

## 2. Processing Description **[REQUIRED]**

### 2.1 Data flow map

```
Collection:    [How PI is collected — form, API, sensor, inference, purchase]
    Source:    [Direct from data subject / third party / generated internally]
    ↓
Storage:       [Where PI is stored — database, cloud provider, region]
    Format:    [Structured / unstructured / encrypted / pseudonymized]
    ↓
Processing:    [What operations — analysis, profiling, sharing, display, training]
    ↓
Retention:     [How long PI is retained — specific period or trigger event]
    ↓
Disposal:      [How PI is destroyed — hard delete / crypto-erase / shredding]

Third parties: [All processors, sub-processors, and recipients with role]
Cross-border:  [Any transfer outside jurisdiction; transfer mechanism used]
```

### 2.2 Personal data inventory **[REQUIRED]**

*List every personal data field collected, generated, or processed. Import from `data-minimization` skill audit if available.*

| Field name | Category | Sensitivity tier | Source | Retention | Encrypted at rest | Encrypted in transit | Notes |
|---|---|---|---|---|---|---|---|
| [field] | [PII / Quasi-ID / Health / Financial / Behavioral / Inferred] | T1–T5 | [Direct / Third-party / Inferred] | [period] | ☐ Y / ☐ N | ☐ Y / ☐ N | |

**Inferred / derived data:** *List any fields generated by the system from other data (ML outputs, risk scores, behavioral profiles). Apply the same classification.*

| Derived field | Input fields | Inference method | Sensitivity tier | Retention |
|---|---|---|---|---|
| [field] | [source fields] | [model / rule / heuristic] | T1–T5 | [period] |

### 2.3 Necessity and proportionality assessment **[REQUIRED]**

*For each field, confirm it is necessary and proportionate to the stated purpose.*

| Field | Necessary? | Proportionate? | If NO — action required |
|---|---|---|---|
| [field] | ☐ Y / ☐ N | ☐ Y / ☐ N | [DROP / HASH / TRUNCATE / etc.] |

**Fields failing necessity or proportionality:** [count]

*These are findings requiring mitigation before the assessment can be approved.*

---

## 3. Risk Register **[REQUIRED]**

*Document all identified privacy risks. Use the twelve risk categories from the PIA skill as a checklist. Score inherent risk (before mitigations) on a 1–5 × 1–5 likelihood × severity scale.*

| Risk ID | Risk description | Category | Source / threat actor | Likelihood (1–5) | Severity (1–5) | Inherent risk score | Immutable? |
|---|---|---|---|---|---|---|---|
| R-001 | | | | | | | ☐ Y / ☐ N |
| R-002 | | | | | | | ☐ Y / ☐ N |

**Risk categories checklist:**
- ☐ Unauthorised access (breach)
- ☐ Unauthorised modification (integrity attack)
- ☐ Unlawful processing (no legal basis / purpose mismatch)
- ☐ Excessive collection
- ☐ Excessive retention
- ☐ Re-identification (quasi-identifier combination)
- ☐ Inference (sensitive attribute derived from non-sensitive data)
- ☐ Cross-border transfer risk
- ☐ Immutability risk (blockchain / append-only)
- ☐ Third-party / processor exposure
- ☐ Data subject rights obstruction
- ☐ Profiling / automated decision-making

**Inherent risk score interpretation:**
- 20–25: CRITICAL
- 12–19: HIGH
- 6–11: MEDIUM
- 1–5: LOW

---

## 4. Mitigation Register **[REQUIRED]**

*For each HIGH and CRITICAL risk, document the mitigations adopted.*

| Mitigation ID | Addresses risk(s) | Mitigation description | Type | Effort | Implemented? | Residual risk |
|---|---|---|---|---|---|---|
| M-001 | R-00x | | M1 (prevent) / M2 (detect) / M3 (respond) | LOW / MED / HIGH | ☐ Y / ☐ N / ☐ Planned [date] | CRITICAL / HIGH / MED / LOW |

**Residual risk summary after all mitigations:**

| Risk ID | Inherent risk | Residual risk | Change |
|---|---|---|---|
| R-001 | | | |

### 4.1 Prior DPA consultation **[IF APPLICABLE]**

*Complete if any residual risk remains HIGH or CRITICAL after all mitigations. GDPR Art. 36 requires prior consultation with the supervisory authority.*

**Residual risks remaining HIGH or CRITICAL:** [count]

**Prior consultation required (GDPR Art. 36(1)):** ☐ YES / ☐ NO

**If YES:**
- Supervisory authority to consult: [national DPA — e.g. ICO, CNIL, DPC]
- Consultation initiated: [date]
- Consultation outcome: [pending / received — summarise]
- Processing may not begin until consultation is complete and any conditions are met.

---

## 5. Data Subject Rights Assessment **[REQUIRED]**

*Assess whether the system enables data subjects to exercise their legal rights.*

| Right | Statutory basis | Mechanism available | Status | Gap / action |
|---|---|---|---|---|
| Right to access | GDPR Art. 15 / PIPEDA Cl. 4.9 | [describe] | ☐ Met / ☐ Gap | |
| Right to rectification | GDPR Art. 16 / PIPEDA Cl. 4.9 | [describe] | ☐ Met / ☐ Gap | |
| Right to erasure | GDPR Art. 17 / CCPA § 1798.105 | [describe] | ☐ Met / ☐ Gap | |
| Right to restriction | GDPR Art. 18 | [describe] | ☐ Met / ☐ Gap | N/A if not GDPR |
| Right to portability | GDPR Art. 20 / CCPA § 1798.100 | [describe] | ☐ Met / ☐ Gap | |
| Right to object | GDPR Art. 21 | [describe] | ☐ Met / ☐ Gap | N/A if not GDPR |
| Rights re: automated decisions | GDPR Art. 22 | [describe] | ☐ Met / ☐ N/A | |
| Right to de-indexing | Quebec Law 25 Art. 28.1 | [describe] | ☐ Met / ☐ N/A | |

**Rights gaps requiring remediation before launch:** [count]

### 5.1 Immutability conflict **[IF APPLICABLE]**

*Complete if any personal data is stored in immutable form (blockchain, append-only log, archival system where deletion is technically impossible).*

| Field | Storage mechanism | Conflict with right | Mitigation adopted |
|---|---|---|---|
| [field] | [blockchain / append-only / archive] | Right to erasure (Art. 17) | ☐ Encrypt before write (key deletion as practical erasure) ☐ Off-chain data, on-chain hash only ☐ No PI on-chain |

**Legal position adopted:** [encryption-as-erasure / other — cite basis and document that local DPA has been consulted if relying on this position]

---

## 6. Stakeholder Sign-off **[REQUIRED]**

| Role | Name | Date | Outcome |
|---|---|---|---|
| Assessment author | | | Submitted for review |
| DPO / Privacy lead | | | ☐ Approved ☐ Approved with conditions ☐ Not approved — see comments |
| Legal | | | ☐ Reviewed ☐ Not required |
| Technical lead | | | ☐ Confirmed implementation ☐ Pending |
| Security | | | ☐ Confirmed controls ☐ Pending |
| Board / senior management notified | | | ☐ Yes ☐ No — basis: |

**DPO / Privacy lead comments:**
[Comments, conditions, or required follow-up actions]

### 6.1 Data subject consultation **[IF APPLICABLE]**

*GDPR Art. 35(9) requires seeking the views of data subjects or their representatives where appropriate.*

**Decision to consult data subjects:** ☐ YES — [describe process and outcome]  ☐ NO — Basis: [explain why consultation was not appropriate or practicable]

---

## 7. Review Schedule **[REQUIRED]**

**Next scheduled review date:** [date — recommend: 12 months for HIGH residual risk; 24 months for MEDIUM; on material change for any risk level]

**Material change triggers requiring reassessment:**
- New processing purpose
- New data categories
- New technology or system component
- Change in processor or third-party recipients
- Change in applicable law or DPA guidance
- Security incident or near-miss involving this system
- New DPA enforcement decision or guidance in relevant area

### 7.1 Review log

| Date | Trigger | Reviewer | Summary of changes |
|---|---|---|---|
| [date] | Initial assessment | [name] | First version |
| | | | |

---

## Appendix A: Regulatory Basis Table

| Requirement | Applicable regulation | Specific provision | How met |
|---|---|---|---|
| Data minimisation | GDPR | Art. 5(1)(c) | [reference to inventory and necessity assessment] |
| Privacy by design | GDPR | Art. 25(1) | [reference to architectural decisions] |
| Storage limitation | GDPR | Art. 5(1)(e) | [reference to retention schedule in inventory] |
| Security | GDPR | Art. 5(1)(f) | [reference to mitigation register] |
| Limiting collection | PIPEDA | Clause 4.4 | [if applicable] |
| Safeguards | PIPEDA | Clause 4.7 | [if applicable] |
| Risk analysis | HIPAA | § 164.308(a)(1)(ii)(A) | [if applicable] |
| Minimum necessary | HIPAA | § 164.502(b) | [if applicable] |
| Data minimisation | CCPA/CPRA | § 1798.100(a)(3) | [if applicable] |
| Necessity principle | LGPD | Art. 6(III) | [if applicable] |
| Minimum necessary | PIPL | Art. 6 | [if applicable] |
| Data minimisation | Quebec Law 25 | Art. 9 / PPIPS | [if applicable] |
| Training data | EU AI Act | Art. 10(3) | [if applicable — high-risk AI systems] |

---

## Appendix B: Linked Assessments

| Assessment | Date | Link / reference |
|---|---|---|
| Data minimization audit | | [file reference or tool output] |
| Threat model | | [file reference or tool output] |
| OPSEC review | | [file reference or tool output] |
| Previous PIA (if update) | | [file reference] |

---

## Appendix C: Glossary

| Term | Definition |
|---|---|
| Controller | Entity that determines purposes and means of processing |
| Processor | Entity processing PI on behalf of the controller |
| Data subject | Identified or identifiable natural person whose PI is processed |
| Special category data | PI under GDPR Art. 9 (health, biometric, racial origin, etc.) |
| Inherent risk | Risk level before any mitigations are applied |
| Residual risk | Risk level remaining after all mitigations are applied |
| T1 asset | Critical sensitivity — irreversible harm on exposure |
| PHI | Protected Health Information (HIPAA) |
| ePHI | Electronic PHI |
| DPA | Data Protection Authority (national GDPR enforcement body) |
| DPO | Data Protection Officer |
| LIA | Legitimate Interests Assessment (GDPR Art. 6(1)(f) basis documentation) |
