---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 21772 {#21772}

Summarized below are the continuous improvements for maintenance release 21772, which was publicly released on August 6, 2025. The previous maintenance release was release 21706.


The 2025.8.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-21772}

* SITES-33025 - Open new CF Editor via ID instead of path
* SITES-32741 - Trigger update of contenf-fragment page references asynchronously
* SITES-32087 - GraphQL: Add support for _ignoreCase on StringArray
* SITES-31791 - Upgrade graphql-java library to 24.0

### Fixed Issues {#fixed-issues-21772}

* SITES-31992 - GraphQL: Fix sporadical errors in model scan during bundles startup
* SITES-29967 - GraphiQL: Long query names are cut off
* SITES-26266 - Content references that don't start with / are not returned from BE response (Java API)
* SITES-17874 - GraphQL persisted queries: Fix encoding for content-type application/graphql-response+json

### Known Issues {#known-issues-21772}

None.

### Deprecated Features and APIs {#deprecated-21772}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-21772}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 4 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-21772}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.80.0|[Oak API 1.80.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.80/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.63 | [Apache Httpd 2.4.63](https://github.com/apache/httpd/blob/2.4.63/CHANGES)|
|AEM Core Components| 2.29.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
