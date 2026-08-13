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

[!DNL Adobe Experience Manager] as a [!DNL Cloud Service] supports basic content management capabilities &mdash; storage, managing metadata online, versioning, upload and download, and so on &mdash; for any binary file, independent of its format. [!DNL Adobe Experience Manager Assets] supports a wide range of file formats and each product feature has varied support for different formats.

In addition, [!DNL Experience Manager Assets] provides extended support to generate previews and renditions and to extract metadata and text for full-text indexing. This extended support is provided using [asset microservices](asset-microservices-configure-and-use.md).

The highlights for asset conversion using asset microservices include:

* Key [Adobe file formats](#adobe-formats) produced by Adobe applications and services, including [!DNL Adobe Photoshop], [!DNL Adobe InDesign], [!DNL Adobe Illustrator], [!DNL Adobe XD], [!DNL Adobe Dimension], and [!DNL Adobe Acrobat] or PDF.
* Key [imaging file formats](#image-formats).
* [Camera Raw file formats](#camera-raw-formats) for a wide range of cameras, including Canon, Nikon, Fujifilm, Olympus, and other manufacturers (powered by Adobe Camera Raw).
* Common [document formats](#document-formats), including Microsoft&reg; Office and Open Document formats.
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
>Some features might seem to work with other formats, but these formats are not officially supported. Results may be inconsistent, and features may not work as expected.
>To ensure consistent and reliable results, use only the supported formats.

## Adobe formats {#adobe-formats}

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

\* For [!DNL Adobe InDesign] files (INDD), the size of renditions are determined by the preview embedded in the INDD file. Configure the preferences in [!DNL InDesign] (**[!UICONTROL Preferences > File Handling > Always Save Preview Images with Documents, Preview Size]**) so you can embed larger renditions.

## Image formats {#image-formats}

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

## 3D formats {#support-3d-formats}

The following 3D formats are supported.

See also [Work with 3D assets in Dynamic Media](/help/assets/dynamic-media/assets-3d.md).

| Format | Storage | Versioning | Workflow | Publishing | Access control | Thumbnail preview | 3D preview | Dynamic Media delivery |
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

## Document formats {#document-formats}

The document formats supported for asset management features are as follows.

| File format | Thumbnail generation | Full-text extraction | Width/Height | Metadata management | [Connected Assets](use-assets-across-connected-assets-instances.md) | Full document preview |
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

## Video formats {#video-formats}

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

## Audio formats {#audio-formats}

[!DNL Assets] as a [!DNL Cloud Service] provides XMP metadata extraction support for AIF, ASF, M4A, MP3, WAV, and WMA audio formats.

## Supported inputs formats for audio and video transcription {#audio-video-transcription-formats}

* FLV (with H.264 and AAC codecs) (.flv)
* MXF (.mxf)
* MPEG2-PS, MPEG2-TS, 3GP (.ts, .ps, .3gp, .3gpp, .mpg)
* Windows Media Video (WMV)/ASF (.wmv, .asf)
* AVI (Uncompressed 8 bit/10 bit) (.avi)
* MP4 (.mp4, .m4a, .m4v)
* Microsoft&reg; Digital Video Recording(DVR-MS) (.dvr-ms)
* Matroska/WebM (.mkv)
* WAVE/WAV (.wav)
* QuickTime (.mov)

## Asset file format support and validation {#asset-file-format-support-and-validation}

AEM Assets processing has two distinct mechanisms that behave differently when a file type isn't fully supported: standard renditions (always requested for every asset, non-configurable) and Dynamic Media / custom processing profiles (configurable, and can be scoped by MIME type or asset selection criteria). Knowing which one is failing determines whether an error is expected behavior or something to fix.

### Standard rendition failures are often expected, not a defect {#standard-rendition-failures}

AEM's asset microservices always request a fixed set of standard renditions (e.g., text extraction, MP4 preview) for every uploaded asset, regardless of its MIME type. For a PNG image, renditions such as cqdam.text.txt or cq5dam.preview.mp4 are inherently inapplicable and will appear as entries in dam:failedRenditions. This is expected, by-design behavior — not a misconfiguration — as long as the renditions relevant to the asset's actual type (e.g., standard image renditions, Dynamic Media processing for images) complete successfully.

### Unsupported or restricted input formats {#unsupported-or-restricted-input-formats}

| File type / scenario | Behavior | Guidance |
|---|---|---|
| ZIP files sent through Dynamic Media processing profiles | Processing step fails explicitly with an unsupported-format error; can cause workflow instances to accumulate in an unhealthy/retrying state at scale | Exclude ZIP (and other archive/3D package files) from Dynamic Media processing profiles using asset selection criteria so the profile is never applied to non-media file types in the first place. |
| AVIF images| File is stored in the DAM, but AEM does not process it — no thumbnail or preview is generated | AVIF is not a supported input format for asset processing in AEM as a Cloud Service. Convert to JPG or PNG before upload if a preview/rendition is required. |
| JFIF images | Not recognized as image/jpeg because of the file extension; the standard image processing pipeline does not run, so no renditions are generated | Rename or re-export JFIF files as .jpg before upload. |
| PPTX files containing restricted (read-only/licensed) fonts, e.g. Avenir| PDF rendition generation fails; the file is reported as corrupted by the PDF conversion microservice (the same underlying service used by Acrobat) | Restricted fonts not bundled with Windows and blocked from export by the font vendor will cause conversion failures independent of AEM. Replace restricted fonts in the source file before upload. Local conversion in Acrobat can be used to confirm whether a given PPTX will fail before uploading, since it uses the same conversion service. |
| SVG files missing the offset attribute on <stop> elements| Dynamic Media's image server returns HTTP 403 via /is/image for that specific file (while /is/content may still render it), because the SVG violates the SVG 1.1 specification| Validate SVGs against the SVG 1.1 spec (e.g. with the W3C Validator) before upload, and re-export from the source tool (e.g. Illustrator) with SVG 1.1 compliance.|
| Files with MIME types outside the configured allow-list (e.g. .pem certificates)| Upload is rejected in the UI | AEM Assets can technically store any binary file, but an organization's asset upload restrictions may limit accepted MIME types. Update the allowed MIME type list (globally, or per folder — see below) to include the required type. |
| Metadata values in a bulk CSV import that start with or contain reserved characters (#, /, ;, \, [, ], %, {, }, ?, &, pipe symbol)| The parser skips or ignores the affected metadata entry without a hard failure| Remove or replace reserved characters in metadata values before running a bulk CSV metadata import. |
| DAM assets carrying non-standard/unregistered XML metadata namespaces (e.g. exifEX, mwg-rs, photomechanic)| Content package import/copy between environments fails with "Unknown namespace prefix" or "No namespace mapping found" | Identify and clean the offending metadata properties on the source assets (they are often introduced by external tools) before re-attempting the package import/content copy. |

### Restricting upload types per folder {#restricting-upload-types-per-folder}

Out-of-the-box MIME type restrictions apply globally across the DAM by default, but folder-specific restrictions are also possible: configure the allowed MIME types for a specific folder (e.g. /content/dam/projects) via Tools > Assets > Assets Configuration, listing only the MIME types that should be accepted for that folder — all other types, including common ones like Excel spreadsheets, will then be blocked for that folder specifically without affecting the rest of the DAM.

### XMP metadata writeback conflicts {#XMP-metadata-writeback-conflicts}

Concurrent updates to an asset's metadata node (cqdam.metadata.xml) — for example, from multiple custom workflows or services writing to the same asset at once — can produce repository conflicts (InvalidItemStateException, CommitFailedException) during XMP writeback. Repeated failures of this kind can also contribute to a backlog of unhealthy/retrying workflow instances. To avoid this:

* Review custom workflows or services for concurrent writes to the same asset's metadata, and serialize them where possible.
* Enable and configure workflow purge maintenance so that completed and stale workflow instances are cleaned up automatically rather than accumulating.

### Troubleshooting checklist {#troubleshooting-checklist}

1. If a rendition failure only affects a rendition type that doesn't apply to the asset's format (e.g. video preview on an image), treat it as expected — check whether the format-appropriate renditions succeeded instead.
2. If a processing profile is failing on files that were never meant to be processed by it (e.g. ZIP, 3D packages), fix the profile's asset selection criteria rather than trying to make the file type "work."
3. If a specific file fails while similar files succeed, suspect the file itself first: check for restricted/licensed fonts (PPTX/PDF), SVG spec compliance, or an unsupported format/extension mismatch (AVIF, JFIF) before assuming an AEM configuration issue.
4. If workflows are backing up in an unhealthy state, check for both unsupported-format processing failures and metadata writeback conflicts — they can co-occur and compound the backlog.

## Tips and limitations {#limitations-and-tips}

* Currently, the file size limit for metadata extraction is approximately 15 GB. When uploading large assets, sometimes the metadata extraction operation fails.

## Dynamic Media - Supported input video formats for transcoding {#video-dynamic-media-transcoding}

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

&Dagger; This video format is not yet supported for use with Interactive Videos in Dynamic Media or for use with Annotation in Experience Manager Assets.

## Dynamic Media - Supported document formats {#document-support-dynamic-media}

| Format | Upload (Input format) | Create image preset (Output format) | Preview dynamic rendition | Deliver dynamic rendition | Download dynamic rendition |
| ------ | --------------------- | ----------------------------------- | ------------------------- | ------------------------- | -------------------------- |
| AI     | ✓                     | -                                   | -                         | -                         | -                          |
| INDD   | ✓                     | -                                   | -                         | -                         | -                          |
| PDF (See Note below)    | ✓                     | ✓                                   | ✓                         | ✓                         | ✓                          |

>[!NOTE]
>
>For secure PDFs, only Upload is supported.

## Dynamic Media - Supported raster image formats {#image-support-dynamic-media}

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

‡ The merged image is extracted from the PSD file. It is an image that is generated by [!DNL Adobe Photoshop] and is included in the PSD file. Depending on the settings, the merged image may or may not be the actual image.

## Dynamic Media - Unsupported raster image formats {#unsupported-raster-image-formats-dm}

The following subtypes of raster image file formats that are *not* supported in [!DNL Dynamic Media]:

* PNG files that have an IDAT chunk size greater than 100 MB.
* PSB files.
* PSD files with a color space other than CMYK, RGB, Grayscale, or Bitmap are not supported. DuoTone, Lab, and Indexed color spaces are not supported.
* PSD files that have a bit depth greater than 16.
* TIFF files that have floating point data.
* TIFF files that have Lab color space.

## Dynamic Media - Supported 3D file formats {#support-3d-formats-dynamic-media}

See also [3D formats supported](/help/assets/file-format-support.md#support-3d-formats)

| 3D file extension | File format | MIME type | Notes |
|---|---|---|---|
| GLB | Binary GL Transmission|model/gltf-binary | Includes the materials and textures as a single asset. |
| OBJ | WaveFront 3D Object File|application/x-tgif | |
| STL | Stereolithography|application/vnd.ms-pki.stl | |
| USDZ | Universal Scene Description Zip archive|model/vnd.usdz+zip |*Support for ingestion and thumbnail generation; 3D previews not yet supported.* USDZ is a 3D format that can be viewed natively by Safari or iOS. |

**See also**

* [Translate Assets](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in Assets view](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)

>[!MORELIKETHIS]
>
>* [Asset processing using asset microservices](asset-microservices-overview.md).
>* [Supported file formats for smart tagging of text-based assets](/help/assets/smart-tags.md#smart-tags-supported-file-formats)

