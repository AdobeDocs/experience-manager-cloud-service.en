---
title: Release Notes for 2021.10.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2021.10.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: ab584923-5f06-4b54-941b-e00bc1158b81
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

* Content Fragment models are now automatically set in read-only state once they are published, to avoid unintentionally breaking live API queries after re-publishing an edited model. Users are prompted with a warning when attempting to edit a published model. Editing is possible upon accepting the warning. 

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

* [!DNL Experience Manager] now supports auto-generation of text transcripts from the supported audio and video assets, using a built-in connector to [!DNL Azure Media Services]. The [supported file types](/help/assets/file-format-support.md#audio-video-transcription-formats) are automatically transcribed and the text is stored in WebVTT format. The WebVTT captions are used for more effective searching, captioning, or translation. Also, the feature improves accessibility, discoverability, and localization of the assets.

### New feature in the [!DNL Assets] prerelease channel {#assets-prerelease-features}

* [!DNL Dynamic Media] Image Smart Crop and Swatch is now powered by latest Sensei services, that generates improved crops and swatches. Also, an enhancement has been launched to generate different crop content, for same aspect ratio but across different resolutions. In addition, any manual edits will be preserved on reprocessing, if there is no change in the width and height in the Image Profile.

* Smart Tags are automatically applied to the assets using asset microservices, instead of Smart Content Services. The underlying model is updated to improve tagging results and reduce bias. <!-- As it uses asset microservices, it is now possible to develop custom workers using Stock10-based Smart Tags. -->

<!-- Leave this commented.
### Bugs fixed in [!DNL Assets] {#assets-bugs-fixed}

No customer-reported bugs fixed in Oct release. Details in CQDOC-18404.
-->

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### What is new in [!DNL Forms] {#what-is-new-forms-oct-2021}

* **Analytics for Adaptive Forms**: You can now capture and track behavior of both logged-in and not logged-in (Anonymous) via Adobe Analytics for Adaptive Forms to gather end user insights. It helps make informed decisions based on data to improve end user experience.

### New features available in [!DNL Forms] prerelease channel {#prerelease-features-forms-oct-2021}

* **Externalize AEM Workflow data for secure processing**: You can store in-process AEM Workflows data (AEM Workflow Variables data) that contains Sensitive Personal Data (SPD) elements in a customer-managed repository for secure processing. The data elements and workflow variables are not stored in AEM repository and are fetched on demand from a customer-managed repository while processing the Workflow.

### Beta features of [!DNL Forms]  {#what-is-new-forms-oct2021-beta}

* **[!DNL AEM Forms as a Cloud Service - Communications]**: [Communication APIs](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/using-communications/aem-forms-cloud-service-communications.html) help you combine a template and XML data to generate print documents in various formats. The service allows you to generate documents in synchronous and batch modes. The APIs enables you to create applications that let you:

  * Generate documents by populating template files (PDF and XDP) with XML data.
  * Generate output forms in various formats, including non-interactive PDF print streams.

You can write to [!DNL formscsbeta@adobe.com] to sign up for the beta program.

## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* The CIF add-on supports latest Commerce v2.4.3 with new GraphQL APIs and schemas

* Authors can add links to product and catalog pages in text fields using the rich text editor (RTE). A CIF icon has been added to the RTE toolbar that will open up the pickers to quickly search and select the product or category without leaving the context.

* Existing pop-up shopping cart and checkout have been replaced with dedicated AEM shopping cart and checkout pages. The components on these pages are built using Adobe Commerce's extensible Peregrine components

* Merchants can hide certain product catalog categories in the navigation using the Commerce backend. The CIF Navigation Core Component respects the commerce backend configuration "include in menu" to show / hide categories in navigation

* AEM Storefront Venia returns HTTP 404 error if category or product page is not found

## Cloud Manager {#cloud-manager}

This section outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.10.0.

### Release Date {#release-date-cm-nov}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.11.0 is November 04, 2021.
The next release is planned for December 09, 2021.

### What's New {#what-is-new-cm-nov}

* Users can now leverage new Front End pipelines to exclusively deploy front end code in an accelerated manner. See [Cloud Manager Front End Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#front-end) to learn more.

   >[!IMPORTANT]
   >You must be on AEM version `2021.10.5933.20211012T154732Z` to leverage new Front End pipelines.

* Code Quality pipeline duration is significantly reduced by performing the code analysis in a more efficient way without the need of building a whole AEM image. This change will roll out progressively over the weeks following the release.

* The Git Commit ID will now be displayed in the pipeline execution details making it easier to track the code that was built.

* Program Creation is now available via publicly exposed API.

* Environment Creation is now available via publicly exposed API.

* The `x-request-id` response header is now visible in the API Playground on [www.adobe.io](https://www.adobe.io/). This header is useful when submitting customer care issues for troubleshooting.

* As a user, I see  Pipeline card with zero pipelines provide me with appropriate guidance. 

* A new Activity Page is now available where activities such as pipeline and code executions can be viewed along with their associated details. Over time, the activities listed in this page will expand in scope along with the details provided.

* A new Pipelines page with an on-hover, status popover for easy view of the summary of details is now available. Pipeline executions can be viewed along with their associated details.

* The Edit Pipeline API now supports changing the environment used in the deploy phases.

* An optimization in the OakPal scanning process has been introduced for large packages.

* The quality issue CSV file will now contain the timestamp for each quality issue. 

### Bug Fixes {#bug-fixes-nov}

* Certain unorthodox build configurations resulted in unnecessary files being stored in the pipeline's Maven artifact cache which resulted in extraneous network I/O when starting and stopping the build container. 

* Pipeline PATCH API fails if deploy phase does not exist.

* The `ClientlibProxyResourceCheck` quality rule was producing false positive issues when there were client libraries with common base paths.

* Error message when max number of repositories has been reached did not specify the reason for the error.

* In rare cases, pipelines were failing due to inappropriate retry handling of certain response codes. 


## Release Date {#release-date-cm-oct}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.10.0 is October 14, 2021.

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
