# Privacy Notice Templates

Complete templates for full privacy policies, short notices, and layered notices across jurisdictions. Populate placeholders marked `[LIKE THIS]` before use. Remove instructional italics before publishing.

> **Source of truth:** statutory anchors in this file derive from `taxonomy/regulatory-taxonomy.md` records (`ca-pipeda-law25`, `eu-gdpr-uk`, `us-ca-ccpa`). Reconciled 2026-07-04; log: `.fable/reconciliation-log.md`. On conflict, the record wins (see `SKILL.md` §Regulatory Source of Truth). Template response-time phrasing ("30 days — GDPR") is a deliberate plain-language rendering of the record's 1-month clock.

---

## Template 1: Full Privacy Notice (GDPR Art. 13/14 + PIPEDA + CCPA)

*Use for: consumer-facing products with EU, Canadian, and California users. Most comprehensive — covers all three regimes simultaneously.*

---

### PRIVACY NOTICE

**[COMPANY NAME]**  
Effective date: [DATE]  
Last updated: [DATE]

---

#### 1. Who We Are

[COMPANY NAME] ("[COMPANY]", "we", "us", "our") is a [description of business] incorporated in [jurisdiction]. We are the data controller for personal information collected through [PRODUCT/SERVICE NAME].

**Contact:** [privacy@company.com]  
**Data Protection Officer:** [Name, dpo@company.com — or "We have not appointed a DPO. Privacy queries should be directed to [contact]."]  
**Postal address:** [Address]

---

#### 2. What Personal Data We Collect and Why

*For each processing activity, state: what data, why (purpose), legal basis, retention period.*

**Account creation and authentication**  
Data: email address, username, password hash  
Purpose: create and maintain your account; authenticate your identity  
Legal basis: GDPR Art. 6(1)(b) — contract performance; PIPEDA Clause 4.3 — consent  
Retention: duration of account + [30 days] after deletion  

**[SERVICE DELIVERY — e.g. payment processing]**  
Data: [list fields]  
Purpose: [purpose]  
Legal basis: [basis]  
Retention: [period]  

**Security and fraud prevention**  
Data: IP address (truncated to /24 subnet), login timestamps, failed login counts  
Purpose: detect and prevent unauthorized access; maintain service integrity  
Legal basis: GDPR Art. 6(1)(f) — legitimate interests (preventing fraud); PIPEDA Clause 4.4  
Retention: 90 days  

**Service improvement and analytics**  
Data: [if collecting — describe minimized form, e.g. "page view counts, aggregated navigation paths — no individual-level behavioral tracking"]  
Purpose: understand how users interact with our service to improve it  
Legal basis: GDPR Art. 6(1)(f) — legitimate interests; consent where required by ePrivacy Directive  
Retention: [period]  

*[Add/remove rows as needed. Every processing activity must be disclosed.]*

---

#### 3. Special Categories of Personal Data

*Complete only if you process GDPR Art. 9 / sensitive data.*

We [do / do not] process special categories of personal data. [If yes:] We process [health / biometric / other] data for [purpose] on the basis of [GDPR Art. 9(2)(x) — specific ground].

---

#### 4. How We Share Your Data

We do not sell your personal data.

**Service providers (processors):** We share data with companies that help us deliver our service, under contracts that require them to protect your data:
- [Provider name]: [what data, what purpose] — located in [country/region]
- [Provider name]: [what data, what purpose] — located in [country/region]

**Legal obligations:** We may disclose data where required by law, court order, or to protect the rights and safety of [COMPANY] and others.

**Business transfers:** If [COMPANY] is acquired or merges, your data may be transferred to the acquiring entity. We will notify you before your data becomes subject to a different privacy notice.

**With your consent:** We will share your data for other purposes only with your explicit consent, which you may withdraw at any time.

---

#### 5. International Transfers

*Complete if transferring data outside EEA/UK, Canada, or applicable jurisdiction.*

We transfer personal data to [countries]. These transfers are protected by:
- ☐ European Commission adequacy decision
- ☐ Standard Contractual Clauses (SCCs) — available on request
- ☐ UK International Data Transfer Agreement (IDTA)
- ☐ Binding Corporate Rules
- ☐ Other: [specify]

---

#### 6. How Long We Keep Your Data

| Data type | Retention period | Basis for period |
|---|---|---|
| Account data | Duration of account + [30] days post-deletion | Contract; then legal obligation |
| Security logs | 90 days | Legitimate interests in fraud prevention |
| [Other] | [Period] | [Basis] |

When retention periods expire, data is [deleted / anonymized] using [describe method].

---

#### 7. Your Rights

Depending on your location, you have the following rights:

