---
title: Release Notes for 2020.9.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: [!DNL Adobe Experience Manager] as a Cloud Service Release Notes for 2020.9.0.
---

# Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service 2020.9.0 {#release-notes}

The following section outlines the general Release Notes for Experience Manager as a Cloud Service 2020.9.0.

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What's New {#what-is-new-commerce}

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
