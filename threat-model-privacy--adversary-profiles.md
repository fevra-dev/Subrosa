# Adversary Profiles

Archetype library for common privacy threat actors. Use to seed Phase 2 adversary profiling. Real adversaries are composites — mix and match as needed.

---

## Archetype 1: Mass Credential Harvester

**Profile:** Criminal organization or botnet operator running automated campaigns at scale.

**Motivation:** Financial — credential resale, account takeover for fraud, ransomware delivery.

**Capability:** CRIMINAL ORG — purchased exploit kits, credential stuffing infrastructure, phishing-as-a-service.

**Access:** Remote only. No targeting — purely opportunistic.

**Persistence:** Opportunistic. If initial access fails, moves on immediately.

**Primary TTPs:**
- Credential stuffing against reused passwords
- Phishing lures (fake invoices, delivery notifications, account warnings)
- Malvertising and drive-by download
- Purchased breach datasets from dark web markets

**Typical targets:** Anyone with reused passwords, email accounts, financial accounts, crypto wallets.

**Indicators of targeting:**
- Failed login attempts from unusual IPs
- Phishing emails with your email address
- Account recovery emails you didn't request

**Falsifier:** Not a plausible adversary if you use unique passwords and MFA everywhere.

---

## Archetype 2: OSINT Aggregator / Dossier Builder

**Profile:** Individual or small group building a profile for deanonymization, doxxing, social engineering, or stalking. Non-technical but OSINT-proficient.

**Motivation:** Variable — harassment, competitive intelligence, social engineering setup, stalking.

**Capability:** ADVANCED INDIVIDUAL (social) — no technical exploits but methodical aggregation of public sources.

**Access:** Remote only via public sources. May attempt to socially engineer access to restricted sources.

**Persistence:** Sustained campaign — may spend weeks building a profile before acting.

**Primary TTPs:**
- Cross-platform username correlation
- Reverse image search
- Social graph mapping (mutual connections, tagged photos)
- LinkedIn / GitHub / Twitter cross-referencing
- Data broker queries (Spokeo, BeenVerified, etc.)
- WHOIS / domain registration history
- Wayback Machine for deleted content
- Metadata extraction from uploaded files (EXIF, PDF metadata)

**Typical targets:** Public figures, security researchers, activists, pseudonymous individuals, anyone involved in controversy.

**Indicators of targeting:**
- Sudden follow/connection requests from unknown accounts
- DMs probing for personal information
- Old content resurfacing in unexpected places
- Fake "recruiter" outreach seeking personal details

**Falsifier:** Not a plausible adversary if you have no public profile and no reason to be targeted.

---

## Archetype 3: Crypto-Targeted Attacker

**Profile:** Individual or small group specializing in cryptocurrency theft. Technical and patient.

**Motivation:** Financial — direct theft of crypto assets.

**Capability:** ADVANCED INDIVIDUAL — phishing infrastructure, clipboard hijackers, fake wallet apps, social engineering against exchange support.

**Access:** Remote. May attempt SIM swap for MFA bypass.

**Persistence:** Sustained — will monitor targets and wait for operational security mistakes.

**Primary TTPs:**
- Spearphishing with fake wallet apps, exchange phishing pages
- Clipboard hijacker malware (replaces copied wallet addresses)
- SIM swap against phone number used for MFA
- Discord / Telegram impersonation of trusted contacts ("I need to send you funds, what's your address?")
- Fake job offers with malicious "skill test" code (steals env files, wallet keys)
- Compromising browser extensions (MetaMask, etc.)
- Targeting seed phrase backup locations (cloud storage, photos, notes apps)
- Discord nitro scams, NFT "collaboration" scams as initial social engineering

**Typical targets:** Anyone publicly active in crypto/Web3 communities, NFT creators and collectors, DeFi users, exchange employees.

**Indicators of targeting:**
- Unexpected DMs with "investment opportunities" or "collaboration"
- Requests to try a new wallet app or browser extension
- Fake support tickets from exchanges you use
- Code review requests containing obfuscated scripts

**Falsifier:** Not a plausible adversary if you have no publicly known crypto holdings and no Web3 social footprint.

---

## Archetype 4: Targeted Harassment Campaign

**Profile:** Individual or coordinated group (often chan-adjacent) targeting someone for sustained harassment.

**Motivation:** Ideological, personal grievance, or coordinated pile-on.

**Capability:** ADVANCED INDIVIDUAL (social) + SCRIPT KIDDIE (technical) — primarily social and platform-level tactics.

**Access:** Remote via platforms. May have insider access if campaign involves people who know the target.

