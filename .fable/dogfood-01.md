# Dogfood 01 — end-to-end consistency test of the propagated suite

**Date:** 2026-07-04 · **Gate:** Phase-2 "dogfood before done" · **Method:** run the suite's skills against one sample input and check that every statutory claim each skill would emit resolves to the same taxonomy-record anchor.

## Sample input

> "Solana delegation-analytics dashboard. Email login; tracks wallet addresses; logs full IP for fraud detection; session analytics. Users in EU, Canada (incl. Quebec), and California. Considering publishing delegation attestations on-chain."

## Routing (privacy-suite.md)

Pattern 1/3 hybrid → `data-minimization` (schema) → `privacy-impact-assessment` (new tech project) → `consent-language` (launch disclosure); `regulatory-taxonomy--conflicts.md` C1 flagged immediately by the on-chain intent. Routing references resolved: PASS (router now names the taxonomy layer).

## Cross-skill consistency matrix

| Claim | data-minimization would cite | consent-language would cite | PIA would cite | Record anchor | Agree? |
|---|---|---|---|---|---|
| Minimization test | GDPR 5(1)(c) · PIPEDA 4.4.1 · CCPA 100(a)(3) | (disclosure of purposes) | necessity check Phase 1 | A3 of all three Tier-1 records; floor A3 | ✅ |
| Full IP retention | P3 TRUNCATE or exception record | notice: "IP truncated to /24" (Template 1) | risk register entry | A3/A11 + conflict C6 (same resolution both sides) | ✅ |
| Wallet ↔ email linkage | P5 scope-reduce; on-chain escalation CRITICAL | blockchain caveat clause (rights-language) | Art. 17-conflict documentation | conflict C1; `eu-gdpr-uk` A7 immutability note | ✅ |
| Breach clocks | — | 72h GDPR Art. 33; Law 25 72h† | incident-response section | A8 `eu-gdpr-uk` + `ca-pipeda-law25`; floor A8 — **[VERIFY]† carried identically in all three places** | ✅ |
| Rights set | — | union incl. de-indexing (Law 25 Art. 28.1), opt-out-of-sale + limit-sensitive (CCPA), restriction (GDPR 18) | rights assessment | A6 of all three records; floor A6 | ✅ |
| Response clock | — | 30 days CA / 1 month GDPR / 45 days CCPA | — | A6; floor: 30-day design floor | ✅ |
| GPC | — | honor as binding CA opt-out (tit. 11 § 7026); EU withdrawal-valid (EDPB 8/2024) | — | `us-ca-ccpa` A2 + `eu-gdpr-uk` divergence block | ✅ |
| PIA duty | — | Law 25 PIA statement clause | **mandatory** — Law 25 63.5 (new tech project + new collection + cross-border) AND EDPB two-of-nine (innovative tech + dataset matching = 2) | A12 `ca-pipeda-law25` + `eu-gdpr-uk`; floor A12 | ✅ |
| On-chain PII | escalate all findings CRITICAL; hash/commit only | blockchain immutability caveat | immutability-conflict documentation | C1 resolution identical in all three consumers | ✅ |

## Verdict

**PASS.** No divergent citations found across the four skill families; the two known `[VERIFY]` flags (Law 25 clock; LGPD objection anchor — not exercised by this sample) propagate *with* their flags rather than silently as facts, which is the designed behavior. One residual noted: the sample never touches Tier-2 records, so their consistency is asserted by construction (built from the same sources), not exercised — a Brazil/China-flavored dogfood is the natural test when Tier-2 promotes to FULL.
