---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
mini-toc-levels: 1
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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2022.10.0) is November 3, 2022.
The next release (2022.12.0) is planned for December 15, 2022.

## Release Video {#release-video}

Have a look at the October 2022 Release Overview video for a summary of the features added in the 2022.10.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/346608/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}


### New features in [!DNL Sites] {#sites-features}
 
* The [Personalization Tab for Experience Fragments](/help/sites-cloud/authoring/fundamentals/experience-fragments.md#personalization-experience-fragment) allows segmentation specification capabilities to the Experience Fragment Editor as well as the flexibility to create nested Experience Fragments whereby headers and footers variations can be created for multiple segments. Prior to the launch of this feature, personalization offered by AEM is only available for site pages, but not for Experience Fragments

* The [Content Fragment Console](/help/sites-cloud/administering/content-fragments/content-fragments-console.md) now enables users to efficiently manage translated content fragments. A 1-click access has been provided to view all the language copies as well. Users are also able to filter the table view by the locale of their interest.

![Content Fragments Languages](/help/release-notes/assets/cfconsole-languages.png)

* Further reduce page load time for visitors by optimizing image sizes settings in templates. Find more information for the image component at [Core WCM Component](https://github.com/adobe/aem-core-wcm-components)

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] prerelease {#prerelease-features-assets}

* Experience Manager Assets now uses an improved artificial intelligence framework for image Smart Tags. This content intelligence results in better relevancy and precision of Smart Tags available to all images assets on ingestion. In addition, orientation information is populated in `cq:tags`, which enables better Search results using the Orientation filter.

   If you are interested in participating in the Beta, [fill this form](https://forms.office.com/pages/responsepage.aspx?id=Wht7-jR7h0OUrtLBeN7O4epXZrTVKKdJkUiHeolccf9UNEwyNEpHVEFaODdBNFZQSlFDREZQOVRRTy4u) by Oct 31.

* Experience Manager Assets now allows you to upload documents in other supported formats and preview them in a PDF format. The supported format types include TXT, RTF, DOC, DOCX, PPT, PPTX, XLS, and XLSX.

  ![PDF rendition for other formats](/help/release-notes/assets/multi-page-other-formats.png)


* Experience Manager Assets now supports SAS Token in addition to the Access Key for authentication while connecting to Azure Blob Storage data source.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features available in [!DNL Forms] prerelease channel {#prerelease-features-forms}

* [Adaptive Forms wizard](/help/forms/creating-adaptive-form.md): AEM Forms provides business user friendly wizard to quickly author Adaptive Forms. The wizard has a quick tab navigation to easily select pre-configured template, styling, fields, and submission options to create an adaptive form. This release brings following improvements to the wizard:

  * Select or deselect fields: The wizard allows you to create an Adaptive Form based on JSON and Form Data Model schemas. You can now select subset of fields within a schema to include in an Adaptive Form. The selected fields are converted to corresponding Adaptive Form data capture components to quickly create the desired adaptive forms.

  * Use Static Templates: Customers with existing investments in legacy static templates can continue their journey of cloud adoption by using static templates in wizard to author adaptive forms. This provides additional time to customers to migrate old static templates to modern editable templates.

* [Remove hidden fields from a Document of Record (DoR) while server-side processing](/help/forms/generate-document-of-record-for-non-xfa-based-adaptive-forms.md): You can generate the document of record PDF for end users containing only those fields which were visible to them during data capture experience. Upon form submission, the server validates which fields were hidden to the end user based on submitted data and excludes from document of record for consistency.

## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* Authors can dynamically enrich product lists with Experience Fragments (example: place banner between product listings).
* The list component now supports associated product / category pages to dynamically show related pages.
* Support for Peregrine 12.5 components was added.
* Support for client-side price loading in product teaser and carousel was added.

## [!DNL Experience Manager as a Cloud Service] Foundation {#foundation}

### What is New {#what-is-new-foundation}

* AEM as a Cloud Service (Author Service) is now integrated with Unified Shell to improve the user experience and unify it with all the other Experience Cloud applications. Additionally, with this integration the type of Cloud Service environment (Production, Stage, or Development) will be displayed as a label on the top header to easily identify the environment that you are currently logged into. Refer to AEM as a [Cloud Service on Unified Shell](/help/overview/aem-cloud-service-on-unified-shell.md) for more details.

* As previously mentioned in release notes, using the replication agent admin screen or replication API for distributing content packages larger than 10 MB (nodes with properties, not including binaries) is deprecated and will be enforced in the coming days. Please refer to [Manage Publication](/help/operations/replication.md#manage-publication) or the [Publish Content Tree workflow](/help/operations/replication.md#publish-content-tree-workflow) for the suggested approaches for replicating these large content packages.

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes-cloud-manager/release-notes-cm-current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
