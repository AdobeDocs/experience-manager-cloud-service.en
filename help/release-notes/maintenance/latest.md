---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 27293 {#release-27293}

Summarized below are the continuous improvements for maintenance release 27293, which was publicly released on July 28, 2026. The previous maintenance release was release 27083.

The 2026.8.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-27293}

* GRANITE-64872: Added support for asynchronous inclusion and dynamic enabling for OpenTelemetry tracing.
* GRANITE-67893: Added a configurable allow-list of trusted URI schemes for the Granite UI.

### Fixed Issues {#fixed-issues-27293}

* ASSETS-69193: Fixed a regression in the Adobe Stock integration (updated the stock-api library to 1.0.14).
* ASSETS-69340: Fixed captions disappearing on Dynamic Media videos after editing or adding a new language.
* GRANITE-63638: Fixed the unlocalized "Cannot reorder profiles that changed" message in Security > Edit User.
* GRANITE-67558: Fixed a `NullPointerException` in Felix Log on service-changed events.
* GRANITE-69183: Improved query performance when fetching aborted workflow tasks.
* GRANITE-69209: Fixed duplicate replication events when batch-replicating a parent and its descendants.
* SITES-47446: Fixed the rich text editor spell checker incorrectly flagging alphanumeric terms as misspelled.

#### AEM Guides {#guides-27293}

* GUIDES-45277: Topics fail to open in the Editor when accessed from Topic reports in Map Dashboard.
* GUIDES-46601: When a MathML equation is inserted as a `conref`, it does not render correctly.
* GUIDES-47085: Bulk asset processing incorrectly includes Content Fragment assets, causing error logs and failures in the processing reports.
* GUIDES-46480: A blank **Topic list** is displayed when a new baseline is used in the AEM Sites preset with composite component mapping.
* GUIDES-37940, GUIDES-20156: In Native PDF output, topic references marked with `toc="no"` attribute are still included in the TOC, resulting in a lengthy and cluttered table of contents.
* GUIDES-33420: In the Review UI, the tagging list displays all users in the review task, which makes it difficult to select the correct user in a comment or reply.

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Known Issues {#known-issues-27293}

None.

### Deprecated Features and APIs {#deprecated-27293}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-27293}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 10 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-27293}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.4.0 | [Oak 2.4.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.4.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.67 | [Apache Httpd 2.4.67](https://apache.googlesource.com/httpd/+/refs/tags/2.4.67/CHANGES)|
|Dispatcher|2.0.274||
|AEM Core Components| 2.32.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
|Java 21|21.0.11|[JDK 21.0.11](https://www.oracle.com/java/technologies/javase/21-0-11-relnotes.html)|
