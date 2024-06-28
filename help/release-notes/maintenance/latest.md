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
* SITES-22141: [Content Fragments] SegmentNotFoundException from CFM ModelChangeRepositoryImpl after OnRC
* SITES-21893: Image Cropping Issue on Author Instance
* SITES-21788: [Content Fragments] Display NOTE in CF and CF model editor when uiSchema is enabled for the model
* SITES-21688: MSM rollout does not update experience fragment (XF) path on live copy pages
* SITES-21659: Return full name of user creating/modifying/replicating a Model resource
* SITES-21609: OpenAPI endpoint to migrate content fragment(s) from one model to the other
* SITES-21598: [Open API] Create CFM - return error if the given Configuration Path doesn't exist
* SITES-21491: [Open API] CF PATCH endpoint should respect live relationships at field level
* SITES-21434: [Open API] CF GET endpoint should respect live relationships at field level
* SITES-21415: CF Editor - support UUID references
* SITES-21326: [Open API] Provide information about presence of references for a Content Fragment
* SITES-21310: [Open API] Add id of Content Fragment in translations API response
* SITES-20859: CF Open API - Return references when retrieving a fragment by path
* SITES-20687: [Open API] Endpoint for batch processing status retrieval
* SITES-20657: [Open API] Provide option to match whole word when replacing a string using `FindAndReplace` endpoint
* SITES-20587: [Open API] Create `COPY` endpoint for Content Fragments
* SITES-20584: [Open API] Optimise reference retrieval
* SITES-20308: [Open API] Enable batch processing on API
* SITES-19976: [Open API] Generic UI schema for conditional fields
* SITES-19556: [Content Fragments] Update uiSchema if exists when model is edited
* SITES-18056: [Open API] When publishing a content fragment to Preview, include references
* SITES-16898: [Schema] OpenAPI endpoint to migrate content fragment(s) from one model to the other
* SITES-16609: List Launches endpoint
* SITES-16606: Create Launch Endpoint
* SITES-21617: [Xwalk] Make Page Properties/Metadata editable within UE
* SITES-19614: [Xwalk] Spreadsheet editor pagination and infinite scroll
* SITES-22163: [Xwalk] Improved support for content served from publish tier for Edge Delivery Sites
* SITES-22109: [Xwalk] Improved handling of richtext markup post processing
* SITES-22035: [Xwalk] Improved handling of MSM and Launches
* SITES-21839: [Xwalk] Improved path mapping and sanitisation for content not served by Edge Delivery

### Fixed Issues {#fixed-issues-X}

* SITES-22457: Promoting a launch which is not deep is not updating source content.
* SITES-22748: [Content Fragments] Enhance error handling for Content Fragment Update Job
* SITES-22349: [Content Fragments] ContentType for empty multiline cf-elements cannot be changed
* SITES-22343: [Content Fragments] Semantic type "enumeration" is broken
* SITES-22194: After setting the redirect, model.json doesn't work anymore
* SITES-21953: [Open API] Etag gets changed based on ordering of the validationStatus
* SITES-21894: [Open API] Enhance parent path validation when creating CFs
* SITES-21887: [Open API] Invalid ETag returned by POST variations endpoint
* SITES-21657: [Open API] Improve validation on CF Search Path property
* SITES-21949: Search APIs invalid cursor returns 500
* SITES-20927: Search APIs return a 500 when the query is missing
* SITES-20544: [Open API] Change the generation of publish package names in order to avoid oak conflicts
* SITES-19710: CVE-2022-47937 - Remove all usages of org.apache.sling.commons.json from Page Editor
* SITES-11992: [Accessibility] Annotation swatch selector button missing an accessible name
* SITES-10979: [Accessibility] Label is not persistent.
* SITES-10962: [Accessibility] Button: Button does not have a role.
* SITES-10905: [Accessibility] State of active component lacks 3 to 1 contrast ratio.
* SITES-2974:  [Accessibility] - Horizontal scrolling at 320px width.
* SITES-22026: Unable to Move Experience Fragments Between Folders in AEM
* SITES-22106: Language Switch Functionality Issue in New Content Fragment Editor
* SITES-21980: Inconsistent handling for UUID-based reference types
* SITES-7257: NPE in ThumbnailServlet
* FORMS-14844: Adaptive Forms allow form submission despite failing reCAPTCHA verification.
* FORMS-14984: Forms with CAPTCHA skip validation if "submitMetaData" is absent in submitted data.
* FORMS-14477: The "Is After" and "Is Before" options in the rules editor malfunction in Date Picker validation.
* FORMS-14019: Rule editor's "Invoke Service" functionality is not working in Universal Editor.
* FORMS-14336: When no form field is selected, editor should open with focus on the entire form element.
* FORMS-15061: Loader circle persists indefinitely upon using invoke service option in the rule editor.
* CQ-4356898: outOfMemory error in CFEmbeddedPageUtil when one element of Content Fragment (CF) contains an unusually large number of URLs/links.
* CQ-4357055 : Auto translation issue using Rest API.
* CQ-4353931 : Add jcr:uuid in translation source page/xf/asset when it is missing.
* CQ-4357591 : Modify “Associate JCR:UUID” workflow to work for existing Pages/XF source and language copies.

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
