---
name: metadata-hygiene
description: Audits and cleans metadata embedded in files before sharing — EXIF in images, author/revision history in documents, GPS in videos/audio, git config real names, archive internal paths, and binary file headers. Use when user says "strip metadata", "clean this file before sharing", "remove EXIF", "scrub this doc", "anonymize this file", "what metadata does this have", "git history cleanup", "remove my name from this", or when preparing any file for external distribution. Operationally distinct from redact (text content) and opsec-review (inference audit) — this skill handles embedded binary and structured metadata in files, not document text.
---

# Metadata Hygiene

Audit and cleaning guidance for embedded metadata in files before external sharing. Covers binary file headers, document properties, version history, geolocation data, device identifiers, and version control artifacts.

**Composable with:**
- `opsec-review` — identifies metadata as a finding; this skill executes the cleaning
- `redact` — handles text content PII; this skill handles embedded file metadata

---

## File Type Coverage

| File type | Primary metadata risks | Reference section |
|---|---|---|
| Images (JPEG, PNG, TIFF, HEIC, WebP) | GPS coordinates, device model, timestamp, author | `references/image-metadata.md` |
| PDF | Author, company, software, creation date, revision history, comments, embedded fonts with license info | `references/document-metadata.md` |
| DOCX / XLSX / PPTX (Office) | Author, last modified by, company, revision history, tracked changes, comments, template path | `references/document-metadata.md` |
| Audio (MP3, FLAC, M4A, WAV) | GPS (phone recordings), device ID, recording software, embedded artwork with its own EXIF | `references/av-metadata.md` |
| Video (MP4, MOV, MKV) | GPS coordinates, device model, recording software, creation timestamp, chapter markers | `references/av-metadata.md` |
| Archives (ZIP, TAR, 7z) | Internal file paths revealing directory structure, creation timestamps, OS identifiers | `references/archive-metadata.md` |
| Git repositories | Real name in commit history, email in commits, internal branch names, accidentally committed secrets | `references/git-metadata.md` |
| Code files | Author in file headers, internal paths in stack traces, debug build artifacts | Inline guidance below |
| Compiled binaries | Compilation paths revealing developer username and directory structure, debug symbols | Inline guidance below |

---

## Metadata Risk Taxonomy

### Tier 1 — Location & Physical Safety (Always strip)
- GPS coordinates (latitude, longitude, altitude) in any file type
- Cell tower / WiFi positioning data
- Location-tagged audio/video

**Risk:** Reveals home address, workplace, regular locations, travel patterns. Physical safety risk for high-threat contexts.

### Tier 2 — Identity & Attribution (Strip for pseudonymous or sensitive sharing)
- Real name in document author fields
- Email address in document properties or git config
- Username in file paths (e.g. `/Users/realname/`, `/home/realname/`)
- Account identifiers embedded in Office documents

**Risk:** Breaks pseudonymous separation; links content to real identity; enables OSINT correlation.

### Tier 3 — Device & Environment Fingerprinting (Strip before security research publication)
- Device make and model (camera model, phone model)
- OS version used to create the file
- Software version used (Adobe Photoshop CC 2024, Microsoft Word 16.x)
- Compilation toolchain version in binaries
- Screen resolution / DPI in document properties

**Risk:** Fingerprints your setup; enables CVE correlation; assists targeted spearphishing.

### Tier 4 — Temporal Signals (Context-dependent)
- Precise creation timestamp
- Modification timestamp history (multiple revisions visible)
- Print timestamps in PDFs
- Recording start/stop times in audio/video

**Risk:** Temporal correlation; reveals work patterns and timezone; can undermine alibi in sensitive contexts.

### Tier 5 — Organizational Signals (Strip before external sharing)
- Company name in Office document properties
- Template path revealing internal file server paths
- Revision history showing internal codenames, colleagues' names
- Tracked changes with internal comments

**Risk:** Organizational intelligence; internal structure leakage; third-party relationship exposure.

---

## Workflow

### Step 1 — Identify file type and sharing context

Ask or infer:
1. What is the file type?
2. Where is it going? (public post, client email, GitHub, security research publication, etc.)
3. What sensitivity context? (personal, pseudonymous, operational security critical)
4. Is this a single file or a batch?

Higher sharing sensitivity → strip all tiers. Lower sensitivity → strip Tier 1-2 minimum.

### Step 2 — Metadata inventory

Before stripping, inventory what is present. Different for each file type — load the appropriate reference. Produce a summary:

```
FILE METADATA INVENTORY
────────────────────────────────
File: photo_2024-01-15.jpg
Type: JPEG with Exif 2.3

[T1 — LOCATION]
  GPS Latitude:      43.6532° N
  GPS Longitude:     79.3832° W   ← Toronto area
  GPS Altitude:      76m

[T2 — IDENTITY]
  Author:            [real name]
  Artist:            [real name]

[T3 — DEVICE]
  Make:              Apple
  Model:             iPhone 14 Pro
  Software:          17.2.1

[T4 — TEMPORAL]
  DateTimeOriginal:  2024:01:15 14:32:11
  CreateDate:        2024:01:15 14:32:11

[T5 — ORGANIZATIONAL]
  (none)

Recommendation: Strip ALL tiers before sharing. GPS alone is physical safety risk.
```

### Step 3 — Cleaning instructions

