# Record: Canada — PIPEDA + Quebec Law 25

| | |
|---|---|
| **Record** | `ca-pipeda-law25` |
| **Instruments** | PIPEDA, S.C. 2000, c. 5 (Schedule 1 principles; breach ss. 10.1–10.3) · Quebec Law 25, S.Q. 2021, c. 25 (amending PPIPS) |
| **Status / Tier** | FULL / Tier 1 |
| **Schema** | v1.0 |
| **Current as of** | 2026-07-04 (content dated June 2026 in sources) |
| **Sources** | `data-minimization--regulatory-reference.md` · `data-minimization--pipeda-gdpr.md` · `consent-language--breach-notification.md` · `consent-language--childrens-consent.md` · `consent-language--rights-language.md` · `privacy-impact-assessment--dpia-triggers.md` |
| **Reform watch** | Bill C-27 (CPPA + AIDA) would replace PIPEDA with a GDPR-aligned regime — verify current Parliamentary status before relying on PIPEDA-specific analysis |

**Design rule (sourced):** design to Law 25 standard for any Quebec data subjects — stricter than PIPEDA on all counts and materially aligned with GDPR.

---

## A0 — Scope & Applicability

- **Territorial:** private-sector organizations; federal statute. Enforcement under s. 11.
- **Overlay:** Quebec Law 25 applies stricter obligations for Quebec data subjects (CAI-enforced; substantive obligations in force Sept 22 2023).
- **Extraterritorial reach:** not stated in suite sources — *not located*. `[UNVERIFIED — OPC asserts jurisdiction via real-and-substantial-connection test; confirm against primary source]`
- **Thresholds/exemptions:** none stated in suite sources — *not located*.

Tag: — (scope axes carry no obligation).

## A1 — Enforcement

| | PIPEDA | Law 25 |
|---|---|---|
| Authority | OPC (s. 11) | CAI |
| Penalty ceiling | not stated in suite sources — *not located* | CAD 25M or 4% worldwide turnover (Art. 90.1 PPIPS) |
| Private right of action | not stated — *not located* | not stated — *not located* |

## A2 — Lawful Basis & Consent Model

- `basis_model:` **consent-centric** — no enumerated basis list; meaningful consent for collection, use, disclosure (Cl. 4.3).
- Default posture: consent may be express or implied as appropriate to sensitivity (per `consent-language.md` PIPEDA checklist: "meaningful consent (explicit or implicit as appropriate)").
- Sensitive escalation: **Law 25 requires explicit opt-in consent for sensitive PI (Art. 12 PPIPS)** — opt-out insufficient.
- Withdrawal: objection/withdrawal hook Cl. 4.3.8 (per rights matrix).

P-mapping: P1, P2 (Cl. 4.2, 4.3 per `data-minimization--pipeda-gdpr.md`). Tag: `PROCEDURAL` (consent UX/notice); the *need* for consent narrows under selective disclosure — data not collected requires no consent (tagging rule 1).

## A3 — Collection Limitation (minimization hook)

- `test_type:` **necessity + non-indiscriminate**.
- Operative text: Cl. 4.4 — collect only what is necessary for stated purpose; **Cl. 4.4.1: "The organization shall not collect personal information indiscriminately."** Every field lacking a documented collection purpose is a 4.4.1 violation.
- Law 25 overlay: Art. 9 (necessity) per jurisdiction quick-select.

