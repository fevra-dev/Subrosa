# Global Regulatory Reference

Field-level applicability guide for privacy and data protection law across major jurisdictions. Includes HIPAA, PIPEDA/Law 25, GDPR, CCPA/CPRA, LGPD, PIPL, COPPA, Australia Privacy Act, APPI, DPDPA, and POPIA.

**Regulatory status:** Current as of July 2026 (EU AI Act timeline updated 2026-07-17 per the Digital Omnibus on AI). Verify effective dates, pending rulemakings, and enforcement guidance against primary sources before advising in a regulated context. This reference is for schema design and audit — not legal advice.

> **Source of truth:** this file was the grounding source for the `taxonomy/regulatory-taxonomy--*.md` records (reconciled 2026-07-04). Going forward the records are canonical for jurisdiction facts and this file is the deep-dive companion; fixes land in the record first, then here. Log: `.fable/reconciliation-log.md`.

---

## Jurisdiction Quick-Select

| Jurisdiction | Statute | Enforcement | Key minimization hook |
|---|---|---|---|
| 🇨🇦 Canada (federal) | PIPEDA, S.C. 2000, c. 5 | OPC | Clause 4.4 (limiting collection) |
| 🇨🇦 Canada (Quebec) | Law 25, S.Q. 2021, c. 25 | CAI | Art. 63.5 (PIA), Art. 9 (necessity) |
| 🇪🇺 EU / EEA | GDPR, Reg. EU 2016/679 | National DPAs | Art. 5(1)(c) (data minimisation) |
| 🇬🇧 UK | UK GDPR + DPA 2018, c. 12 | ICO | Art. 5(1)(c) (same as EU GDPR) |
| 🇺🇸 Healthcare | HIPAA, 45 CFR Parts 160, 164 | HHS OCR | § 164.502(b) (minimum necessary) |
| 🇺🇸 California | CCPA/CPRA, Cal. Civ. Code §§ 1798.100+ | CPPA | § 1798.100(a)(3) (minimization) |
| 🇺🇸 Children's data | COPPA, 15 U.S.C. §§ 6501-6506 | FTC | § 6502(b)(1) (necessary collection) |
| 🇧🇷 Brazil | LGPD, Law No. 13,709/2018 | ANPD | Art. 6(III) (necessity principle) |
| 🇨🇳 China | PIPL, effective Nov 1 2021 | CAC / SAMR | Art. 6 (minimum necessary) |
| 🇦🇺 Australia | Privacy Act 1988 + APPs | OAIC | APP 3.3 (collection limitation) |
| 🇯🇵 Japan | APPI (amended 2022) | PPC | Art. 17(1) (collection limitation) |
| 🇮🇳 India | DPDPA 2023 | DPBI | § 6(1) (purpose limitation) |
| 🇿🇦 South Africa | POPIA, Act 4 of 2013 | Information Regulator (IR) | § 10 (processing limitation) |

---

## HIPAA (United States — Healthcare)

**Statutes:** Health Insurance Portability and Accountability Act of 1996, Pub. L. 104-191. Implementing regulations: 45 CFR Parts 160 and 164. Three operative rules:
- **Privacy Rule:** 45 CFR §§ 164.500-164.534 (effective Apr 14 2003)
- **Security Rule:** 45 CFR §§ 164.302-164.318 (effective Apr 20 2005)
- **Breach Notification Rule:** 45 CFR §§ 164.400-164.414 (HITECH 2009, effective Feb 17 2010)

**Covered entities:** Health plans, health care clearinghouses, health care providers who transmit PHI electronically (45 CFR § 160.103). **Business Associates (BAs):** Vendors who create, receive, maintain, or transmit PHI on behalf of a covered entity — must execute BAA (45 CFR § 164.308(b)).

**Enforcement:** HHS Office for Civil Rights (OCR). Civil monetary penalties: $100–$50,000+ per violation, up to $1.9M per violation category per year (45 CFR § 160.404, adjusted annually). Criminal: up to 10 years imprisonment for knowing misuse (42 U.S.C. § 1320d-6).

### Minimum Necessary Standard (45 CFR § 164.502(b))

The HIPAA data minimization equivalent. Covered entities must make reasonable efforts to limit PHI disclosed to "the minimum necessary to accomplish the intended purpose of the use, disclosure, or request."

**Mapping to minimization principles:**
- § 164.502(b)(1): routine/recurring disclosures → P1, P2
- § 164.514(d): covered entities must implement policies identifying minimum necessary for internal uses → P1, P6
- § 164.514(d)(3): reasonable reliance on business associates' minimum necessary representations → P6

The Minimum Necessary standard does NOT apply to: disclosures to the individual, disclosures to HHS, uses/disclosures required by law, treatment communications between providers.

### The 18 PHI Identifiers (Safe Harbor De-identification)

Under 45 CFR § 164.514(b)(2), data is de-identified (outside HIPAA scope) when ALL 18 identifiers are removed AND the covered entity has no actual knowledge the data can identify an individual.

**These 18 identifiers must be treated as CRITICAL tier in any HIPAA-scoped schema:**

| # | Identifier | Notes |
|---|---|---|
| 1 | Names | All names — first, last, maiden, suffix |
| 2 | Geographic subdivisions smaller than state | Street address, city, county, ZIP. ZIP codes may be retained if: (a) 3-digit prefix contains >20,000 people AND (b) not one of the 17 high-risk 3-digit codes listed in § 164.514(b)(2)(i)(B) |
| 3 | Dates (except year) | Birth date, admission date, discharge date, death date, all ages >89 (must be aggregated into 90+) |
| 4 | Phone numbers | All — including fax |
| 5 | Fax numbers | See above |
| 6 | Email addresses | |
| 7 | Social security numbers | |
| 8 | Medical record numbers | |
| 9 | Health plan beneficiary numbers | |
| 10 | Account numbers | |
| 11 | Certificate / license numbers | Driver's license, professional license, etc. |
| 12 | Vehicle identifiers and serial numbers | Including license plate |
| 13 | Device identifiers and serial numbers | Medical devices, but also phones/tablets used in care context |
| 14 | Web URLs | |
| 15 | IP addresses | Full IP = PHI in HIPAA context; cannot retain even truncated unless expert determination confirms de-identification |
| 16 | Biometric identifiers | Finger and voice prints |
| 17 | Full face photographs and comparable images | |
| 18 | Any other unique identifying number, characteristic, or code | Catch-all — if it could identify the individual, it counts |

**De-identification path 1 — Safe Harbor (§ 164.514(b)(2)):** Remove all 18. No residual actual knowledge. No statistical expertise required.

**De-identification path 2 — Expert Determination (§ 164.514(b)(1)):** A person with appropriate knowledge applies generally accepted statistical/scientific principles and documents that the risk of identification is very small. More flexible but requires expertise and documentation.

**Re-identification prohibition (§ 164.514(c)):** A covered entity may not use or disclose a code or other means of record identification for re-identification unless it was derived by the covered entity and not disclosed.

### HIPAA Security Rule Safeguard Categories (45 CFR § 164.312)

Maps to our P7 (Cryptographic Minimization) and the mitigation library:

**Technical safeguards (§ 164.312):**
- Access control (§ 164.312(a)(1)): unique user identification, emergency access, automatic logoff, encryption/decryption
- Audit controls (§ 164.312(b)): hardware/software/procedural mechanisms to record and examine activity
- Integrity controls (§ 164.312(c)(1)): protect ePHI from improper alteration or destruction
- Transmission security (§ 164.312(e)(1)): guard against unauthorized access during transmission — encryption required for ePHI in transit

**Administrative safeguards (§ 164.308):**
- Risk analysis (§ 164.308(a)(1)): accurate/thorough assessment of potential risks and vulnerabilities to ePHI
- Risk management (§ 164.308(a)(1)(ii)(B)): security measures to reduce risks to a reasonable level
- Workforce training (§ 164.308(a)(5))

**Physical safeguards (§ 164.310):**
- Facility access controls, workstation use policies, device/media controls

### HIPAA Breach Notification (45 CFR §§ 164.400-414)

A breach of unsecured PHI triggers notification obligations unless the covered entity demonstrates low probability of compromise using a 4-factor risk assessment (§ 164.402(2)):
1. Nature and extent of PHI involved (identifiers, likelihood of re-identification)
2. Who accessed / used the PHI, or to whom it was disclosed
3. Whether the PHI was actually acquired or viewed
4. Extent to which risk has been mitigated

**Notification timelines:** Individuals: without unreasonable delay, no later than 60 days (§ 164.404(b)). HHS: simultaneously with individual notification (§ 164.408). Media (breaches >500 in a state): simultaneously (§ 164.406).

**Data minimization reduces breach scope:** Less PHI collected = narrower breach = lower risk assessment score = potentially below notification threshold.

---

## PIPEDA (Canada — Federal)

**Statute:** Personal Information Protection and Electronic Documents Act, S.C. 2000, c. 5. Schedule 1 sets out the ten principles. Breach reporting: ss. 10.1–10.3 (S.C. 2018, c. 12, s. 2, in force Nov 1 2018). OPC enforcement under s. 11.

**Note:** PIPEDA is under active reform. Bill C-27 (Consumer Privacy Protection Act + AIDA) was tabled in 2022 and would replace PIPEDA with a GDPR-aligned regime. Status as of June 2026: verify current Parliamentary status.

