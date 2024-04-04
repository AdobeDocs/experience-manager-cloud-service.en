---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 15787 {#release-15787}

Summarized below are the continuous improvements for maintenance release 15787, which was publicly released on April 4, 2024. The previous maintenance release was release 15575.

2024.3.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-15787}

* SITES-19059 - Content Fragments - OpenAPI - Allow defaultValue for enum fields
* SITES-20013 - Content Fragments - OpenAPI - WCMScriptHelper should abort rendering when no ServletResolver is present
* SITES-19926 - Content Fragments - OpenAPI - Improvements to OnOffTriggerProcessor
* SITES-17945 - Content Fragments - OpenAPI - Get last modified metadata for each version
* SITES-17298 - Content Fragments - OpenAPI - Content Fragment Models Permissions
* SITES-14255 - Content Fragments - OpenAPI - Validate text field uniqueness if unique flag is set in the fragment model
* SITES-15557 - Content Fragments - OpenAPI - Allow defaultValue for enum fields
* SITES-1559 - Content Fragments - OpenAPI - Update CF List API to allow fetching only direct children content fragments (BE)
* SITES-16052 - Content Fragments - OpenAPI - Add the URL for the instance where a resource could be consumed
* SITES-17944 - Content Fragments - OpenAPI - Proper JCR ACLs mapping to CF Permissions endpoint
* SITES-17513 - Content Fragment Control Plane - Unpublish content fragments
* SITES-8831 - Content Fragment Control Plane - PUT - Update a fragment with full information
* SITES-8836 - Content Fragments - OpenAPI -  Control Plane - GET References - Get parent references of a fragment (by UUID)
* SITES-8986 - Content Fragments - OpenAPI - Publish Content Fragment Model
* SITES-18073 - Content Fragments - OpenAPI - PreviewURL Pattern for a CFM
* SITES-15242 - Content Fragments - OpenAPI - Extend the publish events to provide information about the tier
* SITES-18702 - Content Fragments - OpenAPI - [Backend] Ability to publish at the folder level
* SITES-20020 - Content Fragments - OpenAPI - Remove `X-Adobe-Accept-Unsupported-API` before GA
* SITES-16066 - Content Fragments - Fragment Editor - Change asset selector JS URL
* SITES-19326 - Content Fragments - Fragment Editor - Update links in Assets UI to open CF in new CF Editor
* SITES-10515 - Content Fragments - GraphQL API - GraphQL - AbstractFetcher Performance Issue Loading Referenced Content Fragments
* SITES-17364 - Content Fragments - GraphQL API - Return Full Name for the Modified by  and Published by properties
* SITES-19165 - Content Fragments - GraphQL API - Allow global models to be used, referenced and queryable in all GraphQL endpoints
* SITES-17768 - Content Fragments - GraphQL API - Expose Dynamic Media URL for images via _dmS7Url
* SITES-11057 - Core Backend - Avoid loading all versions when opening Timeline > Versions
* SKYOPS-63033 - HTTPD - Trim white spaces of dispatcher environment variables
* SKYOPS-65518 - HTTPD - Fail the validator if there are illegal file names in dispatcher folder
* SITES-19626 - Launches - Merge DAM-CFM lastUpdate fields into main
* SITES-19251 - Quick Site - Creation Wizard - Support sites admin ui side rail when theme reference not equals site name
* SITES-15430 - Universal Editor - Universal Editor under AEM Domain
* CQ-4344966 - WCM - Translation - Create Basic Framework for Structural update of sites and Update existing one for assets
* CQ-4347312 - WCM - Translation - Create workflow to associate "cq:translationsourcejcruuid" in existing source and language copies
* CQ-4354509 - WCM - Translation - Publish Translation Job Events [OSGi EventAdmin]
* SITES-16318 - Crosswalk - AEM-based authoring with Edge Delivery Services
* FORMS-9889: The user can add the POST URL and Cloud configuration while configuring the Submit action for Submit to REST Endpoint
* In the rule editor, users can:
    * FORMS-12160: Validate a field, panel, or form in the Then section of the When condition.
    * FORMS-12570: Reset a field, panel, or form in the Then section of the When condition.
    * FORMS-11541: Use field objects and global objects in the rule editor through the custom functions.
    * FORMS-11714: Define parameters as optional in the custom function. By default, parameters declared in custom functions are mandatory.
    * FORMS-11756: Use caching for custom functions to improve the response time when retrieving the custom function list in the rule editor.
    * FORMS-12053: Add an 'else' statement in the 'When' condition to implement nested conditions.
    * FORMS-11269: Use modern ES10 JavaScript features such as let and arrow functions in the custom function for core components based forms.
    
