# Record: South Africa — POPIA

| | |
|---|---|
| **Record** | `za-popia` · **Status/Tier:** SCAFFOLD / Tier 2 · **Schema:** v1.0 · **Current as of:** 2026-07-04 |
| **Instrument** | Protection of Personal Information Act, Act 4 of 2013; enforcement operative July 1 2021 |
| **Sources** | `data-minimization--regulatory-reference.md` §POPIA · `consent-language--breach-notification.md` · `consent-language--childrens-consent.md` |

**Source-accuracy caution:** the suite's POPIA condition table (ss. 8–25) compresses the eight conditions into single section numbers whose assignments look shifted against the statute's actual structure `[VERIFY — canonical POPIA spreads conditions across ranges: quality s. 16, openness ss. 17–18, safeguards ss. 19–22, participation ss. 23–25; the suite table maps quality→§12, openness→§13, safeguards→§14, participation→§15. Confirm every section number against the primary Act before downstream use]`. Cells below carry the suite's values with this flag standing over them.

## A0 — Scope
Responsible parties processing PI. Extraterritorial reach: *not located*. Thresholds/exemptions: *not located*.

## A1 — Enforcement
**Information Regulator (IR)** per the POPIA section text `[VERIFY — the jurisdiction quick-select tables render this as "IOPA / IO"; "Information Regulator" is the correct body name]`. Penalties: up to ZAR 10M or imprisonment up to 10 years. Private right of action: *not located*.

## A2 — Lawful Basis & Consent
`basis_model:` *not located* — POPIA's justification grounds (s. 11) are not in suite sources `[UNVERIFIED — s. 11 lists consent, contract, legal obligation, legitimate interest et al.; confirm]`. Sensitive escalation: § 26 prohibition except § 27 grounds. Direct marketing by electronic communication: prior consent (§ 69). Tag: `PROCEDURAL`.

## A3 — Collection Limitation
`test_type:` necessity (non-excessiveness). **§ 9 processing limitation** — PI must be adequate, relevant, and **not excessive** (mirrors GDPR Art. 5(1)(c) verbatim, per source) + **§ 10 purpose specification** — specific, explicitly defined, lawful purpose. Together these constitute the POPIA minimization framework (sourced). P-mapping: **P1** (§ 9), **P1/P2** (§ 10). Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation
§ 10 purpose specification + § 11 further-processing limitation (compatibility with original purpose) `[VERIFY — further-processing is s. 15 in the canonical numbering; suite table says § 11]`. P2. Tag: `PROCEDURAL` + `ARCH-SATISFIES` via separation.

## A5 — Sensitive Categories
`sensitive_model:` prohibitive-list. § 26 special information: religious/philosophical beliefs; race/ethnic origin; trade union membership; political persuasion; health/sex life; biometric information; criminal behaviour. Processing prohibited except on § 27 grounds. Tag: `ARCH-DISSOLVES` where provable-not-disclosable; else `PROCEDURAL`.

## A6 — Rights
Data subject participation — access and correction (§ 15 per suite table `[VERIFY — canonical ss. 23–25]`). Erasure / restriction / portability / objection / ADM: *not located in suite sources*. Response clock: *not located*. Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
No dedicated retention condition in suite sources — *not located* `[UNVERIFIED — canonical POPIA s. 14 covers retention and restriction of records; confirm]`. P4. Tag: `ARCH-SATISFIES` (TTL) pending confirmed anchor.

## A8 — Breach Notification
`clock_model:` promptness-standard. "As soon as reasonably possible" to regulator and individuals; threshold: unlawful access to PI (per `consent-language--breach-notification.md` timeline table). Statutory anchor `[UNVERIFIED — s. 22 security-compromise notification; not in suite sources]`. Tag: duty `PROCEDURAL`; trigger shrinks with minimized holdings.

## A9 — Children
**Under 18**; parental/guardian consent — § 35 (per `consent-language--childrens-consent.md` age table). Tag: `PROCEDURAL`.

## A10 — Cross-Border Transfer
*Not located in suite sources* `[UNVERIFIED — canonical anchor s. 72 (adequacy / binding rules / consent / contract necessity); confirm]`. `transfer_model:` pending confirmation.

## A11 — Security Safeguards
Security safeguards condition — integrity and confidentiality via technical/organisational measures (§ 14 per suite table `[VERIFY — canonical ss. 19–22]`). **P7**. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA
`dpia_model:` none documented in suite sources — *not located*.
