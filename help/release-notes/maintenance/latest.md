---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 23963 {#23963}

Summarized below are the continuous improvements for maintenance release 23963, which was publicly released on January 8, 2025. The previous maintenance release was release 23482.

The 2026.1.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

>[!NOTE]
>
>Release 23862 has been made private. 

### Enhancements {#enhancements-23963}

* CQ-4361812: Added support for optional param folderPath in rest api. Description: A new translation project is created by the API, and will be placed within the path specified by the optional `folderPath` parameter, otherwise it defaults to the root project path `/content/projects`.
* FORMS-21960: Added support for canvas editing on local for Interactive Communications, similar to forms-spa.
* FORMS-22001: Added guidance to reduce high volume of `/etc.clientlibs/toggles.json` requests in AEM Forms as a Cloud Service.
* FORMS-22496: Expose Raw ResponseBody in Invoke Service.
* FORMS-22495: Add placeholder property in SetProperty rule.
* FORMS-21925: UBS Footnotes Formatting: Display All Footnotes in the Form During Form Load.
* FORMS-20536: Expose an option of complete response in eventPayload in rule editor without mapping.
* SITES-37199: Annotation Feature triggers repository traversal via unvalidated `authorizables.json` call causing Performance Degradation.
* SITES-37118: Commerce Optimizer support in Product Cockpit.
* SITES-38029: Add logs for tracing MSM push on modify events.
* SITES-37050: Support for "force unpublish", allowing to unpublish content fragments that are referenced by other published resources.
* SITES-37142: Added capability to checkin/checkout a content fragment via content fragment PATCH.
* SITES-37613: In the CF API permissions endpoint return checkin  if the user can checkin a content fragment, or checkout  if the user can checkout a content fragment.
* SITES-37835: When attempting to create multiple content fragments with the same title, but no provided name, automatically generate a new name instead of failing due to conflict.
* SITES-36823: Edge Delivery with Universal Editor: Remove the need for reverse mappings for indexes.
* SITES-34751: Edge Delivery with Universal Editor: Fail for non supported file types and paths out of limits when publishing (Early Access).
* SITES-37888: Edge Delivery with Universal Editor: Use Alt suffix as synonym for Text for links.
* SITES-19850: Edge Delivery with Universal Editor: Add support for multiple sheets in spreadsheets.
* SITES-32490: Edge Delivery with Universal Editor: Add support for data-aue-component and user defined data-aue-label to blocks and default content.
* SITES-37794: Edge Delivery with Universal Editor: Simplify page creation wizard.
* SITES-36963: Migrate Audience/Segment Endpoint to Target API v3 for Workspace Support.

### Fixed Issues {#fixed-issues-23963}

* CQ-4361831: Fixed issue causing genai_dropdown_span is not defined.
* CQ-4360895: Fixed Inaccurate translation job status count in project during concurrent updates.
* CQ-4361599: Fixed skipping of Content Fragments from Translation Jobs after 2025.7 upgrade.
* CQ-4360747: Fixed Repeatable Translation Jobs create empty payloads & trigger too often (NullPointerException in ScheduleRepeatTranslationProject).
* CQ-4359994: Fixed destinationLanguage field type inconsistency for single and multi-language project.
* SITES-38153: Fix cf publish reference provider for uuid based references.
* SITES-37594: Performance improvements for model by tags functionality.
* SITES-37337: FragmentCreateProcessor: provide additional error details in logs.
* SITES-33666: Unlocalized 'Cannot print fragment's Json' error message in Content Fragment Editor.
* SITES-33675: Hardcoded 'undefined' string in Content Fragment Editor > Associated Content.
* SITES-30715: Unlocalized 'General' string in Content Fragment Editor.
* SITES-28592: Unlocalized strings in Content Fragment Model editor > 'Model is locked' dialog.
* SITES-977: Strings "Tags" and "collections" are not localized on edit content fragment page.
* SITES-29699: Unlocalized types of allowed assets in Content Fragment Editor.
* SITES-25240: Call to Action fields in the Teaser Modal do not have a visible label.
* SITES-24869: Truncated tooltip in Template Editor > Separator > Policy.
* SITES-19313: Error is unlocalized when drag and drop a component to deleted template in Template Editor.
* SITES-18103: Unlocalized strings in Page editor > Workflow.
* SITES-17501: Unlocalized strings in Template Editor > Component Policy editor.
* SITES-15091: Strings are unlocalized on text component properties of Experience fragment.
* SITES-8113: 'Assets' string isn't localized in 'Select Image' dialog for 'Templates' in Tools menu.
* SITES-37587: Live copy creation still fails in PROD with NPE in RolloutManagerImpl.
* SITES-37335: Live Copy Page Properties showing error in console related to cq tags.
* SITES-36972: "Rollout" Button Missing in Editable Toolbar.
* SITES-36570: Creating Live Copies fails after chunked Create Live Copy toggle is activated.
* SITES-36158: Rollout fails with Job failed due to an exception.
* SITES-35655: New CF Editor shows active inheritance after it was broken.
* SITES-31425: Unlocalized Error message `Error: {} field is required` displayed in Start workflow in sites.
* SITES-19802: Tooltips is unlocalized in Core Components site > Table of contents.
* SITES-36543: Fixed issue that would allow admin to edit checked out content fragments. 
* SITES-36967: Fixed NullPointerExceptions that occur when attempting to generate thumbnail data for broken content fragments.
* SITES-37791: Fixed an issue where calling FindAndReplace for strings containing `$` would fail.
* SITES-37018: Empty Error Popup When Copying Page with Disallowed Template Path.
* SITES-36243: Edge Delivery with Universal Editor: Fix 404s while publishing of `sling:OrderedFolder`.
* SITES-37684: Edge Delivery with Universal Editor: Fix performance degradation in environments with many sites.
* SITES-37840: Edge Delivery with Universal Editor: Fix publishing failures due to outdated access token for Edge Delivery.
* SITES-37933: Edge Delivery with Universal Editor: Fix (un)publishing failures for deleted resources in Launches.
* SITES-37870: Edge Delivery with Universal Editor: Fix broken rendering of custom page metadata with multi-field support enabled.
* SITES-37349: Edge Delivery with Universal Editor: Render multi-fields with single entries as list with a single list item.
* SITES-36148: Edge Delivery with Universal Editor: Fix data-aue-label for composite multi-fields.

### Known Issues {#known-issues-23963}

None.

### Deprecated Features and APIs {#deprecated-23963}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-23963}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 23 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-23963}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.88.0|[Oak 1.88.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.88.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.30.2|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
