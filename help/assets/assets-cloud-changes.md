---
title: Notable changes in Adobe Experience Manager Assets as a [!DNL Cloud Service]
description: Notable changes to Adobe Experience Manager Assets in AEM [!DNL Cloud Service] as compared to Adobe Experience Manager 6.5.
---

# Notable changes to Experience Manager Assets as a [!DNL Cloud Service] {#notable-changes}

Adobe Experience Manager as a [!DNL Cloud Service] brings many new features and possibilities to manage your AEM projects. However, there are many differences between Experience Manager Assets on-premise or in Adobe Managed Service as compared to Experience Manager as a [!DNL Cloud Service]. This document highlights the important differences for Assets capabilities. 

The main differences as compared to Experience Manager 6.5 are in the following areas:

* [Asset ingestion and upload](#asset-ingestion).
* [Asset microservices for cloud-native processing](#asset-microservices).
* [Removal of Classic UI](#classic-ui).

>[!NOTE]
>
>This document highlights the notable changes to AEM Assets. For changes general to Experience Manager as a [!DNL Cloud Service], and other modules, see:
>
>* [An Introduction to Adobe Experience Manager as a [!DNL Cloud Service]](/help/overview/introduction.md)
>* An [Overview of AEM as a [!DNL Cloud Service] - What is New and What is Different](/help/overview/what-is-new-and-different.md)
>* The [Architecture](/help/core-concepts/architecture.md) of Adobe Experience Manager as a [!DNL Cloud Service]
>* [Notable changes to AEM as a [!DNL Cloud Service] (Release Notes)](/help/release-notes/aem-cloud-changes.md)
>* [Notable changes to AEM Sites as a [!DNL Cloud Service]](/help/sites-cloud/sites-cloud-changes.md)
>* [Adobe Experience Manager as a [!DNL Cloud Service] Tutorials](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/overview.html)

## Asset ingestion and upload {#asset-ingestion}

Asset upload has been optimized for efficiency by enabling better scaling of asset ingestion and faster uploads. Product capabilities (web user interfaces, desktop clients) have been updated. However, this may impact some existing customization.

* Experience Manager uses direct binary access principle for upload and download and asset microservices for asset processing. See [overview of asset ingestion](/help/assets/asset-microservices-overview.md).
  * Asset upload [with direct binary access](/help/assets/asset-microservices-overview.md#asset-upload-with-direct-binary-access).
  * For technical details, see  of [direct binary upload protocol and APIs](/help/assets/developer-reference-material-apis.md#upload-binary).
* The default workflow **[!UICONTROL DAM Asset Update]** in previous versions of AEM is no longer available. Instead, asset microservices provide a scalable, readily available service that covers most of the default asset processing (renditions, metadata extraction, text extraction for indexing).
  * See [configuring and using asset microservices](/help/assets/asset-microservices-configure-and-use.md)
  * To have customized workflow steps in the processing, [post-processing workflows](/help/assets/asset-microservices-configure-and-use.md#post-processing-workflows) can be used.
* Assets that come in via Package Manager require manual reprocessing using the **[!UICONTROL Reprocess Asset]** action in the Assets interface.

Standard renditions generated with asset microservices are stored in a backwards-compatible way in the asset repository nodes (same naming conventions).

## Develop and test asset microservices {#asset-microservices}

Asset microservices provide a scalable and resilient processing of assets using cloud services. Adobe manages the cloud services for optimal handling of different asset types and processing options. Asset microservices help to avoid the need for third-party rendering tools and methods (like ImageMagick) and simplify configurations, while providing out-of-the-box functionality for common file types. You can now process a [broad range of file types](/help/assets/file-format-support.md) covering more formats out-of-the-box than what is possible with previous versions of Experience Manager. For example, thumbnail extraction of PSD and PSB formats is now possible that previously required third-party solutions like ImageMagick. You cannot use the complex configurations of ImageMagick for the [!UICONTROL Processing Profiles] configuration. Use [!DNL Dynamic Media] for advanced FFmpeg transcoding of videos and use processing profiles for [basic transcoding of MP4 videos](/help/assets/manage-video-assets.md#transcode-video).

Asset microservices is a cloud-native service that is automatically provisioned and wired to Experience Manager in customer programs and environments managed in Cloud Manager. To extend or customize Experience Manager, the developers can use the existing content or assets with renditions generated in a cloud environment, to test and validate their code using, displaying, downloading assets.

To do an end-to-end validation of the code and process including asset ingestion and processing, deploy the code changes to a cloud-dev environment using [the pipeline](/help/implementing/cloud-manager/configure-pipeline.md) and test with full execution of asset microservices processing.

## Removal of Classic UI {#classic-ui}

The Classic UI is no longer available in Experience Manager as a [!DNL Cloud Service]. The standard interface is the Touch-enabled UI.
