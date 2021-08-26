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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2021.8.0) is August 26, 2021.
The following release (2021.9.0) is on September 30, 2021.

## Release Video {#release-video}

Have a look at the [August 2021 Release Overview](https://video.tv.adobe.com/v/336277) video for a summary of the features added.

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

* Automated Forms Conversion service can [convert PDF Forms in Italian and Portuguese language](https://experienceleague.adobe.com/docs/aem-forms-automated-conversion-service/using/extending-the-default-meta-model.html?#language-specific-meta-model) to Adaptive Forms.

* **Acroform-based Document of Record**: AEM Forms as a Cloud Service supports using [Adobe Acrobat Form PDF (Acroform PDF)](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/create-an-adaptive-form/generate-document-of-record-for-non-xfa-based-adaptive-forms.html) as a template for Document of Record besides XFA-based form template.

* **Microsoft Azure data store connector**: You can now [connect Form Data Model to Microsoft Azure Storage](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/use-form-data-model/configure-azure-storage.html). It allows you to retrieve and store adaptive form data to Microsoft Azure Storage as a BLOB. 

### New features available in [!DNL Forms] prerelease channel {#prerelease-features-forms}

* **Use Adobe Sign roles in an Adaptive Form**: Adobe Sign for business and enterprise service levels have the option to expand the roles for Agreement recipients, beyond just the Signer, to better match their workflow requirements. You can now enable each recipient of agreement to configure their role in an Adaptive Form, with Signer being the default role.

* **Analytics for Adaptive Forms**: You can now capture and track end user behavior via Adobe Analytics for Adaptive Forms to gather end user insights. It helps make informed decisions based on data to improve end user experience.

* **Easily connect AEM Forms with Microsoft Dynamics and Salesforce.com**: The service provides out of the box data source configuration and data models for Microsoft Dynamics and Salesforce.com, making it faster and easier for developers to configure Microsoft Dynamics and Salesforce.com as data sources for an adaptive form.

## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* New Category Picker UI for improved user experience, increased efficiency and better support for complex product catalog

  ![New Category Picker](/help/assets/CIF/category-picker.png)

* Better A11Y support for CIF Core Components

## Cloud Manager {#cloud-manager}

This section outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.8.0 and 2021.7.0.

## Release Date {#release-date-cm-aug}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.8.0 is August 12, 2021.
The next release is planned for September 09, 2021.

### What's New {#what-is-new-aug}

* Cloud Service customers can now view Service Level Agreement (SLA) reports in Cloud Manager. This will be made available progressively over the next few months.
   See [SLA Reporting](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/sla-reporting.html) to learn more.

* The type and severity of the IndexType and `IndexDamAssetLucene` quality rules has been changed. These are now both Bugs of Blocker *serverity*.

* New Oak index quality rules have been introduced to cover asynchronous and tika configurations.

* Increase max SSL certs per program to 50.

* Self-service capability to allow users to create and manage multiple repositories via Cloud Manager UI.

* SonarQube was unnecessarily reading Git history data. On large code bases, this could lead to an unnecessary build performance penalty.

* There is now an API available to invalidate the Maven dependency cache per pipeline.
 
* The version of the AEM Project Archetype used by Cloud Manager has been updated to version 29. 

### Bug Fixes {#bug-fixes-aug}

* Update Available status should not be displayed when the latest release is less than the current release.

* Initial onboarding was failing for new organizations with very long names.

* Occasionally, when a pipeline is triggered twice for some reason, it results in one of the executions failing with *cannot update pipeline execution status* error. 

## Content Transfer Tool {#content-transfer-tool}

### Release Date {#release-date-ctt-latest}

The Release Date for Content Transfer Tool v1.5.6 is August 11, 2021.

### Bug Fixes {#bug-fixes-ctt}

* In some cases not all users were migrated to the target instance. To get this fix CTT v1.5.6 is required along with aem-ethos-tools 1.2.354 or later version on the target AEM as a Cloud Service instance.

* The **Stop Ingestion** button was being disabled during ingestion to the Publish instance. This is not necessary because there is no mongo restore step during Publish ingestion. 

* CTT did not clean up the `/tmp` directory after a successful extraction. This sometimes led to disk space issues. 

