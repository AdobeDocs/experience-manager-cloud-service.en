---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 21772 {#21772}

Summarized below are the continuous improvements for maintenance release 21772, which was publicly released on August 6, 2025. The previous maintenance release was release 21706.


The 2025.8.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-21772}

* ASSETS-39377: Improve handling of 429s from remote storage in Assets Bulk Importer.
* ASSETS-46026: Configurable max depth for metadata exporter.
* ASSETS-49172: Dynamic Media Template assets should inherit Metadata from Folder.
* ASSETS-50209: Support for substring in DM Templates.
* ASSETS-52326: AEM Assets configuration page to set Title display preferences for Assets.
* ASSETS-52805: Add CSV output/download support for Bulk Operation job.
* ASSETS-52873: Add a new configuration in the folder properties to disable AI processing for that folder.
* ASSETS-53535: Improved YouTube video upload performance.
* ASSETS-53612: Control for Hybrid Search in Assets Omnisearch.
* GRANITE-60183: Update commons-fileupload dependency to 1.6.0.
* GRANITE-60287: Update QS to Jackrabbit 2.22.1.
* SITES-30452: Content API with ASO - Title & Description Suggestions.
* SITES-31677: Custom workspace support AEM Content fragment export to Target.
* SKYOPS-112741: Remove the `com.adobe.granite.product.support` bundle from the AEM-CS SDK.

### Fixed Issues {#fixed-issues-21772}

* ASSETS-12882: UI alignment issues after opening viewer presets.
* ASSETS-48958: Issue with Asset Sync changing Published Status in Sites local AEM.
* ASSETS-50856: `dam:processingAttempts` not being reset on completeUpload.
* ASSETS-51604: Link Share Report CSV Missing “Shared With” Data.
* ASSETS-51783: Fallback to DM config under `/conf/global` if no config is found using search query.
* ASSETS-51857: Asset table items not reorderable.
* ASSETS-52169: New BAT machine rendition erroneously included in asset downloads.
* ASSETS-52229: Missing Inbox Notifications for Asset Reports in AEM as a Cloud Service.
* ASSETS-52399: Version bump in com.day.cq.dam.api might break customer code.
* ASSETS-52780: Asset can be marked for preview even without toggled enabled.
* ASSETS-52866: Migrated DM videos remain in processing state under folder with DM Sync disabled.
* ASSETS-53237: Color Profile dropdown blank in Image Preset editor.
* ASSETS-53240: Asset Report - Disk Usage fails when getting asset rendition size from Dynamic Media.
* ASSETS-53446: Intermittent YouTube auth token refresh failures due to NPE.
* ASSETS-53827: ACL validation blocks saving Mixed Media Sets.
* ASSETS-5403: Dynamicmedia clientlibs used on publish instance should have `allowProxy=true`.
* ASSETS-54261: Metadata import leaks connections and becomes blocked if the file fails to download.
* CQ-4359863: Tags search broken for keywords out of order in Content Fragment Editor/Asset editor.
* CQ-4359958: Make openapi-support compatible with AEM 6.5.22.0 and above.
* CQ-4360256: Include the servlet context path in the request path for HTTP requests handled via the `/adobe` servlet context.
* CQ-4360317: Add method for setting the Sunset date header when building responses.
* GRANITE-60311: AEM SDK Quickstart – NPE on “OSGi Installer Configuration Printer”.
* GS-15285: Users are shown as deactivated.

### Known Issues {#known-issues-21772}

None.

### Deprecated Features and APIs {#deprecated-21772}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-21772}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 4 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-21772}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.80.0|[Oak API 1.80.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.80/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.63 | [Apache Httpd 2.4.63](https://github.com/apache/httpd/blob/2.4.63/CHANGES)|
|AEM Core Components| 2.29.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
