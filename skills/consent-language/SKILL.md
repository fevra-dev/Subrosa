---
name: consent-language
description: Generates legally compliant privacy notices, consent flows, cookie banners, and data subject rights disclosures for products and services. Use when user says "write a privacy policy", "privacy notice", "cookie consent", "GDPR consent flow", "data subject rights page", "at collection notice", "CCPA disclosure", "PIPEDA privacy statement", "opt-in consent copy", "cookie banner text", "legitimate interests notice", "generate consent UI copy", or when launching a product or feature that collects personal data and needs compliant disclosure language. Produces layered notices (short/full), jurisdiction-specific variations, UI copy for consent flows, cookie categorization text, and rights exercise mechanisms. Grounded in GDPR Arts. 13/14, PIPEDA Clause 4.8, CCPA § 1798.100, Quebec Law 25, COPPA, ePrivacy Directive, and PIPL Art. 17.
---

# Consent Language

Generates privacy notices, consent flows, cookie banners, and rights disclosures that satisfy legal requirements across GDPR, PIPEDA, CCPA/CPRA, Quebec Law 25, COPPA, ePrivacy Directive, and PIPL.

**Composable with:**
- `data-minimization` — run first; the field inventory defines what must be disclosed
- `privacy-impact-assessment` — PIA determines legal basis; consent language implements it
- `privacy-architecture` — if ZK or anonymous credentials are used, consent language should reflect the reduced data collection

---

## Regulatory Source of Truth

Statutory citations and jurisdiction facts (deadlines, thresholds, ages, category lists) in this skill and its reference files derive from the normalized taxonomy: `taxonomy/regulatory-taxonomy.md` + the per-jurisdiction records (`taxonomy/regulatory-taxonomy--*.md`, axes A0–A12). Records consumed here: `ca-pipeda-law25`, `eu-gdpr-uk`, `us-ca-ccpa`, `br-lgpd`, `cn-pipl`, `sg-pdpa`, `th-pdpa` (+ COPPA and ePrivacy as sectoral overlays pending their variant profile).

On any discrepancy between this skill's files and a record: **the record wins** — unless this file is more specific or more correct, in which case fix the record and log the reconciliation in `.fable/reconciliation-log.md`. Never resolve a conflict by inventing a citation; unresolved conflicts carry `[UNVERIFIED — confirm against primary source]`.

For "design-to-strictest" defaults use `taxonomy/regulatory-taxonomy--floor.md`. For known cross-regime incompatibilities (erasure vs immutability, etc.) use `taxonomy/regulatory-taxonomy--conflicts.md`.

---

## Output Types

| Output | When needed | Primary law |
|---|---|---|
| **Full privacy notice / policy** | At product launch; any significant change | GDPR Arts. 13/14; PIPEDA Cl. 4.8 |
| **Short / layered notice** | At point of collection (inline) | GDPR Art. 13; PIPEDA Cl. 4.2 |
| **Cookie consent banner** | Any website with non-essential cookies | ePrivacy Dir. Art. 5(3); GDPR |
| **Legitimate interests notice** | When using Art. 6(1)(f) legal basis | GDPR Art. 13(1)(d), Art. 21 |
| **At-collection notice (CCPA)** | California-facing products | CCPA § 1798.100(b); CPRA |
| **Children's / parental consent** | Any product with users under 13 (COPPA) or under 16 (GDPR) | COPPA 16 CFR § 312; GDPR Art. 8 |
| **Data subject rights page** | All EU/UK/CA-facing products | GDPR Arts. 15-22; CCPA §§ 1798.100-1798.125 |
| **Consent withdrawal mechanism** | Any consent-based processing | GDPR Art. 7(3); PIPEDA Cl. 4.3 |
| **Data breach notification** | On occurrence of notifiable breach | GDPR Art. 34; PIPEDA ss. 10.1-10.3; CCPA § 1798.150 |
| **Cross-border transfer notice** | Any transfer outside EEA, Canada, or applicable jurisdiction | GDPR Art. 13(1)(f); PIPL Art. 17(4) |

