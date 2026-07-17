# Document Metadata Reference

Office formats (DOCX, XLSX, PPTX) and PDF metadata schemas with field-level risk ratings and stripping procedures.

---

## Microsoft Office (OOXML — DOCX, XLSX, PPTX)

Office Open XML files are ZIP archives. Metadata is stored in:
- `docProps/core.xml` — Core document properties (author, dates)
- `docProps/app.xml` — Application-specific properties (company, word count)
- `word/settings.xml` — Template path, revision history settings
- `word/comments.xml` — Comments (may contain real names)
- `word/revisions` — Track changes with author names and timestamps

### Core Properties (docProps/core.xml) — All High Risk

```xml
<cp:coreProperties>
  <dc:creator>Real Name Here</dc:creator>          <!-- T2: Real name -->
  <cp:lastModifiedBy>Real Name Here</cp:lastModifiedBy> <!-- T2: Real name -->
  <dc:description>Internal project details</dc:description> <!-- T2: May reveal internal info -->
  <cp:keywords>confidential project helios</cp:keywords>    <!-- T2: Internal keywords -->
  <dc:subject>Q3 Financial Review</dc:subject>     <!-- T2: May reveal internal matter -->
  <dcterms:created>2024-01-15T09:32:11Z</dcterms:created> <!-- T4: Creation time -->
  <dcterms:modified>2024-01-22T14:07:33Z</dcterms:modified> <!-- T4: Modification time -->
  <cp:revision>47</cp:revision>                    <!-- T5: Revision count (how much editing happened) -->
  <cp:lastPrinted>2024-01-16T08:00:00Z</cp:lastPrinted> <!-- T4: Print timestamp -->
</cp:coreProperties>
```

**Every field in core.xml is high-risk for external sharing. Strip all.**

### Application Properties (docProps/app.xml)

```xml
<Properties>
  <Application>Microsoft Word</Application>     <!-- T3: Application name -->
  <AppVersion>16.0000</AppVersion>              <!-- T3: Exact version -->
  <Company>Acme Corp</Company>                  <!-- T2: Organization name -->
  <Manager>Jane Smith</Manager>                 <!-- T2: Manager name -->
  <Template>InternalTemplate_v2.dotx</Template> <!-- T2: Reveals internal template path -->
  <TotalTime>847</TotalTime>                    <!-- T5: Edit time in minutes -->
  <Words>3421</Words>                           <!-- T5: Word count -->
</Properties>
```

**Company** and **Manager** fields are particularly sensitive — directly reveal organizational information.
**Template** field reveals internal file server path if using a networked template: `\\server\templates\InternalTemplate_v2.dotx`

### Track Changes & Comments — Highest Risk

Track changes and comments contain:
- Author's real name (from Word account settings)
- Date and time of each change
- Full text of deleted content (still in file, just marked as deleted)
- Comment text (may contain internal discussions, client names, personal opinions)
- Reviewer email addresses (in some versions)

**Risk:** A "clean" DOCX with track changes accepted still contains the full revision history in the XML if track changes were used during editing. The history is invisible in Word's normal view but readable from the raw XML.

```bash
# Check for track changes in DOCX
unzip -p document.docx word/document.xml | grep -c "w:ins\|w:del"
# Non-zero = tracked changes present in XML

# Secure approach: Save as PDF, then strip PDF metadata
# OR: Copy all content to a new document (breaks revision history)
```

### Stripping Office Metadata

**Method 1: Word Document Inspector (in-app)**
1. File → Info → Check for Issues → Inspect Document
2. Check all boxes especially: Comments/Revisions, Document Properties/Personal Information, Hidden Data
3. Remove All for each category
4. Save As (new file)

**Method 2: ExifTool (command line)**
```bash
# Strip all metadata
exiftool -all= -overwrite_original document.docx

# Verify
exiftool document.docx | grep -iE "author|creator|company|manager|template|modified|created|printed"
```

