# Record: EU/EEA — GDPR + UK GDPR

| | |
|---|---|
| **Record** | `eu-gdpr-uk` |
| **Instruments** | Regulation (EU) 2016/679 (in force 25 May 2018) · UK GDPR + Data Protection Act 2018, c. 12 |
| **Status / Tier** | FULL / Tier 1 |
| **Schema** | v1.0 |
| **Current as of** | 2026-07-04 (content dated June 2026 in sources) |
| **Sources** | `skills/data-minimization/references/regulatory-reference.md` · `skills/data-minimization/references/pipeda-gdpr.md` · `skills/consent-language/SKILL.md` · `skills/consent-language/references/rights-language.md` · `skills/consent-language/references/breach-notification.md` · `skills/consent-language/references/childrens-consent.md` · `skills/consent-language/references/cookie-consent.md` · `skills/privacy-impact-assessment/references/dpia-triggers.md` |
| **Related sectoral overlays** | ePrivacy Directive 2002/58/EC (*lex specialis* for terminal-equipment access — cookie consent is ePrivacy, not GDPR) · EU AI Act Reg. 2024/1689 · NIS2 · DORA — registered SECTORAL in master |

**Design rule (sourced):** UK GDPR mirrors EU GDPR — treat identically for minimization; divergences listed in the block at the end.

---

## A0 — Scope & Applicability

- **Territorial + extraterritorial:** Art. 3 — applies to processing of EU data subjects' data by controllers/processors regardless of establishment where offering goods/services or monitoring behavior (referenced in suite via LGPD Art. 3 "mirrors GDPR Art. 3" and AI Act "mirrors GDPR scope logic").
- Covered entities: controllers and processors.
- Thresholds/exemptions: none stated in suite sources — *not located*.

## A1 — Enforcement

- Authority: national supervisory DPAs (ICO, CNIL, BfDI, Irish DPC, etc.); EDPB coordination.
- Penalty ceiling: **Art. 83(4)** €10M / 2% global turnover (incl. Art. 25 violations) · **Art. 83(5)** €20M / 4% (incl. Art. 5 violations). Minimization failures sit in the *upper* tier.
- Private right of action: not stated in suite sources — *not located*. `[UNVERIFIED — Art. 79/82 provide judicial remedy and compensation; confirm against primary source]`

## A2 — Lawful Basis & Consent Model

- `basis_model:` **enumerated-bases** — Art. 6(1): consent (a), contract (b), legal obligation (c), legitimate interests (f) (bases as used across `skills/consent-language/SKILL.md`; the vital-interests and public-task bases are not exercised in suite sources — *not located there*, standard Art. 6(1)(d),(e) `[UNVERIFIED]`).
- Consent standard: Art. 4(11) — freely given, specific, informed, unambiguous affirmative action; no pre-ticked boxes (Planet49 C-673/17); as easy to withdraw as to give (Art. 7(3)).
- Sensitive escalation: Art. 9(1) prohibition absent explicit consent or an Art. 9(2) ground — **opt-in by construction**.
- Legitimate interests require a documented LIA; absolute objection right for direct marketing (Art. 21(2)).

Tag: `PROCEDURAL` (consent/notice UX). Note: under ePrivacy Art. 5(3), GDPR bases do **not** substitute for consent for terminal-equipment access.

## A3 — Collection Limitation (minimization hook)

- `test_type:` **necessity (three-limb)**.
- **Art. 5(1)(c):** "adequate, relevant and limited to what is necessary" — adequacy + relevance + necessity; every HIGH+ minimization finding fails at least one limb. Recitals 39, 78.
- **Art. 25(1)** privacy by design (legal obligation, not best practice); **Art. 25(2)** by default — default settings must minimize; P1 violations in defaults are Art. 25(2) violations.

P-mapping: **P1, P3** (5(1)(c)); All (25(1)); P1, P2 (25(2)). Tag: `ARCH-DISSOLVES` — Art. 25 is the statute *demanding* privacy-by-architecture; a selective-disclosure design is direct performance of the obligation.

## A4 — Purpose Limitation

- Art. 5(1)(b): specified, explicit, legitimate purposes; no incompatible further processing.

P-mapping: P2. Tag: `PROCEDURAL` (purpose spec) + `ARCH-SATISFIES` via separation and scoped identifiers (P5, P6).

## A5 — Sensitive Categories

- `sensitive_model:` **prohibitive-list.** Art. 9(1): health, biometric, genetic, racial/ethnic origin, political opinions, religious beliefs, trade union membership, sexual orientation — processing prohibited absent explicit consent or Art. 9(2) ground. Criminal data: Art. 10.
- Escalation rule (sourced): any Art. 9 field is CRITICAL tier regardless of context. **Derived/inferred data counts** — a model inferring an Art. 9 attribute produces special-category data even if none was collected (per `skills/data-minimization/SKILL.md` Step 2b).

Tag: `ARCH-DISSOLVES` where the attribute is proven, not disclosed (ZKP predicate proofs, anonymous credentials — `skills/privacy-architecture/SKILL.md`); otherwise `PROCEDURAL` (explicit-consent mechanics).

## A6 — Data-Subject Rights

| Right | EU GDPR | UK GDPR |
|---|---|---|
| Access | Art. 15 | Art. 15 |
| Rectification | Art. 16 | Art. 16 |
| Erasure | Art. 17 (exceptions 17(3)) | Art. 17 |
| Restriction | Art. 18 | Art. 18 |
| Portability | Art. 20 | Art. 20 |
| Objection | Art. 21(1); absolute for direct marketing 21(2) | Art. 21 |
| ADM/profiling | Art. 22 (human review, express view, contest) | Art. 22 |
| Opt-out-of-sale / limit-sensitive / de-indexing | — (no CCPA-style rights; de-indexing case law not modeled here) | — |