| Principle | Sched. 1 Clause | Core obligation | Minimization principle |
|---|---|---|---|
| Accountability | 4.1 | Designate responsible person | — |
| Identifying Purposes | 4.2 | State purpose before/at collection | P1, P2 |
| Consent | 4.3 | Meaningful consent | P1, P2 |
| **Limiting Collection** | **4.4** | **Collect only what is necessary** | **P1** |
| **Limiting Use, Disclosure, Retention** | **4.5** | **No other purposes; don't retain beyond need** | **P2, P4** |
| **Accuracy** | 4.6 | Keep data accurate | P3 |
| **Safeguards** | **4.7** | **Appropriate technical, physical, organizational safeguards** | **P7** |
| Openness | 4.8 | Make policies public | — |
| Individual Access | 4.9 | Access and correction rights | P4, P6 |
| Challenging Compliance | 4.10 | Complaint process | — |

**Clause 4.4.1:** "The organization shall not collect personal information indiscriminately." Every field without documented purpose violates 4.4.1.

**Clause 4.5.3:** "Personal information that is no longer required to fulfil the identified purposes should be destroyed, erased, or made anonymous." ADD TTL and SEPARATE directly address 4.5.3.

**Clause 4.7.1:** Safeguards "appropriate to the sensitivity of the information." **Clause 4.7.3:** Methods must include physical, organizational, and technical measures.

**Breach reporting (s. 10.1):** "Real risk of significant harm" triggers OPC report and individual notification. Factors: sensitivity, number of individuals, systemic nature (s. 10.1(3)). Data minimization = lower exposure = lower breach severity = lower reporting threshold.

### Quebec Law 25 (Stricter overlay for Quebec data subjects)

**Statute:** Act to modernize legislative provisions as regards the protection of personal information, S.Q. 2021, c. 25. Amends the Act Respecting the Protection of Personal Information in the Private Sector (PPIPS). Enforced by Commission d'accès à l'information (CAI). Substantive obligations in force Sept 22 2023.

**Key divergences from PIPEDA (stricter on all counts):**
- **Privacy Impact Assessments (PIAs) mandatory** for any new project involving PI that presents privacy risks (Art. 63.5 PPIPS) — not optional as under PIPEDA
- **Explicit opt-in consent required** for sensitive PI (Art. 12 PPIPS) — opt-out insufficient
- **Prompt breach notification** to CAI + mandatory confidentiality-incident register — vs PIPEDA's "without unreasonable delay" *(corrected 2026-07-05: this file previously stated a 72-hour clock citing "Art. 3.2 PPIPS"; primary-source check found no fixed clock — see `.fable/reconciliation-log.md`)*
- **Right to de-indexing** (Art. 28.1 PPIPS) — broader than GDPR erasure in some respects
- **Right to data portability** (Art. 27 PPIPS) — machine-readable format
- **Data localization:** PI may not be communicated outside Quebec without adequate protection assessment (Art. 17 PPIPS)
- **Penalties:** Up to CAD 25M or 4% of worldwide turnover (Art. 90.1 PPIPS)

**Design to Law 25 standard for any Quebec data subjects** — it is stricter than PIPEDA and materially aligned with GDPR.

---

## GDPR (EU/EEA)

**Regulation (EU) 2016/679**, 27 April 2016. In force 25 May 2018. **UK GDPR** (retained under Data Protection Act 2018, c. 12) mirrors EU GDPR — treat identically for minimization.

| Article | Para | Title | Obligation | Principle |
|---|---|---|---|---|
| Art. 5 | 1(b) | Purpose limitation | Specified, explicit, legitimate purposes; no incompatible further processing | P2 |
| **Art. 5** | **1(c)** | **Data minimisation** | **Adequate, relevant, limited to what is necessary** | **P1, P3** |
| Art. 5 | 1(e) | Storage limitation | Not kept identifiable longer than necessary | P4 |
| Art. 5 | 1(f) | Integrity & confidentiality | Appropriate security | P7 |
| **Art. 25** | **1** | **Data protection by design** | **Technical/organisational measures to implement principles effectively** | **All** |
| Art. 25 | 2 | Data protection by default | By default, only necessary data processed | P1, P2 |
| Art. 17 | 1 | Right to erasure | Erase on request where no overriding ground | P4, P6 |
| Art. 17 | 3 | Erasure exceptions | Legal obligation, public interest, legal claims | — |
| Art. 9 | 1 | Special categories | Health, biometric, genetic, racial/ethnic, political, religious, sexual orientation — prohibited processing absent explicit consent or Art. 9(2) ground | CRITICAL tier always |
| Art. 83 | 4 | Lower tier fines | €10M / 2% turnover for Art. 25 violations | — |
| Art. 83 | 5 | Upper tier fines | €20M / 4% turnover for Art. 5 violations | — |

**Art. 5(1)(c) three-part test:** adequacy (enough to serve the purpose) + relevance (connected to the purpose) + necessity (no more than required). Every HIGH+ finding fails at least one limb.

**Art. 25(2) by default:** Default settings must minimize. P1 violations in default configurations are Art. 25(2) violations enforceable by national DPAs.

**Art. 17 + Blockchain conflict:** EDPB Guidelines 05/2019; no definitive resolution. Best practice: (a) encrypt before writing — key deletion as practical erasure; (b) store only content-addressed hashes on-chain; (c) personal data entirely off-chain. Consult local DPA before relying on encryption-as-erasure in regulated context.

**Recital 39:** "The personal data should be adequate, relevant and limited to what is necessary for the purposes for which they are processed."
**Recital 78:** Controllers should "minimise the processing of personal data, pseudonymise personal data as soon as possible, create transparency with regard to the functions and processing of personal data."

---

## CCPA / CPRA (California)

**CCPA:** Cal. Civ. Code §§ 1798.100-1798.199.100, effective Jan 1 2020. **CPRA:** Prop. 24 (Nov 2020), substantive provisions effective Jan 1 2023. Enforced by California Privacy Protection Agency (CPPA, Cal. Civ. Code § 1798.199.40).

| Right / Obligation | Statutory basis | Requirement | Principle |
|---|---|---|---|
| Right to know | § 1798.100 | Disclose categories and specific pieces of PI | P1 |
| Right to delete | § 1798.105 | Delete PI on verifiable request; no soft-delete | P4, P6 |
| Right to correct | § 1798.106 (CPRA) | Correct inaccurate PI on request | P3 |
| Right to opt out | §§ 1798.120, 1798.135 | No sale/sharing without opt-out | P2 |
| **Data minimization** | **§ 1798.100(c) (CPRA)** | **Reasonably necessary and proportionate to disclosed purpose** | **P1** |
| **Purpose limitation** | **§ 1798.100(a)(4) (CPRA)** | **No use incompatible with purposes disclosed at collection** | **P2** |
| Sensitive PI | § 1798.121 (CPRA) | Right to limit use; special notice required | P1, P6, P7 |
| Security | § 1798.150 | Reasonable security; private right of action for breaches | P7 |

**§ 1798.100(c) proportionality test** *(anchor corrected 2026-07-17)*: not just necessity but proportionality — a field may be necessary but still fail if collection is disproportionate to the stated purpose.

**Sensitive PI (§ 1798.140(ae)):** SSN/SIN/passport/DL numbers; financial account + credentials; precise geolocation (within 1,850 feet / ~565m); racial/ethnic origin; religious beliefs; union membership; contents of mail/email/texts; genetic data; biometric data; health/medical; sexual orientation or gender identity. Always CRITICAL tier.

---

## COPPA (United States — Children's Data)

**Statute:** Children's Online Privacy Protection Act of 1998, 15 U.S.C. §§ 6501-6506. **Rule:** 16 CFR Part 312 (FTC COPPA Rule, amended 2013; further amendments proposed 2023 — verify current status). Enforced by FTC under 15 U.S.C. § 6504.

**Scope:** Operators of websites and online services directed to children under 13, or operators with actual knowledge they are collecting PI from children under 13. Applies regardless of where operator is based if directed at US children.

**Penalties:** Civil monetary penalties up to $51,744 per violation per day (2023 adjusted figure). No private right of action under COPPA itself (state AGs can act under § 6504(b)).

### Core Obligations

**Verifiable parental consent required before:**
- Collecting, using, or disclosing PI from a child under 13 (§ 6502(b)(1)(A))

**Data minimization obligation (§ 6502(b)(1)(D) via 16 CFR § 312.7):**
Operators must not condition a child's participation in an activity on the disclosure of more PI than is reasonably necessary.

**16 CFR § 312.5(a) — Notice and consent:**
- Clear and prominent notice of information practices on website home page AND each page where PI is collected
- Must obtain verifiable parental consent prior to collection

**16 CFR § 312.10 — Data retention and deletion:**
Retain PI only as long as reasonably necessary to fulfill the purpose for which collected. Delete using reasonable measures to protect against unauthorized access during deletion.

**Personal information under COPPA (16 CFR § 312.2):**
First/last name; home/physical address; email; telephone; SSN; persistent identifier (cookie, IP, device ID, processor serial number, unique device ID); photo/video/audio containing child's image or voice; geolocation; and any other information that permits contact with a specific individual.

**Key schema implications:**
- Any persistent identifier (cookie, device ID, IP, advertising ID) = PI under COPPA if associated with a child
- Age-gating mechanisms must be robust — if age gate can be easily circumvented, "actual knowledge" liability accrues
- Do not collect birthdate with enough precision to identify someone as under 13 unless you have a consent mechanism

**Neutral age screening:** If you collect birthdate and a user is under 13, you must either: (a) obtain verifiable parental consent before proceeding, (b) collect no PI and provide a notice to the parent, or (c) block the user. You may NOT collect PI from a user who has identified as under 13 without parental consent, even temporarily.

---

## LGPD (Brazil)

**Statute:** Lei Geral de Proteção de Dados Pessoais, Federal Law No. 13,709/2018, as amended by Law No. 13,853/2019. In force for private entities August 2020; penalties in force August 2021. **Enforcement:** Autoridade Nacional de Proteção de Dados (ANPD). **Penalties:** Up to BRL 50M per violation or 2% of legal entity's revenue in Brazil (capped at BRL 50M per infraction).