**All users:**
- Access the personal data we hold about you
- Correct inaccurate or incomplete data
- Request deletion of your data (subject to legal retention obligations)
- Object to processing based on legitimate interests

**EU/EEA/UK users (GDPR):**
- Restrict processing in certain circumstances
- Receive your data in a portable format
- Rights regarding automated decision-making and profiling
- Lodge a complaint with your national data protection authority ([link to EU DPA finder / ICO for UK])

**California users (CCPA/CPRA):**
- Know what personal information we collect, use, disclose, and sell
- Delete your personal information
- Correct inaccurate personal information
- Opt out of the sale or sharing of personal information
- Limit the use of sensitive personal information
- Non-discrimination for exercising your rights

**Canadian users (PIPEDA / Quebec Law 25):**
- Access and correct your personal information
- Withdraw consent (subject to legal and contractual restrictions)
- Lodge a complaint with the [Office of the Privacy Commissioner (OPC) / Commission d'accès à l'information (CAI) for Quebec]

**To exercise your rights:** Contact us at [privacy@company.com] or [link to rights request form]. We will respond within [30 days — GDPR / 45 days — CCPA]. We may need to verify your identity before fulfilling your request.

---

#### 8. Cookies and Tracking

*If using cookies/tracking — link to separate cookie notice or include here.*

We use cookies and similar technologies. See our [Cookie Notice] for details, including how to manage your preferences.

[If no non-essential cookies: "We use only strictly necessary cookies required for the service to function. We do not use tracking, analytics, or advertising cookies."]

---

#### 9. Children's Privacy

*Select applicable version:*

**Version A — Service not directed at children:**  
Our service is not directed to children under [13 / 16]. We do not knowingly collect personal data from children under this age. If you believe we have inadvertently collected such data, contact us at [privacy@company.com] and we will delete it promptly.

**Version B — Service with children's features (COPPA applies):**  
See our [Children's Privacy Notice / Parental Consent Section] for information about how we handle data from users under 13.

---

#### 10. Security

We implement [describe measures — e.g. "encryption at rest and in transit, access controls, regular security assessments"] to protect your personal data. No method of transmission or storage is 100% secure; we cannot guarantee absolute security.

---

#### 11. Changes to This Notice

We will notify you of material changes by [email / in-app notification / posting notice prominently on our website] at least [30] days before changes take effect. Continued use after the effective date constitutes acceptance.

---

#### 12. Contact Us

**Privacy queries:** [privacy@company.com]  
**Data subject rights requests:** [rights@company.com / link to form]  
**DPO:** [dpo@company.com — if appointed]  
**Postal:** [Address]

---

## Template 2: Short / Layered Notice (Point of Collection)

*Use at the moment of data collection — form header, sign-up screen, checkout page. Links to full notice. Required under GDPR Art. 13.*

```
We collect your [email address / name / other] to [specific purpose].
[COMPANY NAME] is the data controller. Legal basis: [contract / consent / legitimate interests].
We retain this data for [period].
[Full privacy notice] | [Manage preferences] | [Contact DPO]
```

**Mobile/space-constrained version:**
```
Your data is used for [purpose]. [Privacy Notice →]
```

---

## Template 3: At-Collection Notice (CCPA § 1798.100(b))

*Required for California users at or before the point of collection.*

```
NOTICE AT COLLECTION

[COMPANY NAME] collects the following categories of personal information:
• [Category 1 — e.g. Identifiers (name, email, IP address)]
• [Category 2 — e.g. Commercial information (purchase history)]
• [Category 3 — e.g. Internet activity (pages visited)]

We collect this information for the following purposes:
• [Purpose 1]
• [Purpose 2]

[If selling/sharing:] We sell or share personal information with [categories of third parties] for [purposes]. You may opt out: [link]

[If sensitive PI:] We collect sensitive personal information [categories]. You may limit our use: [link]

Retention: We retain personal information for [period / the period necessary to fulfill the purposes described].

For more information, see our [Privacy Policy →]
```

---

## Template 4: Legitimate Interests Notice (GDPR Art. 13(1)(d) + Art. 21)

*Required when processing on Art. 6(1)(f) basis.*

```
We process your [data type] on the basis of our legitimate interests in [specific
interest]. We have assessed that:
1. We have a genuine legitimate interest: [state it specifically]
2. The processing is necessary to achieve that interest
3. Our interest is not overridden by your privacy rights because [reasoning]

You have the right to object to this processing at any time. To object, contact:
[privacy@company.com]

If you object, we will stop processing unless we can demonstrate compelling
legitimate grounds that override your interests, rights, and freedoms, or for
the establishment, exercise, or defence of legal claims.
```
