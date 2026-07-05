# Archive Metadata Reference

ZIP, TAR, 7z, RAR, and other archive format metadata — internal path signals, timestamp leakage, and OS fingerprinting.

---

## Why Archives Are a Privacy Surface

Archives appear to be neutral containers, but they embed:
1. **Internal file paths** — revealing directory structure, usernames, project names
2. **Timestamps** — creation, modification, access times for every file
3. **Creator metadata** — compression tool, OS version
4. **File attributes** — Unix permissions, Windows attributes
5. **Comments** — some formats support archive-level and file-level comments

The archive is often created from a working directory, which means the internal paths reflect the creator's local development environment.

---

## ZIP Format

### Metadata stored per-file entry

| Field | Risk | Notes |
|---|---|---|
| **Filename / path** | **T2** | Full relative path from archive root: `src/utils/auth.py` — OK; `/Users/realname/projects/company/src/utils/auth.py` — reveals username and internal org |
| **Last modified time** | T4 | Per-file modification timestamp; timezone in some implementations |
| Compression method | T5 | Deflate, Store, etc. — no PI |
| CRC-32 | T5 | File integrity check — no PI |
| **Extra field** | **T2** | Extension data — may contain: Unix UID/GID (user identity), extended timestamps, Info-ZIP Unix extension (uid/gid → username), NTFS timestamps with nanosecond precision |
| **Archive comment** | T2 | Optional global comment — tool-generated or user-created; may contain real name, company, version info |

### Unix extension in ZIP extra field

Python's `zipfile` and `zip` CLI on macOS/Linux often write a Unix extra field containing:
- `uid` (user ID) — numeric; linkable to username via `/etc/passwd`
- `gid` (group ID) — numeric; linkable to group

The `uid` value doesn't directly expose the username in the ZIP, but in context (if the developer's uid is known from other sources), it's a correlation signal.

```bash
# Inspect ZIP extra fields
python3 -c "
import zipfile
with zipfile.ZipFile('archive.zip') as z:
    for info in z.infolist():
        print(info.filename, info.extra.hex(), info.date_time)
"

# Create ZIP without absolute paths (use -j to junk paths)
# BAD:
zip archive.zip /Users/realname/project/file.py

# GOOD — add from within directory:
cd /tmp/staging && zip -r archive.zip .

# BETTER — use relative paths explicitly:
cd /tmp/staging && zip archive.zip file.py subdir/file2.py
```

### Stripping ZIP metadata

**Method 1: Re-create from clean staging directory**
```bash
# Copy only needed files to staging
mkdir -p /tmp/staging/project
cp src/file.py /tmp/staging/project/
cd /tmp/staging
zip -r clean-archive.zip project/
# Internal paths will be: project/file.py — no username
```

**Method 2: Use `mat2`**
```bash
mat2 archive.zip
# Outputs: archive.cleaned.zip
```

**Method 3: Strip with Python**
```python
import zipfile
import io

def strip_zip_metadata(input_path, output_path):
    with zipfile.ZipFile(input_path, 'r') as zin:
        with zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                # Strip metadata: reset timestamps to epoch, clear extra fields
                clean_info = zipfile.ZipInfo(item.filename)
                clean_info.date_time = (1980, 1, 1, 0, 0, 0)  # Epoch for ZIP
                clean_info.compress_type = zipfile.ZIP_DEFLATED
                clean_info.extra = b''  # Strip extra fields (Unix UID/GID)
                zout.writestr(clean_info, zin.read(item.filename))
```

---

## TAR Format (and .tar.gz, .tar.bz2, .tar.xz)

TAR archives store significantly more metadata than ZIP:

| Field | Risk | Notes |
|---|---|---|
| **Filename / path** | **T2** | Same path issue as ZIP; relative vs. absolute |
| **Owner name (uname)** | **T2** | **Username string stored in TAR header — "realname"** |
| **Owner UID** | T3 | Numeric user ID |
| **Group name (gname)** | T2 | Group name string |
| **Group GID** | T3 | Numeric group ID |
| **mtime** | T4 | Modification time (seconds since epoch) |
| File mode | T5 | Unix permissions — no PI |
| **PAX extended headers** | T2 | Extended attribute format — may contain: `mtime` with nanosecond precision, `atime`, `ctime`, extended owner info, custom vendor attributes |
| `usr/local/` vs `/Users/` | T2 | Absolute path format reveals OS: macOS paths start `/Users/`, Linux `/home/` |

⚠️ **TAR is the most revealing common archive format** because it stores the username string (not just a numeric UID) in every file entry header.

```bash
# View TAR headers (shows uname/gname)
tar -tvf archive.tar | head -5

# Create TAR without ownership info (--no-same-owner equivalent)
# GNU tar:
tar --owner=0 --group=0 --numeric-owner -czf clean.tar.gz -C /tmp/staging .
# This sets all ownership to root (uid=0, gid=0) and uses numeric IDs

# Remove username from existing TAR (requires re-creation):
mkdir /tmp/extracted && tar -xf archive.tar -C /tmp/extracted
tar --owner=0 --group=0 -czf clean.tar.gz -C /tmp/extracted .

# Verify — owner column should show "0/0" or "root/root":
tar -tvf clean.tar.gz | head -5
```

