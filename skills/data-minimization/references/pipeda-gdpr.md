# Regulatory Mapping: PIPEDA / GDPR / CCPA

Field-level applicability guide for Canadian, EU, and California privacy law.

> **Source of truth:** this file was a grounding source for the `ca-pipeda-law25`, `eu-gdpr-uk`, and `us-ca-ccpa` taxonomy records (reconciled 2026-07-04). The records are canonical for jurisdiction facts; this file is the field-level companion. Log: `.fable/reconciliation-log.md`. On conflict, the record wins (see `SKILL.md` §Regulatory Source of Truth).

---

## PIPEDA (Canada) — Ten Fair Information Principles

**Statute:** Personal Information Protection and Electronic Documents Act, S.C. 2000, c. 5. Schedule 1 sets out the ten principles; breach reporting obligations are in ss. 10.1–10.3 (added by S.C. 2018, c. 12, s. 2 — RRSHIELDSS amendments, in force Nov 1 2018). OPC enforcement under s. 11. Quebec's Law 25 (Act to modernize legislative provisions as regards the protection of personal information, S.Q. 2021, c. 25) imposes stricter obligations for Quebec-resident data subjects and aligns more closely with GDPR — note where it diverges below.

| Principle | Sched. 1 Clause | Core obligation | Most relevant minimization principles |
|---|---|---|---|
| Accountability | 4.1 | Designate someone responsible for compliance | — |
| Identifying Purposes | 4.2 | State why you collect before or at collection | P1, P2 |
| Consent | 4.3 | Meaningful consent for collection, use, disclosure | P1, P2 |
| **Limiting Collection** | **4.4** | **Collect only what is necessary for stated purpose** | **P1** |
| **Limiting Use, Disclosure, Retention** | **4.5** | **Don't use for other purposes; don't retain beyond need** | **P2, P4** |
| **Accuracy** | 4.6 | Keep data accurate and up to date | P3 |
| **Safeguards** | **4.7** | **Appropriate technical, physical, and organizational safeguards** | **P7** |
| Openness | 4.8 | Make policies publicly available | — |
| Individual Access | 4.9 | Individuals can access and correct their data | P4, P6 |
| Challenging Compliance | 4.10 | Process for complaints | — |

**Clause 4.4 (Limiting Collection)** is the primary statutory hook for data minimization findings. Clause 4.4.1: "The organization shall not collect personal information indiscriminately." Every field lacking a documented collection purpose is a 4.4.1 violation.

**Clause 4.5 (Limiting Use, Disclosure, Retention)** catches purpose-binding violations. Clause 4.5.3: "Personal information that is no longer required to fulfil the identified purposes should be destroyed, erased, or made anonymous." ADD TTL and SEPARATE remediations directly address 4.5.3.

**Clause 4.7 (Safeguards)** — Clause 4.7.1 requires safeguards "appropriate to the sensitivity of the information." 4.7.3 requires that "the methods of protection should include physical measures…organizational measures…[and] technical measures." ENCRYPT and TOKENIZE remediations are the technical measure response.

**Breach reporting (ss. 10.1–10.3):** Organizations must report to the OPC and notify affected individuals of breaches involving a "real risk of significant harm" (s. 10.1(1)). Factors: sensitivity of PI, number of individuals affected, systemic nature (s. 10.1(3)). Data minimization directly reduces PIPEDA breach exposure — less data = lower severity = lower reporting threshold.

**Quebec Law 25 divergences (effective Sept 2023):** Privacy Impact Assessments mandatory for new projects involving PI (s. 63.5); explicit opt-in consent for sensitive PI; prompt breach notification to Commission d'accès à l'information + mandatory incident register *(corrected 2026-07-05 — previously misstated as a 72-hour clock)*; right to data portability (s. 27); right to de-indexing (s. 28.1). Stricter than PIPEDA on all counts — design to Law 25 standard for any Quebec data subjects.

---

## GDPR (EU/EEA) — Key Articles

**Regulation (EU) 2016/679** of the European Parliament and of the Council of 27 April 2016. In force 25 May 2018. Enforced by national supervisory authorities (UK ICO, German BfDI, Irish DPC, French CNIL, etc.). UK GDPR (retained post-Brexit under the Data Protection Act 2018, c. 12) mirrors EU GDPR with minor divergences — treat identically for minimization purposes.

