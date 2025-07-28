---
title: Use [!DNL Dynamic Media with OpenAPI capabilities] to preview assets on AEM Site Page
description: Use [!DNL Dynamic Media with OpenAPI capabilities] to preview assets in your Sites page before making them publicly available. Share the preview page with multiple stakeholders to refine assets through a review cycle, and create and track multiple asset versions throughout the review process
role: Admin, User
---

# Use [!DNL Dynamic Media with OpenAPI capabilities] to preview assets on AEM Site Page{#asset-preview-using-Dynamic-Media-with-OpenAPI-capabilities}

[!DNL Dynamic Media with OpenAPI capabilities] lets you preview assets available in your [!DNL Adobe Experience Manager (AEM) Sites] author page before making them publicly available. 

To [generate an asset preview](#asset-preview-on-sites-page-using-Dynamic-Media-with-OpenAPI-capabilities) update the asset on the AEM sites author page and publish the page to generate a preview URL. Share this preview URL with stakeholders for review and feedback. After generating the preview page, [revert to the original live asset](#revert-to-the-original-live-asset) to keep the live site unchanged until you finalize the asset version for publishing. Reverting to the original live asset preserves the integrity of the live site and ensures that users continue to see the original, consistent asset.

During the review cycle, you can create and manage multiple versions of the asset before publishing the final version for public use.

## Before you begin{#prerequisites-for-previewing-assets-using-Dynamic-Media-with-OpenAPI-capabilities}

Ensure you have:

* Access to [!DNL AEM Assets as a Cloud Service].
* Permission to edit the Review Status property of assets.

## Preview an asset on a sites page {#asset-preview-on-sites-page-using-Dynamic-Media-with-OpenAPI-capabilities}

Follow these steps to preview an asset on your Sites page before publishing it live:

1. [ Set the asset status to [!UICONTROL Approved] for public delivery](#approve-asset-for-public-delivery)
2. [Replace the existing asset in your live site and publish the page](#replace-the-existing-asset-and-publish-the-page)
3. [Set the asset status to [!UICONTROL Preview] and generate a preview page](#set-the-asset-to-preview-status-and-generate-a-preview-page)

### Set the asset status to [!UICONTROL Approved] for public delivery{#approve-asset-for-public-delivery}

Execute the following steps to approve an asset for public delivery:

1. In [!DNL Assets View], select **[!UICONTROL Assets]** and navigate to your folder.
2. Select the asset to preview.
1. Click **[!UICONTROL Details]**.
3. In the [!UICONTROL Information Panel], set **[!UICONTROL Status]** to **[!UICONTROL Approved]**, then click **[!UICONTROL Save]**.

   >[!NOTE]
   >
   >Only approved assets are available in the asset selector panel in the Sites authoring page for public delivery.

### Replace the existing asset and publish the page {#replace-the-existing-asset-and-publish-the-page}

Execute these steps to replace the existing asset on your site with the latest approved asset and then publish the page:

1. In your Sites authoring page, follow the steps in [Access remote assets in AEM Page Editor](/help/assets/integrate-remote-approved-assets-with-sites.md#access-remote-assets-in-aem-page-editor) section to select the latest approved asset.
1. Publish the page by executing the steps in [Publishing from the Page Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/publishing#publishing-from-the-page-editor) section. Alternatively, follow the steps in [Publishing Pages from the Sites Console](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/sites-console/publishing-pages#publishing-from-the-sites-console) section to publish your page from your site's console.

   A confirmation message **[!UICONTROL Page has been published]** displays after successful publication.

1. Select [View as Published](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/introduction#view-as-published) from the authoring page to display a published view of your live page (with updated asset) in a new tab. Use this copy of your live page to [Verify the publish status](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/sites-console/publishing-pages#determining-publication-status).

### Set the asset status to [!UICONTROL Preview] and generate a preview page{#set-the-asset-to-preview-status-and-generate-a-preview-page}

Execute the following steps to change the asset status from approved to preview to generate a preview URL of the page:

1. In [!DNL Assets View], navigate to the asset's details page and change the **[!UICONTROL Status]** to **[!UICONTROL Preview]**. Click **[!UICONTROL Save]**.
1. Navigate to your Sites authoring page and follow the steps in the[Publishing Content to Preview](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/sites-console/previewing-content) section to generate a preview URL of your page. Share this preview URL with the stakeholders for review and feedback.

   >[!TIP]
   >
   >Switch between Preview and Publish versions of the page by replacing the word Preview with Publish (or vice versa) in the URL.

After sharing the preview page with the stakeholders for review, [revert to the original live asset](#revert-to-the-original-live-asset) until you finalize the asset version to publish. This step helps to maintain the integrity of the live site and ensure that users continue to see the original, consistent asset.

## Revert to the original live asset{#revert-to-the-original-live-asset}

Meanwhile, the stakeholders review your asset file and suggest changes, revert to the original live asset to keep the live site unchanged to ensure that your users continue to see the original, consistent asset. Execute the following steps to revert to the original live asset:

1. In [!DNL Assets View], locate the asset that was originally live, navigate to its details page and set the **[!UICONTROL Status]** to **[!UICONTROL Approved]**. Click **[!UICONTROL Save]**.
1. Navigate to your Sites authoring page and execute the steps in [Access remote assets in AEM Page Editor](/help/assets/integrate-remote-approved-assets-with-sites.md#access-remote-assets-in-aem-page-editor) section to select this re-approved asset using the asset selector panel. 
1. Publish the page again by executing the steps in [Publishing from the Page Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/publishing#publishing-from-the-page-editor) section.

After receiving the **[!UICONTROL Page has been published]** message, refresh the published page to confirm that the original asset is restored on the live site.