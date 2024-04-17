---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 15939 {#release-15939}

Summarized below are the continuous improvements for maintenance release 15939, which was publicly released on April 17, 2024. The previous maintenance release was release 15860.

2024.4.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-15939}

* GRANITE-39892: Update distribution for queue size limit and publish ready.
* GRANITE-48777: Update QS to com.adobe.granite.security.user-0.4.84 done.
* GRANITE-49421: Added properties for the segment service principal.
* GRANITE-49855: Write a feature model analyser that fails the Quickstart build in case of new commons.json usage.
* GRANITE-47995: Allow to switch writing of cq:isDelivered.
* GRANITE-36205: Update the internal oak release version to the latest.
* GRANITE-50156 Bind AEMCS affinity to IMS User ID for Universal Editor.
* GRANITE-50556: Upgrade crosswalk bundle to v0.1.18.
* GRANITE-50728: Update FileVault to 3.7.3-T20240308111857-81fa88f1.
* GRANITE-50957: Update QS to com.adobe.granite.repository to 1.8.114.
* GRANITE-50158: Add support for OAuth Server to Server Credential flow in  YAML loader.
* GRANITE-51327: Update Oak to the latest public release (1.62.0).
* SKYOPS-68091 Update Java 11 runtime images to version 3.0.0.
* SKYOPS-70421: Upgrade the org.apache.sling.servlet-helpers bundle
* SKYOPS-73483: Allow logging token on AEM.

### Fixed Issues {#fixed-issues-15939}

* GRANITE-46901: Add metrics to messaging client.
* GRANITE-48793: Update QS to com.adobe.granite.crx-explorer-1.1.28.
* GRANITE-48937: Omniseaarch doesn't work on aem/start.html page.
* GRANITE-49638: Fix wrong content type configuration for the RUM transformer factory.
* GRANITE-50141: IMSProviderImpl is spamming the log.
* SITES-20949: ComponentsIT.testEmbed failing after Youtube added referrerpolicy="strict-origin-when-cross-origin".
* SITES-21233: Core Components update - Fix Accordion for GS1 US after upgrade to 15860.
* SKYOPS-74819: Broken backwards compatibility for duplicate keys in Apache Commons.
* SKYOPS-67087: Clientlib aggregation not working in certain cases.
* CQ-4355415: AEM Notifications links is not working in 6.5 SP18.

### Known Issues {#known-issues-15939}

None.

### Deprecated Features and APIs {#deprecated-15939}

* [JWT Credentials Deprecation in Adobe Developer Console](/help/security/jwt-credentials-deprecation-in-adobe-developer-console.md)

Have a look at [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) to know what has been deprecated or removed in AEM as a Cloud Service.

### Embedded Technologies {#embedded-tech-15939}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.62.0|[Oak API 1.62.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.62.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.24.6|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
