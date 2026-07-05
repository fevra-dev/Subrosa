# Fable 5 Prompt — Phase 2: Suite Integration & Cross-Regime Derivation

**Target:** fresh Claude Fable 5 session (`claude-fable-5`), working dir `/Users/fevra/Apps/Guise`.
**Prerequisite:** Phase 1 (`01-regulatory-normalization.md`) is done — the frozen taxonomy exists and Tier-1 is populated.
**Effort:** high.
**Why this is the next phase, not the long tail:** the long-tail fan-out is just Phase 1 again with the tier list changed — low marginal value to run as its own phase. The phase that makes normalization *pay off* is wiring the downstream generative skills to consume one source of truth, and deriving the cross-regime artifacts (strictest-wins defaults, conflict register, architecture-vs-policy roll-up) that a normalized mapping makes possible. That's where the suite becomes one system instead of a stack of files — and where the cypherpunk payoff lands.

Paste everything below the line.

---

I'm continuing work on **Guise**, my privacy-compliance skill suite. Phase 1
produced a normalized regulatory taxonomy (the frozen axis set) with Tier-1
jurisdictions fully populated. Right now that mapping is a reference nobody consumes:
the generative skills — consent-language (and its notice/cookie/children/breach/
rights sub-files), data-minimization (and its sub-files), privacy-impact-assessment,
threat-model-privacy — still carry their own embedded, independently-authored
citations, which is exactly the drift the normalization was meant to kill. I need
those skills rewired to derive from the frozen taxonomy, plus the cross-regime
artifacts the mapping now makes possible. The point of the suite is that a citation
is fixed once and propagates, and that "compliance is a floor, selective disclosure
is the ceiling" is enforced, not just asserted.

Working directory: /Users/fevra/Apps/Guise. Read the frozen taxonomy and Phase-1
output first — it is the source of truth this phase consumes. Also read
/Users/fevra/Apps/Guise/.fable/lessons.md before starting.

GOAL — a correct, complete result is:

1. **Single source of truth (propagation).** The downstream generative skills
   reference the frozen taxonomy for every statutory citation and every jurisdiction
   fact, rather than restating them. Where a sub-file's citation disagrees with the
   core, reconcile — but see the correctness rule: do not blindly overwrite.

2. **Strictest-regime-wins default matrix.** A "design-to-this" floor derived across
   Tier-1 (extensible to later tiers): for each taxonomy axis, the single most
   demanding requirement across regimes (e.g., 72-hour breach clock, opt-in for
   sensitive categories, PIA-mandatory, honor GPC). A product built to this matrix is
   compliant everywhere in scope by construction. Cite which regime sets each floor.

3. **Cross-regime conflict register.** Obligations that are mutually incompatible
   across regimes, systematized — the suite already names several in prose (Art. 17
   erasure vs blockchain immutability; EU AI Act Art. 12 logging vs GDPR storage
   limitation; PIPL data-localization vs portability). Each entry: the two
   obligations, the regimes, why they collide, and the suite's recommended resolution
   with its residual-risk note.

4. **Architecture-vs-policy roll-up (the cypherpunk payoff).** From the per-obligation
   structural/procedural tags applied in Phase 1, produce the summary view: which
   obligations *dissolve* under a selective-disclosure architecture (data never
   collected can't be breached, erased, or unlawfully transferred) versus which are
   irreducibly procedural. This is the bridge from the compliance layer to
   privacy-architecture.md — make the "compliance is a floor" thesis operational.

SEQUENCING:
- Start with propagation on the ONE richest downstream skill (consent-language) end
  to end, so the wiring pattern is proven before it fans out. Freeze the pattern.
- Then fan the propagation across the remaining downstream skills via subagents, one
  skill per subagent, each applying the frozen wiring pattern. Hold the canonical
  taxonomy yourself; a subagent's summary is a pointer — re-read its diff before
  merging.
- Derive artifacts 2–4 last, from the reconciled, propagated state (they're only
  correct once the citations are consistent).

CORRECTNESS (legal-citation artifact — a wrong citation is worse than a missing one):
- On drift between a sub-file and the core, do NOT silently overwrite the sub-file to
  match the core. Diff them. If the sub-file's citation is more specific or more
  correct, fix the CORE and log it — the sub-files were authored with real statutory
  care and may be right where the core is thin. Every reconciliation gets a one-line
  log entry (which won, why).
- Never invent a citation to resolve a conflict. Unresolved → mark
  `[UNVERIFIED — confirm against primary source]`.
- Preserve the "current as of [date]" hygiene and the not-legal-advice framing.

DOGFOOD BEFORE DONE: before declaring the phase complete, run the suite end to end on
a sample input — a short product/schema description — and confirm that routing, the
generated privacy notice, the data-minimization findings, and the applicable rights
language all cite the frozen taxonomy consistently and agree with each other. If they
diverge, the propagation isn't done. Report the test and its result.

WORKING METHOD:
- Delegate independent per-skill propagation to subagents and keep working while they
  run; intervene if one drifts from the frozen wiring pattern.
- Every few skills, verify with a subagent against the taxonomy and the reconciliation
  log.
- Append lessons to /Users/fevra/Apps/Guise/.fable/lessons.md — one per section,
  one-line summary at top, why it mattered. Update existing notes rather than
  duplicating.

REPORTING / PACE: when you have enough to act, act — don't narrate options you won't
pursue or re-derive settled facts. Lead with the outcome: your first sentence when a
step finishes says what changed and what's left. Pause for me only on a real scope
change (e.g., a reconciliation reveals the frozen taxonomy needs a structural fix that
reshapes Tier-1) or a decision only I can make — otherwise proceed and report at step
boundaries.