P-mapping: **P1** (primary statutory hook). Tag: `ARCH-DISSOLVES` — the obligation is satisfied *by construction* in a selective-disclosure design; this is the axis where architecture and statute say the same thing (Hughes' transaction necessity ≡ Cl. 4.4, per `privacy-suite.md`).

## A4 — Purpose Limitation

- Cl. 4.2 (identify purposes before/at collection); Cl. 4.5 (no use/disclosure for other purposes without consent).

P-mapping: P2 (+ P4 via 4.5 retention limb). Tag: `PROCEDURAL` (purpose documentation) + `ARCH-SATISFIES` where purpose-binding is enforced by separation (P6) and scoped identifiers (P5).

## A5 — Sensitive Categories

- `sensitive_model:` **contextual — no closed list.** PIPEDA scales safeguards to sensitivity (Cl. 4.7.1: safeguards "appropriate to the sensitivity of the information") rather than enumerating categories.
- Law 25 overlay: explicit consent required for "sensitive PI" (Art. 12 PPIPS); the suite sources do not enumerate a Quebec category list — *not located*.

P-mapping: P7 via 4.7.1. Tag: `ARCH-SATISFIES` (sensitivity-scaled technical safeguards).

## A6 — Data-Subject Rights

| Right | PIPEDA | Law 25 |
|---|---|---|
| Access | Cl. 4.9 | Art. 27 PPIPS |
| Rectification | Cl. 4.9 | Art. 27 PPIPS |
| Erasure/disposal | Cl. 4.5.3 (destruction when no longer required) | Art. 28 PPIPS |
| Restriction | — | — |
| Portability | — | Art. 27 PPIPS (machine-readable) |
| Objection | Cl. 4.3.8 | — |
| ADM/profiling | — | — (not stated in suite sources) |
| De-indexing | — | **Art. 28.1 PPIPS** (unique among these regimes; broader than GDPR erasure in some respects) |
| Opt-out-of-sale / limit-sensitive | — | — |

- **Response clock:** PIPEDA 30 days, reasonable extension with notice before expiry · Law 25 30 days + 10-day extension with notice (per `consent-language--rights-language.md`).
- Complaint routes: OPC (priv.gc.ca) · CAI (cai.gouv.qc.ca).

Tag: `PROCEDURAL` (rights handling is a workflow); access/portability scope shrinks with holdings (tagging rule 1).

## A7 — Retention & Erasure

- Cl. 4.5.3: PI no longer required "should be destroyed, erased, or made anonymous." ADD TTL and SEPARATE remediations directly address 4.5.3 (per `data-minimization--pipeda-gdpr.md`).

P-mapping: P4. Tag: `ARCH-SATISFIES` (automated TTL / crypto-erasure); `ARCH-DISSOLVES` for data held only in anonymized/aggregate form.

## A8 — Breach Notification

- `clock_model:` PIPEDA **promptness-standard** · Law 25 **fixed-clock** `[VERIFY]`.
- PIPEDA (ss. 10.1–10.3): report to OPC and notify individuals "as soon as feasible" where breach presents **real risk of significant harm (RROSH)**; factors: sensitivity, number affected, systemic nature (s. 10.1(3)).
- Law 25: **72 hours to CAI and to individuals** per `consent-language--breach-notification.md` and `data-minimization--regulatory-reference.md` (citing Art. 3.2 PPIPS); threshold: privacy incident with "serious injury" risk. `[VERIFY — suite files state a 72-hour clock; primary text may phrase the duty as "promptly/with diligence" — confirm against PPIPS before relying on the fixed clock]`
- Minimization linkage (sourced): less data → lower breach severity → lower reporting threshold.

Tag: duty once triggered `PROCEDURAL`; trigger surface `ARCH-DISSOLVES` under minimized/commitment-only holdings (the RROSH threshold is directly a function of what was held).

## A9 — Children

- **No statutory threshold.** OPC guidance: under 13, meaningful parental consent (per `consent-language--childrens-consent.md`).

Tag: `PROCEDURAL` (consent mechanism).

## A10 — Cross-Border Transfer

- `transfer_model:` PIPEDA **accountability** — transfers governed through the accountability principle (Cl. 4.1); organization remains responsible for PI transferred for processing. `[UNVERIFIED — the specific OPC transfer-for-processing guideline is not in suite sources; confirm against primary source]`
- Law 25 overlay: **Art. 17 PPIPS** — PI may not be communicated outside Quebec without adequate-protection assessment (data localization pressure).

P-mapping: P6. Tag: `PROCEDURAL` (assessment duty) + `ARCH-DISSOLVES` where processing is local-only or on data rendered non-personal before transfer (HE/MPC/DP per `privacy-architecture.md`).

## A11 — Security Safeguards

- Cl. 4.7; 4.7.1 safeguards appropriate to sensitivity; 4.7.3 methods must include physical, organizational, **and technical** measures. Specificity: principles-based.

P-mapping: **P7** (ENCRYPT/TOKENIZE are the technical-measure response, per `data-minimization--pipeda-gdpr.md`). Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA

- `dpia_model:` PIPEDA **none** statutory — OPC guidance recommends PIAs for significant new projects (sourced: `privacy-impact-assessment.md` regime table) · Law 25 **mandatory-triggered**.
- **Law 25 Art. 63.5 PPIPS:** PIA mandatory for any technology project involving PI that presents privacy risks. CAI trigger list (per `privacy-impact-assessment--dpia-triggers.md`): new/redesigned systems, new collection, new use, new third-party sharing, cross-border transfer, new tech incl. AI/ML, outsourcing, new retention/disposal processes, M&A, marketing projects.
- **Timing:** before implementation — retroactive PIA inadequate (CAI). **Update duty** on material change. **Consultation:** CAI consultation required before proceeding only if PIA identifies unmitigable high risk; otherwise keep on file, available on request.

Tag: `PROCEDURAL` — irreducibly documentary; but a selective-disclosure design *shrinks the PIA's risk register* (fewer assets, fewer flows), which is the architecture-to-paper bridge.

---

## Divergence Block — Law 25 vs PIPEDA (sourced summary)

Stricter on all counts: mandatory PIAs (63.5) · explicit opt-in for sensitive PI (Art. 12) · 72h breach clock `[VERIFY]` (vs "as soon as feasible") · portability (Art. 27) · de-indexing (Art. 28.1) · outside-Quebec transfer assessment (Art. 17) · CAD 25M / 4% penalties (Art. 90.1).
