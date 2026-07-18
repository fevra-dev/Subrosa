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

## 2026-07-17 — quarterly currency sweep (standing watches; web-verified)

- **EU AI Act — Digital Omnibus on AI**: Annex III high-risk deferred **Aug 2 2026 → Dec 2 2027**; Annex I embedded-product → Aug 2 2028; AI-generated-content marking → Dec 2 2026; other Art. 50 transparency unchanged (Aug 2 2026). Parliament Jun 16 2026 · Council Jun 29 2026 · OJ publication expected Jul 2026 · **records fixed** — `eu-ai-act` header/reform-watch + reg-reference §EU AI Act phased-application block. Sources: Travers Smith; Morgan Lewis; Inside Global Tech; artificialintelligenceact.eu.
- **CCPA — CPPA regs finalized**: ADMT/risk-assessment/cyber-audit regs adopted Jul 24 2025, OAL-approved Sep 23 2025, **eff. Jan 1 2026**; ADMT compliance Jan 1 2027; pre-2026 activities assessed by Dec 31 2027; first filings Apr 1 2028; audits phased 2028–2030 · **record fixed** — `us-ca-ccpa` A6 ADM row + A12 upgraded from [UNVERIFIED]; master quick-index row updated. Sources: cppa.ca.gov (Sep 23 2025 announcement); White & Case; Skadden.
- **Canada — Bill C-27 dead**: died on the Order Paper at prorogation **Jan 6 2025**; no PIPEDA replacement tabled as of mid-2026; **Bill C-15** (third reading Feb 26 2026) adds data-mobility framework to PIPEDA · **record fixed** — `ca-pipeda-law25` reform-watch row. Sources: Fasken; Blakes; Gowling WLG; LEGISinfo.
- **India — DPDP Rules 2025**: notified **Nov 14 2025**; phased commencement Nov 14 2025 / Nov 14 2026 (Consent Managers) / **May 13 2027** (core duties) · **record fixed** — `in-dpdpa` banner rewritten from "NOT IN FORCE" to phased-commencement; A5/A8 flags annotated with Rules dates. Sources: MeitY notification coverage (S&R Associates; Shardul Amarchand Mangaldas; Privacy World).
- **Vietnam — Decree 356/2025/ND-CP** (Dec 31 2025, eff. Jan 1 2026) **formally replaced Decree 13/2023** — resolves the `vn-pdpl` Transition hedge ("presumably ceases effect"); `vn-pdpd` historical banner annotated. Sources: DLA Piper Data Protection Laws of the World (VN); DataGuidance.
- **Malaysia — CBPDT Guidelines No. 3/2025** (Apr 29 2025) contents reviewed: whitelist replaced by receiving-jurisdiction assessment (substantially-similar law / at-least-equivalent protection / exceptions) · **record fixed** — `my-pdpa` A10; standing-watch item closed. Sources: pdp.gov.my GP_CBPDT; Mayer Brown; Hogan Lovells.

## 2026-07-17 — UNVERIFIED resolution pass (primary-source web verification, 12 records)

**Citation error caught and corrected suite-wide:** the CCPA minimization/proportionality test ("reasonably necessary and proportionate") was miscited as **§ 1798.100(a)(3)** in 9 locations across 5 files — the correct anchor is **§ 1798.100(c)**; (a)(3) is the at-collection retention-disclosure/limitation provision. Both grounding sources (`pipeda-gdpr.md`, `regulatory-reference.md`) carried the error, which is why every derived artifact repeated it. All 9 corrected with dated notes (record + floor + quick index + both grounding sources). Sources: FindLaw § 1798.100; law.justia; Greenberg Traurig analysis.

**Anchors resolved from [UNVERIFIED] (34 flags, all web-verified 2026-07-17):**
- `eu-gdpr-uk` (7): Arts. 79/82 (remedy/compensation) · 6(1)(d)/(e) bases · 33(1) "unlikely to result in a risk" carve-out + 33(4) phased disclosure · 34(3)(a) unintelligible-data exemption (exact text) · Chapter V Arts. 45/46(2)(c)/47/49 · 32 security · 36 prior consultation. Source: gdpr-info.eu article pages.
- `us-ca-ccpa` (6): § 1798.140(d) thresholds (incl. 2026 CPI adjustment $26.625M) · residency reach · § 1798.155 fines ($2,500/$7,500) · § 1798.100(a)(3) retention disclosure · § 1798.120(c) minors two-tier opt-in · anchor correction above.
- `au-apps` (2): Part IIIC ss. 26WE/26WK/26WL (OAIC) · agencies PIA mandate — APP Code 2017 s. 12 + PIA register (OAIC/legislation.gov.au).
- `kr-pipa` (2): Art. 22-2 under-14 legal-representative consent + verification · Art. 33 PIA public-mandatory/private-voluntary.
- `jp-appi` (1): Art. 26 breach — four trigger classes, prelim ~3–5 days, confirmed 30/60 days (IAPP; DLA Piper).
- `sg-pdpa` (1): ss. 21/22 + Fifth/Sixth Schedule exceptions + s. 22A preservation (SSO; PDPC guidelines).
- `cn-pipl` (3): Art. 19 shortest-period retention · Art. 57 breach (incl. individual-notice waiver) · Art. 51 safeguards catalogue (chinalawtranslate family).
- `br-lgpd` (2): Art. 7 ten bases · Arts. 15/16 termination/elimination (lgpd-brazil.info; IAPP).
- `za-popia` (1): s. 72(1) transfer grounds (popia.co.za; Michalsons).
- `in-dpdpa` (5): s. 3(b) extraterritoriality · §§ 11–14 rights · s. 8(5) safeguards · s. 8(6) dual breach intimation · s. 16(1) blacklist transfer model (FPF; dpdpa.com).
- `us-coppa` (2): § 312.4 notice content verified against eCFR (closes the 2026-07-05 flag) · § 1798.120(c) cross-reference.
- `ch-nfadp` (2): Art. 25 access · Arts. 16/17 transfer adequacy + exceptions (bj.admin.ch; EDÖB).

