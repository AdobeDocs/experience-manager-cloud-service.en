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

Summarized below are the continuous improvements for maintenance release X, which was publicly released on July X, 2024. The previous maintenance release was release 16799.

2024.7.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-X}

* SITES-22948: Remove commerce references in foundation content for AEM CS
* SITES-22142: Disable failing XFTranslateIT test
* SITES-22141: SNFE from CFM ModelChangeRepositoryImpl after OnRC
* SITES-22106: Language Switch Functionality Issue in New Content Fragment Editor
* SITES-22026: Unable to Move Experience Fragments Between Folders in AEM
* SITES-21954: Add examples in documentation
* SITES-21937: Investigate headless flaky test `FragmentVariationGetProcessorTest`
* SITES-21893: Image Cropping Issue on Author Instance
* SITES-21788: Display NOTE in CF and CF model editor when uiSchema is enabled for the model
* SITES-21688: MSM rollout does not update experience fragment (XF) path on live copy pages
* SITES-21659: Return full name of user creating/modifying/replicating a Model resource
* SITES-21619: Downgrade WARN message in PageImpl
* SITES-21609: [Implementation] OpenAPI endpoint to migrate content fragment(s) from one model to the other
* SITES-21598: Create CFM - return error if the given Configuration Path doesn't exist
* SITES-21491: [AUDI] CF PATCH endpoint should respect live relationships at field level
* SITES-21434: [AUDI] CF GET endpoint should respect live relationships at field level
* SITES-21415: CF Editor - support UUID references
* SITES-21326: Provide information about presence of references for a Content Fragment
* SITES-21310: Add id of Content Fragment in translations API response
* SITES-21265: [Schema] Get allowed content fragment models for a Fragment's folder
* SITES-21053: [cq-commons] Remove usages of Commons Collections 3
* SITES-21052: [Sites Headless] Remove usages of Commons Collections 3
* SITES-21040: [MSM][Async] Implement the code in WCM to use the newly refactored methods from granite async jobs
* SITES-20996: Refactor Search APIs
* SITES-20859: CF Open API - GET fragments by path (+ all references)
* SITES-20846: Optimise the number of repository reads
* SITES-20845: Logging consistency
* SITES-20844: Keep response codes consistent with the actual problem
* SITES-20841: Improve support for Problem Details meta types
* SITES-20687: Endpoint for batch processing status retrieval
* SITES-20657: [BE] Provide option to match whole word when replacing a string
* SITES-20587: Create `COPY` endpoint for Content Fragments
* SITES-20584: Optimise reference retrieval
* SITES-20308: Enable batch processing on API
* SITES-19976: [Open API] Generic UI schema for conditional fields
* SITES-19556:	Update uiSchema if exists when model is edited
* SITES-18056: When publishing a content fragment to Preview, include references
* SITES-16898: [Schema] OpenAPI endpoint to migrate content fragment(s) from one model to the other
* SITES-16609: List Launches endpoint
* SITES-16606: Create Launch Endpoint
* SITES-15914: [Best Buy] Preview and compare version doesn't work after moving experience fragments
* SITES-21617: [Xwalk] Make Page Properties/Metadata editable within UE
* SITES-19614: [Xwalk] Spreadsheet editor pagination and infinite scroll
* SITES-22163: [Xwalk] improved support for content served from publish tier for edge delivery sites
* SITES-22109: [Xwalk] improved handling of richtext markup post processing
* SITES-22035: [Xwalk] improved handling of MSM and Launches
* SITES-21839: [Xwalk] Improved path mapping and sanitisation for content not served by Edge Delivery

### Fixed Issues {#fixed-issues-X}

* SITES-22457: Promoting a launch which is not deep is not updating source content.
* SITES-22981: [Launch] Promoting a nested launch which is not deep is not publishing
* SITES-22748: Enhance error handling for Content Fragment Update Job
* SITES-22349: ContentType for empty multiline cf-elements cannot be changed
* SITES-22343: Semantic type "enumeration" is broken
* SITES-22194: [RELEASE BLOCKER] After setting the redirect, model.json doesn't work anymore
* SITES-21953: Etag gets changed based on ordering of the validationStatus
* SITES-21949: Search APIs invalid cursor returns 500
* SITES-21894: Enhance parent path validation when creating CFs
* SITES-21887: Invalid ETag returned by POST variations endpoint
* SITES-21657: Improve validation on CF Search Path property
* SITES-20927: The /adobe/sites/cf/fragments/search operation returns a 500 when the query is missing
* SITES-20544: xdmPublished event got triggered but content was not published
* SITES-19710: CVE-2022-47937 - Remove all usages of org.apache.sling.commons.json from Page Editor
* SITES-15951: Both tag processors throw exceptions during tests
* SITES-11992: [Accessibility] Annotation swatch selector button missing an accessible name
* SITES-10979: Label is not persistent.
* SITES-10962: Button: Button does not have a role.
* SITES-10906: State of active component lacks 3 to 1 contrast ratio.
* SITES-10905: State of active component lacks 3 to 1 contrast ratio.
* SITES-2974: Accessibility - Horizontal scrolling at 320px width.

### Known Issues {#known-issues-X}

None.

### Change Notice {#change-notice-X}

* Starting in September 2024, AEM as a Cloud Service will disable the serialization of Resource Resolvers via the Sling Model Exporter framework. See [the documentation](/help/implementing/developing/hybrid/disallow-the-serialization-of-resourceresolvers-via-sling-model-exporter.md) for more details.

### Deprecated Features and APIs {#deprecated-X}

To know what is deprecated or removed in AEM as a Cloud Service, see [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md).

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.64.0|[Oak API 1.64.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.64.0/index.html)| 
|AEM SLING API | 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.22-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.25.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
