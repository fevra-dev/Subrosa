---
name: privacy-impact-assessment
description: Conducts structured Privacy Impact Assessments (PIA) and Data Protection Impact Assessments (DPIA) in compliance with GDPR Art. 35, Quebec Law 25 Art. 63.5, HIPAA § 164.308(a)(1) risk analysis, and analogous requirements across PIPEDA, LGPD, PIPL, PDPA, and the EU AI Act. Use when user says "PIA", "DPIA", "privacy impact assessment", "data protection impact assessment", "risk analysis for this system", "I need to document privacy risks", "compliance documentation for a new project", "is a DPIA required", "assess privacy risks before launch", or when starting a new product, feature, AI system, or processing activity that involves personal data. Also triggers when user is responding to a regulator, auditor, or client requesting privacy documentation, or when another skill (data-minimization, threat-model-privacy) has produced findings that require formal documentation. Produces a complete, regulator-ready PIA/DPIA document as output.
---

# Privacy Impact Assessment

Structured PIA/DPIA workflow producing regulator-ready documentation. Mandatory under GDPR Art. 35, Quebec Law 25 Art. 63.5, and recommended/required under HIPAA, PIPEDA, LGPD, PIPL, EU AI Act Art. 9, and Singapore PDPA.

**Composable with:**
- `threat-model-privacy` — Phase 3 (risk identification) imports adversary profiles directly
- `data-minimization` — Phase 2 (processing description) and Phase 4 (risk mitigation) import schema audit findings
- `opsec-review` — Phase 4 mitigations include artifact-level controls
- `redact` — Identify fields requiring sanitization as a mitigation

---

## Regulatory Source of Truth

Statutory citations and jurisdiction facts in this skill and its reference files derive from the normalized taxonomy: `taxonomy/regulatory-taxonomy.md` + the per-jurisdiction records (`taxonomy/regulatory-taxonomy--*.md`; DPIA/PIA triggers are axis **A12**). Records consumed here: `ca-pipeda-law25`, `eu-gdpr-uk`, `us-ca-ccpa`, `br-lgpd`, `cn-pipl`, `sg-pdpa` (+ HIPAA § 164.308 and EU AI Act Art. 9 as sectoral overlays — S-profile records `us-hipaa`, `eu-ai-act`).

On any discrepancy between this skill's files and a record: **the record wins** — unless this file is more specific or more correct, in which case fix the record and log the reconciliation in `.fable/reconciliation-log.md`. Never resolve a conflict by inventing a citation. The assessment floor (PIA-before-any-risky-project, Law 25 Art. 63.5) lives in `taxonomy/regulatory-taxonomy--floor.md` axis A12.

---

## Is a PIA/DPIA Mandatory?

Run this checklist before intake. If ANY trigger fires, a DPIA is mandatory or strongly advised.

Load `references/dpia-triggers.md` for full trigger analysis per regime.

### GDPR Art. 35 Mandatory DPIA Triggers

A DPIA is required when processing is "likely to result in a high risk" to natural persons. GDPR Art. 35(3) enumerates three automatic triggers:

- **Art. 35(3)(a):** Systematic and extensive evaluation of personal aspects based on automated processing, including profiling, on which decisions are taken that significantly affect individuals (e.g. credit scoring, hiring algorithms, fraud detection ML)
- **Art. 35(3)(b):** Large-scale processing of special categories of data (Art. 9) or criminal conviction data (Art. 10)
- **Art. 35(3)(c):** Systematic monitoring of a publicly accessible area on a large scale (e.g. CCTV, geolocation tracking)

EDPB Guidelines 09/2022 add nine additional criteria — **two or more present = DPIA required:**
1. Evaluation or scoring (including profiling)
2. Automated decision-making with legal or similarly significant effects
3. Systematic monitoring
4. Sensitive data or data of a highly personal nature
5. Data processed on a large scale
6. Matching or combining datasets
7. Data concerning vulnerable data subjects (children, employees, patients)
8. Innovative use or applying new technological or organisational solutions
9. Processing that prevents data subjects from exercising a right or using a service

### Quebec Law 25 Art. 63.5 Mandatory PIA Triggers

Any project involving personal information that presents **privacy risks** requires a PIA conducted prior to implementation. Broad scope — interpreted to cover:
- New systems or applications collecting PI
- Significant modifications to existing systems affecting PI
- New uses of existing PI
- Data sharing arrangements with third parties
- Outsourcing involving PI
- Cross-border transfers of PI

