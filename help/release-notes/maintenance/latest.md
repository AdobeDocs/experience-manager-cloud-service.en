---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 15860 {#release-15860}

Summarized below are the continuous improvements for maintenance release 15860, which was publicly released on April 10, 2024. The previous maintenance release was release 15787.

2024.3.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-15860}

None.

### Fixed Issues {#fixed-issues-15860}

* Fixes regression for displaying Launches console when a launch refers to a deleted or moved page.

### Known Issues {#known-issues-15860}

None.

### Deprecated Features and APIs {#deprecated-15860}

* [JWT Credentials Deprecation in Adobe Developer Console](/help/security/jwt-credentials-deprecation-in-adobe-developer-console.md)

Have a look at [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) to know what has been deprecated or removed in AEM as a Cloud Service.

### Change Notice {#change-notice-15860}

**Actions Required**

#### Set CM Java Version to 11 {#set-java-version-11}

The new version of the aem-sdk-api contains classes compiled with a Java 11 target, which is not compatible with the Cloud Manager Build environment default JDK version 1.8. This update requires that Maven is executed using JDK 11.

Customers are advised to add a `.cloudmanager/java-version` file to the root of their git repo with the contents: `11`. See [Build Environment / Setting the Maven JDK Version](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#alternate-maven-jdk-version).


### Embedded Technologies {#embedded-tech-15860}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.60-T20240131102219-0cde853|[Oak API 1.60.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.60.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.24.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
