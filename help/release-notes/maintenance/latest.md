---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 21005 {#21005}

Summarized below are the continuous improvements for maintenance release 21005, which was publicly released on May 27, 2025. The previous maintenance release was release 20626.

The 2025.5.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-21005}

* GRANITE-58927: Semantic Search toggle improvements.
* SKYOPS-106509: Enhanced GSON compatibility via reflective access in Java 21.
* GRANITE-58800: Update of Apache Commons Collections to version 4.5.0.
* GRANITE-58866: Update of Oak to 1.80.0.
* SKYOPS-107761: Update of Sling Models Jackson Exporter to 1.1.6.
* SKYOPS-107813: Update to Sling ResourceResolver 1.12.8.

### Fixed Issues {#fixed-issues-21005}

* CNTBF-443: Fixed SearchSlingJob EVENT_JOB_TOPIC property.
* GRANITE-57853: Fixed dropdown alignment issues in UI.
* GRANITE-58107: Fixed 404 errors on Publish by disabling user-based pod affinity in OAuth handler.
* SKYOPS-105151: Fixed NPE when accessing bundle list.
* GRANITE-58276, SLING-12755: Fixed OSGi dependency cycles that could prevent the HTL Script Engine factory from starting correctly, causing intermittent server-side rendering errors.
* SKYOPS-83910, SKYOPS-82371 - Fixed JSP compilation concurrency issues.

### Known Issues {#known-issues-21005}

None.

### Deprecated Features and APIs {#deprecated-21005}

* GRANITE-54164: Removed `org.apache.jackrabbit.oak.plugins.blob` from public API.
* GRANITE-54280: Removed `org.apache.jackrabbit.oak.cache` from public API.
* GRANITE-58332: Deprecated `org.apache.jackrabbit.oak.plugins.memory` in public API.

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-21005}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 5 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Change Notice {#change-notice-21005}

* This release contains the following new product index versions:
  * **damAssetLucene-12**

Custom versions of the previous index versions will be automatically merged with the new product index version. Please apply further custom updates to the merged version.

#### Update aem-cloud-testing-clients {#update-aem-cloud-testing-clients-21005}

Upcoming changes will require the library [aem-cloud-testing-clients](https://github.com/adobe/aem-testing-clients) used in your custom functional tests to be updated to at least version **1.2.1** (Recommended: latest version 1.2.9)

Make sure that your dependency in `it.tests/pom.xml` has been updated.

```xml
<dependency>
   <groupId>com.adobe.cq</groupId>
   <artifactId>aem-cloud-testing-clients</artifactId>
   <version>1.2.9</version>
</dependency>
```

This change needs to be performed before June 15, 2025.

Failing to update the dependency library will result in pipeline failures at the "Custom Functional Testing" step.

### Embedded Technologies {#embedded-tech-21005}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.80.0|[Oak API 1.80.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.80.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.29.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
