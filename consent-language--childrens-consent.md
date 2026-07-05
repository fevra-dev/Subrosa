# Children's Consent & Privacy

COPPA (US under-13), GDPR Art. 8 (EU under-16), and analogous requirements across PIPEDA, LGPD, PIPL, and POPIA.

> **Source of truth:** the age-threshold table derives from `regulatory-taxonomy.md` records — axis A9 in each record (COPPA is a sectoral overlay pending its variant profile). Reconciled 2026-07-04; log: `.fable/reconciliation-log.md`. On conflict, the record wins (see `consent-language.md` §Regulatory Source of Truth).

---

## Age Thresholds by Jurisdiction

| Jurisdiction | Age threshold | Law | Consent mechanism |
|---|---|---|---|
| United States | Under 13 | COPPA (15 U.S.C. §§ 6501-6506) | Verifiable parental consent |
| EU/EEA | Under 16 (default); member states may lower to 13 | GDPR Art. 8 | Parental/guardian consent |
| UK | Under 13 | UK GDPR + Age Appropriate Design Code (AADC) | Parental consent for under 13; AADC applies to all under 18 |
| Canada | Under 13 (guidance); no statutory threshold | OPC guidance | Meaningful parental consent |
| Brazil | Under 18 | LGPD Art. 14 | Specific consent from parent/guardian |
| China | Under 14 | PIPL Art. 31 | Consent from parent/guardian |
| South Africa | Under 18 | POPIA § 35 | Parental/guardian consent |
| Australia | Under 15 (guidance) | Privacy Act + OAIC guidance | Parental consent |

**EU member state age thresholds (GDPR Art. 8(1) allows 13-16):**
- Age 13: Bulgaria, Czech Republic, Denmark, Estonia, Finland, Latvia, Lithuania, Malta, Romania, Slovenia, Sweden, UK (post-Brexit)
- Age 14: Austria, Hungary, Italy, Spain
- Age 15: France (but CNIL enforces 15)
- Age 16: Croatia, Cyprus, Germany, Greece, Ireland, Luxembourg, Netherlands, Poland, Portugal, Slovakia

---

## COPPA (United States — Under 13)

**Statute:** 15 U.S.C. §§ 6501-6506. **Rule:** 16 CFR Part 312. **Enforcement:** FTC. **Penalties:** Up to $51,744 per violation per day (2023 inflation-adjusted).

### Key Obligations

**When COPPA applies:**
- Operator of a website/online service directed to children under 13
- Operator with **actual knowledge** they are collecting PI from children under 13

"Directed to children" factors (16 CFR § 312.2): subject matter, visual content, music, animated characters, celebrities appealing to children, advertising, age of models, presence of child celebrities.

**Mixed audience sites:** If site is directed to general audiences but has actual knowledge a particular user is under 13 → COPPA applies to that user.

### Verifiable Parental Consent (VPC) Methods (16 CFR § 312.5(b))

| Method | Description | Approved? |
|---|---|---|
| Email plus | Email to parent + additional step (toll-free call, credit card, digital cert) | Yes |
| Print and send | Parent prints, signs, returns consent form via mail/fax | Yes |
| Video conference | Real-time video conference with operator | Yes |
| Government ID check | Check photo ID + delete afterward | Yes |
| Credit/debit card | Use in transaction + notice to cardholder | Yes |
| Knowledge-based auth | Dynamic knowledge questions sufficient to be commercially reasonable | Yes (2013 amendment) |
| Face match with ID | Facial recognition match to photo ID | Yes (proposed 2023 amendment) |
| Email only | Send consent form, await reply email | No — not verifiable |

**"Email plus" template:**
```
Dear Parent/Guardian,

[CHILD'S ACCOUNT NAME OR EMAIL] has created an account on [PRODUCT NAME].
Before we can allow [them] to use our service, we need your permission to
collect the following information: [list data types].

This information will be used to [purpose].

To give your consent, please [complete one of: call our toll-free number at
[number] / reply to this email with the completed consent form attached /
complete the form at [URL]].

If you did not create this account or do not wish to give consent, please
do nothing. The account will not be activated, and we will delete any
information collected within [14] days.

For more information about our privacy practices for children, see our
[Children's Privacy Notice].

[COMPANY NAME]
[privacy@company.com]
[Address]
```

### COPPA Notice Templates

