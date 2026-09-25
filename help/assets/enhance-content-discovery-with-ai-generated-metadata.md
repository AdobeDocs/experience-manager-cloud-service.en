---
title: Enhance content discovery with AI-Generated metadata in Admin View
description: Learn how to enhance content discovery with AI-Generated metadata in Admin View
feature: Smart Tags,Tagging
role: Admin,User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: c76379e3-6bdf-4dba-9d2b-f2120f85052f
---
# Enhancing content discovery with AI-Generated metadata {#ai-smart-tags}

| UIs | Article link |
| -------- | ---------------------------- |
| Assets View  |    [Click here](/help/assets/ai-generated-metadata-assets-view.md)                  |
| Admin View     | This article         |

**AI-generated metadata** automatically assigns descriptive tags to digital assets, replacing manual input with automated classification. These **AI-generated tags** enhance metadata quality, making the assets easier to search, categorize, and recommend. Because tags are applied automatically rather than by hand, this approach improves efficiency, ensures consistent labeling, and scales reliably across extensive libraries of digital content.

## How AI-generated tagging works

For image assets, AI analyzes the visual content and detects recognizable elements, then generates relevant descriptive tags automatically. AI can identify:

- **Objects** within the frame
- **Scenes** and settings
- **Emotions** expressed in the image
- **Brand logos** and visual identifiers

From these detections, the system produces relevant tags such as **"sunset," "beach," "vacation,"** or **"smiling."** This automated recognition removes the need for a person to inspect and label each file individually, which is why the method remains reliable even as content volumes grow.

## Key benefits

AI-generated tagging enhances asset discovery in several ways:

<!--If the asset is a document, AI reads and interprets the text to assign meaningful keywords that summarize its content—such as "climate change," "policy," or "renewable energy.-->

![Enhanced smart tags](assets/enhanced-smart-tags1.png)

- **Faster search** — descriptive tags surface relevant assets quickly without manual keywording.
- **Reliable categorization** — assets are grouped consistently according to their detected content.
- **Smarter recommendations** — richer metadata enables more relevant asset suggestions.
- **Scalable consistency** — the same tagging standards apply automatically across every asset in the library.

## Semantic and lexical search

AI-generated tags enhance asset search by leveraging both **semantic search** and **lexical search** techniques. Lexical search matches the exact keywords and tag text, while semantic search interprets the meaning and intent behind a query to return conceptually related results. Combining both approaches ensures users find the right assets whether they search by precise terms or by broader descriptive concepts. See more [Search Assets](search-assets.md).

## How to enable AI-generated metadata? {#enable-ai-generated-metadata}

AI-generated metadata automatically produces descriptive information—such as titles, descriptions, and tags—for assets, reducing manual tagging effort and improving asset discoverability, searchability, and content management efficiency.

**Prerequisites**

Before enabling AI-generated metadata, confirm that your environment meets the required baseline:

* The minimum required **Adobe [!DNL Experience Manager] (AEM)** release version is **`20626`**.

This version requirement ensures the AI-generated metadata capability and its underlying services are available and supported in your environment. Attempting to enable the feature on an earlier release will not surface the option, because the necessary functionality is introduced at release **`20626`** and later.

**Enabling the feature**

To enable AI-generated metadata once the prerequisite is met, activate the AI-generated metadata capability from your AEM configuration for assets, and confirm the feature is turned on. As general guidance, feature enablement of this type is typically managed by an administrator with the appropriate permissions, after which newly processed assets can benefit from automatically generated metadata.

## Configure AI-generated titles {#configure-ai-generated-titles}

Adobe [!DNL Experience Manager] (AEM) enables you to configure how asset titles display in **Card view** or **List view** on the **Asset Browse** page. You can choose to display the asset title defined by you, an **AI-generated title**, or use an AI-generated title only when no existing title is defined for the asset. This configuration helps maintain consistent, descriptive labeling across the asset library, particularly for assets that lack manually entered titles.

To configure AI-generated titles:

1. Navigate to **[!UICONTROL Tools > Assets > Assets Configurations > Smart Tag Enhancement Configuration]**.

2. Select one of the following options:

   * **Display DC (Dublin Core) Title (Default)**: Specify the title in the **[!UICONTROL Title]** field available in asset properties to display it in Card view or List view. If the asset title is not defined, AEM Assets displays the **file name** as a fallback. Use this option when you want author-defined titles to take precedence.

   * **Display AI-Generated Title**: Displays the **AI-generated title** and ignores the title specified in asset properties. This ensures assets show a descriptive, machine-generated label even when properties are inconsistent. If an AI-generated title is not available for an asset, AEM Assets displays the default asset title available in its properties, so a title is always shown. Use this option when you want AI-generated titles to take precedence across the asset library.

   * **Display AI-Generated Title only if DC Title does not exist**: AEM Assets displays the **AI-generated title only when an asset title is not defined** for that asset. This preserves any manually entered titles while automatically filling gaps with AI-generated titles, combining author control with automated coverage.

     ![Configure AI-generated titles](assets/configure-title-ai-generated.png)

