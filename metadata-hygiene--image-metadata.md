# Image Metadata Reference

Full field inventory for JPEG, PNG, TIFF, HEIC, WebP with risk ratings.

---

## EXIF (Exchangeable Image File Format)

Primary metadata standard for digital photos. Embedded in JPEG, TIFF, HEIC by default.

### GPS Fields — ALL Tier 1 (Always Strip)

| Field | ExifTool tag | Content |
|---|---|---|
| GPS Latitude | GPSLatitude | Degrees, minutes, seconds |
| GPS Latitude Ref | GPSLatitudeRef | N/S |
| GPS Longitude | GPSLongitude | Degrees, minutes, seconds |
| GPS Longitude Ref | GPSLongitudeRef | E/W |
| GPS Altitude | GPSAltitude | Meters above sea level |
| GPS Timestamp | GPSTimeStamp | UTC time of fix |
| GPS Date Stamp | GPSDateStamp | Date of fix |
| GPS Speed | GPSSpeed | Speed of device at capture |
| GPS Direction | GPSImgDirection | Camera direction in degrees |
| GPS Dest Latitude | GPSDestLatitude | Destination (used in some apps) |
| GPS Processing Method | GPSProcessingMethod | "GPS", "CELLID", "WLAN" — reveals positioning method |

Strip command: `exiftool -GPS:all= filename.jpg`

### Identity Fields — Tier 2

| Field | ExifTool tag | Risk |
|---|---|---|
| Artist | Artist | Photographer name |
| Copyright | Copyright | May contain real name |
| Image Description | ImageDescription | Free text, may contain name/location |
| User Comment | UserComment | Free text |
| Camera Owner Name | CameraOwnerName | Registered owner of camera |
| Camera Serial Number | CameraSerialNumber | Links photos from same camera |
| Lens Serial Number | LensSerialNumber | Same |

### Device Fields — Tier 3

| Field | ExifTool tag | Risk |
|---|---|---|
| Make | Make | Camera/phone manufacturer |
| Model | Model | Exact device model |
| Software | Software | OS version or software version |
| Lens Make | LensMake | |
| Lens Model | LensModel | |
| Body Serial Number | BodySerialNumber | |

### Temporal Fields — Tier 4

| Field | ExifTool tag | Notes |
|---|---|---|
| DateTimeOriginal | DateTimeOriginal | When shutter was pressed |
| CreateDate | CreateDate | When file was created |
| ModifyDate | ModifyDate | Last modification |
| SubSecTimeOriginal | SubSecTimeOriginal | Millisecond precision |
| OffsetTimeOriginal | OffsetTimeOriginal | Timezone offset — reveals locale |

---

## IPTC (International Press Telecommunications Council)

Older metadata standard, common in professional photography workflows.

| Field | Risk |
|---|---|
| By-line (Author) | T2 — real name |
| City | T1/T2 — location |
| Country | T2 |
| Caption | T2 — may contain names/locations |
| Keywords | T2/T5 |
| Copyright Notice | T2 |
| Credit | T2 |

Strip command: `exiftool -IPTC:all= filename.jpg`

---

## XMP (Extensible Metadata Platform)

XML-based metadata embedded or as sidecar. Adobe products write extensively to XMP.

| Field | Risk |
|---|---|
| dc:creator | T2 — real name |
| dc:description | T2 — may contain identifying info |
| xmp:CreatorTool | T3 — software and version |
| xmp:CreateDate | T4 |
| xmp:ModifyDate | T4 |
| photoshop:AuthorsPosition | T2 |
| photoshop:City | T2 |
| photoshop:Country | T2 |
| Lightroom catalog path | T2/T5 — may reveal internal path |

Strip command: `exiftool -XMP:all= filename.jpg`

---

## PNG Specific

PNG doesn't use EXIF natively but embeds metadata in tEXt, iTXt, and zTXt chunks.

Common tEXt chunks written by software:

| Chunk key | Content | Risk |
|---|---|---|
| Author | Creator name | T2 |
| Copyright | Copyright string | T2 |
| Creation Time | Timestamp | T4 |
| Software | App that created it | T3 |
| Comment | Free text | T2 |
| Source | Source file path | T2 — may reveal internal path |

Strip command: `exiftool -all= filename.png` (strips tEXt/iTXt chunks)
Alternative: `convert input.png -strip output.png` (ImageMagick)

**Note:** PNG screenshots from iOS/Android typically have NO metadata. Desktop screenshots may have creation timestamp only.

---

## HEIC / HEIF (iPhone default format)

HEIC is a container format using EXIF for metadata — same fields as JPEG EXIF apply.

Additionally may contain:
- Live Photo pairing data (links still to video component)
- Depth map metadata
- Portrait mode parameters

Strip with ExifTool same as JPEG: `exiftool -all= filename.heic`

**Convert to JPEG with strip:**
```bash
exiftool -all= filename.heic
# or convert and strip simultaneously
convert filename.heic -strip output.jpg
```

---

## Camera Serial Numbers as Persistent Identifier

Camera and lens serial numbers are a persistent identifier that links all photos from a device. If publishing photos pseudonymously, serial numbers must be stripped.

A camera serial number uniquely identifies the device. If two "anonymous" photos share a serial number, they were taken by the same device — even if GPS, author, and all other fields are stripped.

Strip: `exiftool -CameraSerialNumber= -BodySerialNumber= -LensSerialNumber= filename.jpg`
