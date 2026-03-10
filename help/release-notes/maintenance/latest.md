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

Summarized below are the continuous improvements for maintenance release AAA, which was publicly released on March 18, 2026. The previous maintenance release was release 24464.

The 2026.3.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-AAA}

* ASSETS-62815: Fix the failing IT in SDK
* CNTBF-613: Fix Access Denied (JCR-101) - failed to register node types
* CNTBF-625: Release Content Copy bundle 2.0.32
* CQ-4362304: [GenAI] Create Guidelines Frontend / Update LLM config UI
* * GRANITE-36205: Automated update for internal oak release in QS
* GRANITE-53957: Upgrade Azure SDK V8 to V12 for oak-blob-azure
* GRANITE-57035: Use Bouncy Castle as the default security provider
* GRANITE-59249: Avoid registering a security provider in the JVM
* GRANITE-61564: [SLA3] View Settings on /security/users.html fails to open
* GRANITE-61760: Fix failed activation of AdminUserInitializer
* GRANITE-62067: Client bundle compatibility with OAK-11941
* GRANITE-63180: com.day.cq:cq-mailer:5.15.2 exports commons.lang which is deprecated
* GRANITE-63420: OakRS client: refresh long-running sessions after compaction
* GRANITE-63821: Update QS to filevault release fixing JCRVLT-831/JCRVLT-839
* GRANITE-64207: Update QS to filevault test release for JCRVLT-831
* GRANITE-64389: Online migration bundle with support for back migration
* GRANITE-64538: Deprecate org.apache.jackrabbit.webdav.client.methods
* GRANITE-64748: OIDC: configurable sling.oauth-request-key Cookie expiry; bump handler
* GRANITE-64764: Update Apache Commons Text to version 1.15.0
* GRANITE-64872: [OPTEL] Support async inclusion and dynamic enabling
* GRANITE-64962: Update CS Quickstart: latest public release of Oak (1.92.0)
* GRANITE-64963: Update QS to filevault release 4.2.0
* GRANITE-64965: QS builds should fail when new Commons-Collections (not collections4) deps introduced
* GRANITE-64977: Deprecationtool: match root package as well
* SITES-38099: Fix failing XF IT test
* SITES-39767: Support nonce value via request attribute (CSP)
* SKYOPS-126100: No discovery for mutable content pods on mongo and oakrs
* SKYOPS-126217: Stop using java_v21_oracle_build image during AEM image build
* SKYOPS-128653: Use latest Sling Feature Extension Apiregion in FACT
* SKYOPS-129301: Set APIs jar javadoc compliance level to 17
* SKYOPS-129351: Update reactive-streams and reactive-core for MCP SDK
* SKYOPS-131325: Bump fact tool to 0.6.18
* SKYOPS-131405: Remove bundle toggle for Netcentric AC Tool
* SKYOPS-131412: [Quickstart] update org.apache.commons:commons-exec
* SKYOPS-131432: [Quickstart] Update Felix SCR to 2.2.14
* SKYOPS-131907: [Quickstart] Update Sling API region bundle
* SKYOPS-131938: [Quickstart] Update GSON
* SKYOPS-132151: Update API Deprecation dates
* SKYOPS-132173: [Quickstart] update commons-codec
* SKYOPS-132182: [Quickstart] Update Sling Tenant
* SKYOPS-132267: [Quickstart] update org.osgi.service.component
* SKYOPS-132272: [Quickstart] update sling feature model bundle
* SKYOPS-132525: Add analyser to quickstart that prevents new API removals
* SKYOPS-13927: Flaky Test Detection: update dependency


### Fixed Issues {#fixed-issues-AAA}

* GRANITE-64422: [6.5 + LTS] Tests failing on LTS SP2 upgraded setup
* GRANITE-64443: workflow.core is using outdated log4j
* GRANITE-64543: Permission restrictions response; update security.user dependency
    
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

