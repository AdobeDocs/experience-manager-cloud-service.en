---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 17882 {#release-17882}

Summarized below are the continuous improvements for maintenance release 17882, which was publicly released on September 24, 2024. The previous maintenance release was release 17689.

The 2024.10.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-17882}

* ASSETS - 37750: [Priority 4] [GraphQL] Support for DM scene7 URLs: image smart crops.
* CQ - 4354583: [AEMaaCS] Send translation process events via Adobe Pipeline.
* CQ - 4357642: Update MSFT credentials in OOTB Connector.
* CQ - 4358217: Deserialise request body from request entity.
* CQ - 4358342: Register RequestProcessors on only one HTTP method.
* FORMS - 10781: Enhance rule editor to create rules for next/prev item in a panel.
* FORMS - 14595: [Browserless Feature] Values are missing in the DoR when prefilled data is used to compute the DoR for Browserless rendering.
* FORMS - 15619: AEM Forms Updated Translation Kit.
* FORMS - 16113: [Adobe Sign]Unable to update agreement status by a different user.
* FORMS - 16155: [Rule Editor] Implement Async function.
* GRANITE - 53872: Add new env vars for IMS Client ID.
* SITES - 23738: Release Core Components 2.27.0.
* SITES - 16610: Content Fragments: Get launch details endpoint.
* SITES - 16614: Content Fragments: Rebase Launch endpoint.
* SITES - 16615: Content Fragments: Promote Launch endpoint.
* SITES - 24215: Content Fragments: Implement Get Launch sources endpoint.
* SITES - 20336: Content Fragments: Improve validation when deleting a Content Fragment Model.
* SITES - 21658: Content Fragments: Upgrade to use UUID-references.
* SITES - 23054: Content Fragments: Copy Content Fragment Models.
* SITES - 23264: Content Fragments: Create a static schema of a model.
* SITES - 23265: Content Fragments: Expose the static schema of a model through the UI schema GET endpoint.
* SITES - 23266: Content Fragments: Customers should be able to add constraints to models.
* SITES - 23778: Content Fragments: Search CFMs should allow searching for models that have never been published.
* SITES - 23335: Content Fragments: Add support for external asset references.
* SITES - 24626: Content Fragments: RTC: Permissions for UUID migration: 2.
* SITES - 24904: Content Fragments: Remove usage of referenced service-user in headless bundle.
* SITES - 23380: GraphQL: use proper API to read asset metadata.
* SITES - 22864: [Edge Delivery] Universal editor with new AEM content structure integration H2 2024.
* SITES - 23584: Foundation component tests fail on Java 17.
* SITES - 23662: User that triggers a publish cannot be extracted from JCR log statements in server logs. 
* SITES - 23756: Allow users with limited privileges access to fullName.
* SITES - 23301: Add support for starting a new workflow `/etc/workflow/models/dam/dam-create-language-copy/jcr:content/model`.
* SITES - 24091: MSM content package split: master.
* SITES - 24114: isSourceRenderCondition: Reduce error log message to DEBUG.
* SITES - 24166: Remote assets mitigation for Touch-UI editor.
* SITES - 24409: Register all request processors on only one HTTP method.
* SITES - 24786: Enhancements for `referencesTree` endpoint.
* SITES - 24833: Remove the validation of HTML input against a list of allowed HTML tags.
* SITES - 25008: Improve handling of PersistenceExceptions and permissions problems.
* SITES - 16770: [Xwalk] Add cache hit/miss metrics to CodeBusHttpClient.
* SITES - 23904: [Xwalk] Rename `repository` in Edge Delivery Services config to `Site Name`.
* SITES - 23518: [Xwalk] To improve authoring performance we should load web renditions of assets.
* SITES - 24428: [Xwalk] Rename `Helix 5` in Edge Delivery Services.
* SITES - 24821: [Xwalk] Make aem.page / aem.live the default.

### Fixed Issues {#fixed-issues-17882}

