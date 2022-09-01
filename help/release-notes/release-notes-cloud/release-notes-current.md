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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2022.8.0) is September 1, 2022.
The next release (2022.9.0) is planned for September 29, 2022.

## Release Video {#release-video}

Have a look at the August 2022 Release Overview video for a summary of the features added in the 2022.8.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/346608/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in [!DNL Sites] {#sites-features}

* The [Personalization Tab for Experience Fragments](/help/sites-cloud/authoring/fundamentals/experience-fragments.md) allows segmentation specification capabilities to the Experience Fragment Editor as well as the flexibility to create nested Experience Fragments whereby headers and footers variations can be created for multiple segments. Prior to the launch of this feature, personalization offered by AEM is only available for site pages, but not for Experience Fragments.
 
* The Email component allows the creation of content in AEM that is then delivered as emails via Campaign Classic. The Core Email Component:
  * is based on the [Core WCM Component](https://github.com/adobe/aem-core-wcm-components) which supports Editable Templates and the Style System.
  * provides 10 email-optimized production-ready components (Page, Container, Title, Text, Image, Button, Teaser, Experience Fragment, Content Fragment, Segmentation).
  * provides advanced personalization and segmentation, thanks to the [insertion of Campaign variables](https://github.com/adobe/aem-core-email-components/wiki/RTE-Personalization) on most dialog fields, and to the flexible [Segmentation component](https://github.com/adobe/aem-core-email-components/wiki/Segmentation-component-(Technical-Documentation)).
  * provides optimal email-friendly HTML output, thanks to the [CSS styles inliner](https://github.com/adobe/aem-core-email-components/wiki/HTML-Inliner:-Technical-documentation), the [HTML attribute inliner](https://github.com/adobe/aem-core-email-components/wiki/HTML-Inliner:-Technical-documentation), and the [HTML sanitizer](https://github.com/adobe/aem-core-email-components/wiki/HTML-sanitizing:-Technical-documentation).
  * allows the creation of the emails anywhere.

### New features available in [!DNL Sites] prerelease channel {#prerelease-features-sites}

* The [Content Fragment Console](/help/sites-cloud/administering/content-fragments/content-fragments-console.md) provides users with an option to display the total number of language copies associated with a content fragment. A 1-click access has been provided to view all the language copies as well. Users are also able to filter the table view by the locale of their interest. 

![Content Fragments Languages](/help/release-notes/assets/cfconsole-languages.png)

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#features-assets}

* You can now configure Adobe Experience Manager Assets to [restrict the type of assets that users can upload based on the MIME type](/help/assets/configure-asset-upload-restrictions.md).

  ![Asset upload restrictions](/help/assets/assets/asset-upload-restrictions.png)

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features available in [!DNL Forms] prerelease channel {#prerelease-features-forms}

* [Adaptive Forms wizard](/help/forms/creating-adaptive-form.md): AEM Forms provides business user friendly wizard to quickly author Adaptive Forms. The wizard has a quick tab navigation to easily select pre-configured template, styling, fields, and submission options to create an adaptive form. This release brings following improvements to the wizard:

  * Select or deselect fields: The wizard allows you to create an Adaptive Form based on JSON and Form Data Model schemas. You can now select subset of fields within a schema to include in an Adaptive Form. The selected fields are converted to corresponding Adaptive Form data capture components to quickly create the desired adaptive forms.

  * Use Static Templates: Customers with existing investments in legacy static templates can continue their journey of cloud adoption by using static templates in wizard to author adaptive forms. This provides additional time to customers to migrate old static templates to modern editable templates.

* [Remove hidden fields from a Document of Record (DoR) while server-side processing](/help/forms/generate-document-of-record-for-non-xfa-based-adaptive-forms.md): You can generate the document of record PDF for end users containing only those fields which were visible to them during data capture experience. Upon form submission, the server validates which fields were hidden to the end user based on submitted data and excludes from document of record for consistency.

## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* Association of AEM pages to products and categories via AEM page properties plus overview in product cockpit
 ![product cockpit page association](/help/assets/CIF/product_cockpit_page_association.png)

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes-cloud-manager/release-notes-cm-current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
