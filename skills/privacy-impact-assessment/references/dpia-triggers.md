# DPIA Triggers Reference

Per-regime mandatory trigger checklists. Run before Phase 1 intake.

---

## GDPR Art. 35 — Full Trigger Analysis

### Art. 35(3) — Automatic Mandatory Triggers (any ONE = mandatory)

☐ **35(3)(a):** Systematic and extensive evaluation of personal aspects relating to natural persons based on automated processing, including profiling, and on which decisions are taken that have a significant effect on individuals.

Examples: Credit scoring, insurance risk assessment, fraud detection ML, hiring algorithm screening, price personalisation, behavioural advertising with automated bidding.

☐ **35(3)(b):** Processing on a large scale of special categories of data (Art. 9) or criminal conviction data (Art. 10).

Special categories: health, biometric, genetic, racial/ethnic origin, political opinions, religious beliefs, sexual orientation, trade union membership.

Large scale: EDPB guidance — consider number of data subjects, volume of data, geographic extent, duration/permanence. No fixed threshold — context-dependent. Processing of an entire city's health data = large scale. Processing of a single hospital's patient records = not necessarily large scale. Processing 100,000+ individuals' health data across a region = large scale.

☐ **35(3)(c):** Systematic monitoring of a publicly accessible area on a large scale.

Examples: CCTV systems, drone surveillance, WiFi tracking in public spaces, geolocation tracking of individuals through a city, smart city sensor networks.

### EDPB Guidelines 09/2022 — Nine Criteria (TWO OR MORE = mandatory)

Work through each. Mark Y (yes), N (no), U (uncertain).

**Criterion 1 — Evaluation or scoring (including profiling and predicting)**
Processing involves evaluating, scoring, or predicting aspects concerning data subjects' performance at work, economic situation, health, personal preferences, interests, reliability, behaviour, location, or movements.
☐ Y / N / U

**Criterion 2 — Automated decision-making with legal or similarly significant effects**
Processing enables decisions that produce legal effects concerning the data subject or that similarly significantly affect them.
☐ Y / N / U

Significant effect examples: denial of credit, employment decisions, insurance pricing, law enforcement profiling, access to essential services.

**Criterion 3 — Systematic monitoring**
Processing used to observe, monitor, or control data subjects, including collection via networks or "systematic monitoring of a publicly accessible area."
☐ Y / N / U

**Criterion 4 — Sensitive data or data of a highly personal nature**
Processing involves special categories (Art. 9) or data of a highly personal nature: financial data, location data, communications data, children's data, HR data.
☐ Y / N / U

**Criterion 5 — Data processed on a large scale**
See Art. 35(3)(b) guidance above. Consider volume, number of subjects, geographic scope, duration.
☐ Y / N / U

**Criterion 6 — Matching or combining datasets**
Combining, matching, or cross-referencing datasets originating from two or more processing operations performed for different purposes or by different controllers in a way that would exceed reasonable expectations of data subjects.
☐ Y / N / U

**Criterion 7 — Vulnerable data subjects**
Processing data of individuals who cannot easily consent or object, or whose interests may not coincide with those processing: children, employees (power imbalance), patients, elderly, people with mental illness, asylum seekers.
☐ Y / N / U

**Criterion 8 — Innovative use or applying new technological or organisational solutions**
Use of innovative technology or organisational solutions where state of the art has not been established and risks are not yet fully understood.
☐ Y / N / U

Examples: AI/ML systems, IoT, facial recognition, acoustic data channels (note: relevant to Kyma), blockchain-based processing, federated learning.

**Criterion 9 — Processing that prevents data subjects from exercising a right or using a service or contract**
Processing that aims at, or results in, individuals being excluded or denied access to a service, contract, or right.
☐ Y / N / U

**Criteria count:** [_] of 9 criteria met.
**Threshold:** 2 or more → DPIA mandatory.

### National DPA Mandatory DPIA Lists

Several national DPAs have published mandatory DPIA lists under GDPR Art. 35(4). Key examples:

**ICO (UK):** 11 mandatory categories including: processing biometric data for unique ID, processing genetic data, large-scale profiling, processing location data on a large scale, processing health data, processing data of children on large scale.

**CNIL (France):** 17 mandatory categories including: social network processing, AI-based processing of personal data, use of technologies that infer sensitive attributes, systematic processing of data to evaluate people.

**BfDI (Germany):** 16 categories including: employee monitoring systems, processing in smart homes, clinical trials, processing of telematics/tracking data.