**Extraterritorial scope (Art. 3):** Applies to any processing of data of individuals in Brazil, regardless of where the processing entity is located — mirrors GDPR Art. 3.

### Key Minimization Provisions

**Art. 6 — Principles (ten principles, directly analogous to GDPR Art. 5):**

| Art. 6 | Principle | GDPR analog | Minimization hook |
|---|---|---|---|
| 6(I) | Purpose | Art. 5(1)(b) | Collection for legitimate, explicit, informed purposes only |
| 6(II) | Adequacy | Art. 5(1)(c) | Compatible with purposes disclosed to data subject |
| **6(III)** | **Necessity** | **Art. 5(1)(c)** | **Limited to minimum necessary for purposes** — primary minimization hook |
| 6(IV) | Free access | Art. 20 | Consultation, correction, portability |
| 6(V) | Data quality | Art. 5(1)(d) | Accurate, relevant, updated |
| 6(VI) | Transparency | Art. 5(1)(a) | Clear information about processing |
| 6(VII) | Security | Art. 5(1)(f) | Technical and administrative measures |
| 6(VIII) | Prevention | Art. 25 | Prevent harm before it occurs |
| 6(IX) | Non-discrimination | — | No discriminatory processing |
| 6(X) | Accountability | Art. 5(2) | Demonstrate compliance |

**Art. 6(III) necessity principle:** "limitação ao mínimo necessário para a realização de suas finalidades" — limitation to the minimum necessary for the purposes. Direct P1 hook.

**Sensitive data (Art. 5(II) + Art. 11):** Racial/ethnic origin; religious beliefs; political opinions; union membership; health/sexual life/sexual orientation; genetic/biometric data — require specific legal basis (explicit consent or one of Art. 11(II) grounds). CRITICAL tier always.

**Art. 46 — Security measures:** Controller and operator must adopt technical and administrative security measures to protect PI from unauthorized access and accidental or unlawful destruction, loss, alteration, disclosure, or any improper form of treatment.

**Art. 48 — Breach notification:** Communicate to ANPD and data subject "within a reasonable time period" (ANPD Resolution CD/ANPD No. 15/2023: 3 business days to ANPD, 5 business days to data subjects for high-risk incidents).

**International transfer (Art. 33):** PI may be transferred internationally only to countries with adequate protection, or under specific safeguards (standard contractual clauses per Art. 33(V), binding corporate rules per Art. 33(VII)). ANPD adequacy decisions current as of 2026: verify current list.

---

## PIPL (China)

**Statute:** Personal Information Protection Law of the People's Republic of China, promulgated Aug 20 2021, effective Nov 1 2021. **Enforcement:** Cyberspace Administration of China (CAC) as primary regulator; also Ministry of Public Security, State Administration for Market Regulation (SAMR), and sector-specific regulators. **Penalties:** Up to RMB 50M or 5% of prior year revenue; individuals: up to RMB 1M; suspension/revocation of business license for serious violations.

**Most restrictive cross-border transfer regime of any major framework.**

**Extraterritorial scope (Art. 3):** Applies to processing of PI of natural persons within China, and processing outside China that (a) is for the purpose of providing products/services to individuals within China, (b) involves analysis/assessment of behavior of individuals within China, or (c) is otherwise required by law or regulation.

### Core Minimization Requirements

**Art. 6 — Minimum necessary principle:** "处理个人信息应当具有明确、合理的目的，并应当与处理目的直接相关，采取对个人权益影响最小的方式。收集个人信息，应当限于实现处理目的的最小范围，不得过度收集个人信息。"

Translation: Personal information processing shall have a clear and reasonable purpose, be directly related to the processing purpose, and adopt the method that has the least impact on personal rights. Collection shall be limited to the minimum scope necessary to achieve the processing purpose; excessive collection is prohibited.

**Direct P1 mapping — stricter than GDPR:** PIPL Art. 6 explicitly prohibits "excessive collection" (过度收集) — enforcement has cited this against apps collecting location, contacts, and other data not required for stated function.

**Art. 17 — Transparency:** Controllers must proactively inform data subjects of identity, purpose, category of PI, retention period, and rights.

**Art. 13 — Legal bases:** Consent; necessary for contract performance; necessary to fulfill legal obligation; necessary to respond to public health emergencies; processing for the public interest; within reasonable scope for already-disclosed PI; other bases per law.

### Sensitive Personal Information (Art. 28-32)

Requires "specific purposes and sufficient necessity" AND separate consent:
- Biometric characteristics
- Religious beliefs
- Medical health information
- Financial accounts
- Whereabouts/location tracking
- Personal information of minors under 14

**Minors (Art. 31):** PI of minors under 14 is sensitive PI — requires consent from parent or guardian; operators must formulate special processing rules.

### Cross-Border Transfer Requirements (Arts. 38-43)

**The strictest cross-border transfer regime globally.** One of the following must be met:
- CAC security assessment (mandatory for: (a) operators of critical information infrastructure, (b) processors of PI above threshold volumes — 1M+ individuals' PI total, or 100,000+ individuals' PI / 10,000+ sensitive PI in preceding year)
- Personal information protection certification by CAC-recognized agency
- Standard contracts concluded with overseas recipient (CAC Standard Contract, effective June 1 2023)
- Other conditions prescribed by CAC

**Implication for schema design:** If processing PI of individuals in China and transferring outside China, the data architecture must support the applicable transfer mechanism from day one. This affects what PI can even be collected — if you cannot lawfully transfer it, don't collect it.

**Art. 43 — Reciprocal restrictions:** China may take reciprocal countermeasures against countries/regions that impose discriminatory or restrictive measures against China regarding PI protection.

---

## Australia Privacy Act 1988 + Australian Privacy Principles (APPs)

**Statute:** Privacy Act 1988 (Cth). **Australian Privacy Principles:** Schedule 1 to the Privacy Act (as amended by Privacy Amendment (Enhancing Privacy Protection) Act 2012). **Enforcement:** Office of the Australian Information Commissioner (OAIC). **Penalties:** Up to AUD 50M, or 3× benefit obtained, or 30% of adjusted turnover in relevant period — for serious or repeated interferences (Privacy and Other Legislation Amendment Act 2024, amending s. 13G).

**Small business exemption:** Most businesses with annual turnover ≤ AUD 3M are exempt (s. 6C) — but exemption is narrowing under reform proposals.

### Key APPs

| APP | Title | Core obligation | Minimization principle |
|---|---|---|---|
| APP 1 | Open and transparent management | Privacy policy; implement practices to comply | — |
| APP 2 | Anonymity and pseudonymity | Offer individuals option to interact anonymously where lawful and practicable | P5 |
| **APP 3** | **Collection of solicited PI** | **Collect only if reasonably necessary for functions/activities** | **P1** |
| APP 3.3 | Collection from third parties | Only if reasonable and practicable to collect directly from individual | P1 |
| APP 5 | Notification | Notify individual of collection at or before time of collection | P2 |
| APP 6 | Use or disclosure | Use/disclose only for primary purpose of collection (or secondary purpose with consent / meets exceptions) | P2 |
| **APP 11** | **Security of PI** | **Reasonable steps to protect from misuse, interference, loss, unauthorised access/modification/disclosure** | **P7** |
| APP 11.2 | Destruction/de-identification | Destroy or de-identify PI no longer needed for any purpose | P4 |
| APP 12 | Access | Provide access to PI on request | P6 |
| APP 13 | Correction | Correct PI on request | P3 |

**APP 3.3 (solicited collection):** Must not collect PI unless it is reasonably necessary for, or directly related to, one or more of the entity's functions or activities. For sensitive information: "reasonably necessary" for a health service, or consent-based.

**Sensitive information (s. 6 Privacy Act):** Racial/ethnic origin; political opinions; membership of political association; religious beliefs/affiliations; philosophical beliefs; membership of professional/trade association; membership of trade union; sexual orientation or practices; criminal record; health information; genetic information; biometric information. Requires consent for collection in addition to APP 3 necessity test.

**APP 11.2 — Destruction/de-identification:** Entity must take reasonable steps to destroy or de-identify PI when it is no longer needed for any purpose for which it may be used/disclosed. No longer "holding" PI that has no further purpose — this is the APP analog of GDPR Art. 5(1)(e) storage limitation and PIPEDA Clause 4.5.3.

---

## APPI (Japan)

**Statute:** Act on the Protection of Personal Information (個人情報の保護に関する法律), Act No. 57 of 2003. Major amendments: 2015 (effective 2017), 2020 (effective April 2022). **Enforcement:** Personal Information Protection Commission (PPC). **Penalties (2022 amendments):** Corporations up to JPY 100M; individuals up to JPY 1M; and JPY 500,000 for reporting violations.

**Extraterritorial scope (Art. 24-bis, 2022 amendments):** Domestic operators must impose equivalent obligations on overseas recipients of personal information via contracts or equivalent measures.

### Core Minimization Provisions

**Art. 17(1) — Collection limitation:** Personal information shall be acquired with specification of the purpose of use and shall not be acquired beyond the scope necessary to achieve the purpose.

**Art. 19 — Accuracy:** A business operator shall endeavor to keep personal data accurate and up-to-date within the scope necessary to achieve the purpose of use, and to delete personal data without delay when they are no longer required.

**Art. 20 — Security measures:** A business operator shall take necessary and appropriate action for the prevention of leakage, loss, or damage, and for other secure management of personal data.

**Sensitive information (要配慮個人情報, Art. 2(3)):** Racial origin; creed; social status; medical history; criminal record; criminal damage record; and other information requiring special care as specified by cabinet order (disability, health examination results, etc.). Requires explicit consent for collection (Art. 17(2)).

