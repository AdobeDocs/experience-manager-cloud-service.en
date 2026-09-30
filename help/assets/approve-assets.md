---
title: Approve assets in Experience Manager
description: Learn how to approve assets in [!DNL Experience Manager].
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: fe61a0f1-94d3-409a-acb9-195979668c25
---
# Approve assets in [!DNL Experience Manager]

Brand Managers and Marketers maintain strict control over brand assets. Only the **approved, latest version** of an asset is available for use. This ensures **brand consistency** across all channels and applications, because downstream users can only access assets that have already been reviewed and approved.

You can approve assets in **Adobe [!DNL Experience Manager] (AEM) Assets** to streamline asset management, establishing a controlled and efficient process for handling assets throughout their lifecycle.

## Why asset approval matters

Asset approval acts as a governance checkpoint in the digital asset management (DAM) workflow. When an asset is approved, it is designated as the authoritative, ready-to-use version, while unapproved or superseded versions are held back from general distribution. This distinction matters because it protects the brand from the accidental use of outdated, off-brand, or unlicensed content.

By approving assets in AEM Assets, Brand Managers and Marketers create a **single source of truth** for creative and marketing teams. As a result, everyone across the organization draws from the same reviewed set of assets, reducing the risk of inconsistent messaging and visual identity across campaigns, websites, and applications.

## Benefits of approving assets in AEM Assets

- **Ensures brand consistency:** Only approved, current versions are available, so every channel and application reflects the correct, on-brand content.
- **Enforces version control:** Because approval is tied to the latest version, teams avoid distributing superseded or draft assets.
- **Streamlines asset management:** A defined approval step creates a controlled, repeatable, and efficient process for handling assets.
- **Maintains strict brand governance:** Brand Managers and Marketers retain oversight of which assets are cleared for use, keeping control of brand assets in the hands of accountable stakeholders.
- **Reduces downstream errors:** Restricting access to approved assets prevents the accidental publication of outdated or unauthorized material.

Approving assets is a foundational step in a governed asset management workflow, connecting review and control directly to the assets that teams ultimately publish and reuse.

## Before you begin {#pre-requisites}

Before you start, confirm that both of the following prerequisites are met. Meeting these requirements upfront ensures you can complete the workflow without interruption:

- **Access to Adobe [!DNL Experience Manager] (AEM) Assets as a Cloud Service.** You must have an active account with access to your organization's AEM Assets as a Cloud Service environment.
- **Permissions to edit the [!UICONTROL Review Status] property for an asset.** Your user profile must include the permissions required to modify the **[!UICONTROL Review Status]** property on an asset.

These permissions ensure you are authorized to change an asset's review state, because AEM Assets restricts property edits to users with the appropriate access level. If you cannot access AEM Assets as a Cloud Service or cannot edit the **[!UICONTROL Review Status]** property, contact your administrator to request the necessary access before proceeding.

## Configuration

You must make a one-time update to the applicable metadata schema in Admin view before you can approve an asset. This update exposes the approval target field that the approval workflow relies on, which is why the configuration is a prerequisite for the approval action. You can skip this configuration for Assets view, because that view already provides the required approval controls. Completing this setup once enables asset approval and determines how approved assets are subsequently made available.

Follow these steps to configure the metadata schema:

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Schemas]**.
1. Select the applicable metadata schema and click **[!UICONTROL Edit]**. <br>The **[!UICONTROL Metadata Schema Form Editor]** opens with the **[!UICONTROL Basic]** tab highlighted.
1. Scroll down and click **[!UICONTROL Review Status]**.
1. Click the **[!UICONTROL Rules]** tab on right side panel.
1. Uncheck **[!UICONTROL Disable edit]**. Unchecking this option allows the **[!UICONTROL Review Status]** field to be edited during the approval process.
  If you need to view the property that the **[!UICONTROL Review Status]** field is mapped to, navigate to **[!UICONTROL Settings]** tab and view the `./jcr:content/metadata/dam:status` value in the **[!UICONTROL Map to property]** field.
