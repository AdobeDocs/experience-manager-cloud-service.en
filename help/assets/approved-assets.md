---
title: Approve assets in Experience Manager
description: Learn how to approve assets in [!DNL Experience Manager].
role: User
---
# Approve assets in [!DNL Experience Manager]

You can approve assets in AEM Assets to streamline asset management, ensuring a controlled and efficient process for handling assets.

## Before you begin

You must have access to AEM Assets CS and permissions to edit the **[!UICONTROL Review Status]** for assets.

## Configuration 

You need to make a one-time update to the default metadata schema in the [!DNL Experience Manager] before you can approve an asset. To make the update:

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Schemas]**.
1. Select the **[!UICONTROL default]** metadata schema and click **[!UICONTROL Edit]**. <br>The **[!UICONTROL Metadata Schema Form Editor]** opens with the **[!UICONTROL Basic]** tab highlighted. 

    >[!NOTE]
    >
    >If your assets or folders have a different default schema, make sure to make this update in that particular schema.

1. Scroll down and click **[!UICONTROL Review Status]**.
1. Click the **[!UICONTROL Rules]** tab on right side panel.
1. Uncheck **[!UICONTROL Disable edit]** and click **[!UICONTROL Save]**.

## Approve assets

To approve an asset in [!DNL Experience Manager Assets]:

1. Select the asset and click **[!UICONTROL Properties _(p)_]** in the top pane.
1. In the **[!UICONTROL Basic]** tab, scroll down to **[!UICONTROL Review Status]**.
1. Change the review status to **[!UICONTROL Approved]**.
1. Click **[!UICONTROL Save & Close]**. 
<!-- A toast message saying Properties updated successfully, apperas at the bottom of the screen. -->

### Video: Configure and approve assets in [!DNL Experience Manager]

>[!VIDEO]

## Bulk approve assets

Streamline your workflow by quickly approving multiple assets at once. You can bulk approve assets to expedite the approval process, saving time and enhancing productivity.
<br>To approve bulk assets:

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
1. In the **[!UICONTROL Metadata Profiles]** page, select the metadata profile you previously created.
1. Click **[!UICONTROL Apply Metadata Profile to Folder(s)]** from the top action bar.
1. Select the folder(s) you need to approve and click **[!UICONTROL Apply]**.
<br> The permission for the entire folder is set for approval and any assets uploaded to this folder is automatically approved.

### Video: Bulk approve assets in [!DNL Experience Manager]

>[!VIDEO]

>[!NOTE]
> 
>This approach approves the newly created assets in the folder. For existing assets in the folder, you need to manually select and approve them. <br> Alternatively, you can use the **[!UICONTROL Reprocess]** option to apply the changes from the metadata profile to older assets.
