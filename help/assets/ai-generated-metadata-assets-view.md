---
title: Enhance content discovery with AI-generated metadata
description: Learn how to enhance content discovery with AI-generated metadata
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 51d8500e-8a19-40b3-a222-4c7e27eeb667
---
# Enhance content discovery with AI-generated metadata {#ai-smart-tags}

**AI-generated tags automatically enrich digital assets with descriptive metadata, making assets easier to search, categorize, and recommend.** Instead of relying on manual input, **Artificial Intelligence (AI)** automatically assigns descriptive tags to digital assets, removing the labor and inconsistency of hand-tagging large libraries.

## How AI-generated tags work

AI analyzes the content of each asset and generates relevant tags without human intervention. For an image, AI can detect a range of visual elements and produce corresponding tags:

- **Objects** within the frame
- **Scenes** and settings
- **Emotions** conveyed by subjects
- **Brand logos** and identifiable marks

For example, a single photograph may be automatically tagged with terms such as **"sunset," "beach," "vacation,"** or **"smiling."** Because tags are applied by a consistent model rather than by different individuals, the resulting metadata remains uniform and reliable across the entire asset catalog.

## Benefits of AI-generated metadata

<!--If the asset is a document, AI reads and interprets the text to assign meaningful keywords that summarize its content—such as "climate change," "policy," or "renewable energy.-->

![AI Generated metadata](/help/assets/assets/enhanced-smart-tags.png)

AI-generated metadata delivers measurable improvements to digital asset management:

- **Efficiency** — eliminates the manual tagging effort required for every asset
- **Consistency** — applies the same tagging logic across all content, reducing gaps and duplication
- **Scalability** — handles large volumes of digital content that would be impractical to tag by hand
- **Discoverability** — enriches metadata so assets surface more accurately in search and recommendation results

## Improving search with semantic and lexical techniques

AI-generated tags enhance asset discovery by leveraging both **semantic search** and **lexical search** techniques. **Lexical search** matches the exact keywords and terms a user enters, while **semantic search** interprets meaning and context to return conceptually related results even when the precise words differ. Combining both approaches ensures assets are retrievable whether users search by literal keyword or by intent, which broadens the range of queries that return the right asset.

See more [Search Assets](search-assets-view.md).

## How to enable AI-generated metadata? {#enable-ai-generated-metadata}

AI-generated metadata automatically produces descriptive tags, titles, and captions for assets, streamlining content management and improving asset discoverability. Enabling this capability requires meeting a minimum platform version and activating the feature within your environment.

### Prerequisites

* The minimum required **Adobe [!DNL Experience Manager] (AEM)** release version is **`20626`**. This ensures the underlying AI metadata generation capabilities are available and supported in your environment. Running a release earlier than **`20626`** prevents the feature from being activated, because the required services are not present in prior versions.

### Steps to Enable AI-Generated Metadata

To enable AI-generated metadata, complete the following steps:

1. **Verify the platform version.** Confirm that your Adobe [!DNL Experience Manager] (AEM) environment is running release version **`20626`** or later, as this is the minimum required to access the feature.
2. **Access the configuration settings.** Sign in with an administrator account and open the AEM administration or configuration area where asset and metadata features are managed.
3. **Locate the AI-generated metadata option.** Find the AI-generated metadata setting within the asset processing or metadata configuration section.
4. **Activate the feature.** Enable the AI-generated metadata option to turn on automatic metadata generation for your assets.
5. **Save and apply the configuration.** Save the changes so the setting takes effect across your environment.

Once enabled, AI-generated metadata is applied to eligible assets, reducing manual tagging effort and creating more consistent, searchable metadata across your content library.

## Using AI-generated metadata {#using-ai-generated-smart-tags}

<!--
[!NOTE]
>
>The enhanced smart tags capability is available only for the newly uploaded assets.
-->

<!--Alternatively, to update enhanced smart tags in an existing content, click **[!UICONTROL reprocess]**.-->

The enhanced smart tags feature uses Artificial Intelligence (AI) to automatically generate descriptive metadata—titles, descriptions, and keywords—for uploaded image assets, improving content discovery and reducing manual tagging effort. To use the enhanced smart tags feature, execute the following steps:

1. In the [!DNL Experience Manager] interface, go to the desired folder and click **[!UICONTROL Add Assets]**. **Supported image file formats** include `png`, `jpg`, `jpeg`, `psd`, `tiff`, `gif`, `webp`, `crw`, `cr2`, `3fr`, `nef`, `arw`, and `bmp`.

1. Wait until the newly uploaded asset is processed. Processing is required because [!DNL Experience Manager] analyzes the asset during this stage and generates its AI metadata; the smart tags become available only after processing completes. Once done, go to asset details.

1. Go to the **[!UICONTROL AI-Generated]** tab, which contains the AI-produced metadata fields for the asset. If the [!DNL Experience Manager] version is incompatible or not updated, this tab is not visible. The following fields are there:

    * **[!UICONTROL Generated title]:** The title provides a clear and concise headline that captures the core idea of an uploaded asset, making it easy to understand at a glance. When adding an asset, if you provide a title (in `dc:title`), [!DNL Experience Manager] displays that provided title in the assets browse view. If the title is left blank, [!DNL Experience Manager] automatically assigns an AI-generated title in its place, so every asset always carries a meaningful headline.
    * **[!UICONTROL Generated description]:** The description gives a brief yet informative summary of what the asset is about, helping users and the search module (content discovery engine) quickly grasp its relevance and surface the asset in relevant searches.
    * **[!UICONTROL Generated keywords]:** The keywords are targeted terms that represent the main themes of an asset, aiding in tagging and content filtering. Accurate keywords improve searchability and make it easier to organize and retrieve assets across large libraries.

1. [Optional] You may add additional tags or create your own if you feel any relevant tags are missing. To do this, write your tags in the **[!UICONTROL Generated keywords]** field and click **[!UICONTROL Save]**.

For information on how to disable AI-generated metadata, see [Disable AI-generated metadata](/help/assets/enhance-content-discovery-with-ai-generated-metadata.md#disable-ai-generated-metadata).


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
