---
title: Manage your PDF documents in [!DNL Adobe Experience Manager].
description: Manage PDF documents in [!DNL Adobe Experience Manager] as a [!DNL Cloud Service].
feature: Asset Management
role: User, Admin
exl-id: 29660869-6902-4093-845b-cd629be59d4d
---
# Manage PDF documents in Experience Manager Assets as a Cloud Service {#add-assets-to-experience-manager}

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

Experience Manager Assets integrates with the Document Cloud PDF Viewer seamlessly, which lets you preview multiple pages of a PDF document. In addition, you can also use advanced Document Cloud PDF viewer features such as annotations, search text, navigate the PDF document using bookmarks and thumbnails, and more under the same roof. Experience Manager Assets also lets you upload documents in other supported formats and preview them in a PDF format.

Document Cloud PDF viewer benefits AEM Assets in the following ways:

* [Support for PDF Document Cloud Viewer Components](#pdf-doc-cloud)
* [Support for Multiple Pages Preview and Annotations for PDF Asset](#multi-page)
* [Support for Multiple Pages Preview for Documents in Other Formats](#multi-format)

>[!TIP]
>
> If you are unable to get multiple pages preview of a previously uploaded PDF document then select the PDF and click ![Reprocess](/help/assets/assets/Reprocess.svg) **Reprocess Assets**.

## Support for PDF Document Cloud Viewer Components {#pdf-doc-cloud}

The native PDF Doc Cloud viewer has the following components in AEM Assets:

* **PDF viewer using page thumbnails** Thumbnail view is a small preview of the pages of a PDF document. Using thumbnails, you can directly jump to the desired page. You can access thumbnails of the selected PDF document through ![thumbnail](/help/assets/assets/thumbnail.svg) on the left pane.

* **PDF viewer using bookmarks** Bookmark is a direct link that navigates you to the content in the document. You can access bookmarks of the selected PDF document through ![bookmark](/help/assets/assets/bookmark.svg) on the left pane.

* **Search in PDF** You can use search ![search](/help/assets/assets/Search.svg) to look up the text in the PDF document.

* **Page Up/Page Down** Use Page Up ![Page Up](/help/assets/assets/ArrowUp.svg) or Page Down ![Page Down](/help/assets/assets/ArrowDown.svg) to scroll through the document.

* **Zoom Out/Zoom In** Use Zoom Out ![Zoom Out](/help/assets/assets/Zoom-out.svg) or Zoom In ![Zoom In](/help/assets/assets/zoom-in.svg) to streak the document.

* **Page Fit** Use width or height dimensions to fit the document as per your screen size. 

* **Dock/Undock PDF** You can dock or undock the components of native PDF viewer using this option.

## Support for Multiple Pages Preview and Annotations for PDF Asset {#multi-page}

Adobe Experience Manager Assets lets you preview PDF document consisting of several pages. To preview multiple pages of a PDF document, consider the following steps:

1.  Follow the steps to [upload assets in AEM](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/assets/manage/add-assets.html?lang=en).
1.  Browse the PDF document that you want to upload and preview.
1.  Open the document.
1.  The PDF document viewer loads by default. You can also select PDF rendition under the rendition panel.
1.  Under Renditions drop-down, select **All Renditions**.

You can also apply [annotations](#pdf-annotations) to the PDF document in a multiple pages preview.

>[!NOTE]
>
> The maximum size of an Asset that you can preview is up to 100 MB.

>[!VIDEO](https://video.tv.adobe.com/v/3409355)

<!--
![Multi-page Preview](/help/assets/assets/multi-page.png)
-->

**PDF Annotations {#pdf-annotations}** 

Experience Manager Assets lets you add comments to a PDF document. A PDF document can have multiple annotations. 

To annotate a PDF document, perform the following steps:

1.  Go to the Assets interface, navigate to the PDF document that you want to annotate. The native PDF viewer opens on the right showing preview of the selected PDF document.
1.  Click **Annotate** from the top menu.
Following are the Annotations that can be applied on a PDF document:

<table>
        <tr>
             <th> Annotation </th>
            <th> Description </th>
        </tr>
        <tr>
           <td> <img src="/help/assets/assets/Comment.svg"> Comment </td>
            <td> Select Comment to express an observation. </td>
        </tr>
        <tr>
            <td> <img src="/help/assets/assets/Text.svg"> Textbox </td>
            <td> Select Textbox to enter the text. </td>
        </tr>
        <tr>
            <td> <img src="/help/assets/assets/Note.svg"> Sticky notes </td>
            <td> Add a small text or reminder that you can add to a particular area on the PDF. </td>
        </tr>
        <tr>
            <td> <img src="/help/assets/assets/Comment.svg"> Text highlighter </td>
            <td> Select the text to highlight in different colors. </td>
        </tr>
        <tr>
            <td> <img src="/help/assets/assets/TextUnderline.svg"> Text underliner </td>
            <td> Select the text that you want to underline. </td>
        </tr>
        <tr>
            <td> <img src="/help/assets/assets/TextStrikethrough.svg"> Strikethrough </td>
            <td> Select the text that you want to cross out. </td>
        </tr>
        <tr>
            <td> <img src="/help/assets/assets/Draw.svg"> Drawing </td>
            <td> Insert a visual art to the PDF. </td>
        </tr>
        <tr>
            <td> <img src="/help/assets/assets/Erase.svg"> Erase drawing </td>
             <td> Remove or undo drawing. </td>
        </tr>
    </table>

>[!NOTE]
>
>The annotations that you add to the PDF document are available in the preview mode. However, the annotations are not displayed when you download or print the PDF document. 

## Support for Multiple Pages Preview for Documents in Other Formats {#multi-format}

In addition to the PDF documents, you can also preview multiple pages for documents in other format types. The supported document format types are TXT, RTF, DOC, DOCX, PPT, PPTX, XLS, and XLSX. Experience Manager Assets automatically converts these document formats into a PDF format and make them available for preview.

![Multi-page Preview of Documents in Other Formats](/help/assets/assets/multi-page-other-formats.png)

For the multiple page preview of other supported document formats, perform the following steps:

1.  Follow the steps to [upload assets in AEM](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/assets/manage/add-assets.html?lang=en).
1.  Browse the document that you want to upload and preview.
1.  Open the document.
1.  Select PDF under the static section in the left panel. The right panel showcases the multiple pages preview of an Asset. Select thumbnail from the left panel to choose the page that you want to preview.

>[!NOTE]
>
> * The maximum size of an Asset that you can preview is up to 100 MB.
> * The maximum size of XLS or XLSX files to preview is 20 MB.

**See also**

* [Translate Assets](translate-assets.md)
* [Assets HTTP API](mac-api-assets.md)
* [Assets supported file formats](file-format-support.md)
* [Search assets](search-assets.md)
* [Connected assets](use-assets-across-connected-assets-instances.md)
* [Asset reports](asset-reports.md)
* [Metadata schemas](metadata-schemas.md)
* [Download assets](download-assets-from-aem.md)
* [Manage metadata](manage-metadata.md)
* [Search facets](search-facets.md)
* [Manage collections](manage-collections.md)
* [Bulk metadata import](metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)
