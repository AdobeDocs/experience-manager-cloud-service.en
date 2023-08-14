---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release X {#release-X}
 
Summarized below are the continuous improvements for maintenance release X, which was publicly released on August 2, 2023. This maintenance release is an update from previous maintenance release 12790.

2023.8.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-X}

None.

### Fixed Issues {#fixed-issues-X}

* When an Adaptive Form is rendered in a different locale, the visibility of components is interpreted and applied inaccurately. (FORMS-9971)
* When an Adaptive Form is set to redirect to an external URL (thank you page) on form submission, it fails to redirect to the external URL. (FORMS-9888)
* After clearing a dropdown using the rule editor, the previously provided values persist, despite the supposed clearance. (FORMS-9845)
* When the label of a checkbox contains special characters and a user clicks the checkbox, it does not result in the respective checkbox being selected. (FORMS-9263)
* As a user scrolls through the text of the Terms & Conditions component, the checkbox within the component is automatically enabled even before the user has scrolled through the entire text. (FORMS-9254)
* The script tag does not resolve external fragment references in the base XDP. (FORMS-9045)
* When attempting to create an Adaptive Form using a JSON schema that has Enums with empty strings and validates without errors, the process results in a failure. Subsequently, upon refreshing the page, the form fails to load properly, displaying a blank form along with an error in the logs. (FORMS-9026)
* In Android Chrome/Firefox, text becomes uneditable   in Text Box Component if max character limit is reached. (FORMS-8964)
* Excessive Java stack dumps in error logs, despite functional form rendering, causing log file bloat. (FORMS-8668)
* Adaptive Forms with lazy loading enabled do not work in preview mode of the author instance. (FORMS-8554)
* When the forms service is active, an exception "com.adobe.aem.formsndocuments.publish.AssetReferenceProvider Failed to retrieve asset dependencies." occurs. The error disappears on disabling the form service. (FORMS-8177)
* Some objects are missing IIFE (Immediately Invoked Function Expression) scoping. The primary purposes of using an IIFE is to create a new scope for variables within the function, preventing those variables from polluting the global scope. (FORMS-3691)


### Known Issues {#known-issues-X}

None.

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.52-T20230629133256-25c01b8|[Oak API 1.52.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.52.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
