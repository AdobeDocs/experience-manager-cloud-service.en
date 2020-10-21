---
title: Smart tag your video assets
description: Smart tagging video assets automates the asset tagging by applying contextual and descriptive business tags using Adobe Sensei services.
---

# Smart tag your video assets {#video-smart-tags}

Purpose: for content velocity...

[!DNL Adobe Experience Manager] as a Cloud Service supports automated tagging of video assets assisted by artificial intelligence. Tagging the videos manually can be time-consuming. However, Adobe Sensei powered video smart tagging feature uses artificial intelligence models to analyze video content and add tags to the video assets. Thereby reducing time for DAM users to deliver rich experiences to their customers.

The video assets with file formats MP4, MKV, MOV, AVI, FLV, and WMV are supported for smart tagging. Moreover, the functionality supports tagging of videos up to the size 300 MB. The automated tagging of video assets occurs as standard asset processing after a video is uploaded, or when a re-processing is triggered. The video tagging process runs in parallel to thumbnail creation, and metadata extraction in the Asset Compute service, thereby increasing the processing time for video assets. You can, therefore, [opt-out of video smart tagging](#opt-out-video-smart-tagging) on a folder.

## Smart tagging videos on ingestion {#smart-tag-assets-on-ingestion}

When you [upload video assets](add-assets.md#upload-assets) to [!DNL Adobe Experience Manager] as a Cloud Service, the videos undergo ![processing](assets/do-not-localize/assetprocessing.png). Once the processing is complete, see the [!UICONTROL Basic] tab of asset [!UICONTROL Properties] page. Smart tags are automatically added to the video under [!UICONTROL Smart Tags]. Asset Compute Service leverages Adobe Sensei to create these smart tags.

>[!IMPORTANT]
>
>You are advised to review these automatically generated tags to ensure that they conform to your brand and its values.

## Smart tagging existing videos in DAM {#smart-tag-existing-videos}

The already existing video assets in DAM are not smart tagged automatically. You need to [!UICONTROL Reprocess Assets] manually to generate smart tags for them.

To smart tag video assets, or folders (including subfolders) of assets that already exist in assets repository, follow these steps:

1. Select the [!Adobe Experience Manager] logo and then select assets from the [!UICONTROL Navigation] page.

1. Select [!UICONTROL Files] to display the Assets interface.

1. Navigate to the folder to which you want to apply smart tags.

1. Select the entire folder or specific video assets.

1. Select ![reprocess assets icon](assets/do-not-localize/reprocess-assets-icon.png) from the toolbar and select the [!UICONTROL Full Process] option.

Once the process completes, navigate to the [!UICONTROL Properties] page of any video asset within the folder. The automatically added tags are seen in [!UICONTROL Smart Tags] section in [!UICONTROL Basic] tab.

## Search for smart tagged videos {#search-smart-tagged-videos}

To search for the video assets based on the auto generated smart tags, use [Omnisearch](search-assets.md#search-assets-in-aem):

1. Select the search icon ![search icon](assets/do-not-localize/search_icon.png) from the toolbar to display the Omnisearch field.

1. Specify a tag, in the Omnisearch field, that you have not explicitly added to a video.

1. Search based on the tag.

The search results display the video assets based on the tag you specified.

## Moderate video smart tags {#moderate-video-smart-tags}

[!DNL Adobe Experience Manager] allows you to curate the smart tags to:

* remove inaccurate tags assigned to your brand videos.

* refine tag-based searches for videos by ensuring that your video appears in search results for the most relevant tags. It, therefore, eliminates the chances of unrelated videos from showing up in search results.

* assign a higher rank to a tag to increase its relevance with respect to a video. Promoting a tag for a video increases the chances of the video appearing in search results when a search is performed based on that tag.

To know more about how to moderate the smart tags for assets, see [Manage smart tags](smart-tags.md#manage-smart-tags-and-searches).

>[!NOTE]
>
>Any tags that are moderated using the steps in [Manage smart tags](smart-tags.md#manage-smart-tags-and-searches) are not remembered on reprocessing of the asset. The original set of tags are displayed again.

## Opt out of video smart tagging on asset ingestion {#opt-out-video-smart-tagging}

As the automated tagging of videos runs in parallel to other asset processing tasks like thumbnail creation and metadata extraction, it can be time consuming. To expedite the asset processing you can opt out of video smart tagging at folder level.

To opt out of automated video smart tags generation for assets uploaded to specific folder:

1. Open [!UICONTROL Asset Processing] tab in folder [!UICONTROL Properties].

1. In [!UICONTROL Smart Tags for Videos] menu, [!UICONTROL Inherited] option is selected by default and video smart tag is enabled.

    When the [!UICONTROL Inherited] option is selected, the inherited folder path is also visible along with the information whether it is set to [!UICONTROL Enable] or [!UICONTROL Disable].

1. Select [!UICONTROL Disable] to opt out of smart tagging of videos uploaded to the folder.

## Confidence score {#confidence-score-video-tag}

General instructions on, Configuring OSGi for AEM as a Cloud Service: https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/deploying/configuring-osgi.html. This contains information how to configure services and where to add those configuration files in the CloudManager Git repository associated with the customer environment. 

The confidence score OSGI configuration must be added to the project deployed to AEM as a Cloud Service via Cloud Manager:

In the AEM project (ui.config since Archetype 24, or previously ui.apps) the config.author OSGi configuration, include a config file named com.adobe.cq.assetcompute.impl.senseisdk.SenseiSdkImpl.cfg.json with the following contents:

inside the ui.config Maven Project
/apps/example/osgiconfig/config.author/com.adobe.cq.assetcompute.impl.senseisdk.SenseiSdkImpl.cfg.json

{
  "minVideoActionConfidenceScore":0.5,
  "minVideoObjectConfidenceScore":0.5,
}
Confidence score value in OSGI config should have a value between 0 and 1. Default value is set to 0.7.

## Limitations {#video-smart-tagging-limitations}

* Training the Smart Tag Service (or Enhanced Smart Tags) for tagging your video assets is not supported yet.

* Tagging progress is not shown.

* Only the videos of size not more than 300 MB are suitable for tagging. The Adobe Sensei service smart tag the videos meeting this criteria and skip tagging other videos in a folder.

>[!MORELIKETHIS]
>
>* [Manage smart tags and asset searches](smart-tags.md#manage-smart-tags-and-searches)
>* [Train Smart Tag service and tag your images](smart-tags.md)