**Children's privacy notice (required):**
```
CHILDREN'S PRIVACY NOTICE

[COMPANY NAME] ("we," "us") operates [PRODUCT NAME]. This notice
explains how we handle information from children under 13.

WHAT WE COLLECT
We collect [list: e.g. "first name and email address"] from children
under 13 only after receiving verifiable parental consent.

We do NOT collect: [list things you specifically don't collect — e.g.
"last name, precise location, phone number, photo or video of the child"]

WHY WE COLLECT IT
[Specific purpose — e.g. "to allow the child to save their progress in
the game"]

HOW LONG WE KEEP IT
[Period — e.g. "as long as the account is active. We delete all
information within [14] days of account deletion."]

WHO SEES IT
[Staff who need it for the purpose / no third-party sharing /
service providers under COPPA-compliant contracts]

PARENTAL RIGHTS
Parents/guardians may:
- Review the personal information collected from their child
- Request deletion of their child's personal information
- Refuse further collection or use
- Revoke consent

To exercise these rights: [privacy@company.com] or [toll-free number]
We will respond within [10] business days.

CONTACT
[privacy@company.com]
[Address]
[Toll-free number if under 13 service]
```

**Neutral age screening (required practice):**
```
When a user provides a date of birth indicating they are under 13:
1. Do NOT collect any additional PI at that point
2. Do NOT ask them to provide a different birth date
3. EITHER: gate them out (explain parental consent required; provide
   notice to parent; do not activate account)
4. OR: collect parental email only → send VPC request → do not process
   child's data until consent received
5. Delete any data collected before the age identification within [x] days

Never: "Ask again" or provide a way to bypass the age gate.
The FTC has enforced against "neutral" age screens that were easily circumvented.
```

---

## GDPR Art. 8 (EU — Information Society Services)

**Applies to:** Online services directed at children where consent is the legal basis under Art. 6(1)(a).

**Art. 8(1):** Where consent is relied upon, processing of a child's personal data is lawful only if the child is at least 16 (or lower member-state threshold) OR where parental/guardian consent is obtained.

**Art. 8(2):** Controllers must make reasonable efforts to verify parental consent, taking into account available technology.

**Art. 8(3):** Art. 8 does not affect general contract law of member states (e.g. contractual capacity).

### Age Verification Language
```
To use [PRODUCT], you must be at least [13/16] years old.

Date of birth: [DD/MM/YYYY] [field]

[If under threshold:]
Thank you for your interest in [PRODUCT]. To use our service, someone
under [age] needs a parent or guardian's permission.

Please ask a parent or guardian to:
[Option A: Complete the form at [URL]]
[Option B: Email us at [parental-consent@company.com]]

We will not use any information you have provided until we receive
parental consent. If we do not hear from a parent or guardian within
[14] days, we will delete the information you provided.
```

### UK Age Appropriate Design Code (Children's Code)

The UK's ICO Children's Code (effective Sept 2021) applies to online products "likely to be accessed by children" (defined as under 18). 15 standards including:

- **Best interests:** Prioritise children's best interests
- **Data minimisation:** Only collect what is strictly necessary
- **Default settings:** Privacy settings should be high privacy by default
- **Geolocation off by default**
- **Profiling off by default** — no profiling of children unless demonstrably in their best interests
- **No nudge techniques** — no design choices that encourage children to provide more PI
- **No detriment** for exercising privacy rights
- **Parental controls** — offer tools but do not undermine children's privacy

**If product is "likely to be accessed" by UK children (broad — any general consumer product):** Must complete a Data Protection Impact Assessment addressing the 15 standards.

---

## LGPD Art. 14 (Brazil — Under 18)

```
We do not process personal data of children and adolescents (under 18)
without specific consent from at least one parent or legal guardian.

Processing of children's data must be in the best interests of the child.
Collection of data unnecessary for the provision of the service is prohibited.
Parents and guardians may request, at any time, deletion of their child's data
to the extent that processing was based on consent.
```

**ANPD Regulation (Resolution CD/ANPD No. 4, 2023):** Operational requirements for children's data processing — detailed assessment required for any product processing children's data.

---

## PIPL Art. 31 (China — Under 14)

```
We process personal information of minors under 14 (minor personal
information subject to special protection under PIPL) only with consent
from their parents or guardians.

We have formulated specific personal information processing rules for
minors, available at [link].

Parents and guardians may exercise rights on behalf of minors under 14,
including access, correction, deletion, and transfer requests.
```

**PIPL requirement:** Operators must formulate separate PI processing rules for minors. Disclosure must be given directly to parents/guardians. Verification of parental identity required.

---

## General Principles for All Jurisdictions

**Data minimization for children:** Collect less from children than you collect from adults. If you collect name and email from adults, collect only a username from children. The regulator asks: "Was every field necessary for the child-directed service?"

**No behavioral advertising targeting children:** No jurisdiction permits behavioral advertising targeting children. Many prohibit even contextual advertising on children-directed services.

**No dark patterns for children:** Design for children's wellbeing, not engagement metrics. Avoiding notifications, streaks, and features that exploit developmental vulnerabilities is increasingly an enforcement expectation (UK Children's Code, COPPA proposed 2023 amendments).

**Easy parental access:** Parents must be able to review, correct, and delete their child's data without requiring the child's password or cooperation.
