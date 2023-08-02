---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 12874 {#release-12874}
 
Summarized below are the continuous improvements for maintenance release 12874, which was publicly released on Aug 2, 2023. This maintenance release is an update from previous maintenance release 12790.

2023.8.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-12874}

- New version of index definition: `/oak:index/damAssetLucene-9`

  - ASSETS-18351: Switches to insecure facets - to improve search performance
  - ASSETS-17896: Removes Feature Vectors from the index - similarity search based on smart tags
  - ASSETS-8715: Adds null check / not null check for the property "jcr:content/metadata/dam:status"
  - GRANITE-45138: Removes property index from the predicted tags dynamic boost property
  - ASSETS-17614: Adds Scene7 ID as an indexed property (null check and not null check enabled)
  - ASSETS-14516: Adds properties for 'new UI' Trash functionality to the index
  - ASSETS-16270: Adds coalesced title property to the index (for use in sorting)
  - ASSETS-24478: Remove 5 potentially large properties from the index (based on analysis of customer index data)
  - ASSETS-3383: Adds an additional tag 'assetsOmnisearch'

AEM releases 12874 and above contain a new version of the damAssetLucene index (damAssetLucene-9). In order to provide the most responsive search experience, damAssetLucene-9 changes the behaviour of Oak Query result faceting to no longer evaluate access control on the facet counts returned by the underlying search index (referred to as "insecure" mode).

As such, it is possible that users will be presented with facet count values which include assets which the current user does not have access to. This does not allow the user to access, download, or read those assets, nor does it allow the user to gain any further information about the assets' existence.

If the previous behaviour is desired, Customers should follow the steps described in [Content Search and Indexing](/help/operations/indexing.md) to create a custom version of the damAssetLucene-9 index with the previous "statistical" facet mode.

### Fixed Issues {#fixed-issues-12874}

- ASSETS-24379: Made improvements to the ReplicateOnModifyListener.
- ASSETS-25794: Resolved an issue with S7ConfigResolverImpl that caused it to execute an expensive query at startup.
- ASSETS-25473: Fixed a bug where the Quick Publish Option was visible to users without replication permission.
- ASSETS-24803: Addressed an XSS vulnerability in the Viewers feature.
- ASSETS-25489: Corrected an issue where Smart croppings were being downloaded with the wrong suffix.
- ASSETS-25435: Fixed an error where the WidthxHeight fields were missing in the Download for dynamic renditions
- ASSETS-25741: Fixed the absence of a visual asterisk (*) symbol for the mandatory 'width' edit field in the 'Basic' tab section.
- ASSETS-25759: Improved the visibility of focus on dropdown elements in high contrast black/white modes.
- ASSETS-25749: Fixed the issue where focus was not moving to multiple controls below the video when navigating using the keyboard Tab, resulting in them being inaccessible.
- ASSETS-26074: Restored the limit of 127 characters for names of non-video assets.
- ASSETS-21428: Fixed an issue where a Multi Line field in Metadata Schema Editor would overlap the following field
- ASSETS-21989: Fixed an issue CORS headers could be overwritten on 302 and 401 responses, preventing remote DAM login
- ASSETS-22603: Fixed issues affecting column names and values when viewing Asset Download Reports
- ASSETS-23120: Fixed an issue in AssetSetLastModifiedProcess related to leaking resource resolvers
- ASSETS-25456: Fixed an issue where an Asset with a long name prevents clicking actions in the Asset Properties Editor
- ASSETS-25832: Fixed Issue with relating assets from a full access folder to read only access folder.
- ASSETS-25397: Fixed an issue where the new name of an Asset renamed in the new UI would not be reflected in search results
- ASSETS-26102: Fixed an issue that could prevent uploads from CI Hub connector
- ASSETS-26172: Reduced the size of Bulk Import progress log content saved in persistent Sling Job nodes
- ASSETS-26292: Deprecated AssetManager createOrUpdateAsset() and createOrReplaceAsset() methods in the Java API
- ASSETS-26399: Fixed an issue preventing collections from being published to Brand Portal
- ASSETS-26533: Fixed an issue in Indesign Server Integration that could lead to a timeout for long processing requests
- ASSETS-26549: Fixed an issue in Assets List View which caused "External User" to be displayed as the last modified user for all uploaded assets
- ASSETS-26551: Resolved an issue in which Assets deleted on author were not unpublished
- ASSETS-26571: Fixed an issue with the Assets Reports page in which the page would fail to load if multiple failed report jobs were present in the list
- ASSETS-26147: Fixed an issue where Unified Shell would attempt to redirect an iframe into /ui when window.top.opener is set but not window.opener
- ASSETS-26576: Fixed an issue with Dropbox Import in which the incorrect folder hierarchy was created
- ASSETS-26671: Fixed an issue preventing Bulk Import from including files located within a DCIM folder
- ASSETS-26700: Fixed an issue in which saving a Public folder’s properties page with no changes would creates 3 unnecessary groups
- CQ-4353449: Fixed an issue that allowed users with read-only Tagging permissions to create tags using the Tagging UI
- GRANITE-46601: Fixed an issue preventing the Quickstart SDK from starting up on JDK 11.0.20
- SKYOPS-33168: Fixed an issue in CM Developer Console that prevented loading of /content/dam for asset names without extension
- SKYOPS-61484: Fixed an issue in the RDEProvider service that allowed unsubstituted ${sling.home} tokens to persist in merged OSGi configurations
- Various security, accessibility, and localization fixes

### Known Issues {#known-issues-12874}

- GRANITE-46851: Test connection in content distribution does not work

### Embedded Technologies {#embedded-tech-12874}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.52-T20230629133256-25c01b8|[Oak API 1.52.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.52.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
