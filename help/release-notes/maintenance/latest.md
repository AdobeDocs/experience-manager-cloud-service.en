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

Summarized below are the continuous improvements for maintenance release X, which was publicly released on February 18, 2025. The previous maintenance release was release 19352.

The 2025.2.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-X}

None.

### Fixed Issues {#fixed-issues-X}

None.

#### AEM Guides {#guides}

* GUIDES-23526: When updating conditions from the folder profile, all the condition groups are lost and the conditions become flattened.
* GUIDES-22574: If an external link contains a UUID, it goes in post processing and converts the external link to UUID link thereby breaking the link on editor and also on the publishing sites.
* GUIDES-24983: When copying an image from any external product (for example, MS PowerPoint) and pasting it into Guides, the functionality to upload the asset on the fly for use in the file breaks.
* GUIDES-21772: Native PDF generation fails for content with **chunk attribute** set to **to-content**.
* GUIDES-23964: When choosing **Edit properties**, the baseline dialog does not show the previously saved criteria for dynamic baseline.
* GUIDES-19067: When duplicating any folder profile, its admin user list also gets copied from the original folder profile

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/overview). 

### Known Issues {#known-issues-X}

None.

### Deprecated Features and APIs {#deprecated-X}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-X}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses X identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.72.0|[Oak API 1.72.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.72.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.24-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.27.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
