---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 18311 {#18311}

Summarized below are the continuous improvements for maintenance release X, which was publicly released on October 22, 2024. The previous maintenance release was release 18175.

The 2024.10.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-18311}

- ASSETS-41820 : Indexing improvements for processing watchdog
- ASSETS-43720 : Functional improvements to processing watchdog
- ASSETS-42554 : Performance improvements for large folders

### Fixed Issues {#fixed-issues-18311}

- ASSETS-37534 : Changes in search to not expose property used for approval target
- ASSETS-38322 : Remove publish criteria provider config Remove publish event feature
- ASSETS-40482 : Accessibility issue in play/pause and mute/unmute button in Scene7 video player
- ASSETS-40593 : Error page occurs after clicking on "Properties" button in Assets > Files
- ASSETS-40598 : Sync smart crops when unsynced asset is moved to a sync enabled folder
- ASSETS-40743 : Issues with triggering Replace Asset dialog when certain characters exist in filename
- ASSETS-40825 : Assets Search Facets Disappearing After Editing Search Form
- ASSETS-41007 : Deletion on AEM sometimes leaves orphan Assets on Delivery
- ASSETS-41172 : Dynamic Media Templates special chars not allowed in name
- ASSETS-41896 : Assets mentioned in cq:discarded property on the folder should NOT be published to Brand Portal
- ASSETS-42067 : Dynamic Media Templates - Download gives error
- ASSETS-42070 : Dynamic Media Templates - Non-admin users should have Template create/edit access
- ASSETS-42344 : Connected Assets Sync disconnected - Reconnect and advice for customer
- ASSETS-42620 : Issue with the preview option of asset versions - shows blank preview when we open the asset
- ASSETS-42701 : Web Optimized Image Delivery and Cropping Issue
- ASSETS-42966 : Async barricade can become unblocked in error due if multiple jobs share the same path
- ASSETS-43072 : Dynamic Media Templates - Template references lookup breaks on an invalid reference
- ASSETS-43212 : Internationalisation issues in metadata schema editor
- ASSETS-43202 : Fixes for selecting annotations to print from timeline
- ASSETS-43502 : AEM CS Existing Image Preset Name Not Displayed on Edit Page
- ASSETS-43538 : Async copy assets job uses incorrect property for source path
- ASSETS-43798 : Check for destination path first before copying assets
- ASSETS-43945 : Increase retry delay to 20 min for async assets job queue
- ASSETS-44025 : Async delete assets job fails for when individual assets are selected

- SITES-26128 : Class cast exception in CreateLiveCopyStep

### Known Issues {#known-issues-18311}

* FORMS-15818: Component descriptor entry `OSGI-INF/com.adobe.aemfd.docmanager.impl.*.xml` not found statements in server logs. These are harmless log statements.

### Deprecated Features and APIs {#deprecated-18311}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-18311}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses X identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-18311}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.70.0|[Oak API 1.70.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.70.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.24-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.27.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
