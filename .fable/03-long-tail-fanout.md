# Fable 5 Prompt — Phase 3: Long-Tail Jurisdiction Fan-Out

**Target:** fresh Claude Fable 5 session (`claude-fable-5`), working dir `/Users/fevra/Apps/Guise`.
**Prerequisite:** Phase 1 (`01`) frozen taxonomy exists; Phase 2 (`02`) derived artifacts exist (strictest-wins matrix, conflict register, architecture-vs-policy roll-up).
**Effort:** high.
**What makes this more than a tier-swap of `01`:** each new jurisdiction must fold into the Phase-2 derived artifacts too — a stricter regime can move the "design-to-this" floor, and can add conflict-register entries. So this isn't just appending records; it's extending records *and* re-deriving the artifacts that consume them. It also surfaces one genuine modeling question the omnibus-designed taxonomy hasn't been tested against: sectoral/state laws (see below).

Paste everything below the line.

---

I'm continuing work on **Guise**, my privacy-compliance skill suite. Phases 1–2 gave
me a frozen regulatory taxonomy with Tier-1/Tier-2 populated, the downstream skills
wired to consume it, and three derived artifacts: a strictest-regime-wins default
matrix, a cross-regime conflict register, and an architecture-vs-policy roll-up. This
phase extends coverage across the long tail of regimes — and folds each new
jurisdiction into those derived artifacts, not just into the reference.

Working directory: /Users/fevra/Apps/Guise. Read the frozen taxonomy, the three
Phase-2 artifacts, and /Users/fevra/Apps/Guise/.fable/lessons.md first. The taxonomy
is frozen source-of-truth; do not redesign it (see the sectoral exception below).

GOAL — a correct, complete result is:
1. Long-tail jurisdictions populated against the frozen taxonomy, at the tier depth
   below.
2. The strictest-wins default matrix re-derived: if a newly-added regime sets a
   stricter floor on any axis (a shorter breach clock, a lower children's threshold,
   a harder cross-border bar), the matrix moves and the citation updates.
3. The conflict register extended with any new mutual incompatibilities the added
   regimes introduce.
4. The architecture-vs-policy roll-up extended: tag each new regime's obligations
   structural vs procedural, same as Tier-1.

LONG-TAIL TIERS (bound the run — "every country" is not one session):
- Tier 3a (do fully): the regimes already partially present in the reference —
  normalize them into the frozen taxonomy — Australia APPs, APPI (Japan), DPDPA
  (India), plus the US sectoral/state laws already drafted (HIPAA, GLBA, COPPA, BIPA).
- Tier 3b (scaffold): additional national omnibus laws not yet present — e.g.
  Switzerland (nFADP), South Korea (PIPA), UAE (PDPL), Saudi Arabia (PDPL), Nigeria
  (NDPA), Kenya (DPA), Indonesia (PDP Law), Vietnam (PDPD). Confirm each is worth
  including before drafting; skip any you can't source.
- Tier 3c (stubs only): the remaining long tail — normalized template stubs, clearly
  marked, so a later run fills them.

SECTORAL / STATE-LAW EXCEPTION (the one place the frozen taxonomy may not fit):
The taxonomy was designed for omnibus data-protection regimes. HIPAA, GLBA, COPPA,
and BIPA are sectoral or single-purpose — they don't have, e.g., a general
data-subject-rights matrix or an omnibus lawful-basis model. Do NOT force them into
the omnibus shape by inventing cells. If they need a variant record type (a sectoral
profile: scope trigger, covered entities, the axes that apply, N/A on the rest),
that is a real taxonomy change — pause and flag it to me with your proposed shape
rather than special-casing silently. This is the one scope-change checkpoint in this
phase.

CORRECTNESS (legal-citation artifact — a wrong citation is worse than a missing one):
every citation verifiable against a source or flagged
`[UNVERIFIED — confirm against primary source]`. Never invent an article/section
number; an empty cell marked "not located" is correct, a fabricated citation is a
defect. These newer/less-familiar regimes are exactly where fabrication risk is
highest — hold the line. Preserve "current as of [date]" hygiene and the
not-legal-advice framing.

WORKING METHOD:
- Fan out one jurisdiction per subagent, each filling the frozen template; hold the
  canonical taxonomy and derived artifacts yourself and reconcile every returned
  record before merging — a subagent's summary is a pointer, re-read its output.
- Re-derive the strictest-wins matrix and conflict register only after a batch is
  merged and reconciled (they're only correct against the consistent state).
- Every ~4 jurisdictions, verify with a subagent against the taxonomy and the
  citation rule.
- Append lessons to /Users/fevra/Apps/Guise/.fable/lessons.md — one per section,
  one-line summary at top, why it mattered. Update existing notes, don't duplicate.

REPORTING / PACE: when you have enough to act, act — don't narrate options you won't
pursue or re-derive settled facts. Lead with the outcome: your first sentence when a
batch finishes says which regimes landed and whether the default matrix moved. Pause
for me only on the sectoral scope-change checkpoint above, or a decision only I can
make — otherwise proceed through the tiers and report at batch boundaries.
