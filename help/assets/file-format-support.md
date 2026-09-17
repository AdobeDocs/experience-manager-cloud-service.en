---
title: Supported file formats and MIME types
description: File formats and MIME types supported by [!DNL Experience Manager Assets] as a [!DNL Cloud Service].
contentOwner: AG
feature: Asset Management, Renditions
role: User, Admin
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: e848aa77-7829-4adc-8b88-0279791a4525
---
# [!DNL Assets] supported file formats {#supported-file-formats}

[!DNL Adobe Experience Manager] as a [!DNL Cloud Service] delivers **basic content management capabilities** for any binary file, independent of its format — including storage, online metadata management, versioning, and upload and download of files. **[!DNL Adobe Experience Manager Assets]** supports a wide range of file formats, and each product feature provides specific levels of support for different formats.

In addition, [!DNL Experience Manager Assets] provides **extended support** to generate previews and renditions and to extract metadata and text for **full-text indexing**. This extended support is delivered through [asset microservices](asset-microservices-configure-and-use.md), which enable scalable, automated processing of assets in the cloud so that previews, renditions, and metadata extraction run consistently across large asset libraries.

The highlights for asset conversion using asset microservices include:

* Key [Adobe file formats](#adobe-formats) produced by Adobe applications and services, including **[!DNL Adobe Photoshop], [!DNL Adobe InDesign], [!DNL Adobe Illustrator], [!DNL Adobe XD], [!DNL Adobe Dimension], and [!DNL Adobe Acrobat] or PDF (Portable Document Format)**.
* Key [imaging file formats](#image-formats).
* [Camera Raw file formats](#camera-raw-formats) for a wide range of cameras, including **Canon, Nikon, Fujifilm, Olympus, and other manufacturers** (powered by Adobe [!DNL Camera Raw]).
* Common [document formats](#document-formats), including **Microsoft&reg; Office and Open Document formats**.
* Wide range of [video](#video-formats) and [audio](#audio-formats) formats.

The following legend describes the level of support for each format.

| Support level |         Description         |
| ------------- | --------------------------- |
| &#10003;      | Supported                   |
| *             | See remarks below the table |
| -             | Not applicable              |

>[!IMPORTANT]
>
>[!DNL Adobe Experience Manager Assets] supports only the file formats listed in this article.
>Some features might seem to work with other formats, but these formats are not officially supported. As a result, output can be inconsistent, and features may not work as expected.
>Because unsupported formats can produce unreliable results, use only the supported formats to ensure consistent and predictable behavior.

## Adobe formats {#adobe-formats}

[!DNL Adobe Experience Manager] (AEM) [!DNL Assets] processes a range of native Adobe file formats, generating previews and extracting embedded information so assets remain searchable and usable within the digital asset management system. The table below identifies which processing capabilities are supported for each Adobe format.

**Supported capabilities defined:**

- **Thumbnail generation** — creates a visual preview (rendition) of the asset for browsing and search results.
- **Full-text extraction** — indexes readable text content inside the file so the asset can be found by keyword search.
- **Metadata extraction** — reads embedded metadata (such as author, title, and descriptive fields) from the file.
- **Width/Height** — detects and records the pixel or page dimensions of the asset.

| File format | Thumbnail generation | Full-text extraction | Metadata extraction | Width/Height |
| ----------- | -------------------- | ------------------- | ------------------- | ------------ |
| AI          | &#10003;             | -                   | &#10003;            | &#10003;     |
| COLLAGE     | -                    | -                   | &#10003;            | -            |
| DN          | &#10003;             | -                   | &#10003;            | &#10003;     |
| SBSAR       | &#10003;             | -                   | &#10003;            | &#10003;     |
| IDEAS       | -                    | -                   | &#10003;            | -            |
| INDD        | &#10003;             | -                   | &#10003;            | &#10003; *   |
| INDT        | -                    | -                   | &#10003;            | -            |
| PDF         | &#10003;             | &#10003;            | &#10003;            | &#10003;     |
| PROTO       | -                    | -                   | &#10003;            | -            |
| PSB         | &#10003;             | -                   | &#10003;            | &#10003;     |
| PSD         | &#10003;             | -                   | &#10003;            | &#10003;     |
| XD          | &#10003;             | -                   | &#10003;            | &#10003;     |

**Among all listed Adobe formats, PDF is the only format that supports full-text extraction** in addition to thumbnail generation, metadata extraction, and width/height detection. Every format in the table supports **metadata extraction**, while thumbnail generation and width/height detection are supported for the raster and design formats but not for the container or template formats.

**Formats supporting thumbnail generation and width/height detection:** AI, DN, SBSAR, INDD, PDF, PSB, PSD, and XD. In contrast, COLLAGE, IDEAS, INDT, and PROTO support metadata extraction only.

**Adobe format acronyms explained:**

- **AI** — [!DNL Adobe Illustrator] vector artwork.
- **COLLAGE** — Adobe collage file.
- **DN** — Adobe file with the DN extension.
- **SBSAR** — Adobe Substance material archive.
- **IDEAS** — Adobe Ideas sketch file.
- **INDD** — [!DNL Adobe InDesign] document.
- **INDT** — [!DNL Adobe InDesign] template.
- **PDF** — Portable Document Format.
- **PROTO** — Adobe prototype file.
- **PSB** — [!DNL Adobe Photoshop] Large Document (big).
- **PSD** — [!DNL Adobe Photoshop] Document.
- **XD** — [!DNL Adobe XD] experience design file.

\* For [!DNL Adobe InDesign] files (INDD), the size of renditions is determined by the preview image embedded in the INDD file. To embed larger renditions, configure the preview preferences in [!DNL InDesign] at **[!UICONTROL Preferences > File Handling > Always Save Preview Images with Documents, Preview Size]**. Selecting a larger preview size ensures that AEM [!DNL Assets] can generate higher-resolution thumbnails for [!DNL InDesign] documents.

## Image formats {#image-formats}

The following image file formats are supported for processing, with capabilities spanning **thumbnail generation**, **metadata extraction**, **width/height detection**, and **cropping**. Supported formats include common raster formats such as **BMP (Bitmap)**, **GIF (Graphics Interchange Format)**, **JPEG (Joint Photographic Experts Group)**, **PNG (Portable Network Graphics)**, **TIFF (Tagged Image File Format)**, and **WebP**, along with vector and specialized formats including **EPS (Encapsulated PostScript)**, **SVG (Scalable Vector Graphics)**, **SGI™**, **RGB**, and **RGBA**.

### Supported capabilities defined

- **Thumbnail generation** — creates a smaller preview representation of the source image, useful for listings, galleries, and quick visual identification.
- **Metadata extraction** — reads embedded information such as color profile, encoding details, and other properties stored within the file.
- **Width/Height** — detects the pixel dimensions of the image, enabling accurate layout and scaling.
- **Crop** — trims the image to a specified region, removing unwanted areas while preserving the retained content.

### Capability support by format

| File format | Thumbnail generation | Metadata extraction | Width/Height |   Crop   |
| ----------- | -------------------- | ------------------- | ------------ | -------- |
| BMP         | &#10003;             | -                   | &#10003;     | &#10003; |
| EPS         | &#10003;             | &#10003;            | -            | -        |
| GIF         | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| JPEG        | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| PNG         | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| RGB         | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| RGBA        | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| SGI&trade;         | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| SVG         | &#10003;             | -                   | &#10003;     | &#10003; |
| TIFF        | &#10003;             | &#10003;            | &#10003;     | -        |
| WebP        | &#10003;             | &#10003;            | &#10003;     | &#10003; |

### Key support notes

- **All listed formats support thumbnail generation**, making preview creation universally available across the supported set.
- Formats supporting **all four capabilities** — thumbnail generation, metadata extraction, width/height detection, and cropping — are **GIF**, **JPEG**, **PNG**, **RGB**, **RGBA**, **SGI™**, and **WebP**.
- **BMP** and **SVG** support every capability **except metadata extraction**, reflecting that these formats carry limited embedded property data.
- **EPS** does not support width/height detection or cropping, consistent with its role as a PostScript-based format rather than a fixed-dimension raster image.
- **TIFF** supports thumbnail generation, metadata extraction, and width/height detection, but does **not** support cropping.

As widely acknowledged in image processing, raster formats such as **JPEG**, **PNG**, and **WebP** store pixel-based data with defined dimensions, which is why they consistently support width/height detection and cropping. Vector-oriented formats like **SVG** and **EPS** describe images through scalable instructions rather than fixed pixel grids, which explains the more limited support for certain dimension- and metadata-dependent operations reflected in the table above.

## 3D formats {#support-3d-formats}

Nine 3D file formats are supported: **DN**, **gLB**, **gLTF**, **OBJ**, **STL**, **FBX**, **3DS**, **USDz**, and **SBSAR**. Each format supports storage, versioning, and workflow, while publishing, thumbnail preview, 3D preview, and [!DNL Dynamic Media] delivery vary by format as shown in the support matrix below.

See also [Work with 3D assets in [!DNL Dynamic Media]](/help/assets/dynamic-media/assets-3d.md).

### Supported 3D format definitions

The supported formats correspond to widely used 3D file types:

- **gLB** and **gLTF** — GL Transmission Format (glTF), an open standard for efficient transmission and loading of 3D scenes and models. **gLB** is the binary packaging of the format.
- **OBJ** — Wavefront OBJ, a common geometry definition format for representing 3D meshes.
- **STL** — Stereolithography (STL), widely used for 3D printing and rapid prototyping.
- **FBX** — Filmbox (FBX), an interchange format for 3D content, animation, and scenes.
- **3DS** — 3D Studio (3DS), a legacy mesh and scene format.
- **USDz** — Universal Scene Description Zip (USDz), an AR-oriented container format for 3D assets.
- **SBSAR** — Substance Archive (SBSAR), a parametric material and texture format.
- **DN** — a supported storage and workflow format for 3D assets.

### Capability columns explained

Each column in the support matrix indicates whether a given capability is available for that format:

- **Storage** — the format can be stored and managed as a 3D asset.
- **Versioning** — multiple versions of the asset can be tracked and retained.
- **Workflow** — the asset can be processed through automated workflows.
- **Publishing** — the asset can be published for delivery. Because publishing is required for downstream delivery, formats without publishing support are limited to internal use.
- **Access control** — permissions can be applied to govern who can view or manage the asset.
- **Thumbnail preview** — a static thumbnail image is generated for quick visual identification.
- **3D preview** — an interactive 3D preview is available for inspecting the model.
- **[!DNL Dynamic Media] delivery** — the asset can be delivered through [!DNL Dynamic Media]. The formats that support full [!DNL Dynamic Media] delivery are **gLB**, **OBJ**, **STL**, and **USDz**.

### 3D format support matrix

| Format | Storage | Versioning | Workflow | Publishing | Access control | Thumbnail preview | 3D preview | [!DNL Dynamic Media] delivery |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| DN | &#10003; | &#10003; | &#10003; |- | &#10003; | &#10003; | -| -|
| gLB | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; |
| gLTF | &#10003; | &#10003; | &#10003; |- | &#10003; |- | &#10003; |- |
| OBJ | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; |
| STL | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; |- | &#10003; | &#10003; |
| FBX | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | - |- |
| 3DS | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | - |- |
| USDz |&#10003;| &#10003; | &#10003; | &#10003; | &#10003; | &#10003; |- | &#10003; |
| SBSAR |&#10003;| &#10003; | &#10003; |- | &#10003; | &#10003; |- |- |

## [!DNL Camera Raw] formats {#camera-raw-formats}

All **27 camera raw file formats** listed below support the same three core operations: **thumbnail generation**, **metadata extraction**, and **width/height detection**. Every format in the table is fully supported across all three capabilities, making the coverage uniform and comprehensive across the major camera raw standards.

### Supported operations for each format

Each supported capability serves a distinct purpose when processing camera raw files:

- **Thumbnail generation** produces a preview image embedded in or derived from the raw file, enabling fast visual browsing without decoding the full sensor data.
- **Metadata extraction** reads the embedded EXIF and manufacturer-specific information, such as camera settings, exposure values, and capture details stored within the raw file.
- **Width/Height detection** determines the pixel dimensions of the image, which is essential for layout, cataloging, and downstream processing.

| File format | Thumbnail generation | Metadata extraction | Width/Height |
| ----------- | -------------------- | ------------------- | ------------ |
| 3FR         | &#10003;             | &#10003;            | &#10003;     |
| ARW         | &#10003;             | &#10003;            | &#10003;     |
| CR2         | &#10003;             | &#10003;            | &#10003;     |
| CR3         | &#10003;             | &#10003;            | &#10003;     |
| CRW         | &#10003;             | &#10003;            | &#10003;     |
| DCR         | &#10003;             | &#10003;            | &#10003;     |
| DNG         | &#10003;             | &#10003;            | &#10003;     |
| ERF         | &#10003;             | &#10003;            | &#10003;     |
| FFF         | &#10003;             | &#10003;            | &#10003;     |
| GPR         | &#10003;             | &#10003;            | &#10003;     |
| IIQ         | &#10003;             | &#10003;            | &#10003;     |
| KDC         | &#10003;             | &#10003;            | &#10003;     |
| MEF         | &#10003;             | &#10003;            | &#10003;     |
| MFW         | &#10003;             | &#10003;            | &#10003;     |
| MOS         | &#10003;             | &#10003;            | &#10003;     |
| MRW         | &#10003;             | &#10003;            | &#10003;     |
| NEF         | &#10003;             | &#10003;            | &#10003;     |
| NRW         | &#10003;             | &#10003;            | &#10003;     |
| ORF         | &#10003;             | &#10003;            | &#10003;     |
| PEF         | &#10003;             | &#10003;            | &#10003;     |
| RAF         | &#10003;             | &#10003;            | &#10003;     |
| RAW         | &#10003;             | &#10003;            | &#10003;     |
| RW2         | &#10003;             | &#10003;            | &#10003;     |
| RWL         | &#10003;             | &#10003;            | &#10003;     |
| SRF         | &#10003;             | &#10003;            | &#10003;     |
| SRW         | &#10003;             | &#10003;            | &#10003;     |
| X3F         | &#10003;             | &#10003;            | &#10003;     |

### Manufacturer origins of listed raw formats

Camera raw formats are largely proprietary standards tied to specific camera manufacturers, which is why the list spans so many distinct file extensions. As general background, several of the supported extensions map to well-known camera makers:

- **CR2** and **CR3** (Canon Raw version 2 and 3), along with **CRW**, are associated with Canon cameras.
- **NEF** (Nikon Electronic Format) and **NRW** are Nikon raw formats.
- **ARW**, **SRF**, and **SRW** correspond to Sony and Samsung raw imaging.
- **ORF** is the Olympus raw format, **RAF** is associated with Fujifilm, **RW2** and **RWL** with Panasonic and Leica.
- **PEF** and **DCR**/**KDC** are linked to Pentax and Kodak imaging.
- **DNG** (Digital Negative) is an open, non-proprietary raw archival format designed for broad cross-manufacturer compatibility.
- Additional formats such as **3FR**, **FFF**, **IIQ**, **MEF**, **MFW**, **MOS**, **MRW**, **ERF**, **GPR**, and **X3F** originate from medium-format, action-camera, and specialized sensor systems.

Because all listed formats deliver identical support for thumbnail generation, metadata extraction, and dimension detection, users can rely on consistent behavior regardless of which camera manufacturer produced the raw file. This broad, uniform coverage ensures that files from a wide range of camera systems can be previewed, cataloged, and processed without format-specific limitations.

## Document formats {#document-formats}

Asset management features support **19 document formats**, spanning word processing, spreadsheet, presentation, publishing, and markup file types. The following matrix specifies which capabilities apply to each format.

### Capability definitions

Each column in the compatibility matrix corresponds to a distinct asset management capability:

- **Thumbnail generation** — produces a visual preview image of the document, enabling faster identification when browsing large asset libraries.
- **Full-text extraction** — indexes the document's text content so it can be searched, improving discoverability across the repository.
- **Width/Height** — captures the document's dimensional metadata, which supports layout-aware handling and rendering.
- **Metadata management** — reads and stores embedded document properties, allowing assets to be organized, filtered, and governed by their attributes.
- **[Connected [!DNL Assets]](use-assets-across-connected-assets-instances.md)** — makes the asset available for use across connected instances, extending reuse beyond a single environment.
- **Full document preview** — renders the complete document for in-application viewing without requiring the native application.

| File format | Thumbnail generation | Full-text extraction | Width/Height | Metadata management | [Connected [!DNL Assets]](use-assets-across-connected-assets-instances.md) | Full document preview |
| ----------- | -------------------- | ------------------- | ------------ | ------------------- | ---------------- |--------|
| DOC         | -                    | -                   | -            | &#10003;            | &#10003;         | &#10003;|
| DOCX        | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         | &#10003; |
| EPUB        | -                    | &#10003;            | -            | -                   | -                | - |
| HTML        | -                    | &#10003;            | -            | &#10003;            | &#10003;         | - |
| ODF         | &#10003;             | &#10003;            | &#10003;     | -                   | -                | - |
| ODM         | &#10003;             | &#10003;            | &#10003;     | -                   | -                | - |
| ODP         | &#10003;             | &#10003;            | &#10003;     | -                   | -                | - |
| ODS         | &#10003;             | &#10003;            | &#10003;     | -                   | -                | - |
| ODT         | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         | - |
| OFG         | &#10003;             | &#10003;            | &#10003;     | -                   | -                | - |
| PDF         | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         | &#10003;|
| PPT         | -                    | -                   | -            | &#10003;            | &#10003;         | &#10003;|
| PPTX        | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         | &#10003;|
| PS          | -                    | -                   | &#10003;     | -                   | -                | - |
| RTF         | -                    | &#10003;            | -            | &#10003;            | &#10003;         | &#10003;|
| TXT         | &#10003;             | &#10003;            | -            | &#10003;            | &#10003;         | &#10003;|
| XLS         | -                    | -                   | -            | &#10003;            | &#10003;         | &#10003;|
| XLSX        | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         | &#10003;|
| XML         | -                    | &#10003;            | -            | -                   | -                |- |

### Format abbreviations

For reference, the format codes in the matrix correspond to the following common document types:

- **DOC / DOCX** — Microsoft Word documents (legacy and Open XML formats)
- **EPUB** — Electronic Publication e-book format
- **HTML** — HyperText Markup Language documents
- **ODF / ODM / ODP / ODS / ODT / OFG** — OpenDocument Format family (formula, master, presentation, spreadsheet, text, and graphics variants)
- **PDF** — Portable Document Format
- **PPT / PPTX** — Microsoft PowerPoint presentations (legacy and Open XML formats)
- **PS** — PostScript
- **RTF** — Rich Text Format
- **TXT** — Plain text
- **XLS / XLSX** — Microsoft Excel spreadsheets (legacy and Open XML formats)
- **XML** — Extensible Markup Language documents

The **Open XML–based formats (DOCX, PPTX, XLSX)** and **PDF** offer the broadest capability coverage, supporting thumbnail generation, full-text extraction, dimensional metadata, metadata management, Connected [!DNL Assets], and full document preview. This comprehensive support makes them the most versatile choices for asset workflows that depend on preview, search, and cross-instance reuse.

## Video formats {#video-formats}

The table below lists every supported video **file format** and the processing capabilities available for each. Support varies by format: some formats can be fully processed for thumbnails, metadata, and delivery, while others are limited to a subset of these operations.

**Legend — what each column means:**

- **File format** — the video container or codec type, identified by its common extension (for example, **MP4**, **MOV**, **AVI**, and **WebM** are among the most widely used web-compatible video containers).
- **Thumbnail generation** — the format supports automatic creation of a still preview image.
- **Metadata extraction** — the format allows technical metadata (such as duration, codec, and frame details) to be read from the file.
- **Width/Height** — the format's pixel dimensions can be detected automatically.
- **Preview** — the format can be previewed directly.
- **Output** — the format is supported as a delivery/output format for playback or distribution.

A checkmark (**✓**) indicates the capability is supported for that format; a dash (**-**) indicates it is not supported.

| File format | Thumbnail generation | Metadata extraction | Width/Height | Preview | Output |
| ----------- | -------------------- | ------------------- | ------------ | ------- | ------- |
| 3G2         | -                    | &#10003;            | -            | -       |  -           |
| 3GP         | -                    | &#10003;            | -            | -       | -            |
| AVI         | &#10003;             | &#10003;            | &#10003;     | &#10003;| -            |
| DIVX        | &#10003;             |  -                  | &#10003;     | &#10003;| -             |
| F4V         | &#10003;             | &#10003;            | &#10003;     | &#10003;| -             |
| FLV         | &#10003;             | &#10003;            | &#10003;     | &#10003;| -             |
| M2T         | &#10003;             | -                   | &#10003;     | &#10003;| -             |
| M2TS        | &#10003;             | -                   | &#10003;     | &#10003;| -             |
| M2V         | &#10003;             | -                   | &#10003;     | &#10003;| -             |
| M4V         | &#10003;             | &#10003;            | &#10003;     | &#10003;| -             |
| MKV         | &#10003;             | -                   | &#10003;     | &#10003;| -             |
| MOV         | &#10003;             | &#10003;            | &#10003;     | &#10003;| -             |
| MP4         | &#10003;             | &#10003;            | &#10003;     | &#10003;| &#10003;            |
| MPEG        | &#10003;             | &#10003;            | &#10003;     | &#10003;| -             |
| MPG         | &#10003;             | &#10003;            | &#10003;     | &#10003;| -             |
| MTS         | &#10003;             | -                   | &#10003;     | &#10003;| -             |
| MXF         | &#10003;             | -                   | &#10003;     | &#10003;| -             |
| OGV         | &#10003;             | -                   | &#10003;     | &#10003;| -             |
| QT          | &#10003;             | -                   | &#10003;     | &#10003;| -             |
| R3D         | -                    | &#10003;            | &#10003;     | &#10003;| -             |
| SWF         | &#10003;             | -                   | &#10003;     | &#10003;| -             |
| WebM        | &#10003;             | -                   | &#10003;     | &#10003;| &#10003;             |
| WMV         | &#10003;             | &#10003;            | &#10003;     | &#10003;| -             |

**Formats supporting output:** Only **MP4** and **WebM** are marked as supported **Output** formats. This reflects their role as the standard delivery containers for modern web and streaming playback, ensuring broad compatibility across browsers and devices. Most other listed formats support **thumbnail generation, preview, and dimension detection** for ingest and processing but are not intended as final output containers.

Note that support for **metadata extraction** and **thumbnail generation** is not uniform across all formats — for example, container formats such as **3G2** and **3GP** support metadata extraction but not thumbnail generation or preview, because their intended use and internal structure limit which operations can be performed. Formats such as **AVI**, **F4V**, **FLV**, **M4V**, **MOV**, **MP4**, **MPEG**, **MPG**, and **WMV** offer the fullest set of processing capabilities among ingest formats.

## Audio formats {#audio-formats}

**[!DNL Assets] as a [!DNL Cloud Service] supports Extensible Metadata Platform (XMP) metadata extraction for six audio formats: AIF, ASF, M4A, MP3, WAV, and WMA.** XMP metadata extraction reads the embedded descriptive information stored within an audio file—such as title, artist, copyright, and other tagging fields—and makes it available within the asset management system. This enables uploaded audio assets to be searched, filtered, and organized based on their intrinsic metadata rather than filename alone.

The supported audio formats include:

- **AIF (Audio Interchange File Format):** An uncompressed audio format commonly used for high-quality audio storage.
- **ASF (Advanced Systems Format):** A container format designed for streaming media.
- **M4A (MPEG-4 Audio):** A compressed audio format widely used for music and audiobooks.
- **MP3 (MPEG-1 Audio Layer III):** One of the most widely adopted compressed audio formats for general-purpose audio distribution.
- **WAV (Waveform Audio File Format):** An uncompressed audio format favored for high-fidelity and professional audio work.
- **WMA (Windows Media Audio):** A compressed audio format developed within the Windows Media ecosystem.

Because XMP metadata is extracted automatically for each of these formats, ingested audio assets carry their descriptive tags into the platform, improving discoverability and streamlining large-scale digital asset management.

## Supported inputs formats for audio and video transcription {#audio-video-transcription-formats}

The following container and file formats are supported for audio and video transcription. Each entry lists the format name, the applicable codecs where relevant, and the accepted file extensions (shown in parentheses) that identify the input file type.

* **FLV** (with **H.264** and **AAC** codecs) (**.flv**)
* **MXF** (**.mxf**)
* **MPEG2-PS**, **MPEG2-TS**, **3GP** (**.ts**, **.ps**, **.3gp**, **.3gpp**, **.mpg**)
* **Windows Media Video (WMV)/ASF** (**.wmv**, **.asf**)
* **AVI** (Uncompressed 8 bit/10 bit) (**.avi**)
* **MP4** (**.mp4**, **.m4a**, **.m4v**)
* **Microsoft&reg; Digital Video Recording (DVR-MS)** (**.dvr-ms**)
* **Matroska/WebM** (**.mkv**)
* **WAVE/WAV** (**.wav**)
* **QuickTime** (**.mov**)

## Tips and limitations {#limitations-and-tips}

### File size limits for metadata extraction

Key limitations to keep in mind include:

* **The file size limit for metadata extraction is approximately 15 GB.** When uploading large assets that approach or exceed this threshold, the metadata extraction operation can fail. This happens because the extraction process must scan and parse the entire file within available processing limits, and very large assets increase the processing time and resources required to complete extraction successfully.

* **Metadata extraction is most reliable for assets that stay comfortably within the size limit.** As a practical result, keeping individual files under **approximately 15 GB** helps ensure that metadata is extracted consistently and without interruption. If extraction fails on a large asset, reducing the file size, splitting the asset into smaller components, or re-uploading can help the extraction operation complete as expected.

## [!DNL Dynamic Media] - Supported input video formats for transcoding {#video-dynamic-media-transcoding}

[!DNL Dynamic Media] transcoding accepts a defined set of input video formats, and successful transcoding depends on matching the correct **container** (such as MP4, MOV, or WMV) with a **recommended video codec** (such as **H264/AVC — Advanced Video Coding**). Each supported container is paired below with the codecs known to transcode reliably, alongside the codecs that are unsupported and will not process correctly. Selecting a recommended codec for the container ensures the source video is accepted and converted without failure.

| Video file extension | Container | Recommended video codecs | Unsupported video codecs |
| --- | --- | --- | --- |
| AVI                  | A/V Interleave     | XVID, DIVX, HDV, MiniDV (DV25), Techsmith Camtasia, Huffyuv, Fraps, Panasonic DVCPro | Indeo3 (IV30), MJPEG, Microsoft&reg; Video 1 (MS-CRAM) |
| FLV, F4V             | Adobe Flash        | H264/AVC, Flix VP6, H263, Sorenson | SWF (vector animation files) |
| M4V                  | Apple iTunes       | H264/AVC                    | &minus; |
| MKV                  | Matroska           | H264/AVC                    | &minus; |
| MOV, QT              | Apple QuickTime    | H264/AVC, Apple ProRes422  & HQ, Sony XDCAM, Sony DVCAM, HDV, Panasonic DVCPro, Apple DV  (DV25), Apple PhotoJPEG, Sorenson, Avid DNxHD, Avid AVR | Apple Intermediate, Apple Animation  |
| MP4                  | MPEG-4             | H264/AVC (all profiles)     | &minus; |
| MPG, VOB, M2V, MP2   | MPEG-2             | MPEG-2                      | &minus; |
| MXF &Dagger;         | MXF                | Sony XDCAM, MPEG-2, MPEG-4, Panasonic DVCPro | &minus; |
| OGV, OGG             | OGG                | Theora, VP3, Dirac          | &minus; |
| WebM                 | WebM               | Google VP8                  | &minus; |
| WMV                  | Windows Media 9    | WMV3 (v9), WMV2 (v8), WMV1 (v7), GoToMeeting (G2M2, G2M3, G2M4)  | Microsoft&reg; Screen (MSS2), Microsoft&reg; Photo Story (WVP2) |

&Dagger; The **MXF (Material Exchange Format)** container is not yet supported for use with Interactive Videos in [!DNL Dynamic Media] or for use with Annotation in [!DNL Experience Manager Assets]. As a result, MXF source files can still be transcoded through the standard formats above, but workflows that depend on Interactive Video or Annotation features must use an alternative supported container.

## [!DNL Dynamic Media] - Supported document formats {#document-support-dynamic-media}

[!DNL Adobe Experience Manager] [!DNL Dynamic Media] supports three document input formats: **[!DNL Adobe Illustrator] (AI)**, **[!DNL Adobe InDesign] (INDD)**, and **Portable Document Format (PDF)**. The table below establishes exactly which operations each format supports across the full asset workflow — from initial upload through dynamic rendition delivery.

### Supported input and output formats

| Format | Upload (Input format) | Create image preset (Output format) | Preview dynamic rendition | Deliver dynamic rendition | Download dynamic rendition |
| ------ | --------------------- | ----------------------------------- | ------------------------- | ------------------------- | -------------------------- |
| AI     | ✓                     | -                                   | -                         | -                         | -                          |
| INDD   | ✓                     | -                                   | -                         | -                         | -                          |
| PDF (See Note below)    | ✓                     | ✓                                   | ✓                         | ✓                         | ✓                          |

**Portable Document Format (PDF)** is the most fully supported document format in [!DNL Dynamic Media]. PDF supports every stage of the workflow: **Upload**, **Create image preset**, **Preview dynamic rendition**, **Deliver dynamic rendition**, and **Download dynamic rendition**. In contrast, **[!DNL Adobe Illustrator] (AI)** and **[!DNL Adobe InDesign] (INDD)** support **Upload only** — these formats can be ingested into [!DNL Dynamic Media], but they cannot be used to create image presets or to preview, deliver, or download dynamic renditions.

Each column represents a distinct step in the [!DNL Dynamic Media] pipeline:

- **Upload (Input format):** The format can be ingested into [!DNL Dynamic Media] as a source asset.
- **Create image preset (Output format):** The format can be processed into an image preset for reuse across renditions.
- **Preview dynamic rendition:** A dynamically generated rendition of the asset can be previewed.
- **Deliver dynamic rendition:** A dynamically generated rendition can be delivered to a website, application, or other endpoint.
- **Download dynamic rendition:** A dynamically generated rendition can be downloaded.

Because AI and INDD are native design source files, they are supported for upload as source assets, while PDF — a portable, print-and-web-ready delivery format — flows through the entire rendition workflow.

### Secure PDF handling

>[!NOTE]
>
>For secure PDFs, only Upload is supported.

For secure (password-protected or permission-restricted) PDFs, only **Upload** is supported. This means a secure PDF can be ingested into [!DNL Dynamic Media], but it cannot be used to create image presets or to preview, deliver, or download dynamic renditions. This restriction reflects the access controls embedded in secure PDF files, which limit the downstream processing that [!DNL Dynamic Media] can perform on them.

## [!DNL Dynamic Media] - Supported raster image formats {#image-support-dynamic-media}

[!DNL Adobe Experience Manager] **[!DNL Dynamic Media]** supports a defined set of raster image formats, and each format differs in whether it can be uploaded, converted through an image preset, previewed, delivered, downloaded, or used within specific set types. The table below maps every supported format against these capabilities. A **dynamic rendition** is an on-demand, dynamically generated version of an image that [!DNL Dynamic Media] serves at request time, which is why delivery support is a key distinction between formats.

The supported formats include **AVIF** (AV1 Image File Format), **BMP** (Bitmap), **EPS** (Encapsulated PostScript), **GIF** (Graphics Interchange Format), **HEIC** (High Efficiency Image Container), **JPEG** (Joint Photographic Experts Group), **PICT**, **PNG** (Portable Network Graphics), **PSD** (Photoshop Document), **TIFF** (Tagged Image File Format), and **WEBP**.

| Format | Upload (Input format) | Create image preset (Output format) | Preview dynamic rendition | Deliver dynamic rendition | Download dynamic rendition | Set types that support this format |
|---|:---:|:---:|:---:|:---:|:---:| --- |
| AVIF | &minus; | &minus; | &minus; | &#10003; | &minus; | &minus; |
| BMP | &#10003; | &minus;| &minus; | &minus; | &minus; | [Image](/help/assets/dynamic-media/image-sets.md), [Mixed Media](/help/assets/dynamic-media/mixed-media-sets.md), and [Spin](/help/assets/dynamic-media/spin-sets.md) |
| [EPS](/help/assets/dynamic-media/managing-image-presets.md#adobe-illustrator-ai-postscript-eps-and-pdf-file-formats) | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | &minus; |
| GIF | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | &minus; |
| HEIC | &minus; | &minus; | &minus; | &#10003; |&minus; | &minus; |
| JPEG | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | [Image](/help/assets/dynamic-media/image-sets.md), [Mixed Media](/help/assets/dynamic-media/mixed-media-sets.md), and [Spin](/help/assets/dynamic-media/spin-sets.md) |
| PICT | &#10003; | &minus; | &minus; | &minus; | &minus; | &minus; |
| PNG | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | [Image](/help/assets/dynamic-media/image-sets.md), [Mixed Media](/help/assets/dynamic-media/mixed-media-sets.md), and [Spin](/help/assets/dynamic-media/spin-sets.md) |
| PSD &Dagger; | &#10003;| &minus; | &minus; | &minus; | &minus; | &minus; |
| TIFF | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | [Image](/help/assets/dynamic-media/image-sets.md), [Mixed Media](/help/assets/dynamic-media/mixed-media-sets.md), and [Spin](/help/assets/dynamic-media/spin-sets.md) |
| WEBP | &minus; | &minus; | &minus; | &#10003; | &minus; | &minus; |

<!-- AVIF, HEIC, and WebP added to table above on March 4, 2024 based on CQDOC-21294 -->

### How to read the capability columns

- **Upload (Input format):** The format can be ingested into [!DNL Dynamic Media] as a source asset.
- **Create image preset (Output format):** The format can be generated as an output through an image preset.
- **Preview dynamic rendition:** A dynamically generated version of the asset can be previewed within the interface.
- **Deliver dynamic rendition:** The dynamically generated version can be served at request time to end users.
- **Download dynamic rendition:** The generated rendition can be downloaded.
- **Set types that support this format:** The specific set types — **Image**, **Mixed Media**, and **Spin** — in which the format can be used.

Formats that support the full pipeline — upload, preset creation, preview, delivery, and download — include **EPS**, **GIF**, **JPEG**, **PNG**, and **TIFF**. By contrast, **AVIF**, **HEIC**, and **WEBP** support delivery of a dynamic rendition only, without upload, preset creation, preview, or download. **BMP**, **JPEG**, **PNG**, and **TIFF** are the formats supported across the **Image**, **Mixed Media**, and **Spin** set types.

### About the merged image extracted from PSD files

&Dagger; For **PSD (Photoshop Document)** files, the merged image is extracted from the PSD file. This merged image is generated by [!DNL Adobe Photoshop] and is embedded within the PSD file itself. Depending on how the file was saved and its settings, the merged image may or may not match the actual composite image, so the extracted result can differ from what the original layered document displays.

## [!DNL Dynamic Media] - Unsupported raster image formats {#unsupported-raster-image-formats-dm}

[!DNL Dynamic Media] does not support the following subtypes of raster image file formats. Files matching these criteria fail to process because their encoding, color space, or bit depth falls outside the supported range:

* **PNG (Portable Network Graphics) files with an IDAT chunk size greater than 100 MB.** The IDAT chunk stores the compressed image data, and chunks above this threshold exceed the processing limit.
* **PSB (Large Document Format / Photoshop Big) files** — the extended Photoshop format used for documents larger than the standard PSD size limit.
* **PSD (Photoshop Document) files in a color space other than CMYK, RGB, Grayscale, or Bitmap.** DuoTone, Lab, and Indexed color spaces are not supported.
* **PSD files with a bit depth greater than 16 bits per channel.**
* **TIFF (Tagged Image File Format) files that contain floating point data.**
* **TIFF files in the Lab color space.**

## [!DNL Dynamic Media] - Supported 3D file formats {#support-3d-formats-dynamic-media}

See also [3D formats supported](/help/assets/file-format-support.md#support-3d-formats)

Adobe [!DNL Dynamic Media] supports four primary 3D file formats for asset ingestion and delivery: **GLB**, **OBJ**, **STL**, and **USDZ**. Each format serves distinct workflows, from web-based interactive viewing to 3D printing and native mobile augmented-reality experiences.

| 3D file extension | File format | MIME type | Notes |
|---|---|---|---|
| **GLB** | Binary GL Transmission Format (glTF Binary) | **model/gltf-binary** | Packages the geometry, **materials, and textures as a single self-contained asset**. Because everything is bundled into one file, GLB is efficient to transmit and is widely used for real-time and web-based 3D rendering. |
| **OBJ** | WaveFront 3D Object File | **application/x-tgif** | A widely adopted, text-based format that stores 3D geometry such as vertices, faces, and surface data. OBJ is commonly used across 3D modeling and design applications, and materials are typically referenced through an accompanying material file. |
| **STL** | Stereolithography | **application/vnd.ms-pki.stl** | A standard geometry format that describes the surface of a 3D model as a mesh of triangles. STL is the established format for **3D printing** and computer-aided manufacturing, focusing on shape rather than color or texture. |
| **USDZ** | Universal Scene Description Zip archive | **model/vnd.usdz+zip** | *Support for ingestion and thumbnail generation; 3D previews are not yet supported.* USDZ is a 3D format that can be viewed natively in **Safari or iOS**, making it well suited for augmented-reality (AR) experiences on Apple devices. |

## Asset file format support and validation {#asset-file-format-support-and-validation}

[!DNL Adobe Experience Manager] (AEM) [!DNL Assets] processing relies on **two distinct mechanisms**, and each behaves differently when a file type is not fully supported. Identifying which mechanism is failing is the fastest way to determine whether the observed behavior is expected or whether it indicates a problem that requires a fix.

The two mechanisms are:

- **Standard renditions** — Always requested for every asset and non-configurable. Because standard renditions run automatically on all ingested assets, they represent the baseline processing that AEM applies regardless of asset type.
- **[!DNL Dynamic Media] or custom processing profiles** — Fully configurable and can be scoped by the MIME (Multipurpose Internet Mail Extensions) type or by asset selection criteria. This configurability allows these profiles to target specific file types or subsets of assets rather than applying uniformly.

### Why the distinction matters

The key difference lies in configurability. **Standard renditions** apply to every asset and cannot be adjusted, while **[!DNL Dynamic Media] or custom processing profiles** are configurable and selectively scoped. As a result, when a file type is not fully supported, the two mechanisms can produce different outcomes.

Determining which mechanism is failing clarifies whether the result is expected behavior or an issue to troubleshoot. If a failure originates from a non-configurable standard rendition, the behavior reflects AEM's baseline handling of that file type. If it originates from a configurable processing profile, the scope defined by MIME type or asset selection criteria is the more likely factor to investigate.

### Expected Rendition Failures {#expected-rendition-failures}

**Rendition failures for inapplicable formats are expected, by-design behavior in AEM — not a misconfiguration.** [!DNL Adobe Experience Manager] (AEM) asset microservices always request a fixed set of standard renditions for every uploaded asset, regardless of its MIME (Multipurpose Internet Mail Extensions) type. This fixed set includes text extraction and an MP4 (video) preview, which the pipeline attempts uniformly across all assets.

Because this request set is applied uniformly, certain renditions are inherently inapplicable to certain asset types. For a PNG (Portable Network Graphics) image, the following renditions cannot be produced:

- **`cqdam.text.txt`** — a text-extraction rendition intended for documents and other text-bearing assets. An image contains no extractable body text, so this rendition cannot be generated.
- **`cq5dam.preview.mp4`** — a video preview rendition intended for moving-image assets. A static image has no video stream to encode, so this rendition cannot be generated.

Because these renditions do not apply to the asset's actual format, they are recorded as entries in **`dam:failedRenditions`**. This is expected, by-design behavior and not a misconfiguration.

The presence of such entries is harmless as long as the renditions **relevant to the asset's actual type** complete successfully. For an image asset, this means:

- **Standard image renditions** generate as expected.
- **[!DNL Dynamic Media] processing** for the image completes successfully.

In other words, `dam:failedRenditions` entries for formats that do not apply to a given asset type indicate the pipeline correctly skipping non-applicable outputs, rather than a genuine processing error. Investigation is only warranted when a rendition that *is* relevant to the asset's actual type fails.

### Unsupported or restricted input formats {#unsupported-or-restricted-input-formats}

The following formats and scenarios are known to be unsupported or restricted for asset processing in [!DNL Adobe Experience Manager] (AEM) as a [!DNL Cloud Service], along with the observed behavior and recommended remediation for each.

| File type or scenario | Behavior | Guidance |
|---|---|---|
| ZIP files sent through [!DNL Dynamic Media] processing profiles | Processing step fails explicitly with an unsupported-format error. This causes the workflow instance to accumulate in an unhealthy or retrying state at scale. | Exclude ZIP (and other archive or 3D package files) from [!DNL Dynamic Media] processing profiles using asset selection criteria so the profile is never applied to non-media file types in the first place. |
| AVIF images| File is stored in the Digital Asset Management (DAM), but AEM does not process it and no thumbnail or preview is generated. | AVIF is not a supported input format for asset processing in AEM as a cloud service. Convert to JPG or PNG before uploading if a preview or rendition is required. |
| JFIF images | This is not recognized as an image or JPEG because of the file extension. The standard image processing pipeline does not run, so no renditions are generated. | Rename or re-export the JFIF files as .JPG before uploading. |
| PPTX files containing restricted (read-only or licensed) fonts, for example, Avenir| PDF rendition generation fails; the file is reported as corrupted by the PDF conversion microservice (the same underlying service used by Acrobat) | Restricted fonts not bundled with Windows and blocked from export by the font vendor causes conversion failures independent of AEM. Replace the restricted fonts in the source file before uploading. Local conversion in Acrobat can be used to confirm whether a given PPTX fails before uploading, since it uses the same conversion service. |
| SVG files missing the `offset` attribute on `<stop>` elements| [!DNL Dynamic Media]'s image server returns **HTTP 403** through `/is/image` for that specific file, while `/is/content` still renders it. This is because SVG violates the **SVG 1.1** compliance.| Validate SVGs against the **SVG 1.1** compliance, for example, with the W3C Validator before uploading. Re-export from the source tool, for example, Illustrator with **SVG 1.1** compliance.|
| Files with MIME (Multipurpose Internet Mail Extensions) types outside the configured allow-list, for example, `.pem` certificates| Upload is rejected in the user interface. | AEM [!DNL Assets] can technically store any binary file, but an organization's asset upload restrictions can limit the accepted MIME types. Update the allowed MIME type list globally, or per folder to include the required type. |
| Metadata values in a bulk CSV (comma-separated values) import that start with or contain reserved characters such as `#`, `/`, `;`, backslash symbol, pipe symbol, `[`, `]`, `%`, `{`, `}`, `?`, `&` | The parser skips or ignores the affected metadata entry silently, without a hard failure, so the import completes but the value is lost.| Remove or replace the reserved characters in metadata values before running a bulk CSV metadata import. |
| DAM assets carrying non-standard or unregistered XML metadata namespaces, for example, `exifEX`, `mwg-rs`, `photomechanic`| Content package import or copy between the environments fail with messages such as unknown namespace prefix or no namespace mapping found. | Identify and clean the offending metadata properties on the source assets (they are often introduced by the external tools) before re-attempting the package import or content copy. |

### Restricting upload types per folder {#restricting-upload-types-per-folder}

**Folder-specific upload restrictions let you accept only certain file types within a single folder, while leaving the rest of the repository untouched.** By default, **Multipurpose Internet Mail Extensions (MIME)** type restrictions apply **globally** across the entire **Digital Asset Management (DAM)** system, but these global rules can be overridden at the **folder level** to enforce tighter, location-specific controls.

To configure allowed MIME types for a specific folder — for example, `/content/dam/projects` — follow these steps:

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Assets Configuration]**.
2. Select the target folder path (such as `/content/dam/projects`).
3. List **only** the MIME types that should be accepted for that folder.

Because the folder configuration acts as an explicit allowlist, any MIME type not on the list is automatically blocked for that folder. As a result, common formats such as Excel spreadsheets are rejected in that folder specifically, without affecting uploads anywhere else in the DAM. This scoped approach ensures that each folder can enforce its own content standards — keeping project directories, brand asset stores, or department-specific folders limited to their intended file types while the broader repository continues to operate under its global rules.

### XMP metadata writeback conflicts {#XMP-metadata-writeback-conflicts}

Concurrent updates to an asset's metadata node (`cqdam.metadata.xml`)—for example, from multiple custom workflows or services writing to the same asset at once—can produce repository conflicts (**`InvalidItemStateException`**, **`CommitFailedException`**) during Extensible Metadata Platform (XMP) writeback. These conflicts occur because each save operation expects the metadata node to be in a consistent, unchanged state; when two processes modify the same node simultaneously, the repository detects that the underlying item has already changed and rejects the stale write. As a result, one or more of the competing operations fails rather than silently overwriting the other.

**Common symptoms and causes**

Because these failed writes are frequently retried, repeated failures of this kind accumulate into a backlog of unhealthy or retrying workflow instances. Left unmanaged, this backlog can compound over time, degrading overall workflow throughput and making the root cause harder to diagnose.

**Recommended resolution**

To prevent XMP writeback conflicts and reduce the resulting workflow backlog, apply the following measures:

* **Serialize concurrent metadata writes.** Review custom workflows or services for concurrent writes to the same asset's metadata node, and serialize them so that only one process writes to a given metadata node at a time. Coordinating access in this way removes the contention that triggers `InvalidItemStateException` and `CommitFailedException`.
* **Enable workflow purge maintenance.** Enable and configure workflow purge maintenance so that completed and stale workflow instances are cleaned up automatically rather than accumulating. This keeps the workflow inbox healthy and prevents transient writeback failures from building into a persistent backlog.

### Troubleshooting checklist {#troubleshooting-checklist}

1. **Rule out format-inapplicable renditions.** If a rendition failure only affects a rendition type that does not apply to the asset's format—for example, a video preview requested on an image—treat it as expected behavior, not an error. Verify instead that the **format-appropriate renditions** for that asset succeeded.
2. **Correct profile selection criteria for excluded file types.** If a processing profile is failing on files that were never meant to be processed by it—for example, **ZIP archives** or **3D packages**—fix the profile's asset selection criteria rather than trying to force the file type to process. Restricting the profile to supported formats resolves the failure at its root, because the file was never a valid input in the first place.
3. **Suspect the individual file before the configuration.** If a specific file fails while similar files succeed, suspect the file itself first. Check for **restricted or licensed fonts** (in **PPTX** or **PDF** files), **SVG compliance**, or an **unsupported format or extension mismatch** (such as **AVIF** or **JFIF**) before assuming an [!DNL Adobe Experience Manager] (AEM) configuration issue.
4. **Investigate compounding causes when workflows back up.** If workflows are backing up in an unhealthy state, check for both **unsupported-format processing failures** and **metadata writeback conflicts**. Because these two failure modes can occur simultaneously, they compound one another and accelerate the backlog, so resolving both is necessary to clear it.

**See also**

* [Translate [!DNL Assets]](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage [!DNL Dynamic Media] templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in [!DNL Assets] view](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish [!DNL Assets] to AEM and [!DNL Dynamic Media]](/help/assets/publish-assets-to-aem-and-dm.md)

>[!MORELIKETHIS]
>
>* [Asset processing using asset microservices](asset-microservices-overview.md).
>* [Supported file formats for smart tagging of text-based assets](/help/assets/smart-tags.md#smart-tags-supported-file-formats)
