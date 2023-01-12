---
title: Auto-tag assets with [!DNL Adobe Sensei] smart service
description: Tag assets with an artificially intelligent service that applies contextual and descriptive business tags.
contentOwner: AG
feature: Smart Tags,Tagging
role: Admin,User
exl-id: a2abc48b-5586-421c-936b-ef4f896d78b7
---

# Smart tags for AEM Assets {#using-smart-tags}

Organizations have many digital assets and these are growing continuously. Searching the desired asset while dealing with such enormous amount of data is a significant challenge. To deal with this challenge, *metadata* and *tags* are used to enhance the search capability of digital assets. Organizations use taxonomy-controlled vocabulary in asset metadata. Essentially, it includes a list of keywords that employees, partners, and customers commonly use to refer to and search for their digital assets. Tagging assets with taxonomy-controlled vocabulary ensures that the assets can be easily identified and retrieved in searches. 

For an instance, the words saved in the dictionary in an alphabetical order are easier in search, rather than searching the scattered words. Tagging also solves the same purpose. It aligns assets based on business taxonomy and ensures that the most relevant assets appear in searches. For example, a car manufacturer can tag car images with model names so only relevant images are displayed when searched to design a promotion campaign.

## Prerequisites and configuration

Smart Tags is automatically provisioned for [!DNL Adobe Experience Manager] as a [!DNL Cloud Service].

## Smart Tags workflow

![Smart-tags-flow-diagram](assets/smart-tags.png)

