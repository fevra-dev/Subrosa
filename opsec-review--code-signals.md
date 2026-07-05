# Code Signal Patterns

Detailed OPSEC signal patterns for: source code, repositories, logs, stack traces, API payloads, config files, scripts.

---

## Infrastructure Fingerprinting — Code Specifics

### Version strings to flag
```
# Runtime/language versions
"python": "3.11.4"        # Exact patch — flag
"node": ">=20.0.0"        # Range — OK
rustc 1.75.0 (82e1608df 2023-12-21)  # Compiler output in logs — flag

# Library pinning in requirements/lock files
requests==2.31.0          # Exact — flag if public-facing
requests>=2.28.0          # Range — OK

# Docker base images
FROM ubuntu:22.04          # Exact — flag
FROM ubuntu:latest         # Latest — different risk (supply chain)
FROM node:20.11.0-alpine   # Exact + distro — flag

# Tool version output in logs/docs
npm 10.2.4                 # Flag
cargo 1.75.0               # Flag
```

### File paths that fingerprint OS/environment
```
/Users/[name]/             # macOS home dir — reveals OS + username
/home/[name]/              # Linux home dir — reveals username
C:\Users\[name]\           # Windows — reveals OS + username
/opt/homebrew/             # macOS Apple Silicon homebrew
/usr/local/homebrew/       # macOS Intel homebrew
/snap/                     # Ubuntu snap — reveals distro
/nix/store/                # NixOS — reveals distro
~/.config/nvim/            # Neovim config — reveals editor
~/.cargo/                  # Rust toolchain path
/mnt/c/                    # WSL path — reveals Windows + WSL
```

### Cloud/infra identifiers
```
arn:aws:                   # AWS ARN — reveals cloud provider + region
projects/[project-id]/     # GCP project ID
/subscriptions/[guid]/     # Azure subscription
*.s3.amazonaws.com         # S3 bucket name — enumerable
*.blob.core.windows.net    # Azure storage
[name].vercel.app          # Vercel project name
[name].railway.app         # Railway project name
cluster.[name].k8s         # K8s cluster name
*.internal                 # Internal DNS zone
*.local                    # mDNS local network
```

### CI/CD leakage
```
GITHUB_REPOSITORY: org/repo     # Org name in workflow env
CIRCLE_PROJECT_USERNAME         # Org name
runner: self-hosted             # Reveals self-hosted runner (attack target)
[branch-name]                   # Internal branch naming conventions
cache-key: ${{ hashFiles(...) }} # Cache strategy reveals dependency structure
secrets.INTERNAL_TOKEN          # Secret name reveals what credentials exist
```

---

## Organizational Structure — Code Specifics

### Internal identifiers in code
```python
# Variable/function names that reveal internal codenames
PROJECT_HELIOS_API_URL = ...
helios_client = HeliosClient()
LEGACY_TITAN_COMPAT = True       # Reveals old codename

# Internal ticket references in comments
# TODO(PROJ-1234): fix this       # Reveals ticket system + project prefix
# See JIRA-5678 for context       # Reveals JIRA usage

# Internal team/owner annotations
# @team:platform                  # Team structure
# @owner:alice                    # Employee handle
# CODEOWNERS file contents        # Entire org chart of code ownership
```

### Dead code / feature flags
```python
# Reveals planned but unannounced features
FEATURE_FLAG_DARK_MODE = False
ENABLE_NEW_BILLING = os.getenv("BILLING_V2", False)
# TODO: remove after Project Atlas launch
```

---

## Tradecraft Leakage — Code Specifics

### Security tool artifacts
```bash
# Nmap output left in repo
# Nmap 7.94 scan initiated...
# PORT     STATE SERVICE
# 443/tcp  open  https

# SQLmap artifacts
# sqlmap identified the following injection point...

# Nuclei/HTTPX scan remnants in test fixtures
# Burp Suite export files committed
.burp                      # Flag extension in .gitignore absence

# Pentest wordlists
rockyou.txt
common-passwords.txt
```

### Monitoring/detection surface
```python
# Reveals what you're alerting on (and what you're not)
ALERT_THRESHOLD_FAILED_LOGINS = 10   # Attacker knows: 9 attempts is safe
RATE_LIMIT_REQUESTS_PER_MINUTE = 60  # Reveals rate limit
MAX_UPLOAD_SIZE_MB = 50              # Attack planning

# Log levels that reveal what's captured
logging.DEBUG   # in production — reveals verbose logging posture
# vs
logging.ERROR   # Only errors — reveals gaps in detection
```

### Auth flow details
```python
SESSION_EXPIRY_HOURS = 24            # Session duration revealed
TOKEN_ROTATION_DAYS = 90             # Token lifetime revealed
MFA_BYPASS_CODES = [...]             # Never commit
ADMIN_OVERRIDE_KEY = ...             # Never commit
```

---

## Dependency & Supply Chain — Code Specifics

### Private registry leakage
```
# .npmrc or pip.conf revealing internal registry
registry=https://npm.internal.company.com/
--extra-index-url https://pypi.internal.company.com/

# Package names that reveal internal packages
@company/internal-auth
company-internal-utils
```

### Dependency confusion targets
```
# Private package names in package.json that aren't on public npm
# If an internal package name is exposed, adversary can register it on npm
# and wait for developers to pull it
"dependencies": {
  "@acme/auth-helpers": "^1.0.0",    # Is this on public npm? Flag for check.
}
```

---

## Logs & Stack Traces

### High-value signals in log dumps
```
# Absolute paths reveal environment
File "/home/ubuntu/app/src/auth.py", line 42

# Database connection strings
postgresql://user:pass@db.internal:5432/prod  # Full connection string

# Internal service names in stack traces
at com.company.internal.AuthService.validate()

# Request IDs that reveal internal routing
X-Request-ID: gw-prod-us-east-1-abc123   # Reveals infra topology

# User/session IDs in error context
user_id=12345, session=abc...             # PII in logs

# Timing information
Took 2340ms — db query 2200ms            # Reveals db performance = attack surface
```

---

## API Payloads & Schemas

### What schemas reveal
```json
{
  "internal_user_id": "...",      // Internal ID format exposed
  "legacy_account_ref": "...",    // Reveals legacy system exists
  "feature_flags": {              // Reveals feature flag system
    "new_dashboard": false
  },
  "debug_info": { ... },          // Debug fields in prod payload
  "_metadata": {
    "service": "user-service-v2", // Internal service name
    "region": "us-east-1"         // Cloud region
  }
}
```
