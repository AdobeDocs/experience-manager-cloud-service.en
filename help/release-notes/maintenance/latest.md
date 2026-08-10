---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 27550 {#release-27550}

Summarized below are the continuous improvements for maintenance release 27550, which was publicly released on August 10, 2026. The previous maintenance release was release 27293.

The 2026.8.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-27550}

* AEMARCH-328: Exposed a default 404 message constant in the OpenAPI support layer.
* ASSETS-52544: Introduced countdown timer support in Dynamic Media templates for Open Time Personalization.
* ASSETS-52644: Introduced conversion of PSD designs to Dynamic Media templates.
* ASSETS-60359: Introduced the Tagging API.
* ASSETS-63722: Added a Folders Copy API.
* ASSETS-64376: Added PATCH support to the Task API.
* ASSETS-64760: Added asset download/archive support on the author tier.
* ASSETS-64763: Added download job status endpoints.
* ASSETS-67409: Improved bulk re-approval with direct queue injection and skip-event marker.
* ASSETS-67662: Added event production for Touch UI metadata update, deletion, and sync actions.
* ASSETS-67664: Refactored search to be reusable across folders, tasks, and collections.
* ASSETS-68862: Added an endpoint to assign a license to an asset.
* ASSETS-69203: Added async bulk folder creation to the OpenAPI.
* ASSETS-69206: Added bulk tag creation with async job support to the OpenAPI.
* ASSETS-69581: Added Collections Bundle implementation, phase 2.
* ASSETS-70289: Added SEO support for embed codes.
* ASSETS-70312: Renamed search API parameter allowUnsafeSearch to allowUnindexedSearch (now optional).
* ASSETS-70431: Added Collections Bundle implementation, phase 2.
* ASSETS-71036: Improved AI processing to trigger correctly for a limited set of file types.
* ASSETS-71442: Updated Folder API command result message format.
* ASSETS-72401: Added support for metadata-only versioning of assets.
* ASSETS-74731: Migrated Asset Insights to Analytics 2.0 with IMS OAuth.
* ASSETS-74799: Updated Asset Metadata Schema API implementation.
* ASSETS-75096: Improved Asset Metadata API to exclude non-file assets from responses.
* ASSETS-75278: Added support for early activation in non-GenStudio environments.
* CQ-4364085: Updated AEM CS Translation Kit.
* CQ-4364138: Updated AEM CS Translation Kit.
* SITES-39116: Added ability to expose metadata schema on the GET fragment endpoint via Assets OpenAPI.
* SITES-47432: Improved performance of the BFF List Folders API query.
* SITES-49250: Added per-component marker filter support for headless components on author.

### Fixed Issues {#fixed-issues-27550}

* ASSETS-52795: Fixed asset UUID not being retained when an asset is replaced.
* ASSETS-62661: Fixed WebP renditions showing generic size labels instead of configured processing profile names.
* ASSETS-64116: Fixed inability to delete static renditions for PDF/PPTX documents.
* ASSETS-64682: Fixed assets incorrectly showing "PublishIncomplete" status with shorter polling durations.
* ASSETS-66372: Fixed inability to update thumbnails on existing Collections.
* ASSETS-67068: Fixed Bulk Import Admin UI "Dry Run" showing "undefined" statistics.
* ASSETS-68644: Fixed unbounded recursive folder traversal hanging the Timeline Rail workflow.
* ASSETS-70137: Fixed Created Date relative filter failing when notNullCheckEnabled is true.
* ASSETS-70192: Fixed Saved Searches in AEM Assets not applying filters until page refresh.
* ASSETS-70217: Fixed "Internal Error occurred while saving the form" when adding/editing content.
* ASSETS-70998: Fixed missing pagination and exact-match group display in the Assets Permissions Picker.
* ASSETS-73365: Fixed missing "Required" indicator when one dropdown sets multiple mandatory fields.
* ASSETS-74286: Fixed captions stuck in "Processing" for up to an hour after generation.
* ASSETS-74870: Fixed duplicate "Change Thumbnail" tabs shown when both DMS7 and Polaris are enabled.
* ASSETS-74915: Fixed report wizard failures on very slow network connections.
* ASSETS-75767: Fixed asset processing failures caused by broken event handler registration.
* SITES-48494: Fixed incorrect minimum length validation on model metadata (regression rollback).

### Known Issues {#known-issues-27550}

None.

### Deprecated Features and APIs {#deprecated-27550}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-27550}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 2 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-27550}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.4.0 | [Oak 2.4.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.4.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.67 | [Apache Httpd 2.4.67](https://apache.googlesource.com/httpd/+/refs/tags/2.4.67/CHANGES)|
|Dispatcher|2.0.274||
|AEM Core Components| 2.32.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
|Java 21|21.0.11|[JDK 21.0.11](https://www.oracle.com/java/technologies/javase/21-0-11-relnotes.html)|
