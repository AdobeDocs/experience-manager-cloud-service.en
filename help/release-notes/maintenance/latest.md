---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 21193 {#21193}

Summarized below are the continuous improvements for maintenance release 21193, which was publicly released on June 10, 2025. The previous maintenance release was release 21005.

The 2025.6.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-21193}

* ASSETS-51245: Improved performance for large folder listings in Touch UI.
* CQ-4360131: Improved error response for OpenAPI endpoints allowing API clients to receive correct structured error information.
* ASSETS-51686: Improvements to bulk operations job, including easier job cancellation, enhanced logging, audit downloads for large results

### Fixed Issues {#fixed-issues-21193}

* ASSETS-41007: Deleted assets could remain showing in Content Hub.
* ASSETS-50994: AemRequestEventFilter causing excessive Jetty thread contention.
* ASSETS-50155: Fix duplicate autogen events.
* ASSETS-50716: Sorting by Title in Assets List view did not work as expected.
* ASSETS-50820: Ensure invalid requests to the asset relations API are properly rejected with a 400 error
* ASSETS-50562: Updated the Asset Upload API so that versioning is now the default behavior on name conflict.
* ASSETS-50992: Assets API initiateUpload.json endpoint was returning a Content-Type of text/plain instead of application/json.
* ASSETS-51322: Automatic removal and expiration of async barricades that remain persisted indefinitely after a failed job.
* ASSETS-51809: Fixed an issue in Admin View where the CSV editor did not show recently saved changes due to browser caching.
* SITES-31678: Experience Fragments (XF) with context-aware references did not resolve the correct language root in XF Publishing API.

### Known Issues {#known-issues-21193}

None.

### Deprecated Features and APIs {#deprecated-21193}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-21193}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 2 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-21193}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.80.0|[Oak API 1.80.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.80.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.29.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
