---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
---

# Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for [!DNL Experience Manager] as a Cloud Service.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2020.11.0 is December 17, 2020.
The following release (2020.12.0) will be on January xx, 2020

## [!DNL Adobe Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

* Integration with [!DNL Adobe InDesign Server] lets users use [!DNL Assets] templates user interface to create brochures or ads. It supports high-fidelity, multi-page previews of INDD file type. Full-text search is supported as [!DNL Experience Manager] extracts and indexes full text. <!-- TBD: Add link to article. -->

* [!DNL Experience Manager] desktop app lets users upload digital assets by dragging from Windows Explorer or Mac Finder. See [add assets using desktop app](https://experienceleague.adobe.com/docs/experience-manager-desktop-app/using/using.html#upload-and-add-new-assets-to-aem).

* [!DNL Experience Manager] is enhanced to track and display asset references when an asset is used in a remote [!DNL Experience Manager Sites] deployment using the Connected Assets functionality. A new [!UICONTROL References] tab in asset's [!UICONTROL Properties] page now lists local and remote references of the asset. The references let DAM users track asset usage in [!DNL Sites] pages and in compound assets in [!DNL Assets]. <!-- TBD: Add link to article. -->

* [!DNL Dynamic Media] capabilities are now accessible via [!DNL Sites] image-based Core Components. Authors can quickly configure components to use Image Presets, Smart Crop, and Image Modifiers when creating webpages. <!-- TBD: Add link to article. -->

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What is New {#what-is-new-commerce}

* Released CIF Venia Reference Site - 2020.12.01 that includes the lastest CIF Core Components version v1.6.0. Refer to [CIF Venia Reference Site](https://github.com/adobe/aem-cif-guides-venia/releases/tag/venia-2020.12.01) for more details.

* Released CIF Core Components v1.6.0. Refer to [CIF Core Components](https://github.com/adobe/aem-core-cif-components/releases/tag/core-cif-components-reactor-1.6.0) for more details.

## Cloud Manager {#cloud-manager}

### Release Date {#release-date-cm}

The Release Date for Cloud Manager in AEM as a Cloud Service 2020.12.0 is December 10, 2020.

### What is new in [!DNL Cloud Manager] {#what-is-new-cm}

* Self service management of [SSL Certificates](/help/implementing/cloud-manager/managing-ssl-certifications/introduction.md) and [Custom Domain Names](/help/implementing/cloud-manager/custom-domain-names/introduction.md).

* Self service management of [IP Allow Lists](/help/implementing/cloud-manager/ip-allow-lists/introduction.md).

* Updated **Environment** details page now allows users to manage Custom Domain Names and IP Allow Lists on their environments.

### Bug Fixes {#bug-fixes-cloud-manager}

* Some occurrences of failures at code scanning stage without providing results addressed.

* Environment card did not consistently display **Add** button.

## Code Refactoring Tools {#code-refactoring-tools}

### What is new in [!DNL Code Refactoring Tools] {#what-is-new-crt}

* New version of AIO-CLI plugin released. Latest version of this plugin includes bug fixes for the AEM Dispatcher Converter and the Repository Modernizer and also supports a new utility - Index Converter. Please refer to [Unified Experience](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/refactoring-tools/unified-experience.html?lang=en#benefits) to learn more about this plugin. 

* Index Converter is a utility that can be used to transform a customer's Custom OAK Index Definitions to AEM as a CLoud Service compatible OAK Index Definitions. Please refer to [Index Converter](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/index-converter) for more details.

* New feature added to [Repository Modernizer](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/repository-modernizer) that creates a separate package `ui.config` to contain all OSGi configurations. 

### Bug Fixes {#crt-bug-fixes}

* Several bug fixes done on the AEM Dispatcher Converter and Repository Modernizer tools. Please refer to [AEM Dispatcher Converter](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/dispatcher-converter) and [Repository Modernizer](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/repository-modernizer).
