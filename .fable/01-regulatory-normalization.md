# Fable 5 Prompt — Phase 1: Regulatory Taxonomy Normalization

**Target:** fresh Claude Fable 5 session (`claude-fable-5`), working dir `/Users/fevra/Apps/Guise`.
**Effort:** xhigh for Phase-1 taxonomy design, high for Phase-2 fan-out (stated inline).
**Output:** a normalized regulatory-mapping layer the prose skills cite; Tier-1 full, Tier-2 scaffolded, long-tail stubbed.
**Framing:** zero offensive surface — pure legal/compliance cross-referencing. No classifier risk.

Paste everything below the line.

---

I'm building **Guise**, a privacy-compliance skill suite (a bundle of Claude Code
skills) that pairs statute-level regulatory mapping with a cypherpunk architecture
layer. The thesis, stated in privacy-suite.md, is *compliance is a floor, selective
disclosure is the ceiling*. The suite already has deep, statute-precise content
across many regimes — but each jurisdiction was written as standalone prose, so it
doesn't scale: adding a country means re-deriving structure from scratch, and
cross-jurisdiction questions ("who has a 72-hour breach clock?", "which regimes
treat precise geolocation as sensitive?") have no single structure to resolve
against. I need the regulatory layer normalized so adding a jurisdiction is filling
a template, and so the suite can eventually reach every major regime in tiers
without the content drifting out of sync.

Working directory: /Users/fevra/Apps/Guise. Treat the existing *.md files as
authoritative source-of-truth to normalize and extend — do NOT discard their
statutory precision or rebuild from zero.

GOAL — a correct, complete result is:
1. A single **normalized taxonomy**: the shared axis set every jurisdiction is
   described against, authored once and proven to generalize before anything fans
   out.
2. Every **Tier-1 jurisdiction** fully populated against that taxonomy, reconciled
   with the existing prose files.
3. **Tier-2 jurisdictions** scaffolded to a defined depth.
4. **Long-tail** left as clearly-marked template stubs.
5. The cypherpunk framing preserved and extended: tag each regime's obligations for
   whether they're satisfiable *structurally* (architecture) or only *procedurally*
   (policy), tying the compliance layer back to privacy-architecture.md. This is the
   "plus cypherpunk" — not compliance theater, but compliance mapped against the
   architecture that makes the obligation moot.

TIERS:
- Tier 1 (do fully): PIPEDA + Quebec Law 25 — home jurisdiction, nail this first —
  then GDPR + UK-GDPR, then CCPA/CPRA.
- Tier 2 (scaffold): LGPD, POPIA, PIPL, PDPA family (Singapore, Malaysia, Thailand).
- Long tail (normalized stubs only): everything else (APPI, DPDPA, Australia APPs,
  and beyond) — several already have partial content; leave them as template stubs.

RECOMMENDED TAXONOMY AXES — already implied by the existing files; refine if you
find a cleaner cut, but freeze it before fan-out: enforcement authority + penalty
ceiling · collection-limitation / minimization hook · purpose limitation · lawful
basis + consent model (opt-in vs opt-out, sensitive-data carve-outs) · sensitive-
category definition + trigger · data-subject rights matrix · retention / erasure ·
breach notification (authority, timeline, threshold) · children's age threshold +
consent mechanism · cross-border transfer mechanism · security-safeguards mandate ·
DPIA/PIA trigger. Map every cell to a statutory citation and to the suite's
minimization principles P1–P7.

SEQUENCING (hard constraint — this is the "build the mapping logic once" part):
- Phase 1: design the taxonomy and author it fully for PIPEDA/Law 25, GDPR, and
  CCPA/CPRA. It must accommodate a civil-law necessity regime, a common-law
  reasonableness regime, and a US sectoral/proportionality regime without special-
  casing any of them. Freeze it. Do not fan out until the schema has survived all
  three.
- Phase 2: fan out the Tier-1 finish + Tier-2 scaffold across subagents, one
  jurisdiction per subagent, each filling the frozen template. Hold the canonical
  taxonomy yourself and reconcile every returned record against it — a subagent's
  summary is a pointer, re-read its output before merging.

CORRECTNESS (this is a legal-citation artifact — a wrong citation is worse than a
missing one): every statutory citation must be verifiable against the existing
reference files or flagged `[UNVERIFIED — confirm against primary source]`. Never
invent an article/section number to fill a cell; an empty cell marked "not located"
is correct, a fabricated citation is a defect. Preserve the "current as of [date]"
hygiene and the not-legal-advice framing already in the files.

WORKING METHOD:
- Effort: run Phase-1 taxonomy design at xhigh; run the Phase-2 fan-out at high.
- Delegate independent per-jurisdiction subtasks to subagents and keep working while
  they run; intervene if one drifts from the frozen template or lacks context.
- Every ~4 jurisdictions, verify your work with a subagent against the frozen
  taxonomy and the citation rule.
- Keep lessons in /Users/fevra/Apps/Guise/.fable/lessons.md: one lesson per section,
  a one-line summary at top, corrections and confirmed approaches alike with why
  they mattered. Update an existing note rather than duplicating.

REPORTING / PACE: when you have enough to act, act — don't narrate options you won't
pursue or re-derive settled facts. Lead with the outcome: the first sentence when
you finish a phase says what got built and what's left. Pause for me only on a real
scope change (e.g., the taxonomy needs an axis that reshapes Tier-1 output) or a
decision only I can make — otherwise proceed through the tiers and report at phase
boundaries.
