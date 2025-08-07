---
title: Preview assets before using them in your AEM Sites pages 
description: Dynamic Media with OpenAPI capabilities enables you to preview assets before using them in your Adobe Experience Manager (AEM) Sites pages. The asset preview is available on your site's author and Preview tier, enabling you and your stakeholders to review and validate the updates to your assets before publishing the pages with updated assets. 
role: Admin, User
---

# Preview assets before using them in your AEM Sites pages {#asset-preview-using-Dynamic-Media-with-OpenAPI-capabilities}

[!DNL Dynamic Media with OpenAPI capabilities] lets you preview assets available in your [!DNL Adobe Experience Manager (AEM) Sites] author pages before making them publicly available. .

To [generate assets preview](#asset-preview-on-sites-pages-using-Dynamic-Media-with-OpenAPI-capabilities), update your AEM Sites author pages by either adding the new assets or replacing the existing ones. Then publish your updated author pages to the preview tier to generate a preview URL of the page. [!DNL Dynamic Media with OpenAPI capabilities] enables the preview of updated assets in your Sites preview tier. Share this preview page with stakeholders to collect feedback on the visual quality and contextual alignment of the updated assets. Refine the assets based on the feedback. 

During the review cycle, you can create and manage multiple versions of the asset before publishing the final version for public use.

## Before you begin{#prerequisites-for-previewing-assets-using-Dynamic-Media-with-OpenAPI-capabilities}

Ensure you have:

* Access to [!DNL AEM Assets as a Cloud Service].
* Permission to edit the Review Status property of assets.
* [Added [!UICONTROL Preview] value to the [!UICONTROL  Status] metadata property available in [!UICONTROL Basic] tab](/help/assets/metadata-schemas.md#edit-metadata-schema-forms) of the metadata form applied to the folder containing the assets to preview.
![Add Preview option](/help/assets/assets/metedata-form-preview.png)
* The key to generate the preview token. [Contact Adobe support](https://helpx.adobe.com/in/contact.html) and raise a request for the key.

## Preview assets in your sites preview page {#asset-preview-on-sites-pages-using-Dynamic-Media-with-OpenAPI-capabilities}

You can preview new assets or assets that are already approved. Approved assets only display on your live Sites pages.

Execute the following steps to set the asset status to preview in [!DNL Assets View] and then publish your Sites authoring page to the preview tier to generate a preview URL of the page:

1. Set asset status to **[!UICONTROL Preview]** by executing the following steps:

   1. In [!DNL Assets View], select **[!UICONTROL Assets]** and navigate to your folder.
   1. Select the asset to preview.
   1. Click **[!UICONTROL Details]**.
   1. In the [!UICONTROL Information Panel], set **[!UICONTROL Status]** to **[!UICONTROL Preview]**, then click **[!UICONTROL Save]**.
   ![Preview](/help/assets/assets/preview-boat-at-bay.png)

1. Navigate to your Sites authoring page. Execute the steps in [Access remote assets in AEM Page Editor](/help/assets/integrate-remote-approved-assets-with-sites.md#access-remote-assets-in-aem-page-editor) section to select the asset you recently set to Preview (status) using the Asset Selector panel. 

   >[!NOTE] 
   >
   > The Asset Selector displays assets with the most recent status update set to either Approved or Preview.

1. Publish your page to the preview tier using the **[!UICONTROL Manage Publication]** option. Execute the steps in the [Publishing Content to Preview](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/sites-console/previewing-content) section to publish your page to the preview tier. After publishing, generate a preview URL of your page. The Preview page displays the assets (with most recent status updates) in your Sites page. 

Share this preview URL with the stakeholders for review and feedback. Ensure that your stakeholders have access to the preview page. See [Access the preview service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-environments#access-preview-service) for information on providing access to the preview pages.

   >[!NOTE]
   >
   >The [Image V3 core component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/wcm-components/image#version-and-compatibility) supports preview version of assets by default. When you select a preview version of an asset (asset with preview status) using the [Asset Selector](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/manage/asset-selector/asset-selector-upload) panel, the Image V3 component automatically renders it in the Preview tier (a preview version on your Sites author page).

After finalising the asset version, [publish your page](#publish-assets-to-publish-tier) to the publish tier for public consumption.

## Publish assets{#publish-assets-to-publish-tier}

After finalising the asset version for public use, set the asset status to **[!UICONTROL Approved]** and then publish your pages to the publish tier. Execute the following steps to publish your page:

1. Follow step 1 in [Preview assets in your sites preview page](#asset-preview-on-sites-pages-using-Dynamic-Media-with-OpenAPI-capabilities) section above to change asset status to **[!UICONTROL Approved]**. 
1. Navigate to your Sites author page and publish it to the [!DNL Publish tier]. Publish the pages by executing the steps in [Publishing from the Page Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/publishing#publishing-from-the-page-editor) section. 
Alternatively, follow the steps in [Publishing Pages from the Sites Console](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/sites-console/publishing-pages#publishing-from-the-sites-console) section to publish your page from your site's console.

   >[!NOTE]
   >
   > Only Approved assets are published to the Publish tier. Approve the assets before publishing them to the Publish tier for public use.

   ![The page has been published](/help/assets/assets/the-page-has-been-publushed.png)
A confirmation message **[!UICONTROL The page has been published]** displays after successful publishing.

## Verify the publish status{#verify-the-publish-status}

After publishing your page, verify that the new assets are available on your Sites page. Execute the following step to verify the publish status:

1. Select [View as Published](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/introduction#view-as-published) option in the authoring page to display a published view of your live pages (with new or updated asset) in a new tab. Use this copy of your live pages to [Verify the publish status](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/sites-console/publishing-pages#determining-publication-status).

   >[!TIP]
   >
   > Switch between Preview and Publish versions of the page by replacing the word Preview with Publish (or vice versa) in the preview or publish URL.

