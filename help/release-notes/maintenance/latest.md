---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 14813 {#release-14813}

Summarized below are the continuous improvements for maintenance release 14813, which was publicly released on January 5, 2023. The previous maintenance release was release 14697.

2024.1.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-14813}

* ASSETS-32101: Metadata for smart crop renditions should be updated in DB.
* ASSETS-31297: Improve checks to prevent deletion of copied assets from dynamic media.

### Fixed Issues {#fixed-issues-14813}

* ASSETS-32679: Add cache-killer to rendition URLs when previewing content.
* ASSETS-32755: configure ordered queue for asset move events.
* ASSETS-30756: asset move fails when folder name ends in 'html'.
* ASSETS-32754: [Collab API] Tasks cannot be assigned to users who have not logged in previously in GenStudio and AEMCS.
* ASSETS-29011: Smart crop visible for read-only users.
* ASSETS-32311: Asset Delivery opt-in for VIP program.
* ASSETS-30756: Add CM exclusion.
* ASSETS-28767: Updated cq-dam-mac-sync version.
* ASSETS-31330:  Update dynamic media packages.
* ASSETS-31657: Support new Content Hub service code in granite.auth.ims bundle.
* ASSETS-32509: Allowing the Content Hub Client ID.
* ASSETS-32230: Update RAPI bundle to 366.
* ASSETS-31260: Resolve select issues with schema forms.
* ASSETS-26549: Assets / Nodes with "jcr:lastModifiedBy": "workflow-process-service" show as "external user" in list view.
* ASSETS-31038: Add user mapping for eventrecorderhelper.
* ASSETS-30068: New status COMPLETED_WITH_ERROR for bulk import AE.
* ASSETS-31297: Prevent deletion of copied assets from dynamic media.

### Known Issues {#known-issues-14813}

None.

### Change Notice {#change-notice-14813}

**Action Required**

Upcoming changes will require the library [aem-cloud-testing-clients](https://github.com/adobe/aem-testing-clients) used in your custom functional tests to be updated to at least version **1.2.1**

Make sure that your dependency in `it.tests/pom.xml` has been updated.

```xml
<dependency>
   <groupId>com.adobe.cq</groupId>
   <artifactId>aem-cloud-testing-clients</artifactId>
   <version>1.2.1</version>
</dependency>
```

This change will be required after February 12, 2024.

Failing to update the dependency library will result in pipeline failures at the "Custom Functional Testing" step.

### Embedded Technologies {#embedded-tech-14813}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.58-T20231123092841-619e1bd|[Oak API 1.58.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.58.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
