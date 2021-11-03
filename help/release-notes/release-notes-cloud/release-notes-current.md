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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2021.10.0) is November 4, 2021.
The following release (2021.11.0) is on December 2, 2021.

## Release Video {#release-video}

Have a look at the [October 2021 Release Overview](https://video.tv.adobe.com/v/338253) video for a summary of the features added.

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New feature in [!DNL Sites] {#sites-features}

* Content Fragment models are now automatically set in read-only state once they are published, to avoid unintentially breaking live API queries after re-publishing an edited model. Users are prompted with a warning when attempting to edit a published model. Editing is possible upon accepting the warning. 

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

* Annotation of PDF files is now supported using native commenting and annotation tools from Adobe Document Cloud. Annotate PDF content by adding text, highlights, sticky notes, and drawings directly within the document preview window. Users can also jump to pages of interest in the PDF by clicking on specific comments

* Users can now sort the assets displayed in the search results in Column and Card views. The sorting works on Name, Created, Modified, or None columns.

  ![Sort the search results in [!DNL Assets] in Column and Card views](/help/assets/assets/sort-searched-assets.png)
  *Figure: Sort the search results in [!DNL Assets] in Column and Card views.*

### New feature in the [!DNL Assets] prerelease channel {#assets-prerelease-features}

* [!DNL Assets] now includes a built-in connector to [!DNL Azure Media Services] for audio and video transcription. When configured, the supported files are automatically transcribed and generate WebVTT files. The WebVTT captions are used for more effective searching, captioning, or translation for use as subtitles.

<!-- TBD: 'Unpublishing' this feature as suggested by engineering.

* To programmatically invoke processing using asset microservices, a new API is introduced. Developers can now apply an existing folder-level processing profile on one or more specific assets in a folder. The processing profile gets applied based on custom metadata properties updates. See `AssetProcessor` in the [[!DNL Experience Manager] API reference](https://www.adobe.io/experience-manager/reference-materials/). As before, it is possible to [use asset microservices from the user interface](/help/assets/asset-microservices-configure-and-use.md).

-->
<!-- Leave this commented.

### New feature in the [!DNL Assets] prerelease channel {#assets-prerelease-features}

Apparently, no new Assets features in Sep prerelease channel.
A/V transcription feature via CQ-4303854 has moved to Oct prerelease now.

### Bugs fixed in [!DNL Assets] {#assets-bugs-fixed}

No customer-reported bugs fixed in Sep release.
CQ-4328183 was not reported on CS so not documented here.
-->

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### What is new in [!DNL Forms] {#what-is-new-forms-sep-2021}

* **Use Adobe Sign roles in an Adaptive Form**: Adobe Sign for business and enterprise service levels have the option to expand the roles for Agreement recipients, beyond just the Signer, to better match their workflow requirements. You can now [enable each recipient of agreement to configure their role in an Adaptive Form](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/create-an-adaptive-form/use-adobe-sign/working-with-adobe-sign.html#addsignerstoanadaptiveform), with Signer being the default role.

* **Analytics for Adaptive Forms**: You can now capture and [track end user behavior via Adobe Analytics](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/integrate-aem-forms-with-adobe-analytics.html) for Adaptive Forms to gather end user insights. It helps make informed decisions based on data to improve end user experience.

* **Easily connect AEM Forms with Microsoft Dynamics and Salesforce**: The service provides out of the box data source configuration and data models for Microsoft Dynamics and Salesforce, making it [faster and easier for developers to configure Microsoft Dynamics and Salesforce as data sources for an adaptive form](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/use-form-data-model/configure-msdynamics-salesforce.html?lang=en).

* **E-Sign an adaptive form using DocuSign:** [You can use DocuSign to e-sign an adaptive form](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/integrate-docusign-adaptive-forms.html). The service provides a custom submit action to use DocuSign with an adaptive form.

### Beta features of [!DNL Forms]  {#sep-what-is-new-forms-prerelease}

* **Unified Storage Connector:** Use Unified Storage Connector to externalize in-process data in customer-managed repositories. For example, you can store in-process AEM Workflows data (AEM Workflow Variables data) that contains Sensitive Personal Data (SPD) in a customer-managed repository.
  <!--* Enable Forms Portal’s save and resume functionality and store adaptive forms drafts in a customer-managed data repository.-->  

* **[!DNL AEM Forms as a Cloud Service - Communications]**: [Communication APIs](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/aem-forms-cloud-service-communications.html?lang=en) help you combine XDP templates and XML data to generate print documents in various formats. The service allows you to generate documents in synchronous mode. The APIs enables you to create applications that let you:
  * Generate documents by populating template files with XML data.
  * Generate output forms in various formats, including non-interactive PDF print streams.
  * Generate print PDF files from an XFA form PDF and Adobe Acrobat Form.

You can write to [!DNL formscsbeta@adobe.com] to sign up for the beta program.

## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* The CIF add-on supports latest Commerce v2.4.3 with new GraphQL APIs and schemas

* Authors can add links to product and catalog pages in text fields using the rich text editor (RTE). A CIF icon has been added to the RTE toolbar that will open up the pickers to quickly search and select the product or category without leaving the context.

* Existing pop-up shopping cart and checkout have been replaced with dedicated AEM shopping cart and checkout pages. The components on these pages are built using Magento's extensible Peregrine components

* Merchants can hide certain product catalog categories in the navigation using the Commerce backend. The CIF Navigation Core Component respects the commerce backend configuration "include in menu" to show / hide categories in navigation

* AEM Storefront Venia returns HTTP 404 error if category or product page is not found

## Cloud Manager {#cloud-manager}

This section outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.10.0.

## Release Date {#release-date-cm-oct}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.10.0 is October 14, 2021.
The next release is planned for November 04, 2021.

### What's New {#what-is-new-cm-oct}

* In preparation for some upcoming changes, existing deployment pipelines will now be referenced and labelled in the user interface as **Full Stack** pipelines.

* Pipeline card has been refreshed to now display a single, integrated face that shows both production and non-production pipelines, and user can select Run/Pause/Resume directly from the action menu associated with each pipeline.

* A user in Deployment Manager role can now delete Production pipeline in a self-service manner via the UI.

* Add and edit pipeline experiences have been refreshed to now use familiar, modern modals.

* Users of Cloud Manager can now submit feedback directly from the user interface via the **Feedback** button on top right of the landing page.

* Yearly SLA Graphs can now be downloaded from the Cloud Manager's user interface. 

* Code quality and non-production pipeline executions will now use a more efficient shallow cloning process during the build step, leading to a faster build time for customers with especially large git repositories. 

* Add IP Allow List wizard will now inform the user if maximum allowed number of IP Allow Lists has been reached. 

* The Cloud Manager API documentation now includes an interactive playground that allows logged-in users to experiment with the API from their browser. See [Cloud Manager API Playground](https://www.adobe.io/experience-cloud/cloud-manager/reference/playground/) for more details.

* The tool tip on the Program card will be more descriptive if a selection option under 'Navigate To' is disabled. It now displays "A production environment does not exist." 

### Bug Fixes {#bug-fixes-cm-oct}

* In rare situations, when an Adobe staff would restore a customer's environment, the restore was considered complete before the environment was fully operational.

* Certain internal requests made during environment creation were not being retried.

* If deployment failed error occurs following domain name verification, the error message has been corrected to request the customer to contact their Adobe representative.

## Best Practices Analyzer {#best-practices-analyzer}

### Release Date {#release-date-bpa-latest}

The Release Date for Best Practices Analyzer v2.1.20 is October 05, 2021.

### What's New {#what-is-new}

* Ability to detect and report on node name length.

* Ability to detect and report on the total Index size.

* Ability to detect and report on assets that are missing their original rendition.
