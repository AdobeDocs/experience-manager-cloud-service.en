---
title: Approve assets in Experience Manager
description: Learn how to approve assets in [!DNL Experience Manager].
role: User
exl-id: fe61a0f1-94d3-409a-acb9-195979668c25
---
# Approve assets in [!DNL Experience Manager]

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

>[!AVAILABILITY]
>
>Dynamic Media with OpenAPI capabilities guide is now available in PDF format. Download the entire guide and use Adobe Acrobat AI Assistant to answer your queries. 
>
>[!BADGE Dynamic Media with OpenAPI capabilities Guide PDF]{type=Informative url="https://helpx.adobe.com/content/dam/help/en/experience-manager/aem-assets/dynamic-media-with-openapi-capabilities.pdf"}

Brand Managers and Marketers maintain strict control over brand assets. Only approved and latest version of the asset is available for use, ensuring brand consistency across all channels and applications. 

You can approve assets in AEM Assets to streamline asset management, ensuring a controlled and efficient process for handling assets.

## Before you begin {#pre-requisites}

You must have access to AEM Assets as a Cloud Service and permissions to edit the **[!UICONTROL Review Status]** property for an asset.

## Configuration 

You need to make a one-time update to the applicable metadata schema in Admin view before you can approve an asset. You can skip this configuration for Assets view. Follow these steps to configure the metadata schema:

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Schemas]**.
1. Select the applicable metadata schema and click **[!UICONTROL Edit]**. <br>The **[!UICONTROL Metadata Schema Form Editor]** opens with the **[!UICONTROL Basic]** tab highlighted. 
1. Scroll down and click **[!UICONTROL Review Status]**.
1. Click the **[!UICONTROL Rules]** tab on right side panel.
1. Uncheck **[!UICONTROL Disable edit]**.
  If you need to view the property that the **[!UICONTROL Review Status]** field is mapped to, navigate to **[!UICONTROL Settings]** tab and view the `./jcr:content/metadata/dam:status` value in the **[!UICONTROL Map to property]** field.
1. Drag and drop a **[!UICONTROL Dropdown]** field from the **[!UICONTROL Build Form]** section in right side to Metadata section in the form.
1. Click the newly added field, and then do the following updates in the **[!UICONTROL Settings]** panel:
    1. Change the **[!UICONTROL Field Label]** to _Approval Target_.
    1. Update the **[!UICONTROL Map to property]** to _./jcr:content/metadata/dam:activationTarget_. 
    1. Add the choices with `contenthub` and `delivery` as option values.

   >[!NOTE]
   >
   >When you select the approval target as Content Hub using the Assets view, the assets are made available in Content Hub to the users that are part of the same organization. When you select approval target as Delivery, the assets are available to all users.
   
1. Click **[!UICONTROL Save]**.

  >[!NOTE]
  >
  >If your assets or folders have a different default schema, make sure to make this update in that particular schema.
  
## Approve assets {#approve-assets}

To approve assets in [!DNL Experience Manager Admin view], follow these steps:

1. Select the asset (s) and click **[!UICONTROL Properties]** in the top pane.
1. In the **[!UICONTROL Basic]** tab, scroll down to **[!UICONTROL Review Status]**.
1. Change the review status to **[!UICONTROL Approved]**.
 ![image](/help/assets/assets/approve-old-ui.png)
