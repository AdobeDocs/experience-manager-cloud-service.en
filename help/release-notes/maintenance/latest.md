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

Summarized below are the continuous improvements for maintenance release X, which was publicly released on August 19, 2025. The previous maintenance release was release 21772.

The 2025.8.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### New Features  {#new-features-X}

None.

### Enhancements {#enhancements-X}

None.

### Fixed Issues {#fixed-issues-X}

None.

#### AEM Guides {#guides-X}

* GUIDES-26688: CSS and Page layout files in Native PDF templates exhibit inconsistent file locking behavior, allowing edits even when the files are locked.
* GUIDES-30900: Copying a folder with a large number of assets from the Assets UI leads to an API timeout. The operation continues to run in the backend and completes after some time, but no success or failure message, or notification is shown in the UI.
* GUIDES-29090: In the Native PDF output, the List of Index (LOI) appears in a non-alphabetical order and nested index terms are not grouped properly, making the index difficult to navigate.
* GUIDES-11227: Copying a DITA map from the Assets UI also copies its attached Baseline to the new map.
* GUIDES-31506: The Home page goes blank when one of the files listed in the Recent files widget is based on a template whose source template does not include a thumbnail.

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Known Issues {#known-issues-X}

Apache HTTPD version 2.4.65 introduces changes that may affect certain configurations due to new restrictions implemented as part of security fixes. These fixes address vulnerabilities by ensuring that directives such as RequestHeader set, edit, and edit_r used to modify the Content-Type header are now correctly limited to request headers. This change prevents unintended modifications to response headers, particularly for static content.

### Deprecated Features and APIs {#deprecated-X}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-X}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses X identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.80.0|[Oak API 1.80.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.80/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.29.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
