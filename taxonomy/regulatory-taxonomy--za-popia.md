# Record: South Africa — POPIA

| | |
|---|---|
| **Record** | `za-popia` · **Status/Tier:** SCAFFOLD / Tier 2 · **Schema:** v1.0 · **Current as of:** 2026-07-17 (verification pass) |
| **Instrument** | Protection of Personal Information Act, Act 4 of 2013; enforcement operative July 1 2021 |
| **Sources** | `skills/data-minimization/references/regulatory-reference.md` §POPIA · `skills/consent-language/references/breach-notification.md` · `skills/consent-language/references/childrens-consent.md` · **primary-source web check 2026-07-05** (gov.za Act text; popia.co.za; see reconciliation log) |

**Correction record (2026-07-05):** the suite's original condition table compressed each condition into a single shifted section number. Canonical structure, now used throughout: Accountability **s. 8** · Processing limitation **ss. 9–12** (lawfulness s. 9; **minimality s. 10** — adequate, relevant, not excessive; consent/justification s. 11; direct collection s. 12) · Purpose specification **ss. 13–14** (s. 14 = retention) · Further-processing limitation **s. 15** · Information quality **s. 16** · Openness **ss. 17–18** · Security safeguards **ss. 19–22** (breach notification **s. 22**) · Data-subject participation **ss. 23–25**.

## A0 — Scope
Responsible parties processing PI. Extraterritorial reach: *not located*. Thresholds/exemptions: *not located*.

## A1 — Enforcement
**Information Regulator (IR)** (naming corrected — one suite table had "IOPA"). Penalties: up to ZAR 10M or imprisonment up to 10 years. Private right of action: *not located*.

## A2 — Lawful Basis & Consent
`basis_model:` justification-grounds — **s. 11**: consent, contract, legal obligation, protection of legitimate interest, public-law duty, legitimate interests of responsible/third party (web-confirmed placement; enumeration `[UNVERIFIED — confirm the full s. 11(1) list against the Act text]`). Sensitive escalation: § 26 prohibition except § 27 grounds. Direct marketing by electronic communication: prior consent (§ 69). Tag: `PROCEDURAL`.

## A3 — Collection Limitation
`test_type:` necessity (non-excessiveness). **s. 10 — minimality:** PI must be adequate, relevant, and **not excessive** (mirrors GDPR Art. 5(1)(c)); within the processing-limitation condition ss. 9–12. P-mapping: **P1**. Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation
**s. 13** purpose specification (specific, explicitly defined, lawful purpose) + **s. 15** further-processing compatibility. P2. Tag: `PROCEDURAL` + `ARCH-SATISFIES` via separation.

## A5 — Sensitive Categories
`sensitive_model:` prohibitive-list. § 26 special information: religious/philosophical beliefs; race/ethnic origin; trade union membership; political persuasion; health/sex life; biometric information; criminal behaviour. Processing prohibited except on § 27 grounds. Tag: `ARCH-DISSOLVES` where provable-not-disclosable; else `PROCEDURAL`.

## A6 — Rights
Data-subject participation **ss. 23–25**: access (s. 23), correction/deletion request (s. 24), manner of request (s. 25). Objection: s. 11(3) `[UNVERIFIED — confirm]`. Portability: none in the Act. Response clock: *not located*. Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
**s. 14:** retention only as long as necessary for the purpose; destruction/deletion/de-identification thereafter (within the purpose-specification condition). P4. Tag: `ARCH-SATISFIES` (TTL).

## A8 — Breach Notification
`clock_model:` promptness-standard. **s. 22:** notify the Information Regulator and affected data subjects **as soon as reasonably possible** after reasonable grounds to believe PI was accessed/acquired unlawfully (anchor web-confirmed; previously [UNVERIFIED]). Tag: duty `PROCEDURAL`; trigger shrinks with minimized holdings.

## A9 — Children
**Under 18**; parental/guardian consent — § 35 (per children's-consent age table). Tag: `PROCEDURAL`.

## A10 — Cross-Border Transfer
**s. 72(1)** (web-verified 2026-07-17) — grounds: recipient bound by law / BCRs / binding agreement providing substantially-similar protection (incl. onward-transfer rules) · consent · contract performance with or in the interest of the data subject · transfer for the data subject's benefit where consent is impracticable but likely. `transfer_model:` adequacy+mechanisms.

## A11 — Security Safeguards
**ss. 19–22:** appropriate, reasonable technical and organisational measures against loss, damage, unauthorised destruction, and unlawful access/processing (s. 19); operator duties (ss. 20–21); breach notification (s. 22). **P7**. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA
`dpia_model:` none documented — *not located* (a PIA appears in the Regulator's s. 55 prior-authorisation/compliance-framework context `[UNVERIFIED]`).
