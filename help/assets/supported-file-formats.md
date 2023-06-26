---
title: Supported file formats
description: Supported file formats for the various use cases of [!DNL Assets Essentials]
role: User,Leader,Admin,Architect,Developer
contentOwner: AG
exl-id: bc44e98d-446e-41ff-b5b4-9dc324834630
---
# Files formats support in [!DNL Assets Essentials] {#file-format-support}

[!DNL Assets Essentials] supports a wide range of file formats and each functionality has varied support for different file types.

* ![image file type icon](assets/image-icon.svg) Images: JPG, PNG, GIF, TIFF, and others
* ![creative cloudtype icon](assets/creative-cloud-files.svg) Creative Cloud files: PSD, AI, and INDD
* ![camera type icon](assets/camera-icon.svg) Camera RAW files: CR2/CR3, NEF, SRW/SRF, and others
* ![document file type icon](assets/document-icon.svg) Documents: DOCX, PDF, PPTX, and XLSX
* ![video file type icon](assets/video-icon.svg) Videos: MP4

[!DNL Assets Essentials] supports any binary file format with basic services, such as, storage, upload, copy, move, delete, and adding metadata.

[!DNL Assets Essentials] also supports camera RAW files from a wide range of leading camera manufacturers including Canon (CR2/CR3), Nikon (NEF), Sony (SRW/SRF), Fujifilm (RAF), Olympus (ORF), and others, powered by Adobe Camera Raw.

The various file types have different degrees of support for the use cases and features, as described below. Use the legend to understand the support level.

| Support Level     | Description             |
|-------------------|-------------------------|
| &#10003;          | Supported               |
| &#10003; &Dagger; | Supported conditionally |
| &minus;           | Not applicable          |

## Add, upload, and view assets {#support-to-upload-view}

<!-- TBD: For AEM, AI files require the PDF option to be selected when saving the AI file.
-->

