---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 18751 {#18751}

Summarized below are the continuous improvements for maintenance release 18751, which was publicly released on December 11, 2024. The previous maintenance release was release 18459.

The 2025.1.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-18751}

None.

### Fixed Issues {#fixed-issues-18751}

* GUIDES-20006: Document state marked as Done reverts back to Draft before saving a new version, resulting in the Done state not persisting in any document versions.
* GUIDES-21840: In the Native PDF output, chapter titles are missing from the TOC, leading to an incorrect hierarchy.
* GUIDES-19558: Editing and then saving a baseline on a cloud setup timesout after 1 minute if the baseline has large number of topics or maps.
* GUIDES-19733: Map translation using baseline becomes slow and eventually fails to load the list of all the associated topics and maps files.

For more information about the new and enhanced features and issues fixed in Experience Manager Guides, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap).

### Known Issues {#known-issues-18751}

None.

### Deprecated Features and APIs {#deprecated-18751}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-18751}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 3 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-18751}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.72.0|[Oak API 1.72.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.72.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.24-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.27.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
