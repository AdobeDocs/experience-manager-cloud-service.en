---
title: Upload your brand approved assets to [!DNL Content Hub]
description: Learn how to upload your brand approved assets to Content Hub
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: f1be7cfc-1803-4c17-bb58-947104aa883c
---
# Upload brand approved assets to [!DNL Content Hub] {#upload-brand-approved-assets-content-hub}

>[!CONTEXTUALHELP]
>id="upload_assets_content_hub"
>title="Upload brand approved assets to [!DNL Content Hub]"
>abstract="Add approved assets to [!DNL Content Hub] either from local file system or import assets from OneDrive or Dropbox data sources. All assets display at the top-level in [!DNL Content Hub] irrespective of the folder structure to enhance search capabilities."

[Content Hub users with rights to add assets](/help/assets/deploy-content-hub.md#onboard-content-hub-users-add-assets) can add assets to the [!DNL Content Hub] either from local file system or import assets from OneDrive or Dropbox data sources. All assets display at the top-level in [!DNL Content Hub] irrespective of the folder structure available on your local file system or OneDrive and Dropbox data sources. This flattened view removes navigation barriers and, as a result, enhances search capabilities across your entire asset library, because assets remain discoverable regardless of how they were originally organized in the source location.

>[!VIDEO](https://video.tv.adobe.com/v/3432980/?learn=on){transcript=true}

The assets marked as **`Approved`** in Assets as a Cloud Service are automatically available in [!DNL Content Hub]. For more information, see [Approve assets for [!DNL Content Hub]](/help/assets/approve-assets-content-hub.md).

To further enhance asset search, [!DNL Content Hub] allows you to:

* **Define key details** relevant to your asset upload, such as campaign name, keywords, channels, and so on. Adding this metadata at upload time ensures assets can be retrieved later through targeted, attribute-based searches.

* **Automatically generate more properties** for each asset upon successful upload, such as file size, format, resolution, and other technical properties. These auto-generated attributes support precise filtering and comparison without any manual entry.

* **Use the artificial intelligence (AI) provided by [Adobe AI](https://business.adobe.com/ai/adobe-genai.html)** to automatically apply relevant tags to all your uploaded assets. The AI analyzes each asset and assigns descriptive tags without requiring manual tagging effort. These tags, named **Smart Tags**, are AI-generated descriptors that increase the content velocity of your projects by helping you find relevant assets quickly. Because Smart Tags surface assets that match a search intent even when exact keywords were not manually entered, they accelerate asset discovery and reduce time spent searching.

![Upload brand approved assets](assets/upload-brand-approved-assets.png)

Ensure that you only upload your [brand approved assets to the [!DNL Content Hub]](/help/assets/approve-assets.md).

## Prerequisites {#prerequisites-add-assets}

Access to add assets in [!DNL Content Hub] is controlled by user permissions. Only [Content Hub users with rights to add assets](/help/assets/deploy-content-hub.md#onboard-content-hub-users-add-assets) are authorized to upload assets to [!DNL Content Hub]. Because uploading is a permission-gated action, a user must first be granted the appropriate add-asset rights before they can contribute assets to the library.

This permission-based requirement ensures that only authorized contributors can introduce new assets, which helps maintain content governance and control over the [!DNL Content Hub] asset library. If a user does not have these rights, the option to upload assets is not available to them. To grant a user the ability to add assets, follow the process for onboarding [!DNL Content Hub] users with add-asset rights described in the linked documentation above.

## Add assets to [!DNL Content Hub] from local file system {#add-assets-local-file-system}

<!--You can define multiple Campaign names for your upload. While you are typing a name, either click anywhere else within the dialog box or press the `,` (Comma) key to register the name.-->

To upload approved assets to [!DNL Content Hub] from your local file system, complete the following steps. This workflow lets you select files, group them under a campaign, tag them for discoverability, and publish them to [!DNL Content Hub] in a single guided process:

1. Click **[!UICONTROL Add Assets]** to view the **[!UICONTROL Add your approved assets]** dialog box that enables you to create an upload.

1. In the **[!UICONTROL Drag files or folders here]** section available in the right pane, you can either drag the assets from the local file system or click **[!UICONTROL Browse]** to manually select files or folders available on the local file system. This list of files that are part of your upload are available as a list. 

   
   You can also preview selected images using the thumbnails and click the X icon to remove any particular image from the list. The X icon displays only when you hover your mouse over the image name or size. You can also click **[!UICONTROL Remove all]** to delete all items from your upload list.

   ![Upload assets to [!DNL Content Hub]](assets/upload-assets-content-hub.png)

   To finish the upload process and enable the **[!UICONTROL Upload button]**, you must group your assets under a Campaign name. This grouping is mandatory because it organizes related assets together, ensuring that every uploaded item belongs to an identifiable collection before publishing proceeds.
   

1. Define the name for your upload using the **[!UICONTROL Campaign name]** field. You can use an existing name or create a new one. The [!DNL Content Hub] suggests matching options as you type the name, helping you reuse an existing campaign for consistency or establish a new one. As a best practice, Adobe recommends completing the remaining fields as well, because doing so creates an enhanced search experience for your uploaded assets.

1. Similarly, define values for the **[!UICONTROL Keywords]**, **[!UICONTROL Channels]**, **[!UICONTROL Timeframe]**, and **[!UICONTROL Region]** fields. Tagging and grouping assets by keywords, channels, and location makes approved company content easier to discover. As a result, everyone who uses these assets can locate them quickly and keep the library organized.

1. Click **[!UICONTROL Upload]** to upload assets to the [!DNL Content Hub]. [!UICONTROL Review details] confirmation box appears. Click [!UICONTROL Continue].

1. Assets begin uploading immediately. Click [!UICONTROL New Upload] to restart the upload procedure. Click [!UICONTROL Done] to complete uploading.

Administrators can also configure the mandatory and optional fields that display while uploading assets, such as Campaign name, Keywords, Channels, and so on. For more information, see [Configure the [!DNL Content Hub] user interface](configure-content-hub-ui-options.md#configure-upload-options-content-hub).

## Manage assets uploaded using [!DNL Content Hub] {#manage-assets-uploaded-using-content-hub}

[Content Hub users with rights to add assets](/help/assets/deploy-content-hub.md#onboard-content-hub-users-add-assets) can [add assets to the [!DNL Content Hub]](/help/assets/upload-brand-approved-assets.md) in two ways: directly from the local file system, or by importing assets from OneDrive or Dropbox data sources. All uploaded assets display at the **top level in [!DNL Content Hub]**, regardless of the folder structure that exists on your local file system, OneDrive, or Dropbox data sources. [!DNL Content Hub] flattens this hierarchy to enhance search capabilities, because a single top-level listing lets you locate any asset quickly without navigating the original folder path.

### Asset display behavior based on the Auto-approval toggle

Whether an uploaded asset appears immediately in [!DNL Content Hub] is determined by the [Auto-approval toggle](/help/assets/configure-content-hub-ui-options.md#configure-import-options-content-hub). The two possible states produce distinct outcomes:

* **[!UICONTROL Auto-approval] enabled:** The assets you upload using [!DNL Content Hub] become **automatically available** in [!DNL Content Hub] with no additional action required.

* **[!UICONTROL Auto-approval] disabled:** The assets you upload using [!DNL Content Hub] do **not** appear automatically in [!DNL Content Hub]. Instead, these assets are placed in the **`hydrated-assets`** folder of your Assets as a Cloud Service environment and remain hidden until they are approved.

To make assets visible when the **[!UICONTROL Auto-approval]** toggle is disabled, complete the following steps:

![Content Hub approval process](/help/assets/assets/content-hub-approval.png)

1. Navigate to the **`hydrated-assets`** folder in your Assets as a Cloud Service environment.
2. [Bulk edit](#bulk-approve-assets-content-hub) the status of the pending assets and set it to **`Approved`**.

As a result, the approved assets display in [!DNL Content Hub]. This approval workflow gives teams control over which uploaded assets become discoverable, ensuring that only reviewed, brand-approved content surfaces to end users.

## Frequently asked questions {#faqs-content-hub-upload-assets}

### What types of assets can I upload to AEM Assets [!DNL Content Hub] and from where? {#asset-types-upload-to-content-hub}

Users of **Adobe Experience Manager (AEM) Assets [!DNL Content Hub]** who have been granted rights to add assets can upload **brand approved assets** directly from a user's **local file system**. This governs both what can be uploaded and where uploads originate: the assets must be **brand approved**, and the source location is the local file system of the user performing the upload.

**Who can upload:** Only [!DNL Content Hub] users with explicit rights to add assets are permitted to upload. This permission-based control ensures that only sanctioned, brand approved content enters the [!DNL Content Hub] library, preserving brand consistency across distributed assets.

**Where uploads come from:** Assets are added directly from a user's **local file system**, allowing contributors to publish approved files without an intermediary repository.

**How uploaded assets are organized:** All uploaded assets are displayed at the **top-level** in [!DNL Content Hub], regardless of their original folder structure. Because the original nested folder hierarchy is flattened on upload, every asset surfaces at the top level, which enhances search capabilities and makes uploaded content easier to locate. As a result, users do not need to navigate through original directory paths to find an asset — flattening the structure improves discoverability and streamlines search across the entire [!DNL Content Hub] library.

### How does AEM Assets [!DNL Content Hub] enhance asset search and organization? {#search-content-hub}

**Adobe Experience Manager (AEM) Assets [!DNL Content Hub] enhances asset search and organization through structured metadata and AI-powered tagging.** [!DNL Content Hub] lets users define key details for each upload, so that every asset is searchable by the attributes teams actually use to locate it.

When uploading, users can specify descriptive metadata including:

- **Campaign name** — links the asset to a specific initiative
- **Keywords** — supports term-based search and discovery
- **Channels** — identifies where the asset is intended for use
- **Timeframe** — organizes assets by their relevant period
- **Region** — narrows results by geographic scope

In addition to this user-defined metadata, [!DNL Content Hub] automatically generates technical properties for each asset, such as **file size, format, and resolution**. Because these attributes are captured without manual entry, assets remain consistently searchable across large libraries.

[!DNL Content Hub] also uses Adobe artificial intelligence (AI) to apply **Smart Tags** to uploaded assets. As a result, relevant content surfaces faster: the combination of user-defined details, auto-generated properties, and AI-driven Smart Tags means users can find the right asset quickly without manually classifying every file. This is especially valuable in large-scale digital asset management, where structured metadata and intelligent tagging directly reduce the time spent locating approved, on-brand content.

### How to upload assets from my local file system to AEM Assets [!DNL Content Hub]? {#upload-assets-content-hub}

To upload assets from your local file system to **Adobe Experience Manager (AEM) Assets [!DNL Content Hub]**, use the built-in upload dialog and organize your files under a campaign before confirming. Follow these steps:

1. Click **Add Assets** to open the upload dialog.
2. Drag and drop files or folders directly into the dialog, or manually browse your local file system to select them.
3. Group your assets under a **campaign name**. Grouping assets under a campaign is required because it organizes uploaded content into a logical structure, making assets easier to locate, manage, and retrieve later.
4. Fill in the additional metadata fields for better organization. Recommended fields include **keywords**, **channels**, **timeframe**, and **region**, all of which improve discoverability and searchability of the uploaded assets.
5. Click **Upload**, review the details you have entered, and confirm to start uploading.

Once you confirm, the upload begins and the assets become available in AEM Assets [!DNL Content Hub], organized under the campaign name you assigned.

### How does the asset approval process work in AEM Assets [!DNL Content Hub]? {#asset-approval-content-hub}

The asset approval process in **Adobe Experience Manager (AEM) Assets [!DNL Content Hub]** is controlled entirely by the **Auto-approval toggle**, which determines whether uploaded assets become visible immediately or require manual review before publication. This toggle governs a single, clear branch in the workflow: enabled means instant availability, while disabled means assets must be manually approved.

**When Auto-approval is enabled**

When the **Auto-approval toggle** is enabled, assets uploaded through Adobe Experience Manager (AEM) Assets [!DNL Content Hub] are **automatically available**. No additional review step is required, and the assets appear in [!DNL Content Hub] as soon as the upload completes. This streamlined path is well suited to teams that trust their contributors and prioritize rapid content turnaround.

**When Auto-approval is disabled**

Unlike the enabled state, when the **Auto-approval toggle** is disabled, uploaded assets are not published automatically. Instead, they are placed in the **hydrated-assets** folder in Assets as a Cloud Service and held there pending manual approval. As a result, the assets remain hidden from [!DNL Content Hub] until their status is explicitly changed. This ensures that only reviewed and approved assets become visible to end users, adding a governance checkpoint to the workflow.

To publish assets held in the **hydrated-assets** folder, an administrator must complete the following steps:

1. Locate the uploaded assets in the **hydrated-assets** folder within Assets as a Cloud Service.
2. Select the assets that require publication and perform a **bulk edit** on their status.
3. Set the status of the selected assets to **Approved**.

Once the status is changed to **Approved**, the assets display in [!DNL Content Hub] and become available to users. Because this manual step is required, disabling Auto-approval effectively gives administrators direct control over which uploaded assets reach the [!DNL Content Hub], making it the preferred configuration for organizations that need an approval or moderation stage before distribution.

### Can I configure the fields that are mandatory or optional while uploading assets to AEM Assets [!DNL Content Hub]? {#available-fields-while-uploading-assets-to-content-hub}

Yes. Administrators can configure which upload fields are **mandatory or optional** in **Adobe Experience Manager (AEM) Assets [!DNL Content Hub]**. Using the **Configuration User Interface**, administrators define the metadata fields that contributors must complete—or may skip—when uploading assets to [!DNL Content Hub].

**How the configuration works**

Administrators use the **Configuration User Interface** to set the field requirements applied during the asset upload workflow. Rather than accepting a fixed default schema, administrators control the metadata prompts that appear to users at upload time. This determines the information captured for every asset entering the [!DNL Content Hub] library.

Through this interface, administrators can:

- Designate specific fields as **mandatory**, requiring completion before an asset upload can be finalized.
- Designate other fields as **optional**, giving contributors flexibility while still allowing enrichment of asset metadata.
- Tailor the upload experience so that the fields presented align with the organization's metadata standards.

**Why field configuration matters**

Governing which fields are required versus optional ensures assets are uploaded with consistent, complete metadata. This supports reliable search, filtering, and discoverability across the [!DNL Content Hub] library, because well-structured metadata is what makes assets findable and reusable at scale. By making critical fields mandatory, administrators enforce data quality at the point of upload, while optional fields reduce friction for contributors who do not need to supply every attribute. The result is a balance between metadata completeness and an efficient, streamlined upload process for the teams using AEM Assets [!DNL Content Hub].

### What should I do if my uploaded assets do not display automatically in AEM Assets [!DNL Content Hub]? {#assets-do-not-display-in-content-hub}

**If uploaded assets do not display automatically in Adobe Experience Manager (AEM) Assets [!DNL Content Hub], the Auto-approval toggle is disabled.** [!DNL Content Hub] surfaces only assets with an **Approved** status, so assets that are still pending approval remain hidden until their status is updated.

**Root cause**

The affected assets are located in the **hydrated-assets** folder of your **Assets as a Cloud Service (AaCS)** environment. Because the **Auto-approval** toggle is turned off, newly uploaded assets are not automatically promoted to **Approved**, and [!DNL Content Hub] does not render assets that lack the **Approved** status.

**Resolution steps**

1. Navigate to the **hydrated-assets** folder in your Assets as a Cloud Service environment.
2. Select the assets that are not appearing in [!DNL Content Hub].
3. Bulk edit the selected assets and set their status to **Approved**.
4. Confirm the change so the newly approved assets appear in AEM Assets [!DNL Content Hub].

Enabling the **Auto-approval** toggle prevents this issue from recurring, because future uploads are then promoted to **Approved** automatically and become immediately visible in [!DNL Content Hub] without manual status updates.

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