Smart tags are implemented in AEM Assets using the following workflow:
1.  Create or upload an asset in AEM.
1.  Text-based tags are generated automatically based on the type of asset that you have created or uploaded. If you find that specific tags are not generated, then you can train your tags accordingly. Refer to [smart tags training](#smart-tags-training.md).
1.  Once smart tags are trained, the tags identification are saved in AEM so that you apply these tags on a similar set of assets.

## Preparing an asset for smart tagging

When you [upload assets](add-assets.md#upload-assets) to [!DNL Adobe Experience Manager] as a [!DNL Cloud Service], the uploaded assets are processed. Once the processing is complete, see the [!UICONTROL Basic] tab of asset [!UICONTROL Properties] page. Smart tags are automatically added to the assets under [!UICONTROL Smart Tags]. Asset microservices uses [!DNL Adobe Sensei] to create these smart tags.

![Smart Tags are added to videos and seen in Basic tab of asset Properties](assets/smart-tags-added-to-videos.png)

<!--
The applied smart tags are sorted in descending order of [confidence score](#confidence-score), combined for object and action tags, within [!UICONTROL Smart Tags].
-->

>[!IMPORTANT]
>
>You are advised to review these automatically generated tags to ensure that they conform to your brand and its values.

## Supported asset types {#smart-tags-supported-file-formats}

You can tag the following types of assets:
![Smart-tag-types](assets/smart-tags-types.png)

### Out of the box smart tags

[!DNL Adobe Sensei] powered smart tagging feature uses artificial intelligence models to analyze content and add tags to the assets. Thereby-reducing time for DAM users to deliver rich experiences to their customers. The smart tags are displayed in descending order of their [confidence score](#confidence-score) in asset [!UICONTROL Properties]. 

#### Text-based assets 

For text-based assets, the efficacy of Smart Tags does not depend on the amount of text in the asset but on the relevant keywords or entities present in the text of the asset. The Smart Tags are the keywords that appear in the text but the ones that best describe the asset.
For supported assets, Experience Manager already extracts the text, which is then indexed and is used to search for the assets. However, Smart Tags based on keywords in the text provide a dedicated, structured, and higher priority search facet. The latter helps improve asset discovery as compared to a search index.

**Example of tagging assets with Smart Tags**

All types of supported assets are automatically tagged by [!DNL Experience Manager Assets] when uploaded. Tagging is enabled and works, by default. [!DNL Experience Manager] as a [!DNL Cloud Service] applies the appropriate tags in near-real-time.

#### Image-based assets

For images and videos, the Smart Tags are based on some visual aspect. Images in many formats are tagged using the Adobe Sensei's smart content services. Smart Tags are applied to the supported file types that generate renditions in JPG and PNG format.

![Image Smart Tag](assets/image-smart-tag.png)

#### Video-based assets

For video-based assets, tagging is enabled by default in [!DNL Adobe Experience Manager] as a [!DNL Cloud Service]. [Videos are auto-tagged](/help/assets/smart-tags-video-assets.md) when you upload new videos or reprocess existing ones. [!DNL Adobe Sensei] generates two sets of tags for a video. One set corresponds to objects, scenes, and attributes in that video, whereas, the other set relates to actions such as drinking, running, and jogging. 
Videos are auto-tagged when you upload new videos or reprocess existing ones. [!DNL Experience Manager] also creates the thumbnails and extracts metadata of the video files. Also check [opt out video smart tagging](#opt-out-video-smart-tagging).

 ##### Confidence Score {#confidence-score}

[!DNL Adobe Experience Manager] as a [!DNL Cloud Service] applies a minimum confidence threshold for object and action-smart tags to avoid having too many tags for each asset, which slows down indexing. Your asset search results are ranked based on the confidence scores, which generally improve search results beyond what an inspection of the assigned tags of any asset suggests. Inaccurate tags often have low confidence scores so they seldom appear at the top of the Smart Tags list for assets.

The default threshold for action and object tags in [!DNL Adobe Experience Manager] for an image is 0.5 and for video it is 0.7 (should be value from 0 through 1). If some assets are not tagged by a specific tag, then it indicates that the algorithm is less than 70% confident in the predicted tags. The default threshold might not always be optimal for all the users. You can, therefore, change the confidence score value in OSGI configuration.

To add the confidence score OSGI configuration to the project deployed to [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] through [!DNL Cloud Manager]:

* In the [!DNL Adobe Experience Manager] project (`ui.config` since Archetype 24, or previously `ui.apps`) the `config.author` OSGi configuration, include a config file named `com.adobe.cq.assetcompute.impl.senseisdk.SenseiSdkImpl.cfg.json` with the following contents:

```json
{
  "minVideoActionConfidenceScore":0.5,
  "minVideoObjectConfidenceScore":0.5,
}
```

>[!NOTE]
>
>Manual tags are assigned a confidence of 100% (maximum confidence). Therefore, if there are assets with manual tags that match the search query, they are displayed before smart tags matching the search query.

### Trainable smart tags check 

Image type smart tags can be trained to provide more accuracy and efficacy in the tags. Refer to the [smart tags training](#/help/assets/smart-tags-training.md) to understand the training of images with custom or enhanced smart tags.

#### Determining the requirement of smart tags training {#smart-tag-training-requirement}

Smart tags training is required in the following scenarios:
* To add an automated labeler to save iterations of adding labels every time you upload the same asset.
* To improve the ability of assets to apply relevant tags.
* To increase accuracy of the tags appearing for an asset.
* To add unavailable or missing labels.

### Supported file formats for smart tags {#supported-file-formats}

|Images (MIME types) | Text-based assets (file formats) | Video assets (file formats and codecs) |
|----|-----|------|
| image/jpeg | CSV | MP4 (H264/AVC) |
| image/tiff | DOC | MKV (H264/AVC) |
| image/png | DOCX | MOV (H264/AVC, Motion JPEG) |
| image/bmp | HTML | AVI (indeo4) |
| image/gif | PDF | FLV (H264/AVC, vp6f) |
| image/pjpeg | PPT | WMV (WMV2) |
| image/x-portable-anymap | PPTX |  |
| image/x-portable-bitmap | RTF |  |
| image/x-portable-graymap | SRT |  |
| image/x-portable-pixmap | TXT |  |
| image/x-rgb | VTT |  |
| image/x-xbitmap | |  |
| image/x-xpixmap | |  |
| image/x-icon |  |  |
| image/photoshop |  |  |
| image/x-photoshop |  |  |
| image/psd |  |  |
| image/vnd.adobe.photoshop |  |  |

## Smart tagging existing assets in DAM {#smart-tag-existing-assets}

The existing assets in DAM are not smart tagged automatically. You need to [!UICONTROL Reprocess Assets] manually to generate smart tags for them.

To smart tag assets, or folders (including subfolders) of assets that exist in assets repository, follow these steps:

1. Select the [!DNL Adobe Experience Manager] logo and then select assets from the [!UICONTROL Navigation] page.

1. Select [!UICONTROL Files] to display the Assets interface.

1. Navigate to the folder to which you want to apply smart tags.

1. Select the assets and click ![Reprocess assets icon](assets/do-not-localize/reprocess-assets-icon.png) [!UICONTROL Reprocess Assets] icon and select the [!UICONTROL Full Process] option.

![Reprocess assets to add tags to videos existing DAM repository](assets/reprocess.gif)

Once the process completes, navigate to the [!UICONTROL Properties] page of any asset within the folder. The automatically added tags are seen in [!UICONTROL Smart Tags] section in [!UICONTROL Basic] tab. These applied smart tags are sorted in descending order of [confidence score](#confidence-score).

## Moderate smart tags {#moderate-smart-tags}

[!DNL Adobe Experience Manager] as a [!DNL Cloud Service] allows you to curate the smart tags to:

* remove inaccurate tags assigned to your brand assets.

* refine tag-based searches for assets by ensuring that your asset appears in search results for the most relevant tags. It, therefore, eliminates the chances of unrelated assets from showing up in search results.

* assign a higher rank to a tag to increase its relevance with respect to an asset. Promoting a tag for an asset increases the chances of the particular asset appearing in search results when a search is performed based on that tag.

To know more about how to moderate the smart tags for assets, see [Manage smart tags](smart-tags.md#manage-smart-tags-and-searches).

![Moderate video smart tags](assets/manage-video-smart-tags.png)

>[!NOTE]
>
>Any tags that are moderated using the steps in [Manage smart tags](smart-tags.md#manage-smart-tags-and-searches) are not remembered on reprocessing of the asset. The original sets of tags are displayed again.



## Manage smart tags and asset searches {#manage-smart-tags-and-searches}

You can curate smart tags to remove any inaccurate tags that may have been assigned to your brand assets, so that only the most relevant tags are displayed.

Moderating smart tags also helps refine tag-based searches for assets by ensuring that your assets appear in search results for the most relevant tags. Essentially, it helps eliminate the chances of unrelated assets from showing up in search results.

You can also assign a higher rank to a tag to increase the tag's relevance for the asset. Promoting a tag for an asset increases the chances of the asset appearing in search results when a search is performed based on the particular tag.

To moderate the smart tags of your digital assets:

1. In the search field, search for digital assets based on a tag.

1. To identify the digital assets that you do not find relevant to your search, inspect the search results.

1. Select an asset, and then select ![Manage tags icon](assets/do-not-localize/manage-tags-icon.png) from the toolbar.

1. From the **[!UICONTROL Manage Tags]** page, inspect the tags. If you do not want the asset to be searched based on a specific tag, then select the tag and select ![Delete icon](assets/do-not-localize/delete-icon.png) from the toolbar. Alternatively, select `X` symbol next to the label.

1. To assign a higher rank to a tag, select the tag and select ![Promote icon](assets/do-not-localize/promote-icon.png) from the toolbar. The tag you promote is moved to the **[!UICONTROL Tags]** section.

1. Select **[!UICONTROL Save]** and then select **[!UICONTROL OK]** to close the [!UICONTROL Success] dialog.

1. Navigate to the [!UICONTROL Properties] page for the asset. Observe that the tag that you promoted is assigned a high relevance and, therefore, appears higher in the search results.

### Understand [!DNL Experience Manager] search results with smart tags {#understand-search}

By default, [!DNL Experience Manager] combines the search terms with an `AND` or `OR` clause to find any of the search terms in the applied smart tags. Using smart tags does not change this default behavior. For example, consider searching for `woman running`. Assets with just `woman` or just `running` keyword in the metadata do not appear in the search results by default. However, an asset tagged with either `woman` or `running` using smart tags appears in such a search query. So the search results are a combination of,

* Assets with `woman` and `running` keywords in the metadata.

* Assets smart tagged with either of the keywords.

The search results that match all search terms in metadata fields are displayed first, followed by the search results that match any of the search terms in the smart tags. In the above example, the approximate order of display of search results is:

1. matches of `woman running` in the various metadata fields.
1. matches of `woman running` in smart tags.
1. matches of `woman` or of `running` in smart tags.

## Opt out of smart tagging {#opt-out-smart-tagging}

As the automated tagging of assets runs in parallel to other asset processing tasks like thumbnail creation and metadata extraction, it can be time consuming. To expedite the asset processing, you can opt out of smart tagging on upload at folder level.

To opt out of automated smart tags generation for assets uploaded to specific folder:

1. Open [!UICONTROL Asset Processing] tab in folder [!UICONTROL Properties].

1. In [!UICONTROL Smart Tags for Videos] menu, for example, [!UICONTROL Inherited] option is selected by default and video smart tag is enabled.

    When the [!UICONTROL Inherited] option is selected, the inherited folder path is also visible along with the information whether it is set to [!UICONTROL Enable] or [!UICONTROL Disable].

    ![Disable smart tagging](assets/disable-tagging.png)

1. Select [!UICONTROL Disable] to opt out of smart tagging uploaded to the folder.

>[!IMPORTANT]
>
>If you have opted out of tagging on a folder at the time of upload and want to smart tag the after upload, then **[!UICONTROL Enable Smart Tags]** from [!UICONTROL Asset Processing] tab of the folder [!UICONTROL Properties] and use [[!UICONTROL Reprocess Asset] option](#smart-tag-existing-assets) to add smart tags to the assets.

## Benefits of smart tags to your assets {#benefits-of-smart-tags}

Following are the benefits of using smart tags in your AEM Assets:
*  Smart tags are generated automatically to your assets, thus, it minimizes your effort to perform tagging manually.
*  It allows the usage of the same vocabulary, tag structure, and taxonomy so that you need not to worry about tagging if by chance you miss tagging at first.
*  Whether you are tagging "runners" or "running" shoes, you do not need to worry about typos, wrong spellings, or alternative search terms as smart tags know it already!
*  Helps your assets to become organized and categorized.

## Limitations and best practices related to smart tags {#limitations}

These models are not always perfect at identifying tags. The current version of the Smart Tags has the following limitations:

* Inability to recognize subtle differences in images. For example, slim-fit versus regular-fit shirts.
* Inability to identify tags based on tiny patterns or parts of an image. For example, logos on shirts.
* The tags that are not handled relate to:

  * Non-visual, abstract aspects. For example, the year or season of release of a product, mood or emotion evoked by an image, and a subjective connotation of a video.
  * Fine visual differences in products such as shirts with and without collars or small product logos embedded on products.

* To train the model, use the most appropriate images. The training cannot be reverted or training model cannot be removed. Your tagging accuracy depends on the current training, so do it carefully.
* You cannot train the service that applies Smart Tags to videos using any specific videos. It works with default [!DNL Adobe Sensei] settings.
* Tagging progress is not displayed.
* Only the videos smaller than 300 MB in file size are auto-tagged. The [!DNL Adobe Sensei] service skips video files that are larger in size.
* To search for files with smart tags (regular or enhanced), use the [!DNL Assets] search (full-text search). There is no separate search predicate for smart tags.
* In comparison of general tags, the assets that are tagged using business taxonomy are easier to identify and retrieve by tag-based searches.

>[!NOTE]
>
>The ability of the Smart Tags to train on your tags and apply them on other images depends on the quality of images you use for training.
>For best results, Adobe recommends that you use visually similar images to train the service for each tag.

## Frequently asked questions

* **How do smart tags improve search experience of an asset?**
  Adobe Sensei tags the assets automatically once you upload them. The automated process runs so fast at the backend that you will see tags added in your assets after a few seconds once the upload is completed.

* **What happens if the smart tag list is inaccurate or showing unwanted tag?**
  An inaccurate or unwanted tag can be removed from the list. For example, as an automobile dealer, you might want to remove "damaged" tag from the list.

* **How can you prioritize assets containing same tags?**
  Yes, you can prioritize assets containing the same tags. You can promote a tag into the Smart Tags list of an asset to perform prioritization. Promoting a tag allows you to prioritize the images appearing in the search results for that particular tag.

* **Is the application of Smart Tags limited to a particular folder?**
  Smart tags are configurable and can be applied on any folder inside DAM.

* **How may I know that tagging needs training?**
  Refer to [Determining the requirement of smart tags training](#smart-tag-training-requirement).

* **What are the supported file formats for tagging an asset?**
  Refer to [Supported file formats](##supported-file-formats).

* **I do not want to use video smart tagging anymore.**
You can [opt out smart tagging](#opt-out-smart-tagging) anytime you want to discontinue.