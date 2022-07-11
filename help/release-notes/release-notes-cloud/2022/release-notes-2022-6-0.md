---
title: Release Notes for 2022.6.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2022.6.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2022.6.0) is June 30, 2022.

The next release (2022.7.0) is planned for July 28, 2022.

## Release Video {#release-video}

Have a look at the June 2022 Release Overview video for a summary of the features added in the 2022.6.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/344308/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in [!DNL Sites] {#sites-features}

* A new [user interface](/help/sites-cloud/administering/content-fragments/content-fragments-console.md) is now available for content admins and content authors to efficiently manage (take actions such as publish, unpublish, copy, move, etc.), search/filter, and create content fragments for Headless use-cases.

    ![Content Fragment Console](/help/release-notes/assets/cf-ui.png)

* The new [Table of Contents Component](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/components/tableofcontents.html) works not only with the Core Components but with all components, automatically rendering ToCs on content pages. And because it is rendered server-side and fully cached by the dispatcher, it is also efficient to load.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

Experience Manager Assets uses Adobe Sensei AI capabilities to now [distinguish between colors in an image and apply those as tags automatically on ingestion](/help/assets/color-tag-images.md). These tags enable enhanced Search experience, based on image color composition. You can configure the number of colors, within a range of one to forty, that are tagged to an image so that you can search for images based on those colors later.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features in [!DNL Forms] {#forms-features}

* **[Integrate Adaptive Forms with Microsoft® Power Automate](/help/forms/forms-microsoft-power-automate-integration.md)**: You can now configure an Adaptive Form to run a Microsoft® Power Automate Cloud Flow on submission. The configured Adaptive Form sends captured data, attachments, and Document Of Record to Power Automate Cloud Flow for processing. It helps you build custom data capture experience while harnessing the power of Microsoft® Power Automate to build business logics around captured data and automate customer workflows.

* **Wizard to create an Adaptive Form**: You can use business user friendly wizard to quickly author Adaptive Forms. The wizard provides a quick tab navigation to easily select pre-configured template, styling, fields, and submission options to create an adaptive form.

    ![Wizard to create an Adaptive Form](/help/release-notes/assets/wizard.png)

## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* New product cockpit properties page for better and simplified overview

 ![product cockpit properties overview](/help/assets/CIF/product_cockpit_properties_overview.png)

* Improved compatibility and robustness for 3rd party connectors on I/O Runtime

* Improved support for GQL Client configuration overwrites (e.g. set custom caching behavior)

* Multiple commerce endpoints are now supported out-of-the-box and can be configured via Cloud Manager. You can find details in the CIF blog [here](https://medium.com/adobetech/use-aem-as-a-cloud-service-with-multiple-adobe-commerce-systems-9295612a9554).


### Bug fixes {#bug-fixes-cif}

* Multi value product picker field shows 2nd and additional products as invalid

* Product Picker is occasionally hidden behind components

## Reference Demos Add-on {#cloud-services-demos}

### What is New {#what-is-new-demos}

* New WKND Content & Commerce template that extends WKND with an E2E shopping experience featuring product catalog, shopping cart, checkout, and myAccount. This template uses CIF and its CIF Core Components, thus you also need to install the CIF add-on. You can find details in the CIF blog [here](https://medium.com/adobetech/learn-how-to-create-a-shoppable-experience-with-the-new-wknd-reference-site-and-cif-b3b2c161f67e).

 ![WKND shop](/help/assets/CIF/wknd_shop.png)

 ![WKND pdp](/help/assets/CIF/wknd_pdp.png)

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### What is New {#what-is-new-foundation}

* AEM as a Cloud Service is now integrated with Unified Shell to improve the user experience and unify it with all the other Experience Cloud applications. Refer to [AEM as a Cloud Service on Unified Shell](/help/overview/aem-cloud-service-on-unified-shell.md) for more details.

* As mentioned in the May (2022.5.0) release notes, the "Add tree” option under the replication agent admin screen’s **Distribute** tab was removed. Packages with a tree hierarchy of content should instead be replicated using [Manage Publication](/help/operations/replication.md#manage-publication) or the [Publish Content Tree](/help/operations/replication.md#manage-publication#publish-content-tree-workflow) workflow.

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes-cloud-manager/release-notes-cm-current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
