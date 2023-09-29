---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 13665 {#release-13665}

Summarized below are the continuous improvements for maintenance release 13665, which was publicly released on September 27th, 2023. This maintenance release replaces release 13420.

2023.10.0 Feature Activation provides the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-13665}

* Various improvements in the Content Fragment APIs.
* ASSETS-26713: Assets Dashboard: New Experience UI Dashboard now reachable from Touch UI.
* SITES-11206: Content Fragments: Search API for Content Fragments.
* SITES-11262: Content Fragments: Button to switch to the new Content Fragment Editor.
* SITES-15447: Core Components: Release of version 2.23.4.
* FORMS-9624: Introduced CAPTCHA component for Adaptive Forms based on Core Components. 
* FORMS-9913: Enhanced the visual editor's invoke service by adding the capability to validate fields and display appropriate error and success messages.
* FORMS-10106: Enhanced GeneratePDFOutput API to return the number of pages contained within the generated document.
* FORMS-2494: Added support for Form Fragments for Adaptive Forms based on Core Components. 
* FORMS-9807: Added support to allow navigating to a page URL that is returned as a result of a successful submission through the Adaptive Form rule editor. 
* FORMS-10571: Added the ability to set a thank you page redirect URL based on response of a service used in a custom submit action for Adaptive Forms based on Core Components. 

### Fixed Issues {#fixed-issues-13665}

* Various translation-related updates.
* CQ-4354428: Workflows: Unable to complete a task in Inbox.
* SITES-9733: Content Fragments: Asset References in content fragment reference panel shows 0(zero) references.
* SITES-14561: Content Fragments: Fixed and improved HTML to Markup conversion.
* SITES-14882: Content Fragments: Once we edit Content Fragment and close the tab without clicking on save or close button, the values are getting stored.
* SITES-15167: Content Fragments: Patching a variation with an invalid payload does not return 400 but 500.
* SITES-15514: Content Fragments: Malformed Markdown output for table inside RTE.
* SITES-15661: Content Fragments: Do not use unique constraint and reorder items in references fields in Fragments API.
* SITES-15730: Screens: Screens Channel Preview functionality not working on Dashboard.
* SITES-15995: Content Fragments: Mime types of both model and fragment long text fields are hardcoded.
* SITES-16074: Content Fragments: Tag fields which are not String[] cannot be retrieved from JCR.
* SITES-16084: Content Fragments: CFHomeCardModelImpl is missing target navigator.
* SITES-14773: Experience Fragments: Link Reference does not get updated inside experience fragment.
* SITES-14899: Experience Fragments: Multiple offers created for XF variations in Target.
* SITES-8590: GraphQL: Encoding issues with variables in persisted queries.
* SITES-9224: GraphQL: "Writer has already been closed" exception in GraphQLServlet.
* SITES-14800: GraphQL: Exception in persisted GraphQL queries with variables.
* SITES-15586: GraphQL: Issue with persisted queries filtering with null values.
* SITES-15622: GraphQL: Issue with persisted queries with numbers & bool parameters.
* SITES-15654: GraphQL: Issue with unions & properties with same name.
* SITES-15267: Launches: Promotion does not pick up launch pages modified before time of modifying the launch configuration.
* SITES-15406: Launches: Unable to add a Launch Page.
* SITES-15427: Launches: Inconsistent behavior of "Promote current page and sub pages" scope.
* SITES-15429: Launches: Authoring pages deleted while promoting launches.
* SITES-15462: Launches: Auto promotion process publishes pages out of promotion scope.
* SITES-15815: Launches: Deleted Page from Launch causes Launch to not Promote Successfully.
* SITES-15223: Page Editor: Not able to resize components whin in tablet size emulator.
* SITES-15463: Page Templates: Templates cannot be published.
* FORMS-10700: When utilizing the date picker component within an Adaptive Form built on Core Components:
    * When the user submits the form without providing any input for date component, an error is logged.
    * On using localized versions of the date picker, some months operate seamlessly, selecting certain others leads to a component malfunction.
