---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 17689 {#release-17689}

Summarized below are the continuous improvements for maintenance release X, which was publicly released on September 10, 2024. The previous maintenance release was release 17569.

The 2024.9.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-17689}
- ASSETS-41404: Changes to support DRM improvements
- ASSETS-41621: Updated async Asset copy job
- ASSETS-32166: Updated async Asset move job
- ASSETS-41429: Image presets support in DM OpenAPI.
- ASSETS-38968: Improve representation of Content Fragments references
- ASSETS-41787, ASSETS-41183: Improvements for Assets Bulk Operations framework
- GRANITE-52917: Optimizations to improve content copy package installation times

### Fixed Issues {#fixed-issues-17689}
- ASSETS-40875: Spurious NPE logged by AssetDeleteHandler
- ASSETS-42422: Avoid triggering of async job for single Asset move
- ASSETS-41234: Unified Shell - Global nav might not work if opened when search bar is open.
- ASSETS-42256: Unified Shell - Tag/Badge indicating environment only works intermittently
- ASSETS-41271: Prevent unnecessary republish of Assets during move operations
- ASSETS-38894: Limit Retries by processing watchdog
- ASSETS-40815: Use preview PDF rendition for showing PPT file in Link Share UI 
- ASSETS-37123: Cannot load Asset preview in Link Share Dialog
- CQ-4358156: update backlinks of tag being deleted

### Known Issues {#known-issues-17689}

- FORMS-14340: Error in instantiation of FormsAndDocumentOmniSearchHandler and CloudStorageSubmitActionInserter. These are harmless log statements.
- FORMS-15818: Component descriptor entry ‘OSGI-INF/com.adobe.aemfd.docmanager.impl.*.xml’ not found statements in server logs. These are harmless log statements.
- SITES-23662: User that triggers a publish cannot be extracted from JCR log statements in server logs. This is for a feature under development that might cause intermitent and harmless “Cannot find a valid user id in the batch of OSGI events” errors in the log.

### Change Notice {#change-notice-17689}

* Starting in September 2024, AEM as a Cloud Service will disable the serialization of Resource Resolvers via the Sling Model Exporter framework. See [the documentation](/help/implementing/developing/hybrid/disallow-the-serialization-of-resourceresolvers-via-sling-model-exporter.md) for more details.

### Deprecated Features and APIs {#deprecated-17689}

Please note that we are in the proces of updating `com.day.cq.wcm.api` and with the current release, we have marked as `@Deprecated` a few of its methods and classes. These will be removed in future releases, so please consider switching to their suggested alternatives if you are using any of them.

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-17689}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses X identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-17689}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.68.0|[Oak API 1.68.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.68.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.24-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.26.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
