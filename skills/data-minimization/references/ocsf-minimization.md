# OCSF Minimization Reference

Data minimization guidance for Open Cybersecurity Schema Framework (OCSF) schemas, SIEM event structures, and security telemetry pipelines.

> **Source of truth:** statutory anchors in this file (GDPR Art. 5(1)(c)/25(1), PIPEDA Cl. 4.7.1; NIS2 is a sectoral overlay) derive from `taxonomy/regulatory-taxonomy.md` records. Reconciled 2026-07-04; log: `.fable/reconciliation-log.md`. The logging-vs-storage-limitation tension this file resolves is conflict **C2** in `taxonomy/regulatory-taxonomy--conflicts.md`.

---

## OCSF Overview

OCSF (Open Cybersecurity Schema Framework) — open-source schema released 2022 by AWS, Splunk, IBM, and others. Version 1.x. Schema browser: schema.ocsf.io.

**Taxonomy:** 6 categories → 14 subcategories → 60+ event classes. Each class has:
- Required attributes (must be present)
- Recommended attributes (should be present)
- Optional attributes (may be present)
- Observables (typed key-value pairs for entities like IPs, hashes, domains)

**Minimization principle for OCSF:** Include only attributes required or recommended by the specific event class. Optional attributes should be included only when they serve a documented security purpose. Observables should be minimized to the specific observable types needed for detection and response.

---

## Field Inheritance — Audit Both Layers

Every OCSF event inherits the **Base Event** fields. These must be audited alongside class-specific fields.

### Base Event fields — minimization audit checklist

| Field | Type | Minimization consideration |
|---|---|---|
| `activity_id` | Integer | Required — no minimization |
| `category_uid` | Integer | Required — no minimization |
| `class_uid` | Integer | Required — no minimization |
| `time` | Timestamp | **Precision** — wall-clock ms often not needed; consider slot/block number for on-chain events or second-precision for logs |
| `message` | String | **Optional** — only include if adding information not in structured fields; avoid redundant natural-language description of structured data |
| `metadata.uid` | String | **PII risk** — if using user-generated IDs that contain PI (email-based IDs, etc.) |
| `metadata.product.uid` | String | Low risk — product identifier |
| `metadata.version` | String | **Stack fingerprinting** — reveals exact product version; acceptable for internal SIEM, flag for external sharing |
| `metadata.labels` | Array | **PII risk** — free-form labels may contain user-provided content with PI |
| `raw_data` | String | **HIGH RISK** — raw log line may contain PI not captured in structured fields; apply `redact` skill before storing |
| `severity_id` | Integer | Required — no minimization |
| `status_id` | Integer | Required — no minimization |
| `timezone_offset` | Integer | **Revealing** — timezone narrows geographic location; consider dropping for externally shared events |
| `type_uid` | Integer | Required — no minimization |
| `unmapped` | Object | **HIGH RISK** — catch-all for fields not mapped to OCSF; likely to contain unminimized PI; audit all unmapped fields |

---

## Class-Specific Minimization

### Class 2008 — IAM Analysis Finding (delegation-security tooling primary class)

**Use case:** Security findings about identity and access management — delegation risk, excessive permissions, anomalous access patterns.

**Required fields:** `activity_id`, `category_uid` (5), `class_uid` (2008), `finding`, `metadata`, `severity_id`, `status_id`, `time`, `type_uid`

**Observable minimization for class 2008:**

| Observable | OCSF type | Minimization recommendation |
|---|---|---|
| User / wallet address | `user` observable | HMAC-SHA256 with domain-separated key; do not store plaintext in shared/external logs |
| Resource / token mint | `resource` observable | HMAC-SHA256 or content hash; mint address is pseudonymous but linkable |
| IP address | `network_endpoint` observable | Truncate to /24; only include if network-layer correlation needed for finding |
| Process | `process` observable | Include only if process identity is relevant to finding (scanner process, not user process) |
| Timestamp | `time` | Block/slot number for on-chain events; second precision for off-chain; drop millisecond precision for external sharing |

**Finding object minimization:**

