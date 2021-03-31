---
title: Notable changes in [!DNL Adobe Experience Manager Assets] as a [!DNL Cloud Service]
description: Notable changes to [!DNL Adobe Experience Manager Assets] in [!DNL Experience Manager] as a [!DNL Cloud Service] as compared to [!DNL Adobe Experience Manager 6.5.
---

# Notable changes to [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#notable-changes}

[!DNL Adobe Experience Manager] as a [!DNL Cloud Service] brings many new features and possibilities to manage your Experience Manager projects. There are many differences between [!DNL Experience Manager Assets] on-premise or hosted as Adobe Managed Service as compared to [!DNL Experience Manager] as a [!DNL Cloud Service]. This article highlights the important differences for [!DNL Assets] capabilities.

The main differences as compared to [Experience Manager] 6.5 are in the following areas:

* [Asset ingestion, upload, and processing](#asset-ingestion).
* [Asset microservices for cloud-native processing](#asset-microservices).
* [Removal of Classic UI](#classic-ui).

## Asset ingestion and processing {#asset-ingestion}

Asset upload is optimized for efficiency by enabling better scaling of ingestion, faster uploads, faster processing using microservices, and bulk ingestion. Product capabilities (web user interfaces, desktop clients) are updated. Also, this may impact some existing customizations.

* [!DNL Experience Manager] uses direct binary access principle to upload and download assets and uses asset microservices to process asset. See [overview of microservices](/help/assets/asset-microservices-overview.md).
  * Asset upload [with direct binary access](/help/assets/asset-microservices-overview.md#asset-upload-with-direct-binary-access).
  * For technical details, see [direct binary upload protocol and APIs](/help/assets/developer-reference-material-apis.md#upload-binary).
  * For a comparison of the available API methods for basic CRUD operations, see [APIs and asset operations](/help/assets/developer-reference-material-apis.md#use-cases-and-apis).
* The default workflow **[!UICONTROL DAM Asset Update]** in previous versions of [!DNL Experience Manager] is no longer available. Instead, asset microservices provide a scalable, readily available service that covers most of the default asset processing (renditions, metadata extraction, and text extraction for indexing).
  * See [configure and use asset microservices](/help/assets/asset-microservices-configure-and-use.md)
  * To have customized workflow steps in the processing, [post-processing workflows](/help/assets/asset-microservices-configure-and-use.md#post-processing-workflows) can be used.

The standard renditions generated with asset microservices are stored in a backward-compatible way in the asset repository nodes using the same naming conventions.

## Develop and test asset microservices {#asset-microservices}

Asset microservices provide a scalable and resilient processing of assets using cloud services. Adobe manages the cloud services for optimal handling of different asset types and processing options. Asset microservices help to avoid the need for third-party rendering tools and methods (like ImageMagick) and simplify configurations, while providing out-of-the-box functionality for common file types. You can now process a [broad range of file types](/help/assets/file-format-support.md) covering more formats out-of-the-box than what is possible with previous versions of Experience Manager. For example, thumbnail extraction of PSD and PSB formats is now possible that previously required third-party solutions like ImageMagick. You cannot use the complex configurations of ImageMagick for the [!UICONTROL Processing Profiles] configuration. Use [!DNL Dynamic Media] for advanced FFmpeg transcoding of videos and use processing profiles for [basic transcoding of MP4 videos](/help/assets/manage-video-assets.md#transcode-video).

Asset microservices is a cloud-native service that is automatically provisioned and wired to [!DNL Experience Manager] in customer programs and environments managed in Cloud Manager. To extend or customize [!DNL Experience Manager], the developers can use the existing content or assets with renditions generated in a cloud environment, to test and validate their code using, displaying, downloading assets.

To do an end-to-end validation of the code and process including asset ingestion and processing, deploy the code changes to a cloud-dev environment using [the pipeline](/help/implementing/cloud-manager/configure-pipeline.md) and test with full execution of asset microservices processing.


## Feature parity with [!DNL Experience Manager] 6.5 {#cloud-service-feature-status}

[!DNL Experience Manager] as a [!DNL Cloud Service] introduces many new features and more performant ways for existing features to work. However, when moving from [!DNL Experience Manager] 6.5 to [!DNL Experience Manager] as a [!DNL Cloud Service], you may notice that some features either work differently, are not available, or are available partially. The following is a list of such features:

| Functionality or use case | Status in [!DNL Experience Manager] as a [!DNL Cloud Service] | Comments |
|-----|-----|-----|
| [Duplicate asset detection](/help/assets/manage-digital-assets.md#detect-duplicate-assets) | Works differently. | See [how it worked in [!DNL Experience Manager] 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/managing/duplicate-detection.html). |
| [For Placement Only (FPO) renditions](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/configure-aem-assets-for-asset-link.ug.html#configfporendition) | Works differently | |
| Metadata writeback | Not supported. | See [metadata writeback in [!DNL Experience Manager] 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/administer/xmp-writeback.html) |
| Processing of assets uploaded using Package Manager | Needs manual intervention. | Manually reprocess using the **[!UICONTROL Reprocess Asset]** action. |
| MIME type detection | Not supported. | If you upload a digital asset without an extension or with an incorrect extension, it may not be processed as desired. Users can still store the binary files without an extension in the DAM. See [MIME type detection in [!DNL Experience Manager] 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/administer/detect-asset-mime-type-with-tika.html). |
| Subasset generation for compound assets | Not supported. | Dependent use cases are not fulfilled. For example, annotation of multi-page PDF files is impacted. See [subasset creation in [!DNL Experience Manager] 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/managing/managing-linked-subassets.html#generate-subassets). |
| Home page | Not supported. | See [[!DNL Assets] Home Page experience in [!DNL Experience Manager] 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/using/assets-home-page.html) |
| Extract assets from ZIP archive | Not supported. | See [ZIP extraction in [!DNL Experience Manager] 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/managing/manage-assets.html#extractzip). |
| Classic UI | Not supported. | Only Touch-enabled UI is available. |

>[!MORELIKETHIS]
>
>The following resources are available for [!DNL Experience Manager] as a [!DNL Cloud Service]:
>
>* [List of deprecated and removed features](/help/release-notes/deprecated-removed-features.md)
>* [An introduction](/help/overview/introduction.md)
>* [What is new and different](/help/overview/what-is-new-and-different.md)
>* [The architecture](/help/core-concepts/architecture.md)
>* [Notable changes](/help/release-notes/aem-cloud-changes.md)
>* [Notable changes [!DNL Sites]](/help/sites-cloud/sites-cloud-changes.md)
>* [Video tutorials](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/overview.html)
