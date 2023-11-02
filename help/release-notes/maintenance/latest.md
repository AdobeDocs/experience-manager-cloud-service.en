---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 14029 {#release-14029}

Summarized below are the continuous improvements for maintenance release 14029, which was publicly released on October 25, 2023. This maintenance release is an update from previous maintenance release 13804.

2023.11.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-14029}

* ASSETS-28551: Improve scalability of My Link Shares UI
* ASSETS-28566: Add dam:metadataForm Lucene index
* ASSETS-29281: Update RAPI to send v2 download events

### Fixed Issues {#fixed-issues-14029}

* ASSETS-25199: image core component not showing right smart crops
* ASSETS-26142: unified-shell.js customEnvLabel not set or reattempted if discovery request fails or is interrupted
* ASSETS-26416: Relative Date Predicate always defined as "1 day(s) ago" in Search Form
* ASSETS-27321: clear group cache on team membership changes
* ASSETS-27591: Fix dependency on old org.json
* ASSETS-28439: Smart tags Blocklist NPE when global block list is not configured
* ASSETS-28612: BlockedTagResolver fix in "repository-api"
* ASSETS-28634: Omnisearch field in Adobe stock doesn't get asset data added automatically
* ASSETS-28727: Processing Profile Configuration list does not show the specified custom height and width values
* ASSETS-29056: Add transcoding renditions AEM standard processing profile
* ASSETS-29105: Restriction provider missing from SecurityProviderRegistration requiredServicePids in RDE feature model
* ASSETS-29106: View on Adobe stock throws error on unified shell enabled AEM
* ASSETS-29115: Remove configuration property for Restriction Provider paths
* ASSETS-29208: Errors on asset upload caused by requests sent to an author pod before service CompleteUploadAssetServlet is registered
* ASSETS-29297: Issue while creating Save search with checked out filter option
* ASSETS-29363: Metadata profile not applying default values for IPTC
* ASSETS-29404: Link Shares report hitting query limit
* ASSETS-29431: Remove old feature flags
* ASSETS-29443: Unified Shell Hero Remains Visible and Clickable when Granite Shell Header Mode changes to "selection"
* ASSETS-29476: scene7DAMService.getS7FileReference(asset) Api call does not return the expected value. 
* ASSETS-29515: Assets / Nodes with "jcr:lastModifiedBy": "workflow-process-service" show as "external user" in list view
* ASSETS-29579: NonAdmin users unable to create Image Set
* ASSETS-29631: Use dam:roles for secure delivery/search
* ASSETS-29689: dc:roles (and the new property dam:roles) should be filtered from AEM side
* ASSETS-29738: Asset Upload Restriction fails with NullPointerException
* ASSETS-29779: Small assets cannot get processed to webp because not in blob storage
* ASSETS-29892: Metadata export is failing on folder with large number of assets
* ASSETS-29996: "External User" as modifier when uploading assets intermittently only on PROD instance
* ASSETS-30167: HTML for adobe_dam:restrictions breaks after uploading an asset
* ASSETS-30276: Share Link UI: can not share from assetdetails
* ASSETS-30434: Asset processing completed event not sent to Pipeline
* ASSETS-30519: Add RAPI to REDMetricsServletFilter
* CQ-4354413: QueryBuilder: queries with square brackets are wrongly translated to xpath
* CQ-4354834: Unable to add comment in inbox task
* CQ-4354836: Unable to start Workflow or Create Task from Projects Console
* CQ-4354867: ToggleCondition reference refers to non-existent field in InstanceActionServlet
* CQ-4354895: AEM Translation Kit: October 12
* GRANITE-45560: Common schema representation in Eventing envelope
* GRANITE-47267: Update to Apache Felix Http Jetty 4.2.18
* GRANITE-47599: Content imports fail since 13323 upgrade (JCRVLT-721)
* GRANITE-47873: Update to Apache Felix Webconsole 4.9.6

### Known Issues {#known-issues-14029}

* ASSETS-31015: Unable to upload files to Assets with unknown file extensions.

### Embedded Technologies {#embedded-tech-14029}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.56-T20230927085643-189caed|[Oak API 1.56.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.56.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
