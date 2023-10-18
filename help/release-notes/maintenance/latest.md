---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 13804 {#release-13804}

Summarized below are the continuous improvements for maintenance release 13804, which was publicly released on October 10, 2023. This maintenance release is an update from previous maintenance release 13665.

2023.10.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-13804}

* GRANITE-47238: Audit Log Maintenance - Purge cronjobs to use the customer configuration.
* GRANITE-47123: Publish (Sling) - Improve startup time by initializing vanity path cache asynchronously by default.
* GRANITE-46618: Publish (Replication) - Improve Publish startup speed through replication status messages batching.
* GRANITE-47136: Indexing (Download) - Improve download speed of new parallel index downloader (by disabling checksum validation).
* GRANITE-47211: Publish (Infra) - Improve decoupling of Publish tier deployments (by storing and fetching segment store revision name).
* GRANITE-47267:  Update to Apache Felix Http Jetty 4.2.18 (includes bug fix for request parameter handling ([FELIX-6625](https://issues.apache.org/jira/browse/FELIX-6625)) with performance improvements for local and RDE developments).
* GRANITE-47247: Update to Sling Servlets Resolver 2.9.14 with performance improvements in servlet resolution.

### Fixed Issues {#fixed-issues-13804}

* GRANITE-47376: Author (Infra) - Fix for DiscoveryTopologyUndefined errors after rolling restart.
* CQ-4353436: AEM Web Console (Sling) - Empty configurations in ServiceUserMapperImpl Validators (Principal/User) breaks AEM Instance ([SLING-11912](https://issues.apache.org/jira/browse/SLING-11912)).
* SKYOPS-63925: Transform Job - Avoid TransformJob failures with JDK 11 - ZipException: Invalid CEN header errors (with disableZip64ExtraFieldValidation JVM flag).
* SKYOPS-63361: Transform Job (Logging) Improved logging with Transform Jobs (CUSTOMER_EXTRACT substep).
* SKYOPS-64103: FACT Tool (Logging) - Reduce, or truncate Clientlib compilation error and warning messages.
* SKYOPS-65109: FACT Tool (Error Handling) - Content Packages with unresolved dependencies results in a properly reported error.
* SKYOPS-65368: FACT Tool (Error Handling) - Tool runs into endless inclusion cycle and eventually times out on circular embeds of Clientlibs.
* SKYOPS-64031: RDE - ComponentCacheImpl can get into inconsistent state due to duplicate ResourceResolverFactory registration ([SLING-12019](https://issues.apache.org/jira/browse/SLING-12019)).
* ASSETS-29105: RDE - Restriction provider missing from SecurityProviderRegistration requiredServicePids in RDE feature model.
* GRANITE-44674: CoralUI - Datepicker required field functionality is incorrect.

### Known Issues {#known-issues-13804}

* CQ-4354836: Unable to start Workflow or Create Task from Projects Console.
* CQ-4354834 : Users are unable to add comments in an inbox task. 

### Embedded Technologies {#embedded-tech-13804}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.56-T20230927085643-189caed|[Oak API 1.56.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.56.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
