---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 19352 {#19352}

Summarized below are the continuous improvements for maintenance release 19352, which was publicly released on February 5, 2025. The previous maintenance release was release 19149.

The 2025.2.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-19352}

* FORMS-13998: Add Accordion component.
* FORMS-17913: Add Cards Variant for Radio Group.
* FORMS-17333: Enabling HTML Email Templates in AEM Form Submission.
* FORMS-17702: Enable the PDFs generated in Output Sync APIs to be uploaded to Azure Blob Storage.
* SITES-28282: Edge Delivery with Universal Editor: Provide base path, site name and org as page info for any page.
* SITES-27055: Edge Delivery with Universal Editor: Support query parameters in reverse proxy servlet.
* SITES-26796: Edge Delivery with Universal Editor: Support custom columns for the Taxonomy spreadsheet.
* SITES-26087: Edge Delivery with Universal Editor: Support CSV export for spreadsheets.
* SITES-26265: Edge Delivery with Universal Editor: Display the TA account to integrate with Edge Delivery in the configuration UI.
* SITES-20372: Edge Delivery with Universal Editor: Enable basic MSM use cases for spreadsheets.
* SITES-26681: Edge Delivery with Universal Editor: Support the ?sheet= parameter for the Taxonomy spreadsheets on the author.
* SITES-26479: [Schema] Contents-Fragment Model Scheduled Publication Status Endpoint.
* SITES-25944: [Livecopy Overview] add status "live copy up to date with limited inheritance".
* SITES-28713: [V2] Add structured data support to content scraper.
* SITES-27896: CommentsTab auto opening on notification.
* SITES-26720: User should not be allowed to select an entire Collection from the asset selector.
* SITES-27875: Make any editable within a container moveable by default.
* SITES-28340: Dark Alley Universal Editor Service Plugin.
* SITES-26098: Possibility to avoid publishing referenced pages when publising a Content-Fragment.
* SITES-27789: Support of data attribute data-aue-component in the DOM.
* SITES-25997: Enhance variations to support modified date.
* SITES-28023: GraphQL output for remote asset references (repository + asset ID).
* SITES-26058: Content-Fragment Model Scheduled Publication Status Endpoint.
* SITES-25108: Model Migration for UUID references.
* SITES-26630: Content-Fragment Scheduled Publication Status Endpoint for multiple content fragments.
* SITES-23432: Improve delete references capability.
* SITES-25797: Support for external asset references - GraphQL.
* SITES-17514: Delete endpoint enhancement to unpublish Content-Fragment.
* SITES-14633: Validate Content-Fragment Model create payloads before installing - Dry Run.

### Fixed Issues {#fixed-issues-19352}

* SITES-28415: Edge Delivery with Universal Editor: Fix Open Properties button for spreadsheets.
* SITES-26669: Edge Delivery with Universal Editor: Fix issues when uploading CSV files encoded in UTF-8 with a BOM as spreadsheet.
* SITES-26543: Edge Delivery with Universal Editor: Fix empty blocks without a model rendering incorrect markup.
* SITES-26857: Edge Delivery with Universal Editor: Fix the site authentication token being visible in UI for file-based configurations.
* SITES-26662: Edge Delivery with Universal Editor: Fix issues with case-sensitive bulk-metadata.
* SITES-28133: Publish to "Preview" is causing Content available on Production.
* SITES-27187: Scheduled Page/Asset Activation including references (Experimental) miss to publish references.
* SITES-27264: 2 Content-Fragment-LiveCopy-Creation related Selenium tests are failing consistently on master.
* SITES-26559: Pin query for Content-Fragment models to cqPageLucene index.
* SITES-24469: Interactive element is not keyboard accessible.
* SITES-24518: Name and Model buttons in the Parent Reference table are not keyboard accessible.
* SITES-27937: UISchema constraints are set to null after updating the model.
* SITES-27852: Model UISchema missing Categorizations.
* SITES-27904: MetadataSchema missing from list/search Content-Fragment Models for full projection.
* SITES-26827: Listing Fragments ends up in an infinite loop.
* SITES-27678: [Performance] Prevent unnecessary fetching of _references.
* SITES-27589: UUID Upgrade failure for Content Fragment models with multiple content/fragment reference fields.
* SITES-26679: Unpublish Content Fragments Models should only validate published references.
* SITES-26666: referencesTree and references endpoint returning with different results.
* SITES-26499: Wrong order of tag-field's value in GET fragment(s) & PATCH randomise the order.
* SITES-26585: Fix small description error in the schema.
* SITES-26647: Delete endpoint and UnpublishFragments reference validation can fail for non-admin users.
* SITES-26458: [Search Content-Fragment Model] Fix filtering by replication status.
* SITES-23513: [Content-Fragment Model Editor] Validation fails for "Fragment Reference" - "Allowed Content Fragment Model" property.
* SITES-26575: Unpublishing a fragment from preview should update the previewStatus.
* SITES-26571: Page references cannot be saved when FT_SITES-12435 is enabled.
* SITES-26660: Content fragment version comparison might be broken when @ContentType is of "string" type.
* SITES-26626: Missing customErrorMessage on number & boolean fields.
* SITES-26268: Wrong status code returned if a reference is invalid when creating a fragment.
* FORMS-18098, FORMS-17954: Adaptive Forms fail to load in Internet Explorer mode of Microsoft Edge browser.
* FORMS-17162: Publishing an asset leads to running of OOTB queries which degraded publish performance.

### Known Issues {#known-issues-19352}

None.

### Deprecated Features and APIs {#deprecated-19352}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-19352}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 36 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-19352}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.72.0|[Oak API 1.72.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.72.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.24-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.27.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
