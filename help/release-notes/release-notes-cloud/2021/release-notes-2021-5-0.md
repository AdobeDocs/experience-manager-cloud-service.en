---
title: Release Notes for 2021.5.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2021.5.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: 3f9d7339-7e37-4702-821e-f2b03cd7e224
feature: Release Information
role: Admin
---
# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>From here, you can navigate to release notes of previous versions; for example, for those in 2020, 2021 and so on.

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2021.5.0 is May 27, 2021.
The following release (2021.6.0) will be on June 28, 2021.

## AEM as a Cloud Service Foundation {#foundation}

### What is New in AEM as a Cloud Service Foundation {#what-is-new-foundation}

* [Prerelease Channel](/help/release-notes/prerelease.md): Preview upcoming features for a full month before they go live in production!

* [API Deprecation](/help/release-notes/deprecated-removed-features.md): a list of the latest deprecated APIs for AEM as a Cloud Service is available. 

* [AEM as a Cloud Service SDK Build Analyzer Maven Plugin](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/build-analyzer-maven-plugin.html):  Update your maven projects to the latest version, which includes a deprecated Java API check and other improvements. 

## [!DNL Adobe Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### What is new in [!DNL Sites] {#what-is-new-sites}

* You will soon be able to verify content on a new [Preview tier](/help/sites-cloud/authoring/sites-console/previewing-content.md) to simulate the final experience look and feel as you would on the Publish tier. This is enabled by the AEM Sites Managed Publication wizard which is now allowing you to choose a publish destination between Publish or Preview. Experiences on Preview can then be accessed via a dedicated URL. After validation on Preview, content can be published from Author to Publish as usual. Enabling the Preview Service in AEM as a Cloud Service environments will be gradually rolled out in the next few weeks.

## [!DNL Adobe Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### What is new in [!DNL Assets] {#what-is-new-assets}