**2022 Key amendments:**
- Pseudonymously processed information (仮名加工情報) — new category allowing internal use with less restriction than PI
- Anonymously processed information (匿名加工情報) — stricter standards for true de-identification
- Opt-out restriction: personal information that is "requiring special care" (sensitive) cannot be provided to third parties via opt-out mechanism
- Cross-border transfer: must confirm equivalent protection level in receiving country and provide individuals with required information

---

## DPDPA (India)

**Statute:** Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023). Received Presidential assent August 11 2023. **Operative provisions:** Not yet in force as of June 2026 — await Central Government notification under s. 1(2). **Enforcement:** Data Protection Board of India (DPBI). **Penalties:** Up to INR 250 Cr (approx. USD 30M) per breach per instance, scale by category.

**Note:** Rules under the DPDPA are pending. Monitor MeitY (Ministry of Electronics and Information Technology) for implementation dates and rule drafts.

### Anticipated Core Obligations

**§ 4 — Lawful basis:** Personal data may be processed only for lawful purpose with consent, or for certain legitimate uses.

**§ 6 — Purpose limitation:** Personal data shall be processed only for the purposes for which it was collected.

**§ 8(3) — Data minimization:** A Data Fiduciary shall ensure that personal data collected is limited to such data as is necessary for the specified purpose.

**§ 8(7) — Retention limitation:** Personal data shall not be retained beyond the period necessary for the specified purpose. Data Fiduciary must delete upon fulfillment of purpose or withdrawal of consent (subject to legal retention obligations).

**§ 9 — Children's data:** Processing PI of children (under 18) or persons with disabilities requires verifiable parental/guardian consent. No behavioral tracking or targeted advertising directed at children.

**§ 10 — Significant Data Fiduciaries:** Central Government may designate entities as Significant Data Fiduciaries based on volume, sensitivity, national security implications — additional obligations including periodic DPIA, data audits, appointment of Data Protection Officer.

---

## POPIA (South Africa)

**Statute:** Protection of Personal Information Act, Act 4 of 2013. Operative from July 1 2021 (commencement of enforcement). **Enforcement:** Information Regulator (IR). **Penalties:** Up to ZAR 10M or imprisonment up to 10 years.

**Eight Conditions for Lawful Processing (Chapter 3, Part A — ss. 8-25):**

| §§ | Condition | Core obligation | Minimization principle |
|---|---|---|---|
| § 8 | Accountability | Responsible party must ensure compliance | — |
| §§ 9–12 | Processing limitation | Lawful processing (s. 9); **minimality — adequate, relevant, not excessive (s. 10)**; consent/justification (s. 11); direct collection (s. 12) | P1 |
| **§§ 13–14** | **Purpose specification** | **Specific, explicitly defined, lawful purpose (s. 13); retention limited to purpose (s. 14)** | **P1, P2, P4** |
| § 15 | Further processing limitation | Further processing compatible with original purpose | P2 |
| § 16 | Information quality | Complete, accurate, not misleading, updated | P3 |
| §§ 17–18 | Openness | Documentation; data subject notified of collection | — |
| §§ 19–22 | Security safeguards | Integrity/confidentiality via technical & organisational measures; operator duties; breach notification (s. 22) | P7 |
| §§ 23–25 | Data subject participation | Access and correction rights | P4 |

*(Section ranges corrected 2026-07-05 against the Act — this table previously compressed each condition to a single shifted section number; see `.fable/reconciliation-log.md`.)*

**§ 10 (minimality, within processing limitation ss. 9–12) + § 13 (purpose specification) together constitute the POPIA minimization framework.** § 10 requires that PI be adequate, relevant, and not excessive (mirrors GDPR Art. 5(1)(c) verbatim). § 13 requires collection for a specific, explicitly defined purpose communicated to the data subject. *(Anchors corrected 2026-07-05.)*

**Special information (§ 26):** Religious/philosophical beliefs; race/ethnic origin; trade union membership; political persuasion; health/sex life; biometric information; criminal behaviour. Prohibited processing except on specific grounds in § 27.

**Direct marketing (§ 69):** Prohibition on processing for direct marketing by means of electronic communication (email, SMS, automated calls) without prior consent.

---

## Cross-Regime Field Risk Matrix

Fields that are HIGH risk under **all** regimes — always flag regardless of jurisdiction:

| Field | HIPAA | PIPEDA | GDPR | CCPA | LGPD | PIPL | APPs |
|---|---|---|---|---|---|---|---|
| Full name | PHI #1 | Cl. 4.4 | Art. 5(1)(c) | PI | Art. 6(III) | Art. 6 | APP 3 |
| Email address | PHI #6 | Cl. 4.4 | Art. 5(1)(c) | PI | Art. 6(III) | Art. 6 | APP 3 |
| IP address (full) | PHI #15 | Cl. 4.4 | Art. 5(1)(c) + CJEU | PI | Art. 6(III) | Art. 6 | APP 3 |
| Precise geolocation | PHI #2 | Cl. 4.4 | Art. 5(1)(c) | Sensitive PI | Art. 6(III) | Sensitive | APP 3 |
| Date of birth | PHI #3 | Cl. 4.4 | Art. 5(1)(c) | PI | Art. 6(III) | Art. 6 | APP 3 |
| Phone number | PHI #4 | Cl. 4.4 | Art. 5(1)(c) | PI | Art. 6(III) | Art. 6 | APP 3 |
| Device / biometric ID | PHI #13, #16 | Cl. 4.4 | Art. 5(1)(c) | PI | Art. 6(III) | Sensitive | APP 3 |
| Health data | PHI (all) | Cl. 4.4 + 4.7 | Art. 9 | Sensitive PI | Art. 11 | Sensitive | Sensitive |
| Financial account | PHI #10 | Cl. 4.4 + 4.7 | Art. 5(1)(c)+(f) | Sensitive PI | Art. 6(III) | Sensitive | APP 3 |
| Racial/ethnic origin | — | Cl. 4.7 | Art. 9 | Sensitive PI | Art. 11 | Sensitive | Sensitive |

---

## Defensible Exception Documentation

When minimization is deliberately limited (e.g., security logs needing full fidelity for detection), document with full multi-regime statutory citations. Undocumented exceptions are violations. Documented, justified exceptions with compensating controls are defensible.

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

Compensating controls:
  - Role-based access restricted to security team (logged)
  - Not replicated to analytics or marketing pipelines
  - 90-day hard TTL with automated deletion job
  - Encrypted at rest (AES-256-GCM)
  - Pseudonymized in any external-facing reports

Regulatory basis:
  HIPAA § 164.502(b): minimum necessary satisfied — full IP
    necessary for fraud detection purpose; not disclosed beyond.
  GDPR Art. 5(1)(c): "adequate" and "necessary" — three-part test
    satisfied for stated security purpose.
  GDPR Art. 25(1): privacy-by-design met via compensating controls.
  PIPEDA Cl. 4.4.1: collection not indiscriminate — documented purpose.
  PIPEDA Cl. 4.7.1: safeguards appropriate to sensitivity level.
  CCPA § 1798.100(c): reasonably necessary and proportionate
    to stated security purpose.
  LGPD Art. 6(III): limited to minimum necessary for security purpose.
  APPs APP 3.3: reasonably necessary for security function.

