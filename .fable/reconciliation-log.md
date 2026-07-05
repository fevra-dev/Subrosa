# Reconciliation Log — taxonomy ↔ downstream skills

## 2026-07-05 — [VERIFY] ledger resolved by primary-source web research (6/6)

Five genuine suite errors + one supersession, all corrected across records, prose files, master, floor, and conflicts:

1. **Law 25 breach clock — SUITE WAS WRONG.** No 72-hour clock exists; the standard is *prompt* notification to CAI/individuals + a mandatory all-incident register. Corrected in `ca-pipeda-law25` A8, breach-notification table, reg-ref, pipeda-gdpr, master quick index, floor A8 (GDPR Art. 33 now the sole fixed-clock floor-setter). Sources: Gowling WLG, OneTrust, Termly, CFIB analyses of Law 25 s. 3.5.
2. **POPIA condition numbering — SUITE WAS WRONG (whole table shifted).** Canonical: processing limitation ss. 9–12 (minimality s. 10), purpose spec ss. 13–14, further processing s. 15, quality s. 16, openness ss. 17–18, safeguards ss. 19–22 (breach s. 22), participation ss. 23–25. Record rewritten; reg-ref table + minimization-framework paragraph corrected. Sources: gov.za Act text, popia.co.za.
3. **LGPD objection anchor — SUITE WAS WRONG.** Objection = **Art. 18 § 2**, not Art. 18(II) (that's access). Also gained Art. 18(IV) (deletion of *excessive* data — a statutory minimization right). Corrected in `br-lgpd` A6 + rights matrix. Sources: lgpd-brazil.info, IAPP, ICLG.
4. **nFADP "Art. 12" — SUITE CONFLATED two provisions.** Art. 12 = register of processing activities (>250 employees); the notify-unless-DPO mechanic is Art. 23(4); DPIA = Art. 22 + Ordinance Art. 14; FDPIC consultation = Art. 23. Corrected in `ch-nfadp` A12. Sources: fedlex.admin.ch, kmu.admin.ch, Termly.
5. **UAE penalties — suite's AED 20M figure uncorroborated; withdrawn.** Web: administrative fines AED 50k–5M; implementing rules = Cabinet Decision No. 33 of 2024 (in force); Data Office de facto 72h breach standard. Corrected in `ae-pdpl` A1/A8. Sources: Securiti, RecordingLaw, CookieYes.
6. **Vietnam — INSTRUMENT SUPERSEDED.** PDPL No. 91/2025/QH15 (enacted 2025-06-26, effective 2026-01-01) replaced Decree 13. Also resolves the Art. 9 collision: PDPL Art. 9 = consent, rights at Art. 4; the Decree's own Art. 9 was rights, so the quick-select "Art. 9 (minimization)" was wrong twice over. Record banner added; registry, C3, floor A10 caveated pending re-authoring. Sources: Rouse, Tilleke & Gibbins, FPF, luatvietnam.vn.

One line per reconciliation: file · claim · outcome (record-wins / subfile-wins→core-fixed / consistent / both-flagged). Subagent fragments (`recon-*.md`) merge here.

## 2026-07-04 — consent-language family (wiring pattern proof, done inline)

- `consent-language--rights-language.md` · response timelines (GDPR 1mo+2, CCPA 45+45, PIPEDA 30, Law25 30+10, LGPD 15) · **consistent** with records A6.
- `consent-language--rights-language.md` · LGPD Object → Art. 18(II) duplicates the Access anchor · **both-flagged** — `[VERIFY]` inline (†) and in `br-lgpd` A6. Not resolvable from suite sources; do not guess the correct anchor.
- `consent-language--breach-notification.md` · Law 25 72h to CAI + individuals · **both-flagged** — consistent across suite files, but primary-source doubt stands (`[VERIFY]` inline † and in `ca-pipeda-law25` A8). GDPR 72h floor unaffected.
- `consent-language--breach-notification.md` · all other timeline rows · **consistent** with records A8 (LGPD 3bd/5bd, SG 3cd/500+, PIPL immediately, PIPEDA RROSH-feasible, POPIA ASAP, CCPA none).
- `consent-language--childrens-consent.md` · age table · **consistent** with records A9 (CA 13-guidance, EU 16/13–16, UK 13+AADC, BR 18, CN 14, ZA 18, AU 15-guidance).
- `consent-language--notice-templates.md` · "[30 days — GDPR]" in templates vs 1-month clock in records/timeline table · **consistent-by-design** — deliberate plain-language rendering (Grade-8 target); noted in the file's provenance line, no edit.
- `consent-language--notice-templates.md` · UK IDTA in transfer checklist · operational template content, no record equivalent (A10 UK divergence block doesn't enumerate IDTA) · **no action** — record A10 already carries `[UNVERIFIED]` on Chapter V mechanics.
- `consent-language--cookie-consent.md` · GPC table (CA §7026 binding; EU withdrawal-only per EDPB 8/2024; UK ICO draft) · **consistent** with `us-ca-ccpa` A2 / `eu-gdpr-uk` divergence block.
- `consent-language.md` · Art. 6 bases, Art. 4(11)/7(3) consent standard, Arts. 13/14 checklist · **consistent** with `eu-gdpr-uk` A2/A6.

## 2026-07-04 — data-minimization family (done inline; subagents lost to session limit)

- `data-minimization--regulatory-reference.md` · POPIA enforcer "IOPA / IO" in both quick-select tables vs "Information Regulator (IR)" in its own section text · **fixed** — both table cells corrected to match section text; `[VERIFY]` on body-name stands in `za-popia`.
- `data-minimization--regulatory-reference.md` + `--pipeda-gdpr.md` · grounding-source provenance notes added (records canonical going forward; fixes land record-first).
- `data-minimization--quasi-identifiers.md` · 1 statutory-pattern line (prose GDPR caution, no citations) · **no-action** — left untouched by design.
- `data-minimization--ocsf-minimization.md` · exception-record citations (GDPR 5(1)(c)/25(1), PIPEDA 4.7.1, NIS2 Art. 21) · **consistent** with records; provenance added; cross-linked to conflict C2.

## 2026-07-04 — privacy-impact-assessment family (done inline)

- `privacy-impact-assessment.md` · LGPD Art. 38 (ANPD may require DPIAs) · **subfile-wins → core fixed** — `br-lgpd` A12 upgraded from [UNVERIFIED] to sourced; trigger-scope flag retained.
- `privacy-impact-assessment.md` · Singapore PDPC-advisory DPIA recommendation · **subfile-wins → core fixed** — `sg-pdpa` A12 upgraded from [UNVERIFIED] to sourced.
- `privacy-impact-assessment.md` · PIPEDA OPC-recommended PIAs · **subfile-wins → core enriched** — `ca-pipeda-law25` A12.
- `privacy-impact-assessment.md` · PIPL Art. 55 trigger row listed "large-scale processing", not in the Art. 55 list per its own `--dpia-triggers.md` (entrusting/sharing is) · **record-wins → subfile fixed** — row corrected to match Art. 55.
- `privacy-impact-assessment--dpia-triggers.md` · Law 25 63.5 list, EDPB 09/2022, HIPAA, PIPL 55/56 · **consistent** with records A12 (records were built from this file); grounding-source provenance added.
- `privacy-impact-assessment--pia-template.md` · 45 statutory-pattern lines · provenance added; **consistent**.

## 2026-07-04 — threat-model-privacy family (done inline)

- All three sub-files (`adversary-profiles`, `asset-taxonomy`, `mitigations`) · 0 statutory-pattern lines each · **no-action** — left untouched by design.
- `threat-model-privacy.md` · regulatory-grounding pointer paragraph added (axes A1/A8/A10 + conflicts register for Archetypes 6–7 / INSTITUTIONAL class).

## 2026-07-05 — independent verification pass (12 Tier-3 + sectoral records)

- Context-match verification (subagent, thorough): **1 issue in 12 records.** `us-coppa` S2 cited § 312.4 untagged — substantively correct COPPA but not traceable to suite sources · **fixed** — [UNVERIFIED] tag added. Informational: "no private right of action" in `us-hipaa`/`us-glba` untagged standard characterizations · **fixed** — tagged. All other untagged citations and concrete values confirmed matching on both section number and content (AU s. 13G penalties, JP Art. 2(3) list, KR Art. 34 clocks, HIPAA §§ 160.404/164.404-408, GLBA § 314.4 element letters, BIPA § 15(a)–(e) + verdicts, COPPA VPC table).

## 2026-07-04 — suite router

- `privacy-suite.md` · "GDPR/PIPAA/HIPAA/LGPD" typo · **fixed** → PIPEDA.
- `privacy-suite.md` · taxonomy routing section + skill summary added.
