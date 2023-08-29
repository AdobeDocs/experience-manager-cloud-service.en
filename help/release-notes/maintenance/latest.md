---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 13239 {#release-13239}

Summarized below are the continuous improvements for maintenance release 13239, which was publicly released on August 29, 2023. This maintenance release replaces release 13206.

2023.9.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-13239}
- GRANITE-46784 - Add option to disable BearerAuthenticationHandler
- GRANITE-36205 - Update internal oak release version to latest
- GRANITE-43908 - Jackson-databind-2.13.4.jar embeds vulnerable jackson-databind
- GRANITE-47059 - Remove Granite Jetty SSL Bundle
- ASSETS-26713 - Touch UI External Link to New Experience UI Dashboard - unified-shell-integration and ui-touch-optimized upgraded
- SKYOPS-63302 - Upgrade com.adobe.granite:com.adobe.granite.auth.saml to v1.0.54
- GRANITE-46634 - Upgrade to eventing client 1.4.0
- GRANITE-46788 - Update Apache Commons Libraries
- GRANITE-29211 - Update tooling to Sling Feature Model 2.0
- GRANITE-46705 - Update to Apache Felix Http Jetty 4.1.14
- GRANITE-46631 - Update Jackrabbit version to 2.20.11
- SKYOPS-61895 - Update to Jackrabbit Filevault 3.7.0

### Fixed Issues {#fixed-issues-13239}
- SKYOPS-63290 - Fixed incorrect evolution of buckets
- SKYOPS-54607 - Ratelimiter serverload computation not correct for request that failed
- ASSETS-27648 - ContentModelIT fails to read exclusion files from other bundles
- GRANITE-43160 - Sling Error Handler overwrites Content-Type
- GRANITE-43744 - Sling Authenticator does not work properly if there is misconfiguration with authentication-requirement and vanity path
- GRANITE-46419 - AEM integration issue with Auth0 Idp
- GRANITE-46292 - Okta SAML configuration not working after AEM Cloud update

### Known Issues {#known-issues-13239}

None.

### Embedded Technologies {#embedded-tech-13239}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.54-T20230817132355-3800a65|[Oak API 1.54.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.54.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.2|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