---

## Workflow

### Step 1 — Intake

Establish before generating any language:

1. **Jurisdiction(s):** Where are data subjects located? (EU/EEA, UK, Canada, California, China, Brazil, multiple?)
2. **Legal basis:** What lawful basis applies? (Consent, contract, legitimate interests, legal obligation — per jurisdiction)
3. **Data types:** What personal data is collected? (Import from `data-minimization` field inventory if available)
4. **Output type:** What document or UI element is needed?
5. **Tone:** Formal (legal/enterprise) / Plain (consumer app) / Minimal (developer API)?
6. **Children:** Does the product have users under 13 (COPPA) or under 16 (GDPR Art. 8)?
7. **Cookies:** Does the product use non-essential cookies or tracking technologies?

If a field inventory is not available, ask for the data types before proceeding. Generating a privacy notice without knowing what data is collected produces non-compliant output.

### Step 2 — Select template and jurisdiction stack

Load the appropriate reference file for the output type. Apply jurisdiction-specific requirements as overlays.

| Output type | Reference |
|---|---|
| Privacy notices (all types) | `references/notice-templates.md` |
| Cookie consent | `references/cookie-consent.md` |
| Rights disclosures | `references/rights-language.md` |
| Children's consent | `references/childrens-consent.md` |
| Breach notifications | `references/breach-notification.md` |

### Step 3 — Generate output

Produce the requested document with:
- All legally required disclosures populated
- Jurisdiction-specific variations clearly marked
- Placeholder markers `[COMPANY NAME]`, `[DPO EMAIL]`, `[EFFECTIVE DATE]` for fields to be completed by the user
- Plain language — aim for Flesch-Kincaid Grade 8 or below for consumer-facing notices
- No legal jargon where plain language serves

### Step 4 — Completeness check

After generating, run this checklist against the output:

**GDPR Arts. 13/14 checklist (if EU/UK):**
- ☐ Controller identity and contact details
- ☐ DPO contact (if applicable)
- ☐ Purposes of processing
- ☐ Legal basis for each purpose
- ☐ Legitimate interests (if Art. 6(1)(f)) — specific interests stated
- ☐ Recipients or categories of recipients
- ☐ Third country transfers and safeguards (if applicable)
- ☐ Retention periods (or criteria for determining them)
- ☐ All Art. 15-22 rights listed
- ☐ Right to withdraw consent (if consent-based)
- ☐ Right to lodge complaint with supervisory authority
- ☐ Whether provision is statutory/contractual/voluntary and consequences of not providing
- ☐ Any automated decision-making including profiling (Art. 22)

**PIPEDA checklist (if Canada):**
- ☐ Identity and contact of organisation
- ☐ Purposes identified before or at collection
- ☐ Meaningful consent (explicit or implicit as appropriate)
- ☐ How to access and correct personal information
- ☐ How to file a complaint

**CCPA/CPRA checklist (if California):**
- ☐ Categories of PI collected
- ☐ Purposes for collection
- ☐ Categories of sources
- ☐ Categories of third parties PI shared with
- ☐ Right to know, delete, correct, opt-out, non-discrimination
- ☐ "Do Not Sell or Share My Personal Information" link (if applicable)
- ☐ How to submit requests (at least two methods)
- ☐ Sensitive PI — right to limit use

### Step 5 — Flag gaps

If required information was not provided (e.g., retention period is unknown, DPO is not appointed), flag each gap explicitly rather than generating placeholder text that might be submitted as-is:

```
GAP — Retention period not specified
Required by: GDPR Art. 13(2)(a), PIPEDA Cl. 4.5
Action: Determine retention period per data category before finalising this notice.
Default: Cannot generate compliant notice without this information.
```

---

## Legal Basis Language

### Consent (GDPR Art. 6(1)(a))
```
We process your [data type] with your consent. You may withdraw consent at any time
by [withdrawal mechanism]. Withdrawal does not affect the lawfulness of processing
before withdrawal.
```