```json
{
  "finding": {
    "uid": "DS-2024-001247",          // Internal reference — no PI
    "title": "High-risk delegation",   // Descriptive — no PI
    "types": [...],                    // OCSF taxonomy — no PI
    "desc": "Anomalous delegation velocity detected",  // Generic — no PI
    "confidence_score": 85,           // OK — no PI
    "severity_id": 3,                 // OK — no PI
    "related_events": []              // CAUTION: may contain PI if including raw event refs
  }
}
```

**Drop from class 2008 in external/shared logs:**
- `actor.user.email_addr` — use HMAC pseudonym
- `actor.user.full_name` — use pseudonym
- `src_endpoint.ip` — use /24 truncation
- `raw_data` — strip or redact before storage
- `metadata.version` — acceptable internal, flag external

---

### Class 3002 — Security Finding

**Use case:** Generic security findings — vulnerability scan results, CSPM findings, posture assessments.

**Key minimization concerns:**

| Field | Risk | Action |
|---|---|---|
| `affected_resources[].uid` | May be user-specific resource ID | HMAC if resource is user-associated |
| `affected_resources[].data` | Arbitrary data — high PI risk | Apply `redact` skill; audit all values |
| `evidences[].data` | Raw evidence — may include PI | Strip or redact |
| `finding.uid` | Ticket IDs may reveal internal systems | OK for internal; consider opaque ID for external |
| `resources[].owner` | May be individual user | HMAC or role-based reference |

---

### Class 4001 — Network Activity

**Use case:** Network connection events — firewall logs, IDS alerts, flow records.

**High-sensitivity fields:**

| Field | Minimization |
|---|---|
| `src_endpoint.ip` | /24 truncation; never full IP in external logs |
| `dst_endpoint.ip` | External IPs: preserve for threat intel; internal IPs: truncate/pseudonymize |
| `src_endpoint.hostname` | May reveal internal network topology; pseudonymize for external |
| `http_request.url` | May contain query parameters with PI; strip query params or redact PI values |
| `http_request.user_agent` | Full UA is fingerprint; truncate to major browser/OS only |
| `traffic.bytes_in/out` | Bucket into ranges if individual values not needed for detection |

**Retention tension:** Network flow records often need 90-365 days for threat hunting. Full IP addresses in long-term retained logs create GDPR storage limitation issues. Solution: tiered retention — full fidelity 30 days, /24 truncated 90 days, aggregated counts only after 90 days.

---

### Class 1001 — File System Activity

**Use case:** File access, creation, modification, deletion events.

| Field | Minimization |
|---|---|
| `file.path` | May contain username in path (`/Users/realname/...`); pseudonymize username component |
| `file.owner` | User identity — HMAC for external; acceptable for internal SIEM |
| `actor.user.uid` | Pseudonymize for external sharing |
| `actor.user.name` | Pseudonymize for external sharing |
| `file.content` | **NEVER log file content** — may contain arbitrary PI |
| `file.hashes` | OK — hashes are not PI |

---

### Class 6003 — API Activity

**Use case:** API request/response events — REST APIs, GraphQL, RPC calls.

| Field | Minimization |
|---|---|
| `http_request.url` | Strip query parameters containing tokens, IDs, or PI values |
| `http_request.http_headers` | **HIGH RISK** — Authorization headers contain bearer tokens; strip before logging |
| `http_request.body` | **HIGH RISK** — Request body may contain PI; never log raw request bodies |
| `http_response.body` | **HIGH RISK** — Response body may contain PI; never log raw response bodies |
| `actor.user.uid` | Pseudonymize for external; acceptable for internal |
| `src_endpoint.ip` | /24 truncation |

---

## Observable Types — Minimization by Type

OCSF observables are typed instances of entities that appear in events. Each type has specific minimization considerations.

| Observable type | Type ID | Minimization |
|---|---|---|
| `Hostname` | 1 | Internal hostnames: pseudonymize for external; OK for internal |
| `IP Address` | 2 | /24 truncation for logs; full for active threat response only |
| `MAC Address` | 12 | Pseudonymize — MAC addresses are device identifiers |
| `User Name` | 4 | HMAC pseudonym for external; acceptable for internal SIEM |
| `Email Address` | 5 | HMAC pseudonym always — high-sensitivity PII |
| `URL` | 6 | Strip query params; redact PI in path components |
| `File Name` | 7 | Strip username from path; OK otherwise |
| `Hash` | 8 | OK — hashes are not PI |
| `Subnet` | 9 | OK — /24 is already minimized |
| `Process Name` | 13 | OK for system processes; pseudonymize if user-named process |
| `Command Line` | 27 | **HIGH RISK** — CLI args often contain tokens, passwords, paths with usernames; redact |
| `User` | 14 | HMAC pseudonym for external |
| `Geo Location` | 10 | City/country level only; never coordinates |
| `Domain` | 3 | OK for public domains; pseudonymize internal domain components |

