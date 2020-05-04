---
title: File formats and MIME types supported by Experience Manager Assets as a Cloud Service
description: File formats and MIME types supported by Experience Manager Assets as a Cloud Service.
contentOwner: AG
---

# Assets supported file formats {#supported-file-formats}

Adobe Experience Manager as a Cloud Service supports basic content management capabilities &mdash; storage, managing metadata online, versioning, upload and download, and so on &mdash; for any binary file, independent of its format. Adobe Experience Manager Assets supports a wide range of file formats and each product feature has varied support for different formats.

In addition, Experience Manager Assets provides extended support to generate previews and renditions and to extract metadata and text for full-text indexing. This extended support is provided using [asset microservices](asset-microservices-configure-and-use.md).

The following legend describes the level of support.

| Support level |         Description         |
| ------------- | --------------------------- |
| &#10003;      | Supported                   |
| *             | See remarks below the table |
| -             | Not applicable              |

## Asset conversion using asset microservices {#asset-microservices-supported-formats}

The highlights include:

* Key [Adobe file formats](#adobe-formats) produced by Adobe applications and services, including Adobe Photoshop, Adobe InDesign, Adobe Illustrator, Adobe XD, Adobe Dimension, and Adobe Acrobat or PDF.
* Key [imaging file formats](#image-formats).
* [Camera Raw file formats](#camera-raw-formats) for a wide range of cameras, including Canon, Nikon, Fujifilm, Olympus, and other manufacturers (powered by Adobe Camera Raw).
* Common [document formats](#document-formats), including Microsoft Office and Open Document formats.
* Wide range of [video](#video-formats) and [audio](#audio-formats) formats.

### Adobe formats {#adobe-formats}

| File format | Thumbnail generation | Fulltext extraction | Metadata extraction | Width/Height |
| ----------- | -------------------- | ------------------- | ------------------- | ------------ |
| AI          | &#10003;             | -                   | &#10003;            | &#10003;     |
| COLLAGE     | -                    | -                   | &#10003;            | -            |
| DN          | &#10003;             |                     | &#10003;            | &#10003;     |
| IDEAS       | -                    | -                   | &#10003;            | -            |
| INDD        | &#10003;             | -                   | &#10003;            | &#10003; *   |
| INDT        | -                    | -                   | &#10003;            | -            |
| PDF         | &#10003;             | &#10003;            | &#10003;            | &#10003;     |
| PROTO       | -                    | -                   | &#10003;            | -            |
| PSB         | &#10003;             | -                   | &#10003;            | &#10003;     |
| PSD         | &#10003;             | -                   | &#10003;            | &#10003;     |
| XD          | &#10003;             | -                   | &#10003;            | &#10003;     |

\* For INDD (InDesign files), the size of rendition is determined by the preview embedded in the INDD file. Configure the preferences in InDesign (**[!UICONTROL Preferences > File Handling > Always Save Preview Images with Documents, Preview Size]**) to embed larger rendition.

### Image formats {#image-formats}

| File format | Thumbnail generation | Metadata extraction | Width/Height |   Crop   |
| ----------- | -------------------- | ------------------- | ------------ | -------- |
| BMP         | &#10003;             | -                   | &#10003;     | &#10003; |
| EPS         | -                    | &#10003;            | -            | -        |
| GIF         | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| JPEG        | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| PNG         | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| SVG         | -                    | &#10003;            | -            | -        |
| TIFF        | &#10003;             | &#10003;            | &#10003;     | -        |

### Camera RAW formats {#camera-raw-formats}

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

### Document formats {#document-formats}

The document formats supported for asset management features are as follows.

| File format | Thumbnail generation | Fulltext extraction | Width/Height | Metadata management | [Connected Assets](use-assets-across-connected-assets-instances.md) |
| ----------- | -------------------- | ------------------- | ------------ | ------------------- | ---------------- |
| PDF         | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         |
| DOCX        | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         |
| DOC         | -                    | -                   | -            | &#10003;            | &#10003;         |
| PPTX        | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         |
| PPT         | -                    | -                   | -            | &#10003;            | &#10003;         |
| XLSX        | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         |
| XLS         | -                    | -                   | -            | &#10003;            | &#10003;         |
| ODF         | &#10003;             | &#10003;            | &#10003;     | -                   | -                |
| OFG         | &#10003;             | &#10003;            | &#10003;     | -                   | -                |
| ODM         | &#10003;             | &#10003;            | &#10003;     | -                   | -                |
| ODP         | &#10003;             | &#10003;            | &#10003;     | -                   | -                |
| ODS         | &#10003;             | &#10003;            | &#10003;     | -                   | -                |
| ODT         | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         |
| EPUB        | -                    | &#10003;            | -            | -                   | -                |
| HTML        | -                    | &#10003;            | -            | &#10003;            | &#10003;         |
| PS          | -                    | -                   | &#10003;     | -                   | -                |
| RTF         | -                    | &#10003;            | -            | &#10003;            | &#10003;         |
| TXT         | -                    | &#10003;            | -            | &#10003;            | &#10003;         |
| XML         | -                    | &#10003;            | -            | -                   | -                |

### Video formats {#video-formats}

| File format | Thumbnail generation | Metadata extraction | Width/Height |
| ----------- | -------------------- | ------------------- | ------------ |
| 3G2         | -                    | &#10003;            | -            |
| 3GP         | -                    | &#10003;            | -            |
| AVI         | &#10003;             | &#10003;            | &#10003;     |
| DIVX        | &#10003;             |                     | &#10003;     |
| F4V         | &#10003;             | &#10003;            | &#10003;     |
| FLV         | &#10003;             | &#10003;            | &#10003;     |
| M2T         | &#10003;             | -                   | &#10003;     |
| M2TS        | &#10003;             | -                   | &#10003;     |
| M2V         | &#10003;             | -                   | &#10003;     |
| M4V         | &#10003;             | &#10003;            | &#10003;     |
| MKV         | &#10003;             | -                   | &#10003;     |
| MOV         | &#10003;             | &#10003;            | &#10003;     |
| MP4         | &#10003;             | &#10003;            | &#10003;     |
| MPEG        | &#10003;             | &#10003;            | &#10003;     |
| MPG         | &#10003;             | &#10003;            | &#10003;     |
| MTS         | &#10003;             | -                   | &#10003;     |
| OGV         | &#10003;             | -                   | &#10003;     |
| QT          | &#10003;             | -                   | &#10003;     |
| R3D         | &#10003;             | -                   | &#10003;     |
| SWF         | &#10003;             | -                   | &#10003;     |
| WEBM        | &#10003;             | -                   | &#10003;     |
| WMV         | &#10003;             | &#10003;            | &#10003;     |

### Audio formats {#audio-formats}

Assets as a Cloud Service provides XMP metadata extraction support for AIF, ASF, M4A, MP3, WAV, and WMA audio formats.

>[!MORELIKETHIS]
>
>* [Asset processing using asset microservices](asset-microservices-overview.md)
