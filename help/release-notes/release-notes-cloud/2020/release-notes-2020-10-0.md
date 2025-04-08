---
title: Release Notes for 2020.10.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: "[!DNL Adobe Experience Manager] as a Cloud Service Release Notes for 2020.10.0."
exl-id: ac741744-5b47-47a4-b5af-e1089e92c3f0
feature: Release Information
role: Admin
---
# Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service 2020.10.0 {#release-notes}

The following section outlines the general Release Notes for [!DNL Experience Manager] as a Cloud Service 2020.10.0.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2020.10.0 is October 28, 2020.
The following release (2020.11.0) will be on December 1, 2020.

## [!DNL Adobe Experience Manager Sites] as a Cloud Service {#sites}

### What is new in [!DNL Sites] {#what-is-new-sites}

* **[Core Components 2.12.0](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html)**: Adobe Experience Manager as a Cloud Service benefits from automatic updates to the latest release of the Core Components. Release 2.12.0 includes the latest improvements contributed by the community. Improvements include [a new POST form handler;](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/components/forms/form-container.html#post-data) the ability to include custom CSS, JavaScript, and metadata [tags via context aware configuration;](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/including-clientlibs.html#context-aware-loading) and a [`DataLayerBuilder`](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/data-layer/integrations.html#enabling-custom-components) utility to simplify Adobe Data Layer integration in custom components. See the [list of changes](https://github.com/adobe/aem-core-wcm-components/releases/tag/core.wcm.components.reactor-2.12.0) in 2.12.0.

* **[Project Archetype 24](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html)**: The recommended foundation to start a new Experience Manager project got better. It now includes the new [Adobe Client Data Layer](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/data-layer/overview.html), option to [deliver site in AMP](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/amp.html), and new [extension points to add project CSS/JS](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/including-clientlibs.html#context-aware-loading).

* **[ContextHub Folders](/help/sites-cloud/authoring/personalization/contexthub-segmentation.md#organizing-segments)**: Ability to create audience folders to easily organize, find, and select audience segments to use for ContextHub offer targeting capabilities.

## [!DNL Adobe Experience Manager Assets] as a Cloud Service {#assets}

* **[!DNL Adobe Sensei] powered video smart tagging**: By applying AI models to analyze video content for object and action-specific tags, DAM users can spend less time adding tags and more time using the exposed, rich information. In turn, you deliver the right experience to customers. See [Smart tag video assets](/help/assets/smart-tags-video-assets.md).

* **Brand Portal enhancements**: The following new features and more are available in [!DNL Brand Portal]. For details, see [[!DNL Brand Portal] release notes](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/introduction/brand-portal-release-notes.html).

  * [Enhanced download experience](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/download/brand-portal-download-assets.html) for simplified, quick downloads. Additional download configurations can be configured by administrators to offer an experience that suits the needs of the users and businesses.
  * One-click navigation to Files, [Collections](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/share/brand-portal-share-collection.html), and Shared Links is now possible from any page.
  * Users can [select and download specific renditions](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/download/brand-portal-download-assets.html#download-assets-from-asset-details-page) now. The new rendition download option is available in the Renditions panel in the Asset details page.
  * A timeout of 15 minutes for guest user sessions ensures a better experience to all concurrent users.

* **[!DNL Adobe Asset Link] version 2.1**: A new version of [Adobe Asset Link](https://helpx.adobe.com/enterprise/using/manage-assets-using-adobe-asset-link.html) extension for [!DNL Adobe Photoshop], [!DNL Adobe Illustrator], and [!DNL Adobe InDesign] is available. It adds compatibility with the latest [!DNL Adobe Creative Cloud] applications with version 2021, released in October 2020.

* **[!DNL Assets] WebP file support**: [!DNL Assets] as a Cloud Service now supports WebP image format. WebP is an emerging image format created by Google. Images in WebP file format are visually indistinguishable from JPG or PNG files and the files are much smaller. Lowered file size of assets improves the page-load times and help content creators deliver a faster web experience. See how to use WebP in [create processing profile](/help/assets/asset-microservices-configure-and-use.md#create-standard-profile).

## [!DNL Adobe Experience Manager Forms] as a Cloud Service {#forms-oct-2021}

### What is new in [!DNL Forms] {#what-is-new-forms-oct-2021}

* **Analytics for Adaptive Forms**: You can now capture and track behavior of both logged-in and not logged-in (anonymous) by way of Adobe Analytics for Adaptive Forms to gather user insights. It helps business users make informed decisions about adaptive form content, layout, and style based on the gathered insights. 

### New features available in [!DNL Forms] prerelease channel {#prerelease-features-forms-oct-2021}

* **Externalize AEM Workflow data for secure processing**: You can store in-process AEM Workflow variables data that contains Sensitive Personal Data (SPD) elements in a customer-managed repository for secure processing. While processing the workflow, the data stored in workflow variables is not kept in AEM repository. It is fetched on demand from the customer-managed repository.

### Beta features of [!DNL Forms]  {#sep-what-is-new-forms-oct-prerelease}

* **[!DNL AEM Forms as a Cloud Service - Communications]**: [Communication APIs](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/using-communications/aem-forms-cloud-service-communications.html) help you combine a template and XML data to generate  documents in various formats. The service lets you generate documents in synchronous and batch mode.

You can write to [!DNL formscsbeta@adobe.com] to sign up for the beta program.

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What is New {#what-is-new-commerce}

* Released CIF Venia Reference Site - 2020.10.2 that includes the latest CIF Core Components version v1.4.0. See [CIF Venia Reference Site](https://github.com/adobe/aem-cif-guides-venia/releases/tag/venia-2020.10.2) for more details.

* Released CIF Core Components v1.4.0. See [CIF Core Components](https://github.com/adobe/aem-core-cif-components/releases/tag/core-cif-components-reactor-1.4.0) for more details.

### Bug Fixes {#bug-fixes-commerce}

* GraphQL requests that were in the Product Console and Pickers were done by way of HTTP POST. This issue has been fixed to ensure that the Apollo GraphQL client respects the setting in the GraphQL client OSGi configuration to support GET requests if configured.

* CIF Cloud config UI displayed "Save & Close" buttons for configs in /lib and /apps/. But these interfaces are read-only hence UI fixed to display "Close" button only.

## Cloud Manager {#cloud-manager}

### Release Date {#release-date-cm}

The Release Date for Cloud Manager in Experience Manager as a Cloud Service 2020.10.0 is October 02, 2020.

### What is new in [!DNL Cloud Manager] {#what-is-new-cm}

* The Environments page has been redesigned.

* Hibernated environments now show a discrete status in Cloud Manager when they are hibernated.

* The Cloud Manager "build container" now supports compiling projects using either Java&trade; 8 or Java&trade; 11. Support for Java&trade; 11 is provided by the Maven toolchains system.

* The number of environment variables per environment has been increased to 200.

* The Environment card on the Overview page now lists up to three environments. Users can select the **Show All** button to navigate to the Environment summary page to view a table with a complete list of environments.
   See [Viewing Environment](/help/implementing/cloud-manager/manage-environments.md#viewing-environment) for more details.

### Bug Fixes {#bug-fixes-cloud-manager}

* The link from Cloud Manager to the Developer Console was incorrectly active before environments were fully created.

* The link to the Developer Console directly from Cloud Manager did not display the option to de-hibernate/hibernate a Sandbox Program's environment.

* The Cancel and Save buttons on the Non-Production Pipeline Edit page were not always visible.

* Certain failures in the code quality process could result in the log file not being generated correctly.

* When creating a program, the suggested name would sometimes return a duplicate of an existing program name.

* Some large pipeline step logs could not be consistently downloaded through the user interface.

* The validation of environment names had an off-by-one error.

* The Environments page would sometimes show publish and Dispatcher segments when none was present.

## Adobe Experience Manager as a Cloud Service Foundation {#cloud-service-foundation}

### Workflows {#workflows}

* Support was added for searching workflow instances based on Workflow Title, Workflow Model, Status, Initiator, Payload Path and Start Date. See [Search Workflow Instances](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/sites/administering/workflows-administering.html).

## Content Transfer Tool {#content-transfer-tool}

Learn more about what is new and the updates for [Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/overview-content-transfer-tool.html) Release v1.1.12.

### What is New {#what-is-new-ctt}

* User experience for logs improved. Timestamps added to Extraction and Ingestion logs. Message added to indicate if logs are empty.

### Bug Fixes {#ctt-bug-fixes}

* Content Transfer Tool was skipping content files if the migration set contained paths that had partially similar file names.
