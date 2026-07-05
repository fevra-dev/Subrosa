# Guise Regulatory Normalization — Lessons

## Sectoral laws compose as overlays, not parallels — and they're where ARCH-MANDATES lives
The operator-approved S0–S5 profile models sectoral laws as modifiers on omnibus floors (S3 map), keeping floor/conflict derivations composable. Payoff was immediate: the profile surfaced two more ARCH-MANDATES instances (BIPA § 15(c) profit ban; COPPA's non-bypassable no-PI age gate) and the cleanest dissolution argument in the suite — BIPA's entire class-action exposure collapses under on-device biometric matching. Sectoral statutes, being single-purpose, state architectural requirements more directly than omnibus ones.

## The long tail strengthened the thesis instead of just widening coverage
Tier-3 was expected to be rote fan-out; instead it held the four strongest pro-architecture statutes in the whole set — AU APP 2 *mandates offering* anonymity, APPI's 仮名加工/匿名加工 ladder statutorily rewards the suite's own remediation vocabulary, KR PIPA makes P5/P6/crypto-erasure statutory (Arts. 3(7)/23/21), and DPDPA § 9's child-tracking ban is satisfiable only by architecture. Why it matters: the arch-rollup's claim ("architecture is the cheapest compliance program") gained direct statutory evidence — and the `ARCH-MANDATES` case (APP 2) exceeds the three-tag vocabulary, worth a tag-set note at the v1.1 bump. Also: strictness ≠ conflict — the Tier-3 scan moved six floors but added zero new register entries, only parties to C1/C3.

## Suite-internal citation doubts get flagged, never silently resolved
The suite states a 72-hour Law 25 breach clock in two files (citing "Art. 3.2 PPIPS"); the primary statute may phrase the duty as "promptly/with diligence." Also POPIA's regulator appears as "IOPA / IO" in one table but "Information Regulator (IR)" in the section text. Rule adopted: carry the sourced value with `[VERIFY — reason]`, keep the doubt visible. Silent correction breaks source-of-truth discipline; silent propagation launders a possible error into the canonical layer.

## Preserve existing P-mappings verbatim even where semantics look loose
`data-minimization--regulatory-reference.md` maps e.g. PIPEDA Cl. 4.9 (individual access) → P4, P6, which reads oddly against the strict P1–P7 definitions in `data-minimization.md` (P6 = Separation of Concerns). Design contract keeps the suite's mappings verbatim; reconciling mapping semantics is Phase-2 work (where the fix lands in the core with a log entry), not something to freelance during normalization.

## Enumerated field values are what made the schema survive three regime types
The axes generalize because each carries a typed enum (`basis_model`, `clock_model`, `sensitive_model`, `test_type`, `transfer_model`, `dpia_model`) instead of GDPR-shaped prose. CCPA's "no lawful basis at all" and PIPEDA's "no sensitive category list" become legal enum values, not special cases. Any future axis must ship with its enum or it will silently assume the GDPR shape.

## Sectoral laws are registered, not modeled
HIPAA/GLBA/COPPA/BIPA/FERPA/ePrivacy/NIS2/DORA/AI Act would need invented cells to fit the omnibus axes (no rights matrix, no omnibus basis model). Registered `SECTORAL` in the master; variant profile is a declared later-phase scope change, per the Phase-3 checkpoint.

## Tagging rule 1 prevents the cypherpunk tag from collapsing
Every obligation trivially dissolves for data never collected, so tags describe obligations for data the system *does* hold; the universal P1 dissolution is stated once in the master. Without this rule every cell reads ARCH-DISSOLVES and the tag carries zero information.

## No-source jurisdictions produce all-[UNVERIFIED] records by design
Malaysia PDPA has zero suite source. The record must say so in its header and tag every cell — a scaffold of flagged cells is the honest artifact; a clean-looking record would misrepresent verification status.

## Ground the orchestrator before fanning out — it's the fallback when subagents die
All 7 fan-out subagents failed instantly on a session limit. Recovery was cheap only because the orchestrator had already read every source section during Phase-1 grounding, so the Tier-2 scaffolds could be authored inline from held context with no re-reading. Pattern: do the grounding reads in the orchestrator *before* dispatching, even when delegation is the plan — parallelism then degrades to single-thread instead of to a stall.

## Grep presence-check is a usable verification floor when agent dispatch is unavailable
A fixed-string sweep of all concrete untagged values (63 penalty amounts, deadlines, section numbers) against the source files caught nothing loose: 61 PASS, 2 FAIL — and both FAILs were Malaysia cells already declared unsourced. This validates value *presence*, not context-match; the independent subagent verification pass is still owed (re-dispatch after the session-limit reset).

## The bidirectional conflict rule earned its keep on day one
Phase-2 reconciliation ran in BOTH directions immediately: `privacy-impact-assessment.md` held LGPD Art. 38 and Singapore PDPC-advisory facts the records had marked [UNVERIFIED] (subfile-wins → three record upgrades), while the same file's PIPL trigger row drifted from its own deeper reference (record-wins → subfile fixed). A one-directional "core always wins" rule would have destroyed real information; "records win unless the file is more specific — then fix the record" is the correct asymmetry.

## Session limits recur mid-phase — treat subagent fan-out as opportunistic, never load-bearing
The limit hit twice in one day (resets 2:40pm, then 7:50pm), killing 11 subagents total across both phases. The phase design that survives this: orchestrator grounds first, fans out opportunistically, and every subagent task must be inline-executable from held context. Standing debt: the independent context-match verification pass has now been deferred twice — run it as the first action of the next session.

## The [VERIFY] ledger is accumulating real Phase-2 reconciliation targets
Found during scaffolding, all flagged in-record rather than resolved: Law 25 72h breach clock (suite says fixed clock; primary may say "promptly/with diligence") · POPIA condition table's section numbering looks shifted vs the canonical Act (quality/openness/safeguards/participation) · POPIA regulator named "IOPA" in one table vs "Information Regulator" in section text · LGPD rights matrix maps both Access and Object to Art. 18(II). Phase 2's reconciliation step should work this ledger first.
