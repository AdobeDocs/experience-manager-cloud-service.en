---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release AAA {#release-AAA}

Summarized below are the continuous improvements for maintenance release AAA, which was publicly released on March 18, 2026. The previous maintenance release was release 24678.

The 2026.3.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-AAA}

* CNTBF-613: Fix Access Denied (JCR-101) - failed to register node types
* GRANITE-53957: Upgrade Azure SDK V8 to V12 for oak-blob-azure
* GRANITE-57035: Use Bouncy Castle as the default security provider
* GRANITE-59249: Avoid registering a security provider in the JVM
* GRANITE-61564: View Settings on /security/users.html fails to open for admins
* GRANITE-64748: OIDC: configurable sling.oauth-request-key Cookie expiry
* SITES-39767: Support nonce value via request attribute (CSP)
* SKYOPS-129301: Set APIs jar javadoc compliance level to 17
* SKYOPS-132151: Update API Deprecation dates
* GRANITE-64962: Update Apache Jackrabbit Oak to 1.92.0
* GRANITE-64963: Update Apache Jackrabbit Filevault to 4.2.0
* GRANITE-64764: Update Apache Commons Text to version 1.15.0
* SKYOPS-131412: Update Apache Commons Exec to 1.6.0
* SKYOPS-131432: Update Felix SCR to 2.2.14
* SKYOPS-131907: Update Sling API Region to 1.1.10
* SKYOPS-131938: Update GSON to 2.13.2
* SKYOPS-132173: Update Apache Commons Codec to 1.21.0
* SKYOPS-132182: Update Sling Tenant to 1.1.8
* SKYOPS-132267: Update org.osgi.service.component to 1.5.1
* SKYOPS-132272: Update Sling Feature Model to 2.0.4


### Fixed Issues {#fixed-issues-AAA}

* GRANITE-64443: workflow.core remove deprecated exports of log4j
* GRANITE-64543: Permission restrictions response should match API contract
    
### Known Issues {#known-issues-AAA}

None.

### Deprecated Features and APIs {#deprecated-AAA}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-AAA}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 15 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-AAA}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.92.0|[Oak 1.92.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.92.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.30.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|

