---
title: Transcription Support in Dynamic Media Components
description: The transcript support in the Dynamic Media component has been added which improves accessibility, SEO, and content discoverability for video in Adobe Experience Manager (AEM).
role: Admin, User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets."
---
# Transcription Support to videos {#transcription-support}

Transcription in Dynamic Media [!DNL Dynamic Media with OpenAPI capabilities] uses the Automatic Speech Recognition (ASR) technology to convert spoken audio into a written text transcript. It processes audio recordings or live speech, identifies spoken words, and generates a searchable, time-aligned transcript that can be reviewed, edited, and shared. 

Transcripts for videos improves the accessibility for your customers. These are Server Side Rendered (SSR) transcripts which directly increase the SEO and LLM visibility of videos. It also embeds a compliant [VideoObject](https://schema.org/VideoObject) that helps search engine and LLM tools recognise videos in your page. 

The transcripts are generated based on the captions you have added in the video. With native transcription capabilities now integrated into the video, you can easily access and search content without the need for transcription through external sources. 

## Prerequisites {#prerequisites-for-enabling-transcriptions}

To enable the transcription feature, ensure you have videos with captions in Adobe Experience Manager (AEM) Sites.

## Enabling Transcription for videos in Adobe Experience Manager (AEM)  {#enable-transcription}

To enable the transcription feature, follow the steps mentioned below:

1. In Adobe Experience Manager (AEM) Sites, navigate to the homepage of any website. For example, from the homepage, navigate to **[!UICONTROL English]** > **[!UICONTROL Home]** as shown in the figure.
   ![Homepage](/help/assets/assets/homepage.png)
3. Click the **[!UICONTROL Edit]** button ![Edit icon](assets/do-not-localize/edit_icon.svg) on the top of the page to add a Dynamic Media component and a video element inside that Dynamic Media component.
   1. To add a video element inside the Dynamic Media component, select Videos from the Category drop-down. Drag and drop the video element to add it in Dynamic Media.

      ![Video](/help/assets/assets/videos.png)
   
   2. To add a Dynamic Media component, click the Components icon. Drag and drop a Dynamic Media component as shown in the figure.
   ![Dynamic Media Component](/help/assets/assets/dmcomponents.png)

3. Right click on the Dynamic Media component and click on Configure to configure some settings.
   ![Configure](/help/assets/assets/component.png)
4. From the **[!UICONTROL Viewer Preset]** drop down, select **[!UICONTROL Video (new)]** and enable the **[!UICONTROL Show transcript]**. The **[!UICONTROL Viewer Modifiers]** field allows you to select the language in which you want the transcript to be displayed. For example, you can select English as the default language and click **[!UICONTROL Done]**.
   ![Dynamic Media Tab](/help/assets/assets/dmtab.png)
5. Click the **[!UICONTROL Page Information]** icon and select **[!UICONTROL View As Published]**.
      ![Page Information](/help/assets/assets/icon.png)
   The image below shows the video along with the transcription.
      ![Dynamic Media Transcription](/help/assets/assets/trans.png)

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
* [Manage reports](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)

