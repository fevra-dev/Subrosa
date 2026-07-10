# Git Metadata Hygiene

Identity hygiene, history rewriting, and secret removal for git repositories.

---

## What Git Embeds

Every commit records:
- Author name
- Author email
- Committer name (may differ from author in rebased/squashed commits)
- Committer email
- Timestamp with timezone offset (reveals locale)
- Commit message (may contain internal refs, codenames, ticket IDs)
- Parent commit hash (immutable history linkage)

The `.git/config` file records remote URLs, which may include:
- GitHub/GitLab org names
- Internal Gitlab instance hostnames
- SSH key aliases that reveal identity

---

## Pre-flight Checklist Before First Push

Run before any public push. Non-recoverable once history is pushed and forked.

```bash
# Check current identity
git config user.name
git config user.email
git config --global user.name
git config --global user.email

# Audit all unique author identities in history
git log --format="%an <%ae>" | sort -u

# Audit all committer identities
git log --format="%cn <%ce>" | sort -u

# Check for secrets in history (basic)
git log -p | grep -iE "(password|secret|api_key|token|private_key|BEGIN.*KEY)"

# Check for large files that might be accidentally committed keys
git log --all --stat | grep -v "^$" | grep "|" | awk '{print $1}' | sort | uniq -c | sort -rn | head -20
```

---

## Per-Repo Identity Override

For pseudonymous repositories, always set identity at the repo level:

```bash
# Set per-repo (overrides global)
cd /path/to/repo
git config user.name "your-pseudonym"
git config user.email "pseudonym@proton.me"

# Verify
git config --local user.name
git config --local user.email
```

**Set before the first commit.** History rewriting after push is disruptive.

---

## Rewriting History: git-filter-repo (Preferred)

`git-filter-repo` is the modern replacement for `git filter-branch`. Faster, safer, more powerful.

```bash
# Install
pip install git-filter-repo

# Replace author identity using mailmap file
# Create mailmap.txt:
# New Name <new@email.com> <old@email.com>
# New Name <new@email.com> Old Name <old@email.com>
git filter-repo --mailmap mailmap.txt

# Replace a specific string everywhere in history
git filter-repo --replace-text <(echo "real_name==>pseudonym")

# Remove a file from all history (accidentally committed secret)
git filter-repo --path secrets.env --invert-paths
git filter-repo --path .env --invert-paths

# Remove a directory from all history
git filter-repo --path internal-docs/ --invert-paths

# Replace a string in commit messages
git filter-repo --message-callback '
    return message.replace(b"PROJ-", b"TASK-")
'
```

**Warning:** filter-repo rewrites all commit hashes. Anyone who forked before the rewrite has the old history. If already public, coordinate with all forks or accept that old history persists externally.

---

## Removing Accidentally Committed Secrets

If a secret was committed, the threat is that it exists in git history even after deletion. Required steps:

```bash
# Step 1: Rotate the secret IMMEDIATELY
# Don't wait — assume it was scraped by automated scanners (GitHub secret scanning, truffleHog bots)
# Rotation takes priority over history cleaning

# Step 2: Remove from history with filter-repo
git filter-repo --path-glob '*.env' --invert-paths
git filter-repo --path secrets.json --invert-paths

# Step 3: For inline secrets in code files — replace text
git filter-repo --replace-text <(echo "sk-ant-realkey==>sk-ant-REDACTED")

# Step 4: Force push all branches
git push origin --force --all
git push origin --force --tags

# Step 5: Request cache purge from GitHub (if GitHub hosted)
# GitHub support → "cached views" of deleted content
# GitHub secret scanning will auto-revoke some token types

# Step 6: Verify removal
git log -p | grep "sk-ant-realkey"
# Should return nothing
```

---

## Timezone Leakage in Commits

Git commit timestamps include the committer's local timezone offset:

```
Date:   Mon Jan 15 14:32:11 2024 -0500
```

The `-0500` reveals EST/EDT (US East / Canada East). For pseudonymous work, this narrows the candidate population geographically.

**Mitigation — commit in UTC:**
```bash
# Per-invocation or permanent: run git under UTC — both author and
# committer timestamps then record +0000
TZ=UTC git commit -m "message"

# Or export for the whole session
export TZ=UTC
```
Git has no built-in "always UTC" config — the TZ environment variable is the mechanism.

**Rewrite existing timestamp offsets to UTC** (filter-repo exposes dates as raw
bytes `b"<epoch> <offset>"` — not datetime objects):
```bash
git filter-repo --commit-callback '
    commit.author_date = commit.author_date.split(b" ")[0] + b" +0000"
    commit.committer_date = commit.committer_date.split(b" ")[0] + b" +0000"
'
```
Note: this normalizes the *offset* (the locale leak); the epoch instant is unchanged, so activity-hour patterns still show in UTC terms — batching or date-fuzzing is the mitigation if work-hour inference matters.

---

## Commit Message Hygiene

Commit messages are permanent and public. Audit before pushing:

```bash
# Review all commit messages
git log --oneline

# Search for internal references
git log --oneline | grep -iE "(PROJ|JIRA|TICKET|internal|confidential|codename)"

# Rewrite messages with filter-repo
git filter-repo --message-callback '
    import re
    message = re.sub(b"PROJ-\d+", b"", message)
    return message
'
```

---

## .gitignore Pre-flight

Common files that should never be committed:

```gitignore
# Secrets and credentials
.env
.env.*
*.pem
*.key
*.p12
*.pfx
id_rsa
id_ed25519
secrets.json
credentials.json
serviceAccountKey.json

# Build artifacts with embedded paths
*.dSYM/
*.map
*.d

# IDE files with developer info
.idea/
*.xcuserstate
*.xcworkspace/xcuserdata/

# OS metadata
.DS_Store
Thumbs.db
desktop.ini

# Solana / crypto
*.json  # Be careful — may contain keypairs
target/  # Rust build artifacts

# Tool output
*.log
npm-debug.log*
```
