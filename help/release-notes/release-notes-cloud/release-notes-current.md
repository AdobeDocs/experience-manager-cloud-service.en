---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
---

# Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for [!DNL Experience Manager] as a Cloud Service.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2020.12.0 is December 17, 2020.
The following release (2021.1.0) will be on January 28, 2021.

## [!DNL Adobe Experience Manager Sites] as a Cloud Service {#sites}

* **[Content Fragment HTTP API](/help/assets/content-fragments/assets-api-content-fragments.md)**: Add the ability to add/update and delete Content Fragment variations using the HTTP API.

## [!DNL Adobe Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

* [!DNL Experience Manager] as a [!DNL Cloud Service] extends the Smart Tags functionality to support the identification of keywords and entities in text-based assets. The text is identified, indexed, and is made available as metadata to improve the search experience without the need for any configuration. See [Smart Tags](/help/assets/smart-tags.md).

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What is New {#what-is-new-commerce}

* Released CIF Venia Reference Site - 2020.12.01 that includes the latest CIF Core Components version v1.6.0. Refer to [CIF Venia Reference Site](https://github.com/adobe/aem-cif-guides-venia/releases/tag/venia-2020.12.01) for more details.

* Released CIF Core Components v1.6.0. Refer to [CIF Core Components](https://github.com/adobe/aem-core-cif-components/releases/tag/core-cif-components-reactor-1.6.0) for more details.

## Cloud Manager {#cloud-manager}

### Release Date {#release-date-cm}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.1.0 is January 14, 2021.

### Bug Fixes {#bug-fixes-cloud-manager}

* Assets Production instance may on occasion, show the Brand Portal status on the **Environments** detail page as *Pending* without allowing the user to take any action.

* When triggering a de-hibernate from Cloud Manager, sometimes a failure message was displayed even when de-hibernation was started successfully. 

* Rare cases of failure encountered in environment creation or deletion has been addressed.

## Code Refactoring Tools {#code-refactoring-tools}

### What is new in [!DNL Code Refactoring Tools] {#what-is-new-crt}

* New version of AIO-CLI plugin released. Latest version of this plugin includes bug fixes for the AEM Dispatcher Converter and the Repository Modernizer and also supports a new utility - Index Converter. Please refer to [Unified Experience](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/refactoring-tools/unified-experience.html?lang=en#benefits) to learn more about this plugin. 

* Index Converter is a utility that can be used to transform a customer's Custom OAK Index Definitions to AEM as a CLoud Service compatible OAK Index Definitions. Please refer to [Index Converter](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/index-converter) for more details.

* New feature added to [Repository Modernizer](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/repository-modernizer) that creates a separate package `ui.config` to contain all OSGi configurations. 

### Bug Fixes {#crt-bug-fixes}

* Several bug fixes done on the AEM Dispatcher Converter and Repository Modernizer tools. Please refer to [AEM Dispatcher Converter](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/dispatcher-converter) and [Repository Modernizer](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/repository-modernizer).

## AEM as a Cloud Service Foundation {#aem-as-a-cloud-service-foundation}

### What is New {#what-is-new-foundation}

* Server-to-server authenticated API calls - Generate the appropriate access tokens to make authenticated server-to-server API calls between your external applications and AEM as a Cloud Service environments. [Learn more](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md).

### SDK Build Analyzers {#sdk-build-analyzers}

The AEM as a Cloud Service SDK Build Analyzer Maven Plugin detects problems in a maven project, including missing dependencies. It gives developers an opportunity to discover issues during local development, well before deploying to Cloud environments with Cloud Manager.

Two new analyzers have been added for this release:

* repoinit analyzer
* bundle-nativecode

For more information, see the documentation [here](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/build-analyzer-maven-plugin.html?lang=en#developing).

## Cloud Transition Tools {#code-transition-tools}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.1.20 is January 08, 2021.

### What is new in [!DNL Content Transfer Tool] {#what-is-new-ctt}

* Users can now learn if their Access Token has expired by hovering on the status icon in the Content Transfer Tool (CTT) user interface. They will also be notified in the Migration Set Details UI that they are unable to connect to their Cloud Service instance.

### Bug Fixes {#ctt-bug-fixes}

* Content Transfer Tool (CTT) user interface status for a migration set did not persist and changed after a period of inactivity. This has been fixed.
* Option to view logs was disabled if the logs were not available. This has been fixed and messaging has been added to notify user why logs are missing.
* Content Transfer Tool user interface status showed FAILED when user stopped an ingestion. This has been fixed to display *STOPPED* instead.
