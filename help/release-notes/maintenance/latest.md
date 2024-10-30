---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release X {#X}

Summarized below are the continuous improvements for maintenance release X, which was publicly released on November 5, 2024. The previous maintenance release was release 18311.

The 2024.11.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-X}

* SITES-23591: Content Fragments: Content fragment upgrade for UUID support
* SITES-25440: Content Fragments: CFM Search API to show replication status
* SITES-24369: Content Fragments: OpenAPI documentation improvements
* SITES-25478: Content Fragments: Add back-end support for external asset references
* SITES-26119: Content Fragments: Add support of external asset references in reference type

### Fixed Issues {#fixed-issues-X}

* FORMS-14978: Enabling page load for a Core Component based form for theme editor
* FORMS-16596: Accessibility Issue: Disabled Buttons Not Recognized by Screen Reader
* SITES-10575: MSM: Blueprint Bloomfilter Loader tries to load >100,000 rows
* SITES-20755: Content Fragments: Asset reference with UUID refresh doesn't show the thumbnail
* SITES-26253: Content Fragments: UUID migration: Change sling job topic to be generic
* SITES-21338: Content Fragments: referencedBy endpoint does not return the correct page reference
* SITES-24421: Content Fragments: Edit CF endpoint does not work for CF retrieved via GET CF
* SITES-25461: Content Fragments: Filter by model in search for CFs should be case-insensitive
* SITES-25471: Content Fragments: Fix validation of global models in the ModelValidatorServlet
* SITES-25795: Content Fragments: CF Model API is failing when there is no cq date set
* SITES-25817: Content Fragments: Enhance promoteLaunch: update last promotion for CF Launches
* SITES-26030: Content Fragments: Endpoint /referencesTree doesn't return needed header
* SITES-26031: Content Fragments: Replication status not returned on CFM search endpoint
* SITES-26213: Content Fragments: Unpublish content fragments should only validate published references
* SITES-26226: Content Fragments: Start workflow issue when none of the given paths are usable
* SITES-26238: Content Fragments: The asset references returned by the API have a different order than the order from JCR
* SITES-25456: Events: When moving a page, a page-deleted event is generated besides the page-moved event
* SITES-25658: Events: The tier and sourceUrl are not populated in the page content state events
* SITES-6497: Launches: Create page in launch not working

### Known Issues {#known-issues-X}

### Deprecated Features and APIs {#deprecated-X}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-X}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 3 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.70.0|[Oak API 1.70.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.70.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.24-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.27.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
