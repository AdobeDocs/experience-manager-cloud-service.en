---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 12790 {#release-12790}
 
Summarized below are the continuous improvements for maintenance release 12697, which was publicly released on July 14, 2023. This maintenance release is an update from previous maintenance release 12549. Maintenance release 12697 replaces 12585 to rectify one issue.

2023.7.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-12790}

None.

### Fixed Issues {#fixed-issues-112790}

- SLING-11974 - Fixed regression in SlingHttpServletRequest#getUserPrincipal for non authenticated requests. The fix ensures that a principal is returned even for unauthenticated requests.

### Known Issues {#known-issues-12790}

None.

### Embedded Technologies {#embedded-tech-12790}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.52-T20230629133256-25c01b8|[Oak API 1.52.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.52.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
