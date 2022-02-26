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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2022.2.0) is March 3, 2022.
The following release (2022.3.0) is on March 31, 2022.

## Release Video {#release-video}

Have a look at the [February 2022 Release Overview](https://video.tv.adobe.com/v/340120) video for a summary of the features added in the 2022.2.0 release.

## Adobe Experience Manager Sites as a Cloud Service {#sites}

* The **[Enable Front End Pipeline](/help/sites-cloud/administering/site-creation/enable-front-end-pipeline.md)** button is available in the **Site** rail of the Sites console for sites that use the v2 of the Page Core Component. This button configures the site to load the themes that are deployed with the Front End Pipeline on top of the existing client libraries.

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### What is New {#what-is-new-foundation}

* For more efficient and effective troubleshooting of custom features in Cloud environments, we’ve released a new developer tool – [the Repository Browser](/help/implementing/developing/tools/repository-browser.md). It’s a lightweight, read-only, HTML browser that you can launch from the Developer Console. Get visibility into the content repository on the publisher, author, and preview tiers—and in all environments, including production, stage, and non-production. Browse the content structure, view properties, and preview and download binaries.

  ![repobrowserrelnotes](/help/release-notes/assets/repobrowserrelnotes.png)

* The credentials used to authenticate server-to-server API calls (e.g., for GraphQL API requests) can now be refreshed before expiration in a self-serve way from the Developer Console. See the [documentation](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md#refresh-credentials) for more info.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

* [!DNL AEM Dynamic Media] now provides the flexibility to [configure one alias account](/help/assets/dynamic-media/dm-alias-account.md) in the user interface, thereby ensuring out-of-the-box Dynamic Media URLs and Viewer Embed code are updated. This positively impacts SEO, to reflect updates made to your business context, such as rebranding.

* You can now use the [!DNL Experience Manager Assets] user interface to:

  * Configure the detection of duplicate assets in a repository.

  * Configure adding digital watermarks to images.

* The administrators can now configure email service for large downloads. It allows the users to [enable email notifications for large downloads](/help/assets/download-assets-from-aem.md#enable-email-notifications-for-large-downloads) from the [!DNL Experience Manager Assets] interface. The user receives an email notification containing the download link of the archived zip folder upon completion of the download process.


* The [Manage Publication](/help/assets/manage-publication.md) feature is enhanced with an improved user interface. The users can publish or unpublish content to and from the selected destination, [Add Content](/help/assets/manage-publication.md#add-content) to the publishing list from across the DAM repository, [Include Folder Settings](/help/assets/manage-publication.md#include-folder-settings) to publish content of the selected folders and apply filters, and [schedule publishing](/help/assets/manage-publication.md#publish-assets-later) to a later date or time.

### New features in the [!DNL Assets] prerelease channel {#assets-prerelease-features}

* 