## Using AI-Generated metadata {#using-ai-generated-smart-tags}

<!--
[!NOTE]
>
>The enhanced smart tags capability is available only for the newly uploaded assets.
-->

<!--Alternatively, to update enhanced smart tags in an existing content, click **[!UICONTROL reprocess]**.-->

The Artificial Intelligence (AI)–generated metadata capability in [!DNL Experience Manager] automatically produces a title, description, and keywords for uploaded assets, reducing manual tagging effort and improving asset discoverability. To use the enhanced smart tags feature, execute the following steps:

1. In the [!DNL Experience Manager] interface, go to the desired folder and click **[!UICONTROL Add Assets]**. The **compatible image file formats** are `png`, `jpg`, `jpeg`, `psd`, `tiff`, `gif`, `webp`, `crw`, `cr2`, `3fr`, `nef`, `arw`, and `bmp`.

1. Wait until the newly uploaded asset is processed. Once processing completes, go to asset properties.

1. Go to the **[!UICONTROL AI-Generated]** tab. If the [!DNL Experience Manager] version is incompatible or not updated, this tab does not appear. The following fields are available:

    * **[!UICONTROL Generated title]:** The title provides a clear and concise headline that captures the core idea of an uploaded asset, making it easy to understand at a glance. When adding an asset, if you provide a title (in `dc:title`), [!DNL Experience Manager] displays it in the assets browse view. If the title field is left blank, an AI-generated title is assigned automatically. This ensures every asset retains a searchable, descriptive headline even when no manual title is entered.
    * **[!UICONTROL Generated description]:** The description gives a brief yet informative summary of what the asset is about, helping users and the search module to quickly grasp its relevance. This improves how efficiently the asset surfaces in search results and browsing.
    * **[!UICONTROL Generated keywords]:** The keywords are targeted terms that represent the main themes of an asset, aiding in tagging and content filtering. Consistent keywords make assets easier to locate, group, and reuse across projects.

1. [Optional] You may add additional tags or create your own if any relevant tags are missing. To do this, write your tags in the **[!UICONTROL Generated keywords]** field and click **[!UICONTROL Save]**.

## Disable AI-generated metadata {#disable-ai-generated-metadata}

**AI-generated metadata** in **Adobe [!DNL Experience Manager] (AEM) as a Cloud Service** can be disabled at two levels: across the entire **AEM as a Cloud Service environment** or selectively at the **folder level**. This gives administrators flexibility to turn off automated metadata generation globally or for specific asset collections.

To disable **AI-generated metadata** for the AEM as a Cloud Service environment:

1. Navigate to **[!UICONTROL Tools > Assets > Assets Configurations > Smart Tag Enhancement Configuration]**.

1. Select **[!UICONTROL Disable Smart Tag Enhancements]**.

1. Click **[!UICONTROL Save]**.

As a result, **AI-generated metadata is disabled for all new assets or folders** uploaded by administrators to AEM Assets after the configuration is saved. Existing assets or folders that already have AI-generated metadata fields continue to display these fields, because disabling the **Smart Tag Enhancement Configuration** applies only prospectively and does not remove or alter metadata that was previously generated. To clear those retained fields, administrators must manage the existing metadata directly on each affected asset or folder.

### Disable AI-generated metadata for folders {#disable-ai-generated-metadata-folder-level}

Disabling AI-generated metadata at a folder-level turns off automatic **Smart Tags** and AI-driven image enhancements for every asset within the selected folder. AI-generated metadata refers to tags, labels, and descriptive attributes that the system produces automatically for images, and disabling it at the folder level applies uniformly to all images stored in that folder.

To disable AI-generated metadata at a folder-level:

1. Select the folder and click **[!UICONTROL Properties]**.

1. Select the **[!UICONTROL Asset Processing]** tab.

1. In the **[!UICONTROL Smart Tags Enhancements for images]** section, select **[!UICONTROL Disable]** from the drop-down menu. This ensures that new and reprocessed images in the folder are not assigned AI-generated tags, giving you full manual control over the metadata applied to those assets.

1. Click **[!UICONTROL Save & Close]** to apply the change and disable AI-generated metadata for the selected folder. The setting takes effect for the folder and its images once saved.


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