* CQ - 4356887: Inconsistency in Translation Project Status for Akamai Technologies Inc.
* CQ - 4357878: Translation framework is not setting error state upon vendor failure translation .
* CQ - 4358028: Failed to create project if thumbnail is uploaded.
* CQ - 4358290: Target Setting is NOT Working on Published Page.
* FORMS - 13173: Dropdown list misalignment in Adaptive Form > Rule Editor > Drop object field.
* FORMS - 13873: AFv2: (“-”) in the name of component result in failure of rules.
* FORMS - 14340: Error in instantiation of FormsAndDocumentOmniSearchHandler and CloudStorageSubmitActionInserter.
* FORMS - 15363: Displayed Name in Rule Editor.
* FORMS - 15381: UI enhancement of Authorization Scope message.
* FORMS - 15595: AEM Form TnC Component Consent Text line break issue.
* FORMS - 15623: AEMaaCS Forms - Alternatives to Update Multiple Tables in Dynamics with One POST.
* FORMS - 15682: AEM Forms - Unable to bind DOR to Dynamics FDM.
* FORMS - 15799: Adobe Sign GovCloud Signature page does note render in iframe.
* FORMS - 15835: Post-submission form URL rewrite issue.
* FORMS - 16091: Consuming the restructured Binary.java.
* FORMS - 16096: Forms User does not have access to restendpoint dialog.
* FORMS - 16139: Adding required logging for DoR in core-components form.
* FORMS - 6935: State of active component lacks 3 to 1 contrast ratio.
* FORMS - 7018: Empty element receives focus.
* GRANITE - 53028: NPE In ExternalProcessPollingHandler.
* GRANITE - 53907: Unable to identify service user as workflow super user.
* SITES - 24405: Content Fragments: Extended Info for enums should be more resilient
* SITES - 24816: Content Fragments: ValidationStatus messages order inconsistent.
* SITES - 23024: Content Fragments: Enumeration does not return locked: true in GET fragments.
* SITES - 23269: Content Fragments: Creating CFs allow setting locked fields.
* SITES - 23695: Content Fragments: Tab description is not available in UiSchema
* SITES - 23704: Content Fragments: Multi-value enums not supported in _extendedInfo
* SITES - 24150: Content Fragments: [CF GET Version] Authoring data about creation is missing
* SITES - 24230: Content Fragments: [Search CFM] Fix filtering after `modified` replication status
* SITES - 24233: Content Fragments: [Search CFM] Filtering by `publishedBy` can include unpublished resources
* SITES - 23474: Content Fragments: Pagination should exclude broken resources in Search Fragments.
* SITES - 23781: Content Fragments: Duplicate values not allowed in enumeration fields
* SITES - 23615: Content Fragments: CF copy AuthoringInfo is not updated
* SITES - 23443: GraphQL: GraphQL Cursor query inconsistent behaviour.
* SITES - 10994: Keyboard focus order is not logical.
* SITES - 16357: AEM: Button is truncated in Setup Analytics tab from Sites menu.
* SITES - 19836: Ghost component in container is displayed on publish and preview instances.
* SITES - 22348: Live Copy Overview page fails to load if their are above 100 live copies for a project.
* SITES - 22960: Unclosed resource resolver in ContentFragmentModelOmniSearchHandler.
* SITES - 23284: URL encoding causing blank path browser dialog.
* SITES - 23337: Batch endpoint with `body` fails with casting exception.
* SITES - 23505: Components show incorrect URLs when the page is moved to another location.
* SITES - 23574: Not able to preview / compare to current versions for many pages
* SITES - 23585: Issue with Restoring Inheritance for components having cq:responsive node
* SITES - 23650: Discrepancy in Incoming Links Count in AEM Author Environment
* SITES - 23659: Content Language Servlet regression caused by the toggle FT_* SITES - 9757
* SITES - 23668: Patch live copy with multifield fails with 400
* SITES - 23759: Assets added on experience fragment are not published with Launches (p42408-e171873)
* SITES - 24025: 302 Redirects in AEM returning location header using internal DNS instead of public DNS
* SITES - 24036: Investigation needed for AEM RTE Persisting Characters in ASCII Format
* SITES - 24317: Proxy Configuration not working with Basic Authentication
* SITES - 24355: Live Relationship is not respected for folder created Content Fragments 
* SITES - 24596: [Xwalk] service worker is not loading path mapping from enabled config service.
* SITES - 24918: [Xwalk] 504 errors returned occasionally when using dedicated ip egress.
* SITES - 25044: [xwalk] Bulk meta data does not work with URL property name.
* SITES - 2864: Accessibility - Drag and Drop feature is not keyboard accessible.

### Known Issues {#known-issues-17882}

* FORMS - 15818: Component descriptor entry `OSGI-INF/com.adobe.aemfd.docmanager.impl.*.xml` not found statements in server logs. These are harmless log statements.

### Deprecated Features and APIs {#deprecated-17882}

Please note that we are in the proces of updating `com.day.cq.wcm.api` and with the current release, we have marked as `@Deprecated` a few of its methods and classes. These will be removed in future releases, so please consider switching to their suggested alternatives if you are using any of them.

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-17882}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 16 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-17882}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.68.0|[Oak API 1.68.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.68.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.24-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.27.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
