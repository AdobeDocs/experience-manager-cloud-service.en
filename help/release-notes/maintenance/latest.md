---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 13665 {#release-13665}

Summarized below are the continuous improvements for maintenance release 13665, which was publicly released on September 12th, 2023. This maintenance release replaces release 13420.

2023.9.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-13665}

* Various improvements in the Content Fragment APIs
* ASSETS-26713: Assets Dashboard: New Experience UI Dashboard now reachable from Touch UI
* SITES-11206: Content Fragments: Search API for Content Fragments
* SITES-11262: Content Fragments: Button to switch to the new Content Fragment Editor
* SITES-15447: Core Components: Release of version 2.23.4

### Fixed Issues {#fixed-issues-13665}

* Various vulnerability-related updates
* Various translation-related updates
* CQ-4354428: Workflows: Unable to complete a task in Inbox
* FORMS-10248: Rule Editor: Unable to set value of Radio button/Checkbox when data value type is boolean in AFv2
* SITES-8590: Content Fragments: Encoding issues with variables in persisted queries
* SITES-9733: Content Fragments: Asset References in content fragment reference panel shows 0(zero) references
* SITES-14561: Content Fragments: Fixed and improved HTML to Markup conversion
* SITES-14882: Content Fragments: Once we edit Content Fragment and close the tab without clicking on save or close button, the values are getting stored
* SITES-14800: Content Fragments: Exception in persisted GraphQL queries with variables
* SITES-14451: Core Components: Fixed missing dependency
* SITES-15202: Core Components: Fixed missing dependency
* SITES-14773: Experience Fragments: Link Reference does not get updated inside experience fragment
* SITES-14899: Experience Fragments: Multiple offers created for XF variations in Target
* SITES-15267: Launches: Promotion does not pick up launch pages modified before time of modifying the launch configuration
* SITES-15406: Launches: Unable to add a Launch Page
* SITES-15427: Launches: Inconsistent behavior of "Promote current page and sub pages" scope
* SITES-15429: Launches: Authoring pages deleted while promoting launches
* SITES-15462: Launches: Auto promotion process publishes pages out of promotion scope
* SITES-15815: Launches: Deleted Page from Launch causes Launch to not Promote Successfully
* SITES-15223: Page Editor: Not able to resize components whin in tablet size emulator
* SITES-15463: Page Templates: Templates cannot be published

### Known Issues {#known-issues-13665}

None

### Embedded Technologies {#embedded-tech-13665}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.54-T20230817132355-3800a65|[Oak API 1.54.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.54.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
