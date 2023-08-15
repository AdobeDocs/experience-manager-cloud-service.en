---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 13099 {#release-13099}

Summarized below are the continuous improvements for maintenance release 13099, which was publicly released on Aug 16, 2023. This maintenance release is an update from previous maintenance release 12874.

2023.8.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-13099}

- SITES-13906: GraphQL - Upgrade to graphql-java 20.1.
- SITES-8972: GraphQL - Add option```label``` in JSON for Enumeration data type.
- SITES-9689: GraphQL - Add title and description in JSON for Content Reference data type.
- SITES-13052: Content Fragments - Export Content Fragments to Adobe Target

### Fixed Issues {#fixed-issues-13099}

- SITES-14937: MSM - Inherit Rollout Configs from Parent value get toggled on hitting Save & Close on live copies.
- SITES-14847: Content Fragments - Content Fragment Links are not highlighted.
- SITES-11620: Content Fragments - References path is slightly cut in the UI.
- SITES-14171: GraphQL - Circular references are not broken for cached data in some cases.
- SITES-14577: Experience Fragments - Bulk publish is not working for live copies.
- SITES-14341: Admin UI - Inconsistent behaviour of the 'Properties' button when delete permissions are removed.
- SITES-11000: Admin UI - References: Incoming links missing in some pages.
- SITES-11559: Admin UI - References: Incoming Links shows wrong pages.
- SITES-14337: Admin UI - Opening editor page produces an error in specific cases.
- SITES-13425: ContextHub - Menu Bar does not display when clicking ContextHub button.
- FORMS-9971: When an Adaptive Form is rendered in a different locale, the visibility of components is interpreted and applied inaccurately. 
- FORMS-9888: When an Adaptive Form is set to redirect to an external URL (thank you page) on form submission, it fails to redirect to the external URL. 
- FORMS-9845: After clearing a dropdown using the rule editor, the previously provided values persist, despite the supposed clearance.
- FORMS-9263: When the label of a checkbox contains special characters and a user clicks the checkbox, the respective checkbox is not selected.
- FORMS-9254: As a user scrolls through the text of the Terms & Conditions component, the checkbox within the component is automatically enabled even before the user has scrolled through the entire text.
- FORMS-9045: The script tag does not resolve external fragment references in the base XDP.
- FORMS-9026: When attempting to create an Adaptive Form using a JSON schema that has Enums with empty strings and validates without errors, the process results in a failure. Next, upon refreshing the page, the form fails to load properly, displaying a blank form along with an error in the logs. 
- FORMS-8964: In Android&trade; Chrome/Firefox, text becomes uneditable   in Text Box Component if max character limit is reached. 
- FORMS-8668: Excessive Java&trade; stack dumps in error logs, despite functional form rendering, causing log file bloat. 
- FORMS-8554: Adaptive Forms with lazy loading enabled do not work in preview mode of the author instance. 
- FORMS-8177: When the forms service is active, an exception "com.adobe.aem.formsndocuments.publish.AssetReferenceProvider Failed to retrieve asset dependencies." occurs. The error disappears on disabling the form service. 
- FORMS-3691: Some objects are missing IIFE (Immediately Invoked Function Expression) scoping. The primary purpose of using an IIFE is to create a scope for variables within the function, preventing those variables from polluting the global scope. 


### Known Issues {#known-issues-13099}

- SITES-15359: The variation name pattern fails to correctly match variations that have ```'_'``` in their resource names.

### Embedded Technologies {#embedded-tech-13099}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.52-T20230629133256-25c01b8|[Oak API 1.52.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.52.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.2|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
