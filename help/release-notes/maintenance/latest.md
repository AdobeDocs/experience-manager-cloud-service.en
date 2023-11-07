---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 14157 {#release-14157}

Summarized below are the continuous improvements for maintenance release 14157, which was publicly released on November 7, 2023. This maintenance release is an update from previous maintenance release 14029.

2023.11.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-14157}

* ASSETS-29631: Assets Cloud: Use dam:roles for secure delivery/search
* CQ-4354515: Translations: Option to Suppress translation of referenced resources
* FORMS-9993: Define Steps to move Forms Core Components into Skyline
* FORMS-10570: Onboard EC APIs to API - First Router
* GRANITE-48143: Upgrade Sling ResourceMerger to 1.4.4
* SITES-14874: Eventing: Expand the CFM tree for model events to include metadata changes
* SITES-2719: Content Fragments: Tagging support for Content Fragment Variations (re-enabled)
* SITES-3619: Content Fragments: GraphQL CF variation tags output in JSON and filtering by variation tag (re-enabled)
* SITES-13750: Content Fragments: Delete tags for a Content Fragment Model
* SITES-13920: Content Fragments: Support for minItems config for multiple fields (pre-release)
* SITES-14080: Content Fragments: Delete tag of a Content Fragment Variation
* SITES-14770: Content Fragments: Fragment variation should include fieldTags property
* SITES-15356: Content Fragments: Returning etag as response header when a resource is created
* SITES-15357: Content Fragments: Allow publishing of fragments without their references
* SITES-15938: Content Fragments: Missing content reference metadata
* SITES-16078: Content Fragments: Fill in the validation result property of the variation when a fragment is fetched.
* SITES-16545: Content Fragments: Add endpoint for retrieving the references of a content fragment's variation
* SITES-16853: Content Fragments: Remove /adobe/sites/cf/fragments/{fragmentId}/variation/{name}/tags endpoint

### Fixed Issues {#fixed-issues-14157}

* Various accessibility issues fixed
* ASSETS-31015: Assets Cloud: Unable to upload .msg files
* ASSETS-24739: Assets Cloud: Disable Frame.io Custom Action Endpoint on Publish
* CMGR-49845: Content Backflow: Issue with identifying the correct root path for given checkpoint
* CMGR-49709: Content Backflow: Update the property filter to ignore additional properties
* CQ-4354503: Adobe IMS Configuration getting randomly removed
* CQ-4354414: ConfigurationReplicationEventHandler creates a lot of individual flush actions
* CQ-4354401: Translations: Asset created by Projects must be saved before starting asset processing 
* CQ-4354430: Translations: Getting an error adding assets not part of a language folder structure to a translation project
* CQ-4354412: Translations: Deleting Translation Job Content not deleting all referenced content
* CQ-4354636: Translations: Creating a language copy at language root level does not adjust paths in the page
* CQ-4354700: Workflows: Workflow payload screen does not load
* CQ-4354834: Workflows: Unable to add comment in workflow inbox task
* FORMS-11302: Title of component edited in RTE is displayed incorrectly in Adaptive Form Editor > Rule Editor
* GRANITE-45706: i18n import fails if the key value has ‚Äú))‚Äù
* SITES-14156: Eventing: Publish events are not always sent
* SITES-14520: GraphQL: Bad performance with paginated graphql queries due to FT_SITES-2719
* SITES-16444: GraphQL: DataFetchingException for same name fields missing from GraphQL query
* SITES-16225: GraphQL: Content types of model and fragment RTE fields returned by the Java API are not correct
* SITES-15373: Content Fragments: The /adobe/sites/cf/fragments/{fragmentId}/variation/{name}/tags endpoint doesn't use the correct resource naming conventions
* SITES-15709: Content Fragments: Create Model endpoint issue when creating Boolean Field
* SITES-15727: Content Fragments: Field of type "Tag" can only be added once in model editor
* SITES-15782: Content Fragments: Missing unique property from field model of Enumeration type
* SITES-15786: Content Fragments: Content Fragment cannot be created in folder containing '
* SITES-15790: Content Fragments: Update Location header for Version Creation
* SITES-15923: Content Fragments: CF Admin does not show all folders
* SITES-15987: Content Fragments: Getting 500 while creating variant
* SITES-16067: Content Fragments: The mime type of long text fragment field cannot be modified
* SITES-16074: Content Fragments: Tag fields which are not String[] cannot be retrieved from JCR
* SITES-16079: Content Fragments: /fragments/{id}/references started to return duplicates
* SITES-16118: Content Fragments: If a fragment is patched and a fragment field is missing from the model, an exception is thrown
* SITES-16119: Content Fragments: If the fragment metadata contains unrecognized fields, an exception is thrown
* SITES-16121: Content Fragments: Retrieval of a model date field throws exception
* SITES-16123: Content Fragments: If a resource is not a content fragment, the get fragments endpoint throws an exception
* SITES-16208: Content Fragments: The ContentFragmentModelIdentifier exposes a misleading title property
* SITES-16707: Content Fragments: Content Fragment Models data types are not correctly read
* SITES-16818: Content Fragments: Perform delete only when tags are present
* SITES-16207: Content Fragments: The POST /adobe/sites/cf/models operation returns two different OK status codes
* SITES-15616: Content Fragments: Publish endpoint does not publish sometimes all the references of a Content Fragment
* SITES-16027: Content Fragments: Variation reference information is missing from fragment response
* SITES-16243: Content Fragments: Find and replace does not work with fields having Render as: Multiple
* SITES-16250: Content Fragments: Patching a CF sometimes returns an incorect etag header
* SITES-16686: Content Fragments: Content Fragment non-fragment references are serialised when parent reference is at max depth
* SITES-16234: ContextHub: Correct Selected Brand Activity Name does not show when Start Targeting
* SITES-12880: Fast-Track: Fix localisation for Sites > Setup Analytics
* SITES-16103: Experience Fragments: Target options are not displayed under Cloud Services due to console error 
* SITES-16001: MSM: Ability to exclude multi field components from rollout configuration while creating Live Copy
* SITES-16559: MSM: Rollout configs removed during rollout process for experience fragments
* SITES-16797: MSM: Fixed Re-enable inheritance for a CF field in Editor
* SITES-16273: Page Editor: Copy paste error inside aem sites pages from the clipboard
* SITES-16126: Sites Admin: Authoring performance slow for non admin users after SITES-10288

### Known Issues {#known-issues-14157}

* ASSETS-31015: Unable to upload files to Assets with unknown file extensions.

### Embedded Technologies {#embedded-tech-14157}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.56-T20230927085643-189caed|[Oak API 1.56.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.56.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
