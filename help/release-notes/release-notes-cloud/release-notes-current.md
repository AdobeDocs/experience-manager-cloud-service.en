---
title: Release Notes for 2020.10.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: [!DNL Adobe Experience Manager] as a Cloud Service Release Notes for 2020.10.0.
---

# Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service 2020.10.0 {#release-notes}

The following section outlines the general Release Notes for [!DNL Experience Manager] as a Cloud Service 2020.10.0.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2020.10.0 is October 28, 2020.
The following release (2020.11.0) will be on November 26.

<!-- The release is moved to Wed, 28 Oct just this once.
-->

## [!DNL Adobe Experience Manager Assets] as a Cloud Service {#assets}

### What is new in [!DNL Assets] {#what-is-new-assets}

* Content to come

### Bugs Fixed {#bugs-fixed-assets}

Content to come

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What is New {#what-is-new-commerce}

* Released CIF Venia Reference Site - 2020.10.2 that includes the lastest CIF Core Components version v1.4.0. Refer to [CIF Venia Reference Site](https://github.com/adobe/aem-cif-guides-venia/releases/tag/venia-2020.10.2) for more details.

* Released CIF Core Components v1.4.0. Refer to [CIF Core Components](https://github.com/adobe/aem-core-cif-components/releases/tag/core-cif-components-reactor-1.4.0) for more details.

### Bug Fixes {#bug-fixes-commerce}

* GraphQL requests in the Product Console and Pickers were done via HTTP POST. This has been fixed to ensure that the Apollo GraphQL client respects the setting in the GraphQL client OSGi configuration to support GET requests if configured. 

* CIF Cloud config UI displayed "Save & Close" buttons for configs in /lib and /apps/. But these are read-only hence UI fixed to display "Close" button only.

## Content Transfer Tool {#content-transfer-tool}

Follow this section to learn about what is new and the updates for [Content Transfer Tool](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/overview-content-transfer-tool.html) Release v1.1.12.

### What is New {#what-is-new-ctt}

* User experience for logs improved. Timestamps added to Extraction and Ingestion logs. Message added to indicate if logs are empty.

### Bug Fixes {#ctt-bug-fixes}

* Content Transfer Tool was skipping content files if the migration set contained paths that had the partially similar file names. This has been fixed.



