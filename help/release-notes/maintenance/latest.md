---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 16357 {#release-16357}

Summarized below are the continuous improvements for maintenance release 16357, which was publicly released on May 22, 2024. The previous maintenance release was release 16145.

2024.5.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-16357}

* SITES-19579: Java API to migrate content fragments from one model to the other.
* SITES-19698: [Open API] Create read operation for managing a UI Schema per model in the OpenAPI definition.
* SITES-19834: Adobe I/O event missing ids for publish/unpublishing.
* SITES-20146: Enable Preview Version / Compare for moved pages.
* SITES-19973: CFM Search API Implementation.
* SITES-20333: Improve validation when creating Content Fragments.
* SITES-20334: Improve validation when editing Content Fragment Models.
* SITES-20585: Enhance Content Fragment Search API to filter by locale.
* SITES-20594: Return the full name of the user creating/modifying/replicating a resource.
* SITES-20601: [OpenAPI] Update CF Search API to allow fetching only direct children content fragments.
* SITES-20656: [BE] Provide option to match case when replacing a string.
* SITES-20405: [Xwalk] Support mimeType for field collapsing.
* SITES-17854: Support UUID for CF & assets references (Pfizer MVP).
* SITES-19555: Simple Model API for UI schema.
* SITES-19611: [Open API] Create write/update operation for managing a UI Schema per model in the OpenAPI definition.
* SITES-19614: [Xwalk] Spreadsheet pagination / infinite scroll.
* SITES-20005: The author pipeline should have a configurable event delay.
* SITES-20121: Allow defaultValue for enum fields.
* SITES-20342: [Backend] Publish at the folder level - add filter to only publish CFs.
* SITES-20355: Remove content fragment models and permissions API servlets.
* SITES-20387: Navigating the tagadmin always calculates the tag usage.
* SITES-20495: [BE] Ability to get the permission to publish at folder level.
* SITES-20653: [Xwalk] add experiment-start-date and -end-date.
* SITES-20666: [Xwalk] experiment's should be turned off per default on authoring.
* SITES-20752: [cq-wcm-core] Apple Launches for CFs.
* SITES-20946: Add etag as a property in LIST models endpoint.
* SITES-20947: [persistence] fetch sub task by content fragment id.
* SITES-21012: Merge Model Metadata Schema to product.
* SITES-21769: Use the /jcr:id/ path prefix for resource-by-id retrieval.
* ASSETS-30379: DRM License check walks entire tree of assets being downloaded.
* ASSETS-35535: [DaaS Adapter Error] Empty Asset Downloads need to be ignored for v1 Events.
* SITES-21550: [Xwalk] Custom metadata: number, date, datetime, time fields.
* SITES-20149: RTC: [cq-wcm-launches-core] Export new API for Launches for CFs.
* SITES-20150: RTC: [cq-command] Add new methods to existing API.
* SITES-20451: Add sidecar plugin to wcm-commons.
* SITES-20499: [MSM][Async] Extract the code from AsyncOperationServlet to a utility class.
* SITES-20763: Update delivery API endpoints in sites integration.
* SITES-20583: Add etag as property in `LIST`/search fragments.
* CQ-4356445: Event Producer & Schema Implementation.
* CQ-4356625: Improve authorization check in languagecopyrendercondition.jsp.
* CQ-4356629: Improve authorization check in isWorkflowUser rendercondition.
* CQ-4356934: Simplify the RequestProcessor API when working with ResponseEntities.
* CQ-4357214: Request processors must not depend on servlet logic.
* SITES-16392: Failed launch creation should not leave garbage content.
* SITES-20238: [RTC] Pfizer MVP - Add CF API to resolve CF paths to IDs and for vice versa.
* SITES-21043: [CF][launches] Side-port performance improvements to Cloud Service.
* SITES-21044: [CF][launches] Side-port async edit payload implementation to Cloud Service.
* FORMS-7483: AEM Forms JSON Schema Parser now supports JSON schema (2020-12).
* FORMS-13209: A handler is included to override Adaptive Forms default submission success and submission failure handlers. You can configure these handlers via Adaptive Forms Rule Editor. 
* FORMS-13612: Screen readers now read error messages, short descriptions, and long descriptions for fields in core component-based Adaptive Forms. Additionally, support has been added to invalidate adaptive form inputs when the form contains errors and is not valid for submission.
* FORMS-12052: A form author can now apply custom functions to preprocess data before submission. 
* FORMS-11295: Added support for SHA256 with ECDSA algorithm for AEM Forms Digital Signature.
* FORMS-9432: An additional content type (REST Endpoint) has been added to the data source cloud configuration. It enables data submission in key-value pairs to an authenticated endpoint.

### Fixed Issues {#fixed-issues-16357}

