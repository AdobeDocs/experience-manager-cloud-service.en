---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 27830 {#release-27830}

Summarized below are the continuous improvements for maintenance release 27830, which was publicly released on August 26, 2026. The previous maintenance release was release 27673.

The 2026.9.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-27830}

* ASSETS-68245: Expose additional Adobe Stock licensing metadata.
* CQ-4361361: Improved Watchdog efficiency by dynamically releasing unused thread resources.
* CQ-4363548: Optimized translation session handling to skip saves when there are no changes.
* FORMS-27178: Font sizes are now rounded to the nearest integer point during PDF generation for more consistent output.
* SITES-43659: Composite Data-Type: Prevent composite fields from being editable in the content-fragment Touch-UI editor.
* SITES-43538: Composite Data-Type: GraphQL support for composite field variations.
* SITES-38060: Content Fragment Model Editor: Show a warning if a model with the same title already exists.
* SITES-38666: New frontend for CIF.
* SITES-49657: Release CIF components 2.18.8.
* SITES-49673: Release Core Components 2.32.6.
* SITES-46868: Content Fragment composite data types now support tag-based dynamic model referencing, matching Content Fragment Reference behavior.
* SITES-47277: Edge Delivery with Universal Editor: add Edge Delivery roles based permissions to preview/publish (early access).
* SITES-42708: Edge Delivery with Universal Editor: respect configured limits and features of Edge Delivery for asset validation.
* SITES-46007: Edge Delivery with Universal Editor: add support for custom names for the Columns block.
* SITES-47291: Edge Delivery with Universal Editor: add primary-language-url for localized urls (w/ sling:alias).
* SITES-47399: Edge Delivery with Universal Editor: add support for authorable login page paths for gated content.

### Fixed Issues {#fixed-issues-27830}

* CQ-4363926: Fixes unnecessary TAGMETADATA object addition when unmodified content is added during translation project creation, potentially causing translation job failures.
* CQ-4363431: Fixed creation of empty-translation jobs during Scheduled Repeat Translation considering  jcr:language property.
* FORMS-25184: In the Data Sources panel, the binding-indicator dots were missing for Core Components-based Adaptive Forms.
* FORMS-26236: The `fd-service` user was missing `jcr:versionManagement` permissions on `/conf`.
* FORMS-26250: Switching fields in the Rule Editor while rules were still loading applied or saved the wrong field's rules, due to a race condition.
* FORMS-26476: The Content Tree did not load in the Adaptive Forms editor.
* FORMS-26500: Uploading multiple files with the same name to a foundation Adaptive Forms file-attachment field saved only one binary on the server.
* FORMS-26627: Concurrent read and update calls in the Rule Editor could overlap and corrupt rule state; a blocking loader now prevents this.
* FORMS-26633: A Forms script misidentified non-Forms dialogs, which broke any component that has an "Advanced" tab.
* FORMS-26813: The File Attachment component ignored the custom "unsupported file type" message (`acceptMessage`).
* FORMS-26824: In the Rule Editor, dragging a form object across an existing target cleared that target and reverted it to "Drop here."
* FORMS-26864: Forms Manager did not download or publish fragments that were bound to variables.
* FORMS-26878: On French Adaptive Forms, the Date Picker validation message was not localized and appeared in English.
* FORMS-26910: Objects went missing after syncing when a template was used as a reference.
* FORMS-26974: The Dropdown component's PDF preview showed the default value instead of the bound value when both were set.
* FORMS-26986: Fragments present in an Interactive Communications (IC) Document disappeared when the document was synced with its template.
* FORMS-27224: In Interactive Communications (IC), pagination and binding properties overridden in an IC Document were not preserved after a template sync.
* FORMS-27506: When a template was used as a reference, legacy document-author overrides were dropped during the template sync.
* SITES-47827: Content Fragment Touch-UI Editor: Saving a Content Fragment in the CF Editor Posts Empty Tag Field When No Tag Is Selected.
* SITES-46019: GraphQL: GraphQL support for `GenericContentRef` in content reference fields.
* SITES-45383: Content Fragment Model Editor : fix localization bugs
* SITES-37328: Content Fragment Model Console : `StringIndexOutOfBoundsException` when a folder below /conf endsWith "settings" in ModelConsole.
* SITES-48264: GraphQL: Fix some corner cases in the schema cache.
* SITES-47330: Rich Text Field in Page Properties Not Editable.
* SITES-46681: Breakpoints Now Mandatory in Responsive Grid Cause Authoring Regression & Large-Scale Content Remediation.
* SITES-46532: Special characters not displayed in RTE.
* SITES-46191: `crop#launchwithratio` fails in inline (non-fullscreen) image editor: screen flickers, no crop box.
* SITES-45771: Inline-Editing (mode=hybrid) does not load / apply custom Crop-Ratios & fails outside Fullscreen.
* SITES-44958: Experience Fragment variation switch while component dialog is open blocks further editing.
* SITES-43186: Unlocalized 'to exit text editor press Esc key' tooltip in Page Editor > Text component configure.
* SITES-42987: [LOC] ENU format used in calendar under 'Skyline' > 'Commerce'.
* SITES-48426: Performance improvements in Sites Console.
* SITES-30879: Unlocalized strings in Sites > Page Editor > Search component.
* SITES-48305: Launch promotion with Live Sync still duplicates nested components when using Promote modified pages.
* SITES-44270: Live-Copy Content Fragments revert to “Draft” instead of “Modified” after rollout.
* SITES-43194: MSM Live Copy Page Properties – `cq:tags` collapse into single tag & data loss on save.
* SITES-48136: Fixed an issue in the Universal Editor where moving a referenced Content Fragment could replace an entire rich-text field with a link.
* SITES-48494: Removed the minimum-length constraint on Content Fragment model metadata.
* SITES-47737: Fixed Preview publication incorrectly republishing up-to-date references (Experience Fragments and pages), which could cause workflow failures.
* SITES-49073: Fixed the Adobe Target IMS configuration dropdown appearing empty in Classic UI, which blocked Experience Fragment export.
* SITES-42708: Edge Delivery with Universal Editor: fix false-negatives publishing validation errors when images are already published.
* SITES-48879: Edge Delivery with Universal Editor: fix publishing validation errors when json-ld is authored as richtext.
* SITES-49193: Edge Delivery with Universal Editor: fix authoring of authenticated sites when using file-based path mapping.
* SITES-49345: Edge Delivery with Universal Editor: fix reference rewriting in metadata when arbitrary keywords resolve to a resource.

### Known Issues {#known-issues-27830}

None.

### Deprecated Features and APIs {#deprecated-27830}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-27830}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 13 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-27830}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.4.0 | [Oak 2.4.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.4.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.67 | [Apache Httpd 2.4.67](https://apache.googlesource.com/httpd/+/refs/tags/2.4.67/CHANGES)|
|Dispatcher|2.0.274||
|AEM Core Components| 2.32.6|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
|Java 21|21.0.11|[JDK 21.0.11](https://www.oracle.com/java/technologies/javase/21-0-11-relnotes.html)|
