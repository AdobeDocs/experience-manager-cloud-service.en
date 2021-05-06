---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
---

# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>From here you can navigate to release notes of previous versions; for example, for those in 2020, 2021 and so on.

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2021.3.0 is April 29, 2021.
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

* Content Fragments - getLastModifieddeep now takes into account the content model's lastModified data (CQ-4319969)

* Content Fragments - moving content fragments or folders now updates nested references inside the fragment (CQ-4320815)

* GraphQL - persisted queries now support user-defined endpoints that are specific to AEM Sites configurations (CQ-4315928)

* Accessibility - improved color contrast in AEM core components (CQ-4320721)

* Accessibility - improved matching of Aria controls with element ID's (CQ-4320243)

* Accessibility - improved keyboard navigation for AEM search component (CQ-4320216)


## [!DNL Adobe Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### What is new in [!DNL Assets] {#what-is-new-assets}

<!-- TBD: refine this list of features and enh. for Feb release.

Customers using the Connected Assets feature can now easily view and track assets used on remote Sites instances. This affords customers a complete view of being used across all Sites powered pages, allowing for better tracking, management, and brand consistency.  

Indicators for expired, approved, and rejected statuses now available for assets in Column view.

Ability to select a root path. select if a minimum number of tags is required. 

Add a Boolean or radio widget type to metadata schema setup. -->

* [!DNL Experience Manager] extends the Connected Assets functionality to support use of [!DNL Dynamic Media] images in the supported core components. See [use Connected Assets](/help/assets/use-assets-across-connected-assets-instances.md).
* Experience Manager administrators can schedule bulk asset ingestions at a specific date or time. Also, administrators can schedule recurring ingestions based on date and time. See [bulk asset ingestion](/help/assets/add-assets.md#asset-bulk-ingestor).

### Bug fixes in [!DNL Assets] {#bug-fixes-assets}

* The copyright page does not display when attempting to download multiple rights-managed assets. (CQ-4314403)
* When choosing to edit an INDD file, the resolution changes unexpectedly. (CQ-4317376)
* Only the last page of the InDesign Template is there in the PDF Rendition. (CQ-4317305)
* Tag picker takes long to open when the picker is part of a complex metadata schema. (CQ-4316426)
* When uploading asset with same filename as an existing one, the name conflict dialog does not display to prompt the user to create a version. (CQ-4315424)
* Folder Metadata Properties can be set and saved from the popup menu in a folder's Properties page. While the selection is saved in the repository, it is not displayed when the Folder Metadata Properties are opened again. (CQ-4314429)
* Assets with filenames containing spaces or special characters get uploaded using the browser. (CQ-4318381)

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

This section outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.4.0 and 2021.3.0.

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


### Release Date {#release-date-cm-march}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.3.0 is March 11, 2021.

### What's New {#what-is-new-march}

* Customers with environments with pre-existing Custom Domain Name configurations for [IP Allow Lists](/help/implementing/cloud-manager/ip-allow-lists/check-ip-allow-list-status.md#pre-existing-cdn), [SSL Certificates](/help/implementing/cloud-manager/managing-ssl-certifications/check-status-ssl-certificate.md#pre-existing-cdn) and [Custom Domain Names](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md#pre-existing-cdn) will see a message about their previously existing configurations and will be able to self-serve via the UI. 

* Users with requisite permissions can now edit a Program, allowing them to do the following in a self-service manner: 

   * Add Sites solution to an existing program with Assets or vice-versa.
   * Remove Sites or Assets from an existing program with both Sites and Assets.
   * Add second, unused solution entitlement either to an existing program or as a new Program. 

* **AEM Push Update** label will now be displayed for both *Pipeline Execution* and *Activity* screens.

*  If an environment is hibernated but there is also an AEM update available, the **Hibernated** status will take precedence over **Update available**.

* Users can now see their Cloud Manager role(s) by selecting the 'View Cloud Manager Role(s)' option after navigating to the User Profile icon (top right) of Unified Shell. 

* The label **Application for Approval** has been relabeled to **Production Approval** for greater clarity.

* The **Version** label has been relabeled to **Git Tag** in the Production pipeline execution screen.

* The labels which define the behavior when important metrics do not meet the defined threshold have been relabeled to reflect their true behavior: **Cancel Immediately** and **Approve Immediately**.

* The class and method deprecation lists have been updated based on version `2021.3.4997.20210303T022849Z-210225` of the AEM Cloud Service SDK.

* Cloud Manager Production pipeline will now include [Custom UI Testing](/help/implementing/cloud-manager/functional-testing.md#custom-ui-testing) capability.

### Bug Fixes {#bug-fixes-cm-march}

* Package versioning was skipped in some cases during AEM push upgrade.

* Some quality issues were not properly discovered when packages were embedded in other packages.

* In obscure situations, the default program name generated upon opening the Add Program dialog could be a duplicate of an existing program name. 

* On occasion, if user navigates away from pipeline execution page immediately after starting a pipeline, an error message is displayed stating that the action failed, although the execution actually starts.

* The build step was unnecessarily restarted when customer builds resulted in invalid packages.

* On occasion, user may see a green "active" status next to an IP Allowlist even when that configuration was not deployed.

* All existing production pipelines will be automatically enabled with the Experience Audit step.

## Content Transfer Tool {#content-transfer-tool}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.3.4 is March 19, 2021.

### Bug Fixes {#bug-fixes-ctt}

* CTT was skipping content from folders with the same name but with a hyphen in the name. This has been fixed. 

### Release Date {#release-date-ctt-march}

The Release Date for Content Transfer Tool v1.3.0 is March 04, 2021.

### What is new in Content Transfer Tool {#what-is-new-ctt-march}

* CTT now installs to `/apps` instead of `/libs` Browser bookmarks to certain pages may no longer be valid.
* When CTT is installed, user will have to navigate an additional level to get to the Content Transfer page. See [Using Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html) for more details.

### Bug Fixes {#bug-fixes-ctt-march}

* When migrating content from a specific path, CTT was pulling in unrelated resources. This has been fixed

## Best Practices Analyzer {#best-practices-analyzer}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.12 is April 12, 2021.

### Bug Fixes {#bug-fixes-bpa-april}

* Duplicate rows were seen in the BPA reported. This has been fixed.
* BPA UI on AEM version 6.4.2 was throwing a JS error that was disabling the Generate Report button. This has been fixed


## Code Refactoring Tools {#code-refactoring-tools}

### What is new in Code Refactoring Tools {#what-is-new-crt}

* New features and enhancements for Repository Modernizer. Refer to [GitHub Resource: Repository Modernizer](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/repository-modernizer) for the latest version.
  * Normalize OSGi configs (except RepoInit configs) to the preferred .cfg.json format.
  * Rename OSGi config folders to the specified format.
  * Generate the ui.apps.structure project.
  * Create the analyze module.
  
* New features and enhancements for Dispatcher Converter. Refer to [GitHub Resource: Dispatcher Converter](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/dispatcher-converter)
  * Creation of separate files for different inclusions instead of in lining the content.
  * Ability to handle both folder path of vhosts and path to vhost files.
  * Generation of farm files with large customer configurations in range of 600 and more.
