# Sectoral Record: EU — NIS2

| | |
|---|---|
| **Record** | `eu-nis2` · **Status:** SECTORAL-OVERLAY (S-profile v1.1) · **Current as of:** 2026-07-05 |
| **Instruments** | Directive (EU) 2022/2555 (repeals NIS1); transposition deadline Oct 17 2024 |
| **Sources** | `data-minimization--regulatory-reference.md` §NIS2 |

**Not a privacy law** (sourced) — a cybersecurity law that intersects privacy at logging, security measures, and board accountability. Registered here because its mandates are the counterparty in conflict **C2**.

## S0 — Scope Trigger
**Essential entities** (energy, transport, banking, FMI, health, water, digital infrastructure, ICT service mgmt, public admin, space) ∪ **important entities** (postal, waste, chemicals, food, manufacturing, digital providers, research) ∪ DNS/TLD/cloud/CDN/data centers/trust services (sourced lists).

## S1 — Enforcement
National competent authorities + CSIRTs. Penalties: essential — €10M or 2% global turnover; important — €7M or 1.4%. **Art. 20: management bodies personally liable; cybersecurity accountability cannot be delegated** — board-level exposure (feeds the A1 personal-liability floor note).

## S2 — Obligation Spine
- **Art. 23 incident reporting:** early warning **24h** → incident notification **72h** (assessment, severity, IoCs) → intermediate on request → final report **1 month**. "Significant incident" threshold (sourced).
- **Art. 21 minimum measures:** risk analysis, incident handling, business continuity, **supply-chain security**, secure development, effectiveness assessment, hygiene/training, **cryptography and encryption policies**, HR security/access control/asset management, **MFA (Art. 21(2)(j))**.

## S3 — Overlay Map (when S0 fires)
| Axis | Override |
|---|---|
| A8 | *incident* clocks (24h/72h/1mo) run parallel to GDPR's *PI-breach* clock — one event can trip both regimes on different triggers; pipeline must serve the tighter 24h early warning |
| A11 | prescriptive floor: MFA + crypto policies + supply-chain security mandated |
| A1 | personal board liability |
| A7 | security-log retention mandates → conflict **C2** party (tiered TTLs are the resolution) |

## S4 — Interactions
C2 (logging vs storage limitation). Supply-chain duty intersects the operator's MCP-server-vetting practice (sourced note). DORA is *lex specialis* for financial entities `[UNVERIFIED — the NIS2/DORA precedence rule is standard but not stated in suite sources]`.

## S5 — Defined Lists
Essential/important sector lists; Art. 21 measure list; Art. 23 report cadence.

**Tags:** measures (encryption, MFA) `ARCH-SATISFIES`; reporting cadence + board accountability `PROCEDURAL`; minimized PI in security telemetry keeps the NIS2-mandated logs out of GDPR trouble — the C2 resolution applied at design time.
