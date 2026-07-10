# Audio & Video Metadata Reference

Metadata schemas and risk ratings for: MP3, FLAC, M4A, WAV, AAC (audio); MP4, MOV, MKV, AVI, WebM (video); and platform-specific formats (iOS HEVC, Android MP4).

---

## Audio Metadata

### ID3 Tags (MP3)

ID3v2 is the dominant tagging standard for MP3. ID3v1 (older, limited) also common.

| Tag | Frame ID | Risk | Action |
|---|---|---|---|
| Title | TIT2 | T5 | OK |
| Artist | TPE1 | T2 — may be real name | Review before sharing |
| Album | TALB | T5 | OK |
| **Comment** | COMM | **T2** — free text; may contain name, location, date | **Review or strip** |
| **Recording date/time** | TDRC | T4 — temporal signal | Strip for privacy |
| **Encoder software** | TSSE | T3 — reveals DAW/tool version | Strip before publishing |
| Encoded by | TENC | T2 — may contain real name | Strip |
| **Copyright** | TCOP | T2 — may contain real name | Review |
| URL/link | WOAS, WOAR | T2/T5 | Review |
| **Unique file ID** | UFID | T3 — device/tool identifier | Strip |
| ISRC | TSRC | T5 — public identifier | OK |
| **Private frames** | PRIV | **T1** — application-specific, often contain metadata beyond spec | **Strip always** |
| Popularimeter | POPM | T5 | OK |
| **Replay Gain** | TXXX:REPLAYGAIN | T3 — calculated from file; can fingerprint audio | Strip for high-security |

**Strip all ID3 tags:**
```bash
# Using eyeD3
eyeD3 --remove-all filename.mp3

# Using ffmpeg (stream-copy — no re-encode, no quality loss)
ffmpeg -i input.mp3 -map_metadata -1 -c:a copy output.mp3

# NOTE: exiftool CANNOT write MP3 (read-only format for it) — do not use
# `exiftool -all=` here; it silently does nothing and the tags remain.
```

### Vorbis Comments (FLAC, OGG, Opus)

FLAC uses Vorbis comments — free-form key=value pairs. No fixed schema; any field can be added.

| Common tag | Risk | Notes |
|---|---|---|
| TITLE, ARTIST, ALBUM | T5/T2 | Artist may be real name |
| **COMMENT** | T2 | Free-form — review for PI |
| **ENCODER** | T3 | Software version fingerprint |
| **DATE** | T4 | Recording date |
| **REPLAYGAIN_**** | T3 | Audio fingerprinting surface |
| **TRACKTOTAL, DISCNUMBER** | T5 | OK |
| Any custom field | Variable | Producers sometimes add GPS, session, studio fields |

```bash
# Strip all Vorbis comments from FLAC (metaflac is the canonical tool;
# exiftool reads FLAC but cannot write it)
metaflac --remove-all-tags filename.flac
# Also remove embedded artwork (its own EXIF rides inside):
metaflac --remove --block-type=PICTURE filename.flac
```

### iTunes/M4A (AAC in MP4 container)

| Atom | Risk | Notes |
|---|---|---|
| `©nam` (title), `©ART` (artist) | T2/T5 | Artist = real name risk |
| `©cmt` (comment) | T2 | Free-form |
| `©day` (date) | T4 | |
| `©too` (encoder tool) | T3 | Software fingerprint |
| `aART` (album artist) | T2 | |
| **`ownr`** | **T2** | **iTunes Store purchase: contains Apple ID (email address)** |
| **`xid`** | T3 | iTunes Store catalog ID — linkable to purchase |
| **`apID`** | **T2** | **Apple ID email address** |

⚠️ **iTunes purchases:** M4A files purchased from iTunes contain the buyer's Apple ID (email address) in the `apID` atom. Strip before sharing.

```bash
exiftool -all= filename.m4a
# Verify:
exiftool filename.m4a | grep -i "apple\|email\|owner\|apid"
```

### WAV / AIFF (Broadcast Wave Format)

WAV files often carry minimal metadata, but professional audio workflows add BWF (Broadcast Wave Format) extension chunks.