Provide exact tool commands for the user's environment. Always provide:
1. The primary recommended tool
2. A verification command to confirm stripping worked
3. A warning if the file type has metadata that cannot be fully stripped

### Step 4 — Verification

Never skip verification. Metadata stripping tools have known limitations per file type. Confirm clean:

```bash
# Verify EXIF removed from JPEG
exiftool output.jpg | grep -E "GPS|Author|Artist|Make|Model"
# Should return nothing

# Verify PDF metadata cleared
exiftool output.pdf | grep -E "Author|Creator|Producer|Company"
# Should return nothing or only desired values
```

### Step 5 — Residual risk statement

Some metadata cannot be removed without degrading the file:
- JPEG quality settings reveal approximate compression level (minor)
- PDF font embedding reveals which fonts were used (minor)
- Certain proprietary formats re-embed metadata on save (flag explicitly)

State what residual metadata remains after cleaning and whether it poses material risk.

---

## Tool Reference (Quick)

### ExifTool (images, audio, video, PDF, documents — universal)
```bash
# Inventory all metadata
exiftool filename.jpg

# Strip ALL metadata (creates filename_original backup)
exiftool -all= filename.jpg

# Strip ALL, overwrite in place (no backup)
exiftool -all= -overwrite_original filename.jpg

# Strip ALL from entire directory (add -r to recurse into subdirectories)
exiftool -all= -overwrite_original -r /path/to/dir/

# Strip only GPS
exiftool -GPS:all= filename.jpg

# Strip specific fields
exiftool -Author= -Artist= -Copyright= filename.jpg

# Strip everything, then set a copyright string (order matters: -all= runs first)
exiftool -all= -copyright="Your Name" filename.jpg

# Strip everything but keep the ICC color profile (bare -all= removes it,
# which can visibly shift colors)
exiftool -all= --icc_profile:all filename.jpg
```

### mat2 (privacy-focused, Linux/macOS)
```bash
# Audit metadata
mat2 --show filename.pdf

# Strip metadata
mat2 filename.pdf
# Outputs: filename.cleaned.pdf

# Verify the cleaned output (mat2 has no --check flag; verify by showing)
mat2 --show filename.cleaned.pdf

# Lighter-touch cleaning that preserves more file integrity
mat2 --lightweight filename.pdf
```

### ImageMagick (images — strip and convert)
```bash
# Strip metadata on convert
convert input.jpg -strip output.jpg

# For PNG specifically (also strips tEXt chunks)
convert input.png -strip output.png
```

### LibreOffice (documents — via command line)
```bash
# Open and re-save strips most dynamic metadata
libreoffice --headless --convert-to docx filename.docx
# Note: author name comes from LibreOffice user settings — set to pseudonym first
```

### Git (version control metadata)
```bash
# Check current git config identity
git config user.name
git config user.email

# Set per-repo (override global for pseudonymous repos)
git config user.name "pseudonym"
git config user.email "pseudonym@example.com"

# Rewrite history to change author — use git-filter-repo (git's own docs
# deprecate filter-branch; it is slow and footgun-prone)
pip install git-filter-repo
# mailmap.txt:  New Name <new@email.com> <old@email.com>
git filter-repo --mailmap mailmap.txt
# Full identity/history playbook: references/git-metadata.md
```

---

## Special Cases

### Screenshots
Screenshots typically carry no EXIF GPS but may contain:
- OS metadata (creation timestamp)
- Filename revealing internal naming conventions
- Visible content in the screenshot itself (separate from metadata — invoke `opsec-review`)

Strip with ExifTool. Low metadata risk but high content risk — review visible content separately.

### Screen recordings / iOS video
iOS encodes GPS into video files recorded on device. Always strip before sharing location-sensitive recordings.

```bash
exiftool -GPS:all= -overwrite_original recording.mp4
```

### PDFs from Word / Office
Office → PDF export embeds author name, company, template path, and software version by default. The Word document's tracked changes and comments are NOT visible in PDF but the document properties author field IS.

```bash
# Full strip
exiftool -all= -overwrite_original document.pdf
# Or use mat2 which handles PDF structure more carefully
mat2 document.pdf
```

### Compiled Binaries
Binaries compiled with debug symbols embed full source file paths, which reveal developer username and directory structure:

```
/Users/realname/projects/company-name/src/auth.c
```

Strip debug symbols before distributing:
```bash
# macOS
strip -S binary

# Linux
strip --strip-debug binary
# or full strip
strip binary

# Go binaries (build without debug info)
go build -ldflags="-s -w" -o output ./...

# Rust (release build strips by default in Cargo.toml)
[profile.release]
strip = true
```

### Archives (ZIP/TAR)
Archive internal paths reveal directory structure. Re-create archives from a neutral staging directory:

```bash
# Bad — reveals full path
zip archive.zip /Users/realname/projects/sensitive/file.txt

# Good — cd first, use relative paths
cd /tmp/staging && zip archive.zip file.txt
```

---

## Reference Files

- `references/image-metadata.md` — Full EXIF/IPTC/XMP field inventory and per-field risk ratings
- `references/document-metadata.md` — Office and PDF metadata schemas with Office XML property paths
- `references/av-metadata.md` — Audio/video metadata schemas including mobile-specific fields
- `references/archive-metadata.md` — Archive format metadata and path sanitization
- `references/git-metadata.md` — Git identity hygiene, history rewriting, and secret removal