Remaining [UNVERIFIED] lines: 80 (down from ~113) — concentrated in TH/NG/AE/MY scaffolds ("not located in suite sources" coverage notes) and structural-absence claims, left flagged deliberately. All touched records' `Current as of` bumped to 2026-07-17.

## 2026-07-17 — gap-closure pass (portfolio depth; all web-verified 2026-07-17)

Operator-requested final pass closing gaps identified in a coverage review against privsec.dev and the awesome-privacy repos. Five additions:

- **C8 — identification mandates vs anonymous transaction systems** (`--conflicts.md`): the register's first architecture-vs-*law* combat entry (C1–C7 are architecture-vs-*policy* dissolution). FATF R16 Travel Rule (USD/EUR 1,000 threshold); EU TFR 2023/1113 (fully applicable Dec 30 2024, zero-threshold for CASPs + self-hosted-wallet verification >EUR 1,000); the enforcement arc — Tornado Cash OFAC sanction (Aug 2022) → *Van Loon v. Treasury* 5th Cir. (Nov 26 2024) → OFAC delisting (Mar 21 2025); Roman Storm conviction (Aug 6 2025, unlicensed money transmitter; deadlock on ML/sanctions); Pertsev (NL, 64mo, on appeal); Samourai founders' guilty pleas (Jul 30 2025), Rodriguez 5yr (Nov 2025). Resolution: Privacy Pools proof-of-innocence (`ARCH-SATISFIES`, explicitly not `ARCH-DISSOLVES`). Sources: fatf-gafi.org; EUR-Lex 2023/1113; Treasury/OFAC; DOJ/SDNY; 5th Cir. Tagged design-informing, not legal advice.

- **Lineage continuation** (`lineage.md` + README + `web3-privacy.md`): the canon no longer stops at Nakamoto 2008. Added CryptoNote (2013), Zerocash (2014), Signal Double Ratchet (2016), Bulletproofs (2018), and **Privacy Pools / "Towards a Practical Equilibrium" (Buterin, Illum, Nadler, Schär, Soleimani 2023)** — the first canonical text written in the taxonomy's own language. New `web3-privacy.md` §Regulatory-Compliant Privacy with the association-set construction and its TTP/liability caveats. Also resolved a now-stale flag: the Chaum 1981 mixnet paper was marked `[UNVERIFIED — not in suite sources]` in the dissolution map; it is now sourced (lineage + comms.md), flag removed.

- **UK OSA age-assurance S-record** (`--uk-osa.md`, new; registered in master): highly-effective age assurance enforceable Jul 25 2025 (Ofcom; passive self-declaration prohibited; £18M/10%-revenue fines). C5 extended with the 2025–26 wave incl. *Free Speech Coalition v. Paxton*, 606 U.S. 461 (Jun 27 2025, 6–3, upholding TX HB 1181). The record where "floor vs ceiling" is most concretely demonstrable (retention-based ID vs ZK age predicate). **Record count 26 → 27**; propagated to README + dissolution-map + privacy-architecture SKILL.

- **DROP currency fix** (`us-ca-ccpa` + threat-model `mitigations.md`/`asset-taxonomy.md`): California Delete Act SB 362 / DROP live for consumers Jan 1 2026, broker processing from Aug 1 2026; CalPrivacy enforcement decisions Jan 8 2026. Replaces the "DeleteMe, tedious but effective" mitigation with the statutory one-stop mechanism. Sources: cppa.ca.gov; privacy.ca.gov/drop; Clark Hill.

- **LINDDUN crosswalk + badness-enumeration anti-pattern**: new `threat-model-privacy/references/linddun-crosswalk.md` mapping the seven LINDDUN categories ↔ archetypes ↔ P1–P7 ↔ axes ↔ primitives (interoperability with the NIST-referenced standard). Named the "badness enumeration" anti-pattern in `opsec-review/SKILL.md`, crediting privsec.dev — making the suite's structural-over-reactive stance legible. This is the methodological (not tool-list) takeaway from the reviewed repos; OS-hardening/VPN/tool-directory content deliberately declined as out of scope.

Conflict register now C1–C8; taxonomy 27 modeled records + derived artifacts.
