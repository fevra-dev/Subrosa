---
name: opsec-review
description: Red-teams documents, code, READMEs, social posts, commit messages, and paste content for inadvertent operational security leakage before external exposure. Use when user says "review this before I post", "OPSEC check", "is this safe to share", "audit this README", "pre-flight check", "what does this reveal", "check before I push", or when preparing any artifact for public release, GitHub push, social media, client delivery, or external API submission. Distinct from PII redaction — focuses on what an adversary can INFER from context, metadata, structure, and timing signals, not just explicit identifiers.
---

# OPSEC Review

Adversarial pre-flight audit for artifacts before external exposure. Identifies unintended disclosure through inference, metadata, structure, and content signals — not just explicit sensitive data.

**Pair with `redact` skill** for PII/credential stripping. This skill covers what `redact` misses: the inferential layer.

---

## Artifact Types

Declare the artifact type at the start of review. Each has a distinct threat surface.

| Type | Load reference |
|---|---|
| Code / repository | `references/code-signals.md` |
| README / documentation | `references/doc-signals.md` |
| Social post / LinkedIn / blog | `references/social-signals.md` |
| Commit message / PR description | `references/doc-signals.md` |
| Paste / log dump / stack trace | `references/code-signals.md` |
| API payload / schema | `references/code-signals.md` |
| General prose / email | `references/doc-signals.md` |

If artifact type is ambiguous, identify it from content before proceeding.

---

## Threat Model

Reviews are scoped to one of three adversary profiles. Confirm with user or infer from context.

### Profile A — PUBLIC INTERNET
Passive adversary. Aggregates public data. Goal: fingerprint stack, infer org structure, identify vulnerabilities, find attack surface.

Typical threat: competitor, researcher, automated scanner, bug bounty hunter, recruiter building a dossier.

### Profile B — TARGETED
Active adversary with specific interest in the user or their org. Goal: correlate across sources, identify entry points, time attacks.

Typical threat: nation-state recon, social engineering setup, corporate espionage, doxxing campaign.

### Profile C — INSIDER / SUPPLY CHAIN
Has partial access. Goal: elevate privileges, extract data, pivot to connected systems.

Typical threat: malicious dependency, compromised contributor, rogue contractor.

Default to **Profile A** unless user specifies otherwise or artifact sensitivity implies higher tier.

---

## Signal Categories

Run all applicable categories for the artifact type. Reference files contain detailed patterns.

### 1. Infrastructure Fingerprinting
What the artifact reveals about the underlying stack:
- OS/distro identifiers (file paths, shebang lines, package managers)
- Exact version strings (libraries, runtimes, tools) — enables CVE correlation
- Internal hostnames, server names, container names
- Cloud provider / region hints (ARNs, GCP project IDs, Azure tenant refs)
- Port numbers, internal service names
- CI/CD platform artifacts (pipeline IDs, runner names, workflow file structure)

**Risk:** Adversary maps your stack and cross-references against known CVEs.

### 2. Organizational Structure Leakage
What the artifact reveals about the org:
- Internal project codenames surfacing in comments, variable names, URLs
- Team names, department names, reporting structure hints
- Employee handles, Slack channel names, internal Jira/Linear ticket IDs
- Internal tool names (proprietary, not public)
- Acquisition targets, partner names before announcement
- Roadmap signals in feature flags, TODO comments, dead code

**Risk:** Competitive intelligence, social engineering targeting.

### 3. Timing & Pattern Signals
What the artifact reveals through metadata and rhythm:
- Commit timestamps revealing work hours, timezone, geographic region
- File modification times embedded in exports
- Frequency patterns (when is the team active, when are deploys?)
- Version cadence revealing release schedules
- Response time in logs revealing infrastructure performance characteristics

**Risk:** Physical security (when is the office empty), targeted phishing timing, infrastructure load profiling.

### 4. Operational Tradecraft Leakage
What the artifact reveals about methods and tooling:
- Security tool names in comments or scripts (reveals defensive posture)
- Penetration testing artifacts left in code (scan output, wordlists, payloads)
- Monitoring/alerting thresholds that reveal detection gaps
- Backup naming conventions, rotation schedules
- Auth flow details that reveal session management approach
- Feature flag naming that reveals A/B testing or phased rollout strategy

**Risk:** Adversary learns what you're watching for (and what you're not).

