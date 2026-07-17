# Record: Japan — APPI

| | |
|---|---|
| **Record** | `jp-appi` · **Status/Tier:** FULL / Tier 3a · **Schema:** v1.0 · **Current as of:** 2026-07-04 |
| **Instrument** | Act on the Protection of Personal Information (個人情報の保護に関する法律), Act No. 57 of 2003; major amendments 2015 (eff. 2017) and 2020 (eff. April 2022) |
| **Sources** | `skills/data-minimization/references/regulatory-reference.md` §APPI |

**Distinctive:** statutory intermediate data categories — pseudonymously processed (仮名加工情報) and anonymously processed (匿名加工情報) information — the clearest statutory recognition of the ARCH-SATISFIES tier among modeled regimes.

## A0 — Scope
Business operators handling personal information. Extraterritorial mechanism (2022): **Art. 24-bis** — domestic operators must impose equivalent obligations on overseas recipients via contract or equivalent measures (obligation-follows-the-data rather than direct long-arm reach).

## A1 — Enforcement
Personal Information Protection Commission (**PPC**). Penalties (2022 amendments): corporations up to **JPY 100M**; individuals up to JPY 1M; JPY 500,000 for reporting violations. Private right of action: *not located*.

## A2 — Lawful Basis & Consent
`basis_model:` consent-centric hybrid — acquisition is purpose-specification-based (Art. 17(1)); **explicit consent required for acquiring sensitive information (Art. 17(2))**; third-party provision ordinarily consent-or-opt-out, but **the opt-out route is statutorily barred for sensitive information** (2022 amendment, sourced). Tag: `PROCEDURAL`.

## A3 — Collection Limitation
`test_type:` necessity (purpose-bounded). **Art. 17(1):** personal information shall be acquired with specification of the purpose of use and not beyond the scope necessary to achieve it. P-mapping: **P1**. Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation
Art. 17(1) purpose specification bounds acquisition and use. P2. Tag: `PROCEDURAL` + `ARCH-SATISFIES` via separation.

## A5 — Sensitive Categories
`sensitive_model:` prohibitive-list (consent-escalation form). **要配慮個人情報, Art. 2(3):** racial origin; creed; social status; medical history; criminal record; criminal-damage record; plus cabinet-order categories (disability, health-examination results). Explicit consent for collection (Art. 17(2)); no opt-out third-party provision. Tag: `ARCH-DISSOLVES` where provable-not-disclosable; else `PROCEDURAL`.

## A6 — Rights
*Not located in suite sources* — the source covers operator obligations, not the data-subject rights chapter `[UNVERIFIED — Arts. 33–35 range (disclosure, correction, cessation-of-use); 2020 amendment expanded scope; confirm]`. Response clock: *not located*. Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
**Art. 19:** keep personal data accurate and up to date within the scope necessary for the purpose, and **delete without delay when no longer required** — a self-executing entity-side deletion duty. **Statutory intermediate categories (2022):** pseudonymously processed information (仮名加工情報) — internal use under lighter obligations; anonymously processed information (匿名加工情報) — stricter de-identification standard, outside core obligations. P4 (P6/P7 for the categories). Tag: `ARCH-SATISFIES` — the category system is a statutory reward ladder for exactly the transforms the suite's remediation vocabulary applies (TOKENIZE → 仮名加工, AGGREGATE/anonymize → 匿名加工).

## A8 — Breach Notification
*Not located in suite sources* — no Japan row in the breach timeline table `[UNVERIFIED — 2022 amendments added mandatory PPC reporting + individual notice for defined breach classes (sensitive data, financial harm risk, 1,000+ subjects); confirm anchors and clocks]`. `clock_model:` pending confirmation. Tag: duty `PROCEDURAL`.

## A9 — Children
*Not located* — no Japan row in the children's age table; APPI sets no general age threshold `[UNVERIFIED — PPC guidance treats minors' consent capacity case-by-case; confirm]`.

## A10 — Cross-Border Transfer
`transfer_model:` adequacy+mechanisms (equivalence-confirmation form). 2022 amendments: confirm equivalent protection level in the receiving country **and provide individuals with required information** about the transfer; Art. 24-bis contractual equivalence for overseas recipients. Tag: `PROCEDURAL` + `ARCH-DISSOLVES` for non-personal-before-export (匿名加工情報 exits scope).

## A11 — Security Safeguards
**Art. 20:** necessary and appropriate action to prevent leakage, loss, or damage and otherwise securely manage personal data. Principles-based. **P7**. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA
`dpia_model:` none — no APPI DPIA regime in suite sources; *not located* `[UNVERIFIED — PPC recommends PIAs in guidance; no statutory mandate; confirm]`.
