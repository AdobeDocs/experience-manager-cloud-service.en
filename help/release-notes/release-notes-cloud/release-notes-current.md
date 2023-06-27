---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
mini-toc-levels: 1
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
---
# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2021 or 2022.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2023.6.0) is June 29, 2023. The next feature release (2023.7.0) is planned for July 27, 2023.

## Release Video {#release-video}

Have a look at the June 2023 Release Overview video for a summary of the features added in the 2023.6.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3420971/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

*   Added support for WebP images to automatically extract metadata, generate thumbnails and custom renditions. Smart Tags capability is also now supported for these files. Dynamic Media capabilities are not supported for WebP as an input format.

*   [Search experience enhancements](/help/assets/search-assets.md#aftersearch) - You can now quickly perform the following operations on the assets that display in the search results:

    * Create a workflow
    * Create a version
    * Relate or Unrelate assets

      You do not need to navigate to the asset location and view its properties to perform these operations.

*   Color Search facet usability improvements - Input field for color values is now editable and search results update only when you exit the color picker. 

*   New protocol support launched (DASH - Dynamic Adaptive Streaming over HTTP) for Adaptive streaming in Dynamic Media video delivery (with CMAF enabled):
    * Adaptive streaming (DASH/HLS) ensures better end user viewing experience for videos
    * DASH is the international standard protocol for adaptive video streaming and is widely adopted in the industry
    * Available in all regions, to be enabled via support ticket

*  Dynamic Media _Snapshot_ - Experiment with test images or Dynamic Media URLs, to see the output of different image modifiers, and assess Smart Imaging optimizations for file size (with WebP and AVIF delivery), network bandwidth, and Device Pixel Ratio. See [Dynamic Media Snapshot](https://experienceleague.adobe.com/docs/experience-manager-learn/assets/dynamic-media/images/dynamic-media-snapshot.html).

### Feature in [!DNL Assets] prerelease {#prerelease-feature-assets}

* Dynamic Media - The user interface for some Smart Crop-related fields in an Image Profile are now updated to reflect the current guidelines for defining a Smart Crop. See [Crop options](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/assets/dynamicmedia/image-profiles.html?lang=en#crop-options). 

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here.](/help/implementing/cloud-manager/release-notes/current.md)

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
