---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

>[!NOTE]
>
> Releases 20936 and 20783 have been made private.

## Release 20626 {#20626}

Summarized below are the continuous improvements for maintenance release 20626, which was publicly released on April 29, 2025. The previous maintenance release was release 20476.

The 2025.5.0 feature activation provides the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-20626}

* ASSETS-46413, ASSETS-46580: Added a new review status “Preview”.
* ASSETS-49542: Expansion of supported languages for video and audio transcribe and translate.
* ASSETS-48264: Expansion of PNG quality support for renditions.

### Fixed Issues {#fixed-issues-20626}

* ASSETS-50387: Correct Content Fragment default thumbnail for use in GenStudio.
* ASSETS-49006: Display video properties when the user does not have write permissions.
* ASSETS-46757, ASSETS-46997: Improve Accessibility in the smart crop editor.
* ASSETS-48018: Improve asset reference tracking in the Assets Publish Report.
* ASSETS-35846: Improve consistency of access between author and delivery tier.
* ASSETS-48171: Improve consistency of Dynamic Media Templating with Canvas.
* ASSETS-49813: Improve Expiration Notification.
* ASSETS-47768, ASSETS-49825, ASSETS-49008, ASSETS-48287: Improve management and visibility into bulk operations.
* ASSETS-50003, ASSETS-50004: Improve naming and control over the renditions included in an asset download.
* ASSETS-47939: Improve organization of responses for Content Hub.
* ASSETS-46738: Improve performance for very large collections.
* ASSETS-50121: Improve reliability of asset published events.
* ASSETS-48490: Improve resiliency of automated processing during image ingestion.
* ASSETS-28106, ASSETS-49404: Improve robustness of full text searching.
* ASSETS-50006, ASSETS-50423: Improve search and traversal performance within a large folder.
* ASSETS-46021: Improve video display for Safari and mobile browsers.
* ASSETS-49002: Improve handling of editing Dynamic Media Templates.
* ASSETS-48376: Miscellaneous improvements in Content Hub UI.
* ASSETS-48504, ASSETS-49378: Miscellaneous improvements to UI behavior.
* ASSETS-49540: Move Asset Relations OpenAPI out of experimental phase.
* ASSETS-40284: Update documentation around Adobe Stock integration.
* ASSETS-49739: Work to integrate Figma from Asset Selector. 

#### AEM Guides {#guides}

* GUIDES-21734: New IDs fail to generate for elements when such elements are added via snippets or created via templates, even when the auto generate ID option is enabled in XMLEditorConfig.
* GUIDES-25969: If the `scope=external` attribute is missing from external links in a DITA topic, HTML5 publishing fails without indicating the files where this attribute is missing in the error logs, especially when the microservice is enabled.
* GUIDES-27288: Unable to pass the metadata properties to map landing pages generated using new AEM Sites publishing.

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Known Issues {#known-issues-20626}

None.

### Deprecated Features and APIs {#deprecated-20626}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-20626}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 11 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-20626}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.78.0|[Oak API 1.78.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.78.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.26-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.29.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
