---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 28386 {#release-28386}

Summarized below are the continuous improvements for maintenance release 28386, which was publicly released on September 23, 2026. The previous maintenance release was release 27830.

The 2026.10.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.


>[!NOTE]
>
>Release 28187 has been made private. 


### Enhancements {#enhancements-28386}

* CQ-4361811: Removed the deprecated `commons-lang` dependency from `cq-commons` (in favor of `commons-lang3`).
* CQ-4365034: Migrated to Adobe Analytics API 2.0 ahead of the Analytics 1.4 API end-of-life (August 31, 2026).
* GRANITE-65723: Added session prolongation support for JWT-based authentication on page requests.
* GRANITE-67893: Added support for custom URI schemes in HTML sanitization via the ALLOWED_URI_SCHEMES configuration.
* GRANITE-69821: Added last-activity timestamp tracking on user profile nodes.
* GRANITE-71327: Added the ability to inspect configured preprocessors.
* GRANITE-72442: Added support for Bouncy Castle-based JSafe-compatible keystores.
* SKYOPS-124458: Increased the AEM Developer Console IMS integration limit to 40 technical accounts.
* SKYOPS-137568: Added support for running the AEM Quickstart on Java 25.
* SKYOPS-138717: Removed a deprecated API from the AEM public API surface.
* SKYOPS-145215: Added a CQ Quickstart MCP server to the AEM as a Cloud Service SDK.
* SKYOPS-155829: Updated Cloud Service platform bundles to remove the deprecated commons-lang dependency.

### Fixed Issues {#fixed-issues-28386}

* ASSETS-9938: Fixed Link Share download failing for ZIP files.
* CQ-4364676: Fixed a broken Help link in the login screen footer.
* GRANITE-64470: Fixed the Publish mail service requiring a pod restart to pick up OSGi configuration changes (for example, OAuth token updates).
* GRANITE-70798: Fixed a login failure on AMS publish instances after the 6.5 LTS SP2 upgrade (TokenAuthenticationHandler/SAML regression).
* GRANITE-71458: Fixed a missing "Remove member" button in the Groups UI for long user or group names.
* GRANITE-72210: Fixed OIDC authentication failures caused by JWK Set size limits; the HTTP retrieval limits are now configurable.
* GRANITE-72324: Fixed precompile-maven-plugin incompatibility with Maven 3.10.
* GRANITE-73303: Fixed JSafe keystores loading only on first use, which caused delayed initialization.
* SITES-48426: Fixed a severe performance slowdown in the Sites console for large sites.
* SITES-50164: Fixed the Preflight Play button failing to launch highlighting, the preview-mode banner, and popover auto-minimize due to a client library load issue.
* SKYOPS-147677: Fixed jcr:content child node deletions not replicating to Publish when a page has comments.
* SKYOPS-152346: Fixed customer-provided overlays being overwritten by the product overlay.

#### AEM Guides {#guides-28386}

* GUIDES-48304: On low-resolution screens, the Insert Keyword dialog fails to appear when inserting a keyword from the toolbar, while it opens as expected when using **More** option.
* GUIDES-48893: Opening the Review panel or applying a project filter takes some time to load the task list.
* GUIDES-49065: The asset status API does not return the correct status for assets whose path contains a comma.
* GUIDES-49325: When you generate AEM Sites (with composite component mapping) output with a baseline targeting an older version, the page content correctly shows that older version, but the page metadata shows the current version instead.
* GUIDES-51759: Starting a translation using an XLIFF project creates an empty project that never moves to an in-progress state.
* GUIDES-52343: When a new learning topic is created using a HTML or learning template with a custom header, the topic title doesn’t appear in the custom header 
* GUIDES-52690: A preset’s saved baseline selection incorrectly displays as *No Baseline* after the baseline is deleted or while a dynamic baseline is still being created.
* GUIDES-52916: Copying a table from Author mode and pasting it into Author mode removes attributes such as `colwidth` and any other attributes defined on `colspec`, causing the column width settings to be lost.

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Known Issues {#known-issues-28386}

None.

### Deprecated Features and APIs {#deprecated-28386}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

>[!NOTE]
>
> On September 28, 2026, environments still using deprecated APIs **will not receive critical Adobe release updates** and will not be subject to Adobe’s standard commitments around performance and availability. As a result, you will not receive new features or bug fixes, application stability and uptime may be negatively affected, and security risk exposure may increase further. To once again receive Adobe release updates, a fullstack pipeline must be successfully executed; the update will then be applied within a few days.

### Security Fixes {#security-28386}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 16 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-28386}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.6.0 | [Oak 2.6.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.6.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.67 | [Apache Httpd 2.4.67](https://apache.googlesource.com/httpd/+/refs/tags/2.4.67/CHANGES)|
|Dispatcher|2.0.275||
|AEM Core Components| 2.32.6|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
|Java 21|21.0.11|[JDK 21.0.11](https://www.oracle.com/java/technologies/javase/21-0-11-relnotes.html)|
