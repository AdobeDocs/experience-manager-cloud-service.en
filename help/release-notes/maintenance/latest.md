---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release X {#release-X}

Summarized below are the continuous improvements for maintenance release X, which was publicly released on September 9, 2026. The previous maintenance release was release 27830.

The 2026.9.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-X}

None.

### Fixed Issues {#fixed-issues-X}

None.

#### AEM Guides {#guides-X}

* GUIDES-48304: On low-resolution screens, the Insert Keyword dialog fails to appear when inserting a keyword from the toolbar, while it opens as expected when using **More** option.
* GUIDES-48893: Opening the Review panel or applying a project filter takes some time to load the task list.
* GUIDES-49065: The asset status API does not return the correct status for assets whose path contains a comma.
* GUIDES-49325: When you generate AEM Sites (with composite component mapping) output with a baseline targeting an older version, the page content correctly shows that older version, but the page metadata shows the current version instead.
* GUIDES-51759: Starting a translation using an XLIFF project creates an empty project that never moves to an in-progress state.
* GUIDES-52343: When a new learning topic is created using a HTML or learning template with a custom header, the topic title doesn’t appear in the custom header 
* GUIDES-52690: A preset’s saved baseline selection incorrectly displays as *No Baseline* after the baseline is deleted or while a dynamic baseline is still being created.
* GUIDES-52916: Copying a table from Author mode and pasting it into Author mode removes attributes such as `colwidth` and any other attributes defined on `colspec`, causing the column width settings to be lost.

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Known Issues {#known-issues-X}

None.

### Deprecated Features and APIs {#deprecated-X}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-X}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses X identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.4.0 | [Oak 2.4.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.4.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.67 | [Apache Httpd 2.4.67](https://apache.googlesource.com/httpd/+/refs/tags/2.4.67/CHANGES)|
|Dispatcher|2.0.275||
|AEM Core Components| 2.32.6|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
|Java 21|21.0.11|[JDK 21.0.11](https://www.oracle.com/java/technologies/javase/21-0-11-relnotes.html)|