* FORMS-9014: Various accessibility related improvements to the scribble Signature component


### Fixed Issues {#fixed-issues-15787}

* Various accessibility and internationalization issues fixed
* SITES-16966 - AEM: Unlocalized "Not Versioned!" string in Sites > Restore > Restore Tree
* SITES-16208 - The ContentFragmentModelIdentifier exposes a misleading title property
* SITES-18024 - When the If-Match header is missing the response must be 428
* SITES-18003 - The user that created a version is not returned correctly
* SITES-17937 - The Content Fragment Created event is emitted before the author pods have synced
* SITES-18029 - The eventing processing pipeline hangs when notified concurrently by JCR observation
* SITES-17882 - Remove fragment text field max length limit from the schema
* SITES-19252 - Fix inconsistencies related to the HTTP status code 406 and 415
* SITES-16964 - [Backend] Sorting by "Modified By" is not working properly
* SITES-17519 - Sites Page properties editor - Long page name is making the buttons non clickable
* SITES-16852 - Publish API is publishing references with NEW status
* SITES-18833 - Uniqueness constraint in not visible in OpenAPI endpoints
* SITES-15553 - XF's side panel failed to load if the XF's URL contains a selector
* SITES-14340 - NPE in VersioningTimelineEventProvider.accepts
* SITES-1605 - [Sites] DeletePageCommand throws NPE in case of null source-path
* SITES-16308 - [GB18030]: Warning message appear when create new Sites folder named with GB18030 characters
* SITES-16304 - [GB18030]: Warning message appear when create new Experience Fragments folder named with GB18030 characters
* SITES-8769 - Improve StyleImpl performance
* CQ-4343815 - Campaign - Targeting - Default variant of a teaser have empty url 
* CQ-4355889 - Campaign - Targeting - Create Audience request fails with IMS Config.
* SITES-12460 - Campaign Integration - Campaign / AEM Cloud Service Integration broken
* SITES-11571 - Content Fragments - GraphQL API - PersistedQueryServlet should send 400s on malformed URLs
* SITES-19946 - Content Fragments - GraphQL API - Models are not scanned anymore at startup
* SITES-1605 - Core Backend - DeletePageCommand throws NPE in case of null source-path
* SITES-5429 - Core Backend - ChildrenListServlet itemResourceType allows direct execution of code
* SITES-15553 - Experience Fragments - XF's side panel failed to load if the XF's URL contains a selector
* SITES-13666 - Headless - Admin - Error Log False Positive "com.adobe.cq.dam.cfm.headless.ui.impl.models.CFHomeCardModelImpl Config Id must not be null"
* SITES-17164 - Page Editor - [Cloud, 6.5 Forms] AF Theme Editor preview is broken
* SITES-14340 - Sites Admin UI - NPE in VersioningTimelineEventProvider.accepts
* SKYOPS-68611 - Sling - repoinit - Port sling repoinit create path fix into the maintenance branch
* CQ-4354678 - WCM - Translation - Translation jobs are exporting translated content
* CQ-4355167 - WCM - Translation - Not getting popup while marking a Translation job Complete or Archive
* CQ-4355913 - WCM - Translation - Translation project language cards erroring out
* GRANITE-47694 - Workflow - Unable to get subtasks in a workflow on cloud for non admin user
* ASSETS-31097 - Assets Cloud - Logs filled up with index Traversed warnings for /bin/numberofentitiesinfolders.json 
* ASSETS-35860 - Assets Cloud - Incorrect Time Zone Conversion in AEM Assets Column View
* SITES-15260 - Classic UI (Legacy) - Bulkedit adds EMPTY properties on page if sheet import is used
* SITES-16834 - Classic UI (Legacy) - Text missing after editing text using Bulk Editor when text has comma's in it
* SITES-17767 - Content Fragments - Admin - Support allowed cf-models also for folders without a jcr:content node
* SITES-17683 - Content Fragments - Core Backend - Content Fragments are not serializable with Jackson exporter
* SITES-18797 - Content Fragments - Core Backend - GraphQL Results Duplicated After Index Customisation
* SITES-18076 - Content Fragments - Core Backend - Multi-value text has incorrect @TypeHint
* SITES-17856 - Content Fragments - Models & Model Editor - CF Models not shown if config is not a folder
* SITES-17071 - Core Backend - Specific page does not display version in timeline
* SITES-17285 - Core Components - Inline Image Crop is different on Author and Publish in AEMaCS 
* SITES-19187 - Core Components - Two methods of placing assets in image component give different results on dialog
* SITES-20077 - Core Components - Inline Image Crop - cropping is wrong and images are blurry
* SITES-17211 - Experience Fragments - Experience Fragments component path picker dialog which shows experience fragments that are deleted
* SITES-17894 - Launches - Promotion of nested launches reverts launch content to a version from its ancestor
* SITES-16042 - MSM - Live Copies - Annotations are displaying incorrectly in the Livecopy after rollouts
* SITES-16691 - MSM - Live Copies - When the customer selects 'rollout' or 'rollout to' from the 'rollout' icon on a component, the 'continue' button is grayed out.
* SITES-16733 - MSM - Live Copies - Blueprint index page cannot be rolled out when rep:policy applied to node
* SITES-17155 - MSM - Live Copies - Headers & Footers are translated back to English when LiveCopy is renamed
* SITES-17492 - MSM - Live Copies - AEM Page Live Copy Layout Inconsistencies
* SITES-19316 - MSM - Live Copies - Reference link to experience fragment does not update in language copy
* SITES-19347 - MSM - Live Copies - Prod Author slowness and service outage messages - pods restarting frequently - health alerts
* SITES-19790 - MSM - Live Copies - Incorrect preview information after the LiveCopy Creation
* SITES-20086 - MSM - Live Copies - MSM rollout for CF in Assets will roll out all live copies even if one live copy is selected to be rolled out
* SITES-20088 - MSM - Live Copies - Blank Page Issue Post XF Rollout in Properties - AEM as a Cloud Service
* SITES-16854 - Page Editor - Drop target overlay covers parsys in components with "Select panel" feature
* CQ-4355563 - Projects - The path parameter is wrong. Populating "?appId=aemshell" for project inbox search script
* SITES-16876 - Quick Site - Theme Deployment - CSS and JS missing on preview pages 2
* SITES-18418 - Sites Admin UI - Show/hide functionality for pathfield widget does not work properly when field is required
* SITES-19534 - Sites Admin UI - Unable to Open Effective Permissions Dialog Post AEM 6.5.19 Upgrade
* SITES-19203 - Template Editor - Editable Template policies Text Misaligned and Styles overlap delete button
* CQ-4354881 - WCM - Translation - Content fragments path is set to source (en-us) when content fragments are translated as part of a page
* CQ-4355289 - WCM - Translation - Only the first 40 elements are displayed in Translation Cloud Services
* CQ-4355866 - WCM - Translation - Translation workflow throwing error for existing pages
* CQ-4355797 - Workflow - Unable to use OOTB workflow step
* GRANITE-48938 - Workflow - Author showing stalled in a 'pending publication' state for assets. Issue in the new persisted payload map cache.
* GRANITE-49036 - Workflow - Feature Request | Ability to schedule and configure purge of workflow packages
* SITES-17393 - Workflow Extensions - Publish content tree fails when using workflow launchers for cq:Tag
* SITES-17759 - Workflow Extensions - Tree-Activation-Workflow for tags not working in AEMaaCS
* FORMS-12411: On Android devices, the `Maximum Number of Characters Validation` option is not working for the Adaptive Form Textbox component. 
* FORMS-13377: When a user tries to add the custom font and run the pipeline to configure it, it fails with the 'ContainersNotReady' error
* FORMS-13267: When a user adds an Adaptive Form Dropdown component, the ID for the Dropdown fails to generate
* FORMS-13544: When a user adds an Adaptive Form Container component with a wizard layout, it does not work properly during form authoring
* FORMS-13091, FORMS-13414: If user tries to configure a custom domain URL in the Azure Blob storage, it fails
* FORMS-13595: When a user tries to save the form in a different location, the user is unable to see the "Select Folder" and "Cancel" buttons if the browser resolution is set to 100%. However, the option is visible  when resolution is set to 75%
* FORMS-10952: When a user adds an Adaptive Form Dropdown component to an Adaptive Form and uses the 'Set Options' property based on various custom rules, the 'Set Options' property functions only for the last rule
* FORMS-11471: The lazy loading of a fragment fails when the 'emitter.json' call fails due to a network interruption.
* FORMS-11786: When a user switches between months in the calendar widget, the date picker component shows an extra row.
* FORMS-12093, FORMS-12093: When a user ticks the Adaptive Form Checkbox to submit a form, the incorrect value with an extra  `\` is stored in the textbox
* FORMS-11993: When a user clicks an image using the "Take a photo" in the Attachment component on an iOS device, all images are added to the folder with the same name
* FORMS-12555: When a user tries to integrate AEM Forms to a mailing platform with an AEM published URL, AEM Forms does not add method=post while rendering the page. This issue occurs even though POST is set in the submit action with the URL. It causes the mailing platform to not recognize this as a form
* FORMS-12938: The HTML5 forms are not functioning or loading properly in the Microsoft Edge browser with IE compatibility mode
* FORMS-12032: When a user submits a form, the path for the submit action path is not pointing correctly
* FORMS-12445: Wrong values are captured in the Form Data Model after the order of the Radio Button options is changed and the form is published.
* FORMS-12947: When a user adds a new language to an existing dictionary, it fails to merge or add
* FORMS-11363: When a user submits a form via Workspace, a display issue occurs in the tables while it is rendered
* FORMS-11756: When a user adds the ES6 JavaScript features such as `let` and `const` in custom functions, the rule editor fails to open. This maintenance release brings support for ES10 
* FORMS-13164: If the user generates a PDF, unexpected blank lines are added to it after submission
* FORMS-13789: When user tries to generate multiple PDFs, the Output batch API fails
* FORMS-11483: When a user converts PDF to PDF/A-2B or PDF/A-3B, it fails to convert and shows a validation error
* FORMS-10501: When a user invokes HSM, the documents are certified but it does not enable LTV
* FORMS-11546: When a form author uses repeated panels in an Adaptive Form, the ARIA attribute is missing from the HTML tags. This improves accessibility of repeated panels of Adaptive Form
* FORMS-11826: Due to matching labels Arial&reg; labelledby and Arial&reg; label, the screen readers are not able to distinguish between these two. To resolve the issue – the label "aria-labelledby" is replaced with "aria-describedby" for the form fields. (F). This improves accessibility of Adaptive Forms
* FORMS-12626, FORMS-13094: Users are unable to access the toolbar using the keyboard to save or edit content on the form editor page. This accessibility issue was fixed
* FORMS-13102: During the form authoring process, the icons available on the Forms and Documents page lack descriptive features for differently abled individuals. This accessibility issue was fixed

### Known Issues {#known-issues-15787}

* SITES-17934 - Content Fragments - Preview fails due to DoS protection for large tree of fragments. See [KB](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-23945)

### Deprecated Features and APIs {#deprecated-15787}

* [JWT Credentials Deprecation in Adobe Developer Console](/help/security/jwt-credentials-deprecation-in-adobe-developer-console.md)

Have a look at [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) to know what has been deprecated or removed in AEM as a Cloud Service.

### Change Notice {#change-notice-15787}

**Actions Required**

#### Set CM Java Version to 11 {#set-java-version-11}

The new version of the aem-sdk-api contains classes compiled with a Java 11 target, which is not compatible with the Cloud Manager Build environment default JDK version 1.8. This update requires that Maven is executed using JDK 11.

Customers are advised to add a `.cloudmanager/java-version` file to the root of their git repo with the contents: `11`. See [Build Environment / Setting the Maven JDK Version](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#alternate-maven-jdk-version).


### Embedded Technologies {#embedded-tech-15787}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.60-T20240131102219-0cde853|[Oak API 1.60.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.60.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.24.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
