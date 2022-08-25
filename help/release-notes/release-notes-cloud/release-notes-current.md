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

* The [Personalization Tab for Experience Fragments](/help/sites-cloud/authoring/fundamentals/experience-fragments.md) allows segmentation specification capabilities to the Experience Fragment Editor as well as the flexibility to create nested experience fragments whereby headers and footers variations can be created for multiple segments. Prior to the launch of this feature, personalization offered by AEM is only available for site pages, but not for experience fragments.
 
* The Email component allows the creation of content in AEM that is then delivered as emails via Campaign Classic. The Core Email Component:
  * is based on the [Core WCM Component](https://github.com/adobe/aem-core-wcm-components) which support Editable Templates and the Style System.
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

### New features in [!DNL Forms] {#forms-features}

* **[Keyboard input support for Scribble signatures](/help/forms/signing-forms-using-scribble.md)**: Adaptive Forms are increasingly being used on touch devices, and one common requirement is to support signatures. Signing documents on touch devices has become an accepted way of signing forms. Adaptive Forms has native support for Scribble Signatures and Adobe Sign for such use cases. Now, along with other already supported options, you can also use keyboard to Scribble signatures in an Adaptive Form. It also helps improve accessibility compliance.

![Keyboard input support for Scribble signatures on iphone](/help/release-notes/assets/scribble-keyboard-mobile.png)

* **Use Adaptive Forms wizard in local language**: You can use the wizard in language of your choice. It now supports all the languages supported by Adobe Experience Manager.

### New features available in [!DNL Forms] prerelease channel {#prerelease-features-forms}

<!-- 

* **[Launch Adaptive Form creation wizard from embed form component](/help/forms/using/embed-adaptive-form-aem-sites.md)**: You can now launch Adaptive Form creation wizard from embed form component. It helps improve content and forms authoring workflows for Sites and Forms practitioners trying to add enrollment experiences to a web page. 

![Keyboard input support for Scribble signatures on iphone](/help/release-notes/assets/froms-container.png) 

-->

* **[Invoke DDX - An AEM Workflow step](/help/forms/aem-forms-workflow-step-reference.md#invokeddx)**: Document Description XML (DDX) is a declarative markup language whose elements represent building blocks of documents. These building blocks include PDF and XDP documents, and other elements such as comments, bookmarks, and styled text. DDX documents are templates for the documents and describe the desired characteristics of source documents that should appear in resultant documents. A single DDX can be used with a range of source documents. You can use the Invoke step an AEM Workflow to perform various operations, like assembling disassembling documents, creating and modifying Acrobat and XFA Forms, and other operations described in [DDX Reference](https://helpx.adobe.com/content/dam/help/en/experience-manager/forms-cloud-service/ddxRef.pdf) documentation.

* **[Convert to PDF/A - An AEM Workflow step](/help/forms/aem-forms-workflow-step-reference.md##convert-pdfa)**: PDF/A is an archival format for long-term preservation of the document’s content, all fonts are embedded and the file is uncompressed. Now, you can use the Convert to PDF/A step an AEM Workflow to convert your documents or files in any format to PDF/A format.

## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* Association of AEM pages to products and categories via AEM page properties plus overview in product cockpit
 ![product cockpit page association](/help/assets/CIF/product_cockpit_page_association.png)

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes-cloud-manager/release-notes-cm-current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
