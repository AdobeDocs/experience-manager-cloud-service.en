---
title: Notable Changes to AEM Assets in AEM Cloud Service
seo-title: Notable Changes to AEM Assets in AEM Cloud Service
description: Notable Changes to AEM Assets in AEM Cloud Service 
seo-description: Notable Changes to AEM Assets in AEM Cloud Service
---

<!-- @asgutpa - please note this document replaces the draft help/assets/compare-with-aem.md, which I removed as a part of PR -->

# Notable changes to AEM Assets in AEM Cloud Service {#notable-changes}

AEM Cloud Service brings many new features and possibilities for managing your AEM projects. However there are a number of differences between AEM Assets on premise or in Adobe Managed Service as compared to AEM Cloud Service. This document highlights the important differences.

>[!NOTE]
>This document highlights the notable changes to AEM Assets. For changes general to AEM in the Cloud see:
>
>* [Notable Changes to Adobe Experience Manager (AEM) as a Cloud Service](/help/release-notes/aem-cloud-changes.md)

The main differences are found in the following areas:

* [Asset ingestion](#asset-ingestion)
* [Removal of Classic UI](#classic-ui)


## Asset ingestion {#asset-ingestion}

Asset upload has been optimized in AEM Cloud Service to be more efficient enabling better scaling of asset ingestion and faster uploads. Product capabilities (web user interfaces, desktop clients) have been updated. However, this may impact some existing custom code.

* AEM as a Cloud Service uses direct binary access principle for upload and download and asset microservices for asset processing. See [overview of asset ingestion](help/assets/asset-microservices-overview.md)
  * Asset upload [with direct binary access](help/assets/asset-microservices-overview.md#asset-upload-with-direct-binary-access)
  * For technical details, see  of [direct binary upload protocol and APIs](help/assets/developer-reference-material-apis.md#overview-binary-upload)
* The default workflow **DAM Asset Update** in previous versions of AEM is no longer available. Instead, asset microservices provide a scalable, readily available service that covers most of the default asset processing (renditions, metadata extraction, text extraction for indexing)
  * See [configuring and using asset microservices](help/assets/asset-microservices-configure-and-use.md)
  * To have customized workflow steps in the processing, [post-processing worfklows](help/assets/asset-microservices-configure-and-use.md#post-processing-workflows) can be used
* Assets that come in via Package Manager require manual re-processing using the  **Reprocess Asset** action in the Assets UI.

Standard renditions generated with asset microservices are stored in a backwards-compatible way in the asset repository nodes (same naming conventions).

## Developing and testing asset microservices {#developing-tesing-asset-microservices}

Asset microservices is a native cloud service that is automatically provisioned and wired to Experience Manager in customer programs and environments managed in Cloud Manager. Developers working with AEM as a Cloud Service SDK locally can use existing content (or assets with renditions generated in a cloud environment) to test and validate their code using, displaying, downloading assets.

To do full end to end validation of the code and process including asset ingestion and processing, code changes should be deployed to a cloud dev environment using pipeline and tested with full execution of asset microservices processing.

## Removal of Classic UI {#classic-ui}

The Classic UI is no longer available in AEM Cloud Service.