Review date:          [quarterly or on material change]
```

---

## GLBA / FTC Safeguards Rule (United States — Financial)

**Statutes:** Gramm-Leach-Bliley Act, 15 U.S.C. §§ 6801-6809 (1999). **FTC Safeguards Rule:** 16 CFR Part 314, substantially revised Dec 9 2021, effective June 9 2023 (enforcement). **FTC Privacy Rule:** 16 CFR Part 313 (notice obligations). **Enforcement:** Federal Trade Commission (FTC) under 15 U.S.C. § 6805. State attorneys general may also enforce. Civil penalties up to $100,000 per violation; individuals up to $10,000 and imprisonment.

**Scope:** "Financial institutions" under FTC jurisdiction — non-bank entities significantly engaged in financial activities. Explicitly includes: mortgage brokers, payday lenders, tax preparers, auto dealers, finders, credit counselors, debt collectors, investment advisers not under SEC jurisdiction. **Critical for Web3/crypto context:** The FTC has signaled that crypto exchanges, DeFi platforms, and NFT marketplaces handling "financial data" may fall under GLBA scope depending on activities. Verify current FTC guidance.

**Customer vs. Consumer distinction:**
- **Consumer:** individual who obtains a financial product or service from a financial institution (one-time relationship)
- **Customer:** consumer with a continuing relationship. Customers receive stronger protections.

### FTC Safeguards Rule — 2021 Revised Requirements (16 CFR § 314)

The 2021 revision made the Safeguards Rule significantly more specific and prescriptive — now the most detailed US privacy/security regulation outside HIPAA.

**§ 314.4 — Elements of an Information Security Program (mandatory):**

| Element | § 314.4 | Requirement | Minimization mapping |
|---|---|---|---|
| Qualified Individual | (a) | Designate a qualified individual responsible for the program | — |
| Risk Assessment | (b) | Identify reasonably foreseeable internal/external risks; assess sufficiency of safeguards | P1, P7 |
| **Safeguards — Access Controls** | **(c)(1)** | **Limit and monitor who can access customer information** | **P6** |
| **Safeguards — Data Inventory** | **(c)(2)** | **Know what customer information you have and where it is stored** | **P1, P4** |
| **Safeguards — Encryption** | **(c)(5)** | **Encrypt customer information in transit and at rest** | **P7** |
| **Safeguards — Authentication** | **(c)(6)** | **Multi-factor authentication for any individual accessing customer information** | **P7** |
| **Safeguards — Disposal** | **(c)(8)** | **Securely dispose of customer information within 2 years if no longer needed** | **P4** |
| **Safeguards — Change Management** | **(c)(9)** | **Monitor and filter for unauthorized access; change management procedures** | **P7** |
| Penetration Testing | (d)(2) | Annual penetration testing; bi-annual vulnerability assessments | — |
| Service Provider Oversight | (f) | Select/retain SPs that maintain appropriate safeguards; contractual requirements | P6 |
| Incident Response Plan | (h) | Written incident response plan with defined roles, escalation, notification | M3 |
| Board Reporting | (i) | Report to board/governing body at least annually on program status | — |

**§ 314.4(c)(2) — Data Inventory mandate:** Organizations must maintain an inventory of customer information, including where it is stored, who can access it, and how it is protected. This is the closest US analogue to GDPR Art. 30 (Records of Processing Activities). **Directly triggers `data-minimization` skill** — you cannot minimize what you haven't inventoried.

**§ 314.4(c)(5) — Encryption:** Customer information must be encrypted both in transit and at rest. No carve-outs for "low sensitivity" customer data.

**§ 314.4(c)(8) — 2-year disposal rule:** Customer information no longer needed for business purposes must be securely disposed of within 2 years of the date it was last used. This is the most specific retention/disposal mandate in US law. Triggers `data-minimization` Step 8 (Policy Mode) — the disposal policy must reflect this deadline.

**§ 314.4(c)(6) — MFA:** Multi-factor authentication required for any individual accessing customer information systems. Exemptions only if alternative control providing equivalent security is documented and approved by the qualified individual.

**§ 314.4(d) — Penetration testing:** Annual pen tests by qualified internal or external party. Results must inform risk assessment update. Vulnerability assessments every 6 months. **Direct overlap with your red team portfolio** — GLBA pen test requirements create demand for the exact skill set in offensive security roles at fintechs.

**Exception for smaller entities (§ 314.6):** Entities with fewer than 5,000 customer records are exempt from the penetration testing, vulnerability assessment, and audit trail requirements — but not from encryption, MFA, disposal, or the information security program itself.

### FTC Privacy Rule (16 CFR Part 313) — Notice Requirements

Financial institutions must provide customers with clear and conspicuous privacy notices:
- **Initial notice:** at time of establishing customer relationship
- **Annual notice:** to customers every 12 months during continuation of relationship
- **Opt-out notice:** before disclosing nonpublic personal information (NPI) to nonaffiliated third parties

**NPI definition (§ 313.3(n)):** Any personally identifiable financial information that is not publicly available — account balances, transaction history, credit scores, payment history, loan applications, any PI provided by consumer in connection with obtaining financial product/service.

### Schema Implications

Any schema in a GLBA-scoped entity must:
- Include `disposal_date` or `last_used_date` field with 2-year TTL enforcement
- Encrypt NPI fields at rest (document encryption method)
- Log all access to customer information (audit trail)
- Inventory all tables/collections containing NPI (§ 314.4(c)(2))

---

## Singapore PDPA

**Statute:** Personal Data Protection Act 2012 (No. 26 of 2012), substantially amended by Personal Data Protection (Amendment) Act 2020 (No. 40 of 2020), effective Feb 1 2021. **Enforcement:** Personal Data Protection Commission (PDPC). **Penalties:** Up to SGD 1M or 10% of annual turnover in Singapore (whichever higher, for egregious cases post-2020 amendment).

**Scope:** Applies to organisations that collect, use, or disclose personal data of individuals in Singapore. Extraterritorial where processing relates to individuals in Singapore.

### Data Protection Obligations (Second Schedule, PDPA)

| Obligation | Section | Core requirement | Minimization principle |
|---|---|---|---|
| **Collection Limitation** | **s. 18** | **Collect personal data only for purposes that a reasonable person would consider appropriate** | **P1** |
| Purpose Limitation | s. 18 | Collect, use, disclose only for purposes individual was notified of and consented to | P2 |
| Notification | s. 20 | Notify individual of purposes before or at time of collection | P2 |
| Consent | s. 14-17 | Obtain voluntary, informed consent; deemed consent provisions | P1, P2 |
| Accuracy | s. 23 | Make reasonable efforts to ensure personal data is accurate/complete | P3 |
| **Retention Limitation** | **s. 25** | **Cease retention when purpose no longer served and retention not required by law** | **P4** |
| Transfer Limitation | s. 26 | Transfer to another country only if recipient provides comparable protection | P6 |
| **Protection** | **s. 24** | **Reasonable security arrangements to prevent unauthorised access/collection/use/disclosure/copying/modification/disposal** | **P7** |
| Data Breach Notification | s. 26C-26H | Notify PDPC within 3 calendar days; notify individuals if significant harm likely | M2, M3 |

**s. 18 — "Reasonable person" collection standard:** Unlike GDPR's necessity test or CCPA's proportionality test, PDPA asks whether a reasonable person would consider the purpose appropriate. This is a lower but vaguer standard. PDPC has issued numerous advisory guidelines providing examples.

**2020 Amendment — Mandatory Data Breach Notification (s. 26C-26H):**
- Notify PDPC within **3 calendar days** of becoming aware of a notifiable breach
- Notify affected individuals if breach is likely to result in significant harm — no fixed timeline but "as soon as practicable"
- Significant harm: financial loss, physical/psychological harm, humiliation, damage to reputation — PDPC advisory guidelines provide examples
- Estimated 500+ individuals affected triggers mandatory PDPC notification regardless of harm assessment

**2020 Amendment — Expanded deemed consent (s. 15A-15D):**
- Deemed consent by contractual necessity
- Deemed consent by notification (with opt-out mechanism)
- Legitimate interests exception (proportionality test required)

**2020 Amendment — Data Portability Obligation (Pt. VIA):** Organisations designated by Minister must port customer data to other organisations on customer request, in machine-readable format. Phased implementation — currently applies to banks and telecommunications.

**Exceptions to consent (Second Schedule):** Research/news/artistic exceptions; legal proceedings; life-threatening emergencies; publicly available data. Narrower than GDPR legitimate interests but meaningful for security research contexts.

### Do Not Call Registry (Part IX, PDPA)

Separate regime prohibiting unsolicited voice/text/fax marketing to Singapore numbers on the DNC Registry. Penalties up to SGD 10,000 per message. Note: this applies to marketing, not transactional communications.

---

## ePrivacy Directive (EU)

**Directive 2002/58/EC** of the European Parliament and of the Council of 12 July 2002, concerning the processing of personal data and the protection of privacy in the electronic communications sector (Directive on privacy and electronic communications). Amended by Directive 2009/136/EC (Cookie Directive). Implemented by member state national law.

**Status of ePrivacy Regulation:** Proposed replacement regulation (COM/2017/10 final) has been stalled in EU legislative process since 2017. The Directive remains operative law. As of June 2026, ePrivacy Regulation adoption remains uncertain — monitor EU legislative tracker.

**Relationship to GDPR:** ePrivacy Directive is *lex specialis* to GDPR — it takes precedence for electronic communications processing. Where ePrivacy Directive applies, GDPR's legal bases do not substitute for ePrivacy consent requirements. This is the source of the "cookie wall" and "consent or pay" debates.

### Core Provisions

**Art. 5(3) — Cookie / Tracking Consent:**
Storage of information or access to information already stored on terminal equipment requires:
1. Clear and comprehensive information provided to the user about purposes
2. User's **consent** (per GDPR Art. 4(11) — freely given, specific, informed, unambiguous indication)

**Exemption from consent (Art. 5(3)):** Technical storage/access strictly necessary for:
- Providing an information society service explicitly requested by the subscriber
- The sole purpose of carrying out transmission of a communication

**Consent-exempt cookies (EDPB guidance):** Session authentication, load balancing, shopping cart state, user preference cookies set in response to explicit user action. NOT exempt: analytics, advertising, A/B testing, social media plugins, CDN fingerprinting.

**Scope of "terminal equipment":** Expands beyond cookies to cover: local storage, IndexedDB, device fingerprinting, pixel tracking, link decoration, canvas fingerprinting, audio fingerprinting. Any method of accessing information on or writing to a user's device.

**Art. 6 — Traffic data:** Traffic data (IP addresses, routing data, duration, time, data volume, protocol) may only be processed for: transmission billing, interconnection payments, fraud detection, network management. Must be erased or anonymised when no longer needed for these purposes. **Traffic data is NOT usable for analytics or advertising without consent.**

**Art. 9 — Location data:** Location data (beyond what is necessary for transmission) requires consent for value-added services. Must be anonymised or user must be given opportunity to withdraw consent for each transmission session.

**Art. 13 — Unsolicited communications:** Prior consent required for email, SMS, automated calls for direct marketing purposes. Soft opt-in exception: existing customer relationship + marketing for similar products/services + clear opt-out provided.

### Global Privacy Control (GPC)

W3C Community Group specification. A browser-level signal (`Sec-GPC: 1` HTTP header + `navigator.globalPrivacyControl` JS API) indicating user's opt-out preference. **Legal status:**
- California: CPPA regulations (Cal. Code Regs. tit. 11, § 7026) require honoring GPC as a valid opt-out of sale/sharing under CCPA § 1798.135
- Colorado CPA: Attorney General rules require honoring universal opt-out signals including GPC
- ePrivacy: EDPB Opinion 8/2024 on GPC acknowledged it as a valid mechanism for ePrivacy Art. 5(3) consent withdrawal — but not as initial consent
- **Schema implication:** If you set first-party cookies or use tracking on any EU or California-facing product, your data pipeline must respect GPC signals and not fire analytics/advertising trackers for users sending `Sec-GPC: 1`

---

## EU AI Act

**Regulation (EU) 2024/1689** of the European Parliament and of the Council of 13 June 2024 on artificial intelligence. Published OJ L 2024/1689 Jul 12 2024. **Phased application:** Prohibited practices — Feb 2 2025. GPAI models — Aug 2 2025. High-risk AI systems: **Annex III — Dec 2 2027; Annex I (embedded products) — Aug 2 2028** (deferred by the Digital Omnibus on AI, adopted Jun 2026; AI-generated-content marking Dec 2 2026; other Art. 50 transparency Aug 2 2026). **Enforcement:** National market surveillance authorities; European AI Office for GPAI models. **Penalties:** Up to €35M or 7% global annual turnover (prohibited practices); €15M or 3% (other provisions); €7.5M or 1% (incorrect information).

**Scope:** Providers placing AI systems on EU market or putting into service in EU; providers/deployers in third countries where output is used in EU. Extraterritorial — mirrors GDPR scope logic.

### Prohibited AI Practices (Art. 5) — Privacy-Relevant Prohibitions

Prohibited as of Feb 2 2025:

**Art. 5(1)(e) — Real-time remote biometric identification in public spaces by law enforcement.** Narrow exceptions for specific serious crimes with judicial/independent authority authorisation.

**Art. 5(1)(g) — Emotion recognition in workplace and educational institutions.** Prohibited except for medical/safety purposes. Note: narrow — doesn't prohibit emotion recognition generally, only in these specific contexts.

**Art. 5(1)(h) — Biometric categorisation systems** inferring sensitive attributes (race, political opinions, trade union membership, religious beliefs, sexual orientation, health status) from biometric data. Prohibition covers building databases.

### High-Risk AI Systems — Data Governance Requirements (Art. 10)

Art. 10 applies to high-risk AI systems listed in Annex III: biometric ID and categorisation, critical infrastructure, education, employment, essential services, law enforcement, migration/asylum, administration of justice.

**Art. 10(2) — Training data governance:**
Training, validation, and testing datasets shall be subject to data governance practices covering:
- (a) relevant design choices
- (b) data collection processes and origin
- (c) relevant data preparation processing operations (labelling, cleaning, enrichment, aggregation)
- (d) formulation of relevant assumptions, notably with respect to the information data is supposed to measure and represent
- (e) **assessment of availability, quantity and suitability**
- (f) **examination in view of possible biases** that are likely to affect health and safety or fundamental rights
- (g) identification of any possible data gaps or shortcomings, and how those gaps are addressed

**Art. 10(3) — Data minimization for training:** Training datasets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. **"To the best extent possible" qualified minimization.** This is the first explicit statutory data minimization requirement for ML training data — not just collected/processed data, but training corpora.

**Art. 10(5) — Special category data in training:** To the extent strictly necessary for the purposes of ensuring bias detection and correction in high-risk AI systems, providers may exceptionally process special categories of personal data — subject to appropriate safeguards. This carves out a bias-auditing exception to GDPR Art. 9 prohibition.

**Art. 12 — Record keeping (logging):** High-risk AI systems must automatically log events during operation ("logs") to the extent technically feasible. Logs retained for minimum period — national law / provider policy where no mandatory period specified. **Tension with GDPR Art. 5(1)(e) storage limitation** — AI Act mandates logging, GDPR demands minimizing retention. Manage via tiered retention with TTLs on sensitive log fields.

**Art. 13 — Transparency:** High-risk AI systems must be transparent — provide sufficient information to deployers to interpret outputs and use appropriately.

**Art. 9 — Risk Management System:** Iterative risk management throughout lifecycle, including:
- Identification and analysis of known and foreseeable risks
- Estimation and evaluation of risks
- Evaluation of risks arising from post-market data

**General Purpose AI (GPAI) Models — Art. 53:**
Providers of GPAI models must (effective Aug 2 2025):
- Maintain technical documentation
- Make available information and documentation to downstream providers
- Publish summary of training data (Art. 53(1)(d)) — copyright compliance + data source disclosure
- **Comply with EU copyright law** — specifically the text and data mining exceptions (DSM Directive Art. 4 opt-out mechanism)

**GPAI models with systemic risk (Art. 55):** Models trained with >10^25 FLOPs presumed to have systemic risk. Additional obligations: adversarial testing, incident reporting, cybersecurity.

### AI Act × Privacy Suite Integration

| AI Act Requirement | Privacy Suite Skill | Mapping |
|---|---|---|
| Art. 10(3) training data minimization | `data-minimization` | P1 — apply to training corpus selection |
| Art. 10(2)(f) bias examination | `data-minimization` → quasi-identifiers | Sensitive attribute detection in training data |
| Art. 9 risk management | `threat-model-privacy` | Adversary profiling + attack surface for AI system |
| Art. 12 logging | `data-minimization` | Retention TTLs on AI operation logs |
| Art. 5(1)(h) biometric categorisation | `redact` | Strip biometric-inferrable fields from training data |
| Art. 53(1)(d) training data summary | `data-minimization` | Data inventory + origin documentation → policy mode output |


---

## BIPA (Illinois — Biometric Data)

**Statute:** Biometric Information Privacy Act, 740 ILCS 14/1 et seq. (2008). **Enforcement:** Private right of action — no state AG enforcement required. Class actions are routine. **Penalties:** $1,000 per negligent violation; $5,000 per intentional/reckless violation; attorney's fees and costs. No cap on aggregate damages; no proof of actual harm required.

**BIPA is the most-litigated US privacy law.** Illinois courts have consistently allowed class actions with per-violation damages, producing verdicts and settlements in the hundreds of millions. Google ($100M, 2022), Facebook/Meta ($650M, 2021), TikTok ($92M, 2021), BNSF Railway ($228M jury verdict, 2022). Any product or employer touching biometric data in Illinois faces existential class action risk.

**Biometric identifiers covered (§ 10):**
- Retina or iris scan
- Fingerprint
- Voiceprint
- Scan of hand or face geometry
- Any other biometric identifier
- **NOT covered:** written signatures, photographs, physical description, demographic data, tattoo description

**Biometric information:** Any information based on a biometric identifier used to identify an individual.

**Core obligations:**

**§ 15(a) — Retention and destruction policy (MANDATORY BEFORE COLLECTION):**
Private entities must:
1. Develop a written policy establishing a retention schedule
2. Establish guidelines for permanent destruction
3. Make the policy publicly available

No collection without this policy being in place. **Many companies lose cases solely on this requirement.**

**§ 15(b) — Informed written consent (MANDATORY BEFORE COLLECTION):**
Must:
1. Inform the subject in writing of the specific purpose and length of collection
2. Obtain a written release signed by the subject (or authorized representative)

```
BIPA CONSENT LANGUAGE:

