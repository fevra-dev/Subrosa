# Sectoral Record: United States — FERPA

| | |
|---|---|
| **Record** | `us-ferpa` · **Status:** SECTORAL-OVERLAY (S-profile v1.1) · **Current as of:** 2026-07-05 |
| **Instruments** | FERPA, 20 U.S.C. § 1232g; 34 CFR Part 99 |
| **Sources** | `data-minimization--regulatory-reference.md` §FERPA |

## S0 — Scope Trigger
**Education records × federally-funded educational agency/institution.** "Education records": records directly related to a student, maintained by the institution. Pulls in EdTech platforms, SIS/LMS vendors handling US K-12 or higher-ed student data.

## S1 — Enforcement
US Department of Education (Family Policy Compliance Office). **No private right of action** — enforcement via withdrawal of federal funding. The exposure model is institutional (funding), not litigational.

## S2 — Obligation Spine
- **Disclosure restriction:** no disclosure of education records without written consent, except enumerated exceptions — school officials with *legitimate educational interest*, transfer schools, financial aid, judicial orders, health/safety emergencies.
- **Parent/student rights:** inspect and review; request amendment; complain.
- **Directory information:** name, address, phone, attendance dates, degrees — disclosable unless the student opts out.

## S3 — Overlay Map (when S0 fires)
| Axis | Override |
|---|---|
| A2 | written-consent-or-enumerated-exception disclosure model |
| A4 | "legitimate educational interest" = a per-staff purpose-limitation and minimization standard — staff access only records needed for their function (sourced P1/P2/P6 mapping) |
| A6 | inspect/review/amend rights replace omnibus rights vector |
| A5 | directory-info carve-out inverts the default: a *disclosable-by-default* class with opt-out |

## S4 — Interactions
School health records are FERPA-covered, **not** HIPAA — except records held by a school health professional acting as a care provider, which flip to HIPAA (sourced; mirrored in `us-hipaa` S4).

## S5 — Defined Lists
Directory-information categories (S2); "education record" definition.

**Tags:** role-scoped access enforcing legitimate-educational-interest is `ARCH-SATISFIES` (P6 as access architecture); consent/exception paperwork and amendment workflow `PROCEDURAL`.
