# Social Media & Public Communication Signal Patterns

OPSEC signal patterns for: LinkedIn, Twitter/X, Mastodon, Discord, Telegram, GitHub profiles, blog posts, conference talks, podcast appearances, and any public-facing communication.

---

## LinkedIn Signals

### Profile-level leakage
```
Full name + employer + role + location:
  → Sufficient for physical targeting, social engineering, and doxxing
  → "Senior Security Engineer at [Company], San Francisco" narrows to
     a small population; salary inference possible via Glassdoor/levels.fyi

Connections count + mutual connections:
  → Social graph density; who you know; org chart inference

Skills & endorsements:
  → Complete tech stack inventory; attack surface for targeted spearphishing
  → "Endorsed for Kubernetes, Terraform, AWS" tells an attacker exactly
     what to weaponize in a phishing email

Featured section / media:
  → Talks, demos, repos — may reveal internal tooling, unreleased projects,
     infrastructure details in presentation screenshots

Activity feed (likes, comments, shares):
  → Reveals opinions, connections, interests, work hours, timezone
  → Pattern of engaging with certain companies = acquisition target signal
    or job search signal

"Open to work" banner:
  → Job searching; financial stress possible; social engineering window

Education:
  → Graduation year → age inference
  → School + major + year → cross-referencing against alumni networks

Volunteer / causes:
  → Political / ideological signals; targeting surface
```

### Post content signals
```
"Just shipped X" → reveals production timeline, what's live, what's next
"We're hiring for Y" → reveals team gaps, missing security roles
"Excited to announce Z partnership" → reveals relationships before PR
"Great meeting with [Name] at [Company]" → business relationship graph
Office/event photos → physical location on specific date
Screenshot of code/dashboard → version strings, internal tooling, data
```

---

## Twitter / X Signals

### Profile signals
```
Handle history:
  → Previous handles visible via third-party tools (e.g. Wayback Machine,
     handle history scrapers) — links current identity to past identities

Pinned tweet:
  → Current priority / project / announcement — often reveals sensitive timing

Following list:
  → Who you follow = interest graph; reveals company strategy, job search,
     personal interests, political views

Follower list:
  → Who follows you = social graph; reveals peers, clients, competitors

Muted words / blocked users:
  → Not public, but inferred from response patterns

Lists membership:
  → Being added to a "Security Researchers" or "Fintech CTOs" list
     confirms identity and role to list creator
```

### Tweet content analysis
```
Temporal patterns:
  → Tweet timing → timezone → location inference
  → Burst of tweets at 3am local = insomnia, incident, travel
  → Regular posting cadence broken = travel, incident, stress

Hashtag usage:
  → Consistent use of conference hashtags → attendance confirmation
     → physical location on specific dates

Reply graph:
  → Who you reply to = social graph; private relationships become visible
  → DMs visible only to parties, but existence inferred from reply patterns

Quote tweets of internal matters:
  → Employees quoting company announcements before they're public
  → Team members reacting to each other → org chart inference

Location tags / geotagged media:
  → Physical location; home neighborhood inference from recurring locations
```

---

## GitHub Profile Signals

### Profile-level
```
Contribution graph:
  → Work hours by day and time → timezone → location
  → Gaps in contribution → vacation, illness, sabbatical, job change
  → Spike in contributions → crunch, project deadline, new job

Repository names:
  → Internal codenames (if pushed without sanitization)
  → Client names in repo names
  → Tech stack fingerprinting from repo language breakdown

Starred repositories:
  → Interest graph; reveals what you're researching or planning to use
  → Starring security research tools → confirms security role

Followers / following:
  → Professional social graph; peer network

Organization membership (public):
  → Employer confirmation even if not on LinkedIn
  → Client relationships if consulting
```

### Commit-level (see also doc-signals.md git section)
```
Author email in commits:
  → Real email address even under pseudonymous handle
  → Internal email domain confirms employer

Commit message content:
  → Internal ticket references (JIRA-1234, GH-5678)
  → Internal codenames
  → Personnel names in co-author lines

Commit timestamps:
  → Work hours, timezone — see doc-signals.md

README content:
  → Stack fingerprinting, internal URLs, dependency versions
  → See doc-signals.md for full README signal analysis
```

---

## Discord / Slack / Telegram Signals

### Server membership (Discord)
```
Public server membership:
  → Communities = interests, affiliations, identity signals
  → Being in a specific crypto project's Discord = holder/developer signal
  → NFT project server membership = investment/affiliation

Username consistency:
  → Same handle across Discord, Twitter, GitHub → trivial correlation
  → Avatar reuse → reverse image search linkage

Status / activity:
  → Custom status reveals current project, mood, location
  → "In a meeting" / "Coding" / "Away in [city]"
```

