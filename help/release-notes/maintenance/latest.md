---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: ed762d86-a04b-452b-a08f-86359bb8ff27
    internal-label: Configuration and operations
subfeature_v2:
  - id: c21ccc2b-e0c8-4853-bf41-f12259ed93f8
    internal-label: Release information
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 29643 {#release-29643}

Summarized below are the continuous improvements for maintenance release 29643, which was publicly released on November 19, 2026. The previous maintenance release was release 29251.

The 2026.12.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-29643}

* ASSETS-68902: Added tag ingestion and deletion using tag IDs.
* ASSETS-73640: Added a Chapters tab to asset details for the new video viewer.
* ASSETS-78871: Added video thumbnail creation at a specified time.
* ASSETS-81789: Added last-modified timestamps when BAM metadata is written back.
* SITES-51330: Added FAQ structured data generation with page and rollout controls.
* SITES-52301: Content API: page IDs and relationships for Experience Fragments.
* SKYOPS-166026: Improved XML processing compatibility with Java 21 defaults.

### Fixed Issues {#fixed-issues-29643}

* ASSETS-3355: Fixed Dynamic Media upload failures caused by HTTP connection errors.
* ASSETS-79244: Fixed link sharing failures for large asset folders.
* ASSETS-80111: Fixed failures saving metadata import results.
* ASSETS-82391: Fixed unhandled errors during asset rendition retrieval.
* GRANITE-72106: Fixed thread dump collection hanging on Java 25.
* SITES-53503: Fixed inability to tag content fragments using Manage Tags.

### Known Issues {#known-issues-29643}

None.

### Deprecated Features and APIs {#deprecated-29643}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-29643}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release includes 1 security fix, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-29643}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.8.0 | [Oak 2.8.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.8.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.67 | [Apache Httpd 2.4.67](https://apache.googlesource.com/httpd/+/refs/tags/2.4.67/CHANGES)|
|Dispatcher|2.0.275||
|AEM Core Components| 2.33.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
|Java 21|21.0.11|[JDK 21.0.11](https://www.oracle.com/java/technologies/javase/21-0-11-relnotes.html)|
