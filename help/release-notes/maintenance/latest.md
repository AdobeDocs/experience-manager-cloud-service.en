---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 16799 {#release-16799}

Summarized below are the continuous improvements for maintenance release 16799, which was publicly released on June 18, 2024. The previous maintenance release was release 16544.

2024.6.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-16799}

* ASSETS-31977: Enhanced Asset Move, Copy and Delete operations.
* ASSETS-33618: Auto-transcription and translation capability for Videos in Dynamic Media.
* ASSETS-35185: Approval Action for ContentHub and DM and add properties to damAssetLucene properties.
* ASSETS-35533: Add DRM and CAI properties to damAssetLucene index.
* ASSETS-37280: Sequential job handling for translation when source subtitle (vtt) is still processing.
* ASSETS-37559: Improved asset deleted event.
* ASSETS-37723: Implement asset published event.
* ASSETS-37724: Implement asset unpublished event.
* ASSETS-38614: Share Link UI enhancements.
* ASSETS-39601: Apply validation regex automatically to Asset Livecopy name.
* ASSETS-39454: Upgrade to viewers 2024.5.0 in Quickstart.
* CNTBF-184: Support paths beneath `/conf` in Content Backflow.

### Fixed Issues {#fixed-issues-16799}

* ASSETS-37335: Editing Search Panel In Filter Unchecks All Boxes.
* ASSETS-38069: AEM DAM PDF Preview Issue on Timeline Filter Selection.
* ASSETS-38215: Adobe Stock license button grayed out in AEM as a Cloud Service for enterprise subscription.
* ASSETS-38578: Incorrect Hyperlinks in Assets Link Share Report.
* ASSETS-38678: View settings broken in Collection Details.
* ASSETS-39071: Web optimized delivery may throw an exception if the original rendition mimetype is null.
* ASSETS-39316: Sorting by name not working in Collections.
* ASSETS-39377: Bulk import from OneDrive might fail when receiving backpressure from remote API.
* ASSETS-39428: Rendering issues in Copyright Management UI.
* CQ-4357150: Guava in cq-content-sync bundle.
* GRANITE-52573: Requests containing a double slash `//` are rejected with status code 400.
* SCRNS-4194: Remove dependency on Google Guava APIs.
* SCRNS-4360: Missing Manage Publication & Quick Publish Button for non-admin users in Content Provider for Channels.
* SCRNS-4323: Hide/Disable launches from screens.html.
  
### Known Issues {#known-issues-16799}

>[!NOTE]
> AEM Engineering has identified a regression for Launches functionality which is affecting current AEM releases starting with 16461. Because of this regression, new Launches (created after new releases have been applied) that include non-deep pages will not be properly promoted due to missing configurations.
> In case your environments are affected, a shell script to identify and update missing configurations is available through customer support (internal reference SITES-22457).
> A longer term fix will be made available that will ensure new Launches are created with all the right configurations. Until then, an internal patch release is also available on demand.

#### Forms

1.	If a user downloads the AEM Forms SDK version greater than `AEM Forms add-on v2024.05.04.00-240400`, the batch file fails to start the Docker service. To resolve this issue:
    1. Download the [folder](/help/forms/assets/sdk_hotfix.zip).
    1. Extract the contents from the downloaded folder and copy the `sdk.sh` and `sdk.bat` files.
    1.	Replace the existing `sdk.sh` and `sdk.bat` files in your AEM Forms SDK with the new files.

### Change Notice {#change-notice-16799}

* This release contains the following new product index versions:
  * **damAssetLucene-11**
  * **fragments-11**

  Custom versions of the previous index versions will be automatically merged with the new product index version. Please apply further custom updates to the merged version.

* Starting in September 2024, AEM as a Cloud Service will disable the serialization of Resource Resolvers via the Sling Model Exporter framework. See [the documentation](/help/implementing/developing/hybrid/disallow-the-serialization-of-resourceresolvers-via-sling-model-exporter.md) for more details.

### Deprecated Features and APIs {#deprecated-16799}

To know what is deprecated or removed in AEM as a Cloud Service, see [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md).

### Embedded Technologies {#embedded-tech-16799}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.64.0|[Oak API 1.64.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.64.0/index.html)| 
|AEM SLING API | 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.22-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.25.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
