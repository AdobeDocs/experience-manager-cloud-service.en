---
title: Approve assets in Content Hub
description: Approve assets in Content Hub
---
# Approve assets for Content Hub {#approve-assets-content-hub}

Brand Managers and Marketers maintain strict control over brand assets. Only approved and latest version of the asset is available for use within Content Hub, ensuring brand consistency across all channels and applications. 

You can approve assets using AEM Assets as a Cloud Service to streamline asset management, ensuring a controlled and efficient process for handling assets.

## Before you begin {#pre-requisites}

* Access to AEM Assets as a Cloud Service

* Role so that you have permissions to edit the **[!UICONTROL Status]** field available in [asset properties](/help/assets/manage-organize-assets-view.md##manage-asset-status) for an asset.

## Approve assets for Content Hub {#approve-assets-for-content-hub}

The assets marked as `approved` in Assets as a Cloud Service are automatically available in Content Hub.

To set the asset status as `approved` using Assets view within AEM as a Cloud Service:

1. Select the asset, and click **[!UICONTROL Details]** in the toolbar.

1. In the **[!UICONTROL Basic]** tab, select the asset status as `approved` from the **[!UICONTROL Status]** drop-down list.

   >[!VIDEO](https://video.tv.adobe.com/v/342495)

If you need to approve assets using Admin view, see [Approve assets using Admin view](/help/assets/approve-assets.md#approve-assets).

## Bulk Approve assets for Content Hub using Assets view {#bulk-approve-assets-content-hub}

Streamline your workflow by quickly approving multiple assets at once. You can bulk approve assets to expedite the approval process, saving time and enhancing productivity.


Bulk approve assets using Assets view for AEM Assets as a Cloud Service. All assets, approved in bulk, then become available in Content Hub.

To bulk approve assets within a folder in Assets view:

1. Select the asset(s) and click **[!UICONTROL Bulk Metadata Edit]**.

1. Select **[!UICONTROL Approved]** in the **[!UICONTROL Status]** field available in the [!UICONTROL Properties] section in the right pane.

1. Click **[!UICONTROL Save]**.

## How to switch between Assets and Admin views? {#access-assets-view-admin-view}

You can switch between Admin and Assets views in the following ways:
![My Workspace overview](assets/assets-view.png)

## Bulk Approve assets for Content Hub using Admin view {#bulk-approve-assets-content-hub-admin-view}

Follow these steps to approve bulk assets in [!DNL Experience Manager Admin view]:

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
    
1. Click **[!UICONTROL Save]**.
1. In the **[!UICONTROL Metadata Profiles]** page, select the newly created metadata profile.
1. Click **[!UICONTROL Apply Metadata Profile to Folder(s)]** from the top action bar.
1. Select the folder(s) you need to approve and click **[!UICONTROL Apply]**.
<br> The permission for the entire folder is set for approval and any assets uploaded to this folder is automatically approved.
   
   >[!VIDEO](https://video.tv.adobe.com/v/3427431)

>[!NOTE]
> 
>This approach approves the newly created assets in the folder. For existing assets in the folder, you need to manually select and approve them. <br> Alternatively, you can use the **[!UICONTROL Reprocess]** option to apply the changes from the metadata profile to older assets.

## Manage assets uploaded using Content Hub {#manage-assets-uploaded-using-content-hub}

[Content Hub users with rights to add assets](/help/assets/deploy-content-hub.md#onboard-content-hub-users-add-assets) can [add assets to the Content Hub](/help/assets/upload-brand-approved-assets.md) either from local file system or import assets from OneDrive or Dropbox data sources. All assets display at the top-level in Content Hub irrespective of the folder structure available on your local file system or OneDrive and Dropbox data sources to enhance the search capabilities.

The display of assets in Content Hub depends on if you have [enabled the **[!UICONTROL Auto-approval]** toggle](/help/assets/configure-content-hub-ui-options.md#configure-import-options-content-hub).

* If the **[!UICONTROL Auto-approval]** toggle is enabled, the assets that you uplaod using Content Hub are automatically available.

* If the **[!UICONTROL Auto-approval]** toggle is disabled, the assets that you upload using Content Hub do not display automatically. The assets are available in the `hydrated-assets` folder of your Assets as a Cloud Service environment. Navigate to the folder and [bulk edit](#bulk-approve-assets-content-hub) the status of those assets to `Approved` for those assets to display in Content Hub.



