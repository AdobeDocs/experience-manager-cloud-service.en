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

## Release X {#release-X}

Summarized below are the continuous improvements for maintenance release X, which was publicly released on November 2, 2026. The previous maintenance release was release 29023.

The 2026.11.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.


### Enhancements {#enhancements-X}

None.

### Fixed Issues {#fixed-issues-X}

None.

#### AEM Guides {#guides-X}

* GUIDES-49847: When a table is pasted from Microsoft Word, the header row cells are created, but their content is lost.
* GUIDES-56812: When the unified shell is enabled, the Adobe Experience Manager Guides header also appears in the Editor and the Map console.
* GUIDES-28877: In a bookmap, when a `booktitle` element contains multiple sub-elements, such as `booklibrary` and `mainbooktitle`, extra whitespace is added between their values in the `dc:title` metadata.
* GUIDES-54591: In the Map console, after output is generated for one map, the **Generate** button is disabled when another map is opened. Refreshing the browser enables the button again.
* GUIDES-45396: On the Translation page, searching and sorting by **Title** use the localized metadata value instead of the title displayed in the column.
* GUIDES-35125: On the **Reviewers** page, when creating or editing a review task, the **Clear Selection**, **Add Reviewers**, **Remove Reviewers**, and **Re-assign Reviewers** buttons are enabled by default, even when no rows are selected.
* GUIDES-56101: Generating a SCORM output for a large course, typically 300 MB to 600 MB, takes more than 30 minutes and fails without error details in the logs.

This is a selected list of issues fixed in this release. For complete information about the new and enhanced features and issues fixed in this release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Known Issues {#known-issues-X}

None.

### Deprecated Features and APIs {#deprecated-X}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-X}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release includes X security fixes, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.6.0 | [Oak 2.6.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.6.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.67 | [Apache Httpd 2.4.67](https://apache.googlesource.com/httpd/+/refs/tags/2.4.67/CHANGES)|
|Dispatcher|2.0.275||
|AEM Core Components| 2.33.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
|Java 21|21.0.11|[JDK 21.0.11](https://www.oracle.com/java/technologies/javase/21-0-11-relnotes.html)|
