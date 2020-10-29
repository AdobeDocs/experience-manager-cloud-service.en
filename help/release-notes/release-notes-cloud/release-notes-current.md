---
title: Release Notes for 2020.10.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: [!DNL Adobe Experience Manager] as a Cloud Service Release Notes for 2020.10.0.
---

# Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service 2020.10.0 {#release-notes}

The following section outlines the general Release Notes for [!DNL Experience Manager] as a Cloud Service 2020.10.0.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2020.11.0 is December 1, 2020.
The following release (2020.12.0) will be on December 17, 2020

## [!DNL Adobe Experience Manager Sites] as a Cloud Service {#sitess}

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

* **[!DNL Assets] WebP file support**: [!DNL Assets] as a Cloud Service now supports WebP image format. WebP is an emerging image format created by Google. Images in WebP file format are visually indistinguishable from JPG or PNG files and the files are much smaller. Lowered file size of assets improves the page-load times and help content creators deliver a faster web experience.

<!--
### Bugs Fixed {#bugs-fixed-assets}

Content to come
-->

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What is New {#what-is-new-commerce}

* Released CIF Venia Reference Site - 2020.10.2 that includes the lastest CIF Core Components version v1.4.0. Refer to [CIF Venia Reference Site](https://github.com/adobe/aem-cif-guides-venia/releases/tag/venia-2020.10.2) for more details.

* Released CIF Core Components v1.4.0. Refer to [CIF Core Components](https://github.com/adobe/aem-core-cif-components/releases/tag/core-cif-components-reactor-1.4.0) for more details.

### Bug Fixes {#bug-fixes-commerce}

* GraphQL requests in the Product Console and Pickers were done via HTTP POST. This has been fixed to ensure that the Apollo GraphQL client respects the setting in the GraphQL client OSGi configuration to support GET requests if configured.

* CIF Cloud config UI displayed "Save & Close" buttons for configs in /lib and /apps/. But these are read-only hence UI fixed to display "Close" button only.

### Cloud Manager {#cloud-manager}

* The Environments page has been redesigned.

* Hibernated environments now show a discrete status in Cloud Manager when they are hibernated.

* The Cloud Manager build container now supports both Java 8 and Java 11.

* The number of environment variables per environment has been increased to 200.

* The Environment card on the Overview page will now list up to three environments. Users can select the **Show all** button to navigate to the Environment summary page to view a table with a complete list of environments.


### Bug Fixes {#bug-fixes-cloud-manager}

* The link from Cloud Manager to the Developer Console was incorrectly active before environments were fully created.

* The link to the Developer Console directly from Cloud Manager did not display the option to de-hibernate/hibernate a Sandbox Program's environment.

* The Cancel and Save buttons on the Non-Production Pipeline Edit page were not always visible.

* Certain failures in the code quality process could result in the log file not being generated correctly.

* When creating a new program, the suggested name would sometimes return a duplicate of an existing program name.

* Some large pipeline step logs could not be consistently downloaded through the user interface.

* The validation of environment names had an off-by-one error.

* The Environments page would sometimes show publish and dispatcher segments when none was present.


## Adobe Experience Manager as a Cloud Service Foundation {#cloud-service-foundation}

### Workflows {#workflows}

* Support added for searching workflow instances based on Workflow Title, Workflow Model, Status, Initiator, Payload Path and Start Date.

## Content Transfer Tool {#content-transfer-tool}

Follow this section to learn about what is new and the updates for [Content Transfer Tool](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/overview-content-transfer-tool.html) Release v1.1.12.

### What is New {#what-is-new-ctt}

* User experience for logs improved. Timestamps added to Extraction and Ingestion logs. Message added to indicate if logs are empty.

### Bug Fixes {#ctt-bug-fixes}

* Content Transfer Tool was skipping content files if the migration set contained paths that had the partially similar file names. This has been fixed.
