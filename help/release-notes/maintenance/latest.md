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
* SITES-31472 - Delete Launch can cause the repository to pause if the launch is massive
* SITES-32175 - Allow intermediary commits for both Live Copy creation and MSM Page rollout
* SITES-28683 - Allow MSM LiveRelationship searches to skip advanced status
* SITES-10575 - "MSM Blueprint Bloomfilter Loader" tries to load >100000 rows
* SITES-14542 - Renaming/moving a live copy source page should trigger publishing the renamed/moved live copy page in case it was perviously published
* SITES-31005 - Enhance Rollout Job UI to show the progress
* SITES-31020 - Enhance Create Live Copy Job UI to show the progress
* SITES-25976 - Links inside Experience Fragments not adapting after MSM rollout
* SITES-23499 - Edge Delivery with Universal Editor: Add support for multiple fields to be used for block options
* SITES-30328 - Edge Delivery with Universal Editor: Add support to preview from Sidekick
* SITES-19754 - Edge Delivery with Universal Editor: Add human readable error message when the integration has issues
* SITES-27792 - Edge Delivery with Universal Editor: Add dedicated Edge Delivery Service Configuration template
* SITES-23518 - Edge Delivery with Universal Editor: Add support for Edge Delivery specific asset renditions
* SITES-27782 - Edge Delivery with Universal Editor: Add specific publisher-subscriber implementation to publish content to Edge Delivery (early access)
* FORMS-19336 - Search added in Data Source Tree in AF editor 
* FORMS-19125 - Support Auto Fragment Mapping in AF editor
* FORMS-19417 - Support of radio buttons in Hierarchy View
* FORMS-16458 - UI for choosing font properties(typeface)
* FORMS-19603 - Support master page and desgin page both in Rule-editor
* FORMS-17707 - AEP connector doesn't work for AEP platform stage
* SITES-31677 - Custom workspace support AEM Content fragment export to Target

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
* SITES-31272 - Not able to create Assets language copy via PageManager.copy
* SITES-30947 - Null pointer exception due to missing "behavior" property on blueprint during rollout
* SITES-31387 - JavaScript error "ns.ui.alert is not a function" when re-enabling ghost component inheritance
* SITES-29075 - Live copy overview not working for high volume websites
* SITES-32095 - Auto-Refresh Fails on afterchilddelete Event Listener in Live Copy
* SITES-30877 - Incorrect Child Page Rollout Status
* SITES-30899 - Rollout “Later” option allows continuing with no date selected
* SITES-30386 - Edge Delivery with Universal Editor: Remove duplicated, legact UE cors.js
* SITES-25433 - Edge Delivery with Universal Editor: Fix rendering of page versions for multi-language site structures
* SITES-29514 - Edge Delivery with Universal Editor: Make GitHub / Project URL mandatory when creating a new site
* SITES-31621 - Edge Delivery with Universal Editor: Remove empty row from Spreadsheets that are live copies
* SITES-32237 - Edge Delivery with Universal Editor: Fix rendering of empty / malformed text components
* SITES-30377 - Edge Delivery with Universal Editor: Sanitize org- and sitenames
* SITES-30695 - Edge Delivery with Universal Editor: Increase ranking of rewriter pipeline to not interfere with custom code
* FORMS-19628 - In Auto Generated DOR, excluding nested panel title also hides root panel title
* FORMS-18526 - When rule with multiple fields in conditions is copied, fixed field does not change
* FORMS-18977 - DOR service is not passing Title of the Document
* FORMS-19651 - Fix rule when button clicked is used in binary condition and also same button is used in then statement
* FORMS-19808 - FormsPortal - Drafts cannot be pulled when lazy loading is enabled
* FORMS-19887 - Access property not working in HTML5 Preview
* FORMS-13990 - Forms Service APIs: Document Generation : data field when left empty after being selected gives 200 when expected is 400  
* FORMS-14309 - Forms Service APIs : Extract data Response Code Rectification
* FORMS-19047 - Translations Missing After Publishing an Adaptive Form on AEM Forms on SP22
* FORMS-19234 - Unable to use timeline feature of PDFs in AEM forms
* CQ-4359866 - LanguageUtils class now support unit test without adding additional dependency
* CQ-4359826 - Resolves inconsistent status in the content fragment reference panel
* CQ-4359756 - Translation Rules now includes filter properties at component level
* SITES-31467 - js-errors from contexthub.authoring-hook.js in the page editor
* SITES-24708 - Filters Rail functionality breaks when zoom is increased to 400%
* SITES-24668 - References Rail functionality breaks when zoom is increased to 400%
* SITES-25235 - Filter Rail content loading message is not announced by screen reader
* SITES-24492 - ARIA tablist has no accessible name
* SITES-24678 - References Rail status message is not announced by screen reader
* SITES-25254 - Horizontal scroll bar appears in Carousel Modal when content is when viewed at 320px
* SITES-30660 - ADA Compliance Issue with Custom AEM Component
* SITES-26890 - While using Keyboard, Scope "Table headers" keyboard focus is not visible in Manage Publication page


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