* SITES-20608: Experience Fragment's with personalization enabled when included in a template causes an infinite loop.
* SITES-19554: [Xwalk] Spreadsheet Editor: Can't empty a cell.
* SITES-19971: Patching a CFM containing tabs changes the order of the fields.
* SITES-20168: Content Fragment Model `locked` field not properly updated.
* SITES-20522: Corrupted Content Fragments break /adobe/sites/cf/fragments endpoint.
* SITES-20816: CF OpenAPI - Output inconsistency with missing model for referenced fragment.
* SITES-21239: Remove ContentFragmentSearchService circular dependency.
* SITES-20582: Searching and listing content fragments should allow depth 0.
* SITES-20559: [MSM][XF][Lufthansa] Rollout of Experience Fragments from masters/language to country/language does not update references.
* SITES-17772: AEM: User with admin group can't unlock page what another user locked.
* SITES-20401: [Xwalk] Section metadata do not support multi-value properties.
* SITES-21391: [OpenAPI Event] No events triggered when modifying the title or tags (properties) of a Content Fragment Model.
* SKYOPS-73234: Error log failure increase on AEM Assets Global DAM program upgrade to AEM release 15553 and PR Id 35362.
* SKYOPS-75341: NoSuchMethodError in distribution Crosswalk bundle.
* SCRNS-3945: Skyline: Unlocalized "Scheduled" string in Screens.
* SITES-20586: Template "Published" timestamp not updated.
* SITES-16674: Inherit rollout configs checkbox not working on live copy properties.
* SITES-18680: Unable to pull reference variations in graphql query (Apple).
* SITES-21233: [CoreCmp] Accordion broken for GS1 US after upgrade to 15860.
* SITES-20367: Issue with Deleting Launches in AEM.
* CQ-4357161: AEM Inbox Payload screen is returning 404.
* SITES-20214: AEM Rollout Configuration Sequence Issue on Save.
* SITES-20364: 302 Redirects Not Working with Selector in URL.
* SITES-20547: Truncated Paths in Live Copy Excluded Paths List on AEM as a Cloud Service.
* SITES-20691: Experience Fragment Template Restriction Not Honoring cq:allowedTemplates.
* SITES-21122: AEM CS Live Copy Defect with Content Fragments.
* ASSETS-38723: NPE thrown by MetadataRulesProviderImpl when getReadRulesForMetadataChildNodes() is called before this.readRules is initialized.
* SITES-11727: [GQL] Full hydration of content fragment references is missing data.
* SITES-19462: Asset search is not working properly in AEM Cloud.
* SITES-19994: Close button clocking when users try to close Content Fragment.
* SITES-20029: Content fragment Versions are created right after closing it without changing the content.
* SITES-21316: Fragment Preview: preview fails due to code changes from SITES-11727.
* SITES-20023: Fileupload is not working for Remote(Next gen assets) assets in multifield.
* ASSETS-37611: "Request to Complete Move Operation" workflow is triggered for un-published asset.
* CQ-4357278: DispatcherServlet throws NPE if getRequestBodyType returns null.
* CQ-4357279: Request processing fails when there is no pathInfo for a request.
* SITES-20496: [Xwalk] No properties option when selecting spreadsheet in site admin.
* FORMS-13827: In the Adaptive Forms Rule Editor, the WHEN operation does not currently support different types of fields with date pickers.
* FORMS-13786: In the Adaptive Forms Rule Editor, the drag-and-drop functionality is not working for custom functions.
* FORMS-13587: In the Adaptive Forms Editor, the Device Emulator feature is not functioning correctly for Core Components based Adaptive Forms.
* FORMS-14376 When a user presses the Reset button, it results in console errors if the static text is marked as unbound.
* FORMS-13801: Even if the terms and conditions component is disabled, the corresponding checkbox remains enabled.
* FORMS-11952: When a form is submitted, the submit URL generated by the form starts with /content/ instead of /portale/, misrouting the request. This prevents the request from reaching the intended servers.
* FORMS-13616: The date picker is showing the current date as one day behind, likely due to a timezone issue, and there's difficulty in setting the correct date format due to this inconsistency and an additional display pattern problem. 
* FORMS-13829: The dropdown, controlled by rules to mimic radio button functionality, fails to populate correctly after a selection is cleared and reselected. The desired behavior is for individual checkboxes to act as radio buttons, allowing only one selection at a time and permitting deselection of all options.
* FORMS-14244: In an Adaptive Form based on an XDP with embedded scripts on checkboxes, the scripts are not executed for elements after such checkboxes.
* FORMS-14267: Users are experiencing consistent timeout errors when sending API requests across development, stage, and production environments. These requests are related to generating PDFs, sometimes with data prefilled using data binding. The issue results in a hanging process that eventually times out but succeeds upon retrying after the error.
* FORMS-11589: For users with only the AEM Forms solution (without any other solutions), the frontend pipeline is not functioning.
* FORMS-13896: In DoR (Document of Record) output, dates, and numbers are displayed in Arabic regardless of whether the input data is merged using Gregorian numbers.

### Known Issues {#known-issues-16357}

None.

### Deprecated Features and APIs {#deprecated-16357}

To know what is deprecated or removed in AEM as a Cloud Service, see [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md).

### Embedded Technologies {#embedded-tech-16357}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.62.0|[Oak API 1.62.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.62.0/index.html)| 
|AEM SLING API | 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.22-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.25.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
