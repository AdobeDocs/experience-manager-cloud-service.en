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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2022.4.0) is May 5, 2022.
The next release (2022.5.0) is planned for May 26, 2022.

## Release Video {#release-video}

Have a look at the [April 2022 Release Overview](https://video.tv.adobe.com/v/342612?quality=12) video for a summary of the features added in the 2022.4.0 release.

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

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes-cloud-manager/release-notes-cm-current.md).

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.9.0 is February 28, 2022.

### What's New {#what-is-new-ctt}

* Check Size Guardrails - The Content Transfer Tool Check Size feature helps reduce failed content transfers.  With the Check Size feature, users can 1) determine whether they have sufficient disk space in the `crx-quickstart` subdirectory before extraction, and 2) estimate the migration set size and verify if it’s supported. If one or both these checks are violated, users will see warnings in the CTT UI. With this guardrail, you can avoid content transfer failures and proactively discuss migration options with Adobe Customer Care. Refer to [Determining migration set size and disk space](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/getting-started-content-transfer-tool.html?lang=en#migration-set-size) for more details.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.28 is April 22, 2022.

### What's New {#what-is-new-bpa}

* Ability to detect and report on usage of unsupported Asset Manager APIs. There are four APIs that are no longer supported in AEM as a Cloud Service. Customers should ensure that they are no longer using these APIs and should be using the new method of asset upload.

* Ability to detect usage of Content Fragment templates. Content Fragment templates are no longer supported for new content fragment creation on AEM as a Cloud Service. Customers will need to create content fragment models to replace content fragment templates.

* Ability to detect assets with more than 100 descendants under the metadate node of the asset in the repository. It is recommended to remove metadata nodes that are not needed to improve the performance when loading folders consisting of such assets.

* Ability to detect and report on type of Data Store used.

* Pattern updated for AEM Form Portal.

### Bug Fixes {#bug-fixes-bpa}

* BPA was reporting findings for core components instead of reporting only on customer components. This has been fixed.
