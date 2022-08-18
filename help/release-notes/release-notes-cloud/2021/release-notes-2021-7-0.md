---
title: Release Notes for 2021.7.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2021.7.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: 848f6a29-2e0f-4976-8ed7-6b7f69408c1b
---
# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions; for example, for those in 2020, 2021 and so on.

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2021.7.0) is July 29, 2021.
The following release (2021.8.0) is on August 26, 2021.

## Release Video {#release-video}

Have a look at the [July 2021 Release Overview](https://video.tv.adobe.com/v/335580) video for a summary of the features added.

## Experience Manager Foundation as a Cloud Service {#foundation}

### What's New {#what-is-new-foundation}

* More flexible dispatcher configuration: Projects can be more easily organized. For example, you can now include multiple rewrite rule files that reflect your site structure. [Learn about](/help/implementing/dispatcher/disp-overview.md#validation-debug) this flexible mode, including how to structure your dispatcher configuration in order to take advantage of it.
* The tree replication UI under the replication agent's "Distribute" tab should be considered deprecated and is planned to be removed after September 30. [Learn about](/help/operations/replication.md#tree-activation) alternative replication strategies.
* Bundle `org.apache.sling.datasource-1.0.4.jar` for Sling datasource support has been removed, as it has outdated functionality and is not in use by customers.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

* Content Automation functionality lets [!DNL Experience Manager Assets] leverage the [!DNL Adobe Creative Cloud] APIs to automate asset production at scale. It improves content velocity by dramatically decreasing the time taken and iterations required to create variations of the same asset. The functionality does not require any programming and works from within the DAM. See [generate variations of assets using Creative Cloud integration](/help/assets/cc-api-integration.md).

* [!DNL Experience Manager Assets] includes the [!DNL Document Cloud] PDF Viewer to preview PDF documents natively. This feature lets users preview multi-page PDF files without any file processing or conversion. This feature improves the parity with [!DNL Experience Manager] 6.5. The controls available in the viewer include zoom, navigate to pages, undock controls, and to view in full screen. Users case also preview and jump to pages and bookmarks. Comments on the file itself are supported and commenting and annotations on content within the PDF file will be added in a future release.

  ![Preview PDF files in [!DNL Experience Manager] using PDF Viewer](/help/assets/assets/preview-pdf-file-viewer.png)

* The Linkshare download functionality uses asynchronous downloads that boost the download speed. See [Download assets shared using link sharing](/help/assets/download-assets-from-aem.md#link-share-download).

   ![Download inbox](/help/assets/assets/download-inbox.png)

* The view settings are enhanced to let users choose a default view and a default sorting parameter.

  ![Set default view in [!UICONTROL View Settings]](/help/assets/assets/view-settings-for-defaults.png)

* Users can search and filter the folders based on property predicates.

  ![Filter search folders using search predicates](/help/assets/assets/search-folders-via-predicates.png)

### New features available in the [!DNL Assets] prerelease channel {#assets-prerelease-features}

<!-- TBD: Not sure about GA of these enh. Shall check with the team.

* A user experience enhancements displays the number of assets present in a folder. For more than 1000 assets in a folder, [!DNL Assets] displays 1000+.

  ![Number of assets in a folder are displayed on the interface](/help/assets/assets/browse-folder-number-of-assets.png)

* You can directly apply a metadata schemas to a folder in its [!UICONTROL Properties].

  ![Add metadata schema from folder properties](/help/assets/assets/metadata-schema-folder-properties.png)
-->

* When you share digital assets as a link, users can copy the URL to clipboard. The enhancement lets you share assets in a faster and more convenient way.

### Bugs fixed in [!DNL Assets] {#assets-bugs-fixed}

The API `com.day.cq.dam.api.collection.SmartCollection` is not available in [!DNL Experience Manager] as a [!DNL Cloud Service]. (CQ-4326322)

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### What is new in [!DNL Forms] {#what-is-new-forms}

* You can now use Automated Forms Conversion service to [convert PDF Forms in French, German, and Spanish language](https://experienceleague.adobe.com/docs/aem-forms-automated-conversion-service/using/extending-the-default-meta-model.html?#language-specific-meta-model) to adaptive forms.
* Added a separate panel to template editor to display errors related to adaptive form components. It helps consolidate all adaptive form errors at one location and reduce resolution time.

### New features available in [!DNL Forms] prerelease channel {#beta-features-forms}

* **[!DNL AEM Forms as a Cloud Service - Communications]**: [Communication APIs](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/aem-forms-cloud-service-communications.html) help you combine XDP templates and XML data to generate print documents in various formats. The service allows you to generate documents in synchronous mode. The APIs enables you to create applications that let you:
  * Generate documents by populating template files with XML data.
  * Generate output forms in various formats, including non-interactive PDF print streams.
  * Generate print PDF files from an XFA form PDF and Adobe Acrobat Form.

* **Variable Data Externalizer**: You can save data of AEM Workflow variables on an external storage system managed by your organization.

* **Acroform-based Document of Record**: You can also [use Adobe Acrobat Form PDF (Acroform PDF)](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/create-an-adaptive-form/generate-document-of-record-for-non-xfa-based-adaptive-forms.html) as a template for Document of Record besides XFA-based form template.

* **Microsoft Azure data store connector**: You can now [connect Form Data Model to Microsoft Azure Storage](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/use-form-data-model/configure-azure-storage.html). It allows you to retrieve and store adaptive form data to Microsoft Azure Storage as a BLOB.  

## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* CIF Core Components v2
  * Simplified and improved configurations for PDP/PLP URL and SEO
  * Visual indicator for staged product data in authoring mode for better visibility of upcoming changes
  * New sitemap component for content and commerce pages

* Support for [Adobe Commerce Sensei Product Recommendation, powered by Adobe Sensei](https://business.adobe.com/products/magento/product-recommendations.html) in AEM Storefront using pre-defined or on-the-fly created recommendations

## [!DNL Experience Manager Screens] as a [!DNL Cloud Service] {#screens}

### Bug Fixes {#bug-fixes-screens}

* Content Provider settings are now validated during create or update.

* All displays views have folders column.

* You can expand Screens Content Structure.

* `bulk-offline-update-service` was missing all permissions for some environments.

* Updated Help link to match the new screens cloud documentation.

* Un-assign playlists and disallow removing playlist(s) with player(s) assigned, now works.

* Player now re-downloads Assets when "ALL" Cache is cleared.

* Repeat Scheduling now works, if the *End Time* is set for following day.

* `Back&Forward` now works in Screens as  a Cloud Service UI.

* Tags with same name but different namespaces could not be created earlier.

## XML Documentation for Experience Manager as a Cloud Service {#xml-documentation}
 
### What is New {#what-is-new-xml-documentation}
 
XML Documentation for Experience Manager as a Cloud Service is generally available. It allows Experience Manager as a Cloud Service customers to procure XML Documentation addon to import, create, manage, and deliver technical content across multiple channels including Experience Manager Sites.

## Cloud Manager {#cloud-manager}

This section outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.7.0.

### Release Date {#release-cm-july}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.7.0 is July 15, 2021.
The next release is planned for August 12, 2021.

### What's New {#what-is-new-cm-july}

* Customers are now able to use Azul 8 and 11 JDKs for their Cloud Manager build processes and can either select to use one of these JDKs for toolchains-compatible Maven plugins *or* the entire Maven process execution.

* The outbound egress IP will now be logged in the build step log file. 

* Stage and Production environments running old versions of AEM will now report a status of **Update Available**. 

* The maximum SSL certificates supported has increased to 20 per program.

* The maximum number of domains that can be configured has increased to 500 per environment.

* The **Manage Git** buttons has been retitled to **Access Git Info** and the dialog has been visually refreshed.

* The version of the AEM Project Archetype used by Cloud Manager has been updated to version 28.

### Bug Fixes {#bug-fixes-cm-july}

* In some situations, Preview was not an available option when binding an IP Allow List to an environment.

* Manually navigating to the execution details page for a non-existing execution did not show an error, just an endless loading screen.

* The error message shown when the maximum number of SSL certificates was reached was not helpful.

* In some circumstances, there could be a discrepancy in the release version shown in the pipeline card on the **Overview** page.

* Add program wizard incorrectly stated that name cannot be changed after creation. 

### Known Issues {#known-issues-cm-july}

Customers switching to use the Azul JDKs should be aware that not all existing applications will compile without error on Azul JDK. It is highly recommended to test locally before switching.

## Cloud Acceleration Manager {#cam}

### Release Date {#release-date-july-cam}

The Release Date for Cloud Acceleration Manager is July 15, 2021.
 
### What is New {#what-is-new-cam}

Cloud Acceleration Manager is a cloud-based application designed to guide your IT teams throughout the transition journey starting from planning to going live on Cloud Service. Set up your teams for a successful migration with Adobe-recommended best practices, tips, documentation, and tools to help at every phase of the journey to AEM as Cloud Service. Learn more [here](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-acceleration-manager/using-cam/getting-started-cam.html?lang=en).

>[!NOTE]
>
> Check this [Cloud Acceleration Manager demo video](https://video.tv.adobe.com/v/335547).
