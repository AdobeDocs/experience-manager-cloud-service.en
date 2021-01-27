---
title: Supported file formats and MIME types
description: File formats and MIME types supported by [!DNL Experience Manager Assets] as a [!DNL Cloud Service].
contentOwner: AG
---

# [!DNL Assets] supported file formats {#supported-file-formats}

[!DNL Adobe Experience Manager] as a [!DNL Cloud Service] supports basic content management capabilities &mdash; storage, managing metadata online, versioning, upload and download, and so on &mdash; for any binary file, independent of its format. [!DNL Adobe Experience Manager Assets] supports a wide range of file formats and each product feature has varied support for different formats.

In addition, [!DNL Experience Manager Assets] provides extended support to generate previews and renditions and to extract metadata and text for full-text indexing. This extended support is provided using [asset microservices](asset-microservices-configure-and-use.md).

The highlights for Asset conversion using asset microservices include:

* Key [Adobe file formats](#adobe-formats) produced by Adobe applications and services, including [!DNL Adobe Photoshop], [!DNL Adobe InDesign], [!DNL Adobe Illustrator], [!DNL Adobe XD], [!DNL Adobe Dimension], and [!DNL Adobe Acrobat] or PDF.
* Key [imaging file formats](#image-formats).
* [Camera Raw file formats](#camera-raw-formats) for a wide range of cameras, including Canon, Nikon, Fujifilm, Olympus, and other manufacturers (powered by Adobe Camera Raw).
* Common [document formats](#document-formats), including Microsoft Office and Open Document formats.
* Wide range of [video](#video-formats) and [audio](#audio-formats) formats.

The following legend describes the level of support.

| Support level |         Description         |
| ------------- | --------------------------- |
| &#10003;      | Supported                   |
| *             | See remarks below the table |
| -             | Not applicable              |

## Adobe formats {#adobe-formats}

| File format | Thumbnail generation | Full-text extraction | Metadata extraction | Width/Height |
| ----------- | -------------------- | ------------------- | ------------------- | ------------ |
| AI          | &#10003;             | -                   | &#10003;            | &#10003;     |
| COLLAGE     | -                    | -                   | &#10003;            | -            |
| DN          | &#10003;             | -                   | &#10003;            | &#10003;     |
| IDEAS       | -                    | -                   | &#10003;            | -            |
| INDD        | &#10003;             | -                   | &#10003;            | &#10003; *   |
| INDT        | -                    | -                   | &#10003;            | -            |
| PDF         | &#10003;             | &#10003;            | &#10003;            | &#10003;     |
| PROTO       | -                    | -                   | &#10003;            | -            |
| PSB         | &#10003;             | -                   | &#10003;            | &#10003;     |
| PSD         | &#10003;             | -                   | &#10003;            | &#10003;     |
| XD          | &#10003;             | -                   | &#10003;            | &#10003;     |

\* For [!DNL Adobe InDesign] files (INDD), the size of rendition is determined by the preview embedded in the INDD file. Configure the preferences in [!DNL InDesign] (**[!UICONTROL Preferences > File Handling > Always Save Preview Images with Documents, Preview Size]**) to embed larger rendition.

## Image formats {#image-formats}

| File format | Thumbnail generation | Metadata extraction | Width/Height |   Crop   |
| ----------- | -------------------- | ------------------- | ------------ | -------- |
| BMP         | &#10003;             | -                   | &#10003;     | &#10003; |
| EPS         | -                    | &#10003;            | -            | -        |
| GIF         | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| JPEG        | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| PNG         | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| RGB         | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| RGBA        | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| SGI         | &#10003;             | &#10003;            | &#10003;     | &#10003; |
| SVG         | &#10003;             | -                   | &#10003;     | &#10003; |
| TIFF        | &#10003;             | &#10003;            | &#10003;     | -        |

## Image formats in [!DNL Dynamic Media] {#image-support-dynamic-media}

| Format  | Upload (Input format) | Create image preset (Output format) | Preview dynamic rendition | Deliver dynamic rendition | Download dynamic rendition |
| ------- | --------------------- | ----------------------------------- | ------------------------- | ------------------------- | -------------------------- |
| BMP     | ✓                     | -                                   | -                         | -                         | -                          |
| EPS     | ✓                     | ✓                                   | ✓                         | ✓                         | ✓                          |
| GIF     | ✓                     | ✓                                   | ✓                         | ✓                         | ✓                          |
| JPEG    | ✓                     | ✓                                   | ✓                         | ✓                         | ✓                          |
| PICT    | ✓                     | -                                   | -                         | -                         | -                          |
| PNG     | ✓                     | ✓                                   | ✓                         | ✓                         | ✓                          |
| PSD   ‡ | ✓                     | -                                   | -                         | -                         | -                          |
| TIFF    | ✓                     | ✓                                   | ✓                         | ✓                         | ✓                          |

‡ The merged image is extracted from the PSD file. It is an image that is generated by [!DNL Adobe Photoshop] and is included in the PSD file. Depending on the settings, the merged image may or may not be the actual image.

The following sub-types of raster image file formats that are not supported in [!DNL Dynamic Media]:

* PNG files that have an IDAT chunk size greater than 100 MB.
* PSB files.
* PSD files with a color space other than CMYK, RGB, Grayscale, or Bitmap are not supported. DuoTone, Lab, and Indexed color spaces are not supported.
* PSD files that have a bit depth greater than 16.
* TIFF files that have floating point data.
* TIFF files that have Lab color space.

## 3D formats {#support-3d-formats}

The following 3D formats are supported.

See also [Working with 3D assets in Dynamic Media.](/help/assets/dynamic-media/assets-3d.md)

| Format | Storage | Versioning | Workflow | Publishing | Access control | Thumbnail preview | 3D preview | Dynamic Media delivery |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| DN | &#10003; | &#10003; | &#10003; |- | &#10003; | &#10003; | -| -|
| gLB | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | -| &#10003; | &#10003; |
| gLTF | &#10003; | &#10003; | &#10003; |- | &#10003; |- | &#10003; |- |
| OBJ | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; |- | &#10003; | &#10003; |
| STL | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; |- | &#10003; | &#10003; |
| USDz |&#10003;| &#10003; | &#10003; | &#10003; | &#10003; |- |- | &#10003; |

## [!DNL Camera RAW] formats {#camera-raw-formats}

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

| File format | Thumbnail generation | Full-text extraction | Width/Height | Metadata management | [Connected Assets](use-assets-across-connected-assets-instances.md) |
| ----------- | -------------------- | ------------------- | ------------ | ------------------- | ---------------- |
| DOC         | -                    | -                   | -            | &#10003;            | &#10003;         |
| DOCX        | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         |
| EPUB        | -                    | &#10003;            | -            | -                   | -                |
| HTML        | -                    | &#10003;            | -            | &#10003;            | &#10003;         |
| ODF         | &#10003;             | &#10003;            | &#10003;     | -                   | -                |
| ODM         | &#10003;             | &#10003;            | &#10003;     | -                   | -                |
| ODP         | &#10003;             | &#10003;            | &#10003;     | -                   | -                |
| ODS         | &#10003;             | &#10003;            | &#10003;     | -                   | -                |
| ODT         | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         |
| OFG         | &#10003;             | &#10003;            | &#10003;     | -                   | -                |
| PDF         | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         |
| PPT         | -                    | -                   | -            | &#10003;            | &#10003;         |
| PPTX        | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         |
| PS          | -                    | -                   | &#10003;     | -                   | -                |
| RTF         | -                    | &#10003;            | -            | &#10003;            | &#10003;         |
| TXT         | -                    | &#10003;            | -            | &#10003;            | &#10003;         |
| XLS         | -                    | -                   | -            | &#10003;            | &#10003;         |
| XLSX        | &#10003;             | &#10003;            | &#10003;     | &#10003;            | &#10003;         |
| XML         | -                    | &#10003;            | -            | -                   | -                |

## Document formats in [!DNL Dynamic Media] {#document-support-dynamic-media}

| Format | Upload (Input format) | Create image preset (Output format) | Preview dynamic rendition | Deliver dynamic rendition | Download dynamic rendition |
| ------ | --------------------- | ----------------------------------- | ------------------------- | ------------------------- | -------------------------- |
| AI     | ✓                     | -                                   | -                         | -                         | -                          |
| INDD   | ✓                     | -                                   | -                         | -                         | -                          |
| PDF    | ✓                     | ✓                                   | ✓                         | ✓                         | ✓                        |

## Video formats {#video-formats}

| File format | Thumbnail generation | Metadata extraction | Width/Height |
| ----------- | -------------------- | ------------------- | ------------ |
| 3G2         | -                    | &#10003;            | -            |
| 3GP         | -                    | &#10003;            | -            |
| AVI         | &#10003;             | &#10003;            | &#10003;     |
| DIVX        | &#10003;             |  -                  | &#10003;     |
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
| MXF         | &#10003;             | -                   | -            |
| OGV         | &#10003;             | -                   | &#10003;     |
| QT          | &#10003;             | -                   | &#10003;     |
| R3D         | -                    | &#10003;            | &#10003;     |
| SWF         | &#10003;             | -                   | &#10003;     |
| WebM        | &#10003;             | -                   | &#10003;     |
| WMV         | &#10003;             | &#10003;            | &#10003;     |

## Video formats in [!DNL Dynamic Media] for transcoding {#video-dynamic-media-transcoding}

| Video file extension   | Container          | Recommended video codecs    | Unsupported video codecs   |
|------------------------|--------------------|--------|-------|
| MP4                    | MPEG-4             | H264/AVC (all profiles) | - |
| MOV, QT                | Apple QuickTime    | H264/AVC, Apple ProRes422  & HQ, Sony XDCAM, Sony DVCAM, HDV, Panasonic DVCPro, Apple DV  (DV25), Apple PhotoJPEG, Sorenson, Avid DNxHD, Avid AVR   | Apple Intermediate, Apple Animation  |
| FLV, F4V               | Adobe Flash        | H264/AVC, Flix VP6, H263, Sorenson  | SWF (vector animation files) |
| WMV                    | Windows Media 9    | WMV3 (v9), WMV2 (v8), WMV1 (v7), GoToMeeting (G2M2, G2M3, G2M4)  | Microsoft Screen (MSS2), Microsoft Photo Story (WVP2) |
| MPG, VOB, M2V, MP2     | MPEG-2             | MPEG-2  |- |
| M4V                    | Apple iTunes       | H264/AVC | - |
| AVI                    | A/V Interleave     | XVID, DIVX, HDV, MiniDV (DV25), Techsmith Camtasia, Huffyuv, Fraps, Panasonic DVCPro | Indeo3 (IV30), MJPEG, Microsoft Video 1 (MS-CRAM) |
| WebM                   | WebM               | Google VP8 |- |
| OGV, OGG               | Ogg                | Theora, VP3, Dirac  | - |
| MXF                    | MXF                | Sony XDCAM, MPEG-2, MPEG-4, Panasonic DVCPro | -|
| MTS                    | AVCHD              | H264/AVC | - |
| MKV                    | Matroska           | H264/AVC  | - |
| R3D, RM                | Red Raw Video      | MJPEG 2000 | -  |
| RAM, RM                | RealVideo          | Unsupported | Real G2 (RV20), Real 8 (RV30), Real 10 (RV40) |
| FLAC                   | Native Flac        | Free lossless audio codec |  - |
| MJ2                    | Motion JPEG 2000   | Motion JPEG 2000 codec | - |

## Audio formats {#audio-formats}

[!DNL Assets] as a [!DNL Cloud Service] provides XMP metadata extraction support for AIF, ASF, M4A, MP3, WAV, and WMA audio formats.

## Tips and limitations {#limitations-and-tips}

* Currently, the file size limit for metadata extraction is approximately 10 GB. When uploading very large assets, sometimes metadata extraction operation fails.

>[!MORELIKETHIS]
>
>* [Asset processing using asset microservices](asset-microservices-overview.md)
