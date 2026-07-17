# Data Subject Rights Language

Complete language for each right, per jurisdiction, including exercise mechanisms, response timelines, and exemption language.

> **Source of truth:** the rights matrix and response timelines in this file derive from `taxonomy/regulatory-taxonomy.md` records (`ca-pipeda-law25`, `eu-gdpr-uk`, `us-ca-ccpa`, `br-lgpd`, `cn-pipl`) — axis A6 in each record. Reconciled 2026-07-04; log: `.fable/reconciliation-log.md`. On conflict, the record wins (see `SKILL.md` §Regulatory Source of Truth).

---

## Rights Matrix by Jurisdiction

| Right | GDPR | UK GDPR | PIPEDA | CCPA/CPRA | Quebec Law 25 | LGPD | PIPL |
|---|---|---|---|---|---|---|---|
| Access | Art. 15 | Art. 15 | Cl. 4.9 | § 1798.100 | Art. 27 PPIPS | Art. 18(II) | Art. 45 |
| Rectification | Art. 16 | Art. 16 | Cl. 4.9 | § 1798.106 | Art. 27 PPIPS | Art. 18(III) | Art. 46 |
| Erasure | Art. 17 | Art. 17 | Cl. 4.5.3 | § 1798.105 | Art. 28 PPIPS | Art. 18(VI) | Art. 47 |
| Restriction | Art. 18 | Art. 18 | — | — | — | — | — |
| Portability | Art. 20 | Art. 20 | — | § 1798.100 | Art. 27 PPIPS | Art. 18(V) | Art. 45 |
| Object | Art. 21 | Art. 21 | Cl. 4.3.8 | § 1798.120 | — | Art. 18 § 2† | Art. 44 |
| Automated decisions | Art. 22 | Art. 22 | — | — | — | Art. 20 | Art. 24 |
| De-indexing | — | — | — | — | Art. 28.1 PPIPS | — | — |
| Opt-out of sale | — | — | — | § 1798.120 | — | — | — |
| Limit sensitive PI | — | — | — | § 1798.121 | — | — | — |

† **Corrected 2026-07-05 (primary-source check):** LGPD objection is **Art. 18 § 2** (opposition to processing on non-consent bases in case of noncompliance). This matrix previously duplicated Art. 18(II) — the access anchor — for Object. Mirrored in the `br-lgpd` record; details in `.fable/reconciliation-log.md`.

---

## Right of Access

### Standard language (all jurisdictions)
```
You may request a copy of the personal data we hold about you, including:
- What data we hold
- Why we hold it
- Who we share it with
- How long we keep it
- Where it came from (if not directly from you)
- Any automated decision-making, including profiling, that significantly
  affects you and the logic involved

To make an access request: [email / form / postal address]
Response time: [30 days — GDPR / 45 days — CCPA / 30 days — PIPEDA]
Format: We will provide the information in a commonly used electronic format
unless you request otherwise.
```

### CCPA-specific addition
```
California residents may request:
(a) The categories of personal information we have collected about you
(b) The categories of sources from which we collect personal information
(c) The purposes for collecting personal information
(d) The categories of third parties with whom we share personal information
(e) The specific pieces of personal information we have collected
(f) [If selling/sharing:] Categories sold or shared and the categories of
    third parties to whom they were sold or shared, by category
```

### Exemptions to disclose proactively
```
We may decline to provide certain information where doing so would:
- Adversely affect the rights and freedoms of other individuals
- Reveal information subject to legal professional privilege
- Interfere with a law enforcement investigation
- Conflict with a legal obligation
We will tell you if we decline a request and explain why, unless the
reason itself is confidential.
```

---

## Right to Rectification / Correction

```
If personal data we hold about you is inaccurate or incomplete, you may
request that we correct it. We will update the data and, where appropriate,
notify third parties to whom we have disclosed it.

To request correction: [contact / form]
Response time: [30 / 45] days
```

### CCPA-specific (§ 1798.106)
```
California residents may request correction of inaccurate personal
information, taking into account the nature and purposes of the processing.
We will use commercially reasonable efforts to correct the information.
```

---

## Right to Erasure ("Right to Be Forgotten")

### Standard language
```
You may request deletion of your personal data in the following circumstances:
- The data is no longer necessary for the purposes for which it was collected
- You withdraw consent (where consent was the legal basis)
- You object to processing and there are no overriding legitimate grounds
- The data has been unlawfully processed
- Deletion is required by law

To request deletion: [contact / form]
Response time: [30 / 45] days
We will confirm deletion or explain why we are unable to comply.
```

### Retention exceptions — include when applicable
```
We may retain your data despite a deletion request where necessary for:
- Compliance with a legal obligation (e.g. financial record-keeping laws
  requiring [X]-year retention)
- Establishment, exercise, or defence of legal claims
- Public interest archiving, scientific or historical research
- [Other specific basis]
In these cases, we will restrict processing to only what the exception permits.
```

### Blockchain / immutability caveat — include when applicable
```
Note regarding blockchain data: Where we have recorded information on a
public blockchain, technical deletion is not possible. We have minimised
the personal data recorded on-chain. Where on-chain records reference
personal data, that data is held off-chain and will be deleted from our
systems. The on-chain commitment will remain but will be rendered
unintelligible without the deleted off-chain data.
```

