---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 19149 {#19149}

Summarized below are the continuous improvements for maintenance release 19149, which was publicly released on January 21, 2025. The previous maintenance release was release 18751.

The 2025.1.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-19149}

* ASSETS-45286 - Show granular progress for download archiving async job
* ASSETS-46296 - Support for Dynamic Media Templates in Asset Selector
* ASSETS-44796 - Fire Assets Events for DAM async assets jobs

### Fixed Issues {#fixed-issues-19149}
* GRANITE-55074 - Ensure CORS response headers are set on error respones
* ASSETS-43755 - Scalability improvements to bulk asset relate
* ASSETS-45399 - Redirect to Assets Console after creating Asset live-copy
* ASSETS-45462 - Browser caching issues with custom folder thumbnails
* ASSETS-46398 - Hide Download and reprocess actions for DM Templates
* ASSETS-44484 - Issues re-saving Connected Assets configuration
* ASSETS-44122 - Async copy assets job does not rename the destination folder when copying to the current folder
* ASSETS-44463 - Download CSV button not visible on successful metadata export
* ASSETS-45134 - Move job with destination title overrides all folder titles
* ASSETS-45137 - Conflicts with bulk uploads through Assets View
* ASSETS-45758 - Asset Relations gets infinite busy/loading animation after adding a relation
* ASSETS-44148 - NODE_MOVED event in AEM can cause spurious NPE in logs
* ASSETS-28607 - JS error when setting custom video thumbnail
* ASSETS-45979 - DM Template Asset renditions are not generated sometimes
* GRANITE-55781 -  Improve group synchronization between Adobe Developer Console and AEM. More details in [Changes in User Group and Product Profile Synchronization](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/changes-in-user-group-and-product-profile-synchronization)
* GRANITE-55754 - Ensure SDK startup scripts support Java 21
* GRANITE-54248 - Unable to scroll through all items in large assets folder
* SCRNS-4597 - Search result list view improvements


### Known Issues {#known-issues-19149}

None.

### Deprecated Features and APIs {#deprecated-19149}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-19149}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses X identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-19149}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.72.0|[Oak API 1.72.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.72.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.24-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.27.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