1. Drag and drop a **[!UICONTROL Dropdown]** field from the **[!UICONTROL Build Form]** section in right side to Metadata section in the form.
1. Click the newly added field, and then do the following updates in the **[!UICONTROL Settings]** panel:
    1. Change the **[!UICONTROL Field Label]** to _Approval Target_.
    1. Update the **[!UICONTROL Map to property]** to _./jcr:content/metadata/dam:activationTarget_.
    1. Add the choices with `contenthub` and `delivery` as option values. These two option values define where an approved asset is delivered.

   >[!NOTE]
   >
   >When you select the approval target as Content Hub using the Assets view, the assets are made available in Content Hub to the users that are part of the same organization. When you select approval target as Delivery, the assets are available to all users.

1. Click **[!UICONTROL Save]** to apply the schema changes.

   >[!NOTE]
   >
   >If your assets or folders have a different default schema, make sure to make this update in that particular schema. Applying the update only to the correct default schema ensures the approval target field appears for the assets that use it.

## Approve assets {#approve-assets}

Approving assets in [!DNL Experience Manager Admin view] marks them as ready for use in production or downstream publishing. To approve one or more assets in the Admin view, follow these steps:

1. Select the asset (s) and click **[!UICONTROL Properties]** in the top pane.
1. In the **[!UICONTROL Basic]** tab, scroll down to **[!UICONTROL Review Status]**, the field that tracks whether an asset has been reviewed and approved for use.
 ![image](/help/assets/assets/approve-old-ui.png)
