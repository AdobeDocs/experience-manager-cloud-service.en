---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 20133 {#20133}

Summarized below are the continuous improvements for maintenance release 20133, which was publicly released on April 1, 2025. The previous maintenance release was release 19823.

The 2025.4.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-20133}

* FORMS-19068: Added support for AEP Connector submit actions in Forms Manager APIs to enhance form data integration capabilities.
* FORMS-18513: Implemented data tree transformation support in AEP Connector to enhance wizard functionality and data handling capabilities.
* FORMS-18432: Implemented form-specific (regex-based) client-side prefill configuration to enable selective prefill functionality without OSGI-level changes.
* FORMS-17551: Added Document of Record (DoR) support for SharePoint list integrations.

### Fixed Issues {#fixed-issues-20133}

* FORMS-19028: Client-side prefill functionality breaks form event handling, preventing Value commit and DOMContentLoaded events from triggering properly on form load.
* FORMS-18360: Enhanced SharePoint list scope management for teams sites in Forms Document Management to improve data organization and access control.
* FORMS-18325: Added Adobe Experience Platform (AEP) Cloud configuration to enhance form data integration and processing capabilities.
* FORMS-18213: Implemented functionality to hide/exclude disabled fields from Document of Record (DoR) to improve document clarity and user experience.
* FORMS-18189: Modified custom function handling to prevent error logging for empty client libraries and improve error display in UI.
* FORMS-18426: SharePoint list lookup functionality fails when list names contain special characters (For example, '-'), affecting form integration with SharePoint lists.
* FORMS-18375: Foundation Components based forms incorrectly select recaptcha configurations from `conf/global` folder when no specific configuration container is selected.
* FORMS-18304: PDF/A-1b documents passing validation in Acrobat and LiveCycle ES4 are incorrectly flagged as non-compliant in AEM 6.5 Forms due to device-dependent color errors.
* FORMS-18271: Forms Theme Editor displays unlocalized error messages, affecting user experience in form configuration and theme customization.
* FORMS-18068: Bold text rendering issues in Document of Record (DoR) for radio button and checkbox groups using rich text fields.
* FORMS-7016: Keyboard focus order in Form Editor does not follow logical navigation.
* FORMS-6950: Added required ARIA roles and attributes to file system navigator treeview components to improve screen reader accessibility and comply with WCAG 4.1.2 Name, Role, Value (Level A) standard.

### Known Issues {#known-issues-20133}

None.

### Deprecated Features and APIs {#deprecated-20133}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-20133}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 34 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-20133}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.76.0|[Oak API 1.76.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.76.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.26-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.28.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
