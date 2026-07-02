---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 26908 {#release-26908}

Summarized below are the continuous improvements for maintenance release 26908, which was publicly released on July 2, 2026. The previous maintenance release was release 26773.

The 2026.7.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-26908}

* ASSETS-52412: Added ability to re-run or duplicate existing Asset Reports.
* ASSETS-62263: Introduced AI-generated captions in Dynamic Media with OpenAPI.
* ASSETS-62482: Updated Adobe Stock integration with latest improvements.
* ASSETS-63388: Added HEAD operation support to Tags OpenAPI.
* ASSETS-63652: Updated asset search to exclude Content Fragments.
* ASSETS-63743: Added Tag ID migration service for UUID-based identifiers.
* ASSETS-64240: Added signing and watermarking support via CAFE API v2.
* ASSETS-64282: Added projected fields for selective metadata in API responses.
* ASSETS-64979: Updated TagManager to auto-populate UUID on new tags.
* ASSETS-65069: Extended Asset Preprocessing API for async Sling Job actions.
* ASSETS-65492: Added folder API enhancements with improved metadata and query support.
* ASSETS-65525: Improved upload info API for request bodies larger than 1 MB.
* ASSETS-65603: Improved folder listing performance via optimized asset count queries.
* ASSETS-65678: Added Frame.io CORS origins to AEM Author configuration.
* ASSETS-65746: Added overwrite parameter support to Assets Move API.
* ASSETS-65889: Added Assets Rename PATCH API for programmatic renaming.
* ASSETS-66032: Added advanced networking proxy support in Assets Bulk Import.
* ASSETS-66196: Updated Publish API job polling and status responses.
* ASSETS-66643: Improved tag lookup performance via UUID-based priority.
* ASSETS-67109: Added prompt group support for AI generation prompts.
* ASSETS-67517: Added AEM-to-CAI metadata sync via PATCH API.
* ASSETS-67525: Added new OpenAPI-based Metadata API implementation.
* ASSETS-67667: Added new OpenAPI-based Asset Metadata Schema API implementation.
* ASSETS-68173: Renamed Feature Check API to Operations API.
* ASSETS-68261: Improved Adobe Stock search landing page.
* ASSETS-68446: Added Video Transcript Service API for Dynamic Media.
* ASSETS-68981: Updated partial asset PATCH behavior in DAM Assets API.
* ASSETS-69129: Added IMS client configurations for Frame.io native integration.
* ASSETS-69156: Added SEO metadata support to Dynamic Media component.
* ASSETS-69214: Introduced Custom Thumbnail support in Polaris asset viewer.
* ASSETS-70416: Added Origin header to eventing allow-list.
* CQ-4363466: Added Context-aware config path resolution for GenAI connectors.
* SITES-42076: Added bulk operations support for AEM Sites pages.
* SITES-42835: Added Content API support for AEM Forms outside the feature toggle.

### Fixed Issues {#fixed-issues-26908}

* ASSETS-36208: Fixed image profile missing in folder properties when DM is disabled.
* ASSETS-61087: Fixed Smart Crop count mismatch and wrong renditions on download.
* ASSETS-63240: Fixed multi-select Relate leaving users on blank metadata editor.
* ASSETS-65076: Fixed incorrect URL scheme causing wrong external URLs.
* ASSETS-65670: Fixed asset ID prefix in C2PA content credentials manifest.
* ASSETS-65932: Fixed missing CSV header in Bulk Operations audit download.
* ASSETS-66149: Fixed trailing slash handling in Folder API.
* ASSETS-66226: Fixed case-sensitive status check causing approved/preview asset deletion to fail.
* ASSETS-66669: Fixed Home button not navigating back to start screen in search.
* ASSETS-66711: Fixed bodyIncluded/contentLength for non-body HTTP methods.
* ASSETS-67113: Fixed Bulk Import ignoring SVG files (0 assets imported).
* ASSETS-67836: Fixed missing bidirectional reference links for ingredient assets.
* ASSETS-68098: Fixed metadata lost on Save and Close with Unified Shell enabled.
* ASSETS-68240: Fixed C2PA manifest rendition not displaying in Asset View.
* ASSETS-68283: Fixed missing Play/Pause tooltip in DM VideoViewer (WCAG 2.1.1).
* ASSETS-69186: Fixed Adobe Stock search empty results for high-volume keywords.
* ASSETS-69662: Fixed subsequent asset edits not applying after first edit.
* ASSETS-69920: Removed outdated folder limit warning from Bulk Import dry run.
* SITES-44265: Added stable content-page-id to resolve search-optimizer 404s.

#### AEM Guides {#guides-26908}

* GUIDES-47432: Switching between Source and Author modes causes content inconsistencies, with portions of the topic disappearing or not being reflected across modes.
* GUIDES-48319: When working with Track changes, rejecting an Imported text insertion removes all content within the tag instead of only rejecting the specific inserted content.

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Known Issues {#known-issues-26908}

None.

### Deprecated Features and APIs {#deprecated-26908}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-26908}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 22 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-26908}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.2.0 | [Oak 2.2.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.2.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.67 | [Apache Httpd 2.4.67](https://apache.googlesource.com/httpd/+/refs/tags/2.4.67/CHANGES)|
|Dispatcher|2.0.274||
|AEM Core Components| 2.31.2|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
|Java 21|21.0.11|[JDK 21.0.11](https://www.oracle.com/java/technologies/javase/21-0-11-relnotes.html)|
