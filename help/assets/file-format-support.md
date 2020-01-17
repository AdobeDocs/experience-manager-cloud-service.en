---
title: File formats and MIME types supported by Experience Manager Assets as a Cloud Service
description: File formats and MIME types supported by Experience Manager Assets as a Cloud Service.
contentOwner: AG
---

# Assets supported file formats {#supported-file-formats}

Adobe Experience Manager as a Cloud Service supports basic content management capabilities - storage, managing metadata online, versioning, upload and download and so on - for any binary file, independent of its format. In addition, for the commonly-used file formats, like image, Adobe proprietary, document, and video, it provides extended support to generate previews and renditions and to extract metadata and text for full-text indexing. This extended support is provided using [asset microservices](asset-microservices-configure-and-use.md).

Some highlights of file formats with extended support include:

* Key [Adobe file formats](#adobe-formats) produced by Adobe applications and services, including Adobe Photoshop, InDesign, Illustrator, XD, Dimension, and Acrobat / PDF.
* Key [imaging file formats](#image-formats)
* [Camera Raw file formats](#camera-raw-formats) for a wide range of cameras, including Canon, Nikon, Fujifilm, Olympus, and other manufacturers (powered by Adobe Camera Raw)
* Common [document formats](#document-formats), including [Microsoft Office](#microsoft-office-formats) (Word, Excel, PowerPoint) and [Open Document](#opendocument-formats) formats
* Wide range of [video](#video-formats) and [audio](#audio-formats) formats

## Legend for detailed support information {#legend-for-detailed-support-information}

The following legend describes the level of support for a feature:

|                        Support level                         |         Description         |
| ------------------------------------------------------------ | --------------------------- |
| ✓ | Supported                   |
| *                                                            | See remarks below the table |
| -                                                            | Not applicable              |

Columns of the support tables provide the following information:

|    Column    |                           Description                           |
| ------------ | --------------------------------------------------------------- |
| Format       | File format (file extension) of the asset original binary       |
| GIF          | GIF format for rendition generation                             |
| JPEG         | JPEG format for rendition generation                            |
| PNG          | PNG format for rendition generation                             |
| XMP          | Extraction of metadata from the original binary                 |
| TXT          | Extraction of text from document for indexing                   |
| Width/Height | Support for defining the width & height of a rendition (pixels) |

<!-- Adding this checkmark icon ✓ does not look good in table. The icon's shade and size has to be toned down for good readability and less clutter.
@gklebus: I suggest using a checkmark character, either U+2713 ✓ CHECK MARK or U+2714 ✔ HEAVY CHECK MARK
-->

## Adobe formats {#adobe-formats}

| File format | GIF | JPEG | PNG | TXT | XMP | Width/Height |
| ----------- | --- | ---- | --- | --- | --- | ------------ |
| Adobe       | ✓   | ✓    | ✓   | ✓   | ✓   | ✓            |
| AI          | ✓   | ✓    | ✓   | -   | ✓   | ✓            |
| COLLAGE     | -   | -    | -   | -   | ✓   | -            |
| DN          | ✓   | ✓    | ✓   |     | ✓   | ✓            |
| IDEAS       | -   | -    | -   | -   | ✓   | -            |
| INDD        | ✓   | ✓    | ✓   | -   | ✓   | ✓*           |
| INDT        | -   | -    | -   | -   | ✓   | -            |
| PDF         | ✓   | ✓    | ✓   | ✓   | ✓   | ✓            |
| PROTO       | -   | -    | -   | -   | ✓   | -            |
| PSB         | ✓   | ✓    | ✓   |  -  | ✓   | ✓            |
| PSD         | ✓   | ✓    | ✓   |  -  | ✓   | ✓            |
| XD          | ✓   | ✓    | ✓   |  -  | ✓   | ✓            |

\* For INDD (InDesign files), the size of rendition is determined by the preview embedded in the INDD file. Configure the preferences in InDesign (**[!UICONTROL Preferences > File Handling > Always Save Preview Images with Documents, Preview Size]**) to embed larger rendition.

## Image formats {#image-formats}

| File format | GIF | JPEG | PNG | XMP | Width/Height |
| ----------- | --- | ---- | --- | --- | ------------ |
| BMP         | ✓   | ✓    | ✓   | -   | ✓            |
| EPS         | -   | -    | -   | ✓   | -            |
| GIF         | ✓   | ✓    | ✓   | ✓   | ✓            |
| JPEG        | ✓   | ✓    | ✓   | ✓   | ✓            |
| PNG         | ✓   | ✓    | ✓   | ✓   | ✓            |
| SVG         | -   | -    | -   | ✓   | -            |
| TIFF        | ✓   | ✓    | ✓   | ✓   | ✓            |


## Camera RAW formats {#camera-raw-formats}

| File format | GIF | JPEG | PNG | XMP | Width/Height |
| ----------- | --- | ---- | --- | --- | ------------ |
| 3FR         | ✓   | ✓    | ✓   | ✓   | ✓            |
| ARW         | ✓   | ✓    | ✓   | ✓   | ✓            |
| CR2         | ✓   | ✓    | ✓   | ✓   | ✓            |
| CR3         | ✓   | ✓    | ✓   | ✓   | ✓            |
| CRW         | ✓   | ✓    | ✓   | ✓   | ✓            |
| DCR         | ✓   | ✓    | ✓   | ✓   | ✓            |
| DNG         | ✓   | ✓    | ✓   | ✓   | ✓            |
| ERF         | ✓   | ✓    | ✓   | ✓   | ✓            |
| FFF         | ✓   | ✓    | ✓   | ✓   | ✓            |
| GPR         | ✓   | ✓    | ✓   | ✓   | ✓            |
| IIQ         | ✓   | ✓    | ✓   | ✓   | ✓            |
| KDC         | ✓   | ✓    | ✓   | ✓   | ✓            |
| MEF         | ✓   | ✓    | ✓   | ✓   | ✓            |
| MFW         | ✓   | ✓    | ✓   | ✓   | ✓            |
| MOS         | ✓   | ✓    | ✓   | ✓   | ✓            |
| MRW         | ✓   | ✓    | ✓   | ✓   | ✓            |
| NEF         | ✓   | ✓    | ✓   | ✓   | ✓            |
| NRW         | ✓   | ✓    | ✓   | ✓   | ✓            |
| ORF         | ✓   | ✓    | ✓   | ✓   | ✓            |
| PEF         | ✓   | ✓    | ✓   | ✓   | ✓            |
| RAF         | ✓   | ✓    | ✓   | ✓   | ✓            |
| RAW         | ✓   | ✓    | ✓   | ✓   | ✓            |
| RW2         | ✓   | ✓    | ✓   | ✓   | ✓            |
| RWL         | ✓   | ✓    | ✓   | ✓   | ✓            |
| SRF         | ✓   | ✓    | ✓   | ✓   | ✓            |
| SRW         | ✓   | ✓    | ✓   | ✓   | ✓            |
| X3F         | ✓   | ✓    | ✓   | ✓   | ✓            |

## Document formats {#document-formats}

| File format | TXT | XMP |
| ----------- | --- | --- |
| EPUB        | ✓   | -   |
| HTML        | ✓   | -   |
| PS          | -   | ✓   |
| RTF         | ✓   | -   |
| TEXT        | ✓   | -   |
| XML         | ✓   | -   |

## Microsoft Office formats {#microsoft-office-formats}

| File format | GIF | JPEG | PNG | TEXT | Width/Height |
| ----------- | --- | ---- | --- | ---- | ------------ |
| DOCX        | ✓   | ✓    | ✓   | ✓    | ✓            |
| PPTX        | ✓   | ✓    | ✓   | ✓    | ✓            |
| XLSX        | ✓   | ✓    | ✓   | ✓    | ✓            |

## OpenDocument formats {#opendocument-formats}

| File format | GIF | JPEG | PNG | TEXT | Height |
| ----------- | --- | ---- | --- | ---- | ------ |
| ODF         | ✓   | ✓    | ✓   | ✓    | ✓      |
| OFG         | ✓   | ✓    | ✓   | ✓    | ✓      |
| ODM         | ✓   | ✓    | ✓   | ✓    | ✓      |
| ODP         | ✓   | ✓    | ✓   | ✓    | ✓      |
| ODS         | ✓   | ✓    | ✓   | ✓    | ✓      |
| ODT         | ✓   | ✓    | ✓   | ✓    | ✓      |

## Video formats {#video-formats}

| File format | GIF | JPEG | PNG | XMP | Width/Height |
| ----------- | --- | ---- | --- | --- | ------------ |
| 3G2         | -   | -    | -   | ✓   | -            |
| 3GP         | -   | -    | -   | ✓   | -            |
| AVI         | ✓   | ✓    | ✓   | ✓   | ✓            |
| DIVX        | ✓   | ✓    | ✓   |     | ✓            |
| F4V         | ✓   | ✓    | ✓   | ✓   | ✓            |
| FLV         | ✓   | ✓    | ✓   | ✓   | ✓            |
| M2T         | ✓   | ✓    | ✓   | -   | ✓            |
| M2TS        | ✓   | ✓    | ✓   | -   | ✓            |
| M2V         | ✓   | ✓    | ✓   | -   | ✓            |
| M4V         | ✓   | ✓    | ✓   | ✓   | ✓            |
| MKV         | ✓   | ✓    | ✓   | -   | ✓            |
| MOV         | ✓   | ✓    | ✓   | ✓   | ✓            |
| MP4         | ✓   | ✓    | ✓   | ✓   | ✓            |
| MPEG        | ✓   | ✓    | ✓   | ✓   | ✓            |
| MPG         | ✓   | ✓    | ✓   | ✓   | ✓            |
| MTS         | ✓   | ✓    | ✓   | -   | ✓            |
| OGV         | ✓   | ✓    | ✓   | -   | ✓            |
| QT          | ✓   | ✓    | ✓   | -   | ✓            |
| R3D         | ✓   | ✓    | ✓   | -   | ✓            |
| SWF         | ✓   | ✓    | ✓   | -   | ✓            |
| WEBM        | ✓   | ✓    | ✓   | -   | ✓            |
| WMV         | ✓   | ✓    | ✓   | ✓   | ✓            |

## Audio formats {#audio-formats}

Assets as a Cloud Service provides XMP support for these audio formats: AIF, ASF, M4A, MP3, WAV, and WMA.

<!-- TBD: Some items from https://helpx.adobe.com/experience-manager/6-5/assets/using/assets-formats.html#SupportedinputvideoformatsforDynamicMediatranscoding may be applicable.

Bring more parity with https://helpx.adobe.com/experience-manager/6-5/assets/using/assets-formats.html#SupportedMIMEtypes.
https://helpx.adobe.com/experience-manager/6-5/assets/using/assets-formats.html#Supportedmultimediaformats
-->

>[!MORELIKETHIS]
>
>[Asset processing using asset microservices](asset-microservices-overview.md)