[COMPANY NAME] is collecting your [fingerprint / facial geometry / voiceprint]
(biometric information) for the purpose of [specific purpose — e.g. "employee
time-keeping authentication"].

Your biometric information will be stored for [specific period — e.g. "the
duration of your employment, and will be permanently destroyed within 3 years
of your last use or within 1 year of termination, whichever is first"].

By signing below, you authorize [COMPANY NAME] to collect, use, and store
your biometric information as described above.

Signature: _________________ Date: _________
```

**§ 15(c) — Prohibition on profit:** Must not sell, lease, trade, or profit from biometric data.

**§ 15(d) — Disclosure restriction:** Must not disclose or disseminate biometric data unless:
- Individual consents
- Disclosure required by law
- Disclosure required by valid warrant or subpoena

**§ 15(e) — Security standard:** Must store biometric data using the same or higher standard as other confidential/sensitive information. Transmit only using the standard of care within the industry.

**Statute of limitations:** 5 years from violation. Class period can extend 5 years back from filing.

**Accrual:** Each collection without consent = one violation. For a workplace with 500 employees scanned daily for a year → potentially hundreds of thousands of violations.

**Minimization mapping:** P1 (collect only what necessary — don't collect biometrics if PIN/password works); P7 (security standard explicitly required); P4 (retention schedule mandatory — the statute requires TTL).

**Other states with biometric laws (less litigated but growing):**
- Texas: Capture or Use of Biometric Identifier Act (CUBI), Tex. Bus. & Com. Code § 503.001 — no private right of action (AG enforcement only)
- Washington: My Health My Data Act (2023) — broad health data; AG enforcement
- New York City: Local Law 894 / Biometric Identifier Information Law — commercial establishments
- California: CCPA covers biometric data as sensitive PI; additional CPRA protections

---

## NIS2 Directive (EU — Cybersecurity)

**Directive (EU) 2022/2555** of the European Parliament and of the Council of 14 December 2022 (NIS2). Repeals NIS1 (2016/1148). **Transposition deadline:** 17 October 2024. **Enforcement:** National competent authorities and CSIRTs (Computer Security Incident Response Teams).

**Scope:** Entities in sectors deemed critical to economy and society:
- **Essential entities:** Energy, transport, banking, financial market infrastructure, health, drinking water, wastewater, digital infrastructure, ICT service management, public administration, space
- **Important entities:** Postal/courier, waste management, chemicals, food, manufacturing (medical devices, computers, electronics, machinery, motor vehicles), digital providers, research

**Also covers:** DNS providers, TLD registries, cloud computing, data centers, CDNs, Trust Service Providers, electronic communications.

**Privacy intersection:** NIS2 is not a privacy law — it is a cybersecurity law. But it intersects with privacy in three ways:

**1. Incident reporting (Art. 23) — creates mandatory security event logging:**

Early warning within **24 hours** of becoming aware of a significant incident.
Full incident notification within **72 hours** (including initial assessment, severity, indicators of compromise).
Intermediate report on request from CSIRT/authority.
Final report within **1 month** (detailed description, type of threat, mitigation measures, cross-border impact).

"Significant incident" — causes or can cause severe operational disruption, financial loss, or affects other persons by causing considerable material or non-material damage.

**2. Security measures (Art. 21) — mandatory minimum measures:**
- Risk analysis and information system security policies
- Incident handling
- Business continuity (backup, disaster recovery, crisis management)
- Supply chain security (MCP server vetting directly relevant)
- Secure acquisition, development, maintenance
- Policies for assessing effectiveness of cybersecurity risk measures
- Basic cyber hygiene and training
- **Cryptography and encryption policies** — directly triggers `privacy-architecture` skill
- Human resources security, access control, asset management
- Multi-factor authentication (Art. 21(2)(j))

**3. Board accountability (Art. 20):** Management bodies of essential and important entities must approve cybersecurity risk management measures and are personally liable for infringements. CEOs/boards cannot delegate cybersecurity accountability.

**Penalties:**
- Essential entities: up to €10M or 2% global annual turnover (whichever higher)
- Important entities: up to €7M or 1.4% global annual turnover

**Relevance to Delegate Scout:** If Exchange.Art or any Solana infrastructure provider is classified as a financial market infrastructure or digital provider in the EU, NIS2 security obligations apply including incident reporting and supply chain security requirements. Delegate Scout's security event logging design (OCSF + on-chain attestation) aligns with NIS2 Art. 23 incident documentation requirements.

---

## DORA (EU — Digital Operational Resilience, Financial Sector)

**Regulation (EU) 2022/2554** on digital operational resilience for the financial sector (DORA). **Application date:** 17 January 2025. **Enforced by:** National financial supervisory authorities (e.g., ECB for significant institutions, BaFin for German entities).

**Scope:** Financial entities — credit institutions, payment institutions, investment firms, crypto-asset service providers (**CASPs under MiCA**), insurance undertakings, credit rating agencies, crowdfunding platforms, and their critical ICT third-party service providers.

**Key DORA requirements with privacy intersection:**

**Art. 9 — Information security:** Financial entities must develop a comprehensive information security policy. Specifically requires:
- Encryption of data at rest and in transit (Art. 9(2)) — maps to our P7
- Access control, strong authentication
- Data classification and data quality policies

**Art. 10 — ICT operations security:** Logging of ICT operations, detection of anomalous activities, documented incident management procedures.

**Art. 17 — ICT-related incident classification:** Mandatory classification of ICT incidents. Significant incidents must be reported to competent authority. Classification criteria include:

| Criterion | Threshold |
|---|---|
| Clients affected | >10% of clients or >50,000 clients impacted |
| Duration | Incident lasted > 24 hours or recurring |
| Data affected | Data loss affecting > 0.1% of assets under management |
| Geographic spread | Incidents in ≥ 3 EU member states |
| Reputation | Significant media coverage; regulatory scrutiny |

**Incident reporting timeline:**
- **Initial notification:** Within 4 hours of major incident classification (or within 24 hours of becoming aware if major incident not yet classified)
- **Intermediate report:** Within 72 hours
- **Final report:** Within 1 month

**Art. 28-30 — Third-party ICT risk:** Financial entities must manage ICT third-party risk. Critical ICT third-party providers are directly supervised by EU financial regulators. Contracts with ICT providers must include: data location, audit rights, security standards, incident reporting obligations.

**DORA × Privacy:** Any crypto-asset service provider (CASP) operating under MiCA in the EU and using cloud, SaaS, or AI tooling must comply with DORA's third-party risk requirements. If OpenClaw or similar AI agent infrastructure is used by a CASP, the CASP must conduct due diligence on that infrastructure as a third-party ICT provider.

---

## Korea PIPA (South Korea)

**Statute:** Personal Information Protection Act (개인정보 보호법), Act No. 11990 (2011), substantially amended 2023 (Act No. 19234). **Enforcement:** Personal Information Protection Commission (PIPC). **Penalties:** Up to KRW 300M (~USD 230K) per violation; up to 3% of annual revenue for data breach; criminal penalties up to 5 years / KRW 50M.

**Extraterritorial scope:** Applies to entities processing PI of Korean nationals, regardless of location.

**Korea PIPA is among the world's strictest biometric privacy regimes.** Under Art. 23, sensitive information (including biometrics) requires explicit separate consent and storage with technical/administrative safeguards distinct from other PI.

**Sensitive information (Art. 23):** Ideology, religion, labor union / political party membership, political views, health/medical records, sexual life, genetic information, criminal records, biometrics for unique individual identification, racial/ethnic origin.

**Key minimization provisions:**

**Art. 3 — Data protection principles:**
- (1) Specify purpose clearly; collect to minimum necessary
- (3) Collect only what is necessary
- (5) Ensure accuracy, completeness, and currency
- (6) Implement technical/managerial/physical safeguards
- (7) Process anonymously to extent possible

**Art. 16 — Collection limitation:** Collect minimum PI necessary for the stated purpose.

**Art. 21 — Destruction:** Destroy PI without delay when retention period expires or purpose achieved. Destruction method must be irreversible.

**Art. 35-40 — Data subject rights:** Access, correction, deletion, suspension of processing, portability (added in 2023 amendment).

**2023 amendment key changes:**
- Right to portability (Art. 35-2) — machine-readable format, transfer to other controllers
- Pseudonymization safe harbor (Art. 28-2) expanded
- Cross-border transfer provisions updated — adequacy decisions and Standard Protection Clauses (SPCs, Korea's SCC equivalent)
- Legal basis for processing strengthened — legitimate interests doctrine added (previously consent-dominated)
- PIPC enhanced enforcement powers

**Breach notification (Art. 34):** Notify affected individuals "without delay" (PIPC guidance: within 5 days). Notify PIPC for large-scale breaches (over 1,000 individuals).

---

## nFADP (Switzerland)

**Statute:** Federal Act on Data Protection (Bundesgesetz über den Datenschutz, DSG / nFADP), SR 235.1. New version in force **1 September 2023**. Replaces 1992 FADP. **Enforcement:** Federal Data Protection and Information Commissioner (FDPIC). **Penalties:** Criminal fines up to CHF 250,000 against responsible individuals (not entities — unusual).

**Scope:** Processing of PI of natural persons in Switzerland by private persons and federal bodies. Applies to processing in Switzerland and to processing with effects in Switzerland (extraterritorial scope similar to GDPR).

**GDPR adequacy:** Switzerland maintains EU adequacy status — PI can flow freely between EU and Switzerland. nFADP alignment with GDPR was intentional.

**Key differences from GDPR:**

| Aspect | GDPR | Swiss nFADP |
|---|---|---|
| Fines | Up to €20M / 4% turnover (entity) | Up to CHF 250,000 (individual) |
| Legal bases | 6 bases including legitimate interests | Principles-based; processing permitted if proportionate to purpose |
| Sensitive data | Special categories requiring explicit legal basis | Sensitive PI requiring justification (broader category) |
| DPO | Mandatory for high-risk processing | Voluntary; FDPIC recommends for large-scale processing |
| DPIA | Mandatory for high-risk (Art. 35) | Data protection impact assessment for high-risk processing (Art. 22) |
| Breach notification | 72 hours to DPA | "As soon as possible" to FDPIC; no fixed timeline |
| Profiling | Regulated (Art. 22) | High-risk profiling requires explicit consent or other justification |

**Sensitive PI under nFADP (Art. 5(c)) — broader than GDPR Art. 9:**
- Religious, ideological, political, or trade union views
- Health, intimate sphere, or racial origin
- Social welfare measures
- Administrative and criminal proceedings/sanctions
- **Genetic data** (explicitly listed)
- **Location data** (if revealing sensitive context)
- **Biometric data** uniquely identifying a person

**Art. 6 — Proportionality principle:** PI processing must be proportionate to the purpose. Effectively a data minimization requirement phrased as proportionality.

**Art. 7 — Privacy by design and by default** (analogous to GDPR Art. 25): Technical and organizational measures; privacy-friendly default settings.

**Registration requirement (Art. 12):** High-risk profiling by private persons requires prior notification to FDPIC (equivalent to GDPR DPIA registration) if no DPO appointed.

---

## Additional Jurisdictions — Briefer Entries

### Vietnam PDPD (Decree 13/2023/ND-CP)

**Effective:** 1 July 2023. **Authority:** Ministry of Public Security (MPS). **Penalties:** Administrative fines up to VND 5B (~USD 200K); criminal liability for serious violations.

**Key provisions:** Two categories of personal data: "basic" and "sensitive" (requiring explicit consent). Sensitive data includes: political views, religion, health, sexual orientation, criminal records, genetic data, biometric data, financial data, geolocation. **Data localization:** Personal data of Vietnamese citizens that is collected, exploited, and used in Vietnam must be stored in Vietnam (Art. 26). Cross-border transfer requires MPS approval or self-assessment. **Consent requirement:** Explicit, voluntary, informed consent for each specific purpose.

### Thailand PDPA (PDPA B.E. 2562)

**Effective:** 1 June 2022. **Authority:** Personal Data Protection Committee (PDPC). **Penalties:** Up to THB 5M civil; up to THB 1M + 1 year imprisonment criminal.

**Closely modeled on GDPR.** Six lawful bases including consent and legitimate interests. Sensitive PI (health, racial origin, religion, political opinion, criminal records, biometrics, genetic data, sexual orientation, disability) requires explicit consent or specific exemption. 72-hour breach notification to PDPC. Data subject rights: access, rectification, deletion, restriction, portability, objection.

### Nigeria NDPA 2023

**Statute:** Nigeria Data Protection Act 2023 (NDPA), signed June 2023. Replaces Nigeria Data Protection Regulation (NDPR) 2019. **Authority:** Nigeria Data Protection Commission (NDPC). **Penalties:** Up to NGN 10M (~USD 13K) or 2% of annual gross revenue (whichever higher).

**Extraterritorial scope:** Applies to processing of PI of persons in Nigeria regardless of where the controller is located. Nigeria has 220M+ population — Africa's largest economy. GDPR-aligned six lawful bases; data subject rights; 72-hour breach notification; DPO requirement for large-scale or sensitive data processors.

### UAE PDPL (Federal Decree-Law No. 45 of 2021)

**Effective:** 2 January 2022 (implementing regulations in force 2023). **Authority:** UAE Data Office. **Penalties:** Up to AED 5M (~USD 1.4M); up to AED 20M for intentional/systematic violations.

**Scope:** Processing of personal data of individuals in UAE by entities operating in UAE. Special note: DIFC (Dubai International Financial Centre) and ADGM (Abu Dhabi Global Market) have their own separate data protection frameworks (DIFC DP Law 2020; ADGM Data Protection Regulations 2021) — each requires separate analysis.

**Key provisions:** Six lawful bases including consent and legitimate interests; sensitive data (health, financial, genetic, biometric, criminal records, children's data) requires explicit consent; cross-border transfer requires UAE Data Office approval or adequacy assessment; data subject rights similar to GDPR.

---

## Updated Jurisdiction Quick-Select (Complete)

| Jurisdiction | Statute | Enforcement | Key minimization hook |
|---|---|---|---|
| 🇨🇦 Canada (federal) | PIPEDA, S.C. 2000, c. 5 | OPC | Clause 4.4 |
| 🇨🇦 Canada (Quebec) | Law 25, S.Q. 2021, c. 25 | CAI | Art. 63.5 (PIA), Art. 9 |
| 🇪🇺 EU / EEA | GDPR, Reg. EU 2016/679 | National DPAs | Art. 5(1)(c) |
| 🇬🇧 UK | UK GDPR + DPA 2018 | ICO | Art. 5(1)(c) |
| 🇺🇸 Healthcare | HIPAA, 45 CFR Parts 160, 164 | HHS OCR | § 164.502(b) |
| 🇺🇸 California | CCPA/CPRA, Cal. Civ. Code §§ 1798.100+ | CPPA | § 1798.100(a)(3) |
| 🇺🇸 Children | COPPA, 15 U.S.C. §§ 6501-6506 | FTC | § 6502(b)(1) |
| 🇺🇸 Biometrics (IL) | BIPA, 740 ILCS 14/ | Private litigation | § 15(b) consent; § 15(a) retention policy |
| 🇺🇸 Financial | GLBA/FTC Safeguards, 16 CFR Part 314 | FTC | § 314.4(c)(2) |
| 🇧🇷 Brazil | LGPD, Law No. 13,709/2018 | ANPD | Art. 6(III) |
| 🇨🇳 China | PIPL, effective Nov 1 2021 | CAC / SAMR | Art. 6 |
| 🇦🇺 Australia | Privacy Act 1988 + APPs | OAIC | APP 3.3 |
| 🇯🇵 Japan | APPI (amended 2022) | PPC | Art. 17(1) |
| 🇮🇳 India | DPDPA 2023 | DPBI | § 6(1) |
| 🇿🇦 South Africa | POPIA, Act 4 of 2013 | Information Regulator (IR) | § 10 |
| 🇸🇬 Singapore | PDPA 2012 (amended 2020) | PDPC | s. 18 |
| 🇪🇺 ePrivacy | Directive 2002/58/EC | National DPAs | Art. 5(3) |
| 🇪🇺 AI Act | Reg. 2024/1689 | National + AI Office | Art. 10(3) |
| 🇪🇺 NIS2 | Directive 2022/2555 | National + CSIRTs | Art. 21 security measures |
| 🇪🇺 DORA | Reg. 2022/2554 | Financial supervisors | Art. 9 (encryption); Art. 17 (incident logging) |
| 🇰🇷 South Korea | PIPA (amended 2023) | PIPC | Art. 3(3), Art. 16 |
| 🇨🇭 Switzerland | nFADP, SR 235.1 (Sept 2023) | FDPIC | Art. 6 (proportionality) |
| 🇻🇳 Vietnam | PDPD, Decree 13/2023 | MPS | Art. 9 (minimization) |
| 🇹🇭 Thailand | PDPA B.E. 2562 (2022) | PDPC | Sec. 22 (minimization) |
| 🇳🇬 Nigeria | NDPA 2023 | NDPC | Sec. 24 (minimization) |
| 🇦🇪 UAE | PDPL, Fed. Decree-Law 45/2021 | UAE Data Office | Art. 4 (minimization) |

---

## Additional Sector-Specific Frameworks

### FERPA (United States — Educational Records)

**Statute:** Family Educational Rights and Privacy Act, 20 U.S.C. § 1232g; implementing regulations at 34 CFR Part 99. **Enforcement:** US Department of Education (Family Policy Compliance Office). No private right of action — enforcement via withdrawal of federal funding.

**Scope:** Educational agencies and institutions that receive federal funding. Covers "education records" — records directly related to a student maintained by the institution.

**Core obligations:**
- **Disclosure restriction:** Schools may not disclose education records without written consent except under enumerated exceptions (school officials with legitimate educational interest; transfer schools; financial aid; judicial orders; health/safety emergencies)
- **Parent/student rights:** Right to inspect and review; right to request amendment; right to file complaint
- **Directory information:** Schools may disclose "directory information" (name, address, phone, dates of attendance, degrees earned) unless student opts out

**Minimization mapping:** FERPA's "legitimate educational interest" standard for disclosure is a purpose limitation and minimization requirement — staff may access only records needed for their function (P1, P2, P6).

**Interaction with HIPAA:** Health records at schools are generally FERPA-covered, not HIPAA-covered. Exception: records maintained by a school health professional in their capacity as a health care provider → HIPAA applies to those specific records.

**Relevant when:** Any product touching US K-12 or higher education student data; EdTech platforms; school management systems; student information systems.

### Argentina — Habeas Data (Law 25.326)

**Statute:** Ley de Protección de los Datos Personales No. 25.326 (2000). **Enforcement:** Agencia de Acceso a la Información Pública (AAIP). **EU adequacy:** Yes — Argentina has EU adequacy decision (Commission Decision 2003/490/EC). Data can flow freely between EU and Argentina.

**Key provisions:** Consent required for collection and processing; sensitive data (health, political opinions, religion, sexual orientation, criminal records) requires heightened protection; data subject rights (access, rectification, deletion — "habeas data" constitutional right); 5-year statute of limitations. Cross-border transfers permitted to countries with adequate protection (EU, Canada) or with consent.

**Relevance:** 45M+ population; significant tech sector; GDPR adequacy means EU data controllers can transfer to Argentine processors without additional safeguards.

### New Zealand — Privacy Act 2020

**Statute:** Privacy Act 2020 (in force Dec 1, 2020). **Enforcement:** Privacy Commissioner. **Penalties:** Up to NZD 10,000 for specified offences; Commissioner can issue compliance notices.

**13 Information Privacy Principles (IPPs):** Closely follow GDPR structure. IPP 3 (collection only from individual where practicable), IPP 4 (collection for lawful purpose connected to function), IPP 5 (retention only as long as necessary), IPP 9 (don't use for purpose other than collected for), IPP 11 (disclosure limitation), IPP 12 (unique identifiers — restricted use).

**Mandatory breach notification:** Must notify Commissioner and affected individuals of privacy breaches causing "serious harm." Commissioner publishes breach register.

**Relevance:** New Zealand is a Five Eyes intelligence-sharing member (US, UK, Canada, Australia, NZ) — relevant for security tooling crossing these jurisdictions. GDPR-aligned; design to GDPR standard provides NZ compliance.

---

## Synthetic Data — Minimization-Compatible Alternative

**What it is:** Algorithmically generated data that preserves the statistical properties of a real dataset without containing any real personal data. Used as a privacy-safe alternative for sharing, analytics, ML training, and testing.

**GDPR status:** Synthetic data that cannot be linked to real individuals is not personal data (Recital 26 — truly anonymous data outside scope). But generating synthetic data from real PI is itself a processing activity requiring a legal basis.

**Generation methods:**

| Method | Privacy guarantee | Utility | Use case |
|---|---|---|---|
| Statistical sampling | Moderate | High | Simple tabular data |
| GAN (Generative Adversarial Network) | Moderate | Very high | Complex distributions |
| Variational Autoencoder (VAE) | Moderate | High | Mixed data types |
| Differential privacy + synthesis (DP-SGD) | High (provable ε-DP) | Medium | Regulated sector |
| Rule-based generation | High | Medium | Structured schemas |

**Membership inference risk:** Standard GAN-generated synthetic data can leak membership information — an adversary can determine with high probability whether a specific individual's record was in the training set. DP-synthetic data (training the generator with differential privacy) provides a provable bound on this leakage.

**Libraries:**
- `Synthpop` (R) — statistical synthesis; good for tabular data
- `SDV` (Synthetic Data Vault, Python) — GAN/VAE based; most feature-complete
- `Gretel.ai` — managed synthetic data service; GDPR-compliant by design
- `CTGAN` (Python) — conditional tabular GAN
- `SmartNoise` (Python, OpenDP) — differentially private synthetic data

**Minimization mapping:** Synthetic data is the ultimate application of P1 (collection limitation) — if synthetic data serves the purpose, no real PI needs to be collected or shared. Also directly satisfies the GDPR Art. 25 privacy-by-design obligation for analytics and testing workflows.

**Remediation action in field inventory:** Add `SYNTHESIZE` to the remediation vocabulary — "Replace this dataset with differentially private synthetic data before sharing with [third party / analytics team / ML pipeline]."
