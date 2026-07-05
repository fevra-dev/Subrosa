# Data Breach Notification Templates

Templates for notifying regulators and affected individuals following a personal data breach. Jurisdiction-specific timelines and required content.

> **Source of truth:** the timeline table and thresholds in this file derive from `regulatory-taxonomy.md` records — axis A8 in each record. Reconciled 2026-07-04; log: `.fable/reconciliation-log.md`. On conflict, the record wins (see `consent-language.md` §Regulatory Source of Truth).

---

## Breach Notification Timeline Reference

| Jurisdiction | Regulator deadline | Individual deadline | Threshold |
|---|---|---|---|
| GDPR (EU/EEA) | 72 hours of becoming aware | Without undue delay (if high risk to individuals) | All breaches to regulator; high-risk to individuals |
| UK GDPR | 72 hours | Without undue delay (if high risk) | Same as GDPR |
| PIPEDA (Canada) | "As soon as feasible" | "As soon as feasible" after regulator notice | Real risk of significant harm (RROSH) |
| Quebec Law 25 | 72 hours to CAI† | 72 hours (same as CAI)† | Privacy incident with "serious injury" risk |
| HIPAA (US Healthcare) | 60 days of discovery | 60 days of discovery | Any unsecured PHI breach |
| HIPAA (>500 in state) | 60 days + media notification | Same | > 500 affected in a state |
| CCPA (California) | N/A (civil action only) | Immediate — prior to contacting individuals | Unauthorized access to PI |
| LGPD (Brazil) | 3 business days (ANPD Res. 15/2023) | 5 business days (high risk) | Significant risk to data subjects |
| PIPL (China) | Immediately | Immediately | Any breach of personal information |
| Singapore PDPA | 3 calendar days | As soon as practicable | Significant harm likely / 500+ individuals |
| Australia Privacy Act | ASAP (NDB scheme) | ASAP | Likely to result in serious harm |
| POPIA (South Africa) | ASAP (reasonable period) | ASAP | Unlawful access to PI |
| NIS2 (EU — critical infrastructure) | 24 hours (early warning) + 72 hours (incident notification) + 1 month (final report) | N/A (NIS2 = regulator/CSIRT) | Significant incidents |

† `[VERIFY — the primary Law 25 text may phrase the CAI/individual duty as "promptly/with diligence" rather than a fixed 72-hour clock. Confirm against PPIPS before relying on the fixed clock. Flag mirrored in the ca-pipeda-law25 taxonomy record. The GDPR 72-hour floor stands independently.]`

---

## GDPR Regulator Notification Template (Arts. 33-34)

