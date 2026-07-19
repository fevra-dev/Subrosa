# Documentation & Social Signal Patterns

Detailed OPSEC signal patterns for: READMEs, docs, blog posts, LinkedIn, social media, commit messages, PR descriptions, emails, prose.

---

## README / Documentation

### Infrastructure signals in docs
```markdown
# Bad — reveals exact stack
Built with Node 20.11 on Ubuntu 22.04, deployed on AWS us-east-1.

# Better — intentionally vague
Built with Node.js, deployed on cloud infrastructure.

# Bad — reveals internal tooling
We use Datadog for monitoring, PagerDuty for alerting, and Vault for secrets.

# Better
Observability and secrets management handled via industry-standard tooling.
```

### Installation instructions that fingerprint environment
```bash
# Reveals developer OS
brew install ...          # macOS
apt-get install ...       # Debian/Ubuntu (and which)
pacman -S ...             # Arch
choco install ...         # Windows

# Reveals internal tooling
npm install --registry https://npm.internal.company.com

# Reveals directory structure convention
mkdir ~/projects/company-name/  # Username hint, org name
```

### Copyright / legal boilerplate
```
Copyright 2024 Acme Corp, Inc.          # Legal entity name
Registered in Delaware, USA             # Jurisdiction
Contact: legal@internal.acme.com        # Internal email

# Office address in footer
123 Main St, Suite 400, San Francisco   # Physical location
```

### Contributor files
```
# AUTHORS, CONTRIBUTORS, MAINTAINERS files
# Reveal: real names, email addresses, GitHub handles
# Often cross-correlatable to LinkedIn, Twitter, other platforms

# .mailmap files
# Reveal: previous email addresses, name changes, alt identities
```

---

## Commit Messages

### Timing signals
```
# Commit at 3:47 AM reveals: timezone, work habits, or incident response
# Regular commits 9-5 Mon-Fri reveal: office hours, jurisdiction
# Commit surge on weekend reveals: crunch, incident, or offshore team
```

### Organizational leakage in commit messages
```
# Internal ticket references
fix: resolve PROJ-1234 auth regression     # Ticket system + project prefix exposed
feat: implement Helios integration          # Internal codename
wip: merging Atlas branch                  # Internal project name

# Personnel signals
Co-authored-by: Alice Smith <alice@company.com>   # Employee + internal email
Reviewed-by: Bob Jones                             # Reviewer identity

# Operational signals
hotfix: patch prod incident from 2024-01-15       # Incident history exposed
revert: rollback failed deploy                     # Operational failures visible
```

### What commit history reveals at scale
- Release cadence and velocity (competitive intelligence)
- Team size and contributor count
- Bus factor (single-contributor repos)
- Burnout signals (irregular commit patterns)
- Geographic distribution (timezone spread in commits)

---

## Social Posts / LinkedIn / Blog

### Stack fingerprinting in posts
```
# "What I'm working with" posts inadvertently reveal:
- Exact tools, versions, and configurations
- Pain points (attack surface hints)
- Upcoming features or products
- Team structure and size

# Job postings reveal:
- Entire tech stack in "requirements"
- Team structure in reporting lines
- Security gaps in "nice to have" (= not currently present)
- Salary bands (acquisition targeting)
```

### Identity correlation signals
```
# Username consistency across platforms
GitHub: @g33k-dev
Twitter: @g33k_dev      # Trivially correlatable
LinkedIn: G33K Dev      # Real name attached

# Profile photo reuse
# Same avatar across platforms = trivial cross-correlation

# Writing style signatures
# Distinctive phrases, punctuation habits, vocabulary
# Abbreviation patterns
# Emoji usage patterns
# Time-of-day posting patterns

# Biographical overlap
# Same employer, same city, same graduation year across platforms
# = identity confirmation even under pseudonym
```

### Operational timing leakage
```
# "Just shipped X" post reveals:
- Release cadence
- What's in production (attack surface)
- When team is distracted (deployment day = less monitoring attention)

# "Incident resolved" post reveals:
- You had an incident
- What systems were affected
- How long resolution took (team response capability)

# "We're hiring" post reveals:
- Team is growing (scaling = new infra = attack surface expanding)
- Which skills are missing (security gaps)
- Which roles exist (org chart reconstruction)
```

### Location leakage
```
# Conference attendance posts reveal:
- Geographic location on specific dates
- Physical security window (office empty? travel patterns?)
- Who you know (social graph)

# "Working from [city]" posts
# Check-in posts / tagged locations
# Background details in photos (skyline, signage, office decor)
# Event photos with badge/lanyard visible
```

---

## PR Descriptions / Issue Tracker