**Method 3: LibreOffice (cross-platform)**
```bash
# Open in LibreOffice, File → Properties → clear all fields
# Or convert via command line (strips most metadata):
libreoffice --headless --convert-to docx --infilter="Microsoft Word 2007-2019" input.docx
# Note: Sets author from LibreOffice user settings — configure to pseudonym first:
# Tools → Options → LibreOffice → User Data → clear all fields
```

**Method 4: Convert to plain format and back**
For maximum metadata removal: export to Markdown or plain text, verify content, recreate document. Destroys formatting but guarantees zero metadata.

---

## PDF Metadata

PDFs store metadata in two locations:
1. **Document Information Dictionary** (older, widely supported)
2. **XMP (Extensible Metadata Platform)** metadata stream (newer, more detailed)

Both must be stripped. ExifTool handles both; Adobe Acrobat's built-in tools handle both; `mat2` handles both.

### Document Information Dictionary

| Field | Risk | Notes |
|---|---|---|
| `Author` | T2 | Real name from Office export |
| `Creator` | T3 | "Microsoft Word 16.0" or "Adobe InDesign" — tool fingerprint |
| `Producer` | T3 | PDF generator tool + version |
| `Title` | T2 | May contain internal project name |
| `Subject` | T2 | Internal matter |
| `Keywords` | T2 | Internal tags, classifications |
| `CreationDate` | T4 | When document was created |
| `ModDate` | T4 | Last modification time |
| `Trapped` | T5 | Print production flag — no PI |

### XMP Metadata Stream

XMP often contains additional detail beyond the Document Information Dictionary:

| XMP field | Risk | Notes |
|---|---|---|
| `xmp:CreatorTool` | T3 | Full application name + version |
| `xmp:CreateDate` | T4 | ISO 8601 creation datetime |
| `xmp:ModifyDate` | T4 | |
| `xmp:MetadataDate` | T4 | When metadata was last written |
| `dc:creator` | T2 | Author name (Dublin Core) |
| `dc:title` | T2 | Document title |
| `dc:description` | T2 | Document description |
| `dc:rights` | T2 | Copyright statement — may include real name |
| `xmpMM:DocumentID` | T3 | Unique document ID — links versions of same document |
| `xmpMM:InstanceID` | T3 | Instance ID — changes each save |
| `xmpMM:History` | **T2** | **Edit history: each save event with tool, action, timestamp** |
| `pdf:Producer` | T3 | PDF generator |
| `pdfaid:conformance` | T5 | PDF/A conformance level — no PI |
| Photoshop XMP fields | T2 | `photoshop:Credit`, `photoshop:AuthorsPosition` — if PDF from Photoshop |

⚠️ **`xmpMM:History`** is particularly sensitive — it records every save event with the tool name, timestamp, and may include information about color space conversions and document processing history.

### PDFs from Specific Sources

**Word/Office export:**
Author field populated from Office account name. Company from organization settings. Template path may appear. Solution: strip before distributing.

**LaTeX (pdflatex):**
Author from `\author{}` command. `Creator: LaTeX with hyperref`. If using `\usepackage[pdfauthor={Real Name}]{hyperref}` — real name in metadata. Solution: set `pdfauthor={}` in hyperref options, or strip post-build.

```latex
\usepackage[
  pdfauthor={},
  pdftitle={},
  pdfsubject={},
  pdfkeywords={}
]{hyperref}
```

**Scanned PDFs:**
OCR tools (Adobe Acrobat, ABBYY) often add metadata including operator name, scanner model, and scan timestamp. Scanned PDFs from medical/legal offices may have been processed by third-party services with their metadata embedded.

**Form PDFs:**
Filled form fields contain user-provided PI. If sharing a filled form, either flatten it (fields → static content) or clear all fields before sharing. Flattening also prevents future field modification.

```bash
# Flatten PDF form fields (requires pdftk or Ghostscript)
pdftk filled_form.pdf output flattened.pdf flatten

# Then strip metadata from flattened version
exiftool -all= flattened.pdf
```

