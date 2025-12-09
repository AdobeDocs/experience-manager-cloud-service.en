---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 23482 {#23482}

Summarized below are the continuous improvements for maintenance release 23482, which was publicly released on December 3, 2025. The previous maintenance release was release 23385.

The 2025.12.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.


### Enhancements {#enhancements-23482}

* ASSETS-49770: Add Quarantine notifications for malware scan results.
* ASSETS-54079: Apply custom metadataform for quarantine folder.
* ASSETS-54083: Create scheduled quarantine cleanup mechanism.
* ASSETS-54278: Remove the `dam:avScanTime` property from assets.
* ASSETS-57284: Restrict file uploads to Quarantine folder (disable drag & drop).
* ASSETS-57428: Hide quarantine folder in Assets View UI.
* ASSETS-57626: Improve retry behavior for async assets jobs.
* ASSETS-57879: Add merge option for async move/copy assets jobs.
* ASSETS-58099: Add config to disable enhanced smart tags for entire environment.
* ASSETS-58136: Implement pagination feedback in Search OpenAPI.
* ASSETS-59402: Add async job endpoints for folder delete API: export packages to internal region.
* ASSETS-59966: Rename Malware Administrators group to Quarantine Administrators.
* ASSETS-60166: Use VideoViewer.js instead of iframe-based URLs.
* GRANITE-61378: Permissions debugging tool - ListPrincipals API.
* GRANITE-63235: Query to identify Sites using `cq:conf` property, support detection of old pages/versions.
* SITES-30452: Content API with ASO - Title & Description Suggestions, XWalk support, JSON Patch operations, IMS Service Principal Binding.

### Fixed Issues {#fixed-issues-23482}

* ASSETS-57430: Fix Assets View upload skipping preprocessing: export `repoapi.preprocessing` package, update RAPI to latest.
* ASSETS-58190: Reduce unnecessarily high guess total in Collections UI.
* ASSETS-58866: Fix Asset title/description/ID returned in OpenAPI responses.
* ASSETS-58868: Fix pagination when sort fields missing on assets.
* ASSETS-58920: Fix bulk assets import skipping preprocessing.
* ASSETS-59168: Fix scan start/end time showing incorrect timezone.
* ASSETS-59702: Fix event ordering when asset status set to No Status.
* ASSETS-59830: Re-queue async jobs stopped during pod termination.
* ASSETS-49757: Fixes for Malware Detection scan events.
* GRANITE-61019: Fix `gcMonitor` not notified on first run after AEM restart.
* GRANITE-62717: Fix `JSafe` password handling with non-ASCII characters.
* SITES-34331: Fix 503 timeout loading Rollout Overlay for non-admin users (`cqLiveSyncCancelled index`).

### Known Issues {#known-issues-23482}

None.

### Deprecated Features and APIs {#deprecated-23482}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-23482}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 4 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-23482}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.88.0|[Oak 1.88.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.88/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.30.2|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|

