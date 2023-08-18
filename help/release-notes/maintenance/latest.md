---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 13173 {#release-13173}

Summarized below are the continuous improvements for maintenance release 13173, which was publicly released on August 18, 2023. This maintenance release is an update from previous maintenance release 123099.

2023.8.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-13173}

None.

### Fixed Issues {#fixed-issues-13173}

- SITES-15463: Sites Templates - Templates cannot be published.

### Known Issues {#known-issues-13173}

- SITES-15359: Content Fragments - The variation name pattern fails to correctly match variations that have ```'_'``` in their resource names.
- FORMS-10444: Adaptive Forms Templates - Templates cannot be published (workaround: use Distribution console).
- CQ-4354191: Worfklows - Custom launcher may trigger many times due to replication metadata present on nt:unstructured nodes (workaround: update launchers to exclude replication metadata properties to avoid overlap).

### Embedded Technologies {#embedded-tech-13173}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.52-T20230629133256-25c01b8|[Oak API 1.52.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.52.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.2|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
