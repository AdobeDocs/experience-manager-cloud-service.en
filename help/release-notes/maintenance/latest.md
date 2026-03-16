---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 24893 {#release-24893}

Summarized below are the continuous improvements for maintenance release 24893, which was publicly released on March 17, 2026. The previous maintenance release was release 24678.

The 2026.3.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-24893}

* CNTBF-613: Fix Access Denied (JCR-101) - failed to register node types.
* GRANITE-53957: Upgrade Azure SDK V8 to V12 for oak-blob-azure.
* GRANITE-57035: Use Bouncy Castle as the default security provider.
* GRANITE-59249: Avoid registering a security provider in the JVM.
* GRANITE-61564: View Settings on /security/users.html fails to open for admins.
* GRANITE-64748: OIDC: configurable sling.oauth-request-key Cookie expiry.
* SITES-39767: Support nonce value via request attribute (CSP).
* SKYOPS-129301: Set APIs jar javadoc compliance level to 17.
* GRANITE-64962: Update Apache Jackrabbit Oak to 1.92.0.
* GRANITE-64963: Update Apache Jackrabbit Filevault to 4.2.0.
* GRANITE-64764: Update Apache Commons Text to version 1.15.0.
* SKYOPS-131412: Update Apache Commons Exec to 1.6.0.
* SKYOPS-131432: Update Felix SCR to 2.2.14.
* SKYOPS-131907: Update Sling API Region to 1.1.10.
* SKYOPS-131938: Update GSON to 2.13.2.
* SKYOPS-132173: Update Apache Commons Codec to 1.21.0.
* SKYOPS-132182: Update Sling Tenant to 1.1.8.
* SKYOPS-132267: Update org.osgi.service.component to 1.5.1.
* SKYOPS-132272: Update Sling Feature Model to 2.0.4.
* SKYOPS-133689: Update Dispatcher to use Apache httpd 2.4.66.

### Fixed Issues {#fixed-issues-24893}

* GRANITE-64443: workflow.core remove deprecated exports of `log4j`.
* GRANITE-64543: Permission restrictions response should match API contract.

#### AEM Guides {#guides-24893}

* GUIDES-38412 : When editing a Schematron `(*.sch)` file and using the find and replace feature, the find and replace panel appears partially off-screen at the bottom, preventing access to its input fields and controls.
* GUIDES-37806: When the same topic is reused across multiple maps with different conditional presets, publishing the latest map to Salesforce overwrites the topic content, resulting in incorrect data being displayed to users of previously published maps.
* GUIDES-39394: When an image initially managed as a language‑specific asset with a specific version (for example, under `/en/`) is moved out to a global folder with an updated version and baseline export is performed, the new baseline continues to reference outdated language‑specific versions of that image, leading to a failed baseline export.
* GUIDES-39054: When creating a dynamic baseline, the Editor sometimes becomes unresponsive due to multiple concurrent API requests, causing all the other operations to halt.
* GUIDES-37781: When assigning a user to a review task, the dropdown lists all users instead of only those associated with the selected projects, resulting in invalid user options.
* GUIDES-39385: While opening a Report for a map, there is a delay in the loading of the Filters panel.

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 
    
### Known Issues {#known-issues-24893}

None.

### Deprecated Features and APIs {#deprecated-24893}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-24893}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 9 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-24893}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.92.0|[Oak 1.92.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.92.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.66 | [Apache Httpd 2.4.66](https://apache.googlesource.com/httpd/+/refs/tags/2.4.66/CHANGES)|
|AEM Core Components| 2.30.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
