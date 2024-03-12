---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release X {#release-X}

Summarized below are the continuous improvements for maintenance release X, which was publicly released on March X, 2024. The previous maintenance release was release 15262.

2024.3.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-X}

#### `UnsupportedClassVersionError` in CM pipeline Build step after upgrading `aem-sdk-api` version to `2024.2.15262.20240224T002940Z-231200`

The new version of the aem-sdk-api contains classes compiled with a Java 11 target, which is not compatible with the Cloud Manager Build environment default JDK version 1.8. This update requires that Maven is executed using JDK 11.

Customers are advised to add a `.cloudmanager/java-version` file to the root of their git repo with the contents: `11`. [Build Environment / Setting the Maven JDK Version](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/create-application-project/build-environment-details.html?lang=en#alternate-maven-jdk-version)

### Fixed Issues {#fixed-issues-X}

None.

### Known Issues {#known-issues-X}

None.

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.60-T20240131102219-0cde853|[Oak API 1.60.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.60.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
