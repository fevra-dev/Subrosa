---
name: data-minimization
description: Audits data schemas, API payloads, database models, event logs, and data pipelines for violations of data minimization principles — collecting, retaining, or exposing more data than necessary for the stated purpose. Use when user shares a schema, data model, API response, event structure, log format, or data flow and asks about privacy, compliance, GDPR, PIPEDA, unnecessary fields, what to drop, what to hash, or how to reduce data surface. Also triggers for OCSF mapping work, SPL/SIEM schema design, on-chain data structure review, and any request to make a data structure "more privacy-friendly", "compliant", or "minimal". Produces field-level findings with drop/hash/encrypt/aggregate remediation recommendations.
---

# Data Minimization

Field-level privacy audit for data schemas, API payloads, event structures, database models, and pipelines. Identifies excess collection, retention, and exposure — then recommends the least-invasive remediation for each violation.

**Composable with:**
- `redact` — strip actual PII values from sample data before analysis
- `threat-model-privacy` — establish what adversary can do with minimized data residual
- `opsec-review` — audit schemas before committing to public repos

---

## Scope

Handles any data structure type:

| Input type | Analysis focus |
|---|---|
| JSON / YAML schema | Field necessity, type precision, nullability |
| API request / response | Exposure surface, over-fetching, response bloat |
| Database model / ERD | Normalization, retention, separation of concerns |
| Event / log format | Temporal retention, identifier persistence, aggregation opportunities |
| OCSF / SIEM schema | Class mapping, field inheritance, observable minimization |
| On-chain data structure | Permanent immutability risk, public ledger exposure |
| Data pipeline / ETL | Transformation points where minimization can be applied |

Declare input type at start of analysis or infer from content.

---

## Regulatory Source of Truth

Statutory citations and jurisdiction facts (deadlines, thresholds, category lists, penalty ceilings) in this skill and its reference files derive from the normalized taxonomy: `taxonomy/regulatory-taxonomy.md` + the per-jurisdiction records (`taxonomy/regulatory-taxonomy--*.md`, axes A0–A12). Records consumed here: `ca-pipeda-law25`, `eu-gdpr-uk`, `us-ca-ccpa`, `br-lgpd`, `za-popia`, `cn-pipl`, `sg-pdpa`, `my-pdpa`, `th-pdpa` (+ HIPAA/GLBA/COPPA/BIPA as sectoral overlays pending their variant profile).

On any discrepancy between this skill's files and a record: **the record wins** — unless this file is more specific or more correct, in which case fix the record and log the reconciliation in `.fable/reconciliation-log.md`. Never resolve a conflict by inventing a citation. For "design-to-strictest" defaults use `taxonomy/regulatory-taxonomy--floor.md`; for cross-regime incompatibilities use `taxonomy/regulatory-taxonomy--conflicts.md`.

---

## Minimization Principles

Seven core principles applied to every audit. Load `references/pipeda-gdpr.md` for full regulatory mapping.

### P1 — Collection Limitation
Collect only what is necessary for the explicitly stated purpose. If no purpose is stated, flag every field.

**Violation signals:**
- Fields present "just in case" or "for future use"
- Fields copied from upstream without necessity check
- Full objects ingested when only one attribute is needed
- Verbose error payloads including internal state

### P2 — Purpose Specification & Binding
Data collected for purpose A must not be used for purpose B without re-consent or re-authorization.

**Violation signals:**
- Analytics fields mixed into transactional schemas
- Audit/debug fields persisted in production tables
- User behavioral data collected in security event logs
- Cross-purpose identifiers that link unrelated data stores

### P3 — Data Accuracy & Minimality of Precision
Collect at the minimum precision required. Don't store millisecond timestamps when day-level is sufficient. Don't store full addresses when city is enough.

**Violation signals:**
- Full timestamps where date or hour suffices
- Full IP address where /24 subnet suffices
- Exact geolocation where region suffices
- Full name where role or pseudonym suffices
- Exact age where age bracket suffices