**GDPR consent requirements:**
- Freely given (no bundling, no conditional access for non-essential processing)
- Specific (separate consent per purpose)
- Informed (notice given before consent)
- Unambiguous indication (affirmative action — no pre-ticked boxes)
- As easy to withdraw as to give

### Legitimate Interests (GDPR Art. 6(1)(f))
```
We process your [data type] on the basis of our legitimate interests in [specific
interest — e.g. "preventing fraud and ensuring the security of our platform"]. We
have assessed that this processing is necessary for those interests and does not
unduly override your privacy rights. You have the right to object to this processing
at any time (see Your Rights below).
```

**LIA documentation note:** Generating legitimate interests language requires a completed Legitimate Interests Assessment on file. If one has not been conducted, flag this as a gap.

### Contract (GDPR Art. 6(1)(b))
```
We process your [data type] because it is necessary to perform the contract we have
with you, or to take steps at your request before entering into a contract.
```

### Legal Obligation (GDPR Art. 6(1)(c))
```
We process your [data type] to comply with [specific legal obligation — e.g.
"anti-money laundering regulations under [Act name]"].
```

---

## Cookie Consent Hierarchy

Generate cookie categories and consent UI copy:

**Category 1 — Strictly Necessary (no consent required):**
```
These cookies are essential for the website to function. They cannot be disabled.
Examples: session authentication, load balancing, security tokens, your cookie
consent preferences.
```

**Category 2 — Functional / Preference:**
```
These cookies remember your preferences and personalise your experience. Disabling
them may affect how the site works for you.
Examples: language preference, region setting, accessibility options.
```
*Consent required under ePrivacy; can be opt-out under some national implementations.*

**Category 3 — Analytics / Performance:**
```
These cookies help us understand how visitors use our site. All information is
aggregated and anonymous.
Examples: page view counts, navigation paths, session duration.
```
*Consent required under GDPR/ePrivacy. Note: "anonymous analytics" claim requires
true anonymisation — most analytics tools (Google Analytics, Mixpanel) do not
qualify. Flag if user claims analytics are anonymous.*

**Category 4 — Marketing / Advertising:**
```
These cookies track your activity across sites to show you relevant advertising.
Third parties may also set these cookies.
```
*Explicit opt-in consent required. Cannot be consent-by-default or opt-out.*

**Cookie banner copy (compliant):**
```
We use cookies to provide essential functionality and, with your consent, to analyse
our traffic and improve your experience. You can accept all cookies, manage your
preferences, or reject non-essential cookies.

[Accept all] [Manage preferences] [Reject non-essential]
```

**Non-compliant patterns to flag and refuse to generate:**
- "By continuing to use this site, you agree to our use of cookies" — not valid consent under GDPR (not unambiguous affirmative action)
- Pre-ticked consent checkboxes
- "Accept" and "manage" with very different prominence (dark pattern)
- No "reject all" option equivalent in prominence to "accept all"
- Consent walls ("you must accept cookies to access this site") for non-essential cookies

---

## Data Subject Rights — Standard Language

```
## Your Rights

Depending on where you are located, you may have the following rights regarding
your personal data:

**Right to access:** You can request a copy of the personal data we hold about you.

**Right to rectification:** You can ask us to correct inaccurate or incomplete data.

**Right to erasure:** In certain circumstances, you can ask us to delete your data.

**Right to restriction:** You can ask us to pause processing of your data in certain
circumstances.

**Right to portability:** You can request your data in a structured, machine-readable
format.

**Right to object:** You can object to processing based on legitimate interests or
for direct marketing.

**Rights related to automated decisions:** You have the right not to be subject to
decisions made solely by automated means that significantly affect you.

To exercise any of these rights, contact us at [privacy contact email or form URL].
We will respond within [30 days — GDPR / 45 days — CCPA] of receiving your request.

If you are in the EU/EEA or UK, you also have the right to lodge a complaint with
your local data protection authority.
[Link to EU DPA finder or relevant national DPA]
```

