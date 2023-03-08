---
title: Latest Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Latest Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release rotes for the latest maintenance release of Experience Manager as a Cloud Service.

## Release 11358 {#release-11358}
 
Summarized below are the continuous improvements for maintenance release 11358, which was publicly released on March 10, 2023. This maintenance release is an update from previous maintenance release 11289.

Feature enablement for this maintenance release will provide you with the full feature set. See the [current release notes](/help/release-notes/release-notes-cloud/release-notes-current.md) for full details.

### Known Issues {#known-issues}

to fill

### Fixed Issues {#fixed-issues}

#### Sites {#sites-issues}

- SITES-11584 Fixed issue with Live Copies that could not be created for pages with annotations
- SITES-11683 Disabled MSM Live Copies with partially broken inheritance

#### Assets {#assets-issues}

- ASSETS-20879 Fixed regression preventing Asset Reports UI from working correctly and resulted in incorrect results in generated reports.
- ASSETS-21020 Fixed issue with broken asset download - Image profile doesn't exist after moving asset
- ASSETS-21023 Fixed issue with image renditions in Dynamic Media preventing access through the API

#### Forms {#forms-issues}

- None

#### Platform {#platform-issues}

- GRANITE-44467 - Fixed issue causing import to fail, when updating an existing node, Filevault under certain instances did not preserve mixin types and child nodes

### Embedded Technologies {#embedded-tech}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.44-T20221206170501-6d59064 |[Oak API 1.44.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.44.0/index.html)| 
|AEM SLING API |Version 2.27.0 |[Apache Sling API 2.27.0 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.21.2|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
