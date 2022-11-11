---
title: Release Notes for 2022.10.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2022.10.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
---

# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions; for example, for those in 2020, 2021, and so on.

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current monthly release (2022.10.0) is November 10, 2022. The next monthly release (2023.1.0) is planned for January 26, 2022.

## Release Video {#release-video}

Have a look at the October 2022 Release Overview video for a summary of the features added in the 2022.10.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3409801/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}


### New features in [!DNL Sites] {#sites-features}
 
* The [Personalization Tab for Experience Fragments](/help/sites-cloud/authoring/fundamentals/experience-fragments.md#personalization-experience-fragment) allows segmentation specification capabilities to the Experience Fragment Editor as well as the flexibility to create nested Experience Fragments whereby headers and footers variations can be created for multiple segments. Prior to the launch of this feature, personalization offered by AEM is only available for site pages, but not for Experience Fragments

* The [Content Fragment Console](/help/sites-cloud/administering/content-fragments/content-fragments-console.md) now enables users to efficiently manage translated content fragments. A 1-click access has been provided to view all the language copies as well. Users are also able to filter the table view by the locale of their interest.

![Content Fragments Languages](/help/release-notes/assets/cfconsole-languages.png)

* Further reduce page load time for visitors by optimizing image sizes settings in templates. Find more information for the image component at [Core WCM Component](https://github.com/adobe/aem-core-wcm-components)

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

* Experience Manager Assets now allows you to upload documents in other supported format types and[ preview them using the included Document Cloud viewer](/help/assets/manage-pdf-documents.md). The supported format types include TXT, RTF, DOC, DOCX, PPT, PPTX, XLS, and XLSX.

  ![PDF rendition for other formats](/help/release-notes/assets/multi-page-other-formats.png)


### New features in [!DNL Assets] prerelease {#prerelease-features-assets}

* Experience Manager Assets now uses an improved artificial intelligence framework for image Smart Tags. This content intelligence results in better relevancy and precision of Smart Tags available to all image assets on ingestion. In addition, orientation information is populated in `cq:tags`, which enables better Search results using the Orientation filter.

   If you are interested in participating in the Beta, [fill this form](https://forms.office.com/pages/responsepage.aspx?id=Wht7-jR7h0OUrtLBeN7O4epXZrTVKKdJkUiHeolccf9UNEwyNEpHVEFaODdBNFZQSlFDREZQOVRRTy4u) by November 14.

* Experience Manager Assets now [supports SAS Token](/help/assets/add-assets.md#asset-bulk-ingestor) in addition to the Access Key for authentication while connecting to Azure Blob Storage data source for ingesting assets using the Bulk Import tool.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features available in [!DNL Forms] prerelease channel {#prerelease-features-forms}

* **Adaptive Forms template editor**: Template editor allows you to pre-define the basic structure and appearance of Adaptive Forms of an organization. This release brings following improvements to the template editor:
  * **[Form Data Model in template editor](/help/forms/creating-adaptive-form.md#edit-form-model-properties-of-an-adaptive-form-edit-form-model)**: You can associate a Form Data Model schema to an Adaptive Form template in the template editor. It helps reduce the time taken to create an Adaptive Form. The option is also added to Adaptive Forms editor to allows users to select or change Form Data Model for existing forms.
  * **[Document of Record in template editor](/help/forms/generate-document-of-record-for-non-xfa-based-adaptive-forms.md#document-of-record-support-in-adaptive-form-editor-dor-support-in-adaptiveform)**: You can now standardize Document of Record generation for all forms created using a template. This helps enhance compliance and standardization for org requirements.

* **[Launch the Adaptive Form wizard from a AEM Sites Page](/help/forms/embed-adaptive-form-aem-sites.md)**: AEM Sites page has extended support for Adaptive Forms. You can now create a new Adaptive Form or embed an existing Adaptive Form while remaining on AEM Sites page. 
* **[Change display alignment for checkboxes and radiobutton in DoR](/help/forms/generate-document-of-record-for-non-xfa-based-adaptive-forms.md#customize-the-branding-information-in-document-of-record-customize-the-branding-information-in-document-of-record)**: You can now set the desired alignment (Horizontal, Vertical, Same as Adaptive Forms) for checkbox and radio button on the Document of Record. This option determines the positioning of checkbox and radio button options in the Document of Record. 

## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* Authors can dynamically enrich product lists with Experience Fragments (example: place banner between product listings).
* The list component now supports associated product / category pages to dynamically show related pages.
* Support for Peregrine 12.5 components was added.
* Support for client-side price loading in product teaser and carousel was added.

## [!DNL Experience Manager as a Cloud Service] Foundation {#foundation}

### What is New {#what-is-new-foundation}

* AEM as a Cloud Service (Author Service) is now integrated with Unified Shell to improve the user experience and unify it with all the other Experience Cloud applications. Refer to AEM as a [Cloud Service on Unified Shell](/help/overview/aem-cloud-service-on-unified-shell.md) for more details.

* As previously mentioned in release notes, using the replication agent admin screen or replication API for distributing content packages larger than 10 MB (nodes with properties, not including binaries) is deprecated and will be enforced in the coming days. Please refer to [Manage Publication](/help/operations/replication.md#manage-publication) or the [Publish Content Tree workflow](/help/operations/replication.md#publish-content-tree-workflow) for the suggested approaches for replicating these large content packages.

* Dispatcher configuration now references a file that lists common marketing campaign query parameters. Customers can choose to uncomment the parameters that are relevant to them, resulting in better caching. Refer to [Marketing campaign parameters](/help/implementing/dispatcher/caching.md#marketing-parameters) for more details.

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes-cloud-manager/release-notes-cm-current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
