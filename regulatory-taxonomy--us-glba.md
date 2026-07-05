# Sectoral Record: United States — GLBA / FTC Safeguards Rule

| | |
|---|---|
| **Record** | `us-glba` · **Status:** SECTORAL-OVERLAY (S-profile v1.1) · **Current as of:** 2026-07-05 |
| **Instruments** | GLBA, 15 U.S.C. §§ 6801–6809 · FTC Safeguards Rule, 16 CFR Part 314 (revised Dec 2021, enforcement June 9 2023) · FTC Privacy Rule, 16 CFR Part 313 |
| **Sources** | `data-minimization--regulatory-reference.md` §GLBA |

## S0 — Scope Trigger
**NPI × financial institution (FTC jurisdiction).** Non-bank entities significantly engaged in financial activities: mortgage brokers, payday lenders, tax preparers, auto dealers, credit counselors, debt collectors, non-SEC investment advisers. **Web3 note (sourced):** FTC has signaled crypto exchanges, DeFi platforms, and NFT marketplaces handling financial data may fall in scope — verify current guidance. Customer (ongoing relationship) > consumer (one-time) protections.

## S1 — Enforcement
FTC (15 U.S.C. § 6805); state AGs may also enforce. Civil penalties to $100,000 per violation; individuals to $10,000 + imprisonment. No private right of action `[UNVERIFIED — standard characterization, not stated in suite sources]`.

## S2 — Obligation Spine (§ 314.4 — the most prescriptive US security regulation outside HIPAA)
Qualified individual (a) · written risk assessment (b) · access controls (c)(1) · **data inventory (c)(2)** — know what customer information you hold and where (closest US analog to GDPR Art. 30) · **encryption at rest and in transit (c)(5)**, no low-sensitivity carve-out · **MFA for anyone accessing customer information (c)(6)** · **secure disposal within 2 years of last use (c)(8)** · change management (c)(9) · annual penetration test + semiannual vuln assessments (d)(2) · service-provider oversight (f) · written IR plan (h) · annual board reporting (i). Small-entity exception: <5,000 customer records exempts pen-testing/audit-trail items only (§ 314.6). Privacy Rule: initial/annual notices + opt-out before NPI sharing with nonaffiliated third parties; NPI defined § 313.3(n).

## S3 — Overlay Map (when S0 fires)
| Axis | Override |
|---|---|
| A2 | notice-and-**opt-out** model for NPI sharing (initial + annual notices) |
| A7 | **2-year disposal deadline** (c)(8) — the most specific retention mandate in US law; schemas need `last_used_date` + enforcement job |
| A11 | prescriptive floor: encryption (c)(5) + MFA (c)(6) mandatory — `ARCH-SATISFIES` obligations stated as rules |
| A12 | written risk assessment (b) + annual board reporting (i) |
| A0/A1 | inventory duty (c)(2) — you cannot minimize what you haven't inventoried (sourced); pen-test cadence (d)(2) |

## S4 — Interactions
Overlays state omnibus laws (CCPA) where the entity is both a business and a financial institution — GLBA-covered data is generally CCPA-exempt `[UNVERIFIED — Cal. Civ. Code § 1798.145(e) GLBA exemption; not in suite sources]`.

## S5 — Defined Lists
**NPI** (§ 313.3(n)): personally identifiable financial information not publicly available — balances, transaction history, credit scores, payment history, application data.

**Tags:** encryption/MFA/disposal `ARCH-SATISFIES` (prescriptive form) · inventory, risk assessment, notices, board reporting, SP oversight `PROCEDURAL` · minimized holdings shrink the (c)(2) inventory and the disposal surface — the P1 dissolution applies upstream as always.
