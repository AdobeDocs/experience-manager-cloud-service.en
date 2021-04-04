---
title: Release Notes for 2020.9.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: [!DNL Adobe Experience Manager] as a Cloud Service Release Notes for 2020.9.0.
exl-id: 2332512f-8c52-4569-a006-faa36a7670a1
---
# Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service 2020.9.0 {#release-notes}

The following section outlines the general Release Notes for [!DNL Experience Manager] as a Cloud Service 2020.9.0.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2020.9.0 is September 24, 2020.

## [!DNL Adobe Experience Manager Sites] as a Cloud Service {#sites}

### What is new in [!DNL Sites] {#what-is-new-sites}

* The Single Page Application (SPA) Editor JavaScript SDK [is now open source.](/help/implementing/developing/hybrid/reference-materials.md)

## [!DNL Adobe Experience Manager Assets] as a Cloud Service {#assets}

### What is new in [!DNL Assets] {#what-is-new-assets}

* Watermarking image files is supported for renditions generated with asset microservices. It can be configured as a Processing Profile and uses a PNG file as a watermark. See [watermark your assets](/help/assets/watermark-assets.md).

* Enhancements in [!DNL Dynamic Media]

  * Selective Publish - It is now possible for a marketing team to access [!DNL Dynamic Media] smart crop images and dynamic renditions that are synchronized to [!DNL Dynamic Media] so they can create promotional materials, all without the need to publish those assets to [!DNL Dynamic Media] for global delivery. [!DNL Experience Manager] and [!DNL Dynamic Media] publishing is decoupled and can occur separately to achieve this. See [selective publish](/help/assets/dynamic-media/selective-publishing.md).
  * Administrators can now reset [!DNL Dynamic Media] Cloud Service password that is received on provisioning. The reset can be done in [!DNL Experience Manager] user interface, without the need to use the [!DNL Dynamic Media Classic] desktop app.

* To know about the following enhancements, see [what is new in Brand Portal](https://docs.adobe.com/content/help/en/experience-manager-brand-portal/using/introduction/whats-new.html).
  
  * Enhanced PDF preview with Adobe Document Cloud View SDK integration.
  * Single-click download functionality.
  * New administration configurations for the download experience.

<!--
### Bugs Fixed {#bugs-fixed-assets}

TBD: list of Assets aaCS bugs that are fixed.
-->

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What is New {#what-is-new-commerce}

* Released CIF Core Components v1.3.0. Refer to [CIF Core Components](https://github.com/adobe/aem-core-cif-components/releases/tag/core-cif-components-reactor-1.3.0) for more details.

* Preview capability with product/category for product and category templates is now available. This allows business users/marketers in AEM to view the product/category templates with real data.

* Properties page added to products and categories to allow business users to view details associated with the product SKU/category id.

* Sorting feature added to Product Console to allow sorting of products/categories by name or price attributes.

* Product search functionality added to Product Console.

### Bug Fixes {#bug-fixes-commerce}

* Commerce Cloud configurations did not respect inheritance. This has been fixed to ensure that configuration inherits values.

## Cloud Manager {#cloud-manager}

### Release Date {#release-date-cm}

The Release Date for [!UICONTROL Cloud Manager] Version 2020.9.0 is September 03, 2020.

### What's New {#what-is-new-cloud-manager}

* Content Audit has been relabeled as Experience Audit.
* The build process has been separated into three separate Maven commands.
* If the Git Repository fails to be cloned, it will be reattempted up to three times.

### Bug Fixes {#bug-fixes-cm}

* The Content Audit tab incorrectly displayed the base URL using the author domain instead of the publish domain.

## Cloud Readiness Analyzer {#cloud-readiness-analyzer}

Follow this section to learn about what is new and the updates for Cloud Readiness Analyzer Release v1.1.0.

### What is New {#what-is-new-cra}

* The Cloud Readiness Analyzer (CRA) has a start state console that displays an explicit **Generate Report** button for the user to click to execute the CRA.

* The CRA UI displays progress while it is running. It displays items being analyzed and findings found during execution.

* The CRA report displays a summary and the number of the findings in a tabular format organized by the type of finding and the importance level. Clicking on the number of that finding will automatically scroll to the location of that finding in the report.

### Bug Fixes {#cra-bug-fixes}

* In certain cases, the CRA report was not getting updated after forcing a refresh. This has been fixed in this version.

## Content Transfer Tool {#content-transfer-tool}

Follow this section to learn about what is new and the updates for Content Transfer Tool Release v1.1.10.

### What is New {#what-is-new-ctt}

* The Content Transfer Tool (CTT) supports Azure Blob Store Data Store.

* The CTT user interface has an auto-reload feature that reloads the overview page every 30 seconds.

* Button added to CTT user interface to retrieve *Access Token* easily.

* Descriptive validation message added for *URL* and *Migration Set Name*.

## Code Refactoring Tools {#code-refactoring}

Follow this section to learn about what is new and the updates for Code Refactoring Tools.

### What is New {#what-is-new-refactoring}

* AIO-CLI plugin supports Repository Modernizer and allows users to execute the tool using the plugin. 

  Refer to [Git Resource: aio-cli-plugin-aem-cloud-service-migration](https://github.com/adobe/aio-cli-plugin-aem-cloud-service-migration) for more details.

* Repository Modernizer utility can be used to restructure existing project packages into packages compatible with the project structure defined for AEM as a Cloud Service. 

  Refer to [Git Resource: Repository Modernizer](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/repository-modernizer) for more details.
