---
title: Latest Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Latest Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release rotes for the latest maintenance release of Experience Manager as a Cloud Service.

## Release 10949 {#release-10949}
 
Summarized below are the continuous improvements for maintenance release 10949, which was publicly released on February X, 2023. This mainteanance release is an update from previous maintenance release 10912.

Feature enablement for this maintenance release will provide you with the full feature set. See the [current release notes](/help/release-notes/release-notes-cloud/release-notes-current.md) for full details.

### Known Issues {#known-issues}

Do not upgrade if you are using CORS. We identified an issue impacting GraphQL content delivery part on this release. A change in default AEM dispatcher config around how GraphQL persisted queries are cached can break the GraphQL content delivery of persisted queries for customers using a CORS configuration.

### Embedded Technologies {#embedded-tech}

|Technology|Version|Link|
|---|---|---|
|AEM WCM Core Components|Version X|[GitHub](https://github.com/adobe/aem-core-wcm-components)|
