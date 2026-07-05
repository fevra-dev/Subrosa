# Quasi-Identifiers & Re-identification Risk

Reference for cross-field analysis during data minimization audits.

---

## What is a Quasi-Identifier?

A quasi-identifier (QID) is a field that does not directly identify an individual but, when combined with other QIDs, narrows the candidate population sufficiently to enable re-identification.

**Seminal finding (Sweeney, 2000):** The combination of `{5-digit ZIP code, birth date, sex}` uniquely identifies 87% of the US population. None of these three fields is a direct identifier.

---

## Common Quasi-Identifier Fields

### High-discriminating QIDs (flag if 2+ present together)

| Field | Why high-discriminating |
|---|---|
| Full date of birth | ~365 × ~100 years = ~36,500 values; highly discriminating |
| 5-digit ZIP / full postal code | ~42,000 US ZIP codes; rural ZIPs have very small populations |
| Precise geolocation (lat/lng, address) | Near-unique in many contexts |
| Full IP address | Often maps to a single household |
| Device fingerprint | Often near-unique |
| Exact salary / income | High discriminating power in many populations |
| Rare medical condition | Small candidate population by definition |
| Rare combination of attributes | Multiplicative narrowing |

### Medium-discriminating QIDs (flag if 3+ present together)

| Field | Why medium-discriminating |
|---|---|
| Age (exact years) | ~100 values; manageable alone, powerful in combination |
| Gender / sex | Binary or small enum; powerful in combination |
| City / municipality | Varies by city size |
| Employer | Powerful for small orgs |
| Job title | Powerful for senior/rare roles |
| Ethnicity / race | Powerful in combination with other fields |
| Native language | Narrows population significantly |
| Education level | Moderate discriminating power |
| Household size | Moderate |

### Low-discriminating QIDs (flag if 4+ present together)

| Field | Notes |
|---|---|
| Country | Low alone; powerful combined with city + age |
| Broad age bracket (18-24, 25-34...) | Acceptable replacement for exact age |
| Platform type (web/mobile/desktop) | Acceptable replacement for full user agent |
| General region / state / province | Acceptable replacement for city in many cases |

---

## Known High-Risk Combinations

These specific combinations have documented re-identification risk:

| Combination | Risk level | Source / notes |
|---|---|---|
| `{ZIP-5, DOB, sex}` | CRITICAL | Sweeney 2000 — 87% US re-identification |
| `{ZIP-5, DOB}` | HIGH | ~50% re-identification without sex field |
| `{lat/lng precise, timestamp}` | CRITICAL | Location traces re-identify via home/work anchors |
| `{age, city, occupation}` | HIGH | Narrows to very small population in smaller cities |
| `{employer, job_title, tenure}` | HIGH | Sufficient for LinkedIn re-identification |
| `{device_fingerprint, timestamp}` | HIGH | Cross-session tracking even without cookies |
| `{IP, timestamp, URL}` | HIGH | ISP-level correlation trivial |
| `{writing_style features, topic}` | HIGH | Stylometric deanonymization |
| `{wallet_address, on-chain activity}` | CRITICAL | Blockchain analytics firms routinely re-identify |

---

## Remediation Strategies for QID Clusters

### Generalization
Replace precise values with ranges or categories:
- `DOB: 1990-03-15` → `age_bracket: "30-34"`
- `ZIP: 90210` → `region: "West"`
- `salary: 127500` → `salary_band: "100k-150k"`

### Suppression
Remove records where combination creates unique identification risk. Applicable when dataset is small enough that some records are unique even after generalization.

### Noise Addition (Differential Privacy)
Add calibrated statistical noise to numeric fields before storage or release. The privacy budget (epsilon) determines the tradeoff between utility and privacy. Requires careful implementation — use established libraries (Apple's DP library, Google's DP library, OpenDP).

### K-Anonymity Check
A dataset satisfies k-anonymity if every record shares its QID combination with at least k-1 other records. Minimum k=5 is common; k=10+ for sensitive data.

To check: group by all QID fields; flag any group with fewer than k members as re-identification risk.

### L-Diversity Extension
K-anonymity alone is insufficient if a sensitive attribute (disease, salary) is uniform within a k-anonymous group. L-diversity requires at least l distinct values of the sensitive attribute within each group.

---

## Wallet Address as Quasi-Identifier (Web3 Context)

Wallet addresses deserve special treatment in Web3 schemas:

**On-chain wallet addresses are permanently public.** They are linkable across all transactions, all protocols, all time. They are not pseudonymous in practice — blockchain analytics firms (Chainalysis, Elliptic, TRM) maintain identity mappings.

**Re-identification vectors for wallet addresses:**
- Exchange KYC (deposits/withdrawals link wallet to verified identity)
- ENS / SNS names (user-chosen, often real name or known handle)
- NFT metadata (often includes real-world identity signals)
- Interaction with known addresses (CEX deposit addresses, charity wallets)
- On-chain activity patterns (timing, amounts, protocol preferences)
- IP address logged at RPC node level during transaction submission

**Minimization recommendations for wallet address in schemas:**
- Never use wallet address as a cross-context correlation key if avoidable
- If wallet address must be stored, treat as T1 asset (see threat model)
- In event logs: hash the wallet address with HMAC (domain-separated per log type)
- In analytics: aggregate to cohort level; never individual wallet-level behavioral analytics
- Never co-locate wallet address with off-chain PII (name, email) unless explicitly necessary

**GDPR conflict:** If wallet address is linkable to a natural person (via exchange KYC or other means), it is personal data under GDPR. Right to erasure is technically impossible on-chain — design around this from day one.