### P4 — Storage Limitation (Retention)
Data must not be retained longer than necessary. Schemas with no TTL or expiry fields are a flag.

**Violation signals:**
- No `expires_at`, `ttl`, or `retention_days` field on time-sensitive data
- Soft-delete only (no hard-delete path)
- Audit logs with no rotation policy in schema
- Session or token data with no expiry

### P5 — Identifier Minimality
Use the least-linking identifier that serves the purpose. Persistent global IDs create cross-context linkage. Prefer ephemeral, scoped, or unlinkable identifiers.

**Violation signals:**
- Global user ID used in contexts where session ID suffices
- Device ID persisted across sessions unnecessarily
- Email address as primary key or foreign key
- Real-world identifier (name, phone) used as internal ID
- Wallet address used as persistent correlation key across unrelated events

### P6 — Separation of Concerns
Sensitive data should be isolated from non-sensitive data. Don't co-locate PII with analytics, behavioral, or operational data.

**Violation signals:**
- PII fields in the same table/collection as behavioral analytics
- User identity co-located with security event data
- Financial data mixed with preference/telemetry data
- Identifiers that unnecessarily link separated stores

### P7 — Cryptographic Minimization
Where raw values are not needed, use hashes, HMACs, or encryption. Where linkability is not needed, use one-way transforms.

**Violation signals:**
- Plaintext storage of values that only need equality checks (→ hash)
- Plaintext storage of values that need recovery only in rare cases (→ encrypt)
- Persistent identifiers where pseudonymous tokens suffice (→ tokenize)
- Unencrypted sensitive fields in event logs

---

## Remediation Vocabulary

Every finding maps to exactly one primary remediation action:

| Action | When to use | Privacy gain |
|---|---|---|
| **DROP** | Field serves no necessary purpose | Eliminates collection entirely |
| **HASH** | Only equality check needed (dedup, lookup) | Unlinkable to original |
| **HMAC** | Equality check needed + domain separation | Unlinkable across contexts |
| **ENCRYPT** | Value must be recoverable by authorized party | Protects at rest |
| **TOKENIZE** | Persistent reference needed without value exposure | Pseudonymous, reversible by token service |
| **TRUNCATE** | Full precision not needed | Reduces re-identification risk |
| **AGGREGATE** | Individual value not needed, only statistics | K-anonymity or differential privacy |
| **SEPARATE** | Field is necessary but shouldn't co-locate | Isolation without loss |
| **ADD TTL** | Field is necessary but retention is unbounded | Time-limits exposure window |
| **SCOPE-REDUCE** | Global identifier replaceable with scoped one | Limits cross-context linkage |

---

## Workflow

### Step 1 — Intake

Identify:
1. Input type (schema, API payload, DB model, event format, pipeline)
2. Stated purpose of the data structure (what is it for?)
3. Regulatory context — select all that apply:
   - **HIPAA**: any health, medical, patient, or clinical data; any US healthcare entity or BA
   - **PIPEDA/Law 25**: Canadian users or Canadian-resident operator
   - **GDPR/UK GDPR**: EU/EEA or UK users
   - **CCPA/CPRA**: California users
   - **COPPA**: any users who may be under 13
   - **LGPD**: Brazilian users
   - **PIPL**: Chinese users or transfer of data originating in China
   - **APPs**: Australian users or Australian-based operator
   - **None stated**: apply GDPR as highest common denominator
4. On-chain / immutable storage involved? (escalates severity — cannot be deleted)
5. Any fields already known to be sensitive by the user
6. **HIPAA flag**: if HIPAA applies, load `references/regulatory-reference.md` HIPAA section immediately — the 18 PHI identifiers override all other sensitivity classifications upward to CRITICAL

If purpose is not stated: ask. Minimization analysis is impossible without knowing what the data is for.

### Step 2 — Field inventory