| Chunk | Risk | Notes |
|---|---|---|
| INFO chunks (INAM, IART, etc.) | T2/T5 | Standard metadata |
| **BWF `bext` chunk** | **T2/T4** | **Contains: Description, Originator (studio/recorder name), OriginatorReference (file ID), OriginationDate, OriginationTime, TimeReference (exact sample position in session)** |
| **BWF `iXML` chunk** | **T2** | **XML metadata: project name, session name, recorder name, scene/take/note fields** |
| **`axml` / `XMP` embedded** | **T2** | XMP metadata with producer/author fields |

```bash
# exiftool CANNOT write WAV/RIFF — strip via ffmpeg remux (stream-copy;
# ffmpeg's WAV muxer omits bext/iXML/INFO unless explicitly asked to write them)
ffmpeg -i input.wav -map_metadata -1 -c:a copy output.wav
# Verify the chunks are gone:
exiftool output.wav | grep -iE "originator|bext|ixml|description"
# Surgical BWF editing (audio-industry standard tool): BWF MetaEdit
bwfmetaedit --out-core-remove filename.wav
```

---

## Video Metadata

### MP4 / M4V (MPEG-4 Container)

| Atom | Risk | Notes |
|---|---|---|
| `©nam`, `©ART`, `©cmt` | T2/T5 | Standard metadata |
| **`©too`** | T3 | Encoder tool + version |
| **`XMP_` or `uuid` XMP** | T2 | XMP data: may contain author, rights, keywords |
| **`udta` / `meta`** | T2 | User data atom: free-form; may contain location, producer |
| **GPS location atoms** | **T1** | **Apple: `©xyz` atom (lat,lon,alt)**; Android: `loci` atom; GPS coordinates are exact location |
| **Creation time** | T4 | Encoded in `mvhd` (movie header) — `utc_date` |
| **Modification time** | T4 | Same atom |
| Track atoms | T5 | Codec, resolution — no PI |

⚠️ **iPhone/iOS video:** Every video recorded on an iPhone contains GPS coordinates in the `©xyz` QuickTime user data atom. Default iOS behavior is to embed precise GPS in all video files. **Strip before any sharing.**

```bash
# Strip GPS and all metadata from MP4
exiftool -all= filename.mp4
# Verify GPS removed:
exiftool filename.mp4 | grep -i "gps\|location\|xyz\|loci"

# If GPS remains after exiftool (embedded in container differently):
ffmpeg -i input.mp4 -map_metadata -1 -c:a copy -c:v copy output.mp4
```

### QuickTime MOV (Apple)

Identical structure to MP4 with additional Apple-specific atoms:

| Atom | Risk | Notes |
|---|---|---|
| **`©xyz`** | **T1** | **GPS coordinates — strip always** |
| **`loci`** | **T1** | **Alternate location atom** |
| `mdta` / `keys` | T2 | User-defined metadata key-value pairs; may contain custom PI |
| **`com.apple.quicktime.make`** | T3 | Device manufacturer |
| **`com.apple.quicktime.model`** | T3 | Exact device model (e.g., "iPhone 14 Pro") |
| **`com.apple.quicktime.software`** | T3 | iOS version |
| **`com.apple.quicktime.creationdate`** | T4 | Exact creation datetime with timezone |
| **`com.apple.quicktime.location.ISO6709`** | **T1** | **GPS in ISO 6709 format — strip** |

```bash
# Strip all Apple QuickTime metadata
exiftool -api QuickTimeHandler -all= filename.mov
# Or comprehensive strip:
exiftool -all= filename.mov
```

### Android Video (MP4)

Android records to MP4. Additional metadata written by Google Camera and manufacturer camera apps:

| Field | Risk | Notes |
|---|---|---|
| `com.google.android.video.timestamp` | T4 | High-precision timestamp |
| **GPS data** | **T1** | Location embedded if camera location permission granted |
| `android.manufacturer`, `android.model` | T3 | Device fingerprint |
| `android.version` | T3 | OS version |
| **`com.android.version`** | T3 | Android version string |

### MKV (Matroska)

MKV uses a flexible tag system. Common tags:

