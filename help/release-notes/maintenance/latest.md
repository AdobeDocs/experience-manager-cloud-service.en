---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 26773 {#release-26773}

Summarized below are the continuous improvements for maintenance release 26773, which was publicly released on June 17, 2026. The previous maintenance release was release 26353.

The 2026.6.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

>[!NOTE]
>
>Release 26635 has been made private. 

### Enhancements {#enhancements-26773}

* GRANITE-67251: Introduced `cqSiteSearch`, a new out-of-the-box index defined over the `cq:Searchable` mixin type. This allows fine-grained control over what content goes into the site index and provides full-fledged site search for AEM websites, including semantic search.
* GRANITE-68099: Updated the embedded Apache Jackrabbit Oak to the latest public release (2.2.0).
* SKYOPS-135241: Introduce aem prefix for immutable farm filters to avoid naming conflicts with customer-defined configurations.

### Fixed Issues {#fixed-issues-26773}

None.

#### AEM Guides {#guides-26773}

* GUIDES-46275: Image dimensions specified with units such as `mm` are not rendered correctly, causing images to be displayed at their original size instead of the specified dimensions.
* GUIDES-45800: Copying and pasting `<keywords>` inside `<topicmeta>` within a `<keydef>` or `<topicref>` results in the keywords being inserted inside unwanted foreign tags.
* GUIDES-45409: When a map contains an external `topicref` pointing to a non-DITA resource (such as `.html`), its preview is not displayed in the Assets UI.
* GUIDES-45254: When working with `.plt` and `.css` files in PDF templates, the **Generate IDs** option is available in the right-click context menu despite not being applicable to these file types.
* GUIDES-45508: Applying a baseline to a map with many assets delays loading of the translation report for the selected language, sometimes leading to request timeout before the report renders.
* GUIDES-45511: The tooltip for the **Version History** icon is missing in the left panel of the Review UI adjacent to the topic name.
* GUIDES-44942: When adding questions to a quiz using the Insert from question bank option, short answer questions are not listed despite having a valid Question ID.

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Known Issues {#known-issues-26773}

None.

### Deprecated Features and APIs {#deprecated-26773}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-26773}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 10 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-26773}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.2.0 | [Oak 2.2.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.2.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.67 | [Apache Httpd 2.4.67](https://apache.googlesource.com/httpd/+/refs/tags/2.4.67/CHANGES)|
|Dispatcher|2.0.274||
|AEM Core Components| 2.31.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
|Java 21|21.0.11|[JDK 21.0.11](https://www.oracle.com/java/technologies/javase/21-0-11-relnotes.html)|