### Stripping PDF Metadata

**Method 1: ExifTool (recommended for batch)**
```bash
# Strip all metadata from PDF
exiftool -all= -overwrite_original document.pdf

# Verify:
exiftool document.pdf | grep -iE "author|creator|producer|title|subject|keyword|company|date|history"
# Should return nothing
```

**Method 2: mat2 (privacy-focused, handles PDF structure carefully)**
```bash
mat2 document.pdf
# Outputs: document.cleaned.pdf
mat2 --show document.pdf  # Preview what would be removed
```

**Method 3: Ghostscript (removes metadata + linearizes)**
```bash
gs -dBATCH -dNOPAUSE -dQUIET -sDEVICE=pdfwrite \
   -dFastWebView=false \
   -sOutputFile=clean.pdf \
   input.pdf
# Note: Ghostscript may add its own Producer metadata — strip again after
```

**Method 4: Adobe Acrobat Pro**
Tools → Redact → Sanitize Document (most thorough — removes hidden layers, metadata, embedded content, scripts)

---

## PowerPoint (PPTX) Specific

PPTX follows the same OOXML structure as DOCX with additional risks:

### Speaker notes
Speaker notes are stored in `ppt/notesSlides/` — often contain:
- Internal reminders ("don't mention the acquisition")
- Talking points revealing strategic information
- Names, client names, confidential context
- Draft content not intended for audience

**Strip before external sharing:** Remove all notes via Presentation → File → Check for Issues → Inspect Document → Presentation Notes.

### Slide master and layout templates
Template paths in `ppt/slides/_rels/` may reveal internal file server paths.

### Embedded objects
Slides often contain embedded Excel charts, Word documents, or other files. These embedded files carry their own metadata including:
- Author name from parent application
- Creation timestamp
- Internal file paths

```bash
# Extract and inspect embedded objects
unzip -d extracted presentation.pptx
# Check ppt/embeddings/ for embedded files
ls extracted/ppt/embeddings/
# Apply exiftool to each embedded file
exiftool extracted/ppt/embeddings/*.xlsx
```

### Video/audio embedded in slides
Embedded media files carry the same EXIF/ID3/video metadata as standalone files. See av-metadata.md for stripping procedures. Note that embedded media is stored in `ppt/media/`.

---

## Excel (XLSX) Specific

### Named ranges and defined names
Named ranges in Excel may contain internal naming conventions, codenames, or project names visible in the Name Manager.

### Custom XML parts
XLSX files may contain custom XML parts (`customXml/`) — used by SharePoint, Power Automate, and enterprise tools to store additional metadata including workflow state, approval history, and user IDs.

```bash
unzip -p spreadsheet.xlsx customXml/item1.xml 2>/dev/null
# If output contains PI, strip the custom XML before sharing:
# (Cannot easily strip with exiftool alone — requires re-packaging ZIP)
```

### External links
Excel files may contain references to external files (`xl/externalLinks/`) — internal network paths, SharePoint URLs, internal server names. Strip or convert to values before sharing.

---

## Quick Reference Commands

```bash
# Office (DOCX/XLSX/PPTX) — strip all metadata
exiftool -all= -overwrite_original FILE.docx

# PDF — strip with mat2 (recommended)
mat2 FILE.pdf
# Output: FILE.cleaned.pdf

# PDF — strip with exiftool
exiftool -all= FILE.pdf

# Verify clean (all formats)
exiftool FILE | grep -iE "author|creator|producer|company|manager|template|subject|keyword|modified|created|printed|history"
# Should return nothing sensitive

# Check for track changes in DOCX
unzip -p FILE.docx word/document.xml | grep -c "w:ins\|w:del"
# If non-zero: accept all changes, then re-export

# Check for speaker notes in PPTX
unzip -p FILE.pptx ppt/notesSlides/notesSlide1.xml 2>/dev/null | grep -o '<a:t>[^<]*</a:t>'
```
