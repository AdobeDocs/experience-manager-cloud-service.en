---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
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
The following release (2021.6.0) will be on June 24, 2021.

## Release Video {#release-video}

Have a look at the [May 2021 Release Overview](https://video.tv.adobe.com/v/333602) video for a summary of the features added.

## AEM as a Cloud Service Foundation {#foundation}

### What is New in AEM as a Cloud Service Foundation {#what-is-new-foundation}

* [Prerelease Channel](/help/release-notes/prerelease.md): Preview upcoming features for a full month before they go live in production!

* [API Deprecation](/help/release-notes/deprecated-apis.md): a list of the latest deprecated APIs for AEM as a Cloud Service is available. 

* [AEM as a Cloud Service SDK Build Analyzer Maven Plugin](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/build-analyzer-maven-plugin.html):  Update your maven projects to the latest version, which includes a deprecated Java API check and other improvements. 

## [!DNL Adobe Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### What is new in [!DNL Sites] {#what-is-new-sites}

* You will soon be able to verify content on a new [Preview tier](/help/sites-cloud/authoring/fundamentals/previewing-content.md) to simulate the final experience look and feel as you would on the Publish tier. This is enabled by the AEM Sites Managed Publication wizard which is now allowing you to choose a publish destination between Publish or Preview. Experiences on Preview can then be accessed via a dedicated URL. After validation on Preview, content can be published from Author to Publish as usual. Enabling the Preview Service in AEM as a Cloud Service environments will be gradually rolled out in the next few weeks.

## [!DNL Adobe Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features available in the prerelease channel {#what-is-new-assets-prerelease}

* Metadata schemas can be applied directly to the folder properties.

  ![Add metadata schema from folder properties](/help/assets/assets/metadata-schema-folder-properties.png)

* The Asset Bulk Ingestor tool lets you add metadata during a bulk ingestion.

* A user experience enhancements displays the number of assets present in a folder. For more than 1000 assets in a folder, [!DNL Assets] displays 1000+.

  ![Number of assets in a folder are displayed on the interface](/help/assets/assets/browse-folder-number-of-assets.png)

### Bugs fixed in [!DNL Assets] {#assets-bugs-fixed}

* Uploading very large files crashes the [!DNL Experience Manager desktop app]. (CQ-4320942)
* The toolbar options are different when the same Collection is selected from within a folder and when it is selected from a search result. (CQ-4321406)

#### What is new in [!DNL Dynamic Media] {#what-is-new-dm}

* Smart Imaging Device Pixel Ratio (DPR) and network bandwidth optimization let you deliver best quality images efficiently, on devices with high resolution displays and constrained network bandwidth. See [smart imaging FAQs](/help/assets/dynamic-media/imaging-faq.md).

   >[!NOTE]
   >
   >The release timeline for the above Smart Imaging enhancements is:
   >
   >* North America May 24, 2021 in NA,
   >
   >* Europe, the Middle East and Africa June 25, 2021,
   >
   >* Asia-Pacific July 19, 2021.

* Introduced support for next-gen image format AVIF in [!DNL Dynamic Media] delivery (fmt URL modifier).

  >[!NOTE]
  >
  >The release timeline for AVIF support is:
  >
  >* North America May 10, 2021,
  >
  >* Europe, the Middle East and Africa May 24, 2021,
  >
  >* Asia-Pacific June 24, 2021.

## [!DNL Adobe Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### What is new in [!DNL Forms] {#what-is-new-forms}

* **Contextual help**: Added contextual help for adaptive forms editor, template editor, and theme editor to help authors better understand various features of editors.
* **Error messages in Properties browser**: Added error messages for each property in the Adaptive Forms Properties browser. These messages help understand allowed values for a field.

### Upcoming beta feature of [!DNL Forms] {#what-is-new-forms-prerelease}

Output as a Cloud service: Output service helps you combine XDP templates and XML data to generate print documents in various formats. The service allows you to generate documents in synchronous and asynchronous batch mode. Output service enables you to create applications that let you:

* Generate final form documents by populating template files with XML data.
* Generate output forms in various formats, including non-interactive PDF print streams.
* Generate print PDFs from XFA form PDFs.

You can write to formscsbeta@adobe.com to sign up for the beta program.

### Bugs fixed in [!DNL Forms] {#forms-bugs-fixed}

* In an Assign Task step of AEM Forms Workflows, when you replace the default icon of the action buttons with a coral icon, the workflow stops working and logs an exception. The workflow performs as expected when default icons are used.
* In the layout layer, when you change the number of columns, open the edit layer, and drag some components in a panel, square blue boxes start appearing in the content area of the adaptive forms editor and the editor becomes unresponsive.
* Error message of a rule editor option related to providing URL of an adaptive or an external asset is too long and is not user friendly.

## Cloud Manager {#cloud-manager}

This section outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.6.0 and 2021.5.0.

## Release Date {#release-date-june-cm}

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


### Release Date {#release-date-cm-may}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.5.0 is May 06, 2021.

### What's New {#what-is-new-may}

* The PackageOverlaps quality rule now detects cases where the same package was deployed multiple times, i.e. in multiple embedded locations, in the same deployed package set.

* The repository endpoint in the Public API now includes the Git URL.

* Deployment log downloaded by a Cloud Manager user will be more insightful and will now include details about failures and success scenarios.

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

* New logging statement was added to the quickstart's error log, if the user doesn't have execute permission on the Java executable.

* When a user deletes a migration set from the CTT UI, where an extraction was performed, the `tmp` folder associated with that migration set will be deleted to save space.

### Bug Fixes {#bug-fixes-ctt-latest}

* When deleting a migration set, occasionally an unhelpful error message would appear in the CTT UI. This has been fixed.

* While running User Mapping, if users had the same email address on the target and the host but different user names, the entire ingestion would fail. This has been fixed. In such a conflicting scenario, the user/group is skipped and is logged as a conflict in the log file.   

### Release Date {#release-date-ctt-may}

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
