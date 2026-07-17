# Sectoral Record: United States — HIPAA

| | |
|---|---|
| **Record** | `us-hipaa` · **Status:** SECTORAL-OVERLAY (S-profile v1.1) · **Current as of:** 2026-07-05 |
| **Instruments** | HIPAA, Pub. L. 104-191; 45 CFR Parts 160, 164 — Privacy Rule §§ 164.500–534 · Security Rule §§ 164.302–318 · Breach Rule §§ 164.400–414 (HITECH) |
| **Sources** | `skills/data-minimization/references/regulatory-reference.md` §HIPAA · `skills/consent-language/references/breach-notification.md` · `skills/privacy-impact-assessment/references/dpia-triggers.md` §HIPAA |

## S0 — Scope Trigger
**PHI × (covered entity ∪ business associate).** Covered entities: health plans, clearinghouses, providers transmitting PHI electronically (§ 160.103). BAs: vendors that create/receive/maintain/transmit PHI for a CE — BAA required (§ 164.308(b)). **Inferred health data is PHI** if held by a covered entity, regardless of source (`skills/data-minimization/SKILL.md` Step 2b rule 2).

## S1 — Enforcement
HHS OCR. Civil: $100–$50,000+ per violation, up to $1.9M per violation category per year (§ 160.404, adjusted annually). Criminal: up to 10 years for knowing misuse (42 U.S.C. § 1320d-6). Private right of action: none under HIPAA itself `[UNVERIFIED — standard characterization, not stated in suite sources]`.

## S2 — Obligation Spine
- **Minimum Necessary** (§ 164.502(b)) — limit PHI to the minimum needed for the purpose; internal-use policies § 164.514(d). *Not* applicable to: disclosures to the individual, to HHS, required-by-law, treatment communications.
- **De-identification paths** — Safe Harbor (§ 164.514(b)(2)): remove all 18 identifiers + no actual knowledge; Expert Determination (§ 164.514(b)(1)): documented very-small risk. Re-identification codes restricted (§ 164.514(c)).
- **Security Rule** — technical (§ 164.312: access control, audit, integrity, transmission encryption), administrative (§ 164.308: risk analysis/management, training), physical (§ 164.310).
- **Breach Rule** — unsecured-PHI breach triggers notification unless 4-factor assessment shows low compromise probability (§ 164.402(2)). Encryption per NIST + uncompromised key = safe harbor (not a reportable breach).

## S3 — Overlay Map (when S0 fires)
| Axis | Override |
|---|---|
| A3 | test becomes **minimum-necessary** — harder than necessity; per-disclosure scoping |
| A5 | the **18 PHI identifiers are all CRITICAL** regardless of omnibus tiering — incl. full IP (#15), all dates except year (#3, ages >89 aggregate to 90+), geographic subdivisions below state (#2, 3-digit ZIP rules) |
| A7 | de-identification (Safe Harbor / Expert Determination) becomes the sanctioned exit from scope — `ARCH-DISSOLVES` with a statutory recipe |
| A8 | clock becomes **60 days** (individuals § 164.404(b); HHS § 164.408; media if >500/state § 164.406); 4-factor trigger test; **encryption safe harbor defeats the trigger** (`ARCH-SATISFIES`) |
| A11 | prescriptive: encryption in transit required (§ 164.312(e)(1)); audit controls; unique user IDs |
| A12 | **risk-analysis-equivalent**: § 164.308(a)(1) risk analysis effectively mandatory — most-cited violation; must be ongoing and documented |

## S4 — Interactions
School health records are generally FERPA-covered, not HIPAA — except records held by a school health professional acting as a provider (sourced). Minimization reduces breach scope → lower 4-factor score → potentially below the notification threshold (sourced).

## S5 — Defined Lists
The **18 PHI identifiers** — full table with nuances: `skills/data-minimization/references/regulatory-reference.md` §HIPAA (canonical; not duplicated here per source-of-truth rule).

**Tags:** minimum-necessary `ARCH-DISSOLVES` · de-identification paths `ARCH-DISSOLVES` (statutory recipe) · encryption safe harbor `ARCH-SATISFIES` · breach duty once triggered, BAAs, training, risk-analysis paper `PROCEDURAL`.
