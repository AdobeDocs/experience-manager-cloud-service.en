---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release X {#release-X}

Summarized below are the continuous improvements for maintenance release X, which was publicly released on April 3, 2024. The previous maintenance release was release 15575.

2024.3.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-X}

Adaptive Forms Authoring: 

* FORMS-9889: The user can add the POST URL and Cloud configuration while configuring the Submit action for Submit to REST Endpoint.

Adaptive Forms Rule Editor: 

* In the rule editor, users can:

    * FORMS-12160: Validate a field, panel, or form in the `Then` section of the `When` condition.
    * FORMS-12570: Reset a field, panel, or form in the `Then` section of the `When` condition. 
    * FORMS-11541: Use field objects and global objects in the rule editor through the custom functions. 
    * FORMS-11714: Define parameters as optional in the custom function. By default, parameters declared in custom functions are mandatory. 
    * FORMS-11756: Use caching for custom functions to improve the response time when retrieving the custom function list in the rule editor. 
    * FORMS-12053: Add an 'else' statement in the 'When' condition to implement nested conditions. 
    * FORMS-11269: Use modern ES10 JavaScript features such as let and arrow functions in the custom function. 

Accessibility: 

* FORMS-9014: Improvements to Scribble Signature component:
    * On pressing the Tab key cursor moves within the signature dialog box.
    * On signing using a brush or keyboard, pressing the Enter key closes the dialog box.
    * When the user signs and moves out of the scribble signature component after clicking the OK button, the focus remains on the signature control.
    * A cross icon to clear the signature is accessible through the tab key.
    * Clear Signature Confirmation" dialog is accessible through the tab key.
    * The label for the keyboard sign button is updated to aria-label="keyboard sign" or aria-label="sign using the keyboard".
    * Contrast improved for the controls within the scribble signature.
    * The OK/check mark button improved to convey the inactive state.
    * The signature control is enhanced to be inside the `fieldset` element.
    * When a signature is typed, users can listen to the text used to create the signature.




### Fixed Issues {#fixed-issues-X}

Adaptive Forms Authoring:

* FORMS-12411: On Android devices, the `Maximum Number of Characters Validation` option is not working for the Adaptive Form Textbox component. 

* FORMS-13377: When a user tries to add the custom font and run the pipeline to configure it, it fails with the 'ContainersNotReady' error. 

* FORMS-13267: When a user adds an Adaptive Form Dropdown component, the ID for the Dropdown fails to generate.

* FORMS-13544: When a user adds an Adaptive Form Container component with a wizard layout, it does not work properly during form authoring.

* FORMS-13091, FORMS-13414: If user tries to configure a custom domain URL in the Azure Blob storage, it fails.

* FORMS-13595: When a user tries to save the form in a different location, the user is unable to see the "Select Folder" and "Cancel" buttons if the browser resolution is set to 100%. However, the option is visible  when resolution is set to 75%.

* FORMS-10952: When a user adds an Adaptive Form Dropdown component to an Adaptive Form and uses the 'Set Options' property based on various custom rules, the 'Set Options' property functions only for the last rule.

* FORMS-11471: The lazy loading of a fragment fails when the 'emitter.json' call fails due to a network interruption.

* FORMS-11786: When a user switches between months in the calendar widget, the date picker component shows an extra row.

* FORMS-12093, FORMS-12093: When a user ticks the Adaptive Form Checkbox to submit a form, the incorrect value with an extra  `\` is stored in the textbox.

* FORMS-11993: When a user clicks an image using the "Take a photo" in the Attachment component on an iOS device, all images are added to the folder with the same name.

* FORMS-12555: When a user tries to integrate AEM Forms to a mailing platform with an AEM published URL, AEM Forms does not add method=post while rendering the page. This issue occurs even though POST is set in the submit action with the URL. It causes the mailing platform to not recognize this as a form.

* FORMS-12938: The HTML5 forms are not functioning or loading properly in the Microsoft Edge browser with IE compatibility mode.

* FORMS-12032: When a user submits a form, the path for the submit action path is not pointing correctly.

* FORMS-12445: Wrong values are captured in the Form Data Model after the order of the Radio Button options is changed and the form is published.

* FORMS-12947: When a user adds a new language to an existing dictionary, it fails to merge or add.

* FORMS-11363: When a user submits a form via Workspace, a display issue occurs in the tables while it is rendered.


Adaptive Forms Rule Editor:

* FORMS-11756: When a user adds the ES6 JavaScript features such as `let` and `const` in custom functions, the rule editor fails to open. This mainatenance release brings support for ES10.  

Communication APIs:

* FORMS-13164: If the user generates a PDF, unexpected blank lines are added to it after submission.
* FORMS-13789: When user tries to generate multiple PDFs, the Output batch API fails. 
* FORMS-11483: When a user converts PDF to PDF/A-2B or PDF/A-3B, it fails to convert and shows a validation error. 
* FORMS-10501: When a user invokes HSM, the documents are certified but it does not enable LTV. 

Accessibility: 

* FORMS-11546: When a form author uses repeated panels in an Adaptive Form, the ARIA attribute is missing from the HTML tags. 
* FORMS-11826: Due to matching labels Arial&reg; labelledby and Arial&reg; label, the screen readers are not able to distinguish between these two. To resolve the issue – the label "aria-labelledby" is replaced with "aria-describedby" for the form fields. (F).

* FORMS-12626, FORMS-13094: Users are unable to access the toolbar using the keyboard to save or edit content on the form editor page. 

* FORMS-13102: During the form authoring process, the icons available on the Forms and Documents page lack descriptive features for differently abled individuals.


### Known Issues {#known-issues-X}

None.

### Deprecated Features and APIs {#deprecated-X}

JWT.

Have a look at [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) to know what has been deprecated or removed in AEM as a Cloud Service.

### Change Notice {#change-notice-X}

**Actions Required**

#### Set CM Java Version to 11 {#set-java-version-11}

The new version of the aem-sdk-api contains classes compiled with a Java 11 target, which is not compatible with the Cloud Manager Build environment default JDK version 1.8. This update requires that Maven is executed using JDK 11.

Customers are advised to add a `.cloudmanager/java-version` file to the root of their git repo with the contents: `11`. See [Build Environment / Setting the Maven JDK Version](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#alternate-maven-jdk-version).


### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.60-T20240131102219-0cde853|[Oak API 1.60.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.60.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