**Filing with:** National DPA (ICO for UK; relevant DPA for EU based on controller's main establishment).

**72-hour clock starts:** When controller becomes "aware" of a breach — i.e. has reasonable degree of certainty that a security incident occurred resulting in compromise of PI. Awareness ≠ certainty. If uncertain, notify and update.

**Part 1 notification (within 72 hours — if full information not available):**
```
DATA BREACH NOTIFICATION — PART 1
Notifying organisation: [COMPANY NAME]
DPO contact: [name, email, phone]
Date/time of notification: [datetime]
Date/time breach discovered: [datetime]
Estimated date/time of breach: [if known]

Nature of breach: [describe — e.g. "Unauthorised access to user database
via compromised administrator credential"]

Categories of PI involved: [e.g. "Email addresses, hashed passwords, IP
addresses, subscription status"]

Approximate number of individuals affected: [number or "unknown — under
investigation"]

Categories of individuals: [e.g. "Registered users of [PRODUCT NAME]"]

Likely consequences: [e.g. "Risk of phishing attacks using exposed email
addresses; low risk of account compromise given password hashing"]

Measures taken/proposed: [e.g. "Compromised credential revoked; affected
accounts force-reset; investigation ongoing"]

Further information to follow: [Yes — expected by [date]]

Signature / authorisation: [name, role, date]
```

**Part 2 notification (when full information available):**
```
DATA BREACH NOTIFICATION — PART 2 / UPDATE
Reference: [Part 1 reference number]
Date of this update: [date]

[Update all fields from Part 1 with complete information]

Description of likely consequences (full assessment):
[Detailed assessment of risk to individuals]

Measures taken to address the breach:
[Technical measures: e.g. "Patch applied; logs reviewed; all sessions
invalidated; passwords force-reset via email"]
[Organisational measures: e.g. "Incident response team convened; forensic
investigation engaged; staff briefed"]
[Measures to mitigate adverse effects on individuals: e.g. "Credit
monitoring offered; helpline established"]

Decision on individual notification:
☐ Individual notification required — see Art. 34 notice
☐ Individual notification not required because: [basis — e.g. "PI was
encrypted with strong keys; risk to individuals is low"]
☐ Notification via public communication (Art. 34(3)(c)) because:
[basis — e.g. "Individual notification would involve disproportionate
effort; > 1 million individuals affected"]
```

---

## GDPR Individual Notification Template (Art. 34)

**Threshold:** "Likely to result in a high risk to the rights and freedoms of natural persons."

**Required content (Art. 34(2)):** Plain language description of the breach; DPO contact; likely consequences; measures taken or proposed.

```
Subject: Important notice regarding your [PRODUCT NAME] account

Dear [Name / "Customer"],

We are writing to let you know about a security incident that affected
your [PRODUCT NAME] account.

WHAT HAPPENED
[Plain language description — e.g. "On [date], we discovered that an
unauthorised party gained access to our user database. This occurred
because [brief technical cause — e.g. 'a security vulnerability in our
login system was exploited']."]

WHAT INFORMATION WAS INVOLVED
The following information associated with your account may have been accessed:
• [Email address]
• [Encrypted password — note: your actual password was not exposed]
• [Other fields]

The following information was NOT accessed:
• [Payment card details — we do not store card numbers]
• [Other fields]

WHAT WE ARE DOING
We have:
• [Action 1 — e.g. Secured the vulnerability that caused the breach]
• [Action 2 — e.g. Invalidated all existing login sessions]
• [Action 3 — e.g. Engaged a specialist cybersecurity firm to investigate]

WHAT YOU SHOULD DO
We recommend you:
• Change your [PRODUCT NAME] password immediately: [link]
• If you used the same password on other sites, change it there too
• Be alert to suspicious emails claiming to be from [PRODUCT NAME]
• [Other specific advice relevant to data exposed]

[OPTIONAL: We are offering [12 months of credit monitoring / identity
theft protection] as a precaution. To sign up: [link / instructions]]

CONTACT US
If you have questions: [breach-support@company.com] or [helpline number]
[Hours of operation]

Data Protection Officer: [dpo@company.com]
[If EU: You have the right to lodge a complaint with your national data
protection authority: [link to EDPB DPA list]]

We are sorry this happened and are committed to preventing similar incidents.

[COMPANY NAME]
[Date]
```

---

## PIPEDA Breach Notification (ss. 10.1-10.3)

**Threshold:** "Real risk of significant harm" (RROSH). Factors: sensitivity of PI, number of individuals, whether PI has been misused.

**OPC Report of Breach Form fields:**
```
Organisation name and contact:
Date breach discovered:
Date breach occurred (estimate):
Nature of PI involved:
Number of individuals affected:
Provinces/territories of affected individuals:
How the breach occurred:
What the organisation has done/plans to do:
Has law enforcement been contacted? [Yes/No]
Have affected individuals been notified? [Yes/No/Planned]
```

**Individual notification (must be direct):**
```
Subject: Notice of privacy breach — your personal information

Dear [Name],

We are contacting you to let you know that [COMPANY NAME] experienced
a privacy breach that may affect your personal information.

WHAT HAPPENED: [description]

INFORMATION INVOLVED: [specific PI]

RISK TO YOU: We have assessed that this breach creates a real risk of
[describe: identity theft / financial harm / reputational harm / other].

WHAT WE ARE DOING: [actions taken]

WHAT YOU SHOULD DO: [specific recommendations]

Contact us: [privacy@company.com] or [phone]
You may also contact the Office of the Privacy Commissioner of Canada
at 1-800-282-1376 or priv.gc.ca.

[COMPANY NAME]
```

---

## HIPAA Breach Notification (45 CFR §§ 164.400-414)

**Threshold:** Breach of "unsecured" PHI — PHI not rendered unusable, unreadable, or indecipherable through encryption or destruction per HHS guidance.

**Safe harbor (not a reportable breach):** PHI encrypted per NIST guidelines + encryption key not compromised; or PHI destroyed (media sanitized per NIST 800-88).

**Risk assessment (§ 164.402(2)) — four factors:**
1. Nature and extent of PHI involved (types of identifiers, re-identification likelihood)
2. Who accessed or could access the PHI
3. Whether PHI was actually acquired or viewed
4. Extent to which risk has been mitigated

If low probability of compromise → not a reportable breach.

**Individual notification (§ 164.404):**
```
[COVERED ENTITY NAME]
[Address]
[Date]

NOTICE OF BREACH OF UNSECURED PROTECTED HEALTH INFORMATION

Dear [Name]:

We are writing to inform you of a breach of your unsecured protected
health information.

WHAT HAPPENED: [description of breach, including date of breach and
date of discovery]

WHAT INFORMATION WAS INVOLVED: [describe types of unsecured PHI —
e.g. name, dates of service, diagnosis codes, insurance information]

WHAT WE ARE DOING: [describe actions taken and planned]

WHAT YOU CAN DO: [specific recommendations — e.g. review Explanation
of Benefits, monitor credit reports, contact insurer]

FOR MORE INFORMATION: Contact our Privacy Officer:
[Name, Title]
[Phone — toll-free if > 500 individuals]
[Email]
[Hours]

[If > 500 individuals: We have notified the Secretary of Health and
Human Services and media outlets as required by law.]

We deeply regret this incident. Protecting your health information
is our highest priority.

Sincerely,
[Covered Entity Name]
```

**HHS breach reporting portal:** ocrportal.hhs.gov/ocr/breach/wizard_breach.jsf  
**Deadline:** 60 days of discovery. < 500 individuals: annual log submission. ≥ 500: immediate report.

---

## LGPD Breach Notification (Art. 48 + ANPD Resolution CD/ANPD No. 15/2023)

**Deadlines:** 3 business days to ANPD (from discovery); 5 business days to data subjects (for high-risk incidents).

**ANPD notification must include:**
```
1. Date of the incident and date of discovery
2. Nature of the affected personal data
3. Number of affected data subjects (or estimate)
4. Data subjects affected (categories)
5. Technical and security measures used to protect the data
6. Risks related to the incident
7. Reasons for delay in notification (if applicable)
8. Measures taken or to be taken to reverse/mitigate effects
9. Whether data processing has been interrupted and for how long
10. Contact of the DPO (if appointed)
```

---

## Internal Breach Response Checklist

Run immediately on discovering a potential breach:

**Hour 0-4 (Contain):**
- [ ] Convene incident response team
- [ ] Isolate affected systems (revoke credentials, segment network)
- [ ] Preserve evidence (logs, memory dumps) before remediation
- [ ] Determine scope: what data, how many individuals, how accessed
- [ ] Determine if breach is still ongoing

**Hour 4-24 (Assess):**
- [ ] Assess what PI was involved and its sensitivity
- [ ] Apply GDPR risk assessment (or HIPAA four-factor test, or RROSH test)
- [ ] Determine notification obligations and deadlines
- [ ] Engage legal counsel
- [ ] Document all decisions and their basis

**Hour 24-72 (Notify regulators if required):**
- [ ] File Part 1 notification with DPA(s) if GDPR threshold met
- [ ] File with HHS if HIPAA breach
- [ ] Notify OPC if PIPEDA RROSH threshold met
- [ ] Notify CAI within 72 hours if Quebec Law 25 threshold met

**Day 3-30 (Notify individuals if required):**
- [ ] Draft individual notification letter
- [ ] Legal/DPO review of notification letter
- [ ] Send to affected individuals via direct contact method
- [ ] Establish support helpline / dedicated email
- [ ] Consider credit monitoring or identity protection if financial data exposed

**Ongoing:**
- [ ] File complete GDPR Part 2 notification when investigation complete
- [ ] Document lessons learned and implement preventive measures
- [ ] Review and update DPIA if applicable
- [ ] Confirm annual HHS log filing if < 500 HIPAA breach