1. Change the review status to **[!UICONTROL Approved]**. This designates the asset as reviewed and cleared for use, signaling to other users that it has passed review.
1. Click **[!UICONTROL Save & Close]**. 

   >[!VIDEO](https://video.tv.adobe.com/v/3427430)

   Similarly, you can approve assets using the [new Assets view](/help/assets/manage-organize-assets-view.md), which provides the same approval capability within an updated interface. Establishing an approved review status supports governance and quality control across the asset lifecycle.

## Bulk approve assets {#bulk-approve-assets}

Streamline your workflow by quickly approving multiple assets at once. Bulk approval expedites the approval process, saving time and enhancing productivity for teams that manage large asset libraries. By configuring a metadata profile, you apply the approved status to assets automatically at the folder level, which eliminates the need to approve each asset individually and ensures consistent, repeatable approval across your content operations.
<br>Follow these steps to approve bulk assets in [!DNL Experience Manager Admin view]:

1. Create a folder in the author environment (https://author-pXXX-eYYY.adobeaemcloud.com). Replace _XXX_ with your program ID and _YYY_ with the environment ID from Adobe [!DNL Experience Manager] (AEM).
1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Profiles]**.
1. Click **[!UICONTROL Create]** in the top right side of the page.
1. Add a Profile title and click **[!UICONTROL Create]**. The metadata profile is successfully created.
1. Select the newly created metadata profile and click **[!UICONTROL Edit _(e)_]**. <br>The **[!UICONTROL Edit Metadata Profile]** form opens with the **[!UICONTROL Basic]** tab highlighted. 
1. Drag and drop a **[!UICONTROL Single Line Text Field]** from the **[!UICONTROL Build Form]** section in right side to Metadata section in the form.
1. Click the newly added field, and then do the following updates in the **[!UICONTROL Settings]** panel:
    1. Change the **[!UICONTROL Field Label]** to _Approved Assets_.
    1. Update the **[!UICONTROL Map to property]** to _./jcr:content/metadata/dam:status_. 
    1. Change the Default value to _approved_. This sets the approval status that the profile applies to assets in the target folder.

1. Drag and drop a **[!UICONTROL Dropdown]** field from the **[!UICONTROL Build Form]** section in right side to Metadata section in the form.
1. Click the newly added field, and then do the following updates in the **[!UICONTROL Settings]** panel:
    1. Change the **[!UICONTROL Field Label]** to _Approval Target_.
    1. Update the **[!UICONTROL Map to property]** to _./jcr:content/metadata/dam:activationTarget_. 
    1. Add the choices with `contenthub` and `delivery` as option values.

    >[!NOTE]
    >
    >When you select the approval target as **Content Hub** using the Assets view, the assets are made available in Content Hub to the users that are part of the same organization. When you select approval target as **Delivery**, the assets are available to all users.    
1. Click **[!UICONTROL Save]**.
1. In the **[!UICONTROL Metadata Profiles]** page, select the newly created metadata profile.
1. Click **[!UICONTROL Apply Metadata Profile to Folder(s)]** from the top action bar.
1. Select the folder(s) you need to approve and click **[!UICONTROL Apply]**. This binds the profile to the folder so that the approved status and approval target are applied automatically.
<br> The permission for the entire folder is set for approval and any assets uploaded to this folder is automatically approved.
   
   >[!VIDEO](https://video.tv.adobe.com/v/3427431)

>[!NOTE]
> 
>This approach approves the newly created assets in the folder. For existing assets in the folder, you need to manually select and approve them. <br> Alternatively, you can use the **[!UICONTROL Reprocess]** option to apply the changes from the metadata profile to older assets.

### Bulk approve assets within a folder in Assets view

Similarly, to bulk approve assets within a folder in Assets view:

1. Select the asset(s) and click **[!UICONTROL Bulk Metadata Edit]**.

1. Select **[!UICONTROL Approved]** in the **[!UICONTROL Status]** field available in the [!UICONTROL Properties] section in the right pane.

   If you select the status as **`Approved`**, and if [Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md) or [Content Hub](/help/assets/product-overview.md), or both are enabled for your [!DNL Experience Manager] Assets, you can view **`Delivery`** and **`Content Hub`** options available in the **[!UICONTROL Approval Target]** field. 
   
   * Select **[!UICONTROL Delivery]** to make the assets available to both **Dynamic Media with OpenAPI capabilities** and **Content Hub**. If you do not have Content Hub enabled, selecting this option makes the assets available to Dynamic Media with OpenAPI capabilities only.
    ![Approval status](/help/assets/assets/approval-status-delivery.png)
   * Select **[!UICONTROL Content Hub]** to make the assets available to **Content Hub**.


   If you are not using the default metadata form and cannot view the **[!UICONTROL Approval Target]** field, [edit your metadata form](/help/assets/metadata-assets-view.md#metadata-forms) to drag the **[!UICONTROL Approval for]** field from the available components to your metadata form and click **[!UICONTROL Save]**.

   >[!NOTE]
   >
   >If you select the approval target as **`Content Hub`** using the Assets view within an organization, the assets are made available in Content Hub to the users that are part of the same organization.

1. Click **[!UICONTROL Save]**.

## Copy delivery URL for approved assets {#copy-delivery-url-approved-assets}

**Prerequisite:** The delivery URL for all approved assets in the repository is available only when you have [!UICONTROL Dynamic Media with OpenAPI capabilities] enabled on your Adobe [!DNL Experience Manager] (AEM) as a Cloud Service instance. Without this capability enabled, the copy delivery URL option does not appear.

A delivery URL provides a direct, ready-to-use link to an approved asset, allowing you to reference and serve that asset—such as an optimized image or rendition—directly within websites, applications, and marketing channels. Because the URL points to the asset served through Dynamic Media, it supports delivery of the approved rendition without exporting or re-uploading the source file.

**Steps to copy the delivery URL for an approved asset within the repository:**

1. Select the asset and click **[!UICONTROL Details]**.

1. Click the Dynamic Media icon available in the right pane.

1. Select **[!UICONTROL Dynamic Media with OpenAPI]** available in the **[!UICONTROL Dynamic Media]** Panel.
![dynamic renditions](/help/assets/assets/dm-with-openapi-non-image-assets.png)

1. Click **[!UICONTROL Copy URL]** to copy the delivery URL of the asset. Use this URL to reference or embed the approved asset directly in your target destination.

   >[!NOTE]
   >
   >The option to copy delivery URL for approved assets is available **only** in **Assets view**.

For information on other renditions that display within the Dynamic Media panel, see [View and download Dynamic Media renditions](/help/assets/renditions.md#view-download-dm-renditions).


**See also**

* [Translate Assets](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in Assets view](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)
