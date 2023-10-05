---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 13712 {#13712}

Summarized below are the continuous improvements for maintenance release X, which was publicly released on September X, 2023. This maintenance release replaces release 13665.

2023.10.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-X}

[GRANITE-47123] set default for vanity path async init to "true"
[GRANITE-47028] Send extra clone-blob-store job logs to splunk
[SKYOPS-61375]  grok-httpderror-aem-metrics container doesn't start on arm64
[GRANITE-47199]  update to org.apache.sling:org.apache.sling.tracer:1.0.8
[GRANITE-47247] Update Servlets Resolver to 2.9.14
[CQ-4354373]  Update contentbackflow-fluent-bit to 0.0.8
[SKYOPS-63925] TransformJob failed JDK 11 - ZipException: Invalid CEN header
[SKYOPS-63361] Transform Job logs not containing error details on failed CUSTOMER_EXTRACT substep
[GRANITE-47422] Update Jackrabbit version to 2.20.12
[GRANITE-47288] Extract clone-blob-store chart
[SKYOPS-15023] Part of logs are lost in splunk for a terminating pod
[SKYOPS-54358] Build for lusotycoon/apache-exporter multiarch container 
[GRANITE-47238] Update purge cronjobs to use the customer configuration
[GRANITE-47376] Remove scope= ServiceScope.PROTOTYPE in PrometheusPullServlet annotation NEW
[GRANITE-47267] Update to Apache Felix Http Jetty 4.2.18 (Bug Fix Release)
[SKYOPS-64103] Reduce or truncate unreasonable clientlib error/warnings
[GRANITE-45752] clone-blob-store sometimes failing to copy .brf files  
[GRANITE-47424] Extract restore publish wrapper job to publish-farmer-k8s-base
[GRANITE-47136] index-downloader: disable checksum validation CODE COMPLETE
[SKYOPS-64031] [RDE] ComponentCacheImpl can get into inconsistent state due to duplicate ResourceResolverFactory registration  
[ASSETS-29105] Restriction provider missing from SecurityProviderRegistration requiredServicePids in RDE feature model
[GRANITE-46618] Improve startup speed of publish in case of many replication status messages in kafka (through batching)
[GRANITE-47697] Update QS to Oak 1.56-T20230921122324-f8a06bc
[SKYOPS-63976] TA must be able to authenticate in all regions
[AEMSRE-1244] Introduce new monitoring labels for sla4, multi region,hipaa
[GRANITE-47211] Changes in cq-quickstart


### Fixed Issues {#fixed-issues-X}

[GRANITE-44674] Datepicker required field functionality is incorrect

### Known Issues {#known-issues-X}

None.

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.54-T20230817132355-3800a65|[Oak API 1.54.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.54.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.2|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
