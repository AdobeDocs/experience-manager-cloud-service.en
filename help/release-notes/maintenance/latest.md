---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 15541 {#release-15541}

Summarized below are the continuous improvements for maintenance release 15541, which was publicly released on March 19, 2024. The previous maintenance release was release 15262.

2024.3.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-15541}

None.

### Fixed Issues {#fixed-issues-15541}

* GRANITE-50774: GraniteContent should use deterministic order of property-values at init time.

### Known Issues {#known-issues-15541}

None.

### Change Notice {#change-notice-15541}

**Actions Required**

#### Set CM Java Version to 11 {#set-java-version-11}

The new version of the aem-sdk-api contains classes compiled with a Java 11 target, which is not compatible with the Cloud Manager Build environment default JDK version 1.8. This update requires that Maven is executed using JDK 11.

Customers are advised to add a `.cloudmanager/java-version` file to the root of their git repo with the contents: `11`. See [Build Environment / Setting the Maven JDK Version](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#alternate-maven-jdk-version).

#### Update aem-cloud-testing-clients to 1.2.1 {#update-aem-cloud-testing-clients}

Upcoming changes will require the library [aem-cloud-testing-clients](https://github.com/adobe/aem-testing-clients) used in your custom functional tests to be updated to at least version **1.2.1**

Make sure that your dependency in `it.tests/pom.xml` has been updated.

```xml
<dependency>
   <groupId>com.adobe.cq</groupId>
   <artifactId>aem-cloud-testing-clients</artifactId>
   <version>1.2.1</version>
</dependency>
```

This change will be required after April 6, 2024.

Failing to update the dependency library will result in pipeline failures at the "Custom Functional Testing" step.

### Embedded Technologies {#embedded-tech-15541}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.60-T20240131102219-0cde853|[Oak API 1.60.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.60.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