* FORMS-9598: The AEM Forms embed component is not working.
* FORMS-9579: You cannot pass a Boolean value to a function while using the Rules Editor.
* FORMS-9916: Marking the field as invalid causes a change event to be triggered again on the same field. This unexpected event triggers the rule once more, creating a loop that keeps repeating until it reaches a maximum limit of 10 repetitions.
* FORMS-10243: The Set Focus option is not working properly for Adaptive Forms based on Core Components. Specifically, when a radio button is clicked, and the "set focus" rule is enabled for a text box object, it fails to set the focus as intended, despite other rules functioning correctly.
* FORMS-10416: For a Headless Adaptive Form, when the ":type" property is included, the multiline-input component appears as a regular single line text-input component.
* FORMS-10015: For an Adaptive Form based on Core Components, in the rule editor, when we choose the Form object, it passes the entire field instance object to the custom function instead of just the field's value.
* FORMS-9890: Users in the cloud administrators group, without forms-user access, can create data sources, forms, and Form Data Model. However, they cannot view available services in the system when using 'Invoke service' in the rule editor.
* FORMS-9075: On submitting an Adaptive Form, the screen readers do not announce all the Error Messages for the mandatory fields.
* FORMS-9014: The following accessibility issues were fixed:
    * When opening the scribble signature box, the cursor skips to the next component, not within the box itself. This behavior has been confirmed as an issue by the Accessibility Team.
    * After signing, pressing Enter doesn't close the dialog; users must explicitly click the OK button. 
    * Post-signing, the tab order resets to the top, rather than staying at the signature component or moving to the next.
    * The option to clear the signature, represented by a cross icon, isn't part of the tab order and only appears on hover. 
    * The "clear signature confirmation" dialog can not be accessed via keyboard.
    * The label for the keyboard sign button should be corrected for clarity.
    * Controls within the scribble signature lack the recommended contrast ratio.
    * The inactive state of the OK/check mark button should include the "aria-disabled" attribute.
    * The screen reader doesn't convey the text used to create the typed signature, making it inaccessible to visually impaired users.
* FORMS-9214: For Adaptive Forms based on Core Components, the Custom Function is not invoked unless it is used to modify another field, such as setting the value of a different field.
* For Document Generation APIs, the "/content" path shows inconsistency in its usage across template path, content root, and data. It functions correctly in some cases but not uniformly.
* FORMS-10718: Added support for the GuideBridge's resolveNode API for Adaptive Forms based on Core Components. 
* FORMS-9998: In Adaptive Forms based on Core Components, the "Is Empty" and "Is Not Empty" functions do not function as expected when validating text input via the Rule Editor.
* FORMS-10236: The File Attachment Component does not function correctly for Adaptive Forms based on Core Components. While using the attachment component, file previews work initially, but if you attach additional files of similar or different types or formats, the preview malfunctions.
* FORMS-10470: In checkbox component, when the default value as unchecked ('off') and datatype is String, the submit button does not work. 
* FORMS-10534: In Adaptive Forms based on Core Components, the Boolean operand option appears on the left side, indicating that it is selectable. However, when a user attempts to select it, an error highlight or some form of error indication occurs, suggesting that the selection is not functioning as expected. 
* FORMS-10248: In Adaptive Forms based on Core Components, setting the value of a Radio button or Checkbox when the data value type is Boolean is not working as expected.
* FORMS-8114: The date picker and pattern not being read correctly by the NVDA screen reader. Specifically, when using the NVDA screen reader, the date picker without a pattern is read correctly. However, when a pattern is applied to the date picker, it is read as a table instead of being interpreted correctly.

### Known Issues {#known-issues-13665}

None.

### Embedded Technologies {#embedded-tech-13665}

|Technology|Version|Link|
|---|---|---|
|AEM Oak |1.54-T20230817132355-3800a65|[Oak API 1.54.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.54.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
