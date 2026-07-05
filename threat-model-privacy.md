---
name: threat-model-privacy
description: Conducts structured IC-methodology personal and project-level privacy threat modeling. Produces adversary profiles, asset inventories, attack surface maps, confidence-graded risk assessments, and tiered mitigation plans. Use when user says "threat model", "model my threats", "what are my risks", "who would target me", "privacy risk assessment", "OPSEC plan", "am I a target", "what should I be protecting", "security posture review", or when starting a new project, identity, or operational context that warrants a structured risk baseline. Also triggers for relationship-context threat modeling (stalking, coercive control, harassment scenarios).
---

# Threat Model: Privacy

Structured adversarial analysis of personal and project-level privacy risk. Produces a defensible, falsifiable threat model using IC-standard analytic methodology.

**Invoke `opsec-review`** to audit specific artifacts once the threat model is established.
**Invoke `redact`** to sanitize content identified as exposed by this model.

**Regulatory grounding:** when a threat model touches statutory exposure — breach-notification clocks, regulator powers, penalty ceilings, cross-border compulsion — pull jurisdiction facts from `regulatory-taxonomy.md` and its records (axes A1/A8/A10) rather than restating them; cross-regime incompatibilities live in `regulatory-taxonomy--conflicts.md`. Relevant to the INSTITUTIONAL capability class and Archetypes 6–7.

---

## Methodology

Four-phase IC-influenced process:

```
Phase 1: ASSET INVENTORY     — What are you protecting?
Phase 2: ADVERSARY PROFILING — Who wants it and why?
Phase 3: ATTACK SURFACE MAP  — How could they get it?
Phase 4: MITIGATION PLAN     — What do you do about it?
```

Analytic standards applied throughout:
- **Falsification-first**: every claim must state what evidence would disprove it
- **ICD 203 confidence framing**: four-dimensional confidence on all risk assessments (source quality, analytic soundness, information completeness, analytic consistency)
- **Pre-mortem discipline**: for each HIGH+ risk, ask "assume this was exploited — what happened?"
- **Adversarial pressure testing**: actively argue against your own conclusions before finalizing

---

## Phase 1 — Asset Inventory

Elicit assets through structured questioning. Do not accept vague answers — push for specifics.

### Asset Categories

**Identity Assets**
- Legal name / pseudonym separation
- Platform accounts and handles
- Email addresses (primary, alias, throwaway)
- Phone numbers
- Biometric data (Face ID, fingerprints enrolled)
- Government-issued ID numbers
- Financial account access

**Operational Assets**
- Source code and IP
- Client/customer relationships and data
- Internal tooling and infrastructure knowledge
- Credentials and key material
- Research and unpublished work
- Communications history

**Relational Assets**
- Social graph (who knows who)
- Family / partner / associate identities
- Employer / client relationships
- Community memberships

**Physical Assets**
- Home address
- Work location
- Regular physical patterns (commute, gym, etc.)
- Hardware (devices, lab equipment)

**Reputational Assets**
- Professional reputation
- Pseudonymous reputation (separately)
- Public statements and positions

### Asset Sensitivity Tiers

For each asset identified, assign:

| Tier | Label | Meaning |
|---|---|---|
| T1 | CRITICAL | Exposure causes irreversible harm |
| T2 | HIGH | Exposure causes significant harm, recoverable with effort |
| T3 | MEDIUM | Exposure causes meaningful harm, manageable |
| T4 | LOW | Exposure is inconvenient or mildly harmful |
| T5 | INFO | Essentially public or harmless |

**Rule:** If uncertain between two tiers, assign the higher one. Document the uncertainty explicitly.

Load `references/asset-taxonomy.md` for detailed classification guidance.

---

## Phase 2 — Adversary Profiling

Identify plausible adversaries. Load `references/adversary-profiles.md` for full archetype library.

### Adversary Dimensions

For each adversary, characterize across five dimensions:

