---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 13420 {#release-13420}

Summarized below are the continuous improvements for maintenance release 13420, which was publicly released on September 11, 2023. This maintenance release replaces release 13323.

2023.9.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-13420}

- ASSETS-19544: Assets last modified by property is now set to the user requesting processing.

### Fixed Issues {#fixed-issues-13420}

- ASSETS-27628: Erroneous “channels” node getting created when customizing Assets search panel 
- ASSETS-27539: Upload restrictions regular expression matching.
- ASSETS-26530: Unified Shell does not bring users back to original page.
- ASSETS-22719: Brackets in Smart Crop Breakpoint Naming break the Smart Crop editing feature.
- ASSETS-27726: linkshare.html should not be indexed by Google.
- ASSETS-27791: Metadata schema validation occurs for only the first field.
- ASSETS-25544: Fixed disabled CDN cache invalidation button.
- ASSETS-26575: Fixed name truncation when creating image sets.
- ASSETS-26705: Fixed unnecessary processing on non-DM folder assets and content fragments.
- ASSETS-25740: Fixed screen readers not narrating Name and role for Edit/Crop controls on 'Edit Smart Crops' page using down arrow keys.
- CQ-4354266: Unable to open inbox items.
- CQ-4354347: Updated AEM Translations.
- DISP-1009: User-Agent as non first header trims X-Forwarded-Host.
- Various accessibility and security related fixes.

### Known Issues {#known-issues-13420}

None.

### Embedded Technologies {#embedded-tech-13420}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.54-T20230817132355-3800a65|[Oak API 1.54.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.54.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.2|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