### Internal context that becomes public
```markdown
# PR description that leaked internal context:
## Summary
Fixes the bug reported by the Enterprise team re: Acme Corp onboarding.

# Reveals: specific customer name, that you have Enterprise tier,
# that onboarding is a pain point, customer identity

# Better:
## Summary
Fixes edge case in onboarding flow for multi-org accounts.
```

### Security-relevant PR signals
```
# "Security fix" PRs that reveal vulnerability class before patch is deployed
# Linked CVE numbers before advisory is published
# Rollback PRs that reveal failed security controls
# "Dependency bump" PRs that reveal you were vulnerable to published CVE
```

---

## Email / Client Communication

### What email headers reveal (if forwarded/screenshotted)
```
Received: from mail.internal.company.com   # Internal mail server hostname
X-Originating-IP: 10.0.1.45               # Internal IP address
Message-ID: <abc@mail.company.com>         # Domain structure
```

### Signature block signals
```
# Over-detailed signature:
Alice Smith | Senior Engineer | Platform Team
Acme Corp | 123 Main St, SF | Direct: +1-415-555-0192
Slack: @alice | Internal Wiki: wiki.acme.internal

# Reveals: full name, role, team, org, physical address, 
# phone number, Slack handle, internal tooling (Confluence/wiki)
```

---

## Pseudonymous Persona Checklist

If user operates under a handle/pseudonym, apply this additional checklist:

