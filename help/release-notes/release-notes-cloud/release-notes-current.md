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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2022.3.0) is March 31, 2022.
The following release (2022.4.0) is on April 28, 2022.

## Release Video {#release-video}

Have a look at the [February 2022 Release Overview](https://video.tv.adobe.com/v/340450) video for a summary of the features added in the 2022.2.0 release.

## Adobe Experience Manager Sites as a Cloud Service {#sites}

* The **[Enable Front End Pipeline](/help/sites-cloud/administering/site-creation/enable-front-end-pipeline.md)** button is available in the **Site** rail of the Sites console for sites that use the v2 of the Page Core Component. This button configures the site to load the themes that are deployed with the Front End Pipeline on top of the existing client libraries.

<!-- Alexandru Sarchiz: Please do NOT delete this. Most of the Foundation features will be released in an intermediary release with no mention in the release notes. Once the proper 2022.02/03 release rolls out, we will publish the release notes as well. Commenting this out temporarily so that it doesn't break validation, since some of the pages linked to here will be moved out of the 2022.02-release branch.

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### What is New {#what-is-new-foundation}

* For more efficient and effective troubleshooting of custom features in Cloud environments, we’ve released a new developer tool – [the Repository Browser](/help/implementing/developing/tools/repository-browser.md). It’s a lightweight, read-only, HTML browser that you can launch from the Developer Console. Get visibility into the content repository on the publisher, author, and preview tiers—and in all environments, including production, stage, and non-production. Browse the content structure, view properties, and preview and download binaries.

  ![repobrowserrelnotes](/help/release-notes/assets/repobrowserrelnotes.png)

* The credentials used to authenticate server-to-server API calls (e.g., for GraphQL API requests) can now be refreshed before expiration in a self-serve way from the Developer Console. See the [documentation](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md#refresh-credentials) for more info.

* Version purge and audit log purge maintenance tasks, which had not previously been enabled, will be enabled for new environments. See the associated values in the Maintenance Task article. Purging for existing environments (any created before 2022.3.0) will be enabled in the next monthly release (2022.3.0) -->

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

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.9.0 is February 28, 2022.

### What's New {#what-is-new-ctt}

* Check Size Guardrails - The Content Transfer Tool Check Size feature helps reduce failed content transfers.  With the Check Size feature, users can 1) determine whether they have sufficient disk space in the `crx-quickstart` subdirectory before extraction, and 2) estimate the migration set size and verify if it’s supported. If one or both these checks are violated, users will see warnings in the CTT UI. With this guardrail, you can avoid content transfer failures and proactively discuss migration options with Adobe Customer Care. Refer to [Determining migration set size and disk space](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/getting-started-content-transfer-tool.html?lang=en#migration-set-size) for more details.

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
