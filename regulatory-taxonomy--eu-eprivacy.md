# Sectoral Record: EU — ePrivacy Directive

| | |
|---|---|
| **Record** | `eu-eprivacy` · **Status:** SECTORAL-OVERLAY (S-profile v1.1) · **Current as of:** 2026-07-05 |
| **Instruments** | Directive 2002/58/EC, amended by 2009/136/EC; implemented via member-state law (UK: PECR 2003; DE: TKG 2021) |
| **Sources** | `data-minimization--regulatory-reference.md` §ePrivacy · `consent-language--cookie-consent.md` |
| **Reform watch** | ePrivacy Regulation (COM/2017/10) stalled since 2017; the Directive remains operative — monitor (sourced) |

**Structural position (sourced):** *lex specialis* to GDPR — where ePrivacy applies, **GDPR legal bases do not substitute** for ePrivacy consent. The source of the cookie-wall and consent-or-pay debates.

## S0 — Scope Trigger
**(a) Storage of or access to information on terminal equipment** — cookies, localStorage, IndexedDB, pixels, link decoration, canvas/audio fingerprinting, any device read/write (sourced breadth) — **∪ (b) processing in the electronic-communications sector** (traffic, location data). EU-facing services regardless of establishment.

## S1 — Enforcement
National DPAs under member-state implementations (CNIL the strictest — sourced: equal-prominence reject, 13-month consent validity; DSK, AEPD, Garante, ICO/PECR positions per `consent-language--cookie-consent.md`).

## S2 — Obligation Spine
- **Art. 5(3):** prior, informed GDPR-quality consent (Art. 4(11)) before terminal-equipment storage/access. Exempt: strictly-necessary only (session auth, load balancing, cart, consent storage) — analytics/ads/A-B/social plugins are **not** exempt even first-party.
- **Art. 6 traffic data:** processable only for transmission billing, interconnection, fraud detection, network management; erase/anonymize after — **not usable for analytics or advertising without consent**.
- **Art. 9 location data:** consent per value-added service; per-session withdrawal.
- **Art. 13 unsolicited communications:** prior consent for email/SMS/automated marketing; soft opt-in for existing customers + similar products + easy opt-out.

## S3 — Overlay Map (when S0 fires)
| Axis | Override |
|---|---|
| A2 | consent-before-fire replaces every other basis for terminal access; GPC valid for withdrawal (EDPB Op. 8/2024), not initial consent |
| A4 | Art. 6 purpose list for traffic data is *closed* — statutory purpose limitation |
| A3 | strictly-necessary exemption is a necessity test applied per-cookie |
| A7 | traffic-data erase/anonymize-when-done duty |

## S4 — Interactions
Sits over GDPR (consent definition imported from Art. 4(11)); UK fork via PECR; anti-pattern refusal list (pre-ticks, cookie walls, "by continuing") per Planet49 C-673/17 and `consent-language--cookie-consent.md`.

## S5 — Defined Lists
Consent-exempt cookie classes; traffic-data permitted-purpose list; the non-compliant-pattern table (cookie-consent file — canonical).

**Tags:** truly-anonymous analytics (Recital-26-grade) `ARCH-DISSOLVES` the Art. 5(3) consent duty — the only exit that isn't a banner; consent plumbing + GPC handling `PROCEDURAL`/`ARCH-SATISFIES`.