| Asset type        | [Browse](/help/using/navigate-view.md)   | Copy     | [Upload](/help/using/add-delete.md)   | Create   | [Delete](/help/using/add-delete.md#delete-assets)   | Details           | Image zoom | [Recently Viewed](/help/using/navigate-view.md) |
|-------------------|----------|----------|----------|----------|----------|-------------------|------------|-----------------|
| Raster images     | &#10003; | &#10003; | &#10003; | &minus;  | &#10003; | &#10003;          | &#10003;   | &#10003;        |
| RAW files         | &#10003; | &#10003; | &#10003; | &minus;  | &#10003; | &#10003;          | &#10003;   | &#10003;        |
| Folders           | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | &#10003;          | &minus;    | &minus;         |
| MP4 videos        | &#10003; | &#10003; | &#10003; | &minus;  | &#10003; | &#10003; &Dagger; | &minus;    | &#10003;        |
| PDF               | &#10003; | &#10003; | &#10003; | &minus;  | &#10003; | &#10003;          | &minus;    | &#10003;        |
| PSD, AI, and INDD | &#10003; | &#10003; | &#10003; | &minus;  | &#10003; | &#10003; &Dagger; | &minus;    | &#10003;        |
| Other binary files | &#10003; | &#10003; | &#10003; | &minus;  | &#10003; | &#10003; | &minus; | &#10003;        |

<!-- Hiding CC Libraries (considered beta) as per PM feedback.
| CC Libraries  | &#10003; | &minus;  | &#10003; | &#10003; | &#10003; | &#10003; | &minus;    | &minus;         |
-->

## Search, use, and edit assets {#support-to-search-use-edit}

| Asset type    | [Download](/help/using/manage-organize.md#download) | Drag and drop | [Image editor](/help/using/edit-images.md) | [Search](/help/using/search.md)   | [Smart Tags](/help/using/metadata.md#tags) | [Rename](/help/using/manage-organize.md)   | [Versions](/help/using/manage-organize.md#versions-of-assets) |
|---------------|----------|---------------|--------------|----------|------------|----------|----------|
| Raster images | &#10003; | &#10003;      | &#10003;     | &#10003; | &#10003;   | &#10003; | &#10003; |
| RAW files     | &#10003; | &#10003; | &minus; |  &#10003;   | &#10003; | &#10003;          | &#10003;   | &#10003;        |
| Folders       | &#10003; | &#10003;      | &minus;      | &#10003; | &minus;    | &#10003; | &#10003;  |
| Videos        | &#10003; | &#10003;      | &minus;      | &#10003; | &#10003;   | &#10003; | &#10003;  |
| CC Libraries  | &minus;  | &minus;       | &minus;      | &minus;  | &minus;    | &#10003; | &#10003;  |
| PDF           | &#10003; | &#10003;      | &minus;      | &#10003; | &#10003;   | &#10003; | &#10003;  |
| PSD           | &#10003; | &#10003;      | &minus;      | &#10003; | &#10003;   | &#10003; | &#10003;  |
| AI and INDD           | &#10003; | &#10003;      | &minus;      | &#10003; | &minus;   | &#10003; | &#10003;  |
| Other binary files          |  &#10003;  | &#10003;      | &minus;      |  &#10003;  |&minus;   |  &#10003;  | &#10003;  |


## Review assets and collaborate {#support-to-review-collaborate}

| Asset type    | Annotate | Comment  | Create tasks and review |
|---------------|----------|----------|-------------------------|
| Raster images | &#10003; | &#10003; | &#10003;      |
| RAW files     | &#10003; | &#10003; | &#10003;      |
| Folders       | &minus;  | &minus;  | &minus;       |
| Videos        | &minus;  | &#10003; | &#10003;      |
| CC Libraries  | &minus;  | &minus;  | &minus;       |
| PDF           | &minus;  | &#10003; | &#10003;      |
| PSD, AI, and INDD | &minus;  | &#10003; | &#10003;  |
| Other binary files| &minus;  | &#10003; | &#10003;  |
| DOC           | &minus; | &#10003;  | &#10003;      |
| DOCX          | &minus; | &#10003;  | &#10003;      |
| PPT           | &minus; | &#10003;  | &#10003;      |
| PPTX          | &minus; | &#10003;  | &#10003;      |
| XLS           | &minus; | &#10003;  | &#10003;      |
| XLSX          | &minus; | &#10003;  | &#10003;      |
| TXT           | &minus; | &#10003;  | &#10003;      |
| RTF           | &minus; | &#10003;  | &#10003;      |

## Other asset management tasks {#support-to-manage-assets}

| Asset type    | [Metadata](/help/using/metadata.md)          | [Renditions](/help/using/add-delete.md#renditions) | [Trash](/help/using/add-delete.md#delete-assets)    | Copy     | Move     |
|---------------|-------------------|------------|----------|----------|----------|
| Raster images | &#10003; | &#10003;   | &#10003; | &#10003; | &#10003; |
| RAW files     | &#10003; | &#10003;   | &#10003; | &#10003; | &#10003; |
| Folders       | &#10003; | &minus;    | &#10003; | &#10003; | &#10003; |
| Videos        | &#10003; | &minus;    | &#10003; | &#10003; | &#10003; |
| CC Libraries  | &#10003; | &minus;    | &minus;  | &minus;  | &minus;  |
| PDF           | &#10003; | &minus;    | &#10003; | &#10003; | &#10003; |
| PSD, AI, and INDD           | &#10003; | &minus;    | &#10003; | &#10003; | &#10003; |
| Other binary files          | &#10003; | &minus;    |&#10003; | &#10003; | &#10003; |

Users of [!DNL Adobe Asset Link] can upload and check-in (upload a new version) files into the [!DNL Assets Essentials] repository from the supported [!DNL Adobe Creative Cloud] desktop applications.

<!-- TBD: Saving the template table separately for later use.
| Asset type    | Features |
|---------------|----------|
| Raster images |          |
| Folders       |          |
| Videos        |          |
| CC Libraries  |          |
| PDF files     |          |
| PSD           |          |
| AI            |          |
| INDD          |          |

>[!MORELIKETHIS]
>
>* []()
-->

## Next Steps {#next-steps}

* Provide product feedback using the [!UICONTROL Feedback] option available on the Assets Essentials user interface

*  Provide documentation feedback using [!UICONTROL Edit this page] ![edit the page](assets/do-not-localize/edit-page.png) or [!UICONTROL Log an issue] ![create a GitHub issue](assets/do-not-localize/github-issue.png) available on the right sidebar

* Contact [Customer Care](https://experienceleague.adobe.com/?support-solution=General#support)