The CAI (Commission d'accès à l'information) has issued guidance indicating PIAs should be initiated early in the project lifecycle, not as a post-hoc exercise.

### EU AI Act Art. 9 Risk Management

High-risk AI systems (Annex III) require iterative risk management throughout lifecycle — functionally equivalent to a continuous DPIA. The Art. 9 risk management system must:
- Identify and analyse known and foreseeable risks
- Estimate and evaluate risks that may emerge when used as intended or under reasonably foreseeable misuse
- Evaluate risks arising from post-market data

### Other Regime Requirements

| Regime | Basis | Requirement type |
|---|---|---|
| HIPAA | § 164.308(a)(1)(ii)(A) | Mandatory Risk Analysis — "accurate and thorough assessment of potential risks and vulnerabilities to the confidentiality, integrity, and availability of ePHI" |
| PIPEDA | OPC guidance | Recommended; expected for significant new projects involving PI |
| LGPD | Art. 38 | ANPD may require DPIAs; voluntary otherwise but expected |
| PIPL | Art. 55 | Mandatory for: sensitive PI, automated decision-making, entrusting/sharing/disclosing PI, cross-border transfers |
| Singapore PDPA | PDPC advisory | Recommended for significant personal data processing activities |

---

## Workflow — Seven Phases

### Phase 1 — Scoping and Necessity Check

**1.1 — Identify the processing activity**

Elicit:
- What system, product, feature, or process is being assessed?
- What personal data will be collected, generated, inferred, or processed?
- What is the stated purpose?
- Who are the data subjects (categories of individuals affected)?
- Who is the data controller? Who are the processors?
- What is the approximate volume and frequency of processing?

**1.2 — Determine mandatory vs. voluntary**

Apply the trigger checklist above. Document the outcome explicitly:

```
DPIA NECESSITY DETERMINATION
Processing activity: [name]
GDPR Art. 35(3) triggers: [list or none]
EDPB criteria met: [count] of 9 — threshold [met / not met]
Quebec Law 25 Art. 63.5: [applies / does not apply]
HIPAA § 164.308(a)(1): [applies / does not apply]
EU AI Act Art. 9: [applies / does not apply]

CONCLUSION: DPIA is [MANDATORY / STRONGLY ADVISED / VOLUNTARY]
Basis: [statutory citation]
```

**1.3 — Determine scope boundary**

Define clearly what is IN scope and OUT of scope for this PIA. Scope creep in PIAs produces unusable documents. A system with 12 processing activities should produce 12 PIAs or one clearly-scoped multi-activity PIA — not one vague document covering everything loosely.

---

### Phase 2 — Processing Description

Produce a systematic description of the processing. Load findings from `data-minimization` if a schema audit has been conducted — import the field inventory directly.

**2.1 — Data flow mapping**

Document the complete lifecycle of personal data:

```
DATA FLOW MAP
─────────────────────────────────────────────────────
Collection:    [how PI is collected, from whom, via what channel]
    ↓
Storage:       [where PI is stored, what format, what encryption]
    ↓
Processing:    [what operations are performed — analysis, profiling, 
                inference, enrichment, sharing, display]
    ↓
Retention:     [how long PI is retained, what triggers deletion]
    ↓
Disposal:      [how PI is destroyed — crypto-erase, shredding, etc.]

Third parties: [list all processors, sub-processors, recipients;
                note transfer mechanism for cross-border flows]
Legal basis:   [GDPR Art. 6 lawful basis; or equivalent per regime]
```

**2.2 — Data inventory**

List all personal data fields with classification. If `data-minimization` has been run, import its field inventory here verbatim. If not, produce one.

```
PERSONAL DATA INVENTORY
Field             | Category      | Sensitivity | Retention  | Encrypted
──────────────────|───────────────|─────────────|────────────|──────────
email_address     | Contact       | HIGH        | 24 months  | Yes
ip_address        | Network       | HIGH        | 90 days    | Yes
user_agent        | Technical     | MEDIUM      | 90 days    | No
wallet_address    | Crypto ID     | CRITICAL    | Indefinite | No  ← FLAG
```

**2.3 — Necessity and proportionality assessment**

For each field, answer:
- Is this field **necessary** to achieve the stated purpose?
- Is collection **proportionate** to the purpose?
- Is the retention period **limited** to what is necessary?

Flag any field that fails necessity or proportionality — these are findings requiring mitigation. Cross-reference with `data-minimization` P1–P3 findings.

