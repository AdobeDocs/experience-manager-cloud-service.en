---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 21772 {#21772}

Summarized below are the continuous improvements for maintenance release 21772, which was publicly released on August 6, 2025. The previous maintenance release was release 21706.


The 2025.8.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.
### New Features  {#new-features-21772}
* SITES-30049  - Added new endpoint for retrieving the language copies of a Content Fragment by its UUID
### Enhancements {#enhancements-21772}

* SITES-33025 - Open new CF Editor via ID instead of path
* SITES-32741 - Trigger update of contenf-fragment page references asynchronously
* SITES-32087 - GraphQL: Add support for _ignoreCase on StringArray
* SITES-31791 - Upgrade graphql-java library to 24.0
* SITES-12211 - Improved Performance in template editor
* SITES-32861  Create Live Copy Chunked 
  - Performance improvement for live copy creation through chunked processing
* SITES-21383 - Improve performance when deleting large CF launches
  - Performance optimization for Content Fragment launch deletion operations
* SITES-31165 - Split the Rollout Job in multiple Chunks
  - Performance enhancement by splitting rollout operations into manageable chunks
* SITES-21353 - [Launches4CFs] use index for CF queries
  - Query performance improvement for Content Fragment launches using database indexing
* SITES-30495 - CF Launch create / edit sources: support fragment reference UUID
  - Enhancement to support UUID-based fragment references in Content Fragment launches
* SITES-32151 - cq:isContainer exposed
  - API enhancement exposing container property functionality
* SITES-26849 - Adjust back-references when a Content Fragment Variation si moved or deleted.
* SITES-31846 - Add option to copy/paste root fragment and references in the same folder for copy tree operation.
* SITES-30241 - Adjust References located inside a long text field when moving, renaming or deleting a fragment.
* SITES-32684 - Enhance mechanism for syncing tab changes in UI schema.
* SITES-33308 - Add retry mechanism for syncing changes to the UI Schema when editing models.
* SITES-32247: [SLA3] AEM "Text and Personalization" Component – Missing Dialog Personalization & UI Misalignment - https://jira.corp.adobe.com/browse/SITES-32247
* SITES-32261: [SLA3] Experience Fragment i18n Not Applied to Field - https://jira.corp.adobe.com/browse/SITES-32261
* SITES-32666: Template Predicate contains \n causing HTML lookup to fail - https://jira.corp.adobe.com/browse/SITES-32666
* SITES-32674: [SLA3] Featured Image Field Image Picker not working for Page Creation Wizard Despite cq:showOnCreate - https://jira.corp.adobe.com/browse/SITES-32674           

### Fixed Issues {#fixed-issues-21772}

* SITES-31992 - GraphQL: Fix sporadical errors in model scan during bundles startup
* SITES-29967 - GraphiQL: Long query names are cut off
* SITES-26266 - Content references that don't start with / are not returned from BE response (Java API)
* SITES-17874 - GraphQL persisted queries: Fix encoding for content-type application/graphql-response+json
* SITES-24506 Screen readers informed on search results
* SITES-25268 Screen reader improvements for annotations
* SITES-32366 Spell Check results hidden behind RTE dialog
* SITES-32829 MediaQuery emulator improvements to parse media query level 3 and 4 
* SITES-32278 Tag fields fixed to use field label correctly
* SITES-25244 Horizontal bar not appearing in image modal anymore
* SITES-33395 - Rollout button disabled for Content Fragment Live-Copy sync via References rail
  - Fixed rollout button functionality for Content Fragment live copy synchronization
* SITES-33147 - PredicateProvider not bound to LiveRelationshipServlet
  - Fixed service binding issue affecting live relationship functionality
* SITES-33528 - Comment timestamps reset to launch promotion time after Launch promotion
  - Fixed timestamp preservation issue during launch promotion
* SITES-33556 - Fix bug introduced by SITES-31178
  - Regression fix for issues introduced in previous enhancement
* SITES-31178 - (Referenced in SITES-33556 fix)
  - Original issue that required subsequent bug fix
* SITES-33014 - Excessive WARN logs from LaunchesAdapterFactory fix
  - Fixed excessive warning log generation from LaunchesAdapterFactory
* SITES-32305 - Live Copy Inheritance Break Fails After Layout
  - Fixed live copy inheritance break functionality after layout changes
* SITES-32268 - Disable URL encoding for Content Fragment Search.
* SITES-32772  - Property locked in variation's fields was always false when enabling the enhancements from SITES-31455 - related to unifying etag value.
* SITES-32696 - Fixed issue when a Content Fragment Live Copy field with broken inheritance couldn't not be edited anymore.
* SITES-33453
* SITES-31712: [SLA3] Slow Queries from the Omni-search on prod Author - https://jira.corp.adobe.com/browse/SITES-31712
* SITES-33039: Page Events not triggering correctly - https://jira.corp.adobe.com/browse/SITES-33039
* SITES-32931: wcm mobile code is readable by everyone - https://jira.corp.adobe.com/browse/SITES-32931
* SITES-31192: Experience Fragments losing Version History after being moved - https://jira.corp.adobe.com/browse/SITES-31192
* SITES-33529: [SLA4] AEMaaCS-ACS integration returns 503 (invalid JSON) – Error while linking the ACS Campaign templates with AEM pages https://jira.corp.adobe.com/browse/SITES-33529
* SITES-33468: [AEM] AEMaaCS unable to connect to ACS - https://jira.corp.adobe.com/browse/SITES-33468      

### Altered functionality {#altered-functionality-21772}
* SITES-26344 - Unify validation of fragmentId / modelId between endpoints - these ids are now validated and a 400 status code is returned if they are not valid.
* SITES-29598 - Validate Content Fragment references added in fragment reference fields when updating a Content Fragment Model.

### Tasks {#tasks-21772}
* SITES-30887: [TouchUI] Add Contet Fragment uuids stored in workflow metadata - https://jira.corp.adobe.com/browse/SITES-30887
* SITES-33678: Add Toggle for SITES-33529 - https://jira.corp.adobe.com/browse/SITES-33678
  
### Known Issues {#known-issues-21772}

None.

### Deprecated Features and APIs {#deprecated-21772}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-21772}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 12 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-21772}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.80.0|[Oak API 1.80.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.80/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.63 | [Apache Httpd 2.4.63](https://github.com/apache/httpd/blob/2.4.63/CHANGES)|
|AEM Core Components| 2.29.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
