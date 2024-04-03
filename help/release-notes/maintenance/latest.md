---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release X {#release-15738}

Summarized below are the continuous improvements for maintenance release X, which was publicly released on April 3, 2024. The previous maintenance release was release 15575.

2024.3.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-15738}

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
* SITES-11057 - Core Backend - Avoid loading all versions when opening Timeline > Versions
* SKYOPS-63033 - HTTPD - Trim white spaces of dispatcher environment variables
* SKYOPS-65518 - HTTPD - Fail the validator if there are illegal file names in dispatcher folder
* SITES-19626 - Launches - Merge DAM-CFM lastUpdate fields into main
* SITES-19251 - Quick Site - Creation Wizard - Support sites admin ui side rail when theme reference not equals site name
* SITES-15430 - Universal Editor - Universal Editor under AEM Domain
* CQ-4344966 - WCM - Translation - Create Basic Framework for Structural update of sites and Update existing one for assets.
* CQ-4347312 - WCM - Translation - Create workflow to associate "cq:translationsourcejcruuid" in existing source and language copies.
* CQ-4354509 - WCM - Translation - Publish Translation Job Events [OSGi EventAdmin]

### Fixed Issues {#fixed-issues-15738}

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
* SITES-11571 - Content Fragments - GraphQL API - PersistedQueryServlet should send proper error codes
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
* SITES-16834 - Classic UI (Legacy) - Text missing after editing text using Bulk Editor when text has comma's in it.
* SITES-17767 - Content Fragments - Admin - Support allowed cf-models also for folders without a jcr:content node
* SITES-17683 - Content Fragments - Core Backend - Content Fragments are not serializable with Jackson exporter
* SITES-18797 - Content Fragments - Core Backend - GraphQL Results Duplicated After Index Customisation
* SITES-17856 - Content Fragments - Models & Model Editor - CF Models not shown if config is not a folder
* SITES-17071 - Core Backend - Specific page does not display version in timeline
* SITES-17285 - Core Components - Inline Image Crop is different on Author and Publish in AEMaCS 
* SITES-19187 - Core Components - Two methods of placing assets in image component give different results on dialog
* SITES-20077 - Core Components - Inline Image Crop - cropping is wrong and images are blurry
* SITES-17211 - Experience Fragments - Experience Fragments component path picker dialog which shows experience fragments that are deleted
* SITES-17894 - Launches - Promotion of nested launches reverts launch content to a version from its ancestor
* SITES-16042 - MSM - Live Copies - Annotations are displaying incorrectly in the Livecopy after rollouts
* SITES-16691 - MSM - Live Copies - When the customer selects 'rollout' or 'rollout to' from the 'rollout' icon on a component, the 'continue' button is greyed out.
* SITES-16733 - MSM - Live Copies - Blueprint index page cannot be rolled out when rep:policy applied to node
* SITES-17155 - MSM - Live Copies - Headers & Footers are translated back to English when LiveCopy is renamed
* SITES-17492 - MSM - Live Copies - AEM Page Live Copy Layout Inconsistencies
* SITES-19316 - MSM - Live Copies - Reference link to experience fragment does not update in language copy.
* SITES-19347 - MSM - Live Copies - Prod Author slowness and service outage messages - pods restarting frequently - health alerts
* SITES-19790 - MSM - Live Copies - Incorrect preview information after the LiveCopy Creation
* SITES-20086 - MSM - Live Copies - MSM rollout for CF in Assets will roll out all live copies even if one live copy is selected to be rolled out
* SITES-20088 - MSM - Live Copies - Blank Page Issue Post XF Rollout in Properties - AEM as a Cloud Service
* SITES-16854 - Page Editor - Drop targert overlay covers parsys in components with "Select panel" feature
* CQ-4355563 - Projects - The path parameter is wrong. Populating "?appId=aemshell" for project inbox search script
* SITES-16876 - Quick Site - Theme Deployment - CSS and JS missing on preview pages 2
* SITES-18418 - Sites Admin UI - Show/hide functionality for pathfield widget does not work properly when field is required
* SITES-19534 - Sites Admin UI - Unable to Open Effective Permissions Dialog Post AEM 6.5.19 Upgrade
* SITES-19203 - Template Editor - Editable Template policies Text Missaligned and Styles overlap delete button
* CQ-4354881 - WCM - Translation - Content fragments path is set to source (en-us) when content fragments are translated as part of a page
* CQ-4355289 - WCM - Translation - Only the first 40 elements are displayed in Translation Cloud Services
* CQ-4355866 - WCM - Translation - Translation workflow throwing error for existing pages
* CQ-4355797 - Workflow - Unable to use OOTB workflow step
* GRANITE-48938 - Workflow - Author showing stalled in a 'pending publication' state for assets. Issue in the new persisted payload map cache.
* GRANITE-49036 - Workflow - Feature Request | Ability to schedule and configure purge of workflow packages
* SITES-17393 - Workflow Extensions - Publish content tree fails when using workflow launchers for cq:Tag
* SITES-17759 - Workflow Extensions - Tree-Activation-Workflow for tags not working in AEMaaCS

### Known Issues {#known-issues-15738}

None.

### Deprecated Features and APIs {#deprecated-15738}

JWT.

Have a look at [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) to know what has been deprecated or removed in AEM as a Cloud Service.

### Change Notice {#change-notice-X}

**Actions Required**

#### Set CM Java Version to 11 {#set-java-version-11}

The new version of the aem-sdk-api contains classes compiled with a Java 11 target, which is not compatible with the Cloud Manager Build environment default JDK version 1.8. This update requires that Maven is executed using JDK 11.

Customers are advised to add a `.cloudmanager/java-version` file to the root of their git repo with the contents: `11`. See [Build Environment / Setting the Maven JDK Version](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#alternate-maven-jdk-version).


### Embedded Technologies {#embedded-tech-15738}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.60-T20240131102219-0cde853|[Oak API 1.60.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.60.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.24.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
