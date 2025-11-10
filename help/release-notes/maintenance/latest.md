---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 23282 {#23282}

Summarized below are the continuous improvements for maintenance release 23282, which was publicly released on November 11, 2025. The previous maintenance release was release 22943.

The 2025.11.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

>[!NOTE]
>
>Release 23122 has been made private on November 3rd.

### Enhancements {#enhancements-23282}

* FORMS-21594: Enable Locking of Interactive Communications Template Content & Layout for Content Authors.
* FORMS-20385: Support XDP Editing in Interactive Communications Editor.
* FORMS-10883: Support for JSON with XHTML namespace tags in DoR generation to ensure accurate rendering of rich-text data submitted via APIs.
* FORMS-21751: Canvas Features - Text Overflow, UI for Page Break.
* FORMS-22049: Interactive Communications Editor - Migration to Spectrum 2.
* FORMS-22050: Support for dynamic page numbering in Interactive Communications Editor.
* FORMS-21606: Public OSGi Render SPIs for Interactive Communications.
* FORMS-21613: Transaction reporting and performance logging for Render Interactive Communications SPIs.
* SITES-35092: Content Fragments - New mixin and upgrade procedure for semantic search.
* SITES-32319: Delivery OpenAPI - Support page references.
* SITES-20123: GraphQL: Support superscript elements in JSON response.
* SITES-34744: New "card" property in the Content Fragment response which contains data which can be used for rendering a thumbnail.
* SITES-34571: Allow enumeration fields to be empty.
* SITES-34812: Added capability to retrieve a Content Fragment without its references, by using the "references" parameter with the value "none".
* SITES-35176: Checking out a content fragment via Touch UI now prevents the editing of the content fragment in the new editor by other users.
* SITES-30371: Added support for uuid based reference fields.
* SITES-19309: retrieve a maximum of 150 references when opening the move page wizard.
* SITES-32515: Edge Delivery with Universal Editor - Add support for multi-fields and composite multi-fields (early access).
* SITES-33784: Edge Delivery with Universal Editor - Add support for ld-json in page metadata.
* SITES-34832: Edge Delivery with Universal Editor - Add public path of a page to page info servlet response.
* SITES-25893: Edge Delivery with Universal Editor - Add support for strong and emphasize to text rendering in blocks.
* SITES-26158: Edge Delivery with Universal Editor - Add support for table markup in blocks and columns (early access).
* SITES-27949: Edge Delivery with Universal Editor - Make path mapping optional.
  
* SITES-35811: Use new index in Content Fragments queries
* CQ-4361363:  Latest AEM and Granite translations
* SITES-33206: Update KonMari bundle to 0.0.10
* SKYOPS-120857: Update filevault to 4.1.4
* GRANITE-62169: Update commons-lang to 3.19.0
* SKYOPS-118390: Update JCR Resource to 3.3.6
* GRANITE-62394: Updated joda-time to 2.12.7
* GRANITE-36205: Update Oak release to 1.88.0
* AEMSRE-2896: Disallow the customization of Logging configuration
* GRANITE-62020: Improve retry policy on RepositoryServiceHttpClient
* SKYOPS-121082: Update versions of org.apache.sling.discovery.standalone, org.apache.sling.jcr.packageinit and org.apache.sling.commons.fsclassloader sling bundles

### Fixed Issues {#fixed-issues-23282}

* CQ-4361144: Fixed the skipping of  Content Fragments from Translation Jobs.
* CQ-4355446: Fixed the unlocalised string in Translation project occurring on Cancel translation job dialog.
* SITES-34555: GraphQL - QueryValidationError after deployments.
* SITES-35077: Content Fragments - Unpublish fails for fragments with parentheses due to incorrect URL-encoding.
* SITES-35374: Content Fragments - Edited Content Fragment Disappears After Navigating Back.
* SITES-36130: NPE in `EditorRestrictionsStatusImpl`.
* SITES-35810: NullPointerException in Launches blocks publishEdgeDeliverySubscriber queue.
* SITES-34368: AEM CIF generates 12 GraphQL aliases – exceeds Magento 2.4.6-P12 limit of 10.
* SITES-36193: CCS connector fixes.
* SITES-35169: Resolved issue that would cause incorrect pagination when invalid fragment resources were returned by the search.
* SITES-34574: Fixed an issue where in some cases the cursor would not be returned by the  Content Fragment Search API.
* SITES-35520: Fixed an issue that caused ClassCastException or timeouts when attempting to publish content.
* SITES-35210: Fixed a NullPointerException that would occur when attempting to publish a broken fragment with empty references filter.
* SITES-35933: Fixed a bug that would result in empty "Request for Activation" workflows being triggered after the content fragment was published.
* SITES-35925: Fixed a bug related to patching Content Fragment Models which would delete the "translatable" and "showThumbnail" properties from the model.
* SITES-35409: Fixed a bug that prevented the republishing of adjusted fragments when moving a page.
* SITES-15757: Fixed a bug that prevented the republishing of adjusted pages when moving a page.
* SITES-34638: Fixed a bug where properties from grandparent pages would not be included when creating new versions.
* SITES-35071: CSV export returns unfiltered results when omnisearch uses quoted phrase.
* SITES-32182: Edge Delivery with Universal Editor - fix encoding issues with URLs containing already encoded request parameters.
* SITES-34324: Edge Delivery with Universal Editor - fix rendering of links with a tel: protocol.
* SITES-35333: Edge Delivery with Universal Editor - fix asset rendition selection for images in page metadata.
* SITES-35549: Edge Delivery with Universal Editor - fix double-encoded html entities in page metadata.

* ASSETS-58926: Fix video change thumbnail feature in DM
* GRANITE-61318 : Fix an issue where the page creation wizard only highlights mandatory fields in basic tab
* GRANITE-60514: Fix an issue where stopped scheduled publications during full-stack pipeline run
* CQ-4360747: Fix an issue where Repeatable Translation Jobs create empty payloads & trigger too often
* GRANITE-61019: Fix issue with GC on first run after AEM restart
* ASSETS-58623: Fix npe in omnisearch when config exists
* GRANITE-60456 - Fix issue when administrator open any user's property page

#### AEM Guides {#guides-23282}

* GUIDES-33597: If an empty `prop` element with no attributes or values is added to a DITAVAL file, then additional `prop` elements cannot be added.
* GUIDES-33693: When you re-upload an edited image through the Experience Manager Guides UI, the image's original rendition gets updated but the associated DITA content continues to display the previous version of the image.
* GUIDES-35607: Error logs that are generated while uploading an asset via the Assets UI or creating a new file from the Editor interface, incorrectly use the term `predecessor` instead of `successor` in the log message.
* GUIDES-37649: When publishing a DITA map using baseline on AEM Sites (with legacy component mapping), the map elements with the attribute `processing-role = resource-only` are also getting published.

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 


### Known Issues {#known-issues-23282}

None.

### Deprecated Features and APIs {#deprecated-23282}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-23282}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 30 identified vulnerabilities, reinforcing our commitment to robust system protection.

Security: (TODO: Delete before merge)
GRANITE-62404 : [VULN-32280] Stored XSS injected at "Configuration Folder Name" and triggered at Templates Component Policy
GRANITE-61684 JWTAuthenticationHandler login failure when IMS user is changing email address
CQ-4361221
GRANITE-62115 - Upgrade com.adobe.granite.crypto
GRANITE-61420 : Fix XSS violations: GRANITE-61420, GRANITE-61424, GRA… 
GRANITE-61591
CQ-4361004-and-GRANITE-61417:
GRANITE-60087
GRANITE-60456: Update granite security content package
CQ-4360564: Sanitising project path to prevent XSS injection
CQ-4360577: Sanitising path to prevent Cross site scripting attacks
NPR-42974, CQ-4361221, NPR-43121, NPR-43056

### Embedded Technologies {#embedded-tech-23282}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.88.0|[Oak 1.88.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.88/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.30.2|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
