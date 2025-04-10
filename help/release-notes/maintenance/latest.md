---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 20133 {#20133}

Summarized below are the continuous improvements for maintenance release 20133, which was publicly released on April 1, 2025. The previous maintenance release was release 19823.

The 2025.4.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-20133}

* ASSETS-47850: Restrict adding Scene7 configurations if AEM CS is ES enabled.
* CQ-4359547: Full removal of Guava from git repository.
* FORMS-17551: Added Document of Record (DoR) support for SharePoint list integrations.
* FORMS-18432: Implemented form-specific (regex-based) client-side prefill configuration to enable selective prefill functionality without OSGI-level changes.
* FORMS-18513: Implemented data tree transformation support in AEP Connector to enhance wizard functionality and data handling capabilities.
* FORMS-19068: Added support for AEP Connector submit actions in Forms Manager APIs to enhance form data integration capabilities.
* GRANITE-57717: Update client bundle in AEM.
* SITES-10469: AdapterFactory should always return the same PageManager instance.
* SITES-25130: Release Core Components 2.28.0.
* SITES-25433: Support full page rendering when comparing old versions.
* SITES-25923: LinkInfoStorageImpl can block when no urls are stored anymore.
* SITES-26208: Deleting a Content Fragment via workflow now allows the option to update referencing resources by removing the newly deleted fragment.
* SITES-26500: Adding the option to move Content Fragments via workflow - `move-fragments`.
* SITES-26711: Rollout Trigger - Links are not updating.
* SITES-27583: Experience Fragments losing Version History after being moved.
* SITES-27618: Searching references of a fragment in pages does not return all the results.
* SITES-27781: Implemented model-level validation for Content Fragment references, allowing validation of referenced fragments against their model constraints and required tag.
* SITES-27784: Update SQL query generation to use PATH function instead of `jcr:path`.
* SITES-28040: Adobe Target ExperienceFragmentsReplicationListener is broken.
* SITES-28051: Get the current user's permissions on a Content Fragment: GET /cf/fragments/{fragmentId}/permissions.
* SITES-28190: Setup for Preview Integration Test.
* SITES-28227: When adding assets as references to a fragment, we validate that the asset exists.
* SITES-28248: Toggle Sites Events based on OSGI config.
* SITES-28255: Full name is missing from all 3 audit properties: created, modified, published.
* SITES-28390: PageImpl: Optimize hasContent().
* SITES-28404: Deleting pages on author should unpublish them from Preview Service.
* SITES-28446: Added 2 new fields that weren't visible in the response - the placeholder in NumberModelField and allowed models from LongTextModelField.
* SITES-28536: Create `RENAME` endpoint for Content Fragments.
* SITES-28537: Adding the option to rename Content Fragments via workflow - `rename-fragments`.
* SITES-28538: References must be republished to maintain valid content on author and publish.
* SITES-28549: Create `/cf/domains` to return the domain id based on AEM tier.
* SITES-29026: Added an optional parameter that specifies the locale of the Content Fragment, using a language and country code.
* SITES-29031: Improved logic for PATCH-ing fragments, thus providing better performance.
* SITES-29169: Resources in status PUBLISHED will be republished if they reference a resource that was moved, renamed or deleted.
* SITES-29376: Add Code toggle to validation of published resource deletion.
* SITES-29417: Update `/libs/cq/Page/proxy.jsp` to forward request to jcr:content node instead of including.
* SITES-2947: Create/modify kibana visualization to compare publish rasp.
* SITES-29733: Increased performance of model search by tags of Content Fragments.
* SITES-8316: Content Policies: Cache the ContentPolicyManager.
* SITES-24906: Edge Delivery with Universal Editor: Support author-created spreadsheets without a mapping (early access).
* SITES-24907: Edge Delivery with Universal Editor: Support publishing Assets to multiple sites for MSM use cases (early access).
* SITES-27956: Edge Delivery with Universal Editor: Improve publishing throughput (early access).
* SITES-27956: Edge Delivery with Universal Editor: Improve error handling for publishing to Edge Delivery Services (early access).
* SITES-29602: CIF: Guava usage removal in core-cif-components-core.
* SITES-25785: CIF: Adding product variant selection for CIF  product reference data type.
* SITES-26392: CIF[Experimental]: JSON+LD in CIF Core Components in PDPs.
* SITES-21278: CIF[Experimental]: CIF ability to clear cache.

### Fixed Issues {#fixed-issues-20133}