List every field in the schema with:
- Field name
- Data type
- Inferred sensitivity (PII / QUASI-IDENTIFIER / OPERATIONAL / NON-SENSITIVE)
- Inferred purpose (why does this field exist?)

Flag fields where purpose is unclear.

### Step 2b — Derived and inferred field inventory

**Collected fields are not the only personal data in a system.** GDPR Art. 4(1) defines personal data as any information that "relates to" an identified or identifiable person — this explicitly covers data *derived* or *inferred* by the system, not just data directly provided by the user. GDPR Recital 26 confirms that inferred data is in scope. Many systems store only innocuous inputs but generate highly sensitive outputs.

For any system involving ML models, rules engines, scoring algorithms, or behavioral analytics, inventory all derived fields separately:

| Derived field | Input fields used | Generation method | What it reveals | Sensitivity | Regulatory flag |
|---|---|---|---|---|---|
| `risk_score` | `delegation_count`, `wallet_age`, `counterparty_list` | Weighted heuristic | Financial behavior profile | T2 | GDPR Art. 22 if used for decisions |
| `health_prediction` | `search_queries`, `purchase_history` | ML classifier | Inferred health condition | T1 | GDPR Art. 9 (special category) |
| `churn_probability` | `session_frequency`, `feature_usage` | Gradient boosting | Behavioral pattern | T3 | — |

**Derived field sensitivity rules:**

1. **A derived field can be higher sensitivity than its inputs.** A model that infers sexual orientation from purchase behavior produces Art. 9 special category data even if no sexual orientation data was collected.

2. **Inferred health data is PHI under HIPAA** if held by a covered entity — regardless of whether it came from a medical source or was inferred from behavioral data.

3. **GDPR Art. 22 applies** if a derived score or prediction is used to make or inform decisions that significantly affect individuals (credit, employment, insurance, access to services). Document explicitly.

4. **Inferred data has the same minimization obligations as collected data** — apply P1-P7 to derived fields. A risk score retained indefinitely without TTL violates P4. A score shared with third parties beyond its stated purpose violates P2.

5. **PIPL Art. 6 explicit prohibition:** excessive collection applies to outputs as much as inputs — generating granular behavioral profiles beyond what the stated purpose requires is a violation even if inputs were minimized.

Apply the same P1-P7 principle sweep (Step 3) to all derived fields identified here. Flag any derived field producing special category inferences as CRITICAL regardless of input sensitivity.

### Step 3 — Principle sweep

Apply each of the seven principles (P1–P7) to the full field inventory. For each violation found:

```
Field:      [field name]
Principle:  [P1–P7 label]
Finding:    [what the violation is]
Severity:   CRITICAL / HIGH / MEDIUM / LOW
Immutable:  YES / NO (on-chain or append-only logs = YES)
Remediation: [DROP / HASH / ENCRYPT / etc.]
Rationale:  [why this remediation is appropriate]
```

### Step 4 — Cross-field analysis

After per-field sweep, look for:

**Quasi-identifier clusters** — combinations of individually innocuous fields that together enable re-identification. Classic example: `{age, zip_code, gender}` re-identifies 87% of US population (Sweeney, 2000).

Flag any cluster of 3+ quasi-identifiers as a MEDIUM+ finding regardless of individual field severity.

**Unnecessary linkage keys** — foreign keys or shared identifiers that join tables/events which don't need to be joined for the stated purpose.

**Precision mismatches** — two fields at different precision levels where the higher-precision field makes the lower-precision one redundant (e.g., storing both `city` and `lat/lng`).

### Step 5 — Emit findings report

