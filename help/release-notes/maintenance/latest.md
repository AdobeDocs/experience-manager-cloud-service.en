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

None.

### Fixed Issues {#fixed-issues-21005}

None.

#### AEM Guides {#guides}

* GUIDES-26919 : When opening a DITA map with the unified shell enabled, the editor refreshes intermittently.
* GUIDES-26282: Failing to close JCR session connections while updating or creating topics result in memory leaks and service downtime.
* GUIDES-26434: Native PDF publishing continues indefinitely, if the DITA content has a weblink without having scope as `external`.
* GUIDES-26516:  Publishing of Native PDFs and AEM sites stalls and gets queued, when there are errors in the content.

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Known Issues {#known-issues-21005}

None.

### Deprecated Features and APIs {#deprecated-21005}

* The [Experience Cloud Setup Automation](/help/sites-cloud/integrating/adobe-analytics-exc-setup-automation.md) functionality has been deprecated.

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-21005}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 5 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Change Notice {#change-notice-21005}

**Actions Required**

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