---

## Right to Restriction (GDPR Art. 18 only)

```
You may request that we restrict the processing of your data while:
- You contest the accuracy of the data (restriction until we verify accuracy)
- The processing is unlawful and you prefer restriction to deletion
- We no longer need the data but you need it for legal claims
- You have objected to processing (restriction until we assess override)

During restriction, we will only store the data. We will tell you before
lifting a restriction.

To request restriction: [contact / form]
```

---

## Right to Data Portability

### Standard language
```
Where we process your data by automated means on the basis of consent or
contract performance, you may request a copy of the data you have provided
to us in a structured, commonly used, machine-readable format (JSON/CSV).

You may also request that we transmit this data directly to another
controller where technically feasible.

To request portability: [contact / form]
Response time: [30 / 45] days
Format: [JSON / CSV — specify]
```

### CCPA portability (§ 1798.100)
```
California residents may request disclosure of specific pieces of personal
information in a portable and, to the extent technically feasible, readily
usable format that allows transmission to another entity.
```

---

## Right to Object

### Legitimate interests (GDPR Art. 21(1))
```
Where we process your data based on legitimate interests (GDPR Art. 6(1)(f)),
you have the right to object at any time on grounds relating to your particular
situation. We will stop processing unless we can demonstrate compelling
legitimate grounds that override your interests, rights, and freedoms, or for
the establishment, exercise, or defence of legal claims.

To object: [contact / form]
```

### Direct marketing (GDPR Art. 21(2)) — absolute right, no override
```
You have an absolute right to object to processing of your personal data
for direct marketing purposes, including profiling for direct marketing.
If you object, we will immediately stop using your data for this purpose.

To opt out of marketing: [unsubscribe link] or [contact / form]
```

---

## Rights Regarding Automated Decisions (GDPR Art. 22)

*Include only if you use automated decision-making with significant effects.*

```
We use automated decision-making [describe: e.g. "to assess fraud risk for
transactions"]. This processing [does / does not] produce legal effects or
similarly significantly affect you.

You have the right to:
- Obtain human review of the automated decision
- Express your point of view
- Contest the decision

To request human review: [contact / form]
```

---

## California-Specific Rights

### Right to opt out of sale/sharing (§§ 1798.120, 1798.135)
```
[If selling/sharing:]
We sell or share personal information with [categories of third parties] for
[purposes]. You have the right to opt out.

[Do Not Sell or Share My Personal Information →]

To opt out: Click the link above, email [ccpa@company.com], or call
[toll-free number]. We will process your request within 15 business days.

Global Privacy Control: We honor the GPC browser signal as a valid opt-out
request. If your browser sends a GPC signal, we will treat this as an opt-out
of sale and sharing.
```

### Right to limit use of sensitive PI (§ 1798.121)
```
[If processing sensitive PI:]
We use sensitive personal information [categories] for [purposes]. You have
the right to direct us to limit our use to what is necessary to perform the
services you request.

[Limit Use of My Sensitive Personal Information →]
```

### Non-discrimination statement (§ 1798.125)
```
We will not discriminate against you for exercising your privacy rights.
We will not:
- Deny you goods or services
- Charge different prices or rates
- Provide a different level of quality of goods or services
- Suggest you will receive a different price or quality
```

---

## Quebec Law 25 Specific Rights

### Right to de-indexing (Art. 28.1 PPIPS)
```
Quebec residents may request that we cease publishing or disseminating
personal information when its dissemination causes them serious injury or
violates their privacy. We will consider requests and respond within
[30] days.

To request de-indexing: [contact / form]
```

---

## Rights Exercise Mechanism

### Identity verification
```
To protect your privacy, we may need to verify your identity before
processing your request. We will ask for [describe — e.g. "the email
address associated with your account" or "two pieces of identifying
information"]. We will not ask for more information than reasonably
necessary to verify identity. We will not use information provided for
verification for any other purpose.
```

### Response timelines
| Jurisdiction | Initial response | Maximum extension | Extension notice |
|---|---|---|---|
| GDPR | 1 month | 2 additional months (3 total) | Must notify within 1 month with reason |
| UK GDPR | 1 month | 2 additional months | Must notify within 1 month |
| CCPA | 45 days | 45 additional days (90 total) | Must notify within 45 days |
| PIPEDA | 30 days | Reasonable extension (notify) | Must notify before expiry |
| Quebec Law 25 | 30 days | 10 additional days | Must notify within 30 days |
| LGPD | 15 days | — | — |

### Complaints
```
If you are unsatisfied with how we have handled your request or concern,
you have the right to complain to your relevant data protection authority:

EU/EEA: [Relevant national DPA — link to edpb.europa.eu/about-edpb/board/members_en]
UK: Information Commissioner's Office — ico.org.uk/make-a-complaint
Canada: Office of the Privacy Commissioner — priv.gc.ca/en/report-a-concern
Quebec: Commission d'accès à l'information — cai.gouv.qc.ca
California: California Privacy Protection Agency — cppa.ca.gov
Brazil: Autoridade Nacional de Proteção de Dados — gov.br/anpd
```
