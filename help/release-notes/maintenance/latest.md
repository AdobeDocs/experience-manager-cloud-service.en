---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 21570 {#21570}

Summarized below are the continuous improvements for maintenance release 21570, which was publicly released on July 15, 2025. The previous maintenance release was release 21484.

>[!NOTE]
>
>[Release 21484](/help/release-notes/maintenance/2025/2025-7-0.md#21484) was made private and replaced by release 21570.

The 2025.7.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-21570}

Migrated to Apache Httpd 2.4.63

### Fixed Issues {#fixed-issues-21570}

* SKYOPS-112722 - Fixed an issue causing vanity URL resolution to fail

### Known Issues {#known-issues-21570}

* The related AEM SDK carries a different release ID (21575) and is available via the Software Distribution portal.
* Apache Httpd version 2.4.63 introduced a breaking change in how mod_rewrite handles question marks (?) in URLs. This change was implemented to prevent the usage of the UnsafeAllow3F flag, which was considered a security risk. This affects any RewriteRule directives that rely on question mark detection in URL patterns.

### Deprecated Features and APIs {#deprecated-21570}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-21570}

None

### Embedded Technologies {#embedded-tech-21570}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.80.0|[Oak API 1.80.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.80.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTPD| 2.4.63 | [Apache Httpd 2.4.63](https://github.com/apache/httpd/blob/2.4.63/CHANGES)|
|AEM Core Components| 2.29.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
