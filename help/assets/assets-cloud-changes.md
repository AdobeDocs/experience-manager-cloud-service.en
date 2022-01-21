---
title: Notable changes in [!DNL Adobe Experience Manager Assets] as a [!DNL Cloud Service]
description: Notable changes to [!DNL Adobe Experience Manager Assets] in [!DNL Experience Manager] as a [!DNL Cloud Service] as compared to [!DNL Adobe Experience Manager] 6.5.
feature: Release Information
role: User,Leader,Architect,Admin
exl-id: 93e7dbcd-016e-4ef2-a1cd-c554efb5ad34
---
# Notable changes to [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#notable-changes}

[!DNL Adobe Experience Manager] as a [!DNL Cloud Service] brings many new features and possibilities to manage your Experience Manager projects. There are many differences between [!DNL Experience Manager Assets] on-premise or hosted as Adobe Managed Service as compared to [!DNL Experience Manager] as a [!DNL Cloud Service]. This article highlights the important differences for [!DNL Assets] capabilities.

The main differences as compared to [!DNL Experience Manager] 6.5 are in the following areas:

* [Asset ingestion, upload, and processing](#asset-ingestion).
* [Asset microservices for cloud-native processing](#asset-microservices).
* [Removal of Classic UI](#classic-ui).

## Asset ingestion, processing, and distribution {#asset-ingestion-distribution}

Asset upload is optimized for efficiency by enabling better scaling of ingestion, faster uploads, faster processing using microservices, and bulk ingestion. Product capabilities (web user interfaces, desktop clients) are updated. Also, this may impact some existing customizations.

* [!DNL Experience Manager] uses direct binary access principle to upload and download assets and uses asset microservices to process asset. See [overview of microservices](/help/assets/asset-microservices-overview.md).
  * Asset upload [with direct binary access](/help/assets/asset-microservices-overview.md#asset-upload-with-direct-binary-access).
  * For technical details, see [direct binary upload protocol and APIs](/help/assets/developer-reference-material-apis.md#upload-binary).
  * For a comparison of the available API methods for basic CRUD operations, see [APIs and asset operations](/help/assets/developer-reference-material-apis.md#use-cases-and-apis).
* The default workflow **[!UICONTROL DAM Asset Update]** in previous versions of [!DNL Experience Manager] is no longer available. Instead, asset microservices provide a scalable, readily available service that covers most of the default asset processing (renditions, metadata extraction, and text extraction for indexing).
  * See [configure and use asset microservices](/help/assets/asset-microservices-configure-and-use.md)
  * To have customized workflow steps in the processing, [post-processing workflows](/help/assets/asset-microservices-configure-and-use.md#post-processing-workflows) can be used.

* The website components that deliver a binary file without any transformation can use direct download. The Sling GET servlet is updated to let developers do this by default. The website components that deliver a binary with some transformation (for example, resize it via a servlet) can continue to operate as is.

The standard renditions generated with asset microservices are stored in a backward-compatible way in the asset repository nodes using the same naming conventions.

## Develop and test asset microservices {#asset-microservices}

Asset microservices provide a scalable and resilient processing of assets using cloud services. Adobe manages the cloud services for optimal handling of different asset types and processing options. Asset microservices help to avoid the need for third-party rendering tools and methods (like [!DNL ImageMagick]) and simplify configurations, while providing out-of-the-box functionality for common file types. You can now process a [broad range of file types](/help/assets/file-format-support.md) covering more formats out-of-the-box than what is possible with previous versions of Experience Manager. For example, thumbnail extraction of PSD and PSB formats is now possible that previously required third-party solutions such as [!DNL ImageMagick]. You cannot use the complex configurations of [!DNL ImageMagick] for the [!UICONTROL Processing Profiles] configuration. Use [!DNL Dynamic Media] for advanced FFmpeg transcoding of videos and use processing profiles for [basic transcoding of MP4 videos](/help/assets/manage-video-assets.md#transcode-video).

Asset microservices is a cloud-native service that is automatically provisioned and wired to [!DNL Experience Manager] in customer programs and environments managed in Cloud Manager. To extend or customize [!DNL Experience Manager], the developers can use the existing content or assets with renditions generated in a cloud environment, to test and validate their code using, displaying, downloading assets.

To do an end-to-end validation of the code and process including asset ingestion and processing, deploy the code changes to a cloud-dev environment using [the pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) and test with full execution of asset microservices processing.

## Feature parity with [!DNL Experience Manager] 6.5 {#cloud-service-feature-status}

[!DNL Experience Manager] as a [!DNL Cloud Service] introduces many new features and more performant ways for existing features to work. However, when moving from [!DNL Experience Manager] 6.5 to [!DNL Experience Manager] as a [!DNL Cloud Service], you may notice that some features either work differently, are not available, or are available partially. The following is a list of such features. In addition, see the [deprecated and removed features](/help/release-notes/deprecated-removed-features.md).

| Functionality or use case | Status in [!DNL Experience Manager] as a [!DNL Cloud Service] | Comments |
|-----|-----|-----|
| [Duplicate asset detection](/help/assets/manage-digital-assets.md#detect-duplicate-assets) | Works differently | See [how it worked in [!DNL Experience Manager] 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/managing/duplicate-detection.html). |
| [For Placement Only (FPO) renditions](/help/assets/configure-fpo-renditions.md) | Works differently | Processing Profiles use asset microservices to generate FPO renditions. In Experience Manager 6.5, a third-party solution such as [!DNL ImageMagick] was available to generate the renditions. |
| Metadata writeback | Works differently | Disabled by default. Enable the corresponding workflow launcher if needed. Writeback is handled by asset microservices. |
| Processing of assets uploaded using Package Manager | Needs manual intervention | Manually reprocess using the **[!UICONTROL Reprocess Asset]** action. |
| MIME type detection | Not supported. | If you upload a digital asset without an extension or with an incorrect extension, it may not be processed as desired. Users can still store the binary files without an extension in the DAM. See [MIME type detection in [!DNL Experience Manager] 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/administer/detect-asset-mime-type-with-tika.html). |
| Subasset generation for a compound assets | Not supported. | Dependent use cases like annotations may not be fulfilled. See [subasset creation in [!DNL Experience Manager] 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/managing/managing-linked-subassets.html#generate-subassets). PDF preview of some file types is available starting [2021.7.0 release](/help/release-notes/release-notes-cloud/release-notes-current.md). |
| Edit images |Not supported | Editing assets is not supported in Experience Manager as a Cloud Service. See [how it worked in Experience Manager 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/managing/manage-assets.html#editing-images). |
| Home page | Not supported | See [[!DNL Assets] Home Page experience in [!DNL Experience Manager] 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/using/assets-home-page.html) |
| Extract assets from ZIP archive | Not supported | See [ZIP extraction in [!DNL Experience Manager] 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/managing/manage-assets.html#extractzip). |
| Assets ratings | Not supported | The rating widget in the metadata schema editor is not supported. |
| Content disposition filter | Not supported | A popular use case of `ContentDispositionFilter` is to let administrators configure [!DNL Experience Manager] to serve HTML files and to open PDF files inline instead of downloading those. On the Publish instances, you can manage the disposition using Dispatcher configuration. On the Author instances, Adobe does not recommend modification to the Content Disposition header. See [Content Disposition filter in [!DNL Experience Manager] 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/content-disposition-filter.html). |
| [Download report](/help/assets/asset-reports.md) | Not supported | For now, the download report that informs of asset use is not available. See [download report in [!DNL Experience Manager] 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/administer/asset-reports.html). |
| Product photoshoot template | Not supported | See [product photoshoot template in [!DNL Experience Manager] 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/authoring/projects/managing-product-information.html). |
| Smart Translation | Not supported| [Smart translation](https://experienceleague.adobe.com/docs/experience-manager-learn/assets/translation/smart-translation-search-feature-video-use.html) is not supported in [!DNL Experience Manager] as a [!DNL Cloud Service]. |
| WebDAV | Not supported | For alternatives, see [[!DNL Creative Cloud] integration](/help/assets/aem-cc-integration-best-practices.md) or [Developer reference material](/help/assets/developer-reference-material-apis.md). |
| Classic UI | Not supported | Only Touch-enabled user interface is available. |

>[!MORELIKETHIS]
>
>The following resources are available for [!DNL Experience Manager] as a [!DNL Cloud Service]:
>
>* [List of deprecated and removed features](/help/release-notes/deprecated-removed-features.md)
>* [An introduction](/help/overview/introduction.md)
>* [What is new and different](/help/overview/what-is-new-and-different.md)
>* [The architecture](/help/overview/architecture.md)
>* [Notable changes](/help/release-notes/aem-cloud-changes.md)
>* [Notable changes [!DNL Sites]](/help/sites-cloud/sites-cloud-changes.md)
>* [Video tutorials](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/overview.html)