---

## SIEM Tiered Retention with OCSF

Recommended retention architecture for OCSF-mapped security logs:

```
Hot (0-30 days):
  Full OCSF event, all fields
  Full observable values
  Raw data included (if needed for investigation)
  Access: SOC analysts, IR team
  Storage: Encrypted at rest; AES-256-GCM; access-controlled

Warm (30-90 days):
  OCSF event with PI fields pseudonymized:
    - user.uid → HMAC(uid, log_domain_key)
    - src_endpoint.ip → /24 truncation
    - http_request.url → query params stripped
  raw_data: removed
  Access: Same as hot, with audit log of access

Cold (90-365 days):
  Aggregated OCSF finding summary per asset/rule/day:
    - Count of findings per rule_id per day
    - Distribution of severity_ids
    - No per-event records
  Access: Compliance team, audit
  
Archive (>1 year — only where legally required):
  Statistical summaries only
  No individual event records
  Access: Legal, regulatory audit
```

---

## Defensible Exception: Security Log Full Fidelity

When full-fidelity OCSF logs are required for a security purpose:

```
MINIMIZATION EXCEPTION — SECURITY TELEMETRY
Field: src_endpoint.ip (full IPv4)
OCSF Class: 4001 (Network Activity)
Exception basis: Active threat hunting and incident response
  Full IP required for: lateral movement correlation, C2 identification,
  threat actor attribution, IOC matching against threat intel feeds
Compensating controls:
  - Hot tier limited to 30 days (not indefinite)
  - Role-based access: IR team only (3 named individuals)
  - All access logged with mandatory justification field
  - Not replicated to analytics or data science pipelines
  - Pseudonymized in all external-facing reports and threat intel sharing
Regulatory basis:
  GDPR Art. 5(1)(c): "adequate" and "necessary" for security purpose
  GDPR Art. 25(1): compensating controls satisfy PbD obligation
  NIS2 Art. 21: security monitoring is a mandatory measure
  PIPEDA Clause 4.7.1: safeguards appropriate to sensitivity
Review: Quarterly or on material change to detection architecture
```

---

## pySigma Pipeline: OCSF + Privacy

If using pySigma for detection rule translation with OCSF output:

```python
from sigma.processing.pipeline import ProcessingPipeline
from sigma.processing.transformations import FieldMappingTransformation

# Pipeline that maps Sigma fields to OCSF + applies minimization
ocsf_privacy_pipeline = ProcessingPipeline(
    name="ocsf-with-privacy",
    transformations=[
        # Map Sigma user field to OCSF user.uid (will be pseudonymized)
        FieldMappingTransformation({
            "user": "user.uid",
            "src_ip": "src_endpoint.ip",
            "dst_ip": "dst_endpoint.ip",
        }),
        # Custom transformation: truncate IP to /24
        IPTruncationTransformation(fields=["src_endpoint.ip", "dst_endpoint.ip"]),
        # Custom transformation: HMAC user fields
        HMACPseudonymizationTransformation(
            fields=["user.uid", "actor.user.uid"],
            domain_key="ocsf-security-logs-2024"
        ),
    ]
)
```

Implement `IPTruncationTransformation` and `HMACPseudonymizationTransformation` as custom pySigma transformation classes. These are not in the standard pySigma library — custom implementation required.

---

## References

- OCSF Schema Browser: schema.ocsf.io
- OCSF GitHub: github.com/ocsf/ocsf-schema
- AWS Security Lake (OCSF reference implementation): docs.aws.amazon.com/security-lake
- pySigma OCSF backend: github.com/SigmaHQ/pySigma-backend-ocsf
- OCSF Class 2008 (IAM Analysis Finding): schema.ocsf.io/1.0.0/classes/iam_analysis_finding