### Message content
```
Server-specific channels:
  → What channels you post in = specific interests
  → Posting in #job-board = looking for work signal
  → Posting in #help channels = skill gaps / current challenges

Timing:
  → Same temporal correlation as Twitter — when you're online

DM patterns:
  → Not public but inferred from response speed and context
```

---

## Conference / Talk Signals

**Highest-density OPSEC surface for security researchers.**

### Talk content signals
```
Demo infrastructure:
  → Screenshots/live demos showing: cloud console, internal tooling,
     production data (even if blurred), version strings, URL structures

Slide content:
  → Architecture diagrams revealing internal system design
  → Team size / structure in org chart slides
  → Client names in case studies
  → Budget/timeline signals in project slides
  → Photo backgrounds with identifiable locations

Speaker bio:
  → Exact employer + role + location + seniority
  → Previously held roles → career trajectory inference

Q&A session:
  → Unrehearsed answers can reveal more than prepared slides
  → Specific technical questions answered → reveals deeper knowledge
     of a topic than the talk itself (unreleased research, internal tools)
```

### Attendance signals
```
Conference badge photos:
  → Name, employer, role — often full-resolution and publicly posted
  → Badge ribbons reveal: speaker, sponsor, staff, press, VIP

Check-in posts:
  → Physical location on specific dates
  → "Excited to be at [conference]!" → confirmed attendance

Group photos:
  → Social graph: who you associate with professionally
  → Physical appearance confirmation for facial recognition

Networking posts:
  → "Great meeting [Name] from [Company]!" → business relationship graph
  → Business card sharing → contact details in third-party databases
```

---

## Podcast / Interview Signals

```
Background analysis:
  → Bookshelves → titles → interests, beliefs, education
  → Art/decor → geographic region, tastes
  → Window light direction → home location inference (sun angle by time)
  → Equipment brands → financial status inference

Offhand mentions:
  → "My co-founder" → reveals business structure
  → "We just moved our infrastructure to..." → vendor relationship
  → "We're probably going to announce..." → unreleased information

Voice characteristics:
  → Accent → geographic origin
  → Vocal patterns → under stress indicators (useful for social engineering)
```

---

## Cross-Platform Correlation

The most dangerous OPSEC failure is not any single platform — it is the correlation of signals across platforms.

### Linkage vectors by type

| Signal | Platform A | Platform B | Correlation method |
|---|---|---|---|
| Username | GitHub: `dev-alice` | Twitter: `dev_alice` | Trivial string match |
| Avatar | LinkedIn photo | Twitter avatar | Reverse image search |
| Writing style | Blog posts | Reddit comments | Stylometric analysis |
| Post timing | Twitter activity | Discord activity | Timezone + schedule correlation |
| Technical interests | GitHub stars | Twitter follows | Topic overlap |
| Social graph | LinkedIn connections | Twitter following | Mutual contacts |
| Email | Git commits | HaveIBeenPwned | Breach database |
| IP address | Forum posts | VPN logs | ISP-level correlation |
| Device fingerprint | Login from browser A | Login from browser B | Same fingerprint |

### Aggregation attack pattern

An adversary building a dossier doesn't need any single piece of identifying information. They aggregate:

```
Step 1: Find GitHub handle via technical blog post
Step 2: GitHub profile → employer (org membership)
Step 3: LinkedIn search for [handle] at [employer] → real name
Step 4: Real name → alumni database → home city
Step 5: Twitter handle (same as GitHub) → tweet timing → timezone confirmed
Step 6: Conference photo (tagged with real name on LinkedIn) → face
Step 7: Voiceprint from podcast → confirmation
Step 8: HaveIBeenPwned for email found in git commits → password database

Time required: 20-40 minutes for a skilled OSINT researcher
```

**Defense:** Break the chain at the weakest link. Username consistency is usually the easiest link to sever and provides the most protection for pseudonymous operators.

---

## Severity Escalation — Pseudonymous Mode

When reviewing social media / public content for a pseudonymous operator:

- Any username or handle consistent with real-identity platforms → **CRITICAL**
- Any avatar used on real-identity platforms → **CRITICAL**
- Writing style matching real-identity samples (without deliberate variation) → **HIGH**
- Post timing overlapping with real-identity active hours → **HIGH**
- Technical interests consistent with real-identity GitHub/blog → **HIGH**
- Any mutual follower/connection with real-identity accounts → **MEDIUM**
- Conference attendance under pseudonym while real identity also attended → **HIGH**

Run `doc-signals.md` stylometric analysis alongside this checklist for any pseudonymous social content review.