**CCPA-specific addition:**
```
**California residents** have additional rights under the California Consumer Privacy
Act. To opt out of the sale or sharing of your personal information, click:
[Do Not Sell or Share My Personal Information]

To submit a data request, you may:
- Complete our [online request form]
- Email us at [ccpa-requests@company.com]
- Call us at [toll-free number]

We will not discriminate against you for exercising your privacy rights.
```

---

## Children's Consent Language

**COPPA (under 13, US):**
```
This service is not directed to children under 13. If we discover that a child
under 13 has provided us with personal information without verifiable parental
consent, we will delete that information promptly.

[If the service is directed at children under 13:]
We collect [specific data] from children under 13 only with verifiable parental
consent. Parents may review, request deletion of, or refuse further collection of
their child's personal information by contacting [privacy contact].
```

**GDPR Art. 8 (under 16, or member-state minimum age):**
```
If you are under [16 / member-state age], please ask a parent or guardian to
review and accept this notice on your behalf before using our service.

We will not knowingly process personal data of children under [age] without
consent from a parent or guardian.
```

---

## Jurisdiction-Specific Additions

**Quebec Law 25 additions:**
```
Privacy Impact Assessment: We have conducted a Privacy Impact Assessment for this
system as required by Quebec's Act respecting the protection of personal information
in the private sector (PPIPS).

Right to de-indexing: Quebec residents have the right to request that we cease
publishing or disseminating information that may injure their reputation or privacy.

Confidentiality officer: Our confidentiality officer can be reached at [contact].
```

**PIPL additions (China):**
```
[Chinese language version required for China-facing products — generate separately]

Personal information handler: [Chinese entity name and contact]
Purposes: [specific purposes per PIPL Art. 17(1)]
Processing methods: [per PIPL Art. 17(2)]
Categories of PI and sensitivity: [per PIPL Art. 17(3)]
Retention period: [per PIPL Art. 17(4)]
Your rights: [inquiry, correction, deletion, transfer, withdrawal — per PIPL Arts. 44-47]
Cross-border transfer safeguards: [per PIPL Art. 38]
```

**LGPD additions (Brazil):**
```
Data Protection Officer: [name and contact — required for large-scale processors]
Legal basis: [from LGPD Art. 7 or Art. 11 for sensitive data]
Your rights: [access, rectification, deletion, portability, opposition — per LGPD Art. 18]
How to contact the ANPD: [anpd.gov.br]
```

---

## Anti-Patterns — Refuse to Generate

These constructs are non-compliant and should not be generated:

| Pattern | Why non-compliant |
|---|---|
| "By using this service you consent to..." | Not valid GDPR consent — not a clear affirmative act |
| Consent bundled with terms of service | Not freely given or specific |
| Pre-ticked opt-in boxes | Not unambiguous indication under GDPR |
| "We may share your data with our partners" | Insufficient specificity — names or categories required |
| Vague retention: "as long as necessary" | Must specify criteria or period — GDPR Art. 13(2)(a) |
| Cookie wall (consent required to access) | Undermines freely given consent for non-essential cookies |
| "We take your privacy seriously" as substantive disclosure | No legal information value |
| Dark pattern: "Accept" prominently, "Manage" tiny | Violates freely given consent requirement |
| "Anonymous analytics" when using Google Analytics | Google Analytics is not anonymous — IP addresses are processed |

---

## Reference Files

- `references/notice-templates.md` — Full privacy notice and short/layered notice templates per jurisdiction
- `references/cookie-consent.md` — Cookie category definitions, banner templates, GPC signal requirements
- `references/rights-language.md` — Data subject rights language per right per jurisdiction
- `references/childrens-consent.md` — COPPA verifiable parental consent mechanisms, GDPR Art. 8 age verification patterns
- `references/breach-notification.md` — Data breach notification templates for individuals and regulators (GDPR Art. 33/34, PIPEDA s. 10.1, CCPA § 1798.150, LGPD Art. 48)
