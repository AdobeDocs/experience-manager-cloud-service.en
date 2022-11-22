---
title: Release Notes for 2022.1.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2022.1.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: 1c40ab67-8fd7-4f29-b8c9-dd98b6d5b490
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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2022.1.0) is February 3, 2022.
The following release (2022.3.0) is on March 31, 2022.

## Release Video {#release-video}

Have a look at the [January 2022 Release Overview](https://video.tv.adobe.com/v/340120) video for a summary of the features added in the 2022.1.0 release.

## Adobe Experience Manager Sites as a Cloud Service {#sites}

* The **[Enable Front End Pipeline](/help/sites-cloud/administering/site-creation/enable-front-end-pipeline.md)** button is available in the **Site** rail of the Sites console for sites that use the v2 of the Page Core Component. This button configures the site to load the themes that are deployed with the Front End Pipeline on top of the existing client libraries.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

* [!DNL Dynamic Media] - You can now use AEM Dynamic Media interface to configure General Settings and Publish Setup instead of having to go through the Dynamic Media Classic desktop application.

* [!DNL Dynamic Media] now supports ingestion, preview, playback and publish for MXF videos. Annotation and shoppable video for MXF videos is not yet supported.

* After configuring a connection between remote DAM and Sites deployments, the assets on remote DAM are made available on the Sites deployment. You can now perform the [update, delete, rename, and move operations](/help/assets/use-assets-across-connected-assets-instances.md) on the remote DAM assets or folders. The updates, with some delay, are available automatically on the Sites deployment.

### New features in the [!DNL Assets] prerelease channel {#assets-prerelease-features}

* [!DNL AEM Dynamic Media] now provides the flexibility to [configure one alias account](/help/assets/dynamic-media/dm-alias-account.md) in the user interface, thereby ensuring out-of-the-box Dynamic Media URLs and Viewer Embed code are updated. This positively impacts SEO, to reflect updates made to your business context, such as rebranding.

* You can now use the [!DNL Experience Manager Assets] user interface to:

  * Configure the detection of duplicate assets in a repository.

  * Configure adding digital watermarks to images.

* The administrators can now configure email service for large downloads. It allows the users to [enable email notifications for large downloads](/help/assets/download-assets-from-aem.md#enable-email-notifications-for-large-downloads) from the [!DNL Experience Manager Assets] interface. The user receives an email notification containing the download link of the archived zip folder upon completion of the download process.


* The [Manage Publication](/help/assets/manage-publication.md) feature is enhanced with an improved user interface. The users can publish or unpublish content to and from the selected destination, [Add Content](/help/assets/manage-publication.md#add-content) to the publishing list from across the DAM repository, [Include Folder Settings](/help/assets/manage-publication.md#include-folder-settings) to publish content of the selected folders and apply filters, and [schedule publishing](/help/assets/manage-publication.md#publish-assets-later) to a later date or time.

### Bug Fixes {#bug-fixes}

* Unprocessed assets with no original rendition are sent to Asset Compute for processing while migrating assets from AEM on-premise to cloud services.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### What is new in [!DNL Forms] {#what-is-new-forms}

* **[!DNL AEM Forms as a Cloud Service - Communications]**: [Communication APIs](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/using-communications/aem-forms-cloud-service-communications.html) help you combine a template and XML data to generate print documents in various formats. The service allows you to generate documents in synchronous and batch modes. The APIs enables you to create applications that let you:

  * Generate documents by populating template files with XML data.
  * Generate forms in various formats, including non-interactive PDF print streams.
  * Generate print PDFs from XFA form PDFs.
  * Generate PDF, PostScript, PCL, and ZPL documents in bulk by merging multiple sets of data with source templates.

* **Custom fonts for Document of Record and PDF documents created with Communications APIs**: You can now use brand approved fonts in PDF documents generated using Communications APIs to align with your organizational requirements.

### New features available in [!DNL Forms] prerelease channel {#prerelease-features-forms}

* **[Assembler API](https://www.adobe.io/experience-manager-forms-cloud-service-developer-reference/references/assembler-sync/)**: Assembler APIs to combine, rearrange, augment and obtain information about PDF documents.


## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* Enhanced myAccount components
* Product Recommendation component supports additional page types (home page, shopping cart, order confirmation)
* **Wishlist**
  * Logged in visitors can add products to a wishlist
  * Managing the wishlist and its products is possible via myAccount
  * The "Add to wishlist" button can be enabled / disabled on a component level via policy (example product teaser, product detail
  * Available as a Core Component and in the AEM Venia Storefront

![Wishlist](/help/assets/CIF/wishlist.png)

## Cloud Manager {#cloud-manager}

### Release Date {#release-date-cm}

The release date for Cloud Manager in AEM as a Cloud Service 2022.01.0 is 20 January 2022. The next release is planned for 10 February 2022.

### What's New {#what-is-new-cm}

* Cloud Manager will [avoid rebuilding the code base when it detects that the same git commit is used](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/setting-up-project.md#build-artifact-reuse) in multiple full-stack pipeline executions.
* Accessing the AEM environment log now requires the **Deployment Manager** product profile. Users without this profile will see a disabled button in the user interface.
*  The UI will not allow front-end pipeline configuration for a program where Sites is not enabled as a solution. 
* Upon generating a git password, the expiration date will be displayed.

### Bug Fixes {#bug-fixes-cm}

* Null pointer exceptions encountered by some front-end pipeline deployments have been corrected.
* Environment variables can now be added, updated, and deleted when an environment is running an outdated version of AEM.
* The build image step will no longer be marked as ERROR for pipelines that used the scheduled step in certain rare cases.
* For programs with only one repository, the pipeline execution screen will now display the repository name.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.8.6 is February 03, 2022.

### What's New {#what-is-new-ctt}

* Content Validation - Users have the ability to reliably determine if all of the content that was extracted by the Content Transfer Tool was successfully ingested into the target instance. To use this feature, you will need to enable it in the `System Console` of the source AEM environment. Refer to [Validating Content Transfers - Getting Started](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/validating-content-transfers.html?lang=en#getting-started) for more details.

### Bug Fixes {#bug-fixes-ctt}

* Some users were not mapped because User Mapping was case sensitive. This has been fixed. User Mapping is no longer case sensitive.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.24 is February 01, 2022.

### What's New {#what-is-new-bpa}

* Ability to detect and report on the number of assets with and without Smart Tags.
* Ability to detect and report on the version of Core Component used.
* Ability to detect and report on the type of source tier (Author or Publish) where BPA was executed.

### Bug Fixes {#bug-fixes-bpa}

* BPA sizing logic was made faster and more efficient.
* In some scenarios, BPA did not increment analyzed count when it was run. This has been fixed.
