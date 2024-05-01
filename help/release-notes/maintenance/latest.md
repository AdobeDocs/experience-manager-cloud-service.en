---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 16145 {#release-16145}

Summarized below are the continuous improvements for maintenance release 16145, which was publicly released on May 2, 2024. The previous maintenance release was release 15977.

2024.4.0 Feature Activation provides the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-16145}

* ASSETS-23489: Repository insights enhancements.
* ASSETS-26926: Dynamic Media upload polling improvements.
* ASSETS-30351: Download dialog should load Dynamic Media rendition sizes asyncronously
* ASSETS-30379: Improve resolution of DRM licences in download
* 
### Fixed Issues {#fixed-issues-16145}


* ASSETS-31058: 	Surface smart crop renditions in AEM assets UI in renditions tab and generate smart cropped images when user clicks on these renditions
* ASSETS-31218: ***-*** 
* ASSETS-31979: ***-*** ASSETS-37263 update com.adobe.granite.jobs.async:1.1.44, com.adobe.granite.jobs.async.ui.commons:1.1.0.
* ASSETS-32148: ***-*** guava replacement with ehcache in approved-assets.
* ASSETS-32321: ***-*** Update to cq-dam-core 5.15.98. Issue fixed: ASSETS-32321.
* ASSETS-32596: ***-*** Update rotary to latest RAPI release * ASSETS-32596 - Update assets rotary to latest RAPI.
* ASSETS-32735: ***-*** Updated eventing bundle version.
* ASSETS-33148: ***-*** Add scene7File property in polaris asset metadata.
* ASSETS-33243: ***-*** Updated cq-dam-content version.
* ASSETS-33537: ***-*** Update dynamic media content package.
* ASSETS-33856: ***-*** adding loggers for download issue.
* ASSETS-34012: ***-*** Allow image profile with smartcrop defn with polaris FT.
* ASSETS-34096: ***-*** Update to cq-dam-commons 5.13.316. Issue fixed: ASSETS-34096. * Update to cq-dam-content-sdk 1.0.20, cq-dam-content 2.6.1650. Issue fixed: ASSETS-34096.
* ASSETS-34493: ***-*** adding exclusions * ASSETS-34493: adding exclusions (#35402) * ASSETS-34493 : fixes for mutli company merged to rotary.
* ASSETS-34661: ***-*** securely access DM Preview and/or Delivery URLs.
* ASSETS-34747: ***-*** adding a new service user that has read access to oak:index * ASSETS-34747 changing dam to oak.
* ASSETS-34824: ***-*** Adding exclusion for sidepanels file.
* ASSETS-34846: ***-*** fix for DM general settings page failure to load due to invalid cache object.
* ASSETS-35226: ***-*** Update to cq-dam-core 5.15.100. Issue fixed: ASSETS-35226.
* ASSETS-35289: ***-*** [Polaris] Add support to pick properties/nodes from child nodes of metadata node in AEM to be included in embedded metadata.
* ASSETS-35525: ***-*** MissingMetadataNotificationJob throws on deactivate.
* ASSETS-35557: ***-*** Added bundle cq-dam-index-reader-bundle-injection-adapter * ASSETS-35557 updating rapi to fix package import issue.
* ASSETS-35559: ***-*** Reduce DM Batch Upload failure log to WARN.
* ASSETS-35587: ***-*** Deleting a smartcrop from image profile applied on a folder does not delete it from cosmos for child assets (no RTC).
* ASSETS-35860: ***-*** Updated cq-dam-content version.
* ASSETS-35935: ***-*** update cq-inbox-content-1.3.130, cq-dam-content-2.6.1652.
* ASSETS-35961: ***-*** Add crop button is not working under image profile.
* ASSETS-36043: ***-*** updating the platform test bundle version.
* ASSETS-36103: ***-*** ASSETS-26926, ASSETS-36103: dm poller enhancement and guava fixes * ASSETS-36103: removal of guava dependent api * ASSETS-36103 : version correction for scene7-api and model.
* ASSETS-36227: ***-*** disable FolderPreviewUpdaterImpl for publish.
* ASSETS-36943: ***-*** Updated cq-dam-cfm-content package version.
* ASSETS-36984: ***-*** Update unified-shell-integration-content to v1.0.98.
* ASSETS-36990: ***-*** Update to cq-dam-content 2.6.1654, cq-dam-core 5.15.102. Issues fixed: ASSETS-37282, ASSETS-36990, ASSETS-37260.
* ASSETS-37032: ***-*** Add expiration date to event asset metadata.
* ASSETS-37113: ***-*** exclude CF + no original rendition from folder reprocess.
* ASSETS-37259: ***-*** [ASSETS-37448] Only ask for C2PA flags when feature flag is set [ASSETS-37259] Parse new C2PA-related XMP properties as booleans.
* ASSETS-37260: ***-*** Update to cq-dam-content 2.6.1654, cq-dam-core 5.15.102. Issues fixed: ASSETS-37282, ASSETS-36990, ASSETS-37260.
* ASSETS-37261: ***-*** PPTx and PDF Annotation Issue on AEM Assets.
* ASSETS-37263: ***-*** ASSETS-31979 ASSETS-37263 update com.adobe.granite.jobs.async:1.1.44, com.adobe.granite.jobs.async.ui.commons:1.1.0.
* ASSETS-37282: ***-*** Update to cq-dam-content 2.6.1654, cq-dam-core 5.15.102. Issues fixed: ASSETS-37282, ASSETS-36990, ASSETS-37260.
* ASSETS-37330: ***-*** Fix OneDrive path bug.
* ASSETS-37448: ***-*** [ASSETS-37448] Only ask for C2PA flags when feature flag is set [ASSETS-37259] Parse new C2PA-related XMP properties as booleans.
* ASSETS-37598: ***-*** Including xcm:keywords tagId in asset metadata in delivery tier * ASSETS-37598: Including xcm:keywords tagId in asset metadata in delivery tier behind a config.
* ASSETS-37609: ***-*** Remove legacy scene7 conf lookup.
* ASSETS-37738: ***-*** index-reader add null check related attributes * ASSETS-37738 retrigger.
* ASSETS-37859: ***-*** IMS Client for Frame.io Native Integration.
* ASSETS-38016: ***-*** Fix changes to metadata not appearing in metadata updated events.
* CNTBF-114: ***-*** [import_v2] contentbackflow version 1.0.42.
* CNTBF-148: ***-*** contentbackflow v2.0.8.
* CQ-4350419: ***-*** Fix for generating existing JWT configs from keystore.
* CQ-4356632: ***-*** [Removal] cq-content-sync leaks Guava into public API.
* CQ-4356992: ***-*** latest AEM and Granite translations.
* CQ-4357161: ***-*** AEM Inbox Payload screen is returning 404.
* GRANITE-50041: ***-*** SKYOPS-75665: revert GRANITE-50279 + GRANITE-50041.
* GRANITE-50279: ***-*** SKYOPS-75665: revert GRANITE-50279 + GRANITE-50041.
* GS-82: ***-*** Enable genstudio client id.
* SITES-16055: ***-*** update cq-experience-fragments-content sidecar to 1.3.152.
* SITES-19326: ***-*** Update to cq-dam-content 2.6.1638. Issue fixed: SITES-19326.
* SITES-20686: ***-*** add dm url for docs and videos.
* SITES-20949: ***-*** ComponentsIT.testEmbed failing after Youtube added referrerpolicy="strict-origin-when-cross-origin" * SITES-20949 upgrade core.wcm.components.it.http to 2.24.6.
* SKYOPS-68091: ***-*** Update to Java 11.0.20 * SKYOPS-68091 Update to Java 11.0.20 - simplifying tests * SKYOPS-68091 Update to Java 11.0.20 - test fix * SKYOPS-68091 Update to Java 11.0.20 - test fix 2 * SKYOPS-68091 Update to Java 11.0.20 - test fix 4.
* SKYOPS-72490: ***-*** revert SKYOPS-72490 * revert SKYOPS-72490.
* SKYOPS-74206: ***-*** Revert "SKYOPS-74206 : Enable RUM for customers with custom rewriter pipeline configuration [INTERNAL]" * Revert "Revert "SKYOPS-74206 : Enable RUM for customers with custom rewriter pipeline configuration [INTERNAL]"".
* SKYOPS-75484: ***-*** [RUM] Implement tracking 404 checkpoints * Revert: SKYOPS-75484 : [RUM] Implement tracking 404 checkpoints.
* SKYOPS-75665: ***-*** revert GRANITE-50279 + GRANITE-50041.


### Known Issues {#known-issues-16145}

None.

### Deprecated Features and APIs {#deprecated-16145}

* [JWT Credentials Deprecation in Adobe Developer Console](/help/security/jwt-credentials-deprecation-in-adobe-developer-console.md)

* Effective May 1, 2024, Adobe Dynamic Media is ending support for the following:

  * SSL (Secure Socket Layer) 2.0
  * SSL 3.0 
  * TLS (Transport Layer Security) 1.0 and 1.1
  * The following weak ciphers in TLS 1.2:
    * `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`
    * `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`
    * `TLS_RSA_WITH_AES_256_GCM_SHA384`
    * `TLS_RSA_WITH_AES_256_CBC_SHA256`
    * `TLS_RSA_WITH_AES_256_CBC_SHA`
    * `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`
    * `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`
    * `TLS_RSA_WITH_AES_128_GCM_SHA256`
    * `TLS_RSA_WITH_AES_128_CBC_SHA256`
    * `TLS_RSA_WITH_AES_128_CBC_SHA`
    * `TLS_RSA_WITH_CAMELLIA_256_CBC_SHA`
    * `TLS_RSA_WITH_CAMELLIA_128_CBC_SHA`
    * `TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA`
    * `TLS_RSA_WITH_SDES_EDE_CBC_SHA`


To know what is deprecated or removed in AEM as a Cloud Service, see [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md).

### Embedded Technologies {#embedded-tech-16145}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.62.0|[Oak API 1.62.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.62.0/index.html)| 
|AEM SLING API | 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.24.6|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
