---
title: Download assets from Content Hub
description: Learn how to download one or more assets and their renditions from the Content Hub portal.
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 96d4ffba-4e3e-4496-9da2-6eb36be8331f
---
# Download assets from [!DNL Content Hub] {#download-assets}

The **[!DNL Content Hub]** lets you download and share your **approved assets** directly from a centralized, brand-governed library. The [!DNL Content Hub] User Interface displays only **approved assets**, ensuring that every file distributed has passed the required review and approval workflow. This governance is what makes the [!DNL Content Hub] a trusted single source of truth for teams that need consistent, compliant content.

These approved assets include **images**, **videos**, **documents**, and other digital content managed within the platform. Because only vetted material is surfaced, users avoid the risk of distributing outdated, unapproved, or off-brand files.

The [!DNL Content Hub] enhances **accessibility** and **adaptability** for effective asset distribution. As a result, marketers, partners, and content teams can quickly locate the right file, retrieve it in the format they need, and reuse it across multiple channels without waiting on manual handoffs.

>[!VIDEO](https://video.tv.adobe.com/v/3433135/?learn=on){transcript=true}

## Downloading assets and renditions

You can download **single or multiple assets** and their available **renditions** using [!DNL Content Hub]. Downloading multiple assets at once streamlines bulk workflows, while renditions give you the same asset in different formats, sizes, or resolutions suited to specific use cases. This flexibility means the correct version of an asset can be pulled for web, print, social, or other channels without needing to re-create or resize files manually.

See the [types of renditions available in [!DNL Content Hub]](#types-of-renditions).

## Download one or more assets and their renditions

To download one or more assets and their renditions, execute the following steps: 

* To download a single asset and its renditions:

   1. Select ![download](/help/assets/assets/download-icon.svg) available on the asset card to preview the asset and its available renditions.
   1. Select the available renditions and click the **[!UICONTROL Download]** option in the dialog box to download the selected renditions as a single **ZIP file**. If the dialog box displays an asset license (for licensed asset), accept the licensing terms and conditions and click **[!UICONTROL Download]**. 

   ![download an asset](/help/assets/assets/download-an-asset-CH-from-asset-card.png)

   Alternatively, click the asset thumbnail and then click ![download](/help/assets/assets/download-icon.svg) to select and view the available renditions on the dialog box before downloading them. You can also copy the delivery URL for the asset renditions if you navigate to Asset properties and click the Download icon. The option to copy the delivery URL is available only if the approval target of the asset is [set to Delivery](/help/assets/approve-assets-content-hub.md#set-approval-target).

* To download multiple assets and their renditions:
   1. Select the assets, click ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]** and review the list of selected assets in the **[!UICONTROL Download assets]** dialog box. Click ![unselect](/help/assets/assets/Close.svg) next to an asset to unselect it from the list. 
   1. Select one or more renditions to download them as a **ZIP file**. Selecting **[!UICONTROL Smart Crop]** and **[!UICONTROL Static Renditions]** downloads all available static and smart crop renditions of each selected asset.
   1. Optional: Unselect **[!UICONTROL Create a separate folder for each asset]** to download the selected assets and their renditions as a flat hierarchy within a single folder in the zip file. This flat structure keeps all files in one location, which simplifies bulk processing. By default, [!DNL Content Hub] downloads the selected assets and their renditions in separate folders within a zip file.
  
      >[!NOTE]
      >
      > * [!DNL Content Hub] saves your selection (**[!UICONTROL Create a separate folder for each asset]**) as your preference and retains it for future downloads.
      > * **[!UICONTROL Create a separate folder for each asset]** option is available only for authenticated [!DNL Content Hub] users. [!DNL Content Hub] enables public users to download assets as individual assets.

   1. Click **[!UICONTROL Download]** to download your selected assets and their renditions. 

![download multiple assets](/help/assets/assets/bulk-asset-download-content-hub.png)

You can continue using [!DNL Content Hub] while the download is in progress, because [!DNL Content Hub] processes downloads in the background. As a result, [!DNL Content Hub] does not interrupt your workflow during the download process.

![download multiple assets](/help/assets/assets/download-assets-notification-ch.png)

If **[!UICONTROL Download assets]** dialog box displays assets licenses, then select each license from the left pane ([!UICONTROL T&C Documents] section) to preview the license and display the selected assets associated with the license in the middle pane of the dialog box. After reviewing each license, select the renditions, click **[!UICONTROL I have read and accepted the terms & conditions mentioned above]** and select **[!UICONTROL Download]** to download them.

![download multiple assets](/help/assets/assets/download-multiple-licensed-assets-CH.png)

>[!NOTE]
>
>* The renditions display only if their visibility is enabled using the [[!UICONTROL Configuration]](/help/assets/configure-content-hub-ui-options.md#renditions-content-hub) User Interface.
>* The users with access to [Dynamic Media with Open API capabilities](/help/assets/dynamic-media-open-apis-overview.md) can view and download dynamic and smart crop renditions.
>* The preview of the license displays only if the asset is approved using [!DNL Assets as a Cloud Service] authoring environment. For more information, see [Manage licensed assets on [!DNL Content Hub]](/help/assets/manage-licensed-assets-on-content-hub.md).

<!--

## Download an asset and its renditions

To download an asset and its renditions, execute the following steps: 

1. Click the asset to view its properties.

1. Click ![download](/help/assets/assets/download-icon.svg) to see the list of available asset renditions in the **[!UICONTROL Download]** panel.

   >[!NOTE]
   >
   >* The renditions display only if their visibility is enabled using the [Configuration](/help/assets/configure-content-hub-ui-options.md#renditions-content-hub) User Interface.
   >* You can download all [static, dynamic, and smart crop renditions](#types-of-renditions) while downloading an asset.

1. Select one or more renditions and click **[!UICONTROL Download]** to download the selected renditions as a zip file. 
While downloading a licensed asset, select **[!UICONTROL I have read and accepted the terms & conditions mentioned above]** before clicking **[!UICONTROL Download]**. You can also click **[!UICONTROL terms & conditions]** to view the asset license. The preview of the license displays only if the asset is approved using Assets as a Cloud Service authoring environment. For more information, see [Manage licensed assets on Content Hub](/help/assets/manage-licensed-assets-on-content-hub.md).

   ![Download single asset renditions](/help/assets/assets/download-single-asset-renditions.png)


If you are downloading a licensed asset, select **[!UICONTROL I have read and accepted the terms & conditions mentioned above]** and then click **[!UICONTROL Download]**. You can also click **[!UICONTROL terms & conditions]** to view the asset license. The preview of the license displays only if the asset is approved using Assets as a Cloud Service authoring environment. For more information, see [Manage licensed assets on Content Hub](/help/assets/manage-licensed-assets-on-content-hub.md).

>[!NOTE]
>
> The users with access to [Dynamic Media with Open API capabilities](/help/assets/dynamic-media-open-apis-overview.md) can view and download dynamic and smart crop renditions.

## Download multiple assets and their renditions {#download-multiple-assets-renditions} 

To download multiple assets and their renditions, execute the following steps: 

1. Select the assets and click ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]**. The [!UICONTROL Download assets] screen displays listing all the selected assets. 
1. Click **[!UICONTROL Download]** to select from the various download options to begin download:

    * **Download [!UICONTROL Originals]**: Select this option to download the selected assets in the original form.
    * **Download [!UICONTROL Static Renditions only]**: Select this option to download all available static renditions of assets except the original assets.
    * **Download [!UICONTROL Originals & Static Renditions]**: Select this option to download both original and static renditions of the selected assets. 

      ![Download multiple renditions](/help/assets/assets/download-multiple-renditions.png)

      >[!NOTE]
      >
      >* The renditions display only if their visibility is enabled using the [Configuration](/help/assets/configure-content-hub-ui-options.md#renditions-content-hub) User Interface.
      >* You can only download [static renditions](#types-of-renditions) while downloading multiple assets.

    If any of the selected asset is a licensed asset, click the license of the asset in left pane to see its preview, which enables you to select **[!UICONTROL I have read and accepted the terms & conditions mentioned above]** and then click **[!UICONTROL Download]**. The preview of the license displays only if the asset is approved using Assets as a Cloud Service authoring environment. For more information, see [Manage licensed assets on Content Hub](/help/assets/manage-licensed-assets-on-content-hub.md).

    ![download-multiple-license](/help/assets/assets/download-multiple-license.png)
-->
    
<!--
1. On the Content Hub homepage, select the asset and click **Download**. The **Download assets** dialog box displays a license or list of licenses associated with the selected assets in the left pane. 
1. Click a license in the left pane to see its PDF in the middle pane and the associated assets with it in the right pane. The license PDF preview is displayed only if the license is approved in your Assets as a Cloud Service environment. [Approve the license PDFs](/help/assets/approve-assets-content-hub.md) of the selected assets to see their previews.
1. Optional: Click ![remove-icon](/help/assets/assets/remove-icon.svg) to remove a license from the dialog box.
1. Select **I have read and accept all the terms and conditions mentioned above.** 
1. Click **Download** to download the selected assets.
-->

<!--
-This dialog box displays the list of licenses associated with the selected assets in the left pane. Select a license to preview its terms and conditions (in pdf format) in the middle pane and the preview of the associated assets to the license in the right. Reviewed licenses are highlighted in light blue.


The dialog box that displays depends on whether the download list includes expired assets or only non-expired assets. <br/>
**Download expired assets dialog box:** This dialog box displays the expired assets' preview along with their expiry date in the left pane. The expired assets' count out of total selected displays in the right pane. Click **Proceed with all assets** to download expired assets with other assets (if present). The Download assets dialog box displays. See the [Download assets dialog box](#Download-asset-dialog-box) to proceed further.
    
    >[!NOTE]
    >
    >[Enable the download option for expired assets](/help/assets/configure-content-hub-ui-options.md#expired-assets-content-hub) to download them. Only expired assets that have enabled downloading are available for download.

   <a id="Download-asset-dialog-box"></a> **Download assets dialog box:** This dialog box displays the list of licenses associated with the selected assets in the left pane. Select a license to preview its terms and conditions (in pdf format) in the middle pane and the associated assets' preview and their count in the right pane. Reviewed licenses are highlighted in light blue.

    >[!NOTE]
    >
    > The **Download Asset dialog box** previews licensing terms and conditions only for approved licenses. [Approve the assets' licenses](/help/assets/approve-assets-content-hub.md) before downloading them to preview their licensing terms in the **Download Asset dialog box**.

1. Click  ![remove-icon](/help/assets/assets/remove-icon.svg) to remove a license from the download dialog box. 

1. Accept the terms and conditions and then click **Download** to download assets associated with the available licenses in the left pane.
-->
<!--![download-multiple-license](/help/assets/assets/download-multiple-license.png)-->

<!--
-
### Download non-licensed Assets {#download-non-licensed-assets}

 To download non-licensed assets, select the assets and click ![download](/help/assets/assets/download-icon.svg) from the top rail.
-->

## Types of renditions {#types-of-renditions} 

**Asset renditions** are alternative representations of an asset's original file, generated to serve the same source content across different platforms, devices, and delivery scenarios. These renditions include thumbnails, optimized versions for web or mobile, watermarked or **DRM (Digital Rights Management)**-protected files, and dynamic elements such as smart crops. They do not need to match the original file type; instead, they represent the same asset across distinct use cases such as web display, mobile responsiveness, print production, and rights-protected distribution.

Learn more about [view and manage renditions in [!DNL Experience Manager Assets]](/help/assets/renditions.md).

[!DNL Experience Manager Assets] supports the following types of renditions:

* [**Static renditions**](/help/assets/renditions.md#static-renditions): Static renditions are pre-created versions of digital assets, typically generated during asset ingestion or modification. They are optimized for specific uses and platforms in advance, which reduces processing at delivery time and ensures consistent output — for example, web thumbnails, mobile-friendly formats for responsive designs, or high-resolution files for printing. This delivers a streamlined and consistent experience.

* [**Dynamic renditions**](/help/assets/renditions.md#dynamic-renditions): Dynamic renditions are real-time, customized versions of assets that perform actions such as resizing images for different device resolutions or cropping to fit various aspect ratios. Because they are generated on demand, dynamic renditions enable personalized and optimized experiences for a wider range of requirements. Dynamic renditions of assets are created in the [!DNL Adobe Experience Manager Assets] author environment. For the steps required to enable dynamic renditions, see [Enable Dynamic renditions](#enable-dynamic-media-renditions).

* [**Smart crop**](/help/assets/dynamic-media/image-profiles.md#creating-image-profiles): Smart crop focuses solely on the essential part of an asset during the cropping process. Dynamic Media smart crop leverages artificial intelligence (AI) powered by Adobe AI to track the point of interest, so that assets look their best on all screen sizes, because the point of interest remains centered regardless of aspect ratio. [!DNL Adobe Experience Manager] smart crop displays the width and height of an asset's renditions along with the title. See more at [using Smart Crop with AEM Assets Dynamic Media](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/smart-crop-feature-video-use).

   Smart Crop renditions display and are available for download only if you have access to [Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md). Smart Crop renditions are available only for image assets.

  ![Renditions types](/help/assets/assets/renditions-types.png)

  >[!NOTE]
  > 
  > The Download panel displays only custom static renditions. The default `cq5dam.*` thumbnails do not display in [!DNL Content Hub].

### Enable Dynamic renditions {#enable-dynamic-media-renditions}

Dynamic renditions enable public delivery of approved image assets through Dynamic Media. To enable Dynamic renditions in [!DNL Content Hub], complete the following steps:

1. Ensure that you have access to [Dynamic Media with OpenAPI (Open Application Programming Interface) capabilities](/help/assets/dynamic-media-open-apis-overview.md).

   Once you have access to Dynamic Media with OpenAPI capabilities, all assets marked as `Approved` become available for public delivery using Dynamic Media. This makes approval status the key control that determines which assets are exposed publicly.

1. Set the [approval target of the asset](/help/assets/approve-assets-content-hub.md#set-approval-target) to [!DNL Content Hub] to approve assets only for [!DNL Content Hub]. This ensures those assets are approved exclusively for [!DNL Content Hub] delivery rather than across all channels.

1. Enable the **[!UICONTROL Enable availability of renditions]** toggle available in the **[!UICONTROL Renditions]** tab of the [Configuration](/help/assets/configure-content-hub-ui-options.md#access-configuration-options-content-hub) User Interface (UI). This toggle activates rendition availability for the configured assets.

1. Re-save the existing image presets to make them available on [!DNL Content Hub]. This step is required only if you have newly onboarded to Dynamic Media with OpenAPI, because existing presets must be re-saved before they are recognized by the new capability.

   To re-save the existing image presets, navigate to the Admin view and select **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Image Presets]**. Select a preset, click **[!UICONTROL Edit]**, and then click **[!UICONTROL Save]**.

   >[!NOTE]
   >
   > Dynamic renditions are available only for image assets. This limitation applies because renditions are generated exclusively for image formats and are not produced for other asset types.

## Frequently asked questions {#faqs-download-assets-content-hub}

### How do I download a single asset or multiple assets from AEM Assets [!DNL Content Hub]?

**[!DNL Adobe Experience Manager] (AEM) Assets [!DNL Content Hub]** supports downloading both single assets and multiple assets directly from the asset grid. The method depends on how many assets you need and whether your administrator has enabled downloads for your organization.

**Download a Single Asset**

1. Locate the asset in the [!DNL Content Hub] grid.
2. Click the **download icon** on the asset card.
3. The asset downloads in its **original rendition** if downloads are enabled by your administrator.

**Download Multiple Assets**

1. Select the assets you want by clicking each asset card.
2. Click **Download** in the action bar.
3. [!DNL Content Hub] begins downloading the selected assets in their **original rendition**, provided downloads are enabled by your administrator.

**Selecting Renditions Before Download**

If asset **renditions** are available, you can select specific renditions before downloading rather than downloading only the original file. A rendition is an alternate version of an asset—such as a resized, reformatted, or web-optimized copy—generated to suit different use cases. This lets you retrieve the exact file variant needed for a given channel or output.

Download availability is controlled by your administrator. Because downloads must be enabled at the account or organization level, the **download icon** and the **Download** action appear only when your administrator has granted download permissions.

### Is there any configuration managed by administrator in AEM Assets [!DNL Content Hub] to allow Users to download original assets or enable availability of renditions?

Yes. Administrators control both original asset downloads and rendition availability directly through the **Renditions** tab of the Configuration UI in **[!DNL Adobe Experience Manager] (AEM) Assets [!DNL Content Hub]**. These settings are managed centrally, so administrators—not individual users—determine what content is available for download across the [!DNL Content Hub].

#### How Administrators Manage Downloads and Renditions

Administrators enable or disable the following two toggles, both located in the **Renditions** tab on the **Configuration UI**:

- **Enable availability of renditions** — Controls whether alternate versions of an asset (renditions) are made available to users. Renditions are variations of an original asset, such as resized, cropped, or reformatted versions generated for specific use cases. Enabling this toggle makes these prepared variations accessible for download.
- **Allow download of original assets** — Controls whether users can download the full-resolution, unmodified source file. When this toggle is enabled, users can retrieve the original asset; when disabled, download of the source file is restricted.

#### Why These Controls Matter

Because these toggles reside in the administrator-managed Configuration UI, they give organizations centralized governance over asset distribution in **AEM Assets [!DNL Content Hub]**. This allows administrators to decide, for example, whether end users receive only web-ready renditions or gain access to high-resolution originals. As a result, teams can enforce consistent asset-usage policies, protect source files where appropriate, and still make the right variations available to the users who need them.

In summary, administrators use the **Enable availability of renditions** and **Allow download of original assets** toggles on the **Renditions** tab of the **Configuration UI** to manage exactly which downloads and renditions are available to users in **[!DNL Adobe Experience Manager] (AEM) Assets [!DNL Content Hub]**.

### What are asset renditions, and what types are available in AEM Assets [!DNL Content Hub]?

**Asset renditions** in **[!DNL Adobe Experience Manager] (AEM) Assets [!DNL Content Hub]** are alternative representations of an original asset file, each generated and tailored to a specific delivery context or use case. Rather than distributing a single master file everywhere, [!DNL Content Hub] produces purpose-built versions so that the right format, size, and quality reach the right channel — a common practice in modern digital asset management (DAM), where the same source image or file must serve web pages, mobile apps, print production, and internal previews.

#### Types of Asset Renditions

AEM Assets [!DNL Content Hub] supports the following rendition types:

- **Static renditions** — pre-generated representations of the asset, including **thumbnails**, **web-optimized** and **mobile-optimized versions**, and **high-resolution files for print**.
- **Custom static renditions** — additional pre-generated variants configured to meet specialized formatting or channel requirements beyond the standard set.
- **Dynamic renditions** — representations produced on demand, including **Smart Crop versions** that automatically adapt framing for different aspect ratios and display contexts.

#### Static vs. Dynamic Renditions: The Key Distinction

The two families differ fundamentally in **when and how they are created**:

- **Static renditions are pre-generated** and stored ahead of time, making them immediately available for fast, repeatable delivery.
- **Dynamic renditions are created in real time, based on the request**, generating the exact representation needed at the moment it is called.

This distinction matters in practice: because static renditions are prepared in advance, they support consistent, low-latency reuse, while dynamic renditions provide flexibility by producing tailored outputs — such as automatically cropped imagery — only when required. Together, these rendition types allow teams to distribute a single approved asset across thumbnails, web, mobile, and print channels without manually recreating each version.

### How does Smart Crop work with assets in AEM Assets [!DNL Content Hub]?

**Smart Crop** in [!DNL Adobe Experience Manager] (AEM) Assets [!DNL Content Hub] is an **AI-powered feature** that automatically identifies the most important part of an image and intelligently crops around it. It ensures that a single source image renders well across different screens, aspect ratios, and delivery formats without requiring manual editing for each output.

#### How Smart Crop Works

Smart Crop applies **artificial intelligence** to analyze an image and detect its primary focal point—the subject or region most likely to carry visual meaning. When the image must be reframed to a different aspect ratio or dimension, the feature preserves that focal region rather than cropping arbitrarily from the center or edges. This keeps the most relevant content in frame across a range of target sizes.

The result is a set of **Smart Crop renditions**: variations of the same source asset that are automatically cropped and adapted for different placements. Because the reframing follows the detected subject, visuals remain consistent and on-message regardless of where they appear.

#### Availability and Requirements

Smart Crop renditions are available for image assets when your organization has **dynamic media capabilities** enabled. Dynamic media capabilities provide the underlying rendition and delivery framework that generates and serves adaptive image variations, and Smart Crop builds on this foundation to produce its intelligently cropped outputs. Without dynamic media enabled, Smart Crop renditions are not generated.

#### Practical Applications

Smart Crop is designed to support a range of content delivery scenarios, including:

- **Responsive layouts** — serving appropriately framed images across desktop, tablet, and mobile screens.
- **Multiple aspect ratios** — adapting a single asset for wide banners, square thumbnails, and vertical formats.
- **Consistent branding** — keeping the intended subject in view across every channel and placement.
- **Reduced manual effort** — eliminating the need to hand-crop each variation, since the AI reframes automatically.

By combining AI-based focal-point detection with dynamic media delivery, Smart Crop in AEM Assets [!DNL Content Hub] streamlines the creation of screen- and format-optimized visuals from a single source image.

### How do I enable Dynamic renditions in AEM Assets [!DNL Content Hub]?

Enabling Dynamic renditions in **[!DNL Adobe Experience Manager] (AEM) Assets [!DNL Content Hub]** requires configuring Dynamic Media with OpenAPI capabilities and completing a short setup sequence. Once configured, approved assets become available for public delivery as optimized, on-demand image variations suitable for distribution across channels.

**Note: Dynamic renditions are supported only for image assets.** Non-image asset types are not eligible for this delivery capability.

#### Prerequisites

- **Dynamic Media with OpenAPI** capabilities must be enabled. This is the delivery mechanism that makes approved assets available for public delivery. Only approved assets are eligible.

#### Setup Steps

1. **Confirm Dynamic Media with OpenAPI is enabled.** This ensures approved assets can be delivered publicly as Dynamic renditions.
2. **Set the asset approval target to [!DNL Content Hub].** This directs approved assets into the **[!DNL Content Hub]** delivery workflow.
3. **Enable rendition availability in the Configuration user interface (UI).** Navigate to the **Renditions tab** and turn on **Enable availability of renditions**.
4. **Re-save existing image presets if newly onboarded.** If you are newly onboarded to Dynamic Media with OpenAPI, go to **Admin view > Tools > Assets > Image Presets**, then select **Edit > Save** for each preset. Re-saving regenerates the presets against the OpenAPI delivery pipeline, ensuring existing renditions are correctly made available through the new delivery capability.

#### Supported Asset Types

Dynamic renditions apply exclusively to image assets. Confirm that the assets you intend to publish through [!DNL Content Hub] are images before enabling this configuration.

### How do I download asset renditions in AEM Assets [!DNL Content Hub]?

In **[!DNL Adobe Experience Manager] (AEM) Assets [!DNL Content Hub]**, you download asset renditions by selecting an asset and running the download action. **Renditions** are the alternate versions of an asset—such as different sizes, formats, or resolutions—generated from the original file. When your administrator enables renditions, [!DNL Content Hub] lets you choose exactly which renditions to download, either individually or in bulk as a single **ZIP file**.

#### Download renditions for a single asset

1. Select the asset you want to download.
2. Click the **download action**.
3. If the administrator has enabled renditions, a dialog opens that lets you select which renditions to download. You can choose **all available renditions** or specific ones, such as **static or dynamic renditions**.
4. For **licensed assets**, accept the licensing terms before downloading. This confirmation step ensures the asset is used in compliance with its license conditions.

#### Download renditions for multiple assets

1. Select the assets you want to download.
2. Choose the renditions to include for the selected assets.
3. Download the selected assets and their renditions together as a single **ZIP file**.

Downloading multiple assets as a **ZIP file** consolidates all selected files and their chosen renditions into one package, which streamlines bulk retrieval and distribution.

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
