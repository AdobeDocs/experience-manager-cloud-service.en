---
title: Release Notes for 2022.4.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2022.4.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: 6c86838a-cabf-4770-b1ae-618af70193a2
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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2022.4.0) is May 5, 2022.
The next release (2022.5.0) is planned for June 9, 2022.

## Release Video {#release-video}

Have a look at the [April 2022 Release Overview](https://video.tv.adobe.com/v/342612?quality=12) video for a summary of the features added in the 2022.4.0 release.

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in [!DNL Sites] {#sites-features}

* Content model data types can now be defined as [translatable](/help/assets/content-fragments/content-fragments-models.md#properties) using a simple checkbox in the content model editor. Additionally, AEM translation rules and configurations are automatically updated.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

* You can now [sort tags](/help/assets/organize-assets.md#use-tags-to-organize-assets) in the tag picker window in ascending or descending order based on the tag name, date of creation, or date of modification.


## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### What is new in [!DNL Forms] {#what-is-new-forms}

* **Communications - Document Manipulation APIs support in Forms as a Cloud Service SDK**: [Document Manipulation APIs](/help/forms/aem-forms-cloud-service-communications.md) help to combine, rearrange, and validate PDF documents. You can now use Communications - Document Generation APIs on a local development environment with the help of AEM Forms as a Cloud Service SDK.

* **Use custom XCI for generating a Document of Record**: You can now [use a custom XCI file to set various properties of a Document of Record](/help/forms/generate-document-of-record-for-non-xfa-based-adaptive-forms.md#use-a-custom-xci-file). It overrides the master XCI with the custom changes. It provides more control over the generation of Documents of Record, increasing personalization, and customization opportunities.

* **Use invisible CAPTCHA in an adaptive form**: You can use the [invisible CAPTCHA to show the CAPTCHA challenge only in the case of a suspicious activity](/help/forms/captcha-adaptive-forms.md). If no suspicious activity is found the CAPTCHA challenge is not displayed. It helps assess human form completion without checkbox requirements, reduce customization efforts, and improve the end-user experience.

* **Form Data Model Configurations**: You can now [reuse Form Data Model configurations across environments](/help/forms/create-form-data-models.md#runmode-specific-context-aware-config), simplifying data integrations and reducing IT costs.

## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* Quick access to product cockpit: Easily access full detailed product information with one-click in Sites Editor

    ![Enable wishlist](/help/assets/CIF/enable-wishlist.png)

* Support for additional marketing commerce components:  Components can be configured to show an add-to-cart and add-to-wishlist call-to-action

    ![Sites editor shortcut to product cockpit](/help/assets/CIF/sites-editor-shortcut-to-cockpit.png)

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### SDK Build Analyzers {#sdk-build-analyzers}

The AEM as a Cloud Service SDK Build Analyzer Maven Plugin detects problems in a maven project, including missing dependencies. It gives developers an opportunity to discover issues during local development, well before deploying to Cloud environments with Cloud Manager. 

A new analyzer has been recently added:

* `content-packages-validation` - validates for well formed content syntax and structure for packages that will be installed during deployment

It is strongly recommended to update your maven project with the latest version of the analyzer or include the analyzer if you haven't yet done so. For more information, see the documentation [here](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/build-analyzer-maven-plugin.html).

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation Security {#foundation-security}

### TLS 1.0, 1.1 deprecation

Starting June 30th 2022, Experience Manager as a Cloud Service will require a more secure network communication and data exchange with users systems. AEM will use exclusively Transport Layer Security (TLS), 1.2 protocol. Older TLS versions 1.0 and 1.1 will be deprecated.

If you continue to use older versions of TLS as 1.0, 1.1, you could potentially lose access to Experience Manager as a Cloud Service.  

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes-cloud-manager/release-notes-cm-current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
