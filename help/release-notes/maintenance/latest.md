---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 13323 {#release-13323}

Summarized below are the continuous improvements for maintenance release 13323, which was publicly released on September 1, 2023. This maintenance release replaces release 13239.

2023.9.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-13323}

- GRANITE-46784: Add option to disable BearerAuthenticationHandler.
- GRANITE-36205: Update internal oak release version to latest.
- ASSETS-26713: Touch UI External Link to New Experience UI Dashboard - unified-shell-integration and ui-touch-optimized upgraded.
- SKYOPS-63302: Upgrade com.adobe.granite:com.adobe.granite.auth.saml to v1.0.54.
- GRANITE-46634: Upgrade to eventing client 1.4.0.
- GRANITE-46788: Update libraries to Apache Commons IO 2.13.0, Commons Lang 3.13.0, Commons Code 1.16.0 and Commons Compress 1.23.0.
- GRANITE-46705: Update to Apache Felix Http Jetty 4.1.14.
- GRANITE-46631: Update Jackrabbit version to 2.20.11.
- SKYOPS-61895: Update to Jackrabbit Filevault 3.7.0.

### Fixed Issues {#fixed-issues-13323}

- ASSETS-28461: Doc cloud viewer not working for PDFs, fixed from 13239.
- SKYOPS-63290: Fixed incorrect evolution of buckets.
- SKYOPS-54607: Ratelimiter serverload computation not correct for request that failed.
- ASSETS-27648: ContentModelIT fails to read exclusion files from other bundles.
- GRANITE-43744: Sling Authenticator does not work properly if there is misconfiguration with authentication-requirement and vanity path.
- GRANITE-46419: AEM integration issue with Auth0 Idp.
- GRANITE-46292: Okta SAML configuration not working after AEM Cloud update.
- GRANITE-47059: Remove Granite Jetty SSL Bundle.

### Known Issues {#known-issues-13323}

- SITES-15622: GraphQL - Issue with persisted queries with number & boolean parameters.
- SITES-15654: GraphQL - Issues with unions and properties of same name.

### Embedded Technologies {#embedded-tech-13323}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.54-T20230817132355-3800a65|[Oak API 1.54.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.54.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.2|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
