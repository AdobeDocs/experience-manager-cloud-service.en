---
title: Approve assets for Content Hub
description: Learn how to approve assets in Assets as a Cloud Service to make them available in Content Hub.
exl-id: fc849028-ab56-4388-b8d6-e36cac8f868f
---
# Approve assets for Content Hub {#approve-assets-content-hub}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

![Approve assets for Content Hub](assets/content-hub-approve-assets.png)

>[!AVAILABILITY]
>
>Content Hub guide is now available in PDF format. Download the entire guide and use Adobe Acrobat AI Assistant to answer your queries. 
>
>[!BADGE Content Hub Guide PDF]{type=Informative url="https://helpx.adobe.com/content/dam/help/en/experience-manager/aem-assets/content-hub.pdf"}

Brand Managers and Marketers maintain strict control over brand assets. Only approved and latest version of the asset is available for use within Content Hub, ensuring brand consistency across all channels and applications. 

You can approve assets using AEM Assets as a Cloud Service to streamline asset management, ensuring a controlled and efficient process for handling assets.

## Before you begin {#pre-requisites}

Before you begin, you should have:

* Access to AEM Assets as a Cloud Service

* Write permissions to edit asset metadata to be able to edit the **[!UICONTROL Status]** field available in [asset properties](/help/assets/manage-organize-assets-view.md##manage-asset-status) for an asset.

## Approve assets for Content Hub{#approve-assets-for-content-hub}

The assets marked as `approved` in Assets as a Cloud Service are automatically available in Content Hub.

>[!NOTE]
>
>Assets as a Cloud Service and Content Hub must use the same organization for the assets to display in Content Hub.

To set the asset status as `approved` using Assets view within AEM as a Cloud Service:

1. Select the asset, and click **[!UICONTROL Details]** in the toolbar.

1. In the **[!UICONTROL Basic]** tab, select the asset status as `approved` from the **[!UICONTROL Status]** drop-down list.
1. Click **[!UICONTROL Save]**.

   >[!VIDEO](https://video.tv.adobe.com/v/3433172)

If you need to approve assets using Admin view, see [Approve assets using Admin view](/help/assets/approve-assets.md#approve-assets).

## Bulk Approve assets for Content Hub using Assets view {#bulk-approve-assets-content-hub}

Bulk approve assets using Assets view for AEM Assets as a Cloud Service. All assets, approved in bulk, then become available in Content Hub.

To bulk approve assets within a folder in Assets view:

1. Select the asset(s) and click **[!UICONTROL Bulk Metadata Edit]**.

1. Select **[!UICONTROL Approved]** in the **[!UICONTROL Status]** field available in the [!UICONTROL Properties] section in the right pane.

1. Click **[!UICONTROL Save]**.

## Automate approval for newly ingested assets in Admin view {#automate-approval-newly-ingested-assets}

After switching from Assets view to Admin view, you can set up folder settings so that all new assets added to the folder get approved automatically.

You can switch between Admin and Assets views in the following ways:
![My Workspace overview](assets/assets-view.png)

Follow these steps to automate approval for newly ingested assets in [!DNL Experience Manager Admin view]:

1. Create a folder in the author environment (https://author-pXXX-eYYY.adobeaemcloud.com). Replace _XXX_ with your program ID and _YYY_ with the environment ID from the Experience Manager.
1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Profiles]**.
1. Click **[!UICONTROL Create]** in the top right side of the page.
1. Add a Profile title and click **[!UICONTROL Create]**. The metadata profile is successfully created.
1. Select the newly created metadata profile and click **[!UICONTROL Edit _(e)_]**. <br>The **[!UICONTROL Edit Metadata Profile]** form opens with the **[!UICONTROL Basic]** tab highlighted. 
1. Drag and drop a **[!UICONTROL Single Line Text Field]** from the **[!UICONTROL Build Form]** section in right side to Metadata section in the form.
1. Click the newly added field, and then do the following updates in the **[!UICONTROL Settings]** panel:
    1. Change the **[!UICONTROL Field Label]** to _Approved Assets_.
    1. Update the **[!UICONTROL Map to property]** to _./jcr:content/metadata/dam:status_. 
    1. Change the Default value to _approved_.

1. Similar to Step 6, drag a **[!UICONTROL Single Line Text Field]** from the **[!UICONTROL Build Form]** section in right side to Metadata section in the form.
1. Click the newly added field, and then do the following updates in the **[!UICONTROL Settings]** panel:
    1. Change the **[!UICONTROL Field Label]** to _Activation Target_.
    1. Update the **[!UICONTROL Map to property]** to _./jcr:content/metadata/dam:activationTarget_. 
    1. Change the Default value to _contenthub_.
    
1. Click **[!UICONTROL Save]**.
1. In the **[!UICONTROL Metadata Profiles]** page, select the newly created metadata profile.
1. Click **[!UICONTROL Apply Metadata Profile to Folder(s)]** from the top action bar.
1. Select the folder(s) you need to approve and click **[!UICONTROL Apply]**.
<br> The permission for the entire folder is set for approval and any assets uploaded to this folder is automatically approved.
   
   >[!VIDEO](https://video.tv.adobe.com/v/3427431)

>[!NOTE]
> 
>This approach approves the newly created assets in the folder. For existing assets in the folder, you need to manually select and approve them.

## Manage assets uploaded using Content Hub {#manage-assets-uploaded-using-content-hub}

[Content Hub users with rights to add assets](/help/assets/deploy-content-hub.md#onboard-content-hub-users-add-assets) can [add assets to the Content Hub](/help/assets/upload-brand-approved-assets.md) either from local file system or import assets from OneDrive or Dropbox data sources. All assets display at the top-level in Content Hub irrespective of the folder structure available on your local file system or OneDrive and Dropbox data sources to enhance the search capabilities.

The display of assets uploaded using Content Hub depends on if you have [enabled the Auto-approval toggle](/help/assets/configure-content-hub-ui-options.md#configure-import-options-content-hub):

* If the **[!UICONTROL Auto-approval]** toggle is enabled, the assets that you upload using Content Hub are automatically available.

* If the **[!UICONTROL Auto-approval]** toggle is disabled, the assets that you upload using Content Hub do not display automatically. The assets are available in the `hydrated-assets` folder of your Assets as a Cloud Service environment. Navigate to the folder and [bulk edit](#bulk-approve-assets-content-hub) the status of those assets to `Approved` for those assets to display in Content Hub.

![Content Hub approval process](/help/assets/assets/content-hub-approval.png)