**Persistence:** Variable — can be a brief coordinated spike or a years-long campaign.

**Primary TTPs:**
- Mass reporting to platforms (account suspension)
- Doxxing and amplification of personal information
- Coordinated negative reviews, complaints to employers
- Impersonation accounts
- Email/SMS bombing
- False legal complaints and DMCA abuse
- SWATting (in extreme cases)

**Typical targets:** Women in tech/gaming, security researchers who've published offensive research, journalists, political figures, anyone who "went viral" negatively.

**Indicators of targeting:**
- Sudden influx of hostile messages from unknown accounts
- Platform account warnings or temporary suspensions
- Employer receiving complaints about you
- Personal information appearing in hostile forums

**Falsifier:** Not a plausible adversary without a recent triggering event (controversial post, public dispute, etc.).

---

## Archetype 5: Insider / Trusted Relationship Adversary

**Profile:** Current or former employer, partner, family member, or close contact with existing access.

**Motivation:** Variable — control, revenge, financial, competitive.

**Capability:** SOCIAL + partial ADVANCED INDIVIDUAL — has legitimate access to some assets, may have technical skills.

**Access:** INSIDER — has or had physical and/or account access. Knows operational patterns and routines.

**Persistence:** Variable but often long-duration with patient observation.

**Primary TTPs:**
- Abuse of shared accounts (cloud storage, email, social)
- Device access (installing stalkerware, cloning credentials)
- Social engineering mutual contacts
- Legal compulsion (family court, employment law)
- Shared financial access as leverage
- Knowledge of security habits (can guess passwords, knows backup locations)

**Note for coercive control context:** This adversary profile requires elevated threat assessment. Their capability is often underestimated because it's relational rather than technical. Physical safety considerations supersede all technical controls.

**Indicators of targeting:**
- Account activity during times you weren't logged in
- Contacts behaving strangely (may have been contacted)
- Devices behaving unexpectedly
- Information appearing in conversations that you only stored digitally

---

## Archetype 6: Institutional / Legal Adversary

**Profile:** Government agency, regulator, law firm, or corporation using legal compulsion tools.

**Motivation:** Legal — regulatory compliance, litigation discovery, criminal investigation, asset seizure.

**Capability:** INSTITUTIONAL — subpoena power, legal compulsion, third-party data access, forensic capability.

**Access:** Remote via legal compulsion of providers. May include physical search/seizure.

**Persistence:** Long-duration, methodical.

**Primary TTPs:**
- Subpoena of cloud providers (email, storage, messaging)
- Subpoena of financial institutions
- Legal compulsion of platform providers (social media, exchanges)
- Device seizure and forensic analysis
- Network-level traffic analysis via ISP compulsion
- International mutual legal assistance (MLAT) for cross-border cases

**Jurisdiction matters enormously.** A Canadian-resident target has different exposure than a US-resident, different again from an EU resident. Data stored in a different jurisdiction than the adversary's authority creates friction but not immunity.

**Falsifier:** Not a plausible adversary without reason to believe legal action or regulatory scrutiny is possible.

---

## Archetype 7: Nation-State / Advanced Persistent Threat

**Profile:** State intelligence agency or state-sponsored threat group.

**Motivation:** Espionage, sabotage, influence operations, economic theft.

**Capability:** NATION-STATE — zero-days, supply chain compromise, physical options, signals intelligence.

**Access:** Remote and potentially physical. Long-term access to infrastructure at provider level.

**Persistence:** Long-term, patient, often years.

**Primary TTPs:**
- Supply chain compromise (tooling, dependencies, hardware)
- Zero-day exploitation of devices and software
- Watering hole attacks against communities target frequents
- HUMINT (human intelligence — cultivating relationships)
- Signals intelligence (metadata even from encrypted communications)
- Physical access to devices (border crossings, hotel rooms)

**Typical targets:** Government officials, defense contractors, critical infrastructure operators, journalists covering state activities, dissidents, high-value IP holders.

**Calibration note:** Most individuals are NOT nation-state targets. Inflating this adversary into every threat model is poor analytic discipline. Apply only with specific reason to believe state interest exists.

**Falsifier:** Not a plausible adversary without specific evidence of state interest (e.g., involvement in national security topics, critical infrastructure, political opposition in an authoritarian state).

---

## Deanonymization Adversaries (Pseudonym-Specific)

For users maintaining pseudonym/real-identity separation, these specialized adversaries apply:

**Identity Researcher (Academic/Journalistic)**
- Goal: identify real person behind pseudonym for publication
- Capability: OSINT-proficient, stylometric analysis, social graph mapping
- Not malicious by default but outcome can be harmful