- **Response clock:** 1 month + 2-month extension (notify within the first month with reason). Complaint right to supervisory authority (Art. 13 checklist; edpb.europa.eu member list / ICO).
- Notice duties feeding rights: Arts. 13/14 (full checklist in `skills/consent-language/SKILL.md` Step 4).

Tag: `PROCEDURAL`; **erasure is the flagship split-tag** — see A7.

## A7 — Retention & Erasure

- Art. 5(1)(e) storage limitation: not kept identifiable longer than necessary.
- Art. 17 erasure grounds + 17(3) exceptions (legal obligation, public interest, legal claims).
- **Immutability conflict (sourced):** Art. 17 vs blockchain — EDPB Guidelines 05/2019 acknowledge without resolving. Mitigations: encrypt-before-write with key deletion as practical erasure; content-addressed hashes on-chain; personal data fully off-chain. Consult DPA before relying on encryption-as-erasure in a regulated context. This is the suite's canonical collision between privacy-by-architecture and privacy-by-policy (`skills/privacy-suite/SKILL.md`).

P-mapping: P4 (+ P6 via 17(1)). Tag: `ARCH-SATISFIES` (TTL, crypto-erasure) · `ARCH-DISSOLVES` for commitment-only/off-chain designs · residual `PROCEDURAL` limb for request handling.

## A8 — Breach Notification

- `clock_model:` **fixed-clock.**
- **Art. 33:** 72 hours to DPA from awareness (awareness ≠ certainty — notify and update; Part 1/Part 2 pattern per `skills/consent-language/references/breach-notification.md`). All breaches to regulator unless unlikely to risk rights `[UNVERIFIED — the "unlikely to result in a risk" carve-out is standard Art. 33(1) text but not stated in suite sources]`.
- **Art. 34:** individuals without undue delay where high risk; content per 34(2); public-communication alternative 34(3)(c) for disproportionate effort.

Tag: duty `PROCEDURAL`; trigger `ARCH-SATISFIES` (Art. 34 exemption where data rendered unintelligible — strong encryption defeats the individual-notice trigger `[UNVERIFIED — Art. 34(3)(a) basis; suite sources state the practical rule ("PI was encrypted with strong keys; risk is low") without the citation]`).

## A9 — Children

- **Art. 8:** consent-based processing lawful from 16; member states may lower to 13. Member-state table in `skills/consent-language/references/childrens-consent.md` (13: Nordics/Baltics et al.; 14: AT/HU/IT/ES; 15: FR; 16: DE/IE/NL et al.).
- Art. 8(2): reasonable efforts to verify parental consent.
- UK: 13 + **Age Appropriate Design Code** applies to all under-18-likely services — 15 standards incl. high-privacy defaults, geolocation off, profiling off, no nudges; DPIA expected for in-scope products.

Tag: `PROCEDURAL` (verification mechanics); AADC defaults are `ARCH-SATISFIES` obligations (the code mandates architecture).

## A10 — Cross-Border Transfer

- `transfer_model:` **adequacy+mechanisms.** Disclosure duty: Art. 13(1)(f). Mechanisms: adequacy decisions, SCCs, BCRs under Chapter V `[UNVERIFIED — Arts. 44–49 not cited in suite sources; confirm]`. Switzerland holds adequacy (sourced); Argentina holds adequacy (Decision 2003/490/EC, sourced).
- Practical enforcement signal (sourced): GA4 without safeguards ruled non-compliant by CNIL/DSK/Austrian DSB over US transfers.

Tag: `PROCEDURAL` (mechanism paperwork) + `ARCH-DISSOLVES` where data is non-personal before export (aggregation/DP) or never leaves (local processing, PSI/MPC).

## A11 — Security Safeguards

- Art. 5(1)(f) integrity & confidentiality; Art. 32 `[UNVERIFIED — Art. 32 not cited in suite sources; suite grounds security in 5(1)(f)]`. Specificity: principles-based.

P-mapping: P7. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA

- `dpia_model:` **mandatory-triggered.**
- **Art. 35(3)** automatic triggers: (a) systematic extensive automated evaluation/profiling with significant effects; (b) large-scale Art. 9/10 processing; (c) large-scale systematic monitoring of public areas.
- **EDPB Guidelines 09/2022:** nine criteria; **two or more → mandatory**. National mandatory lists (ICO 11, CNIL 17, BfDI 16) under Art. 35(4).
- Prior consultation: Art. 36 when residual risk high `[UNVERIFIED — Art. 36 named in skills/privacy-suite/SKILL.md description ("Art. 36 prior consultation trigger") but mechanics not detailed in sources]`.

Tag: `PROCEDURAL`; selective-disclosure design shrinks the risk register the DPIA must document.

---

## Divergence Block — UK GDPR vs EU GDPR (sourced)

- Instrument: retained via DPA 2018, c. 12; regulator ICO; treat identically for minimization.
- Children: UK fixed at 13; **AADC** adds under-18 design code with DPIA expectation (no EU-wide equivalent).
- Cookies: PECR 2003 implements ePrivacy in the UK; ICO 2023 draft guidance broadly aligns with EDPB; ICO recognizes GPC as legitimate opt-out signal (EU: EDPB Opinion 8/2024 — valid for consent *withdrawal*, not initial consent).
- Complaint route: ico.org.uk.