| Tag | Risk | Notes |
|---|---|---|
| `DATE_RECORDED`, `DATE_ENCODED` | T4 | Temporal signal |
| `ENCODER` | T3 | Tool version |
| `ENCODED_BY`, `AUTHOR` | T2 | May be real name |
| `COMMENT` | T2 | Free-form |
| Attachment sections | Variable | May contain album art with EXIF, subtitle files, etc. |

```bash
# Strip MKV metadata — remux with ffmpeg (stream-copy; drops tags and attachments)
ffmpeg -i input.mkv -map 0:v -map 0:a -map 0:s? -map_metadata -1 -c copy output.mkv
# Surgical tag removal in place (mkvtoolnix; attachments are deleted by id):
mkvpropedit filename.mkv --tags all:
mkvmerge -i filename.mkv          # list attachment ids
mkvpropedit filename.mkv --delete-attachment 1
# NOTE: exiftool CANNOT write Matroska — `exiftool -all=` on .mkv is a silent no-op.
```

---

## Screen Recordings

Screen recordings (macOS QuickTime, iOS screen record, OBS, Camtasia, Loom) typically have minimal embedded metadata but carry significant content-level risk:

| Risk | Source | Mitigation |
|---|---|---|
| Username in window title bar or path bar | macOS Finder, file manager | Record at appropriate zoom; use Finder path bar off |
| Desktop visible in recording | Full-screen recording | Use focused window recording mode |
| Notification popups during recording | All platforms | Enable Do Not Disturb before recording |
| Browser URL bar with account-linked URLs | Browser recording | Use private/incognito window or blur URL bar |
| Profile photo/name visible | Any social/communication app | Mock account or blurred region |
| Taskbar/dock application list | Full screen recording | Reveals installed apps |
| System clock time/timezone | Menu bar visible | Temporal + timezone signal |

**Metadata risk for screen recordings:** Low for metadata; HIGH for content. Run through `opsec-review` for content before publishing.

---

## Voice Notes / Phone Recordings

Applications that record voice notes and phone calls often add rich metadata:

| Source | Metadata risk |
|---|---|
| iPhone Voice Memos | GPS coordinates, creation time with timezone |
| Android recorder apps | GPS (if permission granted), device ID |
| Zoom/Teams call recordings | Participant list, organization, meeting ID, creation timestamp |
| Podcast recording software (Riverside, Zencastr) | Participant names, session info |
| Google Meet recordings | Google account identity of recorder |

**Voice recordings and biometrics:** Voice recordings are biometric data under GDPR Art. 9, BIPA (Illinois), CCPA sensitive PI, and PIPL sensitive PI when used for identification purposes. If publishing voice content under a pseudonym, note that voiceprint analysis is a deanonymization vector — see `opsec-review/references/doc-signals.md` stylometric section.

---

## Quick Reference — Stripping Commands

```bash
# Universal (handles most audio and video formats)
exiftool -all= -overwrite_original FILE

# Verify completely clean
exiftool FILE | grep -iE "gps|location|author|creator|owner|email|apple|android|device|model|make|software|encoder|comment|date|time"
# Should return nothing sensitive

# Video: strip via ffmpeg (re-mux without metadata)
ffmpeg -i input.mp4 -map_metadata -1 -c copy output.mp4

# Audio: strip via ffmpeg
ffmpeg -i input.mp3 -map_metadata -1 -c:a copy output.mp3

# FLAC: strip native tags
metaflac --remove-all-tags input.flac

# MKV: strip via mkvpropedit
mkvpropedit input.mkv --tags global:""
```

---

## Platform-Specific Publishing Notes

**YouTube:** Strips most metadata on upload but retains creation timestamp and processes GPS data internally. Do not rely on YouTube stripping for privacy — strip before upload.

**Vimeo:** Similar to YouTube — strips most metadata. Strip before upload.

**Twitter/X video:** Strips embedded metadata. Strip before upload for belt-and-suspenders.

**Instagram / TikTok:** Strips metadata but platforms retain original upload (with metadata) internally. Strip before upload.

**Podcast hosting (Spotify, Apple Podcasts):** Retains embedded metadata in distributed audio files. Listeners can extract ID3 tags from downloaded files. Strip all non-essential ID3 tags before submitting to hosting platforms.

**Soundcloud:** Distributes original file with embedded metadata if not stripped. Strip before upload.
