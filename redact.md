---
name: redact
description: Sanitizes documents, text, and code by detecting and removing or masking personally identifiable information (PII) and sensitive data before sharing, logging, or passing to external APIs. Use when user says "redact", "sanitize", "anonymize", "remove PII", "scrub this", "clean this before I share it", "hide personal info", or uploads a file they want checked for sensitive data. Also triggers on requests to prepare content for external use, bug reports, logs, or pastes that may contain credentials, wallet addresses, or personal identifiers.
---

# Redact

A multi-pass PII detection and sanitization skill. Strips, masks, or pseudonymizes sensitive identifiers from text, code, documents, and structured data.

---

## Modes

Always confirm the mode with the user before proceeding unless it is obvious from context.

| Mode | Output | When to use | Legal standard met |
|---|---|---|---|
| `REDACT` | `[REDACTED]` | Highest privacy — no recovery possible | Exceeds all standards |
| `PSEUDONYMIZE` | `[NAME_1]`, `[EMAIL_2]` | Preserve structure, entities distinguishable | Internal use; not de-identification |
| `TOKENIZE` | `sha256:a3f2...` (first 8 chars) | Consistent mapping for data analysis | Internal use; not de-identification |
| `HIPAA_SAFE_HARBOR` | Remove all 18 PHI identifiers per 45 CFR § 164.514(b)(2) | Healthcare data; producing de-identified data under HIPAA | HIPAA Safe Harbor de-identification |
| `GDPR_ANONYMIZE` | k-anonymous output — all quasi-identifiers generalized or suppressed | Producing data outside GDPR scope for research/analytics | GDPR/WP29 anonymization (high bar) |

Default to `PSEUDONYMIZE` if the user doesn't specify — it preserves readability.

**Critical distinction — pseudonymization vs. anonymization:**
- `PSEUDONYMIZE` / `TOKENIZE` produce **pseudonymous** data — still personal data under GDPR Art. 4(1) and HIPAA. Subject to all regulatory obligations.
- `HIPAA_SAFE_HARBOR` produces **de-identified** data under HIPAA — outside HIPAA scope if all 18 identifiers removed AND no actual knowledge of re-identification risk.
- `GDPR_ANONYMIZE` produces **anonymous** data — outside GDPR scope if re-identification is "reasonably impossible" per EDPB guidelines. This is a much higher bar than HIPAA Safe Harbor.

### HIPAA_SAFE_HARBOR Mode

**Statutory basis:** 45 CFR § 164.514(b)(2). Remove all 18 PHI identifiers. If successful, the resulting data is not PHI and falls outside HIPAA scope.

**The 18 identifiers — all must be removed or generalized:**

1. Names — all names
2. Geographic subdivisions smaller than state — street address, city, county, precinct. **ZIP code rules:** 3-digit prefix may be retained IF the geographic unit contains >20,000 people AND is not one of the 17 high-risk 3-digit codes listed in § 164.514(b)(2)(i)(B). Otherwise suppress to `000`.
3. All dates (except year) — birthdate, admission date, discharge date, death date. **Age >89 rule:** any age over 89 must be aggregated to a single category "90 or older."
4. Phone numbers
5. Fax numbers
6. Email addresses
7. Social security numbers
8. Medical record numbers
9. Health plan beneficiary numbers
10. Account numbers
11. Certificate / license numbers
12. Vehicle identifiers and serial numbers including license plates
13. Device identifiers and serial numbers
14. Web URLs
15. IP addresses — full IPv4 and IPv6
16. Biometric identifiers including fingerprints and voiceprints
17. Full-face photographs and comparable images
18. Any other unique identifying number, characteristic, or code

**HIPAA_SAFE_HARBOR output format:**
```
HIPAA SAFE HARBOR REDACTION REPORT
Mode: HIPAA_SAFE_HARBOR (45 CFR § 164.514(b)(2))
PHI identifiers removed: [count] across [count] categories
ZIP code handling: [retained 3-digit / suppressed to 000 — state basis]
Age handling: [exact year retained / aggregated to 90+ — state basis]

FIELDS PROCESSED:
  [1] Names: [count] instances → REMOVED
  [2] Geographic: [detail] → [action taken]
  [3] Dates: [detail] → Year retained; day/month removed
  ...

RESIDUAL RISK STATEMENT:
  Covered entity confirms: no actual knowledge that remaining information
  could be used to identify an individual (45 CFR § 164.514(b)(2)(ii)).
  [This statement must be confirmed by the covered entity — Claude cannot
  make this attestation on behalf of the organisation.]

RECOMMENDATION: Expert determination review (§ 164.514(b)(1)) is advised
  for datasets where re-identification risk from remaining attributes is uncertain.
```

### GDPR_ANONYMIZE Mode