1. Click **[!UICONTROL Save & Close]**. 

   >[!VIDEO](https://video.tv.adobe.com/v/3427430)

   Similarly, you can approve assets using the [new Assets view](/help/assets/manage-organize-assets-view.md).

## Bulk approve assets {#bulk-approve-assets}

Streamline your workflow by quickly approving multiple assets at once. You can bulk approve assets to expedite the approval process, saving time and enhancing productivity.
<br>Follow these steps to approve bulk assets in [!DNL Experience Manager Admin view]:

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

1. Drag and drop a **[!UICONTROL Dropdown]** field from the **[!UICONTROL Build Form]** section in right side to Metadata section in the form.
1. Click the newly added field, and then do the following updates in the **[!UICONTROL Settings]** panel:
    1. Change the **[!UICONTROL Field Label]** to _Approval Target_.
    1. Update the **[!UICONTROL Map to property]** to _./jcr:content/metadata/dam:activationTarget_. 
    1. Add the choices with `contenthub` and `delivery` as option values.

    >[!NOTE]
    >
    >When you select the approval target as Content Hub using the Assets view, the assets are made available in Content Hub to the users that are part of the same organization. When you select approval target as Delivery, the assets are available to all users.    
1. Click **[!UICONTROL Save]**.
1. In the **[!UICONTROL Metadata Profiles]** page, select the newly created metadata profile.
1. Click **[!UICONTROL Apply Metadata Profile to Folder(s)]** from the top action bar.
1. Select the folder(s) you need to approve and click **[!UICONTROL Apply]**.
<br> The permission for the entire folder is set for approval and any assets uploaded to this folder is automatically approved.
   
   >[!VIDEO](https://video.tv.adobe.com/v/3427431)

>[!NOTE]
> 
>This approach approves the newly created assets in the folder. For existing assets in the folder, you need to manually select and approve them. <br> Alternatively, you can use the **[!UICONTROL Reprocess]** option to apply the changes from the metadata profile to older assets.

Similarly, to bulk approve assets within a folder in Assets view:

1. Select the asset(s) and click **[!UICONTROL Bulk Metadata Edit]**.

1. Select **[!UICONTROL Approved]** in the **[!UICONTROL Status]** field available in the [!UICONTROL Properties] section in the right pane.

   If you select the status as `Approved`, and if [Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md) or [Content Hub](/help/assets/product-overview.md), or both are enabled for your Experience Manager Assets, you can view `Delivery` and `Content Hub` options available in the **[!UICONTROL Approval Target]** field. 
   
   * Select **[!UICONTROL Delivery]** to make the assets available to both Dynamic Media with OpenAPI capabilities and Content Hub. If you do not have Content Hub enabled, selecting this option makes the assets available to Dynamic Media with OpenAPI capabilities only.
   * Select **[!UICONTROL Content Hub]** to make the assets available to Content Hub.

    ![Approval status](/help/assets/assets/approval-status-delivery.png)

   If you are not using the default metadata form and cannot view the **[!UICONTROL Approval Target]** field, [edit your metadata form](/help/assets/metadata-assets-view.md#metadata-forms) to drag the **[!UICONTROL Approval for]** field from the available components to your metadata form and click **[!UICONTROL Save]**.

   >[!NOTE]
   >
   >If you select the approval target as `Content Hub` using the Assets view within an organization, the assets are made available in Content Hub to the users that are part of the same organization.

1. Click **[!UICONTROL Save]**.

## Copy delivery URL for approved assets {#copy-delivery-url-approved-assets}

The delivery URL for all approved assets in the repository is available if you have [!UICONTROL Dynamic Media with OpenAPI capabilities] enabled on your AEM as a Cloud Service instance.

To copy delivery URL for an approved asset within the repository:

1. Select the asset and click **[!UICONTROL Details]**.

1. Click the Dynamic Media icon available in the right pane.

1. Select **[!UICONTROL Dynamic Media with OpenAPI]** available in the **[!UICONTROL Dynamic Media]** Panel.

1. Click **[!UICONTROL Copy URL]** to copy the delivery URL of the asset.
![dynamic renditions](/help/assets/assets/dm-with-openapi-non-image-assets.png)

   >[!NOTE]
   >
   >The option to copy delivery URL for approved assets is just available in Assets view.

For information on other renditions that display within Dynamic Media panel, see [View and download Dynamic Media renditions](/help/assets/renditions.md#view-download-dm-renditions).
