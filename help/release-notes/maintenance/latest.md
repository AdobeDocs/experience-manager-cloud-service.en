---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 21772 {#21772}

Summarized below are the continuous improvements for maintenance release 21772, which was publicly released on August 6, 2025. The previous maintenance release was release 21706.

The 2025.8.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### New Features  {#new-features-21772}

* SITES-30049: Added new endpoint for retrieving the language copies of a Content Fragment by its UUID.

### Enhancements {#enhancements-21772}

* CQ-4358722 : Resolved localization issues caused by differing locale codes between Java 11 and Java 17.
* FORMS-19624: Enabled Interactive Communications (IC). It empowers organizations to deliver personalized, on-demand communications—such as statements, invoices, and correspondence—by combining structured templates with dynamic data. With features like web-based template design, reusable content fragments, rule-driven variations, and seamless data integration, IC enables consistent and scalable customer communications across channels.
* FORMS-19587, FORMS-17107, FORMS-19591, FORMS-19582, FORMS-20129, FORMS-20002, FORMS-19593,FORMS-20655, FORMS-19583, FORMS-18024, FORMS-19581: The following enhancements have been made to the Adaptive Forms Rule Editor:
    * The `validate` method in the function list can now validate panels, fields, and forms.
    * Improved client-side custom function parsing to support ES10+ features and static imports.
    * Added an out-of-the-box (OOTB) "Download Document of Record (DoR)" button in the rule editor.
    * Added support for dynamic variables within rules.
    * Enabled creation of rules based on custom events.
    * Rules for repeatable panels now execute in the correct context, rather than only on the last panel instance.
    * Rules can now be triggered based on query parameters, UTM parameters, and browser parameters.
    * Added support for form-specific custom function scripts in EDS (Experience Data Store).
    * Added support for using `EVENT_PAYLOAD` in the "Navigate To" action within the success handler of the rule editor.
    * Supported function calls within input parameters in rule editor and ensured rules are not saved if any required parameters are missing from the function call.
    * Highlighted broken rules in the rule editor UI.
* FORMS-18450: reCAPTCHA V2 (including invisible reCAPTCHA) is now easier to set up and use in Adaptive Forms. The configuration is now managed in one place, making it simpler for you to enable spam protection in your forms.
* FORMS-18385: Added support for AFP generation from XDP and data in AEM Forms through the Output service.
* FORMS-17789: Added an out-of-the-box button in the rule editor to download Document of Record (DoR).
* FORMS-20313, FORMS-2896: Added support for the `dorExclude` property to disable specific features in core component-based forms.
* FORMS-20262: Handled invalid file attachments (0 byte) on the client-side.
* FORMS-18347: Improved Adaptive Forms editor logging for missing form container proxy components.
* FORMS-16205: Excluded disabled components from Document of Record (DoR) in core component-based forms.
* FORMS-10836: Changed orientation of master page properties in Document of Record (DoR) for Right to Left languages.
* SITES-33025: Open new CF Editor via ID instead of path.
* SITES-32741: Trigger update of contenf-fragment page references asynchronously.
* SITES-32087: GraphQL: Add support for `_ignoreCase` on StringArray.
* SITES-12211: Improved Performance in template editor
* SITES-32861: Performance improvement for live copy creation through chunked processing.
* SITES-21383: Performance optimization for Content Fragment launch deletion operations.
* SITES-31165: Performance enhancement by splitting rollout operations into manageable chunks.
* SITES-21353: Query performance improvement for Content Fragment launches using database indexing.
* SITES-30495: Enhancement to support UUID-based fragment references in Content Fragment launches.
* SITES-32151: API enhancement exposing container property functionality.
* SITES-26849: Adjust back-references when a Content Fragment Variation si moved or deleted.
* SITES-31846: Add option to copy/paste root fragment and references in the same folder for copy tree operation.
* SITES-30241: Adjust References located inside a long text field when moving, renaming or deleting a fragment.
* SITES-32684: Enhance mechanism for syncing tab changes in UI schema.
* SITES-33308: Add retry mechanism for syncing changes to the UI Schema when editing models.
* SITES-32247: Missing Dialog Personalization & UI Misalignment in the "Text and Personalization" Component.
* SITES-32261: Experience Fragment i18n Not Applied to Field.
* SITES-32666: Template Predicate contains `\n` causing HTML lookup to fail.
* SITES-32674: Featured Image Field Image Picker not working for Page Creation Wizard Despite `cq:showOnCreate`.
* SITES-32014: Edge Delivery with Universal Editor: Add automatic configuration of CORS policies for localhost, aem.page and aem.live
* SITES-26532: Edge Delivery with Universal Editor: Add Support for localized URLs (early access).
* SITES-30887: Add Contet Fragment uuids stored in workflow metadata.

### Fixed Issues {#fixed-issues-21772}

* CQ-4360190: Fixed `UnsupportedOperationException` occurring when attempting to use add on a keySet that does not support the operation.
* CQ-4360421:  Addressed an issue with Microsoft Translator subscription key encryption to improve security and compatibility.
* FORMS-20980: Fixed keyboard accessibility issues on Date Picker with custom display format in Adaptive Forms.
* FORMS-20498: Added a check for null pointer exceptions in OdataResponse to prevent runtime errors.
* FORMS-20947: Addressed multiple accessibility issues, including screen-reader violations and text truncation/overlap problems.
* FORMS-21030, FORMS-20630: Resolved issues with dropdown fields configured for multiple selections in adaptive forms. The generated PDF now correctly includes all selected values.
* FORMS-19579: Fixed the issue where the Invoke service rule did not auto-correct on re-save.
* FORMS-20734: Corrected the duplication of signature fields in PDF documents generated by the Output service for XFAF based input PDF templates.
* FORMS-20934: Fixed the Autofill Attribute dropdown in AEM Forms authoring UI to remove duplicate entries and include all standard HTML autocomplete tokens.
* FORMS-20700: Resolved the flickering of dropdown help-text on initial load in AEM Forms.
* FORMS-20307: Fixed the issue where forms embedded on a site page were not getting translated with 4-character locales.
* FORMS-20493: Addressed the issue where forms automatically refreshed when data was fetched, causing user inconvenience.
* FORMS-18455: Enhanced the Adaptive Forms Editor for Core Components to show dots for used data objects in the data source tree.
* FORMS-19373: Prevented replication errors for publish environments that do not have any replication agents configured.
* FORMS-20042: Fixed the broken properties view caused by the Apache Sling GET Servlet Configuration with HTML config enabled.
* FORMS-20036, FORMS-19978: Addressed PDF/A-1b compliance and validation issues.
* FORMS-19166: Moved pagedatasource.jsp to servlet to improve error stack trace clarity and added more guardrails and logging.
* FORMS-16466: Fixed issues with repeatable panels not populating correctly in AEM Forms.
* FORMS-19629: Addressed issues with customer JSON schema parsing providing invalid results.
* LC-3923083: Resolved "path object not tagged" error for bordered items in XDP templates.
* SITES-33177: Edge Delivery with Universal Editor: fix broken section styles when stored as comma separated strings.
* SITES-33262: Edge Delivery with Universal Editor: fix blocks with no name property break page rendering and publishing.
* SITES-33309: Edge Delivery with Universal Editor: fix `IllegalArgumentException` when writing to a spreadsheet with a slash in columns.
* SITES-33408: Edge Delivery with Universal Editor: fix Spreadsheets don't appear as modified after making changes.
* SITES-31992: GraphQL: Fix sporadical errors in model scan during bundles startup.
* SITES-29967: GraphiQL: Long query names are cut off.
* SITES-26266: Content references that don't start with `/` are not returned from BE response (Java API).
* SITES-17874: GraphQL persisted queries: Fix encoding for content-type application/graphql-response+json.
* SITES-24506: Screen readers informed on search results.
* SITES-25268: Screen reader improvements for annotations.
* SITES-32366: Spell Check results hidden behind RTE dialog.
* SITES-32829: MediaQuery emulator improvements to parse media query level 3 and 4.
* SITES-32278: Tag fields fixed to use field label correctly.
* SITES-25244: Horizontal bar not appearing in image modal anymore.
* SITES-33395: Fixed rollout button functionality for Content Fragment live copy synchronization.
* SITES-33147: Fixed service binding issue affecting live relationship functionality.
* SITES-33528: Fixed timestamp preservation issue during launch promotion.
* SITES-33014: Fixed excessive warning log generation from LaunchesAdapterFactory.
* SITES-32305: Fixed live copy inheritance break functionality after layout changes.
* SITES-32268: Disable URL encoding for Content Fragment Search.
* SITES-32772: Property locked in variation's fields was always false when enabling the enhancements from SITES-31455 - related to unifying etag value.
* SITES-32696: Fixed issue when a Content Fragment Live Copy field with broken inheritance couldn't not be edited anymore.
* SITES-31712: Slow Queries from the Omni-search on prod Author.
* SITES-33039: Page Events not triggering correctly.
* SITES-31192: Experience Fragments losing Version History after being moved.
* SITES-33529: Error while linking the ACS Campaign templates with AEM pages.
* SITES-33678: Add Toggle for SITES-33529.
* SITES-33468: AEMaaCS unable to connect to ACS.

### Altered Functionality {#altered-functionality-21772}

* SITES-26344: Unify validation of `fragmentId`/`modelId` between endpoints - these ids are now validated and a 400 status code is returned if they are not valid.
* SITES-29598: Validate Content Fragment references added in fragment reference fields when updating a Content Fragment Model.

### Known Issues {#known-issues-21772}

* SITES-31791: Content Fragments GraphQL - Query failing with "Maximum field count exceeded". See [Knowledge Base article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-27231).
* Apache HTTPD version 2.4.65 includes changes that may impact certain configurations as a result of new restrictions implemented to address the vulnerabilities outlined in the security fixes.  

### Deprecated Features and APIs {#deprecated-21772}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-21772}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 35 identified vulnerabilities, reinforcing our commitment to robust system protection.
In Apache HTTPD version 2.4.65, the following security vulnerabilities have been addressed: CVE-2024-43204, CVE-2024-43394, CVE-2024-47252, CVE-2025-23048, CVE-2025-49630, CVE-2025-49812, and CVE-2025-53020. See : https://httpd.apache.org/security/vulnerabilities_24.html

### Embedded Technologies {#embedded-tech-21772}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.80.0|[Oak API 1.80.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.80/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.29.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