**Legal standard:** GDPR Recital 26; EDPB (formerly WP29) Opinion 05/2014 on anonymization techniques. Data is anonymous only if re-identification is "reasonably impossible" given all means likely to be used. This is a higher and more context-dependent bar than HIPAA Safe Harbor.

**WP29 three-criterion test:** Assess whether the data can:
1. **Singled out** — isolate an individual in the dataset
2. **Linked** — link records relating to the same individual
3. **Inferred** — deduce information about an individual

Anonymization fails if ANY criterion is satisfiable. Pseudonymization fails all three criteria if the pseudonym key is destroyed — but the data is still personal data while the key exists.

**GDPR_ANONYMIZE applies:**
- k-anonymity (minimum k=5; k=10 for sensitive data): every combination of quasi-identifiers appears in at least k records
- l-diversity extension where sensitive attributes are present: at least l distinct sensitive attribute values per equivalence class
- Generalization of quasi-identifiers: exact values → ranges or categories
- Suppression of records that cannot be generalized without k-anonymity violation
- Differential privacy noise for numeric aggregates (ε ≤ 1.0)

**GDPR_ANONYMIZE output format:**
```
GDPR ANONYMIZATION REPORT
Mode: GDPR_ANONYMIZE (EDPB Opinion 05/2014; Recital 26)
k-anonymity achieved: k=[value] (minimum k=5 required)
l-diversity: [value] / [N/A if no sensitive attributes]
ε-differential privacy applied: [yes/no; ε value if yes]

TRANSFORMATIONS APPLIED:
  age: 34 → "30-39" (generalized)
  zip_code: 90210 → "902**" (generalized)
  occupation: "Radiologist" → "Healthcare professional" (generalized)

QUASI-IDENTIFIER ANALYSIS:
  Combination {age_bracket, zip_prefix, gender} → k=7 ✓
  All equivalence classes contain ≥ 5 records ✓

RESIDUAL RISK:
  This output satisfies k=[k]-anonymity. Note that k-anonymity
  does not guarantee immunity from all re-identification attacks,
  particularly with auxiliary data (Sweeney, 2000; Netflix attack, 2006).
  For high-sensitivity data, independent expert review is recommended.

GDPR STATUS: If the above transformations are correctly applied and no
  auxiliary data enables re-identification, this data falls outside
  GDPR scope per Recital 26. However, the controller retains responsibility
  for this determination — Claude's analysis is advisory only.
```

---

## Entity Categories

Run detection across ALL of the following in every pass:

