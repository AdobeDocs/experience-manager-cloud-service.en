---
title: Notable changes in Adobe Experience Manager Assets as a Cloud Service
description: Notable Changes to Adobe Experience Manager Assets in AEM Cloud Service as compared to Experience Manager 6.5
---

# Notable changes to Experience Manager Assets as a Cloud Service {#notable-changes}

Adobe Experience Manager as a Cloud Service brings many new features and possibilities to manage your AEM projects. However, there are a number of differences between Experience Manager Assets on-premise or in Adobe Managed Service as compared to Experience Manager as a Cloud Service. This document highlights the important differences.

>[!NOTE]
>
>This document highlights the notable changes that are specific to Experience Manager Assets as a Cloud Service. See the generic [changes to Experience Manager as a Cloud Service](/help/release-notes/aem-cloud-changes.md).

The main differences as compared to Experience Manager 6.5 are in the following areas:

* [Asset ingestion](#asset-ingestion)
* [Removal of Classic UI](#classic-ui)

## Asset ingestion {#asset-ingestion}

Asset upload has been optimized to be more efficient enabling better scaling of asset ingestion and faster uploads. Product capabilities (web user interfaces, desktop clients) have been updated. However, this may impact some existing custom code.

* Experience Manager uses direct binary access principle for upload and download and asset microservices for asset processing. See [overview of asset ingestion](/help/assets/asset-microservices-overview.md)
  * Asset upload [with direct binary access](/help/assets/asset-microservices-overview.md#asset-upload-with-direct-binary-access)
  * For technical details, see  of [direct binary upload protocol and APIs](/help/assets/developer-reference-material-apis.md#overview-binary-upload)
* The default workflow **[!UICONTROL DAM Asset Update]** in previous versions of AEM is no longer available. Instead, asset microservices provide a scalable, readily available service that covers most of the default asset processing (renditions, metadata extraction, text extraction for indexing)
  * See [configuring and using asset microservices](/help/assets/asset-microservices-configure-and-use.md)
  * To have customized workflow steps in the processing, [post-processing workflows](/help/assets/asset-microservices-configure-and-use.md#post-processing-workflows) can be used
* Assets that come in via Package Manager require manual re-processing using the **[!UICONTROL Reprocess Asset]** action in the Assets interface.

Standard renditions generated with asset microservices are stored in a backwards-compatible way in the asset repository nodes (same naming conventions).

## Develop and test asset microservices {#developing-testing-asset-microservices}

Asset microservices is a native cloud service that is automatically provisioned and wired to Experience Manager in customer programs and environments managed in Cloud Manager. Developers working to extend Experience Manager or do customization can use the existing content (or assets with renditions generated in a cloud environment) to test and validate their code using, displaying, downloading assets.

To do an end-to-end validation of the code and process including asset ingestion and processing, deploy the code changes to a cloud-dev environment using the pipeline and test with full execution of asset microservices processing.

## Removal of Classic UI {#classic-ui}

The Classic UI is no longer available in Experience Manager as a Cloud Service.
