---
title: Preview assets using [!DNL Dynamic Media with OpenAPI capabilities]
description: [!DNL Dynamic Media with OpenAPI capabilities] lets you preview assets in your Sites page before making them publicly available. Share the preview page with multiple stakeholders to refine assets through a review cycle, and create and track multiple asset versions throughout the review process.
role: Admin, User
---

# Asset preview using [!DNL Dynamic Media with OpenAPI capabilities]{#asset-preview-using-Dynamic-Media-with-OpenAPI-capabilities}

[!DNL Dynamic Media with OpenAPI capabilities] lets you preview assets available in your [!DNL Adobe Experience Manager (AEM) Sites] author page before making them publicly available. 

After generating the [!DNL Adobe Experience Manager (AEM) Sites] preview page including new assets, you can share this page with stakeholders to review and refine the assets before making them live. Throughout the review cycle, you can create and track multiple versions of an asset before publishing it for public consumption.
The workflow includes, app

[Generating an asset preview]() includes, updating an asset on the sites author page, and then publishing the page to generate a preview url of the page to share with stakeholders for review. [Revert to the original live asset]() until you finalize the updated version to publish. This helps maintain the integrity of the live site and ensures users continue to see the original, consistent asset.

## Before you begin{#prerequisites-for-previewing-assets-using-Dynamic-Media-with-OpenAPI-capabilities}

Ensure you have:

* Access to [!DNL AEM Assets as a Cloud Service].
* Permission to edit the Review Status property of assets.


## Preview an asset on a sites page {#asset-preview-on-sites-page-using-Dynamic-Media-with-OpenAPI-capabilities}

Follow these steps to preview an asset on your Sites page before publishing it live:

1. [Approve the asset for public delivery](#approve-asset-for-public-delivery)
2. d
3. d

### Approve the asset for public delivery {#approve-asset-for-public-delivery}

Execute the following steps to approve an asset for public delivery:

1. In [!DNL Assets View], select [!UICONTROL Assets] and navigate to your folder.
2. Select the asset to preview and click [!UICONTROL Details].
3. In the [!UICONTROL Information Panel], set [!UICONTROL Status] to [!UICONTROL Approved], then click [!UICONTROL Save].

   >[!NOTE]
   >
   >Only approved assets are available in the asset selector panel in the Sites authoring page for public delivery.

### Replace the existing asset and publish the Page {#approvasset-for-public-delivery}







----

After you preview the asset on the Sites page and share it with stakeholders for review, [revert to the original live asset]() until you finalize the updated version. This helps maintain the integrity of the live site and ensures users continue to see the original, consistent asset.

## Preview assets using [!DNL Dynamic Media with OpenAPI capabilities]{#Preview-assets-using-Dynamic-Media-with-OpenAPI-capabilities}

Execute the following steps to preview assets in your web page using [!DNL Dynamic Media with OpenAPI capabilities] before publishing them live:

1. On the [!DNL Assets View] home page, select **[!UICONTROL Assets]** and go to your folder. 
1. Select the asset to preview it in your sites page and click **[!UICONTROL Details]** to display the **[!UICONTROL Information panel]**.
1. Click the **[!UICONTROL Status]** field dropdown, select **[!UICONTROL Approved]** and click **[!UICONTROL  Save]** to approve the asset for public delivery using [!DNL Dynamic Media with OpenAPI capabilities]. Only approved assets are available for public delivery. These approved assets display in the Asset selector panel within the the [!DNL Adobe Experience Manager (AEM) Site] authoring page. 
1. Execute the steps in [Access remote assets in AEM Page Editor](/help/assets/integrate-remote-approved-assets-with-sites.md#access-remote-assets-in-aem-page-editor) section and select your latest approved asset using the asset selector panel in your [!DNL Adobe Experience Manager (AEM) Site] authoring page.
1. Execute the steps in [Publishing from the Page Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/publishing#publishing-from-the-page-editor) section to publish the page. See [Publishing Pages from the Sites Console](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/sites-console/publishing-pages#publishing-from-the-sites-console) section to publish your page from your site's console. After publishing is complete, **[!UICONTROL Page has been published]** message displays.
1. [Verify the publish status](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/sites-console/publishing-pages#determining-publication-status). Select [View as Published](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/introduction#view-as-published) from the authoring page to open a published view of your page in a new tab.
1. Navigate to the asset's details page in Assets View (of the asset approved above for public delivery), select Preview in the **[!UICONTROL Status]** field and click **[!UICONTROL  Save]**.
1. Go to your [!DNL Adobe Experience Manager (AEM) Site] authoring page and execute the steps in [Publishing Content to Preview](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/sites-console/previewing-content) section to generate the preview page of your content. Share this preview page with the stakeholders for review.
1. Navigate to the asset's details page of the asset that was earlier available on your live Sites page and select Approved status in the **[!UICONTROL Status]** field and click **[!UICONTROL  Save]** to approve the asset for public delivery using [!DNL Dynamic Media with OpenAPI capabilities].
1. Navigate to your [!DNL Adobe Experience Manager (AEM) Site] authoring page and execute the steps in [Access remote assets in AEM Page Editor](/help/assets/integrate-remote-approved-assets-with-sites.md#access-remote-assets-in-aem-page-editor) section to select your approved asset using the asset selector panel in your authoring page.
1. Execute the steps in [Publishing from the Page Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/publishing#publishing-from-the-page-editor) section to publish the page. After publishing is complete, **[!UICONTROL Page has been published]** message displays. Refresh the Published page to see the updated asset in the live page.

>[!TIP]
>
>TReplace *Preview* with *Publish* (or vice versa) in the *Preview* or *Publish* URL to switch between the preview and publish pages.

