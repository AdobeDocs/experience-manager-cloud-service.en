---
title: Supported file formats
description: Supported file formats for the various use cases of [!DNL Assets view]
role: User, Leader, Admin, Architect, Developer
contentOwner: AG
exl-id: 5936ace2-318e-4888-9ad4-23e6f6bfb857
feature: Asset Management, Publishing, Collaboration, Asset Processing
---
# Files formats support in [!DNL Assets view] {#file-format-support}

<table>
    <tr>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/dm-prime-ultimate.md"><b>Dynamic Media Prime and Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/assets-ultimate-overview.md"><b>AEM Assets Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/integrate-aem-assets-edge-delivery-services.md"><b>AEM Assets integration with Edge Delivery Services</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/aem-assets-view-ui-extensibility.md"><b>UI Extensibility</b></a>
        </td>
          <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/enable-dynamic-media-prime-and-ultimate.md"><b>Enable Dynamic Media Prime and Ultimate</b></a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="/help/assets/search-best-practices.md"><b>Search Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/metadata-best-practices.md"><b>Metadata Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/product-overview.md"><b>Content Hub</b></a>
        </td>
        <td>
            <a href="/help/assets/dynamic-media-open-apis-overview.md"><b>Dynamic Media with OpenAPI capabilities</b></a>
        </td>
        <td>
            <a href="https://developer.adobe.com/experience-cloud/experience-manager-apis/"><b>AEM Assets developer documentation</b></a>
        </td>
    </tr>
</table>

[!DNL Assets view] supports a wide range of file formats and each functionality has varied support for different file types.

* ![image file type icon](assets/image-icon.svg) Images: JPG, PNG, GIF, TIFF, and others
* ![creative cloudtype icon](assets/creative-cloud-files.svg) Creative Cloud files: PSD, PSB, AI, and INDD
* ![camera type icon](assets/camera-icon.svg) Camera RAW files: CR2/CR3, NEF, SRW/SRF, and others
* ![document file type icon](assets/document-icon.svg) Documents: DOCX, PDF, PPTX, and XLSX
* ![video file type icon](assets/video-icon.svg) Videos: MP4

[!DNL Assets view] supports any binary file format with basic services, such as, storage, upload, copy, move, delete, and adding metadata.

[!DNL Assets view] also supports camera RAW files from a wide range of leading camera manufacturers including Canon (CR2/CR3), Nikon (NEF), Sony (SRW/SRF), Fujifilm (RAF), Olympus (ORF), and others, powered by Adobe Camera Raw.

The various file types have different degrees of support for the use cases and features, as described below. Use the legend to understand the support level.

| Support Level     | Description             |
|-------------------|-------------------------|
| &#10003;          | Supported               |
| &#10003; &Dagger; | Supported conditionally |
| &minus;           | Not applicable          |

## Add, upload, and view assets {#support-to-upload-view}

<!-- TBD: For AEM, AI files require the PDF option to be selected when saving the AI file.
-->