**DPC (Ireland — home to many tech companies):** Follows EDPB nine criteria; no separate published list but issues case-specific guidance.

**Practical note:** If processing involves EU data subjects and no specific DPA list has been checked, run the EDPB nine criteria. If 2+ criteria are met, run a DPIA regardless of whether any national DPA has specifically listed the processing type.

---

## Quebec Law 25 Art. 63.5 — PIA Triggers

**Scope:** Any technology project (for Law 25 purposes: any project involving a technological system, application, or database) that involves personal information and "presents privacy risks."

CAI guidance identifies the following as presenting privacy risks requiring a PIA:

☐ Acquisition, development, or redesign of an information system involving PI
☐ New collection of PI not previously collected
☐ New use of existing PI (beyond original collection purpose)
☐ PI sharing arrangements with new third parties
☐ Cross-border PI transfers (outside Quebec)
☐ Implementation of new technologies — including AI/ML — involving PI
☐ Outsourcing of PI-related functions to a service provider
☐ New data retention or disposal processes
☐ Mergers, acquisitions, or restructuring affecting PI holdings
☐ Marketing or communications projects using PI

**Timing:** PIA must be completed BEFORE the project is implemented, not after. CAI has emphasised that a retroactive PIA is inadequate.

**Documentation:** The PIA must be kept on file and available to CAI on request. No mandatory disclosure to CAI unless the PIA identifies a high risk that cannot be mitigated — in which case CAI consultation is required before proceeding.

**Update obligation:** PIA must be updated when material changes are made to the project.

---

## HIPAA § 164.308(a)(1) — Risk Analysis Requirements

HIPAA does not use the term "PIA" but requires a mandatory "Risk Analysis" as an addressable implementation specification. HHS OCR treats risk analysis as effectively mandatory — failure is the most commonly cited HIPAA violation.

**§ 164.308(a)(1)(ii)(A) Risk Analysis must:**

☐ Identify the scope of ePHI: all ePHI that the covered entity creates, receives, maintains, or transmits
☐ Identify threats and vulnerabilities to the confidentiality, integrity, and availability of ePHI
☐ Assess current security measures
☐ Determine the likelihood of threat occurrence
☐ Determine the potential impact of threat occurrence
☐ Determine the level of risk
☐ Document the results in the risk analysis

**HHS OCR Guidance (2016):** Risk analysis must be "accurate and thorough," "ongoing," and "documented." A risk analysis conducted once and never updated is insufficient.

**Triggers for updated risk analysis:**
- New system implementation involving ePHI
- Change in environment (new cloud provider, new software)
- Security incident or breach
- Annual review of risk management program
- Workforce changes affecting ePHI access

---

## PIPL Art. 55 — Mandatory PIA Triggers (China)

Under Art. 55, personal information handlers must conduct a Personal Information Protection Impact Assessment (个人信息保护影响评估) BEFORE processing where:

☐ Processing sensitive personal information (biometric, health, financial, location, minors under 14)
☐ Using personal information for automated decision-making
☐ Entrusting personal information processing to a third party, or sharing/disclosing PI
☐ Providing personal information to overseas recipients
☐ Other personal information processing activities with major influence on individuals' rights and interests

**PIPL Art. 56 — PIA content requirements:**
- Whether the processing purpose and means are lawful, legitimate, and necessary
- Impact on individuals' rights and interests and the level of security risk
- Whether protection measures are lawful, effective, and appropriate to the level of risk

PIA records must be retained for at least 3 years.

---

## EU AI Act Art. 9 — Risk Management System (High-Risk AI)

For high-risk AI systems (Annex III), the Art. 9 risk management system is functionally equivalent to a rolling DPIA. Mandatory for:

☐ Biometric identification and categorisation of natural persons
☐ Management and operation of critical infrastructure
☐ Education and vocational training systems
☐ Employment, worker management, and access to self-employment
☐ Access to and enjoyment of essential private and public services/benefits
☐ Law enforcement systems
☐ Migration, asylum, and border control management
☐ Administration of justice and democratic processes

**Art. 9 risk management must:**
- Identify and analyse known and foreseeable risks associated with the AI system
- Estimate and evaluate risks that may emerge during intended use and reasonably foreseeable misuse
- Evaluate other risks based on analysis of data gathered from post-market monitoring
- Adopt suitable risk management measures in accordance with the state of the art

**Iterative requirement:** Risk management is not a one-time exercise — it must be applied throughout the entire lifecycle of the high-risk AI system.