### macOS-specific TAR issues

macOS `tar` creates archives with macOS-specific metadata:
- **`._` AppleDouble files** — created for every file, containing macOS extended attributes (Finder tags, quarantine flags, resource forks). These are additional files in the archive named `._filename`.
- **`.DS_Store`** — Finder metadata; may contain folder structure details, view preferences, icon positions

```bash
# Exclude macOS metadata when creating TAR:
COPYFILE_DISABLE=1 tar -czf clean.tar.gz --exclude='.DS_Store' --exclude='._*' directory/

# Or use GNU tar on macOS (via Homebrew):
gtar --owner=0 --group=0 --no-mac-metadata -czf clean.tar.gz directory/
```

---

## 7z Format

7z archives support rich metadata and encryption:

| Field | Risk | Notes |
|---|---|---|
| Filename / path | T2 | Same path risk as ZIP/TAR |
| Modification time | T4 | 100ns precision (Windows FILETIME) |
| Creation time | T4 | Windows-specific; may reveal OS |
| Access time | T4 | When file was last accessed |
| File attributes | T5 | Read-only, hidden, system flags — no PI |
| Header comment | T2 | Optional; user-specified |
| Method token | T3 | Compression algorithm — fingerprinting signal |

```bash
# Create 7z without extra metadata
7z a -mhc=off clean.7z directory/  # -mhc: disable header compression (easier to inspect)
# Better: use zip or tar for sharing; use 7z only for encryption

# Strip 7z metadata: not easily done in place — re-create from clean staging
```

---

## RAR Format

RAR archives (WinRAR, unrar) store:
- Filename / path (same risk)
- Modification time
- Archive comment (user-specified)
- **Creator version** (RAR 4 vs RAR 5 — tool fingerprint)
- **NTFS timestamps** (creation, modification, access — nanosecond precision)

```bash
# Strip RAR metadata: re-create as ZIP or TAR (preferred)
# RAR is a proprietary format with limited cross-platform metadata stripping
unrar x archive.rar /tmp/extracted/
zip -r clean.zip /tmp/extracted/  # Re-archive as ZIP with clean staging
```

---

## General Archive Best Practices

### Path sanitization workflow

**Before creating any archive for external sharing:**

```bash
# Step 1: Create a clean staging directory
STAGING=$(mktemp -d)

# Step 2: Copy only needed files with relative paths
rsync -av --exclude='.git' --exclude='.DS_Store' --exclude='*.pyc' \
  ./project/ $STAGING/project/

# Step 3: Verify staging contents
find $STAGING -type f | head -20

# Step 4: Create archive from staging (relative paths, clean origin)
cd $STAGING
zip -r clean-archive.zip project/
# OR:
tar --owner=0 --group=0 -czf clean-archive.tar.gz project/

# Step 5: Inspect the archive
zipinfo clean-archive.zip | head -20
# OR:
tar -tvf clean-archive.tar.gz | head -20

# Step 6: Verify no absolute paths, no usernames
zipinfo clean-archive.zip | grep -iE "/Users/|/home/|\.DS_Store|\._"
# Should return nothing

# Step 7: Clean up staging
rm -rf $STAGING
```

### Timestamp normalization

For reproducible builds (and metadata privacy), normalize all timestamps in archives to a fixed date:

```bash
# ZIP with fixed timestamp (Jan 1, 1980 00:00:00 — ZIP epoch)
find project/ -exec touch -t 198001010000 {} \;
zip -r reproducible.zip project/

# TAR with fixed timestamp
SOURCE_DATE_EPOCH=0  # Unix epoch
tar --mtime="@0" -czf reproducible.tar.gz project/

# Verify
zipinfo reproducible.zip | awk '{print $7, $8, $9}'  # Should all be 80-01-01
```

---

## Archive Inspection Commands

```bash
# ZIP — list contents with metadata
zipinfo -v archive.zip
unzip -l archive.zip  # Brief listing

# TAR — list with ownership
tar -tvf archive.tar.gz

# 7z — list
7z l -slt archive.7z  # Detailed technical listing

# Check for absolute paths (red flag)
zipinfo archive.zip | grep "^[/\\\\]"
tar -tvf archive.tar.gz | grep "^[/\\\\]\|/home\|/Users"

# Check for username strings in TAR headers
tar -tvf archive.tar.gz | awk '{print $2}' | sort -u
# Should show "0/0" or "root/root" — not real usernames

# Extract and check for hidden macOS files
zipinfo archive.zip | grep "^\._\|\.DS_Store"
```

---

## Summary: Risk by Format

| Format | Username stored? | Timestamp precision | macOS metadata risk | Recommended for sharing? |
|---|---|---|---|---|
| ZIP (no extra field) | No | 2-second (DOS) | Low | Yes — clean and strip |
| ZIP (with Unix extra) | UID only (no name) | 1-second | Low | Yes — strip extra field |
| TAR (GNU) | **Yes — uname string** | 1-second | Medium | Yes — strip with `--owner=0` |
| TAR (macOS bsdtar) | **Yes** | 1-second | **High** | Use GNU tar instead |
| 7z | No | 100ns (Windows) | Low | OK — watch timestamps |
| RAR | No | 100ns (NTFS) | Low | Prefer ZIP/TAR |