* CQ-4358378: Handling License Errors in the Translation Execution.
* CQ-4359263: No Message getting showed up in dialog when Job is completed.
* CQ-4359386: Can't Add i18n Dictionary to Translation Project in AEMaaCS.
* FORMS-18068: Bold text rendering issues in Document of Record (DoR) for radio button and checkbox groups using rich text fields.
* FORMS-18189: Modified custom function handling to prevent error logging for empty client libraries and improve error display in UI.
* FORMS-18213: Implemented functionality to hide/exclude disabled fields from Document of Record (DoR) to improve document clarity and user experience.
* FORMS-18271: Forms Theme Editor displays unlocalized error messages, affecting user experience in form configuration and theme customization.
* FORMS-18304: PDF/A-1b documents passing validation in Acrobat and LiveCycle ES4 are incorrectly flagged as non-compliant in AEM 6.5 Forms due to device-dependent color errors.
* FORMS-18325: Added Adobe Experience Platform (AEP) Cloud configuration to enhance form data integration and processing capabilities.
* FORMS-18360: Enhanced SharePoint list scope management for teams sites in Forms Document Management to improve data organization and access control.
* FORMS-18375: Foundation Components based forms incorrectly select recaptcha configurations from `conf/global` folder when no specific configuration container is selected.
* FORMS-18426: SharePoint list lookup functionality fails when list names contain special characters (For example, '-'), affecting form integration with SharePoint lists.
* FORMS-19028: Client-side prefill functionality breaks form event handling, preventing Value commit and DOMContentLoaded events from triggering properly on form load.
* FORMS-6950: Added required ARIA roles and attributes to file system navigator treeview components to improve screen reader accessibility and comply with WCAG 4.1.2 Name, Role, Value (Level A) standard.
* FORMS-7016: Keyboard focus order in Form Editor does not follow logical navigation.
* SITES-1960: Improved performance of JSON preview operation of Content Fragment Editor.
* SITES-24308: Horizontal scroll bar appears when content is resized to 400%.
* SITES-24493: Interactive element does not have the required role.
* SITES-24669: References Rail Window Splitter is not keyboard accessible.
* SITES-26881: AEMaaCS Accessibility Bug - Incorrect Role is provided for the "Three dots" Icon Which beside comment input field.
* SITES-26956: Follow up on SITES-24920 Unable to Move Page in Production Environment.
* SITES-27707: Content Finder asset listing fails due to issues with asset names (6.5 SP22 regression).
* SITES-27757: Edge Delivery with Universal Editor: rewrite icons according to helix-html-pipeline semantics.
* SITES-27780: Unexpected &lt;br&gt; Tag Appears in RTE with Plaintext DefaultPasteMode on SP22.
* SITES-27958: Linkchecker throws "This session has been closed" errors.
* SITES-28149: Custom ExperienceFragmentLinkRewriterProvider Not Triggered During XF Export to Target.
* SITES-28449: Workflow Widget UI Bug - Include Children Not Displaying All Child Pages in AEM.
* SITES-28456: Missing notification on UI in case of saving incorrect persisted query in GraphiQL Explorer (Follow up- SITES-28313).
* SITES-28464: Update fragment query to use formatted dates with milliseconds.
* SITES-28486: Inplace editing in the new Content Fragment Editor does not redirect to old editor.
* SITES-28570: Missing assets metadata is properly handled by Content Fragment's GraphQL.
* SITES-28580: Classic Image Asset Finder Broken After SP22 Upgrade.
* SITES-28600: Launches - Content duplicate.
* SITES-28668: Unable to Promote Launch with LaunchPromotionParameters.
* SITES-28820: Launch prefix added twice inside new variation created on rebase.
* SITES-28877: UE URL Service throwing Exception when local externalizer endpoint is not defined.
* SITES-28956: Tag deletion operation is displaying a warning, if tag referenced by Content Fragments.
* SITES-29208: References and variations are properly returned in situations when a reference field contains an invalid path.
* SITES-29363: Reset live copy button is not working for nested live copy content hierarchy.
* SITES-29369: Assets Event Issue in AIO | Incorrectly Triggering Page Published/Unpublished Events.
* SITES-29972: Delete and Rename actions sometimes produce untrue workflow comment.
* SITES-24631: CIF: Search issue on product field.
* SITES-24902: CIF: Product url format not working as expected for #variant_sku.
* SITES-29191: CIF: Unable to Add More Than 20 SKUs to Product List Component.

### Known Issues {#known-issues-20133}

* SITES-30727: drag and drop may fail for sub-components within the AEM editor.

### Deprecated Features and APIs {#deprecated-20133}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

#### Changes in User Group and Product Profile Synchronization {#changes-user-groups}

When using the Adobe Admin Console for permission management, the following groups MUST NOT be used as they will not be synchronized to AEM anymore:
* AEM Groups that end with _GROUP_NAME_SUFFIX.
* Product profiles from other environments, programs or products.

For more details, please check [Changes in User Group and Product Profile Synchronization](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/changes-in-user-group-and-product-profile-synchronization).

#### Deprecation of SPA Editor {#deprecate-spa-editor}

[The SPA Editor](/help/implementing/developing/hybrid/introduction.md) has been deprecated for new projects starting with release 2025.4.0. The SPA Editor remains supported for existing projects, but should not be used for new projects.

The preferred editors for managing headless content in AEM are:

* [The Universal Editor](/help/edge/wysiwyg-authoring/authoring.md) for visual editing.
* [The Content Fragment Editor](/help/assets/content-fragments/content-fragments-managing.md) for form-based editing.

Further details on this deprecation can be found in the document [SPA Editor Deprecation.](/help/implementing/developing/hybrid/spa-editor-deprecation.md)

### Security Fixes {#security-20133}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 34 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-20133}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.76.0|[Oak API 1.76.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.76.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.26-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.28.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
