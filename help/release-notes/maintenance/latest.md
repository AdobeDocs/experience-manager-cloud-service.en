---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 20454 {#20454}

Summarized below are the continuous improvements for maintenance release X, which was publicly released on April 15, 2025. The previous maintenance release was release 20133.

The 2025.4.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-20454}

* GRANITE-57863 - Update Filevault to version 3.8.4
* GRANITE-56154 - Configure exponential retries in oak-segment-azure
* GRANITE-55999 - Improve performance of UserPropertiesService
* GRANITE-55781 - AEM needs to be updated to remove spurious groups
* GRANITE-53956 - Upgrade Azure SDK V8 to V12 for oak-segment-azure
* GRANITE-50654 - On principal permissions tab, remove "everyone" load by default on the front end
* CQ-4359813 - AEM Translation Kit: March 20
* CQ-4359811 - Granite Translation Kit: March 20
* CNTBF-411 - Add possibility to delete sling job in case it is dropped by JCR
* SKYOPS-103444 - Update to Sling ResourceResolver 1.12.6
* SKYOPS-101147 - Update caconfig impl
* SKYOPS-97124 - Add analyser warnings for outdated versions of the SPIFly bundle
* SKYOPS-95826 - Update runtime Java versions
* SKYOPS-53671 - Use customer installed artifacts from feature models on (RDE) AEM restarts


### Fixed Issues {#fixed-issues-20454}

* SITES-30727: drag and drop may fail for sub-components within the AEM editor.
* GRANITE-57265 - Dropdown selection values are not getting selected
* GRANITE-57067 - Missing effective policies on UI
* CQ-4355411 - [AEM]: Tooltips remain on the display in "User Preferences" dialog
* CNTBF-410 - CheckJob getId null pointer in ContentCopy Bundle
* CNTBF-341 - ContentCopy export Index Out Of Bounds
* ASSETS-49027 - [Regression] The AemRequestEventFilter breaks POST requests to the OSGI web console
* SKYOPS-90607 - Sling Jobs are executed in inactive deployment / mutable content
* SKYOPS-95722 - Remove MaxPermSize size from quickstart flags in AEM-SDK
* ASSETS-44956 - Can't Select Any Dynamic Media Rendition - script tags should be loaded in top level component
* SKYOPS-103569 - Certain images cannot be loaded with Java 21: javax.imageio.IIOException: Cannot create Sun JPEGImageReader backend

### Known Issues {#known-issues-20454}

None.

### Deprecated Features and APIs {#deprecated-20454}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-20454}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 5 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.78.0|[Oak API 1.78.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.78.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.26-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.28.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
