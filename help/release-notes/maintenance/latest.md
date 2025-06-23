---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 21331 {#21331}

Summarized below are the continuous improvements for maintenance release 21331, which was publicly released on June 24, 2025. The previous maintenance release was release 21193.

The 2025.7.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-21331}

* SITES-27775 - Optimized reference search during publication (metadata lazy loading)
* SITES-30885 - Optimized JSON processing in persisted queries
* SITES-27486 - Universal Editor - AEM Integration

### Fixed Issues {#fixed-issues-21331}

* SITES-30752 - Do not use `If-modified-since`/`last-modified` headers when generating persisted query response.
* SITES-30353 - GraphQL DataFetchingExceptions for “src” Field in AEM Content Fragments
* SITES-30333 - Read asset metadata from jcr to avoid xmp parsing problems
* SITES-30140 - Dual window issue when creating content fragment reference
* SITES-29748 - Correct renderconditions to show managepublication/quickpublish actions inside the CF editor
* SITES-15452 - Unique CF elements should not be checked against their copies in the launch
* SITES-31987 - Do not show previewURLs for Content Fragments when publishing them to Preview
* SITES-30727 - Unable to Drag and Drop Components on Production Author Editor
* SITES-30871 - DOM Updates after the afteredit listener is triggered
* SITES-30634 - RTE Image Alt Text & Alignment Not Working Consistently
* SITES-31676 - Authoring or Deleting components leaves a blank space at the bottom of the Page
* SITES-31857 - CF creation fails in folders with single quotes
* SITES-24697 - Loading state of Image model is not announced by the screen reader

### Known Issues {#known-issues-21331}

None.

### Deprecated Features and APIs {#deprecated-21331}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-21331}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 21 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-21331}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.80.0|[Oak API 1.80.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.80.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.29.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
