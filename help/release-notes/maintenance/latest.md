---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 25194 {#25194}

Summarized below are the continuous improvements for maintenance release 25194, which was publicly released on April 1, 2026. The previous maintenance release was release 24678.

The 2026.4.0 feature activation provides the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

>[!NOTE]
>
>Release 24893 has been made private. 

### Enhancements {#enhancements-25194}

* ASSETS-65127: Event custom metadata: improved handling of metadata names.
* ASSETS-63313: Auto-create related links for exported assets and parents based on C2PA manifests.
* ASSETS-10995: Limit number of assets in a download zip.

### Fixed Issues {#fixed-issues-25194}

* ASSETS-62882: Admin view: info tooltip breaks when multiple invalid filenames are uploaded.
* ASSETS-63642: Share link fails to render asset on some dev environments (SLA3).
* ASSETS-59267: NPE when loading application metadata for delivery payload.
* ASSETS-59227: Metadata export: unselected properties no longer included due to regex matching.
* ASSETS-65187: CSV preview in Cloud when column data contains escaped commas.
* ASSETS-63441: Ensure all users have permissions to read Assets Omnisearch configuration.
* SITES-40095: Metadata editor: local content fragment references beyond 10 entries.

### Known Issues {#known-issues-25194}

None.

### Deprecated Features and APIs {#deprecated-25194}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-25194}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 9 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-25194}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.90.0|[Oak 1.90.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.90.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.30.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
