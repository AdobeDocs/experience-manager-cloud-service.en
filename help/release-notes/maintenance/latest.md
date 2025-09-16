---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 22450 {#22450}

Summarized below are the continuous improvements for maintenance release 22450, which was publicly released on September 16, 2025. The previous maintenance release was release 22171.

The 2025.9.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-22450}

SITES-32595 Workflows that complete with skipped or rejected fragments can now be identified. A new property is available in the workflow API response, listing fragments that were excluded due to being invalid or having invalid references.
SITES-33642 A new API event is now produced and consumed for modified Content Fragments.
SITES-33320 It is now possible to search for a Content Fragment Model using its technicalName via the Search API.
SITES-34023 The technicalName field has been added to the responses of the Content Fragment Model endpoints for better identification.
SITES-32766 The Content Asset References in Content Fragment Models now support a wider range of binary file types.
SITES-33974 Improved OpenAPI documentation making it more accurate and user-friendly.
SITES-9173 Cache ContentPolicyStatus
SITES-9290 Improve caching of TouchEditContext
SITES-33355 Open new CF Editor on "View payload" in workflow console
SITES-33356 Open new CF Editor on Create CF → Open in TouchUI Admin UI
SITES-32952 Inconsistent handling of default values for CFM fields when using delivery API
SITES-31539 Edge Delivery with Universal Editor: Add support for Universal Editor configuration meta tags in head.html
SITES-20672 Edge Delivery with Universal Editor: Add support for additional bulk metadata spreadsheets in authoring
SITES-32963 Edge Delivery with Universal Editor: Add new experimentation metadata for optimization target, auto-allocate and self-learning
SITES-30847 Release Core Components 2.30.0

### Fixed Issues {#fixed-issues-22450}

SITES-25232 Set Date and Exit Timewarp links do not have a visible focus indicator
SITES-25258 Focus is not managed with Delete Annotation modal dialog
SITES-25305 The Demographic toolbar does not receive focus in a logical orde
SITES-25366 Loading state of teaser modal is not announced by the screen reader
SITES-34276 Edge Delivery with Universal Editor: fix automatically created CORS policy not applied on publish-tier
SITES-34811 Edge Delivery with Universal Editor: fix hlx selector not being added to links to spreadsheets in authoring
CQ-4360550 Fixed Unexpected Disappearance of Language Copy After Reverting Page Move in AEM Cloud Service
SITES-31669 Unlocalized strings 'This page redirects to' in Tools > Sites > Launches
SITES-30879 AEM: Unlocalized strings in Sites > Page Editor > Search component
SITES-30959 AEM: Unlocalized strings in Page Editor > Image component
SITES-21743 Unlocalized 'Please select a document to display.' string in Page Editor > PDF Viewer
SITES-19785 AEM: Strings is unlocalized in Core Components site > Tabs
SITES-22059 Unlocalized "File preview not available" string in Core Components site > PDF Viewer
SITES-33360 AEM: Unlocalized 'Error during operation. Provided path is not a launch' string in Launches > Edit
SITES-32975 Unlocalized date format in Headless UI > Launches > Compare Launch to Source
SITES-32973 Hardcoded strings in Headless UI > Launches > Rebase
SITES-13540 AEM: Unlocalized strings in Launches > Promotion
SITES-13085 AEM: Unlocalized error strings in Sites > Launch creation page
SITES-21499 AEM: Unlocalized string is Sites > Launches > Edit
SITES-14961 AEM: Truncation of date field in Sites >Properties > Blueprint > Rollout dialog
SITES-33764 Launch filters (Source Path / Workflow-created Launches) not working
SITES-33884 “Promote current page and sub pages” unintentionally promotes out-of-scope pages
SITES-33611 Live copy overview not working for high volume markets
SITES-34331 503 Timeout When Loading Rollout Overlay for Non-Admin Users
SITES-34403 NullPointerException in GraphqlClientImpl deactivate() during shutdown
SITES-33817 Resolved synchronization problems between the UI Schema and the JCR model to ensure consistency.
SITES-31141 Content references which are not represented by path are now correctly returned in the API response.
SITES-34080 The Content Fragment creation process is now more robust and will not fail if no fields are provided to the request.
SITES-30773 The regular expression for finding words using 'Find and Replace' has been improved to correctly match UTF-8 characters.
SITES-33742 Resolved a bug that prevented the successful moving of a Content Fragment when using the workflow API.

### Known Issues {#known-issues-22450}

None.

### Deprecated Features and APIs {#deprecated-22450}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-22450}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 18 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-22450}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.84.0|[Oak API 1.84.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.84/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.29.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
