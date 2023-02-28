---
title: Release Notes for 2021.9.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2021.9.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: 8c12ff09-fbc8-42dd-87c0-46e509604f36
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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2021.9.0) is October 6, 2021.
The following release (2021.10.0) is on November 4, 2021.

## Release Video {#release-video}

Have a look at the [September 2021 Release Overview](https://video.tv.adobe.com/v/337381) video for a summary of the features added.

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New feature in the [!DNL Sites] prerelease channel {#sites-prerelease-features}

* Content Fragment models are now automatically set in read-only state once they are published, to avoid unintentially breaking live API queries after re-publishing an edited model. Users are prompted with a warning when attempting to edit a published model. Editing is possible upon accepting the warning. 

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

* Users can now sort the assets displayed in the search results in Column and Card views. The sorting works on Name, Created, Modified, or None columns.

  ![Sort the search results in [!DNL Assets] in Column and Card views](/help/assets/assets/sort-searched-assets.png)
  *Figure: Sort the search results in [!DNL Assets] in Column and Card views.*

* To programmatically invoke processing using asset microservices, a new API is introduced. Developers can now apply an existing folder-level processing profile on one or more specific assets in a folder. The processing profile gets applied based on custom metadata properties updates. See `AssetProcessor` in the [[!DNL Experience Manager] API reference](https://www.adobe.io/experience-manager/reference-materials/). As before, it is possible to [use asset microservices from the user interface](/help/assets/asset-microservices-configure-and-use.md).

<!-- Leave this commented.

### New feature in the [!DNL Assets] prerelease channel {#assets-prerelease-features}

Apparently, no new Assets features in Sep beta channel.
A/V transcription feature via CQ-4303854 has moved to Oct beta now.

### Bugs fixed in [!DNL Assets] {#assets-bugs-fixed}

No customer-reported bugs fixed in Sep release.
CQ-4328183 was not reported on CS so not documented here.
-->

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### What is new in [!DNL Forms] {#what-is-new-forms-sep-2021}

* **Use Adobe Sign roles in an Adaptive Form**: Adobe Sign for business and enterprise service levels have the option to expand the roles for Agreement recipients, beyond just the Signer, to better match their workflow requirements. You can now [enable each recipient of agreement to configure their role in an Adaptive Form](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/create-an-adaptive-form/use-adobe-sign/working-with-adobe-sign.html#addsignerstoanadaptiveform), with Signer being the default role.

* **Analytics for Adaptive Forms**: You can now capture and track end user behavior via Adobe Analytics for Adaptive Forms to gather end user insights. It helps make informed decisions based on data to improve end user experience.

* **Easily connect AEM Forms with Microsoft Dynamics and Salesforce**: The service provides out of the box data source configuration and data models for Microsoft Dynamics and Salesforce, making it [faster and easier for developers to configure Microsoft Dynamics and Salesforce as data sources for an adaptive form](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/use-form-data-model/configure-msdynamics-salesforce.html?lang=en).

* **E-Sign an adaptive form using DocuSign:** You can use DocuSign to e-sign an adaptive form. The service provides a custom submit action to use DocuSign with an adaptive form. You can install the package available on Software Distribution to import the submit action.

### Beta features of [!DNL Forms]  {#sep-what-is-new-forms-prerelease}

* **Unified Storage Connector:** Use Unified Storage Connector to externalize in-process data in customer-managed repositories. For example, you can
  * Enable Forms Portal’s save and resume functionality and store adaptive forms drafts in a customer-managed data repository. 
  * Store in-process AEM Workflows data (AEM Workflow Variables data) that contains Sensitive Personal Data (SPD) in a customer-managed repository.  

* **[!DNL AEM Forms as a Cloud Service - Communications]**: [Communication APIs](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/using-communications/aem-forms-cloud-service-communications.html) help you combine XDP templates and XML data to generate print documents in various formats. The service allows you to generate documents in synchronous mode. The APIs enables you to create applications that let you:
  * Generate documents by populating template files with XML data.
  * Generate output forms in various formats, including non-interactive PDF print streams.
  * Generate print PDF files from an XFA form PDF and Adobe Acrobat Form.

You can write to [!DNL formscsbeta@adobe.com] to sign up for the beta program.

## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* New "associated commerce content" tab in Sites editor increases author efficiency by quickly getting access to relevant AEM  product content for the current context

  ![Associated commerce content](/help/assets/CIF/associated-commerce-content.png)

* Improved product picker UI for better user experience, increased efficiency and support for complex product catalog

  ![New Product Picker](/help/assets/CIF/product-picker.png)

* Respect "include_in_menu" property in navigation component

### Bug Fixes {#bug-fixes-cif}

* Menu cache flush is not working as expected

* JS errors during AEM CS deployment step and when not using clientside components

* Cannot create CIF cloud config in folders that have a sling:configs node

## [!DNL Experience Manager Screens] as a [!DNL Cloud Service] {#screens} 

### What is New {#what-is-new-screens}

* Screens as a Cloud Service now supports basic playback monitoring. The player will now report various playback metrics with each ping (defaults to 30 seconds). Based on the metrics, it provides the ability to detect various edge cases (stuck experience, blank screen, scheduling problem, etc.). This feature allows the team to remotely monitor if a player is properly playing content, improves reactivity to blank screens or broken experiences in the field, and decreases the risk of showing a broken experience to the end user.
   See [Basic Playback Monitoring](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/screens-as-cloud-service/manage-player-registration/installing-screens-cloud-player.html?lang=en#playback-monitoring) for more details.

* Thumbnail Support for videos in now supported in Screens as a Cloud Service. A content author can define a thumbnail for videos so that the image can be used as a placeholder and properly test content playback and targeting, while the actual video is being finalized by the appropriate team. The image can also be used, in case the playback of the video fails.
   See [Thumbnail Support for Videos](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/screens-as-cloud-service/core-product-features/thumbnail-support-videos.html) for more details.

### Bug Fixes {#bug-fixes-screens}

* Player could not show content from Embedded page and this issue is now fixed.

* After a successful login, navigating to the default page (channels) ended up in a Internal Server Error page.

* Associated tag entries were not removed when removing playlist(s).

## [!DNL Experience Manager as a Cloud Service] Foundation {#foundation}

### New features in [!DNL Experience Manager as a Cloud Service] {#foundation-features}

**Advanced Networking**

>[!INFO]
>
>The advanced networking feature is part of the 2021.9.0 release, and will be enabled for customers in mid-October.

[!DNL Adobe Experience Manager] as a [!DNL Cloud Service] now offers several types of advanced networking capabilities, including:

* Flexible Port egress to egress traffic out of non-standard ports. Now possible without contacting Adobe Support.
* Dedicated egress IP address to egress traffic out of AEM as a Cloud Service from a unique IP, now supporting all ports.
* VPN to secure traffic between your infrastructure and AEM as a Cloud Service.

Read the [documentation](/help/security/configuring-advanced-networking.md) for more information, including how to self serve provision advanced networking using Cloud Manager APIs. 

**Index Optimizations**

To improve the performance of search queries and indexing, the full-text index lucene-2 is no longer used out-of-the-box in [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] from this release. In order to remove this full-text index on AEM environments in accordance with AEM customers, Adobe Engineering works individually and pro-actively with customers for a gentle and sustainable removal of the Lucene full-text index. Please visit the [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] [documentation](/help/operations/indexing.md#index-optimizations) for more information and contact our support directly if you have any questions.

## Cloud Manager {#cloud-manager}

This section outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.9.0 and 2021.8.0.

## Release Date {#release-date-cm-sept}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.9.0 is September 09, 2021.
The next release is planned for October 07, 2021.

### What's New {#what-is-new-cm-sept}

* The version of the AEM Project Archetype used by Cloud Manager has been updated to version 30.

* The program cards on Cloud Manager landing page and the associated experience has been refreshed.

* The Code Quality Step Log now includes verbose logging information on the OakPal scanning process.

* The Activity page menu options will now include an option to **Download Log** for completed Code Generator executions. Selecting this will download the log of the build step.

* Clicking directly on the Program card will now navigate to Cloud Manager Overview page.

### Bug Fixes {#bug-fixes-sept}

* User will now see a more comprehensible message when trying to add a new IP Allow List in a program that has reached the maximum allowed number of IP Allow Lists that can be configured.

* Wrong URL was copied when selecting the copy URL menu option from Repositories screen. 

## Cloud Acceleration Manager {#cam}

### Release Date {#release-date-october-cam}

The Release Date for Cloud Acceleration Manager is October 04, 2021.
 
### What is New {#what-is-new-cam}

* Cloud Acceleration Manager now provides users with the ability to view the BPA reports in a printable preview, allowing simple printing or printing to PDF for easy shareability. Refer to Step 6 and 7 in [Using Best Practices Analysis Card](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-acceleration-manager/using-cam/cam-readiness-phase.html?lang=en#best-practices-analysis).

## Content Transfer Tool {#content-transfer-tool}

### Release Date {#release-date-ctt-latest}

The Release Date for Content Transfer Tool v1.6.0 is October 04, 2021.

### What's New {#what-is-new-ctt}

* Improved User Mapping with a simplified User Experience, including the following features listed below. For more details, refer to [Using User Mapping Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html?lang=en#using-user-mapping-tool).
  * Test connection to the User Management API before running the User Mapping
  * Gracefully skip errors and continue with the User Mapping activity
  * User Mapping no longer fails if Access Token expires (after 24 hours). User Mapping can be re-run from where it last stopped.

* To increase CTT robustness, content can be ingested to either Author instance or Publish instance at a time. 

* When versions are included, the path `/var/audit` is automatically included to migrate audit events.

## Best Practices Analyzer {#best-practices-analyzer}

### Release Date {#release-date-bpa-latest}

The Release Date for Best Practices Analyzer v2.1.18 is September 02, 2021.

### What's New {#what-is-new}

* Ability to detect and report on total node count.

* Ability to detect and report on the node store type and size.

### Bug Fixes {#bug-fixes-bpa}

* BPA was falsely detecting presence of Commerce Integration Framework.