### Personal Identifiers
- Full names, usernames, handles
- Email addresses
- Phone numbers (all formats: +1-555-..., (555) ..., international)
- Fax numbers
- Physical addresses, postal/ZIP codes (flag ZIP codes — HIPAA PHI)
- Date of birth, admission/discharge/death dates, any age >89 (HIPAA: must aggregate to 90+)
- Government ID numbers (SIN, SSN, passport, driver's license, certificate/license numbers)
- IP addresses (v4 and v6) — PHI under HIPAA when in health context
- Device identifiers (MAC addresses, UDIDs, IMEI, medical device serial numbers)
- Vehicle identifiers and license plate numbers
- Web URLs when associated with an individual
- Full face photographs or comparable images
- Biometric identifiers (fingerprints, voiceprints, retina scans)
- Any other unique identifying number or code — when in doubt, flag

### Health / Medical (HIPAA PHI — all CRITICAL in healthcare context)
- Medical record numbers
- Health plan beneficiary numbers
- Patient account numbers
- Diagnoses, conditions, procedures, prescriptions
- Lab results, test results, clinical notes
- Health insurance information
- Mental health records
- Substance use disorder records (additional protection under 42 CFR Part 2)
- Genetic information (GINA protection in US, Art. 9 GDPR, sensitive category globally)

### Financial
- Credit/debit card numbers (with or without spaces/dashes)
- Bank account numbers, routing numbers, IBANs, SWIFTs
- CVV/CVC codes
- Health plan / insurance account numbers (dual-classified: financial + PHI)

### Credentials & Secrets
- Passwords and passphrases (in plaintext or assignments: `password=...`)
- API keys and tokens (look for long alphanumeric strings near words like `key`, `token`, `secret`, `bearer`, `sk-`, `pk-`)
- Private keys and mnemonics (seed phrases, PEM blocks)
- Session cookies, JWT tokens

### Crypto / Web3
- Solana public keys and wallet addresses (base58, 32–44 chars)
- Ethereum addresses (0x + 40 hex chars)
- Bitcoin addresses (P2PKH, P2SH, Bech32)
- Transaction hashes and signatures
- NFT mint addresses

### Organizational
- Internal project codenames, ticket IDs (if user flags as sensitive)
- Employee/user IDs, customer IDs
- Internal URLs, hostnames, server names, file paths revealing org structure

---

## Workflow

### Step 1 — Confirm scope and mode
Ask the user:
1. What mode? (REDACT / PSEUDONYMIZE / TOKENIZE) — default PSEUDONYMIZE
2. Any categories to skip? (e.g. "keep email domains", "preserve wallet address format")
3. Any custom sensitive terms to add? (internal codenames, project names)

Skip this step if mode is clear from context and proceed directly.

### Step 2 — First pass: structural scan
Read the full input. Identify the content type: prose, code, JSON/YAML, CSV, logs, mixed. Note which entity categories are likely present.

### Step 3 — Second pass: entity extraction
Extract all candidate sensitive entities. For each:
- Entity text (exact)
- Category (from list above)
- Confidence: HIGH / MEDIUM / LOW
- Context snippet (surrounding 10 words)

Flag LOW confidence hits separately for user review — do not auto-redact without noting uncertainty.

### Step 4 — Apply substitutions
Apply the selected mode. For PSEUDONYMIZE:
- Maintain a consistent mapping within the document: the same entity always gets the same label
- Use typed labels: `[PERSON_1]`, `[EMAIL_1]`, `[WALLET_1]`, `[API_KEY_1]`, etc.
- Increment the counter per entity TYPE, not globally

### Step 5 — Emit redaction manifest
After the sanitized output, always emit a manifest block:

```
--- REDACTION MANIFEST ---
Mode: PSEUDONYMIZE
Entities found: 12
  [PERSON_1]     → detected 3 times  (HIGH)
  [EMAIL_1]      → detected 1 time   (HIGH)
  [API_KEY_1]    → detected 1 time   (HIGH)  context: "Bearer ..."
  [WALLET_1]     → detected 2 times  (MEDIUM) context: "sent to ..."
Low-confidence flags (not auto-redacted):
  "Project Phoenix" — may be internal codename — confirm?
```

### Step 6 — Offer follow-up actions
After delivering the sanitized output and manifest, offer:
- Re-run with a different mode
- Export sanitized version as a file
- Review and manually resolve LOW confidence flags

---

## Special Handling

### Code files
- Redact string literals containing PII, not variable names
- Flag hardcoded secrets in assignments: `API_KEY = "sk-..."` → `API_KEY = "[API_KEY_1]"`
- Do not alter code logic, only literal values

### Logs
- Preserve log structure, timestamps, severity levels
- Redact only the payload fields, not the scaffolding
- Be especially aggressive on IP addresses and user IDs in log lines

### JSON / YAML / CSV
- Preserve keys/headers; redact values only
- Flag if a key name itself is sensitive (e.g. `ssn`, `password` as a key)

### Markdown / Documents
- Preserve all formatting, headings, and structure
- Inline redaction: replace only the sensitive span, not surrounding text

---

## Error Handling

**Input too large to process at once**
Split into logical chunks (paragraphs, JSON objects, log lines). Process each chunk, then merge manifests at the end.

**Ambiguous entity (name that might be a common word)**
Flag as LOW confidence. Do not auto-redact. Surface in manifest for user decision.

**Crypto addresses uncertain**
Solana base58 strings can be ambiguous. Flag anything 32–44 chars that appears near words like `wallet`, `address`, `pubkey`, `from`, `to`, `mint`. Mark MEDIUM confidence if no surrounding context confirms.

**User asks to skip a category**
Honour the request. Note in manifest: "Category [X] excluded by user request."

---

## Reference files

- `references/regex-patterns.md` — Canonical regex patterns for each entity type. Load when doing code-based or structured data redaction.
- `references/crypto-patterns.md` — Detailed Web3 address format specs (Solana, ETH, BTC, tx hashes). Load for any Web3 content.

---

## Examples

### Example 1: Prose redaction
**Input:** "Hi, I'm Sarah Chen, you can reach me at sarah.chen@acme.com or 416-555-0192."
**PSEUDONYMIZE output:** "Hi, I'm [PERSON_1], you can reach me at [EMAIL_1] or [PHONE_1]."
**Manifest:** 3 entities, all HIGH confidence.

### Example 2: Hardcoded API key in code
**Input:** `const apiKey = "sk-ant-abc123xyz456";`
**PSEUDONYMIZE output:** `const apiKey = "[API_KEY_1]";`
**Manifest:** 1 entity, HIGH confidence. Recommend rotating the exposed key.

### Example 3: Solana wallet in log
**Input:** `Transfer 5 SOL from 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU`
**PSEUDONYMIZE output:** `Transfer 5 SOL from [WALLET_1]`
**Manifest:** 1 entity, MEDIUM confidence (base58 pattern + "from" context).