---

### Phase 3 — Risk Identification

Import adversary profiles from `threat-model-privacy` if a threat model exists. If not, generate a privacy-specific risk register.

**3.1 — Risk register format**

```
RISK REGISTER
─────────────────────────────────────────────────────────────────
Risk ID:      R-001
Risk:         Unauthorised access to user email addresses
Category:     Confidentiality breach
Source:       External attacker (credential stuffing, data breach)
Data affected: email_address, user_id
Likelihood:   HIGH — email/password breaches common; reuse prevalent
Severity:     HIGH — enables phishing, account takeover, spam
Inherent risk: HIGH
Mitigations:  [see Phase 4]
Residual risk: [post-mitigation]

Risk ID:      R-002
Risk:         Wallet address linkage enabling financial surveillance
Category:     Re-identification / inference
Source:       Blockchain analytics adversary; data broker aggregation
Data affected: wallet_address, transaction_timestamps
Likelihood:   MEDIUM — requires motivated adversary with analytics tools
Severity:     CRITICAL — permanent, on-chain, irrevocable
Inherent risk: CRITICAL
```

**3.2 — Privacy-specific risk categories**

Systematically consider each category:

| Category | Description | Example |
|---|---|---|
| Unauthorised access | Breach of confidentiality by external or internal actor | Database breach exposing emails |
| Unauthorised modification | Integrity attack on personal data | Altering health records |
| Unlawful processing | Processing without legal basis or beyond stated purpose | Using analytics data for credit decisions |
| Excessive collection | Collecting more PI than necessary | Storing full IP when /24 suffices |
| Excessive retention | Retaining PI beyond stated retention period | Logs retained indefinitely |
| Re-identification | Combining data to identify pseudonymous individuals | Quasi-identifier cluster |
| Inference | Deriving sensitive attributes not directly collected | Predicting health status from behavior |
| Cross-border transfer risk | PI transferred to jurisdiction without adequate protection | Cloud storage in country without adequacy decision |
| Immutability risk | PI written to immutable medium (blockchain) | Wallet address on-chain with linked PI |
| Third-party exposure | Processor or sub-processor breach or misuse | Analytics vendor breach |
| Data subject rights obstruction | System design making rights exercise difficult | No deletion path; no export mechanism |
| Profiling / automated decision | High-risk automated decision without human review | Algorithm denying access without appeal |

**3.3 — Inherent risk scoring**

Score each risk BEFORE mitigations:

```
Inherent Risk = Likelihood × Severity
  Scale: 1 (Very Low) → 5 (Very High)
  
  CRITICAL: 20-25   HIGH: 12-19   MEDIUM: 6-11   LOW: 1-5
```

---

### Phase 4 — Risk Mitigation

For each HIGH and CRITICAL risk, identify mitigations. Reference the `data-minimization` remediation vocabulary (DROP, HASH, ENCRYPT, TOKENIZE, ADD TTL, etc.) and `threat-model-privacy` mitigation library.

**4.1 — Mitigation register**

```
MITIGATION REGISTER
─────────────────────────────────────────────────────────────────
Risk ID:      R-001
Mitigation:   M-001 — Encrypt email addresses at rest (AES-256-GCM)
              M-002 — Implement breach detection alerting
              M-003 — Enforce unique password + MFA via email magic link
              M-004 — Rate limit login attempts; alert on anomalies
Type:         M1 (prevent) + M2 (detect)
Effort:       MEDIUM
Residual risk: MEDIUM (breach still possible; impact reduced by encryption)

Risk ID:      R-002
Mitigation:   M-005 — HASH wallet address (HMAC-SHA256, domain-separated)
                       before storage in analytics pipeline
              M-006 — Store wallet addresses only where operationally
                       required (transaction record keeping); DROP from
                       analytics schema entirely
              M-007 — ADD TTL — wallet-to-user mapping expires 90 days
                       post-account deletion
Type:         M1 (prevent)
Effort:       MEDIUM
Residual risk: LOW (on-chain records remain; off-chain linkage minimized)
```

**4.2 — Consult DPA?**

GDPR Art. 36 requires prior consultation with the supervisory authority where residual risk remains HIGH or CRITICAL after all mitigations. Document explicitly:

```
PRIOR CONSULTATION DETERMINATION
Residual risks remaining HIGH+: [count]
GDPR Art. 36(1) prior consultation required: [YES / NO]
If YES: Contact [national DPA] before proceeding with processing.
```

---