```
=== DATA MINIMIZATION AUDIT ===
Input type:  [type]
Purpose:     [stated purpose]
Regulatory:  [GDPR / PIPEDA / none]
Immutable:   [YES / NO]
Fields:      [count] total, [count] flagged

FIELD FINDINGS
──────────────────────────────────────────
[CRITICAL]  user_email  (P5 — Identifier Minimality)
  Finding:  Email used as foreign key in analytics events.
            Links identity store to behavioral data without necessity.
  Immutable: NO
  Action:   SCOPE-REDUCE → replace with scoped session token per analytics context.
            Token maps back to email only in identity service.

[HIGH]      ip_address  (P3 — Minimality of Precision)
  Finding:  Full IPv4 stored in event log. Geolocation to city level
            possible. Fraud detection requires only /24 subnet check.
  Immutable: NO
  Action:   TRUNCATE → store last octet as 0 (e.g. 192.168.1.0/24).

[HIGH]      created_at  (P4 — Storage Limitation)
  Finding:  No retention policy. Event log has no TTL field.
            Records accumulate indefinitely.
  Immutable: NO
  Action:   ADD TTL → add `expires_at` field; implement deletion job.

[MEDIUM]    user_agent  (P1 — Collection Limitation)
  Finding:  Full User-Agent string stored. Browser fingerprinting vector.
            Stated purpose (mobile vs desktop routing) needs only
            `platform` enum: [web, mobile, desktop].
  Immutable: NO
  Action:   TRUNCATE → extract platform enum, drop raw UA string.

[LOW]       referrer_url  (P2 — Purpose Binding)
  Finding:  Referrer URL stored in security event log.
            Security purpose doesn't require referrer.
  Immutable: NO
  Action:   DROP

CROSS-FIELD FINDINGS
──────────────────────────────────────────
[HIGH]  Quasi-identifier cluster: {age, city, device_type}
  Finding:  Three quasi-identifiers co-located. Combination narrows
            candidate population significantly in smaller cities.
  Action:   AGGREGATE age to bracket; DROP city (platform enum suffices).

SUMMARY
──────────────────────────────────────────
Critical: 1   High: 3   Medium: 1   Low: 1
Immutable violations: 0
Regulatory gaps: PIPEDA Principle 4 (limiting collection) — 3 fields
Recommended priority: address Critical + High before shipping.
```

### Step 6 — Revised schema

Offer to produce a minimized version of the schema with all recommended changes applied and commented. Mark each change with the principle it satisfies.

### Step 7 — Residual risk statement

After minimization, state what re-identification or linkage risk remains in the minimized schema. No schema is zero-risk — be honest about residual surface.

### Step 8 — Policy mode (optional)

If the user needs a formal written data handling and disposal policy (for compliance documentation, client contracts, regulatory audit, or internal governance), offer to generate one from the audit findings. Policy mode produces a standalone document structured as:

```
DATA HANDLING AND DISPOSAL POLICY
System / Schema: [name]
Version: [date]
Regulatory basis: [PIPEDA Clauses / GDPR Articles / CCPA sections]
Owner: [role]

1. PURPOSE OF COLLECTION
   [Documented purpose — basis for all minimization decisions]

2. DATA INVENTORY
   | Field | Classification | Retention | Disposal method |
   |-------|---------------|-----------|-----------------|
   | [field] | [PII/QUASI/OPS] | [TTL or event-based] | [method] |

3. RETENTION SCHEDULE
   [Per-field or per-category retention periods with trigger events]
   E.g.: "user_id: retained for duration of account + 30 days post-deletion"

4. DISPOSAL PROCEDURES
   Active data: [deletion mechanism — hard delete, crypto-erase, etc.]
   Backups: [backup purge schedule and method]
   Third-party processors: [contractual disposal obligations]
   Physical media: [shredding / degaussing / certified destruction]
   Verification: [how disposal is confirmed and logged]

5. EXCEPTIONS AND LEGAL HOLDS
   [Circumstances where normal retention is suspended — legal hold,
    regulatory investigation, litigation, mandatory minimum retention
    under applicable law]

6. ACCESS CONTROLS
   [Who can access which data classifications and under what conditions]

7. INCIDENT RESPONSE
   [What happens to this data in a breach scenario — notification
    obligations, containment steps, preservation requirements]

8. REVIEW SCHEDULE
   [When this policy is reviewed — recommend quarterly for T1/T2 data,
    annually for T3/T4, or on material schema change]

Regulatory basis citations:
  PIPEDA: Clause 4.5.3 (disposal), Clause 4.7 (safeguards)
  GDPR: Art. 5(1)(e) (storage limitation), Art. 25(1) (by design)
  CCPA/CPRA: § 1798.100(a)(3) (minimization), § 1798.105 (deletion)
```

