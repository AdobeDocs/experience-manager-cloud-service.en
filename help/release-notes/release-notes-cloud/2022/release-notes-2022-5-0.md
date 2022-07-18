---
title: Release Notes for 2022.5.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2022.5.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: 1b867582-e34c-435b-b8f8-fc71dddcaccb
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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2022.5.0) is June 9, 2022.
The next release (2022.6.0) is planned for June 30, 2022.

## Release Video {#release-video}

Have a look at the May 2022 Release Overview video for a summary of the features added in the 2022.5.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/343321/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features available in [!DNL Sites] prerelease channel {#prerelease-features-sites}

* Various GraphQL functionalities
* A [new console](/help/sites-cloud/administering/content-fragments/content-fragments-console.md) optimized for Headless use of Content Fragments

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

* [Dynamic Media Smart Imaging](https://medium.com/adobetech/one-solution-fits-all-smart-imaging-with-aem-dynamic-media-be690b62df9f) now supports AVIF file format - further improve Google Core Web Vital (Largest Contentful Paint), with AVIF providing 20% extra size reduction over WebP. In total, AVIF provides up to 41% average size reduction over JPEG (in some images even as high as 76%).

* [!UICONTROL Experience Manager Assets Brand Portal] now executes automatic jobs every twelve hours to delete all Brand Portal assets that are published to AEM. As a result, you do not need to delete the assets in the Contribution folder manually to keep the folder size below the threshold limit. See [What's new in Experience Manager Assets Brand Portal](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/introduction/whats-new.html).

### New features available in [!DNL Assets] prerelease channel {#prerelease-features-assets}

Experience Manager Assets uses Adobe Sensei AI capabilities to now [distinguish between colors in an image and apply those as tags automatically on ingestion](/help/assets/color-tag-images.md). These tags enable enhanced Search experience, based on image color composition. You can configure the number of colors, within a range of one to forty, that are tagged to an image so that you can search for images based on those colors later.


## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features available in [!DNL Forms] prerelease channel {#prerelease-features-forms}

* **Integrate Adaptive Forms with Microsoft® Power Automate**: You can now configure an Adaptive Form to run a Microsoft® Power Automate Cloud Flow on submission. The configured Adaptive Form sends captured data, attachments, and Document Of Record to Power Automate Cloud Flow for processing. It helps you build custom data capture experience while harnessing the power of Microsoft® Power Automate to build business logics around captured data and automate customer workflows.

* **Wizard to create an Adaptive Form**: You can use business user friendly wizard to quickly author Adaptive Forms. The wizard provides a quick tab navigation to easily select pre-configured template, styling, fields, and submission options to create an adaptive form.

    ![Wizard to create an Adaptive Form](/help/release-notes/assets/wizard.png)

## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* Quick access to product cockpit: Easily access full detailed product information with one-click in Sites Editor

    ![Enable wishlist](/help/assets/CIF/enable-wishlist.png)

* Support for additional marketing commerce components:  Components can be configured to show an add-to-cart and add-to-wishlist call-to-action

    ![Sites editor shortcut to product cockpit](/help/assets/CIF/sites-editor-shortcut-to-cockpit.png)


## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### What is New {#what-is-new-foundation}

*  The "Add tree” option under the replication agent admin screen's **Distribute tab**, which was previously announced as deprecated, will be removed on June 20, 2022 or soon thereafter. Packages with a tree hierarchy of content should instead be replicated using [Manage Publication](/help/operations/replication.md#manage-publication) or the [Publish Content Tree workflow](/help/operations/replication.md#publish-content-tree-workflow).

*  Using the replication agent admin screen or replication API for distributing content packages larger than 10 MB (nodes with properties, not including binaries) is deprecated and will be enforced on September 12, 2022 or soon thereafter. Instead, [Manage Publication](/help/operations/replication.md#manage-publication) or the [Publish Content Tree workflow](/help/operations/replication.md#publish-content-tree-workflow) must be used to replicate these large content packages. In July, a warning message will appear in the  replication agent admin screen's **Distribute tab** if attempting to replicate these large content packages and also in the AEM error log whenever the replication API is used to replicate these large content packages. In September, warnings will be replaced by errors. Please adjust your processes accordingly.

### New features available in [!DNL Experience Manager] prerelease channel {#prerelease-features-foundation}

* AEM as a Cloud Service is now integrated with Unified Shell to improve the user experience and unify it with all the other Experience Cloud applications. Refer to [AEM as a Cloud Service on Unified Shell](/help/overview/aem-cloud-service-on-unified-shell.md) for more details.

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation Security {#foundation-security}

### TLS 1.0, 1.1 deprecation

Starting June 30th 2022, Experience Manager as a Cloud Service will require a more secure network communication and data exchange with users systems. AEM will use exclusively Transport Layer Security (TLS), 1.2 protocol. Older TLS versions 1.0 and 1.1 will be deprecated.

If you continue to use older versions of TLS as 1.0, 1.1, you could potentially lose access to Experience Manager as a Cloud Service.  

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes-cloud-manager/release-notes-cm-current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
