# Sectoral Record: EU — AI Act

| | |
|---|---|
| **Record** | `eu-ai-act` · **Status:** SECTORAL-OVERLAY (S-profile v1.1) · **Current as of:** 2026-07-05 |
| **Instruments** | Regulation (EU) 2024/1689; phased: prohibitions Feb 2 2025 · GPAI Aug 2 2025 · high-risk (Annex III) Aug 2 2026 |
| **Sources** | `data-minimization--regulatory-reference.md` §EU AI Act · `privacy-impact-assessment--dpia-triggers.md` §AI Act Art. 9 |

## S0 — Scope Trigger
**AI systems placed on the EU market or whose output is used in the EU** (extraterritorial, GDPR-scope logic — sourced). Tiers: prohibited practices (Art. 5) · high-risk (Annex III: biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, justice) · GPAI models (Art. 53; systemic-risk tier Art. 55 at >10²⁵ FLOPs).

## S1 — Enforcement
National market-surveillance authorities; European AI Office for GPAI. Penalties: €35M/7% (prohibited practices) · €15M/3% · €7.5M/1% (sourced).

## S2 — Obligation Spine
- **Art. 5 prohibitions** (privacy-relevant): real-time remote biometric ID in public by law enforcement (narrow exceptions); emotion recognition in workplace/education; **biometric categorization inferring sensitive attributes** — including *building the databases*.
- **Art. 10 data governance:** 10(2) provenance/bias/gap examination of training data; **10(3) training-data minimization** — the first statutory minimization duty aimed at training corpora; 10(5) narrow Art. 9-GDPR carve-out for bias auditing.
- **Art. 12 logging** (automatic operation logs) — conflict **C2** counterparty.
- **Art. 9 risk management:** iterative, lifecycle-long (functionally a rolling DPIA — sourced).
- **Art. 53 GPAI:** technical documentation, downstream info, **training-data summary (53(1)(d))**, EU copyright/TDM-opt-out compliance; Art. 55 adds adversarial testing + incident reporting for systemic-risk models.

## S3 — Overlay Map (when S0 fires)
| Axis | Override |
|---|---|
| A3 | minimization extends to **training corpora** (Art. 10(3)) — the suite's P1 applied to datasets, not just fields |
| A5 | Art. 5(1)(h): inferring sensitive attributes from biometrics is *prohibited conduct*, not consent-gated — a negative-form `ARCH-MANDATES`: the law bans the build |
| A12 | Art. 9 continuous risk management replaces point-in-time DPIA; layers onto GDPR Art. 35 where PI is processed |
| A7 | Art. 12 log-retention duty → **C2** (tiered TTLs on sensitive log fields — sourced resolution) |
| A6 | transparency to deployers (Art. 13); GPAI training-data summary is a disclosure duty about *datasets* |

## S4 — Interactions
Runs *alongside* GDPR, not instead of it (Art. 10(5) is the one explicit GDPR carve-out). Suite integration table sourced in `data-minimization--regulatory-reference.md` §AI Act × Privacy Suite. Derived/inferred-data rules (`data-minimization.md` Step 2b) are the operational bridge.

## S5 — Defined Lists
Annex III high-risk categories; Art. 5 prohibited-practice list; Art. 17-style classification n/a.

**Tags:** Art. 5 prohibitions are negative-form `ARCH-MANDATES` (compliance = not building the capability); Art. 10(3) `ARCH-DISSOLVES`-aligned (synthetic/DP training data is the strongest satisfaction — see reg-ref §Synthetic Data); Arts. 9/12/13/53 documentation `PROCEDURAL`.
