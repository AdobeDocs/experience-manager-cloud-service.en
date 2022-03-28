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

>[!NOTE]
>
>The 2022.2.0 release was merged into the 2022.3.0 Release. These release notes will cover all the features.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2022.3.0) is March 31, 2022.
The following release (2022.4.0) is on April 28, 2022.

## Release Video {#release-video}

Have a look at the [March 2022 Release Overview](https://video.tv.adobe.com/v/340450) video for a summary of the features added in the 2022.3.0 release.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

* [!DNL AEM Dynamic Media] now provides the flexibility to [configure one alias account](/help/assets/dynamic-media/dm-alias-account.md) in the user interface, thereby ensuring out-of-the-box Dynamic Media URLs and Viewer Embed code are updated. This positively impacts SEO, to reflect updates made to your business context, such as rebranding.

* You can now use the [!DNL Experience Manager Assets] user interface to:

  * Configure the [detection of duplicate assets](/help/assets/manage-digital-assets.md#detect-duplicate-assets) in a repository.

  * Configure [adding digital watermarks](/help/assets/watermark-assets.md) to images.

* The administrators can now configure email service for large downloads. It allows the users to [enable email notifications for large downloads](/help/assets/download-assets-from-aem.md#enable-email-notifications-for-large-downloads) from the [!DNL Experience Manager Assets] interface. The user receives an email notification containing the download link of the archived zip folder upon completion of the download process.

* The [Manage Publication](/help/assets/manage-publication.md) feature is enhanced with an improved user interface. The users can publish or unpublish content to and from the selected destination, [Add Content](/help/assets/manage-publication.md#add-content) to the publishing list from across the DAM repository, [Include Folder Settings](/help/assets/manage-publication.md#include-folder-settings) to publish content of the selected folders and apply filters, and [schedule publishing](/help/assets/manage-publication.md#publish-assets-later) to a later date or time.

### New features in the [!DNL Assets] prerelease channel {#assets-prerelease-features}

* Experience Manager Assets uses Adobe Sensei AI capabilities to now distinguish between colors in an image and apply those as tags automatically on ingestion. These tags enable enhanced Search experience, based on image color composition.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### What is new in [!DNL Forms] {#what-is-new-forms}

* **[!DNL Communications - Document Generation APIs]**: [Document Generation APIs](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/using-communications/aem-forms-cloud-service-communications.html) help to combine, rearrange, and validate PDF documents. The service allows you to generate documents in synchronous mode. The APIs enables you to create applications that let you:

  * Assemble PDF documents.
  * Disassemble PDF documents.
  * Convert to and validate PDF/A-compliant documents.

* **Automatically convert PDF Forms large than 15 pages to adaptive forms**: You can now use automated forms conversion service to convert PDF Forms with up to 40 pages to adaptive forms. The service now provides option to convert sections of forms larger than 15 pages to adaptive form fragments. It helps improve rendering speed of converted forms and makes it easier to load large forms in adaptive form editor.  

### New features available in [!DNL Forms] prerelease channel {#prerelease-features-forms}

* **Use custom XCI for generating a Document of Record**: You can now use a custom XCI file to set various properties of a Document of Record. It overrides the master XCI with the custom changes.

* **Use invisible CAPTCHA in an adaptive form**: You can use the invisible CAPTCHA to show the CAPTCHA challenge only in the case of a suspicious activity. If no suspicious activity is found the CAPTCHA challenge is not displayed.

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### What is New {#what-is-new-foundation}

* For more efficient and effective troubleshooting of custom features in Cloud environments, we’ve released a new developer tool – [the Repository Browser](/help/implementing/developing/tools/repository-browser.md). It’s a lightweight, read-only, HTML browser that you can launch from the Developer Console. Get visibility into the content repository on the publisher, author, and preview tiers—and in all environments, including production, stage, and non-production. Browse the content structure, view properties, and preview and download binaries.

  ![repobrowserrelnotes](/help/release-notes/assets/repobrowserrelnotes.png)

* The credentials used to authenticate server-to-server API calls (e.g., for GraphQL API requests) can now be refreshed before expiration in a self-serve way from the Developer Console. See the [documentation](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md#refresh-credentials) for more info.

* Version purge and audit log purge maintenance tasks, which had not previously been enabled, will be enabled for new environments. See the associated values in the Maintenance Task article. Purging for existing environments (any created before 2022.3.0) will be enabled in the next monthly release (2022.3.0).

## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* Beta: AEM CIF Search Core Component support Commerce LiveSearch
* Improved SEO for multi-store scenarios: URL formats for PDP / PLP can now be configured on a store level via the CIF Cloud Config properties
* Product picker supports staged products via new filter option in the UI.  This enables content practitioners to prepare product content management for upcoming product launches
* Simplified CIF configuration management and error handling by using CIF Cloud Config name instead of config proxy url
* Manual category selection for Product list and Carousel components. This allows content practitioners to use these components on content pages, outside of the catalog experience

## Cloud Manager {#cloud-manager}

### February Release Date {#release-date-cm-feb}

The release date for Cloud Manager in AEM as a Cloud Service 2022.02.0 is 10 February 2022. The next release is planned for 10 March 2022.

### What's New {#what-is-new-cm-feb}

* New accelerated [Web Tier Config pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#web-tier-config-pipelines) have been introduced to exclusively deploy HTTPD/dispatcher configuration.
  * You must be on AEM version `2021.12.6151.20211217T120950Z` or newer and [opt in to the flexible mode of the dispatcher tools](/help/implementing/dispatcher/disp-overview.md#validation-debug) to use this feature.
  * This feature will be rolled out in a phased approach over the two weeks following the 2022.02.0 release.
* The Cloud Manager landing page experience has been refreshed to deliver improved navigation, easy switching between grid/tile views, and pop-overs for quick program summary.
* A new failing threshold (`< D`) has been added to the [reliability rating metric.](/help/implementing/cloud-manager/code-quality-testing.md#understanding-code-quality-rules)
  * Customers with severe quality issues that impact system stability, primarily related to invalid indexes and workflow processes, will not be able to deploy until those issues are resolved.
* The severity of the `BannedPath` [quality rule](/help/implementing/cloud-manager/code-quality-testing.md#understanding-code-quality-rules) has been changed from blocker to critical.
* The pipeline wizard will inform the user when an AEM environment update may be needed before configuring a [Web Tier Config pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#web-tier-config-pipelines) associated with it.

### Bug Fixes {#bug-fixes-cm-feb}

* Old git repository passwords are now always invalidated when a new password is generated.
* Updating environment variables through the API no longer interferes with a pipeline execution in rare situations.

### March Release Date {#release-date-cm-march}

The release date for Cloud Manager release 2022.3.0 in AEM as a Cloud Service 10 March 2022. The next release is planned for 7 April 2022.

### What's New {#what-is-new-cm-march}

* Accessing AEM Environment log can be done using the Developer role.

### Bug Fixes {#bug-fixes-cm-march}

* A subset of git repositories created manually had an incorrect name value which prevented the build artifact reuse feature from being effective. The names of those repositories have been changed and users will see the corrected name in the Cloud Manager API/UI.
* Build artifacts from non-production pipelines were inappropriately reused on production full stack pipelines.
 * When adding or editing a code quality pipeline, the options to handle metric failures is no longer displayed.
* Some unexpected pipeline variable configurations could cause in the build step.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.9.0 is February 28, 2022.

### What's New {#what-is-new-ctt}

* Check Size Guardrails - The Content Transfer Tool Check Size feature helps reduce failed content transfers.  With the Check Size feature, users can 1) determine whether they have sufficient disk space in the `crx-quickstart` subdirectory before extraction, and 2) estimate the migration set size and verify if it’s supported. If one or both these checks are violated, users will see warnings in the CTT UI. With this guardrail, you can avoid content transfer failures and proactively discuss migration options with Adobe Customer Care. Refer to [Determining migration set size and disk space](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/getting-started-content-transfer-tool.html?lang=en#migration-set-size) for more details.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.26 is March 16, 2022.

### What's New {#what-is-new-bpa}

* Ability to detect unprocessed assets. If unprocessed assets are detected, these assets either need to be set to processed or need to be removed from the migration set during content transfer to avoid running into issues during content ingestion.
* Ability to detect if content has more than 1000 vanity URLs. Using a high number of vanity URLs is not best practice since it puts a load on Dispatcher and Publish servers.
* Ability to identify issues related to Oak index definitions and detect incompatibilities with AEM as a Cloud Service.
* Ability to detect and report on usage of Externalizer configurations. In AEM as a Cloud Service Externalizer configurations are set by Cloud Manager, hence, existing Externalizer configurations need to be refactored to maintain compatibility.

### Bug Fixes {#bug-fixes-bpa}

* In some scenarios, BPA failed to run because of FormsSelectiveFeaturesAnalysis throwing an assertion error. This has been fixed.
* BPA was reporting findings related to the WRK pattern as MAJOR instead of CRITICAL. This has been fixed.
* BPA was incorrectly reporting findings related to OAK index definitions in ui.apps as CRITICAL. This has been fixed
