---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 12441 {#release-12441}
 
Summarized below are the continuous improvements for maintenance release 12441, which was publicly released on June 27, 2023. This maintenance release is an update from previous maintenance release 12255.

2023.7.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-12441}

- SITES-8769: Improve StyleImpl calls in ResponsiveGrid
- FORMS-5054: Added support for all the [statues](https://opensource.adobe.com/acrobat-sign/acrobat_sign_events/webhookeventsagreements.html) supported by Adobe Sign. 

### Fixed Issues {#fixed-issues-12441}

- Various accessibility-related updates
- SITES-12688: Page Editor: Logical operator OR not properly working in Asset Finder search
- SITES-4951: Page Editor: Tag-search in Page editor does not find sub-tags
- SITES-12465: Experience Fragments: Arrow keys not working in Experience fragment component dialog
- SITES-12893: Experience Fragments: Apply circular reference validation for Experience Fragments
- SITES-12715: Experience Fragments: Cloud service configs applied to Experience fragments folder do not persist
- SITES-13097: Experience Fragments: Not able to add experience fragments to a translation project
- SITES-13165: GraphQL: Restore default behavior for filtering of null values
- SITES-12577: Link Checker: Transformer not rewriting links intermittently 
- SITES-13559: MSM: 'Is not modifiable' exception thrown when rolling out component
- SITES-11757: MSM: Inherit rollout configuration from Parent does not get reverted back for child pages
- SITES-14073: Sites Admin: CSV Report fails with 500 when selecting no property to export
- FORMS-7648: Unable to validate maximum number of digits in a  Numeric Box component. The validation script is not working.
- FORMS-8177: When the Forms service is active, the `com.adobe.aem.formsndocuments.publish.AssetReferenceProvider Failed to retrieve asset dependencies` error encounters. 
- FORMS-8300: When a user attempts to delegate a task after opening it, the delegate response reloads the task, instead of opening user's AEM Inbox UI.
- FORMS-8500: On Microsoft&reg; Edge browser with the IE Mode option enabled, HTML5 Forms fails to open.
- FORMS-8541: On rendering an Adaptive Forms, a Null Pointer Exception occurs. 
- FORMS-8964: When a form is opened on an Android&trade; Device on Google Chrome or Mozilla Firefox, the text entered in the Text Box Component cannot be removed.
- FORMS-9026: When a user creates an Adaptive Form based on a complex and valid JSON schema, drags related JSON schema fields to Adaptive Forms Editor to create Adaptive Forms fields, and refreshes the Adaptive Forms Editor window, all the fields are deleted and Adaptive Forms editor appears blank. 
- FORMS-9263: When a checkbox option's display text contains special character, users are unable to select such check boxes. 
- FORMS-8668: While rendering a PDF Preview of a form, some non-required Java&trade; stack dumps appears in the error logs. However, there are no issues in rendering the form. 
- FORMS-8116: When rules are applied to the Adaptive Forms Container component, the applied rules are not saved. 
- FORMS-7906: When an Adaptive Form is added to an AEM Sites Container component, the rule editor fails to open.  
- FORMS-8846: The Bind reference property does not work for the Adaptive Forms attachments component.
- FORMS-9072: When you search a Scheme while creating a form fragment, the search result does not return any schema for selection. 
- FORMS: Fixed multiple accessibility-related bugs to improve accessibility of AEM Forms features.

### Known Issues {#known-issues-12441}

None.

### Embedded Technologies {#embedded-tech-12441}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.50-T20230405052634-f9df4aa|[Oak API 1.50.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.50.0/index.html)| 
|AEM SLING API |Version 2.27.0 |[Apache Sling API 2.27.0 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