- [ ] No real name in any field (copyright, git config, email)
- [ ] Distinct username not used on non-pseudonymous platforms
- [ ] Writing style differs from real-identity writing
- [ ] No temporal correlation (posting at same times as real identity)
- [ ] No shared infrastructure (same VPS, same domain registrar account)
- [ ] No cross-linking (pseudonym doesn't link to real identity anywhere)
- [ ] Profile photo is unique (not used elsewhere)
- [ ] No geographic signals that narrow to a small population
- [ ] Timezone in commits doesn't uniquely identify you
- [ ] No shared interests/vocabulary that trivially correlate personas

**Flag any violation of the above as HIGH severity for pseudonymous users.**

---

## Stylometric Fingerprinting & Defense

**What it is:** Computational identification of an author from writing style. Vocabulary choices, syntactic patterns, punctuation habits, sentence length distributions, and function word frequencies form a unique fingerprint — distinct from content, invisible to the author, and persistent across documents.

**Why it matters:** For anyone operating under a pseudonym, stylometric analysis is the highest-probability deanonymization attack vector that doesn't require technical access — only text samples. Modern attacks achieve 80%+ accuracy from as few as 500 words [Narayanan & Shmatikoff, 2008; Koppel et al., 2011].

---

### Stylometric Attack Surface

**Primary signals (highest discriminating power):**

| Feature class | Examples | Resistance to deliberate masking |
|---|---|---|
| Function word frequencies | "the", "a", "in", "of" — unconscious, high-frequency | Very low — nearly impossible to suppress consciously |
| Punctuation patterns | Em dash vs. en dash vs. comma; semicolon usage; ellipsis frequency | Low — habits are automatic |
| Sentence length distribution | Mean, variance, skew of sentence lengths | Low |
| Vocabulary richness | Type-token ratio; rare word frequency | Medium — can be deliberately reduced |
| Character n-grams | Letter sequence frequencies | Very low |
| Syntactic patterns | Passive voice frequency; subordinate clause use; participle usage | Medium |
| Spelling/grammar idiosyncrasies | Recurring errors, British vs. American spelling | High — easy to mask once identified |
| Code style | Indentation preference, naming conventions, comment style, bracket placement | Medium |

**Cross-domain correlation:** If real-identity writing (blog posts, academic papers, emails) and pseudonymous writing share function word fingerprints, they are linkable even if content is completely different.

---

### Threat Models for Stylometric Attack

**Passive aggregation (Adversary: OSINT Aggregator, Profile B — Targeted):**
Adversary collects pseudonymous writing samples and known real-identity samples. Runs authorship attribution analysis (Burrows' Delta, support vector machines, neural stylometry). Links pseudonym to real identity.

*Required sample size:* ~500 words of pseudonymous writing; any amount of real-identity writing.

**Active comparison (Adversary: Platform Enforcement, Deanonymization Adversary):**
Platform or researcher compares writing across pseudonymous and real accounts on the same platform. Authorship clustering identifies accounts with similar stylometric fingerprints.

**Code authorship (Adversary: Competitive Intelligence):**
Code style analysis links commits under a pseudonymous GitHub handle to commits under a real-identity handle. Variable naming conventions, comment density, indentation style, and preferred abstractions are as distinctive as prose fingerprints.

---

### Practical Mitigations

**Tier 1 — High impact, low effort:**

☐ **Deliberate sentence length variation.** If natural writing tends toward similar sentence lengths, consciously vary: mix very short sentences with longer ones. Fragment. Then write a complex compound-complex sentence to create contrast.

☐ **Punctuation audit.** Identify your distinctive punctuation habits in real-identity writing. Suppress them in pseudonymous writing. If you habitually use em dashes — like this — avoid them entirely. If you never use semicolons; start using them.

☐ **Vocabulary register shift.** Write at a slightly different register than real-identity writing. If real-identity writing is technical and terse, pseudonymous writing should be more expansive (or vice versa).

☐ **British/American spelling consistency.** Pick one and never deviate in pseudonymous writing, even if real-identity writing mixes them.

☐ **Avoid signature phrases.** Identify recurring phrases in real-identity writing ("in practice", "the key insight is", "to be clear"). Actively suppress these in pseudonymous contexts.

**Tier 2 — Medium impact, medium effort:**

☐ **AI-assisted style normalization.** Pass pseudonymous writing through a style rewrite prompt before publishing. Prompt: "Rewrite the following in a neutral, generic academic/technical style, preserving content but removing stylistic idiosyncrasies. Vary sentence length. Use active voice throughout." This normalizes toward a generic centroid that is less uniquely attributable.

☐ **Temporal pattern discipline.** Do not write pseudonymously at the same times you write under your real identity. If real-identity writing happens during business hours on weekdays, pseudonymous writing should happen at different times — or metadata timestamps should be stripped (see `metadata-hygiene` skill, git commit timestamps).

☐ **Code style compartmentalization.** Maintain separate `.editorconfig` and linting rules for pseudonymous repos. Deliberately choose different naming conventions (camelCase vs. snake_case), comment density (verbose vs. minimal), and preferred idioms from real-identity repos.

☐ **Length normalization.** Real-identity writing tends toward consistent lengths (paragraphs, posts, commits). Pseudonymous writing should vary length distributions significantly.

**Tier 3 — High impact, high effort:**

☐ **Obfuscation tools.** Adversarial stylometry tools exist that deliberately modify text to evade attribution:
- `Anonymouth` (research, Java) — authorship obfuscation tool [Brennan et al., 2012]
- `ALETHEA` (research) — adversarial authorship attribution evasion
- Custom LLM rewrite pipeline with explicit stylometric diversity constraints

☐ **Imitation mode.** Write pseudonymously in the style of a known public author. Stylometric tools will attribute the writing to that author rather than you. High effort to maintain; risks becoming distinctive in a different way.

☐ **Compartmentalized AI assistance.** Use a local LLM (Ollama on Umbrel node) to draft pseudonymous writing. The LLM's output will have model-characteristic stylistic patterns rather than your personal fingerprint. Review for content only; don't rewrite substantially in your own voice.

---

### Code Stylometry Specifics

**Highest-risk signals in code:**

```python
# Naming convention (very distinctive)
def process_data():        # snake_case — Python community default
def processData():         # camelCase — Java/JavaScript default
def ProcessData():         # PascalCase — C#/Go method default

# Comment density and style
# Terse: no comments
# Verbose: inline explanation of every decision
# Docstring-only: functions have docstrings, no inline comments

# Abstraction preference
# Functional: map/filter/reduce preferred
# Imperative: explicit loops preferred

# Error handling style
try/except vs. result types vs. assertions

# Import organization: absolute vs. relative, grouped vs. flat
```

**Mitigation:** Define a distinct coding style for pseudonymous repos and enforce it via linter configuration committed to the repo. The style should differ from your real-identity repos on at least three dimensions.

---

### Severity in Pseudonymous Contexts

When the user operates under a pseudonym, escalate all stylometric findings to **HIGH** regardless of other context:

```
STYLOMETRIC RISK ASSESSMENT
Pseudonymous mode: ACTIVE
Risk level: HIGH (automatic escalation)

Findings:
  [1] Writing sample length: [word count] — sufficient for attribution attack
  [2] Em dash usage: [count] — matches real-identity writing pattern
  [3] Sentence length distribution: σ=[value] — check against real-identity baseline
  [4] Code comment density: [ratio] — check against real-identity repos

Recommended actions before publishing:
  → AI-assisted style normalization pass
  → Punctuation audit (suppress em dashes)
  → Timestamp review (metadata-hygiene)
```

---

### References

- Narayanan, A. & Shmatikoff, V. (2008). "Robust de-anonymization of large sparse datasets." *IEEE S&P 2008.*
- Brennan, M., Afroz, S. & Greenstadt, R. (2012). "Adversarial stylometry: Circumventing authorship recognition to preserve privacy and anonymity." *TISSEC.*
- Koppel, M., Schler, J. & Argamon, S. (2011). "Authorship attribution in the wild." *Language Resources and Evaluation.*
- Koppel, M. & Winter, Y. (2014). "Determining if two documents are written by the same author." *JASIST.*
- Neal, L., et al. (2017). "Surveying stylometry techniques and applications." *ACM Computing Surveys.*
