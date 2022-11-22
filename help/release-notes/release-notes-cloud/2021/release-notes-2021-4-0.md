---
title: Release Notes for 2021.4.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2021.4.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: 775332b5-24ce-430e-97a2-6eeb80877c64
---
# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for the current (latest) version of [!DNL Adobe Experience Manager] as a Cloud Service.

>[!NOTE]
>From here you can navigate to release notes of previous versions; for example, for those in 2020, 2021 and so on.

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2021.4.0 is May 6, 2021.
The following release (2021.5.0) will be on May 27, 2021.

## AEM as a Cloud Service Foundation{#aem-as-a-cloud-service-foundation}

### What is New {#what-is-new-foundation}

* [Publish Content Tree workflow](/help/operations/replication.md#publish-content-tree-workflow) - A new workflow model and step provides increased performance when publishing deep hierarchies of content.

## [!DNL Adobe Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### What is new in [!DNL Sites] {#what-is-new-sites}

* GraphQL Endpoints - it is now possible to enable the AEM GraphQL API for individual AEM Sites configurations and to create custom GraphQL endpoints for those configurations by using a new GraphQL Console UI. The UI also allows managing GraphQL endpoints. 

* Content Models, enhanced Date&Time data type - it is now possible to configure the Date&Time date type to allow authoring only date, only time, or date and time information. 

* Content Models, enhanced Tags data type - it is now possible to configure the Tags data type to allow authoring single or multiple tags. 

* Content Models, new Tab Placeholder data type - the new Tab Placeholder data type allows grouping data types into sections that will be rendered under tabs in the content fragment editor. 

### Bug fixes in [!DNL Sites] {#bug-fixes-sites}

* Content Fragments - moving content fragments or folders now updates nested references inside the fragment (CQ-4320815)

* GraphQL - persisted queries now support user-defined endpoints that are specific to AEM Sites configurations (CQ-4315928)

## [!DNL Adobe Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### What is new in [!DNL Assets] {#what-is-new-assets}

* [!DNL Experience Manager] does not archive single asset downloads where the original file is downloaded. This enhancement allows for faster downloads. 

* When an asset is downloaded via linkshare option, you can now choose to download or not download the renditions. Previously, all the asset renditions were downloaded.

* Administrators can configure [!DNL Experience Manager] to delete the source of assets after doing a bulk asset ingestions. See [bulk asset ingestion](/help/assets/add-assets.md#asset-bulk-ingestor).

* When executing a health check to import assets in bulk, Experience Manager now provides more information reasons for failures. See [bulk asset ingestion](/help/assets/add-assets.md#asset-bulk-ingestor).

* When importing assets using bulk import tool, administrators now have the option to delete the source files after the import is successful. See [bulk asset ingestion](/help/assets/add-assets.md#asset-bulk-ingestor).

* When editing a metadata schema, a new root path selector field allows administrators to quickly and easily make the selection, thereby reducing the configuration time.

* When editing a metadata schema, a data type is added that provides a free-form text area in the metadata editor. Users can use this text area to enter free-form text as metadata of an asset. See [metadata schema editor](/help/assets/metadata-schemas.md).

* Metadata of many assets can be imported in bulk using a CSV file and can be exported to a CSV file. The default date format is now `yyyy-MM-dd'T'HH:mm:ss.SSSXXX`. Users can leverage a different format by updating the column header. For example, add `Date: DateFormat: yyyy-MM-dd'T'HH:mm:ssXXX` as the column header in the CSV file instead of the word `Date`.

* When browsing assets in Column view, a visual indicator displays the approved or rejected status of each asset.

* When browsing assets in Column view, a visual indicator displays for expired assets.

### Bug fixes in [!DNL Assets] {#bug-fixes-assets}

* When attempting to move multiple assets or folders, an error is logged in the console and the move operation is not completed. Move operation fails if the title cannot be updated. (CQ-4322080)

* A metadata field can be hidden based on a rule such that when a predefined condition is met the metadata is not mandatory. However, such hidden metadata fields are displayed as required fields. (CQ-4321285)

* Bulk metadata import fails because of incorrect date format. (CQ-4319014)

* When a selection is made in the Properties page to update metadata, the interface is slow to respond when there are many options provided by the schema. (CQ-4318538)

* While updating and saving metadata value in a single-line text field, the values in the dropdown menu get deleted, even if edits are disabled on the dropdown menu. (CQ-4317077)

* You can use ellipsis as an annotation to review assets. When a small ellipse is used, the ellipse overlaps with the number of the annotation in the print version. (CQ-4316792)

* The quick publish option does not display when an asset is selected from the search results after searching for it. (CQ-4317748)

## [!DNL Adobe Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### What is new in [!DNL Forms] {#what-is-new-forms}

* **Use Government ID identity authentication method in Adobe Sign enabled Adaptive Forms**

  Powered by advanced machine learning algorithms, Adobe Sign’s Government ID process empowers companies across the globe with the ability to secure a high-quality authentication of their recipient's identity. Now, you can use Government ID identity authentication method in Adobe Sign enabled Adaptive Forms.

  Government ID is a premium identity authentication method that instructs the recipient to [upload the image of a government-issued identity document (driver’s license, national ID, passport)](https://helpx.adobe.com/in/sign/using/adobesign-authentication-government-id.html), and then evaluates that document to ensure it's authentic.

* **Support to use in-form signing experience for asynchronous adaptive form submissions**

  You can now use the in-form signing experience for asynchronous adaptive form submissions. You can also embed an adaptive form in an [!DNL Experience Manager Sites] page and use the in-form signing experience for adaptive form submissions.

* **Support to use a variable to specify an attachment while prepopulating an Adaptive Form for an Assign Task step**

  While prepopulating an Adaptive Form for an Assign Task step, you can now use a document type variable to select an input attachment for the Adaptive Form.

* **Support to use the literal option to set value for a JSON type variable**

  You can use literal option to set value for a JSON type variable in the set variable step of an AEM Workflow. The literal option allows you to specify a JSON in the form of a string.

* **Use local development environment to create Document of Record (DoR)**

  You can use an XDP as a Document of Record template on Cloud Service instances and AEM Forms as a Cloud Service SDK (Local development environment). Previously, the support was limited to Cloud Service instances only.

### Bug fixes in [!DNL Forms] {#bug-fixes-forms}

* When an Adaptive Form configured to not-generate Document of Record is submitted to an AEM Workflow configured to generate Document of Record, no error message is displayed, and the task fails to submit.

### Other updates {#misc-2021-04-0-forms}

* To make easier to recognize content the service now generates live thumbnail for XDP, Dynamic PDF, and Schema files.
* Add ability to move a PDF file to a folder placed in on AEM Forms UI.

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What is New {#what-is-new-commerce}

* Support for category UID - This unlocks 3rd party commerce integrations for systems that use Strings for category ids

* AEM extension for PWA Studio incl. example integration

* New CIF navigation core component that extends WCM navigation core component

* Visual indicator for staged catalog data in AEM storefront

* Commerce endpoint is now configurable via Cloud Manager UI

### Bug Fixes {#bug-fixes-commerce}

* The root category field was not displayed under the commerce tab in the page properties of category pages

## Cloud Manager {#cloud-manager}

This section outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.4.0.

### Release Date {#release-date-cm-april}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.4.0 is April 08, 2021.
The next release is planned for May 06, 2021.

### What's New {#what-is-new-april}

* UI updates to the Add and Edit Program workflows to make it more intuitive.

* A user with requisite permissions can now submit the commerce end point via the UI.

* Environment variables can now be scoped to a specific service, either author or publish. Requires AEM Version `2021.03.5104.20210328T185548Z` or higher.

* The **Manage Git** button is displayed on the Pipelines card even when no pipelines have been configured.

* The version of the AEM project archetype used by Cloud Manager has been updated to version 27.

* Projects in the Adobe I/O Developer Console created by Cloud Manager can no longer be unintentionally edited or deleted.

* When a user adds a new environment they will be informed that once an environment is created it cannot be moved to a different region. 

* Environment variables can now be scoped to a specific service, either author or publish. Requires AEM Version 2021.03.5104.20210328T185548Z or higher. 

* The error message when starting a pipeline when an environment was deleted has been clarified.

* OSGi bundles provided by Eclipse projects are now excluded from rule `CQBP-84--dependencies`.

### Bug Fixes {#bug-fixes-cm-april}

* When editing the Experience audit page of a pipeline, an input path starting with a slash `( / )` will no longer result in the step being stuck in pending status.

* When a new production pipeline is created, if no content audit override is added by the user, the default homepage was not audited.

* Issues for the `CloudServiceIncompatibleWorkflowProcess` had the incorrect severity in the downloadable issue CSV file. 

* The `Runmode` check was producing false positives on non-folder nodes.

## Best Practices Analyzer {#best-practices-analyzer}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.12 is April 12, 2021.

### Bug Fixes {#bug-fixes-bpa-april}

* Duplicate rows were seen in the BPA reported. This has been fixed.
* BPA UI on AEM version 6.4.2 was throwing a JS error that was disabling the Generate Report button. This has been fixed
