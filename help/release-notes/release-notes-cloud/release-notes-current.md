---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
mini-toc-levels: 1
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
mini-toc-levels: 1
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

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2021.6.0 is June 28, 2021.
The following release (2021.7.0) will be on July 29, 2021.

## Release Video {#release-video}

Have a look at the [June 2021 Release Overview](https://video.tv.adobe.com/v/334296) video for a summary of the features added.

## XML Documentation for AEM as a cloud Service {#xml-documentation}
 
### What's New {#what-is-new-xml-documentation}
 
* XML Documentation for AEM as a Cloud Service is now GA.
* This will allow existing AEM Cloud Service customers to procure XML Documentation addon for importing, creating, managing and delivering technical content across multiple channels including AEM sites

## Cloud Manager {#cloud-manager}

This section outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.6.0 and 2021.5.0.

### Release Date {#release-date-june-cm}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.6.0 is June 10, 2021.
The next release is planned for July 15, 2021.

### What's New {#what-is-new-junecm}

* Preview Service will be deployed on a rolling basis to all Programs. Customers will be notified in-product when their Program is enabled for Preview Service. Refer to [Accessing Preview Service](/help/implementing/cloud-manager/manage-environments.md#access-preview-service) for more details.

* Maven Dependencies downloaded during the build step will now be cached between pipeline executions. This feature will be enabled for customers over the next several weeks.

* The name of the program can now be edited through the edit program dialog.

* The default branch name used during both project creation and  in the default push command via manage git workflows has been changed to `main`.

* Edit program experience in the UI has been refreshed.

* The quality rule `ImmutableMutableMixCheck` has been updated to classify `/oak:index` nodes as being immutable. 

* The quality rules `CQBP-84` and `CQBP-84--dependencies` have been consolidated into a single rule. As part of this consolidation, the scanning of dependencies more accurately identifies issues in third party dependencies which are being deployed to the AEM runtime.

* To avoid confusion, the Publish AEM and Publish Dispatcher segment rows on the Environment Details page have been consolidated.

   ![](/help/onboarding/release-notes-cloud-manager/assets/aem-dispatcher.png)

* A new code quality rule has been added to validate the structure of `damAssetLucene` indexes. Refer to [Custom DAM Asset Lucene Oak Indexes](/help/implementing/cloud-manager/custom-code-quality-rules.md#oakpal-damAssetLucene-sanity-check) for more details.

* Environment details page will now display multiple domain names for Publish and Preview services (as applicable). Refer to [Environment Details](/help/implementing/cloud-manager/manage-environments.md#viewing-environment) to more details.

### Bug Fixes {#bug-fixes-junecm}

* JCR node definitions containing a newline after the root element name were not correctly parsed.

* List repositories API would not filter deleted repositories.

* An incorrect error message was displayed when an invalid value was provided for the schedule step.

* On occasion, user may see a green *active* status next to an IP Allow List even when that configuration was not deployed.

* Some program editing sequences could result in the inability to create or edit the production pipeline.

* Some program editing sequences could result in the **Overview** page displaying a misleading message to re-execute program setup.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#ga-features-assets}

* Content Automation functionality lets [!DNL Experience Manager Assets] leverage the [!DNL Adobe Creative Cloud] APIs to automate asset production at scale. It improves content velocity by dramatically decreasing the time taken and iterations required to create variations of same asset. The functionality does not require any code and works from within the DAM.
* [!DNL Adobe Asset Link] v3.0 for [!DNL Adobe Photoshop], [!DNL Adobe Illustrator], and [!DNL Adobe InDesign] and [!DNL Adobe Asset Link] v2.0 for [!DNL Adobe XD] is released. It provides:

  * Support for [!DNL Assets Essentials].
  * Ability to automatically connect to [!DNL Experience Manager] as a [!DNL Cloud Service] or [!DNL Assets Essentials].

<!-- TBD: Checking with PMs if AAE release should be mentioned here.
-->

### New features available in the [!DNL Assets] prerelease channel {#beta-features-assets}

* The view settings are enhanced to let users choose a default view and a default sorting parameter.
* The Linkshare download functionality uses asynchronous downloads that boosts the download speed.
* Users can search and filter the folders based on property predicates.
* [!DNL Experience Manager Assets] embeds the the PDF Viewer powered by [!DNL Adobe Document Cloud] to preview the supported documents. This feature lets users preview PDF and other multi-page files without any complex processing. This improves the feature parity with [!DNL Experience Manager] 6.5.

### Bugs fixed in [!DNL Assets] {#bugs-fixed-assets}

* When you add an owner to a sub-folder, [!DNL Assets] also adds the same user as an owner of the parent folder. (CQ-4323737)
* When adding assets to Collections, if a user applies a filter on Collections search, the user cannot view the Collections in List view. (CQ-4323181)
* When searching for files and folders, if user applies a filter and selects [!UICONTROL Files & Folders], only the files are displayed but not the folder. (CQ-4319543)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in [!DNL Sites] {#ga-features-sites}

* Publish to Preview Tier now shown as page status in Sites Admin UI
* Publish to Preview Tier now surfacing preview URL at the end of the action and persisting the URL in page properties for later reference

## [!DNL Adobe Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features in [!DNL Forms] {#what-is-new-forms}

* Forms administrators can filter custom columns in AEM Inbox.
* Forms developers can use the theme editor and style layer of adaptive form editor to style the captcha component.
* Improved accuracy for automatically detecting logical sections in the source forms and converting those into corresponding adaptive form panels.
* Added move action to help shift a PDF or XDP file from one folder to another.
* Reduced load time and improved performance of adaptive forms editor and theme editor.

### Beta feature of [!DNL Forms]  {#what-is-new-forms-prerelease}

* **[!DNL AEM Forms as a Cloud Service - Communications]**: Communication APIs helps you combine XDP templates and XML data to generate print documents in various formats. The service allows you to generate documents in synchronous mode. The APIs enables you to create applications that let you:
  * Generate documents by populating template files with XML data.
  * Generate output forms in various formats, including non-interactive PDF print streams.
  * Generate print PDFs from an XFA form PDF and Adobe Acrobat Form (AcroForm).

You can write to [!DNL formscsbeta@adobe.com] to sign up for the beta program.

### Bugs fixed in [!DNL Forms] {#forms-bugs-fixed}

* When a field is validated before submitting data to backend service via Form Data Model (FDM), validations succeed but the Form Data Model service fail to invoke post validation.
* When you submit a form containing a standard HTML upload field from an Apple iOS device, sometimes, the content of the file is not sent and a 0-byte file is received at the other end. [FB9117687](https://feedbackassistant.apple.com/feedback/9117687)

## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* New CIF product and category reference data types for Content Fragments (Incl. product / category picker UI support)
* New Commerce Content Fragment Core Component
* Full-text commerce search supported in AEM backend
* Commerce Core Components support Adobe Commerce Sensei Recs data collection
* Improved SEO-friendly URLs for category pages
* Support for custom HTTP headers per site/config


