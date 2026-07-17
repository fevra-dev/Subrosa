# Cross-Regime Conflict Register

**Derived 2026-07-04 from schema v1.0 records + suite prose.** Obligations that are mutually incompatible — or in structural tension — across regimes. Each entry: the colliding obligations, why they collide, the suite's recommended resolution, residual risk, and the enforcement-mode reading (which side architecture dissolves). Not legal advice.

---

## C1 — Erasure rights vs immutable storage
**Collides:** GDPR Art. 17 / Law 25 Art. 28 PPIPS / LGPD Art. 18(VI) / PIPL Art. 47 (erasure) / **KR PIPA Art. 21 (destruction must be *irreversible* — the sharpest form of the duty)** ↔ any append-only or public-chain design.
**Mechanism:** the statutes assume deletion is physically possible; a public ledger makes it impossible post-write. The suite's canonical collision between privacy-by-architecture and privacy-by-policy (`skills/privacy-suite/SKILL.md` §Blockchain Continuity).
**Resolution (sourced):** personal data fully off-chain; only content-addressed commitments on-chain; where on-chain payloads are unavoidable, encrypt-before-write and treat key destruction as practical erasure; the suite's blockchain caveat clause (`skills/consent-language/references/rights-language.md`) discloses the residue.
**Residual risk:** encryption-as-erasure is not settled law (EDPB Guidelines 05/2019 acknowledge without resolving); consult the competent DPA before relying on it in a regulated context.
**Arch reading:** `ARCH-DISSOLVES` — PII that never touches the chain never conflicts.

## C2 — Mandated security logging vs storage limitation
**Collides:** EU AI Act Art. 12 (high-risk AI operation logs) / NIS2 Arts. 21, 23 / DORA Arts. 10, 17 / GLBA audit-trail duties ↔ GDPR Art. 5(1)(e) / PIPEDA Cl. 4.5.3 (don't retain).
**Mechanism:** one regime mandates retention the other mandates minimizing — both apply to the same log line.
**Resolution (sourced):** tiered retention (hot/warm/cold) with sensitivity-graded TTLs on log *fields*, pseudonymized identity fields in logs, and a documented MINIMIZATION EXCEPTION RECORD per retained high-fidelity field (`skills/data-minimization/references/regulatory-reference.md` template).
**Residual risk:** TTL choices are judgment calls a regulator can second-guess; the exception record is the defense.
**Arch reading:** `ARCH-SATISFIES` — the conflict is dissolved at field granularity, not log granularity.

## C3 — Localization regimes vs global service architecture and portability
**Collides:** PIPL Arts. 38–43 (CAC assessment/contract/certification; Art. 43 reciprocity) + **VN PDPL 91/2025 (DPIA + Transfer Impact Assessment dossiers filed with A05; 5%-of-revenue penalty tier — note: the PDPL text reviewed carries no localization mandate; Vietnam's separate Cybersecurity Law/Decree 53 regime may still, `[UNVERIFIED]`)** ↔ GDPR Art. 20 portability, global processing topologies, Law 25 Art. 17 outbound assessments.
**Mechanism:** data that lawfully cannot leave the territory cannot be ported, replicated, or centrally processed; PIPL volume thresholds (1M+ individuals; 100k+/10k+ sensitive) trip mandatory CAC assessment; Vietnam adds a hard storage-location mandate.
**Resolution:** regional data residency; collect-locally-process-locally; and the sourced design rule — *if you cannot lawfully transfer it, don't collect it*.
**Residual risk:** CAC discretion and reciprocity countermeasures are policy-driven and can shift without statutory change.
**Arch reading:** `ARCH-DISSOLVES` under local-only/edge processing; PSI/MPC/HE let global functions run without the data crossing (`skills/privacy-architecture/SKILL.md`).

## C4 — Quebec outbound-communication assessment vs cloud defaults
**Collides:** Law 25 Art. 17 PPIPS (adequate-protection assessment before PI leaves Quebec) ↔ default SaaS/cloud topologies that replicate freely.
**Resolution:** flow inventory + per-provider assessment + contractual safeguards + minimization of what flows; regional hosting where feasible.
**Residual risk:** the assessment standard is judgment-based; CAI expectations are still forming.
**Arch reading:** `ARCH-DISSOLVES` for data that never leaves or is non-personal before it does.

## C5 — Children's verification paradox: VPC vs minimization
**Collides:** COPPA 16 CFR § 312.5(b) verifiable-parental-consent methods (government ID check, credit card, face-match) ↔ P1/collection-limitation in every regime — *verifying the parent requires collecting more data than the service itself*.
**Resolution (sourced + architectural):** ephemeral verification — the sourced VPC method is "check photo ID **+ delete afterward**"; verify, don't retain. Architectural end-state: ZKP age/guardianship predicate proofs (`skills/privacy-architecture/SKILL.md`) — prove "parent of user, over 18" with zero documents retained.
**Residual risk:** ZKP-based VPC is not yet an FTC-approved method (the 2023 face-match proposal shows the direction); until then, deletion discipline is the control.
**Arch reading:** the flagship `ARCH-DISSOLVES` use case for anonymous credentials.

## C6 — Detection fidelity vs minimization
**Collides:** fraud/intrusion detection needing full-fidelity identifiers (full IP, device IDs) ↔ P1/P3 minimization hooks in every regime (GDPR 5(1)(c), PIPEDA 4.4.1, CCPA 100(a)(3)).
**Resolution (sourced):** documented, justified exception with compensating controls — the suite's MINIMIZATION EXCEPTION RECORD (role-scoped access, no analytics replication, hard TTL, encryption, pseudonymized reporting). Undocumented exceptions are violations; documented ones are defensible.
**Residual risk:** the retained identifier remains a breach asset for its TTL window.
**Arch reading:** partial — HMAC/tokenized equality checks (`P7`) shrink the retained surface where detection needs matching, not raw values.

## C7 — Erasure rights vs statutory retention duties *(resolved-by-design exemplar)*
**Collides:** GDPR Art. 17 / CCPA § 1798.105 (delete on request) ↔ financial/tax/AML record-keeping mandates.
**Resolution:** already built into the statutes — Art. 17(3)(b) exception, CCPA deletion exceptions; restrict processing to what the exception permits and disclose the exception in the notice (`skills/consent-language/references/rights-language.md` retention-exceptions clause).
**Residual risk:** minimal in one jurisdiction; edge cases where jurisdiction A mandates retention of what jurisdiction B orders erased — segregate holdings per legal basis so the conflict never shares a record.
**Arch reading:** `SEPARATE` (P6) is the control: retention-mandated data lives apart from erasable data.

---

**Register rule:** new records must be checked against C1–C7 and may add entries; a new regime that moves a floor in `regulatory-taxonomy--floor.md` is also a conflict-register review trigger.

**Tier-3 scan (2026-07-04):** eight regimes checked (AU, JP, IN, CH, KR, AE, NG, VN). No new *mutual incompatibilities* found; two entries gained parties — C1 (+KR Art. 21 irreversible destruction) and C3 (+VN Art. 26 localization). Honest note: the scan added obligations that are *stricter*, not *conflicting* — strictness moves the floor, not the register.
