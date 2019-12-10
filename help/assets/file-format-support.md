---
title: File formats and MIME types supported by Experience Manager Assets as a Cloud Service
description: File formats and MIME types supported by Experience Manager Assets as a Cloud Service.
contentOwner: AG

---

# Assets supported file formats {#supported-file-formats}

## Overview

Experience Manager as a Cloud Service supports basic content management capabilities for any binary file, independent of format - storage, managing metadata online, versioning, upload and download, etc. In addition, for the commonly-used file formats, like key imaging, desing, document and video formats, it provides extended support for generating previews and renditions, extracting metadata and text for full-text indexing. This exetended support is provided by [asset microservices](asset-microservices-configure-and-use.md). 

Some highlights of file formats with extended support include:

* Key [Adobe file formats](#adobe-formats) produced by Adobe applications and services, including Adobe Photoshop, Indesign, Illustrator, XD, Dimension, and Acrobat / PDF.
* Key [imaging file formats](#image-formats)
* [Camera Raw file formats](#camera-raw-formats) for a wide range of cameras, including Canon, Nikon, Fujifilm, Olympus, and other manufacturers (powered by Adobe Camera Raw)
* Common [document formats](#document-formats), including [Microsoft Office](#microsoft-office-formats) (Word, Excel, Powerpoint) and [Open Document](#opendocument-formats) formats 
* Wide range of [video](#video-formats) and [audio](#audio-formats) formats

## Legend
The following legend describes the level of support for a feature:

| Support level |          Description           |
| ------------- | ------------------------------ |
| ![available icon](assets/do-not-localize/checkmark_icon.png)       | Supported                      |
| *             | See remarks below |
| -             | Not applicable                 |

Columns of the support tables provide the following information:

| Column | Description |
| ----- | ----------- |
| Format | file format (file extension) of the asset original binary |
| GIF   | GIF format for rendition generation |
| JPEG  | JPEG format for rendition generation |
| PNG   | PNG format for rendition generation |
| XMP   | Extraction of metadata from the original binary |
| TXT   | Extraction of text from document for indexing |
| Width/Height | Support for defining the width & height of a rendition (pixels) |

<!-- Adding this checkmark icon ![available icon](assets/do-not-localize/checkmark_icon.png) does not look good in table. The icon's shade and size has to be toned down for good readability and less clutter.
@gklebus: I suggest using a checkmark character, either U+2713 ✓ CHECK MARK or U+2714 ✔ HEAVY CHECK MARK
-->

## Adobe formats {#adobe-formats}

|Format|GIF| JPEG | PNG | TXT | XMP |Width/Height|
|---|---|---|---|---|---|---|
|Adobe | ![available icon](assets/do-not-localize/checkmark_icon.png) | ![available icon](assets/do-not-localize/checkmark_icon.png) | ![available icon](assets/do-not-localize/checkmark_icon.png) | ![available icon](assets/do-not-localize/checkmark_icon.png) | ![available icon](assets/do-not-localize/checkmark_icon.png) | ![available icon](assets/do-not-localize/checkmark_icon.png) |
| AI | ![available icon](assets/do-not-localize/checkmark_icon.png) | ![available icon](assets/do-not-localize/checkmark_icon.png) | ![available icon](assets/do-not-localize/checkmark_icon.png) | | ![available icon](assets/do-not-localize/checkmark_icon.png) | ![available icon](assets/do-not-localize/checkmark_icon.png)|
| COLLAGE | | | | | ![available icon](assets/do-not-localize/checkmark_icon.png) | |
| DN | ![available icon](assets/do-not-localize/checkmark_icon.png)| ![available icon](assets/do-not-localize/checkmark_icon.png)| ![available icon](assets/do-not-localize/checkmark_icon.png) | |![available icon](assets/do-not-localize/checkmark_icon.png) | ![available icon](assets/do-not-localize/checkmark_icon.png)|
| IDEAS | | | | | ![available icon](assets/do-not-localize/checkmark_icon.png) | |
| INDD | ![available icon](assets/do-not-localize/checkmark_icon.png)| ![available icon](assets/do-not-localize/checkmark_icon.png)| ![available icon](assets/do-not-localize/checkmark_icon.png)| |![available icon](assets/do-not-localize/checkmark_icon.png) | ![available icon](assets/do-not-localize/checkmark_icon.png)*|
| INDT | | | | |![available icon](assets/do-not-localize/checkmark_icon.png) | |
| PDF |![available icon](assets/do-not-localize/checkmark_icon.png) |![available icon](assets/do-not-localize/checkmark_icon.png) |![available icon](assets/do-not-localize/checkmark_icon.png) |![available icon](assets/do-not-localize/checkmark_icon.png) |![available icon](assets/do-not-localize/checkmark_icon.png) |![available icon](assets/do-not-localize/checkmark_icon.png) |
| PROTO | | | | | ![available icon](assets/do-not-localize/checkmark_icon.png)| |
| PSB | ![available icon](assets/do-not-localize/checkmark_icon.png)| ![available icon](assets/do-not-localize/checkmark_icon.png)|![available icon](assets/do-not-localize/checkmark_icon.png) | |![available icon](assets/do-not-localize/checkmark_icon.png) | ![available icon](assets/do-not-localize/checkmark_icon.png)|
| PSD | ![available icon](assets/do-not-localize/checkmark_icon.png)| ![available icon](assets/do-not-localize/checkmark_icon.png)|![available icon](assets/do-not-localize/checkmark_icon.png)| |![available icon](assets/do-not-localize/checkmark_icon.png) |![available icon](assets/do-not-localize/checkmark_icon.png) |
| XD | ![available icon](assets/do-not-localize/checkmark_icon.png)|![available icon](assets/do-not-localize/checkmark_icon.png) |![available icon](assets/do-not-localize/checkmark_icon.png) | |![available icon](assets/do-not-localize/checkmark_icon.png) |![available icon](assets/do-not-localize/checkmark_icon.png) |

(*) Remarks:

* For INDD (InDesign files), the size of rendition is determined by the preview embedded in the .INDD file. Please note that you can get larger rendition embedded by configuring preferences in InDesign Application (**[!UICONTROL Preferences / File Handling / Always Save Preview Images with Documents, Preview Size]**).

## Image formats {#image-formats}

|     File format     |     GIF     |     JPEG     |     PNG     |     XMP     |     Width/Height     |
|---------------------|-------------|--------------|-------------|-------------|----------------|
|    BMP              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    -        |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    EPS              |    -        |    -         |    -        |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    -           |
|    GIF              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    JPEG             |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    PNG              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    SVG              |    -        |    -         |    -        |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    -           |
|    TIFF             |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |


## Camera RAW formats {#camera-raw-formats}

|     File format     |     GIF     |     JPEG     |     PNG     |     XMP     |     Width/Height     |
|---------------------|-------------|--------------|-------------|-------------|----------------|
|3FR|    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    ARW              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|CR2|    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|CR3|    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    CRW              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    DCR              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    DNG              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    ERF              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    FFF              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    GPR              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    IIQ              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    KDC              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    MEF              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    MFW              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    MOS              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    MRW              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    NEF              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    NRW              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    ORF              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    PEF              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    RAF              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    RAW              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|RW2|    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    RWL              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    SRF              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    SRW              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|X3F|    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |


## Document formats {#document-formats}

|     File format     |     TXT     |     XMP     |
|---------------------|-------------|-------------|
|    EPUB             |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    -        |
|    HTML             |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    -        |
|    PS               |    -        |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |
|    RTF              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    -        |
|    TEXT             |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    -        |
|    XML              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    -        |


## Microsoft Office formats {#microsoft-office-formats}

|     File format     |     GIF     |     JPEG     |     PNG     |     TEXT     |     Width/Height     |
|---------------------|-------------|--------------|-------------|--------------|----------------|
|    DOCX             |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    PPTX             |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    XLSX             |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |


## OpenDocument formats {#opendocument-formats}

|     File format     |     GIF     |     JPEG     |     PNG     |     TEXT     |     Height     |
|---------------------|-------------|--------------|-------------|--------------|----------------|
|    ODF              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    OFG              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    ODM              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    ODP              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    ODS              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |
|    ODT              |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)      |    ![available icon](assets/do-not-localize/checkmark_icon.png)       |    ![available icon](assets/do-not-localize/checkmark_icon.png)         |

## Video formats {#video-formats}

|     File format     |     GIF     |     JPEG     |     PNG     |     XMP     |     Width/Height     |
|---------------------|-------------|--------------|-------------|-------------|----------------|
|3G2|    -    |    -    |    -    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    -    |
|3GP|    -    |    -    |    -    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    -    |
|    AVI    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|    DIVX    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |  |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|F4V|    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|    FLV    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|M2T|    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    -    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|M2TS|    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    -    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|M2V|    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    -    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|M4V|    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|    MKV    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    -    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|    MOV    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|MP4|    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|    MPEG    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|    MPG    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|    MTS    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    -    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|    OGV    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    -    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|    QT    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    -    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|R3D|    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    -    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|    SWF    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    -    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|    WEBM    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    -    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |
|    WMV    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |    ![available icon](assets/do-not-localize/checkmark_icon.png)    |

## Audio formats {#audio-formats}

Assets as a Cloud Service supports XMP format in these audio formats: AIF, ASF, M4A, MP3, WAV, and WMA.

<!-- TBD: Some items from https://helpx.adobe.com/experience-manager/6-5/assets/using/assets-formats.html#SupportedinputvideoformatsforDynamicMediatranscoding may be applicable.

Bring more parity with https://helpx.adobe.com/experience-manager/6-5/assets/using/assets-formats.html#SupportedMIMEtypes.
https://helpx.adobe.com/experience-manager/6-5/assets/using/assets-formats.html#Supportedmultimediaformats
-->

>[!MORELIKETHIS]
>
>[Asset processing using asset microservices](asset-microservices-overview.md)