**Platform Enforcement**
- Goal: link pseudonym to real identity for ToS enforcement
- Capability: Device fingerprinting, IP logging, payment records, behavioral analysis
- Has access to platform-level data not available to public

**Hostile Community Investigator**
- Goal: deanonymize for targeted harassment
- Capability: Coordinated OSINT, social engineering of mutual contacts
- Often chan-adjacent communities with dedicated investigation channels

**Key deanonymization vectors:**
- Writing style (vocabulary, phrasing, punctuation, error patterns)
- Temporal patterns (when you post vs. when real identity is active)
- Topic overlap (interests that narrow the candidate population)
- Technical artifacts (same IP, same device fingerprint, same PGP key)
- Social graph overlap (mutual followers/connections)
- Metadata in uploaded files
- Payment records (if pseudonym involves financial transactions)

---

## Archetype 8: Malicious or Compromised MCP Server / Supply Chain Tool

**Profile:** A third-party tool, MCP server, npm/pip package, or LLM plugin that either was designed maliciously or has been compromised post-release. Has privileged access to agent context windows, tool call parameters, and output pipelines.

**Motivation:** Data exfiltration, credential theft, persistent access, behavioral profiling, lateral movement to connected systems.

**Capability:** INSIDER (functional) + ADVANCED INDIVIDUAL (technical). The tool has legitimate, granted access to data it shouldn't retain or exfiltrate. Operates inside the trust perimeter.

**Access:** INSIDER — tool call parameters, context window contents, agent memory reads/writes, external API credentials passed through the agent.

**Persistence:** Continuous — present in every agent interaction where the tool is invoked.

**Primary TTPs:**

*Exfiltration via tool call parameters:*
A malicious MCP server logs all parameters passed to it — including personal data, credentials, wallet addresses, session tokens embedded in tool calls. These are transmitted to adversary infrastructure.

*Memory poisoning (MINJA-II, environmental injection):*
Tool responses contain adversarial content designed to be written to agent memory — injecting false facts, malicious instructions, or data collection directives that persist across sessions.

*Credential harvesting:*
Agent passes API keys, OAuth tokens, or session cookies to tool for legitimate use. Malicious tool captures and exfiltrates credentials for separate use.

*Context window exfiltration:*
Tool receives context window contents as part of its invocation. For LLMs-as-tools (sub-agent calls), the entire prior conversation may be passed. A malicious sub-agent captures and exfiltrates this.

*Timing-based behavioral profiling:*
Malicious tool logs invocation timestamps and parameter patterns to build a behavioral profile of the user or system — even without capturing plaintext content.

*Dependency confusion / typosquatting:*
For locally installed tools (npm packages, pip packages, CLI tools), adversary publishes a malicious package with a similar name to a legitimate private package. Developer installs it inadvertently; malicious code runs with developer-level access.

**Typical targets:** Any system using third-party MCP servers, npm/pip packages, browser extensions, LLM plugins, or sub-agent APIs. High-value targets: crypto wallets (Kyma, Seed Vault interaction), API key stores, health data pipelines, security tooling (Delegate Scout scanner).

**Real-world precedents:**
- npm `event-stream` compromise (2018) — targeted cryptocurrency wallet
- `xz-utils` backdoor (2024) — sophisticated supply chain attack on SSH
- PyPI malicious packages targeting AWS credentials (multiple, 2022-2024)
- Malicious VS Code extensions with keylogging capability

**Indicators of targeting:**
- Unexpected network requests from tool processes to unknown hosts
- Agent memory entries with unusual provenance tags (sourced from tool responses rather than user input)
- Credentials used from locations inconsistent with normal access patterns
- Tool invocation frequency anomalies

**Mitigations:**
- Vet all MCP servers before integration — treat as data processors (require documented data handling practices)
- Pin dependency versions; verify checksums; use lockfiles
- Tool call parameter minimization (TC-2 from portfolio paper) — pass only what the tool requires
- Namespace-isolated agent memory — tool responses tagged with provenance; restricted from writing to user-context memory without policy authorization
- Monitor MCP server network egress
- Separate agent identity for tool calls from agent identity for user interactions
- Do not pass API keys or credentials in tool call parameters — use server-side credential injection where possible

**Falsifier:** Not a plausible adversary if all tools are self-hosted, open-source with verified checksums, and no third-party tool has access to sensitive parameters.

**Elevated risk contexts:** OpenClaw fleet (MCP-native architecture, multiple third-party tools), Kyma (MWA/MCP tool interactions with Seed Vault), any agent system with external tool integrations.