* You can download the assets shared using the Link Share functionality. This download now uses an asynchronous service that offers faster and uninterrupted downloads, even for very large downloads. See [download assets](/help/assets/download-assets-from-aem.md#link-share-download).

  ![Download inbox](/help/assets/assets/download-inbox.png)

### New features available in the prerelease channel {#what-is-new-assets-prerelease}

* Metadata schemas can be applied directly to the folder properties.

  ![Add metadata schema from folder properties](/help/assets/assets/metadata-schema-folder-properties.png)

* The Asset Bulk Ingestor tool lets you add metadata during a bulk ingestion.

* A user experience enhancements displays the number of assets present in a folder. For more than 1000 assets in a folder, [!DNL Assets] displays 1000+.

  ![Number of assets in a folder are displayed on the interface](/help/assets/assets/browse-folder-number-of-assets.png)

### Bugs fixed in [!DNL Assets] {#assets-bugs-fixed}

* Uploading very large files crashes the [!DNL Experience Manager desktop app]. (CQ-4320942)
* The toolbar options are different when the same Collection is selected from within a folder and when it is selected from a search result. (CQ-4321406)

#### What is new in Dynamic Media {#what-is-new-dm}

* Smart Imaging DPR (Device Pixel Ratio) and network bandwidth optimization enables you to deliver best quality images efficiently, on devices with high resolution displays and constrained network bandwidth. For more information, see [Smart imaging FAQs](/help/assets/dynamic-media/imaging-faq.md) and [Image optimization with next generation image formats WebP and AVIF](https://medium.com/adobetech/image-optimisation-with-next-gen-image-formats-webp-and-avif-248c75afacc4).
* Introduced support for next generation image format AVIF in Dynamic Media delivery (fmt URL modifier).

## [!DNL Adobe Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### What is new in [!DNL Forms] {#what-is-new-forms}

* **Contextual help**: Added contextual help for adaptive forms editor, template editor, and theme editor to help authors better understand various features of editors.
* **Error messages in Properties browser**: Added error messages for each property in the Adaptive Forms Properties browser. These messages help understand allowed values for a field.

### Upcoming beta feature of [!DNL Forms] {#what-is-new-forms-prerelease}

Output as a Cloud service: Output service helps you combine XDP templates and XML data to generate print documents in various formats. The service lets you generate documents in synchronous and asynchronous batch mode. Output service enables you to create applications that let you:

* Generate final form documents by populating template files with XML data.
* Generate output forms in various formats, including non-interactive PDF print streams.
* Generate print PDFs from XFA form PDFs.

You can write to formscsbeta@adobe.com to sign up for the beta program.

### Bugs fixed in [!DNL Forms] {#forms-bugs-fixed}

* In an Assign Task step of AEM Forms Workflows, when you replace the default icon of the action buttons with a coral icon, the workflow stops working and logs an exception. The workflow performs as expected when default icons are used.
* In the layout layer, when you change the number of columns, open the edit layer, and drag some components in a panel, square blue boxes start appearing in the content area of the adaptive forms editor and the editor becomes unresponsive.
* Error message of a rule editor option related to providing URL of an adaptive or an external asset is too long and is not user friendly.


## Cloud Manager {#cloud-manager}

This section outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.5.0.

### Release Date {#release-date-cm-may}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.5.0 is May 06, 2021.
The next release is planned for June 03, 2021.

### What's New {#what-is-new-may}

* The PackageOverlaps quality rule now detects cases where the same package was deployed multiple times, that is, in multiple embedded locations, in the same deployed package set.

* The repository endpoint in the Public API now includes the Git URL.

* Deployment log downloaded by a Cloud Manager user are more insightful and include details about failures and success scenarios.

* Intermittent failures encountered while pushing code to Adobe git have now been resolved.

* Commerce add-on can now be applied to Sandbox programs during the Edit program workflow.

* The Edit program experience has been refreshed. 

* The Domain Names table in the Environment Details page will display up to 250 Domain names via pagination. 

* The Solutions tab in Add Program and Edit Program workflows will display the solution, even if only one solution is available for the Program.

* The error message in the build step log when the build did not produce any deployed content packages was unclear.

### Bug Fixes {#bug-fixes-cm-may}

* On occasion, user may see a green "active" status next to an IP Allow List even when that configuration was not deployed. 

* Instead of removing 'deleted' variables, the pipelines variables API would only mark them with status **DELETED**. 

* Some Code Smell-type quality issues were incorrectly impacting the Reliability Rating.

* Since wildcard domains are not supported, the UI will disallow the user from submitting a wildcard domain.

* When a pipeline execution was started between midnight and 1am UTC the artifact version generated by Cloud Manager was not guaranteed to be greater than a version created the prior day.

* During Sandbox program setup, once the project with sample code has been successfully created, Manage Git will appear as a link from the hero card in the Overview page. 

## Content Transfer Tool {#content-transfer-tool}

### Release Date {#release-date-ctt-latest}

The Release Date for Content Transfer Tool v1.4.6 is May 27, 2021.

### What's New {#what-is-new-ctt-latest}

* New logging statement was added to the quickstart's error log, if the user does not have run permission on the Java executable.

* When a user deletes a migration set from the CTT user interface, where an extraction was performed, the `tmp` folder associated with that migration set is deleted to save space.

### Bug Fixes {#bug-fixes-ctt-latest}

* When deleting a migration set, occasionally an unhelpful error message would appear in the CTT UI. This has been fixed.

* While running User Mapping, if users had the same email address on the target and the host but different user names, the entire ingestion would fail. This has been fixed. In such a conflicting scenario, the user/group is skipped and is logged as a conflict in the log file. 

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.4.0 is May 11, 2021.

### What's New {#what-is-new-ctt-may}

* This version of the Content Transfer Tool creates text renditions for assets being migrated to Cloud Service. Text renditions are required to support full text search on ingested assets.
* The maximum number of Content Transfer Tool migration sets a user can create has been increased from 4 to 10. 

### Bug Fixes {#bug-fixes-ctt-may}

* Multiple bug fixes related to the auto-refresh feature in the Content Transfer Tool UI.
* Content Transfer Tool with `wipe=true` resulted in incorrect counter index on the target. This has been fixed.

## Commerce Add-on {#cloud-services-commerce}

### What is New {#what-is-new-commerce}

* Pagination support for associated content in product console properties

### Bug Fixes {#bug-fixes-commerce}

* Asset thumbnails not displayed in Asset tab of product properties

* Breadcrumb resets preview data in product console