**1. Motivation**
- Financial (fraud, extortion, theft)
- Reputational (discrediting, embarrassing)
- Operational (disruption, sabotage, espionage)
- Personal (harassment, stalking, coercive control)
- Ideological (targeting based on beliefs or affiliations)
- Legal (building a case, discovery, regulatory)

**2. Capability**
- NATION-STATE: Full intelligence apparatus, zero-day access, physical options
- CRIMINAL ORG: Sophisticated tooling, purchased capabilities, scale
- ADVANCED INDIVIDUAL: Technical skills, OSINT proficiency, persistence
- SCRIPT KIDDIE: Off-the-shelf tools, opportunistic
- SOCIAL: Non-technical but socially sophisticated (social engineering, legal tools)
- INSTITUTIONAL: Subpoena power, legal compulsion, compliance access

**3. Access**
- Remote only
- Physical access possible
- Insider / trusted relationship
- Supply chain position

**4. Persistence**
- Opportunistic (one-shot)
- Sustained campaign (weeks/months)
- Long-term (years, nation-state tier)

**5. Targeting**
- Mass / indiscriminate
- Sector-targeted (e.g. crypto community)
- Individual-targeted (you specifically)

### Confidence Assessment (ICD 203 Framework)

For each adversary, rate:
- **Source quality**: How reliable is the basis for believing this adversary exists?
- **Analytic soundness**: Is the reasoning from evidence to conclusion valid?
- **Information completeness**: What do we not know that would change the picture?
- **Analytic consistency**: Does this assessment agree with prior assessments?

Express as: `HIGH / MODERATE / LOW` confidence with a one-line basis statement.

**Falsifiability check**: State what evidence would cause you to REMOVE this adversary from the model.

### Adversary Prioritization

Rank adversaries by: `Motivation × Capability × Access × Likelihood`

Use a 1–5 scale per dimension. Prioritize top 3 for deep analysis. Document but deprioritize the rest.

---

## Phase 3 — Attack Surface Map

For each T1/T2 asset × top-3 adversary combinations, map the attack surface.

### Attack Vector Categories

**Digital — Remote**
- Phishing / spearphishing
- Credential stuffing / account takeover
- Supply chain compromise (dependency, tool, service)
- API abuse / scraping
- Social engineering (platform support, SIM swap)
- Malware / RAT delivery
- Network interception (public WiFi, ISP-level)

**Digital — Platform**
- Platform policy abuse (false reports, account bans)
- Legal compulsion (subpoena of platform data)
- Data broker aggregation
- OSINT correlation (cross-platform identity linking)
- Metadata inference (timing, style, behavioral patterns)

**Physical**
- Device theft / seizure
- Border crossing / customs search
- Physical surveillance
- Mail interception
- Coercive access (legal, relational, coercive control)

**Social**
- Impersonation of trusted contact
- Relationship infiltration
- Reputation attack (coordinated reporting, false accusations)
- Legal harassment (frivolous litigation, regulatory complaints)

### Attack Chain Analysis

For each HIGH priority combination, document the kill chain:

```
Adversary: [name]
Asset: [name / tier]
Vector: [category]

Reconnaissance:  What does adversary need to know first?
Initial access:  How do they get their first foothold?
Execution:       What do they do with that access?
Impact:          What is the actual harm to the asset?
Indicators:      What would tell you this is happening?
```

### Pre-Mortem

For each T1 asset: **Assume it was compromised. It is six months from now. What happened?**

Write 3–5 sentences describing the plausible exploitation path. This surfaces assumptions you didn't know you were making.

---

## Phase 4 — Mitigation Plan

Load `references/mitigations.md` for the full control library.

### Mitigation Tiers

Controls are assigned to one of three tiers:

| Tier | Label | Principle |
|---|---|---|
| M1 | PREVENT | Make the attack impossible or cost-prohibitive |
| M2 | DETECT | Know when an attack is occurring or has occurred |
| M3 | RESPOND | Limit damage and recover when prevention fails |

A complete mitigation posture has all three tiers for every T1 asset. Missing M2 or M3 is a critical gap — prevention alone is not sufficient.

