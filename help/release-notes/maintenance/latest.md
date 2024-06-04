---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 16544 {#release-16544}

Summarized below are the continuous improvements for maintenance release 16544, which was publicly released on June 4, 2024. The previous maintenance release was release 16461.

2024.6.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-16544}

* DXML-17171: The copy and paste operation of topics exceeding 15KB fails with an unexpected error. 
* DXML-17088: The functionality to change the document state from the **File Properties** panel isn’t working correctly and changes to the *Draft* state. 
* DXML-16931: Linked images from the topics fail to appear in the baseline after version creation. 
* DXML-16896: Reusable content panels don’t list elements when the **User preferences** are set to view files by **Filename**. 
* GRANITE-41133: Support Jakarta Servlet API 5 and OSGi Servlet Whiteboard API.
* GRANITE-51355: Deprecate org.slf4j.event.
* GRANITE-51565: AEM loses local group relationship with external group when local group is published from AEM.
* GRANITE-51707: Set the cookie saml_request_path during http redirect for authentication.
* GRANITE-52010: Update Jackrabbit version to 2.20.16.
* GRANITE-52057: Update Filevault to 3.7.3-T20240514105118-694f6aea fixing JCRVLT-745.
* SKYOPS-35998: Update 'Sling RepoInit' dependencies :  Repoinit Parser 1.9.0, Repoinit JCR 1.1.46.

#### Experience Manager Guides 

* **Publish a topic or its elements to an Experience Fragment**
  Now, Experience Manager Guides allow you to publish a topic or its elements to an Experience Fragment. An Experience Fragment is a modular content unit that integrates both content and layout.  Experience Fragments are instrumental and can help you create consistent and engaging experiences. 
* **Ability to pass the topic asset metadata to Native PDF output**
  You can add the topic asset metadata while generating the Native PDF output. This feature helps you add specific metadata for different topics, like the topic title and author, to the topic page headers and footers. 

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap).

### Fixed Issues {#fixed-issues-16544}

* GRANITE-51375: idp-sync throws NPE if no intermediate path is specified.

#### Experience Manager Guides 

* DXML-17171: The copy and paste operation of topics exceeding 15KB fails with an unexpected error. 
* DXML-17088: The functionality to change the document state from the **File Properties** panel isn’t working correctly and changes to the *Draft* state. 
* DXML-16931: Linked images from the topics fail to appear in the baseline after version creation. 
* DXML-16896: Reusable content panels don’t list elements when the **User preferences** are set to view files by **Filename**. 

### Known Issues {#known-issues-16544}

None.

### Deprecated Features and APIs {#deprecated-16544}

To know what is deprecated or removed in AEM as a Cloud Service, see [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md).

### Embedded Technologies {#embedded-tech-16544}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.64.0|[Oak API 1.64.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.64.0/index.html)| 
|AEM SLING API | 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.22-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.25.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