### Phase 5 — Data Subject Rights Assessment

Assess whether the system enables data subjects to exercise their rights. Flag any gap as a finding.

```
RIGHTS ASSESSMENT
Right                  | Mechanism                    | Status
───────────────────────|──────────────────────────────|────────
Right to access (Art. 15) | [how user can request data] | ✓ / ✗
Right to rectification (Art. 16) | [correction mechanism]    | ✓ / ✗
Right to erasure (Art. 17) | [deletion mechanism; hard delete?] | ✓ / ✗
Right to restriction (Art. 18) | [processing pause mechanism]   | ✓ / ✗
Right to portability (Art. 20) | [export in machine-readable format] | ✓ / ✗
Right to object (Art. 21) | [opt-out of processing mechanism] | ✓ / ✗
Right re automated decisions (Art. 22) | [human review available?] | N/A / ✓ / ✗
```

Any ✗ is a HIGH finding requiring remediation before launch.

**On-chain / immutable storage rights conflict:**
If any PI is stored in immutable form (blockchain, append-only log), document the conflict explicitly:
```
RIGHTS CONFLICT — IMMUTABILITY
Field: [field name]
Storage: [blockchain / append-only log]
Conflict: Right to erasure (Art. 17) cannot be satisfied technically.
Mitigation adopted: [encryption with key deletion / off-chain with
                     on-chain hash only / no PI on-chain]
Legal position: [encryption-as-erasure position; encrypt before write]
DPA consultation: [required if residual risk remains]
```

---

### Phase 6 — Stakeholder Sign-off

Document who reviewed and approved the PIA.

```
SIGN-OFF RECORD
PIA conducted by:     [name / role / date]
DPO reviewed:         [name / date] — or — [DPO not appointed; basis]
Legal reviewed:       [name / date] — or — [not required; basis]
Technical reviewed:   [name / date]
Board/exec notified:  [yes/no; date]
Data subjects consulted: [yes/no; basis for decision]
```

GDPR Art. 35(9) requires seeking the views of data subjects or their representatives where appropriate. Document the decision to consult or not to consult and the basis.

---

### Phase 7 — PIA Document Output

Produce the complete PIA document. Load `references/pia-template.md` for the full formatted template.

The output document structure:

```
PRIVACY IMPACT ASSESSMENT
System: [name]
Version: [date]
Controller: [organisation]
DPO: [name / not appointed]
Status: [DRAFT / UNDER REVIEW / APPROVED / REQUIRES DPA CONSULTATION]

EXECUTIVE SUMMARY
[3–5 sentences: what is being assessed, key risks found,
 overall residual risk level, key mitigations adopted]

1. SCOPE AND CONTEXT
2. NECESSITY DETERMINATION
3. PROCESSING DESCRIPTION
   3.1 Data Flow Map
   3.2 Personal Data Inventory
   3.3 Necessity and Proportionality Assessment
4. RISK REGISTER
5. MITIGATION REGISTER
6. RIGHTS ASSESSMENT
7. PRIOR CONSULTATION DETERMINATION
8. SIGN-OFF RECORD
9. REVIEW SCHEDULE

APPENDIX A: Regulatory Basis Table
APPENDIX B: Data Flow Diagram [if applicable]
APPENDIX C: Linked Assessments [data-minimization audit, threat model]
```

---

## Review and Maintenance

A PIA is a living document — not a one-time exercise.

**Mandatory review triggers (GDPR Art. 35(11), EDPB guidance):**
- Material change to the processing activity
- Change in technology used
- Change in purpose
- Change in regulatory landscape (new law, DPA guidance, case law)
- Identified breach or near-miss involving the system
- Scheduled periodic review (annually for HIGH risk systems; every 2 years for MEDIUM)

**Review record:**
```
REVIEW LOG
Date       | Trigger                    | Reviewer        | Changes made
───────────|────────────────────────────|─────────────────|─────────────
[date]     | Annual review              | [name]          | [summary]
[date]     | New feature added          | [name]          | [summary]
```

---

## Reference Files

- `references/dpia-triggers.md` — Full trigger checklists per regime (GDPR Art. 35 + EDPB nine criteria; Quebec Law 25 Art. 63.5; HIPAA § 164.308; PIPL Art. 55; EU AI Act Art. 9); national DPA mandatory DPIA lists for key jurisdictions
- `references/pia-template.md` — Complete formatted PIA/DPIA document template ready for population; includes all seven phases formatted as a professional regulatory document
