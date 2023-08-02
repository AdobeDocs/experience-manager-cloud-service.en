---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 12874 {#release-12874}
 
Summarized below are the continuous improvements for maintenance release 12874, which was publicly released on Aug 2, 2023. This maintenance release is an update from previous maintenance release 12790.

2023.8.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-12874}

- New version of index definition: `/oak:index/damAssetLucene-9`

  - ASSETS-18351: Switches to insecure facets - to improve search performance
  - ASSETS-17896: Removes Feature Vectors from the index - similarity search based on smart tags
  - ASSETS-8715: Adds null check / not null check for the property "jcr:content/metadata/dam:status"
  - GRANITE-45138: Removes property index from the predicted tags dynamic boost property
  - ASSETS-17614: Adds Scene7 ID as an indexed property (null check and not null check enabled)
  - ASSETS-14516: Adds properties for 'new UI' Trash functionality to the index
  - ASSETS-16270: Adds coalesced title property to the index (for use in sorting)
  - ASSETS-24478: Remove 5 potentially large properties from the index (based on analysis of customer index data)
  - ASSETS-3383: Adds an additional tag 'assetsOmnisearch'

### Fixed Issues {#fixed-issues-12874}

- GRANITE-46601: Quickstart SDK fails to start on jdk 11.0.20 without `-Djdk.util.zip.disableZip64ExtraFieldValidation=true` java option
- ASSETS-25794: Resolved an issue with S7ConfigResolverImpl that caused it to execute an expensive query at startup.
- ASSETS-24379: Made improvements to the ReplicateOnModifyListener.
- ASSETS-25473: Fixed a bug where the Quick Publish Option was visible to users without replication permission.
- ASSETS-24803: Addressed an XSS vulnerability in the Viewers feature.
- ASSETS-25489: Corrected an issue where Smart croppings were being downloaded with the wrong suffix.
- ASSETS-25435: Fixed an error where the WidthxHeight fields were missing in the Download for dynamic renditions
- ASSETS-22719: Fixed an issue with Smart Crop Breakpoint Naming when using brackets, which caused problems with the Smart Crop editing feature.
- ASSETS-25741: Fixed the absence of a visual asterisk (*) symbol for the mandatory 'width' edit field in the 'Basic' tab section.
- ASSETS-25759: Improved the visibility of focus on dropdown elements in high contrast black/white modes.
- ASSETS-25749: Fixed the issue where focus was not moving to multiple controls below the video when navigating using the keyboard Tab, resulting in them being inaccessible.
- ASSETS-26074: Restored the limit of 127 characters for names of non-video assets.

### Known Issues {#known-issues-12874}

- TBD

### Embedded Technologies {#embedded-tech-12874}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.52-T20230629133256-25c01b8|[Oak API 1.52.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.52.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
