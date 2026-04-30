---
title: Enhance content discovery with AI-generated metadata
description: Learn how to enhance content discovery with AI-generated metadata
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 51d8500e-8a19-40b3-a222-4c7e27eeb667
---
# Enhance content discovery with AI-generated metadata {#ai-smart-tags}

Instead of relying on manual input, AI automatically assigns descriptive tags to digital assets. These AI-generated tags enhance metadata quality, making the assets easier to search, categorize, and recommend. This approach not only improves efficiency by eliminating manual tagging but also ensures consistency and scalability across large volumes of digital content. For example, if the asset is an image, AI can identify objects, scenes, emotions, or even brand logos within it and generate relevant tags such as "sunset," "beach," "vacation," or "smiling." AI-generated content can enhance the search for assets by leveraging both semantic and lexical search techniques. See more [Search Assets](search-assets-view.md). <!--If the asset is a document, AI reads and interprets the text to assign meaningful keywords that summarize its content—such as "climate change," "policy," or "renewable energy.-->

![AI Generated metadata](/help/assets/assets/enhanced-smart-tags.png)

## How to enable AI-generated metadata? {#enable-ai-generated-metadata}

To enable AI-generated metadata:

* Minimum required AEM release version is `20626`.

  
## Using AI-generated metadata {#using-ai-generated-smart-tags}

<!--
[!NOTE]
>
>The enhanced smart tags capability is available only for the newly uploaded assets.
-->

To use the enhanced smart tags feature, execute the following steps:

1. In the [!DNL Experience Manager] interface, go to the desired folder and click **[!UICONTROL Add Assets]**. <!--Alternatively, to update enhanced smart tags in an existing content, click **[!UICONTROL reprocess]**.--> The compatible image file formats are `png`, `jpg`, `jpeg`,`psd`, `tiff`, `gif`, `webp`, `crw`, `cr2`, `3fr`, `nef`, `arw`, and `bmp`.

1. Wait until the newly uploaded asset is processed. Once done, go to asset details.

1. Go to **[!UICONTROL AI-Generated]** tab. If [!DNL Experience Manager] version is incompatible or not updated, then this tab is not visible.  The following fields are there:

    * **[!UICONTROL Generated title]:** The title provides a clear and concise headline that captures the core idea of an uploaded asset, making it easy to understand at a glance. When adding an asset, if you provide a title (in `dc:title`), it will be displayed in the assets browse view. If left blank, an AI-generated title will be assigned automatically.
    * **[!UICONTROL Generated description]:** The description gives a brief yet informative summary of what the asset is about, helping users and search module to quickly grasp its relevance.
    * **[!UICONTROL Generated keywords]:** The keywords are targeted terms that represent the main themes of an asset, aiding in tagging and content filtering.

1. [Optional] You may add additional tags or create your own if you feel any relevant tags are missing. To do this, write your tags in the  **[!UICONTROL Generated keywords]** field and click **[!UICONTROL Save]**.

For information on how to disable AI-generated metadata, see [Disable AI-generated metadata](/help/assets/enhance-content-discovery-with-ai-generated-metadata.md#disable-ai-generated-metadata).
