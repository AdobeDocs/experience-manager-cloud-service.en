---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 27083 {#release-27083}

Summarized below are the continuous improvements for maintenance release 27083, which was publicly released on July 15, 2026. The previous maintenance release was release 26908.

The 2026.7.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-27083}

* CQ-4354303:Added ability to Delete Translation Configuration.
* FORMS-23746: Data type mismatch between InvokeDDX and Asset Upload workflow steps that prevented using them in sequence.
* FORMS-24585: AEP Connector with easier provisioning.
* FORMS-25250: Introduced ConvertPdf service.
* FORMS-26044: Added file attachment virus/malware scanning for uploads on AF1 and Core Component-based forms.
* GRANITE-69298: Add `cqPageContent-5` and `graphqlConfig-3` indexes.
* SITES-42563: Edge Delivery with Universal Editor: show publishing errors in Universal Editor and Sites Admin (early access).
* SITES-42792: Truncated 'Select Path of Launch Source' placeholder in filter panel in 'Tools' > 'General' > 'Launches'.
* SITES-43178: AEM: Localized time format includes AM / PM in Tools > Sites > Launches.
* SITES-44344: Content API: Treat MSM/language copies as part of the parent site.
* SITES-44598: Present Preflight button in the editor header bar.
* SITES-44676: Content Fragment search results now include the metadata schema ID for each fragment.
* SITES-44767: Added a default metadata schema for Content Fragments.
* SITES-45651: Corrected the OpenAPI Content Fragment example in the API specification.
* SITES-45664: Added a new GET `/cf/metadata/schemas` endpoint to retrieve filterable metadata properties.
* SITES-45725: Content API: add request correlation filter to enable Oak traversal SLO alerting.
* SITES-45817: Edge Delivery with Universal Editor: verify edge delivery roles and permissions while publishing (early access).
* SITES-45842: Edge Delivery with Universal Editor: retain Universal Editor instrumentation for read-only and review/commenting use cases.
* SITES-45848: Edge Delivery with Universal Editor: validate `json-ld` before publishing.
* SITES-46768: Edge Delivery with Universal Editor: show site creation issues in the site creation wizard.

### Fixed Issues {#fixed-issues-27083}

