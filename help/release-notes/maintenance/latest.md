---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 16145 {#release-16145}

Summarized below are the continuous improvements for maintenance release 16145, which was publicly released on May 1, 2024. The previous maintenance release was release 15977.

2024.4.0 Feature Activation provides the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-16145}

* ASSETS-23489: Repository insights enhancements.
* ASSETS-26926: Dynamic Media upload polling improvements.
* ASSETS-30351: Download dialog should load Dynamic Media rendition sizes asynchronously.
* ASSETS-30379: Improve resolution of DRM licences in download.
* ASSETS-31058: Surface smart crop renditions in AEM assets UI in renditions tab and generate smart cropped images when user clicks on these renditions.
* ASSETS-31218: Add support for named smartcrop in assets delivery api.
* ASSETS-31979: Add visual indicator and disable UI functions during Async Assets operations.
* ASSETS-32735: Improvements to asset metadata updated event.
* ASSETS-34661: API for DM Preview and/or Delivery URLs from AEMaaCS Publish.
* ASSETS-37259: XMP parsing improvements.
* ASSETS-37263: Allow cancellation of failing Assets async jobs.
* CNTBF-114: Content backflow improvements.
* CNTBF-148: Content backflow improvements.
* CQ-4356992: Latest AEM and Granite translations.
* SITES-19326: Update links in Assets UI to open CF in new CF Editor.
* SITES-20686: GraphQL - Expose Dynamic Media URL via _dmS7Url (for non-images assets).
* SKYOPS-68091: Update to Java 11.0.20.

### Fixed Issues {#fixed-issues-16145}

* ASSETS-32321: Post-Processing workflow resolution fails if ancestor folder is missing 'jcr:content' subnode.
* ASSETS-33856: JPEG Image Preset downloads file as TXT.
* ASSETS-34096: Fix Touch UI view for async download report.
* ASSETS-34493: Failure while loading download dialog box after enabling multi company feature toggle.
* ASSETS-34824: Copy url shows empty for DM disabled folders.
* ASSETS-35226: Post-Processing workflow not resolved if specified on the DAM root.
* ASSETS-35559: Reduce DM Batch Upload failure log to WARN.
* ASSETS-35860: Incorrect Time Zone Conversion in AEM Assets Column View.
* ASSETS-35935: Incorrect folder navigation after closing payload review.
* ASSETS-35961: Add crop button is not working under image profile.
* ASSETS-36227: Disable FolderPreviewUpdaterImpl service on publish.
* ASSETS-36943: Miss aligned columns when CF and other non CF items are present in a folder in list view.
* ASSETS-36990: Exported metadata jobs failing / slow with large number of properties.
* ASSETS-37113: Reprocess Assets job terminates immediately if query returns only CF results.
* ASSETS-37260: Metadata Export in AEM can produce invalid CSV.
* ASSETS-37261: PPTx and PDF Annotation Issue on AEM Assets.
* ASSETS-37282: Potential slow request opening large folder.
* ASSETS-37330: Bulk Import from OneDrive creates incorrect AEM Folder Structure.
* ASSETS-37609: Remove legacy scene7 conf lookup.
* ASSETS-38016: Some metadata updates are not properly tracked in events.
* CQ-4357161: AEM Inbox Payload screen is returning 404.
* GRANITE-50041: Add Rendition is not working when resolution is more then 1440px width when only "Add Rendition" option is in the dropdown option.
* GRANITE-50279: Disordered Week Names in Coral Datepicker Component.
* SCRNS-3949: Screens channel fetch request time is too long.
* SCRNS-3981: [Sequence channel] Black screen resulted when the sequence of element load/unload events get distorted.
* SCRNS-4180: [Sequence channel] Sequence stops with a Blank screen for channels with videos of duration -1 upon recovery from fallback thumbnail.
* SCRNS-4245: [Sequence channel] Limited duration of Blank screen when a video is loaded & switched from fallback thumbnail.
* SITES-16055: Fix Live Copy and Live Copy Source links within respective properties page.
* SCRNS-4243: Missing buttons in Content Provider for Non-Admin users.

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
