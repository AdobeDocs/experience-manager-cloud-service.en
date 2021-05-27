---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
---

# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>From here, you can navigate to release notes of previous versions; for example, for those in 2020, 2021 and so on.

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2021.5.0 is May 27, 2021.
The following release (2021.6.0) will be on June 24, 2021.

## AEM as a Cloud Service Foundation {#foundation}

### What is New in AEM as a Cloud Service Foundation {#what-is-new-foundation}

* [Prerelease Channel](/help/release-notes/prerelease.md): Preview upcoming features for a full month before they go live in production!

* [API Deprecation](/help/release-notes/deprecated-apis.md): a list of the latest deprecated APIs for AEM as a Cloud Service is available. 

## [!DNL Adobe Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### What is new in [!DNL Sites] {#what-is-new-sites}

* As the [Preview Service](/help/sites-cloud/authoring/fundamentals/previewing-content.md) is being enabled in AEM as a Cloud Service environments, publishing to Preview will be possible in the AEM Sites Managed Publication wizard. This capability will be gradually rolled out in the next few weeks.

## [!DNL Adobe Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### What is new in [!DNL Assets] {#what-is-new-assets}

* You can download the assets shared using the Link Share functionality. This download now uses an asynchronous service that offers faster and and uninterrupted downloads, even for very large downloads. See [download assets](/help/assets/download-assets-from-aem.md#link-share-download).

  ![Download inbox](/help/assets/assets/download-inbox.png)

### New features available in the prerelease channel {#what-is-new-assets-prerelease}

* Metadata schemas can be applied directly to the folder properties.

  ![Add metadata schema from folder properties](/help/assets/assets/metadata-schema-folder-properties.png)

* The Asset Bulk Ingestor tool lets you add metadata during a bulk ingestion.

* A user experience enhancements displays the number of assets present in a folder. For more than 1000 assets in a folder, [!DNL Assets] displays 1000+.

  ![Number of assets in a folder are displayed on the interface](/help/assets/assets/browse-folder-number-of-assets.png)

### Bugs fixed in [!DNL Assets] {#assets-bugs-fixed}

* Uploading very large files crashes the [!DNL Experience Manager desktop app]. (CQ-4320942)
* The toolbar options are different when the same Collection is selected from within a folder and when it is selected from a search result. (CQ-4321406)

#### What is new in Dynamic Media {#what-is-new-dm}

* Smart Imaging DPR (Device Pixel Ratio) and network bandwidth optimization enables you to deliver best quality images efficiently, on devices with high resolution displays and constrained network bandwidth. For more information, see [Smart imaging FAQs](/help/assets/dynamic-media/imaging-faq.md).

   >[!NOTE]
   >
   >The release timeline for the above Smart Imaging enhancements is:
   >
   >* North America May 24, 2021 in NA,
   >
   >* Europe, the Middle East and Africa June 25, 2021,
   >
   >* Asia-Pacific July 19, 2021.

* Introduced support for next-gen image format AVIF in Dynamic Media delivery (fmt URL modifier).

  >[!NOTE]
  >
  >The release timeline for AVIF support is:
  >
  >* North America May 10, 2021,
  >
  >* Europe, the Middle East and Africa May 24, 2021,
  >
  >* Asia-Pacific June 24, 2021.

### Bug fixes in [!DNL Assets] {#bug-fixes-assets}

## Cloud Manager {#cloud-manager}

This section outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.5.0.

### Release Date {#release-date-cm-may}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.5.0 is May 06, 2021.
The next release is planned for June 03, 2021.

### What's New {#what-is-new-may}

* The PackageOverlaps quality rule now detects cases where the same package was deployed multiple times, i.e. in multiple embedded locations, in the same deployed package set.

* The repository endpoint in the Public API now includes the Git URL.

* Deployment log downloaded by a Cloud Manager user will be more insightful and will now include details about failures and success scenarios.

* Intermittent failures encountered while pushing code to Adobe git have now been resolved.

* Commerce add-on can now be applied to Sandbox programs during the Edit program workflow.

* The Edit program experience has been refreshed. 

* The Domain Names table in the Environment Details page will display up to 250 Domain names via pagination. 

* The Solutions tab in Add Program and Edit Program workflows will display the solution, even if only one solution is available for the Program.

* The error message in the build step log when the build did not produce any deployed content packages was unclear.

### Bug Fixes {#bug-fixes-cm-may}

* On occasion, user may see a green "active" status next to an IP Allow List even when that configuration was not deployed. 

* Instead of removing 'deleted' variables, the pipelines variables API would only mark them with status **DELETED**. 

* Some Code Smell-type quality issues were incorrectly impacting the Reliability Rating.

* Since wildcard domains are not supported, the UI will disallow the user from submitting a wildcard domain.

* When a pipeline execution was started between midnight and 1am UTC the artifact version generated by Cloud Manager was not guaranteed to be greater than a version created the prior day.

* During Sandbox program setup, once the project with sample code has been successfully created, Manage Git will appear as a link from the hero card in the Overview page. 

## Content Transfer Tool {#content-transfer-tool}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.4.0 is May 11, 2021.

### What's New {#what-is-new-ctt-may}

* This version of the Content Transfer Tool creates text renditions for assets being migrated to Cloud Service. Text renditions are required to support full text search on ingested assets.
* The maximum number of Content Transfer Tool migration sets a user can create has been increased from 4 to 10. 

### Bug Fixes {#bug-fixes-ctt-may}

* Multiple bug fixes related to the auto-refresh feature in the Content Transfer Tool UI.
* Content Transfer Tool with `wipe=true` resulted in incorrect counter index on the target. This has been fixed.

## Commmerce add-on {#cloud-services-commerce}

### What is New {#what-is-new-commerce}

* Pagination support for associated content in product console properties

### Bug Fixes {#bug-fixes-commerce}

* Asset thumbnails not displayed in Asset tab of product properties

* Breadcrumb resets preview data in product console
