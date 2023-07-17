---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 12697 {#release-12697}
 
Summarized below are the continuous improvements for maintenance release 12697, which was publicly released on July 14, 2023. This maintenance release is an update from previous maintenance release 12549. Maintenance release 12697 replaces 12585 to rectify one issue.

2023.7.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-12697}

- General RDE stability improvements (SKYOPS-61133, SKYOPS-55281, SKYOPS-61216 and SKYOPS-61401)
- DXML-12327: AEM Guides: Support for language variables in Native PDF publishing
- DXML-11518: AEM Guides: Enhanced metadata support in Native PDF publishing
- DXML-10093: AEM Guides: Support for connecting to external data sources and inserting data into dita topics
- DXML-10699: AEM Guides: Support for XLIFF format in translation
- DXML-10141: AEM Guides: Option to use microservice-based publishing for PDF (Native & DITA-OT), HTML & Custom preset types
- SKYOPS-61385 - Update the dispatcher to use libpcre2 when evaluating regular expressions in Apache HTTPD

### Fixed Issues {#fixed-issues-12697}

- AEM Guides: Various Native PDF enhancements and stability fixes
- SKYOPS-53130: Improve AC Tool support in RDE
- SKYOPS-57146: Fix Sling deadlock on AEM startup
- SKYOPS-61646: Last replication date is not updated after upgrade to release 12585

### Known Issues {#known-issues-12697}

None.

### Embedded Technologies {#embedded-tech-12697}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.52-T20230629133256-25c01b8|[Oak API 1.52.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.52.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