### Mitigation Prioritization

Rank controls by:
- **Impact**: How much does this reduce risk to T1/T2 assets?
- **Effort**: Time, cost, and friction to implement
- **Coverage**: How many adversaries / vectors does this address?

Produce a prioritized action list: **Quick wins first** (high impact, low effort), then **structural controls** (high impact, high effort), then **incremental hardening**.

### Residual Risk Assessment

After mitigations: for each T1 asset, state the **residual risk** — what risk remains even after all controls are in place. Be honest. No model eliminates all risk.

---

## Output Format

```
=== THREAT MODEL ===
Scope: [personal / project / infrastructure / identity]
Date: [today]
Analyst: [user or Claude]

ASSET INVENTORY
───────────────────────────────────
[T1] Source code IP (Delegate Scout, Kyma)
[T1] Pseudonym / fevra-dev identity separation
[T2] Client relationships at Exchange.Art
[T3] Home address
...

ADVERSARY PROFILES
───────────────────────────────────
Priority 1: [adversary name]
  Motivation:   [type]
  Capability:   [tier]
  Access:       [type]
  Persistence:  [type]
  Targeting:    [mass/sector/individual]
  Confidence:   MODERATE — [basis]
  Falsifier:    [what would remove this adversary from model]

...

ATTACK SURFACE MAP
───────────────────────────────────
[Asset] × [Adversary] → [Vector]
Kill chain: ...
Pre-mortem: ...

...

MITIGATION PLAN
───────────────────────────────────
QUICK WINS (implement this week)
  1. [control] — addresses [assets] against [adversaries]
  2. ...

STRUCTURAL (implement this month)
  1. ...

INCREMENTAL (ongoing)
  1. ...

RESIDUAL RISK
───────────────────────────────────
[T1 asset]: [residual risk statement] — [what would need to change to reduce further]
...

CONFIDENCE SUMMARY
───────────────────────────────────
Overall model confidence: HIGH / MODERATE / LOW
Key uncertainties:
  - [what we don't know]
  - [what would materially change this model]
Next review trigger: [event or date]
```

---

## Elicitation Guide

If the user hasn't provided enough context, ask these questions — one at a time, not as a list dump:

1. **Scope**: Personal OPSEC, a specific project, an infrastructure environment, or a new identity/pseudonym?
2. **Context**: What's changed recently that prompted this? (new project, new threat, incident, etc.)
3. **Existing posture**: What controls are already in place? (don't build mitigations for things already handled)
4. **Adversary intuition**: Who do you already suspect might be interested in you or your work?
5. **Tolerance**: What level of residual risk is acceptable? (some people accept more friction for more protection)

Do not ask all five at once. Start with scope, infer the rest from context where possible.

---

## Special Contexts

### Pseudonymous Identity Threat Model
When scope includes pseudonym/real-identity separation, load `references/adversary-profiles.md` section on deanonymization adversaries. Identity correlation is the primary attack surface — weight it heavily.

### Relationship-Context Threats (Coercive Control, Stalking, Harassment)
When adversary is a known individual in a personal relationship:
- Capability assessment changes significantly (insider access, shared accounts, physical access history)
- Social engineering vectors are more plausible (shared contacts, impersonation)
- Legal tools may be available to adversary (family court, shared accounts, shared property)
- Recommend device hygiene audit as first action before any other step
- Do not minimize stated risk — err toward higher capability / higher motivation

### Regulatory / Legal Adversary
When adversary has subpoena or regulatory power:
- Data minimization becomes a primary control (you can't produce what you don't have)
- Jurisdiction matters — where is data stored vs. where adversary has compulsion authority?
- Third-party data exposure (what do your providers hold that adversary could compel?)

---

## Reference Files

- `references/adversary-profiles.md` — Adversary archetype library with TTPs, typical targets, and capability baselines
- `references/asset-taxonomy.md` — Detailed asset classification guidance with sensitivity tier examples
- `references/mitigations.md` — Control library organized by vector category, with effort/impact ratings
