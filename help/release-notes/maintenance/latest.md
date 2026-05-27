---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 26309 {#release-26309}

Summarized below are the continuous improvements for maintenance release 26309, which was publicly released on May 26, 2026. The previous maintenance release was release 25892.

The 2026.5.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

>[!NOTE]
>
>Release 26125 has been made private. 

### Enhancements {#enhancements-26309}

* ASSETS-56957: Added multi-audio track and multi-caption upload support for videos in Dynamic Media with OpenAPI.
* ASSETS-58563: Added Adobe Commerce integration to AEM Assets.
* ASSETS-65603: Improved Folder listing performance in Touch UI by allowing configuration of a reduced asset count.
* ASSETS-66032: Added advanced networking proxy support to Assets Bulk Import for environments with IP-restricted cloud storage.
* CQ-4363346: Enhanced the Translation Guideline UI with support for downloading sample guidelines, uploading guideline files in JSON, PDF, and DOCX formats, and deleting existing guidelines.
* GRANITE-67514: Isolated an internal caching library bundle to prevent transform job failures and conflicts with customer-deployed bundles.
* SITES-42076: Experimental: Added bulk find-and-replace operations for pages as MCP primitives in the Content API.
* SITES-42835: Experimental: AEM Forms pages created outside the Content API are now accessible via the AEM Sites Content API without requiring migration or schema changes.
* SITES-44265: Added a stable replicated page identifier to the Content API that remains valid after page moves, preventing stale-reference 404 errors.

### Fixed Issues {#fixed-issues-26309}

* ASSETS-36208: Fixed image profiles not appearing in folder properties when Dynamic Media is disabled.
* ASSETS-63240: Fixed bulk multi-select Relate operations in Append Mode leaving users on a blank page instead of returning to the Assets console.
* ASSETS-65076: Fixed an incorrect protocol value being passed to the Externalizer API, which caused failures when using Sling request builders.
* ASSETS-66102: Fixed Adobe I/O Runtime asset publish events reporting an incorrect `repo:version` value, which caused failures in downstream integrations.
* ASSETS-66226: Fixed assets not being removed from the delivery tier upon deletion when their approval status was stored with mixed-case values.
* ASSETS-66669: Fixed the Home button on the Search Results page not navigating to the Start screen in Touch UI when Unified Shell is enabled.
* ASSETS-66683: Fixed an approval loop in Dynamic Media with OpenAPI triggered by upload failures, which created backlogs and disrupted asset approval workflows.
* ASSETS-67113: Fixed Bulk Import ignoring SVG assets when filtering by MIME type `image/svg+xml`.
* CQ-4363466: Fixed cloud configuration path resolution failures affecting third-party translation connectors that use custom configuration resolution.
* CQ-4363355: Fixed translation requests in the GenAI Translation Connector being routed to an incorrect regional endpoint due to a hardcoded static URL.
* SITES-44186: Fixed meta tag injection on Author breaking Page Editor event handling for some customers.

### Known Issues {#known-issues-26309}

None.

### Deprecated Features and APIs {#deprecated-26309}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-26309}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 19 vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-26125}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.0.0 | [Oak 2.0.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.0.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.30.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
