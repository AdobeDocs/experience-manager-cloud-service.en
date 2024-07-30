---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 17258 {#release-17258}

Summarized below are the continuous improvements for maintenance release 17258, which was publicly released on July 30, 2024. The previous maintenance release was release 17098.

The 2024.8.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-17258}

* ASSETS-31445 - Initial Dynamic Media templating features
* ASSETS-40399 - Updated DM Auto transcribe queue settings
* ASSETS-40873 - Allow metadata export max rows to be set via OSGI config

### Fixed Issues {#fixed-issues-17258}

* ASSETS-30613 - Replace asset doesn't delete and add asset in new Delivery tier
* ASSETS-31882 - Accessing streaming manifest file in author is forbidden
* ASSETS-39598 - Bulk Import not able to delete assets with special characters in name from S3 backend
* CNTBF-209 -  Backflow jobs cancellation improvements
* SCRNS-3762 - Improve playerLogger in Sequence channel to put logs on console when previewing channel on browser
* SCRNS-4455 - Missing “Manage Publication” & "Quick Publish" Button for NON-ADMIN users in Content Provider for Channels
* SITES-22940 - Unable to view content fragment as workflow payload

### Known Issues {#known-issues-17258}

None

### Change Notice {#change-notice-17258}

* Starting in September 2024, AEM as a Cloud Service will disable the serialization of Resource Resolvers via the Sling Model Exporter framework. See [the documentation](/help/implementing/developing/hybrid/disallow-the-serialization-of-resourceresolvers-via-sling-model-exporter.md) for more details.

### Deprecated Features and APIs {#deprecated-17258}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Embedded Technologies {#embedded-tech-17258}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.66.0|[Oak API 1.66.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.66.0/index.html)| 
|AEM SLING API | 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.24-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.25.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