| Article | Paragraph | Title | Core obligation | Minimization principle |
|---|---|---|---|---|
| Art. 5 | 1(b) | Purpose limitation | Collected for specified, explicit, legitimate purposes only; no further incompatible processing | P2 |
| **Art. 5** | **1(c)** | **Data minimisation** | **Adequate, relevant, and limited to what is necessary in relation to the purposes** | **P1, P3** |
| Art. 5 | 1(e) | Storage limitation | Not kept in identifiable form longer than necessary for the purposes | P4 |
| Art. 5 | 1(f) | Integrity & confidentiality | Appropriate security including protection against unauthorised processing and accidental loss | P7 |
| **Art. 25** | **1** | **Data protection by design** | **Controller shall implement appropriate technical and organisational measures designed to implement data-protection principles effectively** | **All** |
| Art. 25 | 2 | Data protection by default | Ensure that by default only personal data necessary for each specific purpose are processed | P1, P2 |
| Art. 17 | 1 | Right to erasure | Must erase on request where no overriding legitimate ground remains | P4, P6 |
| Art. 17 | 3 | Erasure exceptions | Does not apply where processing necessary for legal obligation, public interest, or legal claims | — |
| Art. 20 | 1 | Right to portability | Data in structured, commonly used, machine-readable format | — |
| Art. 83 | 4 | Lower tier fines | Up to €10M or 2% global annual turnover for Art. 25 violations | — |
| Art. 83 | 5 | Upper tier fines | Up to €20M or 4% global annual turnover for Art. 5 violations | — |
| Recital 39 | — | Storage limitation guidance | "The personal data should be adequate, relevant and limited to what is necessary for the purposes for which they are processed" | P1, P3 |
| Recital 78 | — | Privacy by design guidance | Controllers should "minimise the processing of personal data, pseudonymise personal data as soon as possible, create transparency" | P1, P6, P7 |

**Art. 5(1)(c) is the statutory basis for data minimization.** "Adequate, relevant, and limited to what is necessary" is a three-part test: adequacy (enough to serve the purpose), relevance (connected to the purpose), necessity (no more than required). Every HIGH+ finding fails at least one limb.

**Art. 25(1) — Privacy by Design** requires controllers to implement minimization "at the time of the determination of the means for processing and at the time of the processing itself." This makes privacy-by-design a legal obligation, not best practice. Pre-shipping schema audit under this skill directly satisfies Art. 25(1).

**Art. 25(2) — Privacy by Default** specifically requires that "by default, only personal data which are necessary for each specific purpose of the processing are processed." Default settings must be minimizing. P1 violations in default configurations are Art. 25(2) violations.

**Art. 17 + Immutable Storage conflict:** The right to erasure under Art. 17(1) is incompatible with blockchain immutability. EDPB guidance (Guidelines 05/2019 on the criteria of the Right to be Forgotten in the search engines cases) and subsequent Working Party 29 opinions acknowledge this tension without resolving it. Best-practice mitigations: (a) encrypt before writing — key deletion constitutes practical erasure under some interpretations; (b) store only content-addressed hashes on-chain with personal data off-chain; (c) structure on-chain data so no personal data is directly included. Consult local DPA before relying on encryption-as-erasure in a regulated context.

**Special categories (Art. 9):** Health, biometric, genetic, racial/ethnic origin, political opinions, religious beliefs, trade union membership, sexual orientation — require explicit consent or a specific Art. 9(2) ground for processing. Escalate any Art. 9 field to CRITICAL regardless of other context.

---

## CCPA / CPRA (California)

**CCPA:** California Consumer Privacy Act, Cal. Civ. Code §§ 1798.100–1798.199.100, effective Jan 1 2020. **CPRA:** California Privacy Rights Act, Prop. 24 (Nov 2020), amending and expanding CCPA, substantive provisions effective Jan 1 2023. Enforced by the California Privacy Protection Agency (CPPA) — rulemaking authority transferred from AG under Cal. Civ. Code § 1798.199.40.

| Right / Obligation | Statutory basis | Core requirement | Minimization relevance |
|---|---|---|---|
| Right to know | § 1798.100 | Disclose categories and specific pieces of PI collected | Fewer categories = simpler, lower-risk disclosure |
| Right to delete | § 1798.105 | Must delete PI on verifiable consumer request; no soft-delete | P4, P6 |
| Right to correct | § 1798.106 (CPRA) | Must correct inaccurate PI on request | P3 |
| Right to opt out of sale/sharing | §§ 1798.120, 1798.135 | Must not sell or share PI without opt-out | P2 |
| **Data minimization** | **§ 1798.100(a)(3) (CPRA)** | **Collect only what is reasonably necessary and proportionate to the disclosed purpose** | **P1** |
| **Purpose limitation** | **§ 1798.100(a)(4) (CPRA)** | **Don't use PI for purposes incompatible with those disclosed at collection** | **P2** |
| Sensitive PI restrictions | § 1798.121 (CPRA) | Right to limit use of sensitive PI; special notice required | P1, P6, P7 |
| Security obligations | § 1798.150 | Reasonable security procedures; private right of action for breaches | P7 |

