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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current release (2022.6.0) is June 30, 2022.

The next release (2022.7.0) is planned for July 28, 2022.

## Release Video {#release-video}

Have a look at the June 2022 Release Overview video for a summary of the features added in the 2022.6.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/344308/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in [!DNL Sites] {#sites-features}

* The [Content Fragment Console](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/content-fragments-console.html?lang=en) now supports keyboard shortcuts. 

* The new [Table of Contents Component](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/components/tableofcontents.html) works not only with the Core Components but with all components, automatically rendering ToCs on content pages. And because it is rendered server-side and fully cached by the dispatcher, it is also efficient to load.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features available in [!DNL Assets] prerelease channel {#prerelease-features-assets}

You can now configure Adobe Experience Manager Assets to [restrict the type of assets that users can upload based on the MIME type](/help/assets/configure-asset-upload-restrictions.md). It helps prevent accidental uploads of undesired format and malicious files.

![Asset upload restrictions](/help/assets/assets/asset-upload-restrictions.png)

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features in [!DNL Forms] {#forms-features}

* **Keyboard input support for Scribble signatures**: Adaptive Forms are increasingly being used on touch devices, and one common requirement is to support signatures. Signing documents on touch devices has become an accepted way of signing forms. Adaptive Forms has native support for Scribble Signatures and Adobe Sign for such use cases. Now, along with other already supported options, you can also use keyboard to Scribble signatures in an Adaptive Form. It also helps improve accessibility compliance.

![Keyboard input support for Scribble signatures on iphone](/help/release-notes/assets/scribble-keyboard-mobile.png)

### New features available in [!DNL Forms] prerelease channel {#prerelease-features-forms}

* **Launch Adaptive Form creation wizard from embed form component**: You can now launch Adaptive Form creation wizard from embed form component. It helps improve content and forms authoring workflows for Sites and Forms practitioners trying to add enrollment experiences to a web page.

![Keyboard input support for Scribble signatures on iphone](/help/release-notes/assets/froms-container.png)

* **Invoke - An AEM Workflow step**: Document Description XML (DDX) is a declarative markup language whose elements represent building blocks of documents. These building blocks include PDF and XDP documents, and other elements such as comments, bookmarks, and styled text. DDX documents are templates for the documents and describe the desired characteristics of source documents that should appear in resultant documents. A single DDX can be used with a range of source documents. You can use the Invoke step an AEM Workflow to perform various operations, like assembling disassembling documents, creating and modifying Acrobat and XFA Forms, and other operations described in [DDX Reference](https://helpx.adobe.com/content/dam/help/en/experience-manager/forms-cloud-service/ddxRef.pdf) documentation.

* **Convert to PDF/A - An AEM Workflow step**: PDF/A is an archival format for long-term preservation of the document’s content, all fonts are embedded and the file is uncompressed. Now, you can use the Convert to PDF/A step an AEM Workflow to convert your documents or files in any format to PDF/A format.


## CIF Add-on {#cloud-services-cif}

### What is New {#what-is-new-cif}

* Product catalog enrichment now supports AEM pages. This enables authors to manage page - product association.

* Various CIF Core Component improvements

### Bug fixes {#bug-fixes-cif}

* Add login token to client-side price fetching

* Wrong page component in datalayer

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### What is New {#what-is-new-foundation}

* As mentioned in the May (2022.5.0) release notes, the "Add tree” option under the replication agent admin screen’s **Distribute** tab was removed. Packages with a tree hierarchy of content should instead be replicated using [Manage Publication](/help/operations/replication.md#manage-publication) or the [Publish Content Tree](/help/operations/replication.md#manage-publication#publish-content-tree-workflow) workflow.
* Sling Content Distribution (SCD) now supports an explicit "invalidation" action in order to invalidate content without that content being published. See [this article](/help/implementing/dispatcher/caching.md#explicit-invalidation) for further details.

### New features available in [!DNL Experience Manager] prerelease channel {#prerelease-features-foundation}

* AEM as a Cloud Service is now integrated with Unified Shell to improve the user experience and unify it with all the other Experience Cloud applications. Refer to [AEM as a Cloud Service on Unified Shell](/help/overview/aem-cloud-service-on-unified-shell.md) for more details.

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes-cloud-manager/release-notes-cm-current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
