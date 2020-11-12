---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
---

# Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for [!DNL Experience Manager] as a Cloud Service.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2020.10.0 is October 28, 2020.
The following release (2020.11.0) will be on December 1, 2020.

## [!DNL Adobe Experience Manager Sites] as a Cloud Service {#sites}

### What is new in [!DNL Sites] {#what-is-new-sites}

<!-- add when release done: * **Core Components 2.12.0**: With Core Components being on auto-update, benefit from the latest improvements contributed by the community. See list of changes since 2.11.1: Release Notes -->

* **Project Archetype 24**: The recommended foundation to start a new AEM project got better, now including the new Adobe Client Data Layer, option to deliver site in AMP and new extension points to add project CSS/JS.

* **ContextHub Folders**: Ability to create audience folders to easily organize, find and select audience segments to use for ContextHub offer targeting capabilities. 

## [!DNL Adobe Experience Manager Assets] as a Cloud Service {#assets}

### What is new in [!DNL Assets] {#what-is-new-assets}

* **[!DNL Adobe Sensei] powered video smart tagging**: By leveraging AI models to analyze video content for object and action-specific tags, DAM users can spend less time adding tags and more time making use of the rich information exposed to deliver the right experience to customers. See [Smart tag video assets](/help/assets/smart-tags-video-assets.md).

* **Brand Portal enhancements**: The following new features and more are available in [!DNL Brand Portal]. For details, see [[!DNL Brand Portal] release notes](https://docs.adobe.com/content/help/en/experience-manager-brand-portal/using/introduction/brand-portal-release-notes.html).

  * [Enhanced download experience](https://docs.adobe.com/content/help/en/experience-manager-brand-portal/using/download/brand-portal-download-assets.html) for simplified, quick downloads. Additional download configurations can be configured by administrators to offer an experience that suits the needs of the users and businesses.
  * One-click navigation to Files, [Collections](https://docs.adobe.com/content/help/en/experience-manager-brand-portal/using/share/brand-portal-share-collection.html), and Shared Links is now possible from any page.
  * Users can [select and download specific renditions](https://docs.adobe.com/content/help/en/experience-manager-brand-portal/using/download/brand-portal-download-assets.html#download-assets-from-asset-details-page) now. The new rendition download option is available in the Renditions panel in the Asset details page.
  * A timeout of 15 minutes for guest user sessions ensures a better experience to all concurrent users.

* **[!DNL Adobe Asset Link] version 2.1**: A new version of [Adobe Asset Link](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/manage-assets-using-adobe-asset-link.ug.html) extension for [!DNL Adobe Photoshop], [!DNL Adobe Illustrator], and [!DNL Adobe InDesign] is available. It adds compatibility with the latest [!DNL Adobe Creative Cloud] applications with version 2021, released in October 2020.

* **[!DNL Assets] WebP file support**: [!DNL Assets] as a Cloud Service now supports WebP image format. WebP is an emerging image format created by Google. Images in WebP file format are visually indistinguishable from JPG or PNG files and the files are much smaller. Lowered file size of assets improves the page-load times and help content creators deliver a faster web experience. See [create a standard processing profile](/help/assets/asset-microservices-configure-and-use.md#create-standard-profile).

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What is New {#what-is-new-commerce}

* Released CIF Venia Reference Site - 2020.10.2 that includes the lastest CIF Core Components version v1.4.0. Refer to [CIF Venia Reference Site](https://github.com/adobe/aem-cif-guides-venia/releases/tag/venia-2020.10.2) for more details.

* Released CIF Core Components v1.4.0. Refer to [CIF Core Components](https://github.com/adobe/aem-core-cif-components/releases/tag/core-cif-components-reactor-1.4.0) for more details.

### Bug Fixes {#bug-fixes-commerce}

* GraphQL requests in the Product Console and Pickers were done via HTTP POST. This has been fixed to ensure that the Apollo GraphQL client respects the setting in the GraphQL client OSGi configuration to support GET requests if configured.

* CIF Cloud config UI displayed "Save & Close" buttons for configs in /lib and /apps/. But these are read-only hence UI fixed to display "Close" button only.


## Cloud Manager {#cloud-manager}

### Release Date {#release-date-cm}

The Release Date for Cloud Manager in AEM as a Cloud Service 2020.11.0 is November 12, 2020.

### What's New {#what-is-new}

* A new menu option **Local Login** is now be available to users from the environment menu options on the Environment card and Environments Summary pages. 

* The **Learn** tab in Cloud Manager has been refreshed with new images in the UI.

### Bug Fixes {#bug-fixes-cloud-manager}

* The loading of dependencies done prior to build execution required downloading a Maven plugin.
* The link from the Cloud Manager footer to select a language will now navigate to the correct location.
* Sometimes during the code scanning, the SonarQube process would not start. This will now be auto-detected and a restart attempted.
* All existing production pipelines will be automatically enabled with the Experience Audit step. 

## Adobe Experience Manager as a Cloud Service Foundation {#cloud-service-foundation}

### Workflows {#workflows}

* Support was added for searching workflow instances based on Workflow Title, Workflow Model, Status, Initiator, Payload Path and Start Date. See [Search Workflow Instances](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/sites/administering/workflows-administering.html).

## Content Transfer Tool {#content-transfer-tool}

Follow this section to learn about what is new and the updates for [Content Transfer Tool](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/overview-content-transfer-tool.html) Release v1.1.12.

### What is New {#what-is-new-ctt}

* User experience for logs improved. Timestamps added to Extraction and Ingestion logs. Message added to indicate if logs are empty.

### Bug Fixes {#ctt-bug-fixes}

* Content Transfer Tool was skipping content files if the migration set contained paths that had the partially similar file names. This has been fixed.