* CQ-4364078: Fixed rewriting of internal links inside Experience Fragments by Language Copy.
* CQ-4364077: Fixed breaking of Language Copy creation due to OakState0001 conflicts.
* CQ-4363949: Fixed incorrect re-addition of unchanged referenced Experience Fragments in Update-Only Translation.
* CQ-4363942: Tags UI: 'Add Language' dropdown, now shows unlisted locales that were not visible despite persisting in JCR.
* CQ-4363527: Fixed Language Copy widget UI glitch for Agentic Method & Provider.
* FORMS-25979: Upgraded Underscore.js library (1.13.6 → 1.13.8+) in AEM Forms Add-on.
* FORMS-18969: Fixed an issue where AEM Forms Themes prevented users from updating the form preview.
* FORMS-25184: Fixed missing data binding indicator dots in the Data Sources side panel for Core Component-based forms (AF v2).
* FORMS-18721: Fixed an issue preventing AEM Forms Themes from updating the base client library.
* FORMS-19235: Fixed an application error that could expose sensitive information in Forms Manager.
* FORMS-25369: Fixed an issue where copying a theme did not carry over clientlib dependencies from the base client library metadata.
* FORMS-25372: Fixed prefill failures and JSON merge issues affecting embedded Adaptive Forms.
* FORMS-24853: Fixed a tabbing issue with the Scribble signature component (Foundation Component) in Adaptive Forms.
* SCRNS-5141: Screens: Outgoing transition on embedded sequence causes blank/grey content area instead of transitioning from existing content.
* SITES-41928: Contexthub + Unified Shell overlap makes component menu inaccessible in editor.
* SITES-46579: Content API: Fix repository traversal in RelationshipService language-copy query — define index and rewrite query.
* SITES-44192: Forms/Content API: Content API returns 404 for EDS forms using `sling:configRef` instead of `cq:conf`.
* SITES-29367: GraphQL: Protect ModelManager from faulty `cqPageLucene` index customizations.
* SITES-46521: Content API: `jcr:path` in query is causing query traversal.
* SITES-46784: GraphQL: Models in the ModelManager have to be deduplicated.
* SITES-46304: Content API: Content API page search silently excludes `/content/campaigns`.
* SITES-46769: GraphQL: Per Request DataCache with large content fragment models leads to OOM exceptions.
* SITES-46570: Content API: Use indexed path() operand in the templates query for index push-down.
* SITES-24497: Distinct labels are now provided for repeated landmarks so assistive tech can differentiate between them.
* SITES-24525: Fixed incorrect heading role assigned to modal buttons — screen readers now announce them as buttons.
* SITES-24703: The focus indicator for listbox popup buttons is now fully visible and no longer clipped.
* SITES-25217: The info icon has been enlarged to meet the minimum target-size requirement.
* SITES-25263: Corrected the aria-haspopup value on the Timewarp date field so screen readers announce it correctly.
* SITES-25308: Increased contrast on the Demographic toolbar button focus indicators to meet WCAG minimum.
* SITES-25318: Improved text contrast for input fields in the Demographics toolbar.
* SITES-25364: Input instructions are now programmatically linked to their checkbox so assistive tech announces them together.
* SITES-25377: The Assets side rail no longer reloads its content when the filter field receives focus.
* SITES-40752: Improved keyboard navigation through the side panel components list.
* SITES-41121: Prevented screen readers from announcing a hidden group label alongside the component name.
* SITES-43802: Removed a spurious "false" string that was appearing inside the Insert Component modal.
* SITES-46720: Page-Properties radios lose saved selection after 2026.05+ update (SDK ≥ 26353) – values cleared client-side.
* SITES-46680: Unable to create CF Launch due to Sling servlet mapping in custom code.
* SITES-46327: When creating a launch with the “Inherit source page live data” option enabled, the Experience Fragment from the source page.is not getting inherited, and some links are also breaking.
* SITES-45969: Child pages deleted on launch promotion when using “new template” + “include subpages”.
* SITES-45723: SITES-44245 fix breaks Launches: empty-genericFrom guard suppresses legitimate launch reference rewrites.
* SITES-45689: Intermittent MSM Rollout Failures – “No Source Path” & AccessDeniedException.
* SITES-44918: Indonesian language code displayed IN instead of ID.
* SITES-41427: XF rollout reports success but silently fails when no Live Copy exists – request for proper handling or auto-creation
* SITES-36149: Component duplication in Launch after promotion with live sync.
* SITES-25970: Rollout Dialog for Component UI gets cut.
* SITES-30707: Fixed a hardcoded 'General' label in the Content Fragment Editor to support localization.
* SITES-44228: Fixed an issue where deleting a referenced Content Fragment referenced via uuid, the referencing fragments would not get adjusted.
* SITES-45171: Fixed an issue where the publish request could incorrectly trigger a Request for Activation workflow.
* SITES-46303: Fixed version retrieval to avoid unnecessary card migration attempts.
* SITES-46713: Fixed PATCH operations failing when the user lacks delete permissions required for card migration.
* SITES-46590: Fixed a regression where reverting to a previous version in the Timeline did not refresh the asset card thumbnail in Assets Admin View.
* SITES-47292: Edge Delivery with Universal Editor: fix rendering of merged tags in page metadata.

### Known Issues {#known-issues-27083}

None.

### Deprecated Features and APIs {#deprecated-27083}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-27083}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 18 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-27083}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.2.0 | [Oak 2.2.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.2.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.67 | [Apache Httpd 2.4.67](https://apache.googlesource.com/httpd/+/refs/tags/2.4.67/CHANGES)|
|Dispatcher|2.0.274||
|AEM Core Components| 2.31.2|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
|Java 21|21.0.11|[JDK 21.0.11](https://www.oracle.com/java/technologies/javase/21-0-11-relnotes.html)|
