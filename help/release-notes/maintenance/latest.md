---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 21484 {#21484}

Summarized below are the continuous improvements for maintenance release 21484, which was publicly released on July 8, 2025. The previous maintenance release was release 21331.

The 2025.7.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-21484}

None.

### Fixed Issues {#fixed-issues-21484}

None.

#### AEM Guides {#guides-21484}

* GUIDES-29781: When an XML comment is added within an element in the Source view, the leading and trailing spaces around the comment are lost upon switching views.
* GUIDES-29078: When opening a topic in Author view after a browser refresh, previously applied tags in the File Properties panel are not retained, and adding new tags overwrites the existing ones, particularly when a large number of tags are available for selection.
* GUIDES-28214: Attempts to create review tasks through the AEM workflow consistently fail because the review node is not created.
* GUIDES-28104: Publishing a DITA map with `chunk=to-content` attribute creates duplicate JCR nodes in the new AEM Sites output, leading to redundant content structure in AEM Sites.
* GUIDES-29065, GUIDES-28793: Performance issues like longer loading times and intermittent timeouts are observed when working with large collections.

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Known Issues {#known-issues-21484}

None.

### Deprecated Features and APIs {#deprecated-21484}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-21484}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 5 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-21484}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.80.0|[Oak API 1.80.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.80.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.29.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