| Asset type        | [Browse](/help/assets/navigate-assets-view.md)   | Copy     | [Upload](/help/assets/add-delete-assets-view.md)   | Create   | [Delete](/help/assets/add-delete-assets-view.md#delete-assets)   | Details           | Image zoom | [Recently Viewed](/help/assets/navigate-assets-view.md) |
|-------------------|----------|----------|----------|----------|----------|-------------------|------------|-----------------|
| Raster images     | &#10003; | &#10003; | &#10003; | &minus;  | &#10003; | &#10003;          | &#10003;   | &#10003;        |
| RAW files         | &#10003; | &#10003; | &#10003; | &minus;  | &#10003; | &#10003;          | &#10003;   | &#10003;        |
| Folders           | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | &#10003;          | &minus;    | &minus;         |
| MP4 videos        | &#10003; | &#10003; | &#10003; | &minus;  | &#10003; | &#10003; &Dagger; | &minus;    | &#10003;        |
| PDF               | &#10003; | &#10003; | &#10003; | &minus;  | &#10003; | &#10003;          | &minus;    | &#10003;        |
| PSD, PSB, AI, and INDD | &#10003; | &#10003; | &#10003; | &minus;  | &#10003; | &#10003; &Dagger; | &minus;    | &#10003;        |
| Other binary files | &#10003; | &#10003; | &#10003; | &minus;  | &#10003; | &#10003; | &minus; | &#10003;        |

<!-- Hiding CC Libraries (considered beta) as per PM feedback.
| CC Libraries  | &#10003; | &minus;  | &#10003; | &#10003; | &#10003; | &#10003; | &minus;    | &minus;         |
-->

## Search, use, and edit assets {#support-to-search-use-edit}

| Asset type    | [Download](/help/assets/manage-organize-assets-view.md#download) | Drag and drop | [Image editor](/help/assets/edit-images-assets-view.md) | [Search](/help/assets/search-assets-view.md)   | [Smart Tags](/help/assets/metadata-assets-view.md#tags) | [Rename](/help/assets/manage-organize-assets-view.md)   | [Versions](/help/assets/manage-organize-assets-view.md#versions-of-assets) |
|---------------|----------|---------------|--------------|----------|------------|----------|----------|
| Raster images | &#10003; | &#10003;      | &#10003;     | &#10003; | &#10003;   | &#10003; | &#10003; |
| RAW files     | &#10003; | &#10003; | &minus; |  &#10003;   | &#10003; | &#10003;          | &#10003;   | &#10003;        |
| Folders       | &#10003; | &#10003;      | &minus;      | &#10003; | &minus;    | &#10003; | &#10003;  |
| Videos        | &#10003; | &#10003;      | &minus;      | &#10003; | &#10003;   | &#10003; | &#10003;  |
| CC Libraries  | &minus;  | &minus;       | &minus;      | &minus;  | &minus;    | &#10003; | &#10003;  |
| PDF           | &#10003; | &#10003;      | &minus;      | &#10003; | &#10003;   | &#10003; | &#10003;  |
| PSD and PSB          | &#10003; | &#10003;      | &minus;      | &#10003; | &#10003;   | &#10003; | &#10003;  |
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
| PSD, PSB, AI, and INDD | &minus;  | &#10003; | &#10003;  |
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

| Asset type    | [Metadata](/help/assets/metadata-assets-view.md)          | [Renditions](/help/assets/add-delete-assets-view.md#renditions) | [Trash](/help/assets/add-delete-assets-view.md#delete-assets)    | Copy     | Move     |
|---------------|-------------------|------------|----------|----------|----------|
| Raster images | &#10003; | &#10003;   | &#10003; | &#10003; | &#10003; |
| RAW files     | &#10003; | &#10003;   | &#10003; | &#10003; | &#10003; |
| Folders       | &#10003; | &minus;    | &#10003; | &#10003; | &#10003; |
| Videos        | &#10003; | &minus;    | &#10003; | &#10003; | &#10003; |
| CC Libraries  | &#10003; | &minus;    | &minus;  | &minus;  | &minus;  |
| PDF           | &#10003; | &minus;    | &#10003; | &#10003; | &#10003; |
| AI and INDD           | &#10003; | &minus;    | &#10003; | &#10003; | &#10003; |
| PSD and PSB           | &#10003; | &#10003;    | &#10003; | &#10003; | &#10003; |
| Other binary files          | &#10003; | &minus;    |&#10003; | &#10003; | &#10003; |

Users of [!DNL Adobe Asset Link] can upload and check-in (upload a new version) files into the [!DNL Assets view] repository from the supported [!DNL Adobe Creative Cloud] desktop applications.

<!-- TBD: Saving the template table separately for later use.
| Asset type    | Features |
|---------------|----------|
| Raster images |          |
| Folders       |          |
| Videos        |          |
| CC Libraries  |          |
| PDF files     |          |
| PSD, PSB           |          |
| AI            |          |
| INDD          |          |

>[!MORELIKETHIS]
>
>* []()
-->

## Next Steps {#next-steps}

* Provide product feedback using the [!UICONTROL Feedback] option available on the Assets view user interface

* Provide documentation feedback using [!UICONTROL Edit this page] ![edit the page](assets/do-not-localize/edit-page.png) or [!UICONTROL Log an issue] ![create a GitHub issue](assets/do-not-localize/github-issue.png) available on the right sidebar

* Contact [Customer Care](https://experienceleague.adobe.com/?support-solution=General#support)
