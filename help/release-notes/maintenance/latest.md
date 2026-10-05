---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 28702 {#release-28702}

Summarized below are the continuous improvements for maintenance release 28702, which was publicly released on October X, 2026. The previous maintenance release was release 28386.

The 2026.10.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.


### Enhancements {#enhancements-28702}

* ASSETS-54428: Added search events for asset searches through author OpenAPI.
* ASSETS-60359: Added tagging APIs for asset management.
* ASSETS-62685: Improved asset searches that use tags.
* ASSETS-64331: Added asynchronous asset copying through the Assets API.
* ASSETS-64375: Added task search through the Assets API.
* ASSETS-64384: Added APIs to update collection items and improved handling of collection jobs.
* ASSETS-64385: Added an API to delete collections.
* ASSETS-64386: Added collection search through the Assets API.
* ASSETS-64728: Added asynchronous metadata export through the Assets API.
* ASSETS-64763: Added endpoints to check asset download job status and retrieve completed downloads.
* ASSETS-67662: Added asset events for metadata updates, asset deletions, and asset moves.
* ASSETS-67807: Reduced video reprocessing time by skipping redundant Dynamic Media encodes when the video profile is unchanged.
* ASSETS-68147: Added viewer preset editing and support in the new video viewer.
* ASSETS-68244: Added support for relative date ranges in asset search queries.
* ASSETS-69200: Added image width and height metadata for custom renditions uploaded through the API.
* ASSETS-69206: Added asynchronous bulk tag creation through OpenAPI.
* ASSETS-70436: Expanded collection APIs with smart collection and collection metadata support.
* ASSETS-70449: Added an API to delete named asset renditions.
* ASSETS-74710: Added metadata export support for nested properties and arrays of objects.
* ASSETS-75083: Added metadata import support for nested properties and arrays of objects.
* ASSETS-75722: Added a full-page editor for video chapters and overlays.
* ASSETS-75926: Added viewer preset publishing with support for custom CSS.
* ASSETS-76834: Added chapters and overlays to the new video viewer.
* ASSETS-76836: Included video interactivity metadata in asset delivery responses.
* ASSETS-76838: Enabled the video viewer to load chapters and overlays from asset metadata.
* ASSETS-77191: Added support for seconds in Dynamic Media countdown timers.
* ASSETS-77247: Added a Content Credentials indicator in the Assets Admin UI.
* ASSETS-77355: Added video viewer preset options for environments using Dynamic Media with OpenAPI.
* ASSETS-77388: Improved bulk asset approval management, including stopping reapproval operations and cleaning up completed batches.
* ASSETS-77408: Added collection searches as a source for smart collections.
* ASSETS-77669: Added support for custom properties in the dam namespace in asset delivery.
* ASSETS-77856: Improved template font matching using PostScript font names.
* ASSETS-77995: Added an API to manage metadata-driven permissions for prompts.

### Fixed Issues {#fixed-issues-28702}

* ASSETS-24897: Corrected the publication status icon for published assets.
* ASSETS-31575: Localized invalid JSON path error messages in metadata schemas.
* ASSETS-32768: Corrected the alignment of the Clear All button in folder metadata rules.
* ASSETS-33287: Localized processing profile labels.
* ASSETS-36070: Localized the promoted tag label.
* ASSETS-39418: Localized text in asset share links.
* ASSETS-40698: Corrected vertical button text in shared asset downloads.
* ASSETS-40735: Corrected number formatting in shared asset downloads.
* ASSETS-43105: Corrected Japanese text orientation in list headers.
* ASSETS-43307: Localized the Scheduled for Later label in asset column view.
* ASSETS-46298: Corrected date formatting in asset list view.
* ASSETS-47155: Fixed the related asset selector for filenames containing spaces.
* ASSETS-48196: Localized the Locale column labels in asset list view.
* ASSETS-49527: Fixed interactive media hotspot popups appearing behind images.
* ASSETS-52795: Preserved asset identifiers when replacing assets.
* ASSETS-60894: Corrected video profile column header alignment in folder properties.
* ASSETS-74349: Disabled the Download button when no valid assets or renditions are selected.
* ASSETS-75539: Fixed Dynamic Media templates failing to update after their source PSD assets are reprocessed.
* ASSETS-76596: Fixed Adobe Stock imports selecting watermarked previews instead of licensed assets.
* ASSETS-76711: Fixed metadata dropdown rules when multiple values are selected.
* ASSETS-76893: Fixed assets remaining in AI processing in folders configured for Dynamic Media publishing.
* ASSETS-76949: Excluded hidden folders from Folders API results.
* ASSETS-77205: Fixed rerunning asset reports that contain multiple custom properties.
* ASSETS-77434: Fixed metadata API updates using legacy property paths or changes between single-valued and multivalued properties.
* ASSETS-78492: Fixed page editing failures caused by broken smart crop videos.
* ASSETS-78526: Fixed failures when appending metadata through the bulk metadata editor.
* ASSETS-78540: Fixed AI processing failures when a prompt's target property is unavailable.
* ASSETS-78569: Fixed Content Hub searches failing when custom metadata fields are missing.
* ASSETS-78815: Fixed metadata export headers for reimporting data and added support for exporting object arrays.
* ASSETS-78925: Fixed downloads of very large assets.
* ASSETS-79022: Fixed intermittent Smart Tags training failures caused by missing authentication configuration.
* ASSETS-79238: Fixed missing property names and descriptions in processing profiles.
* CQ-4336103: Localized the Multi Path Value Property Predicate label in asset search.
* SITES-45043: Fixed incorrect Content Fragment references in legacy asset search.
* SITES-50482: Restored PDF asset references from custom download and link list components.


### Known Issues {#known-issues-28702}

To be confirmed before publication.

### Deprecated Features and APIs {#deprecated-28702}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-28702}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release includes 17 security fixes.

### Embedded Technologies {#embedded-tech-28702}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.6.0 | [Oak 2.6.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.6.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.67 | [Apache Httpd 2.4.67](https://apache.googlesource.com/httpd/+/refs/tags/2.4.67/CHANGES)|
|Dispatcher|2.0.275||
|AEM Core Components| 2.32.6|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
|Java 21|21.0.11|[JDK 21.0.11](https://www.oracle.com/java/technologies/javase/21-0-11-relnotes.html)|