### 5. Dependency & Supply Chain Surface
What the artifact reveals about trust relationships:
- Unpinned dependencies (version ranges) that invite supply chain substitution
- Private registry references leaking internal package names
- Vendored code with upstream attribution revealing fork points
- Third-party service integrations (reveals data flows)
- Webhook endpoints or callback URLs

**Risk:** Supply chain attack surface mapping, data flow inference.

### 6. Geolocation & Physical Signals
What the artifact reveals about physical location:
- GPS metadata in images (EXIF)
- Timezone in timestamps or locale settings
- Language/locale settings in config files
- Office location in boilerplate, copyright notices, legal jurisdiction clauses
- IP addresses in logs that resolve to physical location

**Risk:** Physical surveillance, jurisdiction-based legal exposure.

### 7. Identity Correlation
What the artifact reveals that links to other identities:
- Usernames consistent across platforms
- Writing style, vocabulary, and phrasing patterns (stylometric fingerprinting)
- Code style signatures (indentation preference, naming conventions, comment patterns)
- Linked accounts in bios, `[authored-by]` fields, copyright lines
- PGP key IDs, SSH key fingerprints
- Avatar/profile image reuse

**Risk:** Identity correlation across pseudonymous personas, deanonymization.

---

## Workflow

### Step 1 — Intake
Identify:
1. Artifact type
2. Intended destination (GitHub public, LinkedIn, client email, API submission, etc.)
3. Adversary profile (default: Profile A)
4. Any categories to skip

Load the appropriate reference file for the artifact type.

### Step 2 — Systematic scan
Work through each Signal Category applicable to the artifact type. For each finding:
- **Signal type** (category name)
- **Location** (line, section, field)
- **Finding** (what was found)
- **Inference** (what an adversary learns)
- **Severity**: CRITICAL / HIGH / MEDIUM / LOW / INFO

### Step 3 — Emit findings report

```
=== OPSEC REVIEW REPORT ===
Artifact: [type]
Destination: [intended exposure]
Adversary profile: [A/B/C]
Reviewed: [signal categories covered]

FINDINGS
────────────────────────────────
[CRITICAL]  Infrastructure Fingerprinting
  Location: package.json line 12
  Finding:  "node": "20.11.0" (exact patch version)
  Inference: Adversary cross-references Node 20.11.0 CVE list.
  Action:   Loosen to ">=20.0.0" or remove engines field entirely.

[HIGH]      Organizational Structure Leakage
  Location: README.md, "Internal Slack: #project-helios"
  Finding:  Internal channel name + codename "Helios" exposed.
  Inference: Social engineering hook; confirms project exists pre-announcement.
  Action:   Remove. Use generic "team channel" if reference needed.

[INFO]      Timing Signal
  Location: Git commit timestamps (not in this artifact)
  Finding:  No timing signals present in artifact itself.
  Inference: N/A
  Action:   None.

SUMMARY
────────────────────────────────
Critical: 0  High: 1  Medium: 2  Low: 3  Info: 1
Overall risk: MEDIUM — address HIGH findings before publishing.
```

### Step 4 — Remediation options
For each CRITICAL and HIGH finding, offer:
- Specific rewrite suggestion
- Whether to remove, generalize, or replace with a placeholder
- Whether `redact` skill should be invoked for any explicit identifiers surfaced

### Step 5 — Re-review offer
After user applies fixes, offer a re-review pass to confirm resolution.

---

## Severity Definitions

| Level | Meaning |
|---|---|
| CRITICAL | Direct, immediate exploitability or deanonymization risk |
| HIGH | Strong inference possible with moderate adversary effort |
| MEDIUM | Useful to adversary when combined with other signals |
| LOW | Minor signal, low standalone value |
| INFO | Noted for awareness, no action required |

---

## Standing Rules

- **Never approve unconditionally.** Even a clean artifact gets an explicit "no significant findings" statement with the categories checked.
- **Infer intent conservatively.** If a signal *could* reveal something sensitive, flag it — let the user decide.
- **Cross-signal correlation.** Note when multiple LOW findings combine into a higher effective risk.
- **Don't just find problems — provide rewrites.** Every CRITICAL/HIGH must include a concrete remediation.
- **Pseudonymous persona mode.** If user indicates they operate under a handle/pseudonym, escalate Identity Correlation signals to HIGH by default.

---

## Reference Files

- `references/code-signals.md` — Detailed signal patterns for code, repos, logs, stack traces, API payloads
- `references/doc-signals.md` — Detailed signal patterns for docs, READMEs, social posts, commit messages, prose