**§ 1798.100(a)(3) (CPRA data minimization):** "A business' collection, use, retention, and sharing of a consumer's personal information shall be reasonably necessary and proportionate to achieve the purposes for which the personal information was collected or processed." This is a proportionality test — not just necessity. A field may be necessary but still fail if its collection is disproportionate to the purpose.

**Sensitive PI (§ 1798.140(ae)):** SSN/SIN/passport/driver's license numbers; financial account + credentials; precise geolocation (within 1,850 feet); racial/ethnic origin; religious beliefs; union membership; contents of mail/email/text messages; genetic data; biometric data; health/medical information; sexual orientation or gender identity. Consumers have the right under § 1798.121 to direct businesses to limit use of sensitive PI to what is necessary to perform the service. Always CRITICAL tier.

**CPRA (effective Jan 2023)** aligned California materially with GDPR on minimization and purpose limitation. Design to CPRA standard = materially GDPR-compatible for most data types.

---

## Field-Level Regulatory Applicability

### Fields that are Automatically High-Risk Under All Three Regimes

| Field type | PIPEDA | GDPR | CCPA/CPRA |
|---|---|---|---|
| Full name | Principle 4 | Art. 5(1)(c) | PI category |
| Email address | Principle 4 | Art. 5(1)(c) | PI category |
| Phone number | Principle 4 | Art. 5(1)(c) | PI category |
| IP address (full) | Principle 4 | Art. 5(1)(c) — personal data per CJEU | PI category |
| Precise geolocation | Principle 4 | Art. 9 (special category if health context) | Sensitive PI (CPRA) |
| Device ID / fingerprint | Principle 4 | Art. 5(1)(c) | PI category |
| Biometric data | Principle 4 | Art. 9 special category | Sensitive PI (CPRA) |
| Financial data | Principle 4 + 7 | Art. 5(1)(c) + (f) | Sensitive PI (CPRA) |
| Health data | Principle 4 + 7 | Art. 9 special category | Sensitive PI (CPRA) |

### Pseudonymous Data

Both GDPR and PIPEDA recognize pseudonymized data as still being personal data if re-identification is possible. Pseudonymization is a risk reduction measure, not an exemption.

Truly anonymized data (k-anonymous, differentially private) is generally outside scope. The bar for "truly anonymous" is high — most data labeled "anonymized" is merely pseudonymized.

---

## Defensible Exception Documentation

When minimization is intentionally limited (e.g., security event logs needing full fidelity for detection), document the exception with statutory precision. Undocumented exceptions are violations. Documented, justified exceptions with compensating controls are defensible under all three regimes.

```
MINIMIZATION EXCEPTION RECORD
Field:                ip_address (full IPv4)
Schema / system:      [system name]
Date documented:      [date]
Reviewed by:          [role]

Exception basis:      Security detection efficacy
Operational need:     Fraud pattern detection requires full IP;
                      /24 truncation creates unacceptable false
                      negative rate for known attack patterns.
                      City-level geolocation is a required output.

Compensating controls:
  - Access restricted to security team (role-based, logged)
  - Not replicated to analytics or marketing pipelines
  - 90-day hard TTL with automated deletion job
  - Encrypted at rest (AES-256-GCM)
  - Pseudonymized in any external-facing reports

Regulatory basis:
  GDPR Art. 5(1)(c): full IP is "adequate" and "necessary"
    for stated security purpose; satisfies three-part test.
  GDPR Art. 25(1): privacy-by-design obligation met via
    compensating controls above.
  PIPEDA Clause 4.4.1: collection not indiscriminate —
    each IP collected for documented fraud detection purpose.
  PIPEDA Clause 4.7.1: safeguards appropriate to sensitivity
    (encryption, access control, TTL).
  CCPA § 1798.100(a)(3): collection reasonably necessary
    and proportionate to stated security purpose.

Review date:          [quarterly — or on material change to
                       fraud detection methodology]
```
