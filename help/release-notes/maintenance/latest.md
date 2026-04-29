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

Summarized below are the continuous improvements for maintenance release X, which was publicly released on May 5, 2026. The previous maintenance release was release 25520.

The 2026.5.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.


### Enhancements {#enhancements-X}

None.

### Fixed Issues {#fixed-issues-X}

None.

#### AEM Guides {#guides-X}

* GUIDES-45110: When selecting an image in the Editor using the **Select file** dialog, only raster formats (such as JPG, PNG, and GIF) are displayed. Vector files (such as `.ai` and `.eps`) are not shown and cannot be selected.
* GUIDES-41938: Creating a topic in a folder with spaces in its name incorrectly creates a duplicate folder where spaces are replaced by hyphens, and the topic is saved there instead of the original folder.
* GUIDES-38377: When changes to an output preset in a Folder profile are applied to existing maps, the saved **Publish Context** for the AEM Sites preset is reset.
* GUIDES-43547: When large topics or maps are opened, the Author instance becomes unresponsive, requiring a restart in some cases.
* GUIDES-32520: When Backspace is used on elements, the Editor scrolls to the top of the topic regardless of the cursor position (Editor 2.0).

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Known Issues {#known-issues-X}

None.

### Deprecated Features and APIs {#deprecated-X}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-X}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses X identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.90.0|[Oak 1.90.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.90.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.30.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
