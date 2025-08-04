---
title: Preview assets before using them in your AEM Sites pages 
description: Dynamic Media with OpenAPIs capabilities enables you to preview assets before using them in your live Adobe Experience Manager (AEM) Sites pages. The asset preview is available on your site's author and Preview tier, enabling you and your stakeholders to review and validate the updates to your assets before publishing the pages with updated assets. 
role: Admin, User
---

# Preview assets before using them in your AEM Sites pages {#asset-preview-using-Dynamic-Media-with-OpenAPIs-capabilities}

[!DNL Dynamic Media with OpenAPIs capabilities] lets you preview assets available in your [!DNL Adobe Experience Manager (AEM) Sites] author pages before making them publicly available. 

To [generate assets preview](#asset-preview-on-sites-pages-using-Dynamic-Media-with-OpenAPIs-capabilities) update your AEM Sites author page by either adding the new assets or replacing the existing ones and then publish the pages. **_Then, generate a preview URL of the page._**
Dynamic Media with OpenAPIs capabilities enables the updated assets' preview in your Sites preview page. **_The preview page mirrors your live site with updated assets_**. Share this preview page with stakeholders to collect feedback on the visual quality and contextual alignment of the updated assets. Refine the assets based on the feedback. 

**_After generating the preview page, [revert to the original live asset](#revert-to-the-original-live-asset) to keep the live site unchanged until you finalize the asset version suitable for public use. Reverting to the original live asset preserves the integrity of the live site and ensures that users continue to see the original, consistent asset._**

During the review cycle, you can create and manage multiple versions of the asset before publishing the final version for public use.

## Before you begin{#prerequisites-for-previewing-assets-using-Dynamic-Media-with-OpenAPIs-capabilities}

Ensure you have:

* Access to [!DNL AEM Assets as a Cloud Service].
* Permission to edit the Review Status property of assets.

## Preview assets in your sites preview page {#asset-preview-on-sites-pages-using-Dynamic-Media-with-OpenAPIs-capabilities}

Follow these steps to preview an asset in your site's Preview page (a replica of your live site) before publishing them live:

1. [ In Assets View, set the asset status to [!UICONTROL Approved] for public delivery](#approve-asset-for-public-delivery)
1. [Replace the existing asset in your live sites' author page and publish the pages](#replace-the-existing-asset-and-publish-the-pages)
1. [In Assets View, set the asset status to [!UICONTROL Preview] and publish your Sites authoring page to preview tier to generate a preview page](#set-the-asset-to-preview-status-and-generate-a-preview-page)

### Set the asset status to [!UICONTROL Approved] for public delivery{#approve-asset-for-public-delivery}

Execute the following steps to approve an asset for public delivery:

1. In [!DNL Assets View], select **[!UICONTROL Assets]** and navigate to your folder.
2. Select the asset to preview.
3. Click **[!UICONTROL Details]**.
4. In the [!UICONTROL Information Panel], set **[!UICONTROL Status]** to **[!UICONTROL Approved]**, then click **[!UICONTROL Save]**.
![](/help/assets/assets/asset-status.png)

   >[!NOTE]
   >
   >Only approved assets are available in the asset selector panel in the Sites authoring page for public delivery.

### Replace the existing asset and publish the pages {#replace-the-existing-asset-and-publish-the-pages}

Execute these steps to replace the existing asset on your site with the latest approved asset and then publish the pages:

1. In your Sites authoring page, select your latest approved asset by executing the steps in [Access remote assets in AEM Page Editor](/help/assets/integrate-remote-approved-assets-with-sites.md#access-remote-assets-in-aem-page-editor) section.
1. Publish the pages by executing the steps in [Publishing from the Page Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/publishing#publishing-from-the-page-editor) section. Alternatively, follow the steps in [Publishing Pages from the Sites Console](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/sites-console/publishing-pages#publishing-from-the-sites-console) section to publish your page from your site's console.
![The page has been published](/help/assets/assets/the-page-has-been-publushed.png)
A confirmation message **[!UICONTROL The page has been published]** displays after successful publishing.

1. Select [View as Published](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/introduction#view-as-published) option in the authoring page to display a published view of your live pages (with updated asset) in a new tab. Use this copy of your live pages to [Verify the publish status](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/sites-console/publishing-pages#determining-publication-status).

### Set the asset status to [!UICONTROL Preview] and generate a preview page{#set-the-asset-to-preview-status-and-generate-a-preview-page}

Execute the following steps to change the asset status from approved to preview in [!DNL Assets View] and then publish your Sites authoring page to preview tier to generate a preview URL of the page displaying the updated assets:

1. In [!DNL Assets View], navigate to the asset's details page and change the **[!UICONTROL Status]** to **[!UICONTROL Preview]**. Click **[!UICONTROL Save]**.
1. Navigate to your Sites authoring page and follow the steps in the [Publishing Content to Preview](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/sites-console/previewing-content) section to publish your page to preview tier using **[!UICONTROL Manage Publication]** option. Then, generate a preview URL of your page. Share this preview URL with the stakeholders for review and feedback. Ensure that your stakeholders have access to the preview page. See [Access the preview service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-environments#access-preview-service) for information on providing access to the preview pages.

   >[!TIP]
   >
   > Switch between Preview and Publish versions of the page by replacing the word Preview with Publish (or vice versa) in the preview or publish URL.

After sharing the preview page with the stakeholders for review, [revert to the original live asset](#revert-to-the-original-live-asset) until you finalize the asset version to publish. This step helps to maintain the integrity of the live site and ensure that users continue to see the original, consistent asset.

## Revert to the original live asset{#revert-to-the-original-live-asset}

Meanwhile, the stakeholders review your asset file and suggest changes, revert to the original live asset to keep the live site unchanged to ensure that your users continue to see the original, consistent asset. Execute the following steps to revert to the original live asset:

1. In [!DNL Assets View], locate the asset that was originally live, navigate to its details page and set the **[!UICONTROL Status]** to **[!UICONTROL Approved]**. Click **[!UICONTROL Save]**.
1. Navigate to your Sites authoring page and execute the steps in [Access remote assets in AEM Page Editor](/help/assets/integrate-remote-approved-assets-with-sites.md#access-remote-assets-in-aem-page-editor) section to select this re-approved asset using the asset selector panel. 
1. Publish the page again by executing the steps in [Publishing from the Page Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/publishing#publishing-from-the-page-editor) section.

After receiving the **[!UICONTROL The page has been published]** message, refresh the published page to confirm that the original asset is restored on the live site.