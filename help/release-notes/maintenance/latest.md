---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: ed762d86-a04b-452b-a08f-86359bb8ff27
    internal-label: Configuration and operations
subfeature_v2:
  - id: c21ccc2b-e0c8-4853-bf41-f12259ed93f8
    internal-label: Release information
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 29023 {#release-29023}

Summarized below are the continuous improvements for maintenance release 29023, which was publicly released on October X, 2026. The previous maintenance release was release 28871.


The 2026.10.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.


### Enhancements {#enhancements-29023}

* CQ-4363433: Added support for the Composite data type in Content Fragment translation.
* CQ-4364430: Added TBX file upload and an overall terminology view to the AI Translation self-service UI.
* CQ-4364830: Improved watchdog efficiency and logging performance for AI Translation.
* CQ-4365346: Added DITA and DITAMAP translation for assets through AI Translation.
* FORMS-27488: Added authoring of PDF bookmarks on headings in the Interactive Communications editor, including bookmark titles, colors, and styles.
* FORMS-27740: Added a Signature Field component to the Interactive Communications editor, with options to lock all fields or include or exclude a named collection of fields after signing.
* FORMS-27806: Added Dynamic Media asset selection and rendering, including Smart Crop and renditions, to the Image component in Core Components based Adaptive Forms.
* FORMS-27807: Added services to resolve and serve Dynamic Media asset URLs in the Forms Image component, while keeping the existing handling of other image assets.
* FORMS-28099: Added support for reading Signature Field settings and named field collections when generating Interactive Communications documents.
* FORMS-28100: Preserved Signature Field references to named field collections in the Interactive Communications PDF preview.
* FORMS-28241: Added support for saving Signature Field components in Interactive Communications forms.
* SITES-44984, SITES-44985, SITES-45098: Added Live Copy creation and rollout for folders in Multi Site Manager, including Content Fragment folders in the Content Fragments console.
* SITES-45040: Exposed metrics for requests to the remote content rendering service.
* SITES-45041: Applied default timeouts to requests to the remote content rendering service.
* SITES-46485: Introduced the Composite data type for Content Fragments to group and repeat fields (pre-release).
* SITES-49845: Enabled the Commerce Integration Framework GraphQL client to forward the original client IP address (X-Forwarded-For) from the publish tier.
* SITES-50850: Updated AEM Core Components to version 2.33.0.
* SITES-51147: Created a new Content Fragment version when metadata is saved, for history and restoration.
* SITES-51658: Expanded the preview templates list in the Content Fragment model details panel to use the full available height.
* SITES-52174: Respected externally synchronized group memberships when checking preview and publish permissions in Edge Delivery Services with Universal Editor (early access).
* SITES-52365: Improved the performance of path-based Content Fragment API queries and reference searches.
* SITES-53054: Added Content Fragment launch support to the permissions API.

### Fixed Issues {#fixed-issues-29023}

* CQ-4363894: Fixed newly added components that were missed during translation harvesting.
* CQ-4364614: Fixed the Go to Projects button still showing in References > Language Copies after the related translation project was deleted.
* FORMS-20721: Fixed a NullPointerException when saving properties of Core Components based Adaptive Forms whose theme SiteConfig or HtmlConfig configuration nodes were missing.
* FORMS-24748: Fixed the Date Field in the Interactive Communications editor Properties panel accepting text and special characters instead of requiring the yyyy-mm-dd format.
* FORMS-24749: Fixed the Date/Time Field in the Interactive Communications editor accepting incorrectly formatted dates without a validation error.
* FORMS-24988: Removed unnecessary "Suspicious quotes" browser-console warnings for Invoke Service rules with double-quoted object keys in request headers or parameters.
* FORMS-25184: Fixed binding indicators in the Data Sources panel staying grey for Core Components based Adaptive Forms that use a JSON schema.
* FORMS-26500: Fixed iOS submissions of Foundation Components based Adaptive Forms saving only one of several attachments that share the same filename.
* FORMS-26668: Fixed incorrect captcha extractor lookups when submitting Adaptive Forms embedded in Sites.
* FORMS-26813: Fixed the File Attachment component showing a generic unsupported-file-type message instead of the author-configured custom message.
* FORMS-26817: Fixed Reset clearing the author-configured Image component in Core Components based Adaptive Forms.
* FORMS-26824: Fixed rule assignments disappearing from the Rule Editor after a form object was dragged across an already populated action target.
* FORMS-26825: Fixed rules that could not be saved after a form object was clicked without dragging in the Rule Editor.
* FORMS-26826: Removed the "Failed to load custom functions" message shown when the Rule Editor was opened for Core Components based Adaptive Forms.
* FORMS-26827: Fixed actions in the Else section being cleared when a condition was added to a When rule.
* FORMS-26878: Localized the Date Picker validation message for partially entered dates in French Adaptive Forms.
* FORMS-27549: Fixed Edge Delivery Services form downloads from Forms Manager omitting referenced fragments.
* FORMS-27655: Fixed component overlays disappearing and forms staying in a loading state after a rule was saved in Foundation Components based Adaptive Forms.
* FORMS-27768: Fixed text field appearance changes (Underline, Solid Box, None) not updating the value area in the Interactive Communications editor.
* FORMS-27770: Fixed field content disappearing when the top or bottom margin was increased in the Interactive Communications editor.
* FORMS-27808: Fixed the Home icon in the Interactive Communications editor side navigation redirecting authors away from the editor.
* FORMS-27811: Fixed the misaligned image-selection icon and text in the Image component Properties panel of the Interactive Communications editor.
* FORMS-27878: Fixed unnecessary document service restarts during deployment reconciliation in environments with custom fonts.
* FORMS-27932: Fixed paragraph-level vertical padding of Interactive Communications Text components missing from the generated PDF preview.
* FORMS-27938: Fixed bold or italic rich text in the Interactive Communications editor appearing unstyled when a document first loaded.
* FORMS-28033: Fixed bold formatting on the first characters of a list item making the entire line bold in the Interactive Communications rich text editor.
* FORMS-28057: Fixed first-level dependency lookups for Edge Delivery Services forms returning transitive fragment dependencies.
* FORMS-28125: Fixed the Forms Manager theme picker showing Canvas instead of the form's saved theme after a frontend theme was redeployed.
* FORMS-28128: Fixed the Document of Record preview loading endlessly when an Adaptive Form was opened through Unified Shell.
* FORMS-28137: Fixed the Dashed border-style icon in the Interactive Communications editor Appearance accordion.
* FORMS-28169: Fixed documents generated in the asset-upload workflow being saved as attachment_1 without a .pdf extension and with incorrect MIME metadata.
* FORMS-28223: Fixed misaligned width, height, and position labels in the Interactive Communications editor Position accordion.
* FORMS-28225: Fixed slow first Form Data Model requests to Dynamics after an upgrade.
* FORMS-28226: Fixed deleting an Edge Delivery Services Adaptive Form, or a folder containing one, removing shared configuration still used by other forms.
* FORMS-28236: Fixed MISSING_ASSET_EXTENSION failures when publishing Edge Delivery Services forms or fragments with assets that have no filename extension.
* FORMS-28333: Included top and bottom margins when a text box uses vertical autofit.
* FORMS-28433: Fixed horizontal padding missing from the Document of Record PDF preview when a floating-field variable was bound to an Interactive Communications fragment at the start of a line.
* SITES-27753, SITES-50163: Fixed values of the Styles dropdown being hidden in the Text component dialog of the Rich Text Editor.
* SITES-42695: Normalized asset filename extensions to lowercase when previewing assets in Edge Delivery Services with Universal Editor.
* SITES-42804: Localized multi-line field tooltips in the Content Fragment editor.
* SITES-43599: Localized the Structure mode label in the Template Editor.
* SITES-46898: Fixed filename validation for referenced assets with non-ASCII characters when publishing pages in Edge Delivery Services with Universal Editor.
* SITES-47353: Improved the performance of Multi Site Manager live copy source lookups by no longer holding a global lock during repository queries.
* SITES-48793: Fixed GraphQL schema generation causing out-of-memory errors when many models are referenced.
* SITES-48797: Fixed Multi Site Manager rollouts duplicating child URL segments after migration.
* SITES-49323, SITES-49324: Included references stored by UUID in individual and batch Content Fragment reference lookups.
* SITES-49634: Accepted tag identifiers that contain periods in Content Fragment API validation.
* SITES-49677: Fixed an internal server error for Content Fragment update requests with a missing JSON Patch value.
* SITES-49694: Preserved a broken inheritance of a whole multi-value composite field during Multi Site Manager rollout.
* SITES-49818: Fixed Content Fragment reference lists omitting valid referrers when unrelated search matches filled the candidate limit.
* SITES-49824: Fixed Multi Site Manager rollouts failing with a ConstraintViolationException when thumbnails were added after Live Copy creation.
* SITES-49850: Fixed page moves and renames creating incorrect audit entries for access-control policy nodes.
* SITES-50002: Added the missing Live Copy label for Content Fragments in the Assets console.
* SITES-50005: Fixed the Rich Text Editor link anchor popover being clipped near the component dialog boundary.
* SITES-50017: Created archive versions when unpublished pages are deleted, so they can be recovered.
* SITES-50092: Fixed the Rich Text Editor Styles dropdown overflowing the component dialog when multiple style groups are configured.
* SITES-50104: Fixed Content Fragments with composite fields breaking launch creation, editing, rebase, and promotion.
* SITES-50142: Fixed Restore Tree deleting non-versioned pages even when Preserve Non-Versioned Pages is enabled.
* SITES-50195: Improved the performance of direct-reference lookups for live-copy Content Fragments.
* SITES-50347: Fixed reference searches for Content Fragment names that contain angle brackets.
* SITES-50354: Removed queries for the Adobe Commerce-only staged field from the Commerce Integration Framework Product List and Product v2 components, fixing compatibility with Magento Open Source.
* SITES-50420: Removed dead space above the first line in Content Fragment multi-line fields.
* SITES-50435: Fixed the page Modified date not being updated when page content is changed through the Content API.
* SITES-50524, SITES-50525: Localized strings in the Create Launch wizard.
* SITES-50534: Republished renamed Content Fragments, so the publish tier and APIs serve the updated name and path.
* SITES-50660: Included the Content Fragment model when a fragment is published with an empty reference filter.
* SITES-50662: Fixed failed find-and-replace rollbacks changing text to lowercase.
* SITES-50678, SITES-50549: Fixed error 500 when breaking Content Fragment field inheritance on Live Copies, and localized the Live Copy Details rail.
* SITES-50683: Fixed the workflows extension retrieving only a filtered subset of available workflows.
* SITES-50750: Showed a clear error when an Edge Delivery Services hostname exceeds the 63-character DNS label limit.
* SITES-51153: Allowed self-referencing Content Fragment models to be created without a false reference-cycle error.
* SITES-51158: Fixed multi-value serialization of allowedResourceTypes in the Commerce Integration Framework configuration console.
* SITES-51227: Fixed auto-promotion of nested launches.
* SITES-51276: Fixed the path mappings source field not showing for existing Edge Delivery Services sites without an explicit configuration.
* SITES-51383, SITES-53031: Returned a 403 error instead of an error 500 for users without permission to create launches or read launch job results, in the UI and the OpenAPI.
* SITES-51452: Fixed garbled non-ASCII characters when opening spreadsheet CSV exports in Excel by adding a UTF-8 byte order mark.
* SITES-51520: Fixed nested page paths when a single page is mapped to a folder in Edge Delivery Services with Universal Editor.
* SITES-51842: Validated mandatory fields of referenced child Content Fragments when a parent fragment is published.
* SITES-51898: Improved persisted query performance in GraphQL by removing an unnecessary repository scan.
* SITES-51904: Fixed multi-value fragment reference fields returning null when one of the referenced fragments is unpublished.
* SITES-51922: Fixed a 400 Bad Request when paginating Content Fragment admin search results, caused by an incorrect timezone offset.
* SITES-51966: Fixed listing Live Copies for folders in Multi Site Manager.
* SITES-52016: Fixed copying a page to a different parent page through the Content API.
* SITES-52175: Stopped Content Fragment event handling from processing unrelated commerce content and flooding the author logs.
* SITES-52275: Made page properties inherited through HTL bindings reliably available regardless of the bindings provider order.
* SITES-52485: Reused a pooled HTTP client for requests to the remote content rendering service instead of creating a new client for every request.
* SITES-52585: Preserved commas and whitespace in custom single-value page metadata in Edge Delivery Services with Universal Editor.
* SITES-52750: Fixed the Preflight button missing for eligible Adobe LLM Optimizer and AEM Sites Optimizer users.
* SITES-52907: Preserved commas when rewriting rich-text links in Edge Delivery Services with Universal Editor.

### Known Issues {#known-issues-29023}

None.

<!-- Confirm known issues before publication. -->

### Deprecated Features and APIs {#deprecated-29023}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-29023}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release includes X security fixes, reinforcing our commitment to robust system protection.


### Embedded Technologies {#embedded-tech-29023}


|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.6.0 | [Oak 2.6.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.6.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.67 | [Apache Httpd 2.4.67](https://apache.googlesource.com/httpd/+/refs/tags/2.4.67/CHANGES)|
|Dispatcher|2.0.275||
|AEM Core Components| 2.33.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
|Java 21|21.0.11|[JDK 21.0.11](https://www.oracle.com/java/technologies/javase/21-0-11-relnotes.html)|
