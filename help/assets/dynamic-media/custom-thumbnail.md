---
title: Custom Thumbnail Support for videos in Polaris
description: Custom thumbnail support for video assets in Polaris (Dynamic Media with OpenAPI) has been added. Users can upload or select a custom thumbnail for a video asset in Adobe Experience Manager (AEM); the video player uses that custom thumbnail as the poster image when available, instead of an auto-generated frame.
role: Admin, User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets."
---
# Custom Thumbnail Support for videos {#custom-thumbnail}

Adobe Experience Manager (AEM) Assets custom video thumbnails let authors select an appropriate thumbnail from a frame within the video or use an uploaded image asset. The number of thumbnails generated for a video asset can be customized. Custom video thumbnails provide greater control over the visual presentation of video assets across digital experiences.

## Enabling Custom Thumbnail for videos {#enabling-custom-thumbnail}

To enable custom thumbnails for videos, follow the steps mentioned below:

1. In [Adobe Experience Manager](https://author-p49105-e258067.adobeaemcloud.com/ui#/aem/sites.html/content/wknd) (AEM), navigate to **[!UICONTROL Assets]** > **[!UICONTROL Files]**.
2. Click any video asset and navigate to **[!UICONTROL Properties]**.
3. You can now see the **[!UICONTROL Change Thumbnail]** option along with the title and other details of the video asset. 
    ![Custom Thumbnail of a video asset](/help/assets/dynamic-media/assets/thumbnails.png)
   1. To generate a thumbnail from an existing video asset, click **[!UICONTROL Change Thumbnail]** and select **[!UICONTROL Select Frame from Video]**. Play the video asset and navigate to the desired frame. Once you have identified the frame you want to use as the thumbnail, click **[!UICONTROL Save Change]** to generate and save the thumbnail from that specific frame in the video asset.
       ![Selecting Thumbnail of a video asset](/help/assets/dynamic-media/assets/changethumbnail.png)
   2. To select a thumbnail from an existing image in Assets, click **[!UICONTROL Change Thumbnail]** and select **[!UICONTROL Select Thumbnail from Assets]**. Click **[!UICONTROL Select Thumbnail]** and select the thumbnail. Click **[!UICONTROL Save Change]**. 
      ![Selecting Thumbnail of a video asset from existing thumbnail](/help/assets/dynamic-media/assets/changethumbnail1.png)
    You can now see the newly generated thumbnail image. 
       ![Selecting Thumbnail of a video asset](/help/assets/dynamic-media/assets/newthumbnail.png)

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
