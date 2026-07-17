# Record: Singapore — PDPA

| | |
|---|---|
| **Record** | `sg-pdpa` · **Status/Tier:** SCAFFOLD / Tier 2 · **Schema:** v1.0 · **Current as of:** 2026-07-04 |
| **Instrument** | Personal Data Protection Act 2012 (No. 26 of 2012), substantially amended by PDP (Amendment) Act 2020 (No. 40 of 2020), eff. Feb 1 2021 |
| **Sources** | `skills/data-minimization/references/regulatory-reference.md` §Singapore PDPA · `skills/consent-language/references/breach-notification.md` |

## A0 — Scope
Organisations collecting, using, or disclosing personal data of individuals in Singapore; extraterritorial where processing relates to individuals in Singapore.

## A1 — Enforcement
PDPC. Penalties: up to SGD 1M or **10% of annual Singapore turnover** (whichever higher, egregious cases post-2020 amendment). Private right of action: *not located*.

## A2 — Lawful Basis & Consent
`basis_model:` consent-centric **hybrid** — consent (ss. 14–17) plus the 2020 amendment's expanded deemed-consent and exception layer: deemed consent by contractual necessity, deemed consent by notification with opt-out, and a legitimate-interests exception with a proportionality test (ss. 15A–15D). Second Schedule consent exceptions: research/news/artistic, legal proceedings, life-threatening emergencies, publicly available data (narrower than GDPR legitimate interests but meaningful for security research, per source). Notification duty: s. 20. Tag: `PROCEDURAL`.

## A3 — Collection Limitation
`test_type:` **reasonableness** — s. 18: collect only for purposes "that a reasonable person would consider appropriate." Explicitly contrasted in the source with GDPR's necessity test and CCPA's proportionality test: **a lower but vaguer standard**; PDPC advisory guidelines supply the concrete examples. P-mapping: **P1**. Tag: `ARCH-DISSOLVES` (a minimized design passes any reasonableness inquiry by construction).

## A4 — Purpose Limitation
s. 18: collect/use/disclose only for purposes notified and consented to; s. 20 notification at/before collection. P2. Tag: `PROCEDURAL` + `ARCH-SATISFIES`.

## A5 — Sensitive Categories
`sensitive_model:` contextual — **no statutory special-category list appears in suite sources**; the PDPA regulates sensitivity through the reasonableness and protection obligations rather than an enumerated class `[UNVERIFIED — PDPC guidance treats e.g. NRIC numbers, health and financial data as higher-risk; confirm before relying]`. Tag: `ARCH-SATISFIES` (sensitivity-scaled safeguards).

## A6 — Rights
Access/correction obligations: *not located in suite source tables* `[UNVERIFIED — canonical anchors ss. 21–22; confirm]`. Accuracy: s. 23. **Portability: Part VIA** (2020 amendment) — designated organisations must port data in machine-readable format on request; phased, currently banks and telecommunications. Do Not Call Registry: Part IX (marketing to SG numbers; up to SGD 10,000 per message). Response clock: *not located*. Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
**s. 25 retention limitation** — cease retention when purpose no longer served and retention not legally required. P4. Tag: `ARCH-SATISFIES` (TTL automation is direct performance).

## A8 — Breach Notification
`clock_model:` fixed-clock. ss. 26C–26H (2020 amendment): **3 calendar days to PDPC** from determining a breach notifiable; individuals "as soon as practicable" where significant harm likely (financial loss, physical/psychological harm, humiliation, reputational damage per PDPC guidance); **500+ affected individuals triggers PDPC notification regardless of harm assessment**. Tag: duty `PROCEDURAL`; the 500-person and significant-harm thresholds are direct functions of holdings — minimization shrinks both.

## A9 — Children
*Not located* — no Singapore row in the suite's children's-consent age table `[UNVERIFIED — PDPC advisory guidance addresses minors' consent capacity; no statutory age in the Act; confirm]`.

## A10 — Cross-Border Transfer
`transfer_model:` adequacy+mechanisms (comparable-protection standard). **s. 26**: transfer only where the recipient jurisdiction/organisation provides protection comparable to the PDPA. P6. Tag: `PROCEDURAL` + `ARCH-DISSOLVES` for non-personal-before-export designs.

## A11 — Security Safeguards
**s. 24 protection obligation** — reasonable security arrangements against unauthorised access, collection, use, disclosure, copying, modification, disposal. Principles-based. **P7**. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA
`dpia_model:` none statutory — PDPC advisory: DPIAs recommended for significant personal-data processing activities (sourced: `skills/privacy-impact-assessment/SKILL.md` regime table — upgraded from [UNVERIFIED] 2026-07-04, see reconciliation log). The Act mandates none.
