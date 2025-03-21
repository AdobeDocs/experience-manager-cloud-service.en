---
title: Content Automation for Creative Cloud integration
description: Generate variations of assets using Creative Cloud integration
contentOwner: AG
feature: Upload, Asset Processing, Publishing, Asset Compute Microservices
role: User, Admin
exl-id: 4cff355e-d12c-44c7-b519-4cc37f49e396
---
# Generate variations of assets using [!DNL Adobe Creative Cloud] integration {#content-automation}

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

Content automation add-on integrates [!DNL Adobe Experience Manager Assets] as a [!DNL Cloud Service] and [!DNL Adobe Creative Cloud] APIs to creatively process your assets at scale. [!DNL Experience Manager] uses cloud-based [asset microservices](/help/assets/asset-microservices-overview.md) to use the [!DNL Adobe Creative Cloud] features and automate the asset creation and media handling.

To edit assets in [!DNL Adobe Photoshop] and [!DNL Adobe Lightroom], you do not have to download assets from [!DNL Experience Manager Assets], edit, and upload them again. You create and configure a processing profile in [!DNL Experience Manager], apply the profile to a folder, and upload the assets to the folder. Your uploaded assets are reprocessed based on the processing profiles and you get variations of these assets. The consistent and effortless bulk processing saves manual efforts and increases content velocity, that too without the need of superb creative skills. Also, the developers and the partners can extend the asset microservices with direct access to these APIs and include custom logic.

Users can create processing profiles to automate the following creative operations on their assets:

* **Auto-tone**: Uses artificial intelligence to analyze the contents of the image and intelligently makes light and color corrections based on the unique attributes of the image.

* **Auto-upright**: Uses artificial intelligence to analyze the content of the image and correct skewed perspective in images. For example, to create level horizons.

   ![auto tone](/help/assets/assets/content-automation-autotone.png)

   *Figure: Auto-tone and auto-straighten can help improve skewed images.*

* **Lightroom presets**: Applies a user-defined look to images to achieve a consistent appearance using custom-made presets.

   ![Lightroom preset](/help/assets/assets/content-automation-lrpresets.png)

   *Figure: Adobe Lightroom preset to improve image quality in a consistent way for many images.*

* **Image Cutout**: Uses artificial intelligence to create selection around salient objects and remove background with a single command.

   ![Remove background and cut an image out of a photo](/help/assets/assets/content-automation-backgroundremove.png)

* **Image Mask**: Uses artificial intelligence to create mask around salient objects with a single command.

   ![Mask an image using AI](/help/assets/assets/content-automation-mask.png)

* **Photoshop Actions**: Applies a series of [!DNL Adobe Photoshop] tasks to a file or a batch of files.

   ![Photoshop actions](/help/assets/assets/content-automation-psactions.png)

* **Smart Object Replacement**: Does personalization at scale by allowing you to swap images while retaining all effects and adjustment applied within a PSD file.

   ![Replace objects smartly](/help/assets/assets/content-automation-objectreplace.png)

## Enable Content Automation for AEM as a Cloud Service program {#enable-content-automation}

To enable the Content Automation add-on for AEM as a Cloud Service program using Cloud Manager:

 1. Contact your account representative to license the Content Automation add-on.
 1. Access Cloud Manager and switch  to your organization using the organization selector.
 1. Click **[!UICONTROL Add Program]** and specify a program name.
 1. Click **[!UICONTROL Continue]**.
 1. Expand **[!UICONTROL Assets]** and select **[!UICONTROL Content Automation]**.
 1. Click **[!UICONTROL Create]**.
 1. Run the pipeline to [deploy the changes to Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/deploy-code.html).

 If you need to add Content Automation add-on to an existing AEM as a Cloud Service program in Cloud Manager:

   1. Click ... on the program card.

   1. Select **[!UICONTROL Edit Program]** and then select **[!UICONTROL Solutions & Add-ons]** tab.

   1. Expand **[!UICONTROL Assets]** and select **[!UICONTROL Content Automation]**.
   1. Click **[!UICONTROL Update]**.
   1. Run the pipeline to [deploy the changes to Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/deploy-code.html).

## Use a processing profile to edit your creative assets in bulk {#process-assets}

To use processing profiles to automatically create variations, follow these steps:

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Processing Profiles]**.

1. Select **[!UICONTROL Create]**, and specify a **[!UICONTROL Name]**.

1. Select the **[!UICONTROL Creative]** tab, specify the output folder, select **[!UICONTROL Add New]** to add a creative configuration.

1. Provide **[!UICONTROL Rendition Name]** (or output name), **[!UICONTROL Extension]** (or file type), select **[!UICONTROL Quality]** (or output parameters), select **[!UICONTROL Includes]** and **[!UICONTROL Excludes]** MIME type lists (or input asset filter), and select the required creative operation.

   ![[!UICONTROL Creative] tab in [!UICONTROL Processing Profile]](assets/creative-processing-profile.png)

1. Some operations require extra parameters (asset). Provide values for these extra parameters, if necessary.

1. Add more creative operations as a part of the same processing profile or Save the profile.

1. Apply the processing profile to a folder. On a folder's **[!UICONTROL Properties]** page, select **[!UICONTROL Asset Processing]**, and select the processing profile to apply.

After you apply the processing profile to a DAM folder, all the assets uploaded or updated in this folder execute the defined operations in addition to the standard processing. The subfolders inherit the same profiles as applied on the parent folders. Users can override this inheritance.

To process the existing assets, select the assets, select **[!UICONTROL Reprocess]** option, and then select the required processing profile.

## Tips and limitations {#limitations-best-practices}

* [!DNL Experience Manager] limits the asset processing to 300 requests per minute per environment and 700 requests per minute per organization.
* File size is limited to 4 GB for [!DNL Adobe Photoshop] API operations, and 1 GB for [!DNL Adobe Lightroom] operations.

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

>[!MORELIKETHIS]
>
>* [Configure and use asset microservices via processing profiles](/help/assets/asset-microservices-configure-and-use.md).
>* [Integrate [!DNL Experience Manager] with [!DNL Creative Cloud]](/help/assets/aem-cc-integration-best-practices.md).
>* [Asset ingestion and processing with asset microservices: An overview](/help/assets/asset-microservices-overview.md).
