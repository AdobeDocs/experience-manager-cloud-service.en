---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release X {#release-X}

Summarized below are the continuous improvements for maintenance release X, which was publicly released on September 10, 2024. The previous maintenance release was release 17569.

The 2024.9.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-X}

None.

### Fixed Issues {#fixed-issues-X}

None.

### Known Issues {#known-issues-X}

None.

### Change Notice {#change-notice-X}

* Starting in September 2024, AEM as a Cloud Service will disable the serialization of Resource Resolvers via the Sling Model Exporter framework. See [the documentation](/help/implementing/developing/hybrid/disallow-the-serialization-of-resourceresolvers-via-sling-model-exporter.md) for more details.

### Deprecated Features and APIs {#deprecated-X}

Please note that we are in the proces of updating `com.day.cq.wcm.api` and with the current release, we have marked as `@Deprecated` a few of its methods and classes. These will be removed in future releases, so please consider switching to their suggested alternatives if you are using any of them.

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-X}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses X identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.68.0|[Oak API 1.68.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.68.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.24-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.26.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