Trigger policy mode when user says "generate a policy", "I need documentation for compliance", "write a data handling policy", "audit trail", or "client contract requires a privacy policy for this system."


---

## Special Contexts

### OCSF / SIEM Schema (Delegate Scout, security tooling)

When auditing OCSF-mapped schemas or SPL/SIEM event structures:

- **Observable minimization**: OCSF observables (IP, email, hostname, user) should be included only when required by the event class. Flag observables present in the schema that aren't defined in the OCSF class definition.
- **Class field inheritance**: OCSF base event fields are inherited — audit inherited fields too, not just declared ones.
- **Severity vs. sensitivity tension**: Security event logs need enough fidelity for detection. Document where minimization was deliberately limited for detection efficacy and why — this is a defensible exception, not a violation.
- **Retention asymmetry**: Security logs often need longer retention than privacy principles prefer. Flag the tension; recommend tiered retention (hot/warm/cold) with sensitivity-graded TTLs.

Load `references/ocsf-minimization.md` if present in environment.

### On-Chain / Immutable Storage

**Immutability changes everything.** Data written to a public blockchain cannot be deleted. GDPR right to erasure is technically impossible for on-chain data — this is a legal and technical conflict requiring explicit design decisions.

For any on-chain schema:
- Escalate ALL personal data findings to CRITICAL — there is no remediation path post-write
- Hash or encrypt ALL user-identifying fields before writing
- Never write wallet addresses to on-chain fields that didn't originate on-chain (creates permanent identity linkage)
- Prefer content-addressed references (IPFS CID, Arweave TX ID) to on-chain storage of actual data
- Permanent metadata (NFT attributes, token metadata) should be treated as public forever — design accordingly

### Analytics & Telemetry Schemas

- Behavioral analytics should never co-locate with PII (P6)
- Session IDs should rotate; never use persistent user ID in analytics events
- Aggregate before storing where individual-level data isn't needed
- Consider differential privacy for population-level statistics

### Financial / Payment Schemas

- PCI-DSS scope: never store raw PAN, CVV, or full track data
- Tokenize card references (Stripe token, not raw card)
- Financial identifiers (account numbers, routing) should be encrypted at rest
- Transaction amounts: necessary; user behavioral patterns derived from transactions: separate schema

---

## Reference Files

- `references/regulatory-reference.md` — Full global regulatory mapping at statutory precision: HIPAA (45 CFR §§ 164.502(b), 164.514 — 18 PHI identifiers, Minimum Necessary standard, Safe Harbor de-identification), PIPEDA (S.C. 2000, c. 5, Schedule 1 clauses + Quebec Law 25), GDPR (Reg. EU 2016/679 article/paragraph/recital level), CCPA/CPRA (Cal. Civ. Code section level), COPPA (15 U.S.C. §§ 6501-6506), LGPD (Law 13,709/2018), PIPL (effective Nov 1 2021, cross-border transfer requirements), Australia Privacy Act + APPs (Schedule 1), APPI (Japan, 2022 amendments), DPDPA (India 2023), POPIA (South Africa Act 4 of 2013). Cross-regime field risk matrix and multi-regime defensible exception template.
- `references/quasi-identifiers.md` — Quasi-identifier taxonomy, known re-identification risk combinations (Sweeney 2000 and others), k-anonymity / l-diversity thresholds, differential privacy guidance, Web3 wallet address re-identification vectors.
