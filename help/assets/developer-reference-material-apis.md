---
title: Developer references for [!DNL Assets]
description: "[!DNL Assets] APIs and developer reference content lets you manage assets, including binary files, metadata, renditions, comments, and [!DNL Content Fragments]."
contentOwner: AG
feature: APIs,Assets HTTP API
role: Developer,Architect,Admin
exl-id: c75ff177-b74e-436b-9e29-86e257be87fb
---
# [!DNL Adobe Experience Manager Assets] developer use cases, APIs, and reference material {#assets-cloud-service-apis}

The article contains recommendations, reference materials, and resources for developers of [!DNL Assets] as a [!DNL Cloud Service]. It includes new asset upload module, API reference, and information about the support provided in post-processing workflows.

## [!DNL Experience Manager Assets] APIs and operations {#use-cases-and-apis}

[!DNL Assets] as a [!DNL Cloud Service] provides several APIs to programmatically interact with digital assets. Each API supports specific use cases, as mentioned in the table below. The [!DNL Assets] user interface, [!DNL Experience Manager] desktop app and [!DNL Adobe Asset Link] support all or some of the operations.

>[!CAUTION]
>
>Some APIs continue to exist but are not actively supported (denoted with an &times;). To the extent possible, do not use these APIs.

| Support level |         Description         |
| ------------- | --------------------------- |
| &#10003;      | Supported                   |
| &times;       | Not supported. Do not use.  |
| -             | Not available               |

| Use case | [aem-upload](https://github.com/adobe/aem-upload) | [Experience Manager / Sling / JCR](https://www.adobe.io/experience-manager/reference-materials/cloud-service/javadoc/index.html) Java APIs | [Asset compute service](https://experienceleague.adobe.com/docs/asset-compute/using/extend/understand-extensibility.html) | [[!DNL Assets] HTTP API](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/assets/admin/mac-api-assets.html#create-an-asset) | Sling [GET](https://sling.apache.org/documentation/bundles/rendering-content-default-get-servlets.html) / [POST](https://sling.apache.org/documentation/bundles/manipulating-content-the-slingpostservlet-servlets-post.html) servlets | [GraphQL](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/graphql/overview.html) |
| ----------------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Original binary** |||||||
| Create original    |&#10003;|&times;|-|&times;|&times;|-|
| Read original      |-|&times;|&#10003;|&#10003;|&#10003;|-|
| Update original    |&#10003;|&times;|&#10003;|&times;|&times; |-|
| Delete original    |-|&#10003;|-|&#10003;|&#10003;|-|
| Copy original      |-|&#10003;|-|&#10003;|&#10003;|-|
| Move original      |-|&#10003;|-|&#10003;|&#10003;|-|
| **Metadata** |||||||
| Create metadata    |-|&#10003;|&#10003;|&#10003;|&#10003;|-|
| Read metadata      |-|&#10003;|-|&#10003;|&#10003;|-|
| Update metadata    |-|&#10003;|&#10003;|&#10003;|&#10003;|-|
| Delete metadata    |-|&#10003;|&#10003;|&#10003;|&#10003;|-|
| Copy metadata      |-|&#10003;|-|&#10003;|&#10003;|-|
| Move metadata      |-|&#10003;|-|&#10003;|&#10003;|-|
| **Content Fragments (CF)** |||||||
| Create CF          |-|&#10003;|-|&#10003;|-|-|
| Read CF            |-|&#10003;|-|&#10003;|-|&#10003;|
| Update CF          |-|&#10003;|-|&#10003;|-|-|
| Delete CF          |-|&#10003;|-|&#10003;|-|-|
| Copy CF            |-|&#10003;|-|&#10003;|-|-|
| Move CF            |-|&#10003;|-|&#10003;|-|-|
| **Versions** |||||||
| Create version     |&#10003;|&#10003;|-|-|-|-|
| Read version       |-|&#10003;|-|-|-|-|
| Delete version     |-|&#10003;|-|-|-|-|
| **Folders** |||||||
| Create folder      |&#10003;|&#10003;|-|&#10003;|-|-|
| Read folder        |-|&#10003;|-|&#10003;|-|-|
| Delete folder      |&#10003;|&#10003;|-|&#10003;|-|-|
| Copy folder        |&#10003;|&#10003;|-|&#10003;|-|-|
| Move folder        |&#10003;|&#10003;|-|&#10003;|-|-|

## Asset upload {#asset-upload}

In [!DNL Experience Manager] as a [!DNL Cloud Service], you can directly upload the assets to the cloud storage using HTTP API. The steps to upload a binary file are below. Execute these steps in an external application and not within the [!DNL Experience Manager] JVM.

1. [Submit an HTTP request](#initiate-upload). It informs [!DNL Experience Manage]r deployment of your intent to upload a new binary.
1. [PUT the contents of the binary](#upload-binary) to one or more URIs provided by the initiation request.
1. [Submit an HTTP request](#complete-upload) to inform the server that the contents of the binary were successfully uploaded.

![Overview of direct binary upload protocol](assets/add-assets-technical.png)

>[!IMPORTANT]
>
>Execute the above steps in an external application and not within the [!DNL Experience Manager] JVM.

The approach provides a scalable and more performant handling of asset uploads. The differences as compared to [!DNL Experience Manager] 6.5 are:

* Binaries do not go through [!DNL Experience Manager], which is now simply coordinating the upload process with the binary cloud storage configured for the deployment.
* Binary cloud storage works with a Content Delivery Network (CDN) or Edge network. A CDN selects an upload endpoint that is nearer for a client. When data travels a shorter distance to a nearby endpoint, the upload performance and user experience improve, especially for geographically distributed teams.

>[!NOTE]
>
>See the client code to implement this approach in the open-source [aem-upload library](https://github.com/adobe/aem-upload).
>
>[!IMPORTANT]
>
>In certain circumstances, changes may not fully propagate between requests to Experience Manager due to eventually consistent nature of the storage in Cloud Service. This leads to 404 responses to initiate or complete upload calls due to the requisite folder creations not being propagated. Clients should expect 404 responses and handle them by implementing a retry with a back-off strategy.

### Initiate upload {#initiate-upload}

Submit an HTTP POST request to the desired folder. Assets are created or updated in this folder. Include the selector `.initiateUpload.json` to indicate that the request is to initiate upload of a binary file. For example, the path to the folder where the asset should be created is `/assets/folder`. The POST request is `POST https://[aem_server]:[port]/content/dam/assets/folder.initiateUpload.json`.

The content type of the request body should be `application/x-www-form-urlencoded` form data, containing the following fields:

* `(string) fileName`: Required. The name of the asset as it appears in [!DNL Experience Manager].
* `(number) fileSize`: Required. The file size, in bytes, of the asset being uploaded.

A single request can be used to initiate uploads for multiple binaries, as long as each binary contains the required fields. If successful, the request responds with a `201` status code and a body containing JSON data in the following format:

```json
{
    "completeURI": "(string)",
    "folderPath": "(string)",
    "files": [
        {
            "fileName": "(string)",
            "mimeType": "(string)",
            "uploadToken": "(string)",
            "uploadURIs": [
                "(string)"
            ],
            "minPartSize": (number),
            "maxPartSize": (number)
        }
    ]
}
```

* `completeURI` (string): Call this URI when the binary finishes uploading. The URI can be an absolute or relative URI, and clients should be able to handle either. That is, the value can be `"https://[aem_server]:[port]/content/dam.completeUpload.json"` or `"/content/dam.completeUpload.json"` See [complete upload](#complete-upload).
* `folderPath` (string): Full path to the folder in which the binary is uploaded.
* `(files)` (array): A list of elements whose length and order match the length and order of the list of binary information provided in the initiate request.
* `fileName` (string): The name of the corresponding binary, as supplied in the initiate request. This value should be included in the complete request.
* `mimeType` (string): The mime type of the corresponding binary, as supplied in the initiate request. This value should be included in the complete request.
* `uploadToken` (string): An upload token for the corresponding binary. This value should be included in the complete request.
* `uploadURIs` (array): A list of strings whose values are full URIs to which the binary's content should be uploaded (see [Upload binary](#upload-binary)).
* `minPartSize` (number): The minimum length, in bytes, of data that may be provided to any one of the `uploadURIs`, if there is more than one URI.
* `maxPartSize` (number): The maximum length, in bytes, of data that may be provided to any one of the `uploadURIs`, if there is more than one URI.

### Upload binary {#upload-binary}

The output of initiating an upload includes one or more upload URI values. If more than one URI is provided, the client may split the binary into parts and make PUT requests of each part to the provided upload URIs, in order. If you choose to split the binary into parts, adhere to the following guidelines:

* Each part, with the exception of the last, must be of a size greater than or equal to `minPartSize`.
* Each part must be of a size less than or equal to `maxPartSize`.
* If the size of your binary exceeds `maxPartSize`, split the binary into parts to upload it.
* You are not required to use all URIs.

If the size of your binary is less than or equal to `maxPartSize`, you may instead upload the entire binary to a single upload URI. If more than one upload URI is provided, use the first one and ignore the rest. You are not required to use all URIs.

CDN edge nodes help accelerate the requested upload of binaries.

The easiest way to accomplish this is to use the value of `maxPartSize` as your part size. The API contract guarantees that there are sufficient upload URIs to upload your binary if you use this value as your part size. To do this, split the binary into parts of size `maxPartSize`, using one URI for each part, in order. The final part can be of any size less than or equal to `maxPartSize`. For example, assume the total size of the binary is 20,000 bytes, the `minPartSize` is 5,000 bytes, `maxPartSize` is 8,000 bytes, and the number of upload URIs is 5. Execute the following steps:

* Upload the first 8,000 bytes of the binary using the first upload URI.
* Upload the second 8,000 bytes of the binary using the second upload URI.
* Upload the last 4,000 bytes of the binary using the third upload URI. Since this is the final part, it does not need to be larger than `minPartSize`.
* You do not need to use the last two upload URIs. You can ignore them.

A common error is to calculate the part size based on the number of upload URIs provided by the API. The API contract does not guarantee that this approach works, and may actually result in part sizes that are outside the range between `minPartSize` and `maxPartSize`. This can result in binary upload failures.

Again, the easiest and safest way is to simply use parts of size equal to `maxPartSize`.

If the upload is successful, the server responds to each request with a `201` status code.

>[!NOTE]
>
>For more information about the upload algorithm, see the [official feature documentation](https://jackrabbit.apache.org/oak/docs/features/direct-binary-access.html#Upload) and [API documentation](https://jackrabbit.apache.org/oak/docs/apidocs/org/apache/jackrabbit/api/binary/BinaryUpload.html) in the Apache Jackrabbit Oak project.

### Complete upload {#complete-upload}

After all the parts of a binary file are uploaded, submit an HTTP POST request to the complete URI provided by the initiation data. The content type of the request body should be `application/x-www-form-urlencoded` form data, containing the following fields.

|Fields | Type | Required or not | Description |
|---|---|---|---|
| `fileName` | String | Required | The name of the asset, as was provided by the initiation data. |
| `mimeType` | String | Required | The HTTP content type of the binary, as was provided by the initiation data. |
| `uploadToken` | String | Required | Upload token for the binary, as was provided by the initiation data. |
| `createVersion` | Boolean | Optional | If `True` and an asset with the specified name exists, then [!DNL Experience Manager] creates a new version of the asset. |
| `versionLabel` | String | Optional | If a new version is created, the label associated with the new version of an asset . |
| `versionComment` | String | Optional | If a new version is created, the comments associated with the version. |
| `replace` | Boolean | Optional | If `True` and an asset with the specified name exists, [!DNL Experience Manager] deletes the asset then re-create it. |
| `uploadDuration` | Number | Optional | The total amount of time, in milliseconds, for the file to upload in its entirety. If specified, the upload duration is included in the system's log files for transfer rate analysis. |
| `fileSize` | Number | Optional | The size, in bytes, of the file. If specified, the file size is included in the system's log files for transfer rate analysis. |

>[!NOTE]
>
>If the asset exists and neither `createVersion` nor `replace` is specified, then [!DNL Experience Manager] updates the asset's current version with the new binary.

Like the initiate process, the complete request data may contain information for more than one file.

The process of uploading a binary is not done until the complete URL is invoked for the file. An asset is processed after the upload process is complete. Processing does not start even if the asset's binary file is uploaded completely but upload process is not completed. If upload is successful, the server responds with a `200` status code.

### Open-source upload library {#open-source-upload-library}

To learn more about the upload algorithms or to build your own upload scripts and tools, Adobe provides open-source libraries and tools:

* [Open-source aem-upload library](https://github.com/adobe/aem-upload).
* [Open-source command-line tool](https://github.com/adobe/aio-cli-plugin-aem).

>[!NOTE]
>
>The aem-upload library and the command-line tool both use the [node-httptransfer library](https://github.com/adobe/node-httptransfer/)

### Deprecated asset upload APIs {#deprecated-asset-upload-api}

<!-- #ENGCHECK review / update the list of deprecated APIs below. -->

The new upload method is supported only for [!DNL Adobe Experience Manager] as a [!DNL Cloud Service]. The APIs from [!DNL Adobe Experience Manager] 6.5 are deprecated. The methods related to upload or update assets or renditions (any binary upload) are deprecated in the following APIs:

* [Experience Manager Assets HTTP API](mac-api-assets.md)
* `AssetManager` Java API, like `AssetManager.createAsset(..)`

>[!MORELIKETHIS]
>
>* [Open-source aem-upload library](https://github.com/adobe/aem-upload).
>* [Open-source command-line tool](https://github.com/adobe/aio-cli-plugin-aem).
>* [Apache Jackrabbit Oak documentation for direct upload](https://jackrabbit.apache.org/oak/docs/features/direct-binary-access.html#Upload).

## Asset processing and post-processing workflows {#post-processing-workflows}

In [!DNL Experience Manager], the asset processing is based on **[!UICONTROL Processing Profiles]** configuration that uses [asset microservices](asset-microservices-configure-and-use.md#get-started-using-asset-microservices). Processing does not require developer extensions.

For post-processing workflow configuration, use the standard workflows with extensions with custom steps.

## Support of workflow steps in post-processing workflow {#post-processing-workflows-steps}

If you upgrade from a previous version of [!DNL Experience Manager], you can use asset microservices to process assets. The cloud-native asset microservices are simpler to configure and use. A few workflow steps used in the [!UICONTROL DAM Update Asset] workflow in the previous version are not supported. For more information about supported classes, see the [Java API reference or Javadocs](https://www.adobe.io/experience-manager/reference-materials/cloud-service/javadoc/index.html).

The following technical workflow models are either replaced by asset microservices or the support is not available:

* `com.day.cq.dam.cameraraw.process.CameraRawHandlingProcess`
* `com.day.cq.dam.core.process.CommandLineProcess`
* `com.day.cq.dam.pdfrasterizer.process.PdfRasterizerHandlingProcess`
* `com.day.cq.dam.core.process.AddPropertyWorkflowProcess`
* `com.day.cq.dam.core.process.CreateSubAssetsProcess`
* `com.day.cq.dam.core.process.DownloadAssetProcess`
* `com.day.cq.dam.word.process.ExtractImagesProcess`
* `com.day.cq.dam.word.process.ExtractPlainProcess`
* `com.day.cq.dam.ids.impl.process.IDSJobProcess`
* `com.day.cq.dam.indd.process.INDDMediaExtractProcess`
* `com.day.cq.dam.indd.process.INDDPageExtractProcess`
* `com.day.cq.dam.core.impl.lightbox.LightboxUpdateAssetProcess`
* `com.day.cq.dam.pim.impl.sourcing.upload.process.ProductAssetsUploadProcess`
* `com.day.cq.dam.core.process.SendDownloadAssetEmailProcess`
* `com.day.cq.dam.similaritysearch.internal.workflow.smarttags.StartTrainingProcess`
* `com.day.cq.dam.similaritysearch.internal.workflow.smarttags.TransferTrainingDataProcess`
* `com.day.cq.dam.switchengine.process.SwitchEngineHandlingProcess`
* `com.day.cq.dam.core.process.GateKeeperProcess`
* `com.day.cq.dam.s7dam.common.process.DMEncodeVideoWorkflowCompletedProcess`
* `com.day.cq.dam.core.process.DeleteImagePreviewProcess`
* `com.day.cq.dam.video.FFMpegTranscodeProcess`
* `com.day.cq.dam.core.process.ThumbnailProcess`
* `com.day.cq.dam.video.FFMpegThumbnailProcess`
* `com.day.cq.dam.core.process.CreateWebEnabledImageProcess`
* `com.day.cq.dam.core.process.CreatePdfPreviewProcess`
* `com.day.cq.dam.s7dam.common.process.VideoUserUploadedThumbnailProcess`
* `com.day.cq.dam.s7dam.common.process.VideoThumbnailDownloadProcess`
* `com.day.cq.dam.s7dam.common.process.VideoProxyServiceProcess`
* `com.day.cq.dam.scene7.impl.process.Scene7UploadProcess`
* `com.day.cq.dam.s7dam.common.process.S7VideoThumbnailProcess`
* `com.day.cq.dam.core.process.MetadataProcessorProcess`
* `com.day.cq.dam.core.process.AssetOffloadingProcess`
* `com.adobe.cq.dam.dm.process.workflow.DMImageProcess`

<!-- Commenting the previous list documented at the time of GA. Replacing it with the updated list via cqdoc-18231.

* `com.day.cq.dam.core.process.DeleteImagePreviewProcess`
* `com.day.cq.dam.s7dam.common.process.DMEncodeVideoWorkflowCompletedProcess`
* `com.day.cq.dam.core.process.GateKeeperProcess`
* `com.day.cq.dam.core.process.AssetOffloadingProcess`
* `com.day.cq.dam.core.process.MetadataProcessorProcess`
* `com.adobe.cq.dam.dm.process.workflow.DMImageProcess`
* `com.day.cq.dam.s7dam.common.process.S7VideoThumbnailProcess`
* `com.day.cq.dam.scene7.impl.process.Scene7UploadProcess`
* `com.day.cq.dam.s7dam.common.process.VideoProxyServiceProcess`
* `com.day.cq.dam.s7dam.common.process.VideoThumbnailDownloadProcess`
* `com.day.cq.dam.s7dam.common.process.VideoUserUploadedThumbnailProcess`
* `com.day.cq.dam.core.process.CreatePdfPreviewProcess`
* `com.day.cq.dam.core.process.CreateWebEnabledImageProcess`
* `com.day.cq.dam.video.FFMpegThumbnailProcess`
* `com.day.cq.dam.core.process.ThumbnailProcess`
* `com.day.cq.dam.cameraraw.process.CameraRawHandlingProcess`
* `com.day.cq.dam.core.process.CommandLineProcess`
* `com.day.cq.dam.pdfrasterizer.process.PdfRasterizerHandlingProcess`
* `com.day.cq.dam.core.process.AddPropertyWorkflowProcess`
* `com.day.cq.dam.core.process.CreateSubAssetsProcess`
* `com.day.cq.dam.core.process.DownloadAssetProcess`
* `com.day.cq.dam.word.process.ExtractImagesProcess`
* `com.day.cq.dam.word.process.ExtractPlainProcess`
* `com.day.cq.dam.video.FFMpegTranscodeProcess`
* `com.day.cq.dam.ids.impl.process.IDSJobProcess`
* `com.day.cq.dam.indd.process.INDDMediaExtractProcess`
* `com.day.cq.dam.indd.process.INDDPageExtractProcess`
* `com.day.cq.dam.core.impl.lightbox.LightboxUpdateAssetProcess`
* `com.day.cq.dam.pim.impl.sourcing.upload.process.ProductAssetsUploadProcess`
* `com.day.cq.dam.core.process.ScheduledPublishBPProcess`
* `com.day.cq.dam.core.process.ScheduledUnPublishBPProcess`
* `com.day.cq.dam.core.process.SendDownloadAssetEmailProcess`
-->

<!-- PPTX source: slide in add-assets.md - overview of direct binary upload section of
https://adobe-my.sharepoint.com/personal/gklebus_adobe_com/_layouts/15/guestaccess.aspx?guestaccesstoken=jexDC5ZnepXSt6dTPciH66TzckS1BPEfdaZuSgHugL8%3D&docid=2_1ec37f0bd4cc74354b4f481cd420e07fc&rev=1&e=CdgElS
-->

>[!MORELIKETHIS]
>
>* [[!DNL Experience Cloud] as a [!DNL Cloud Service] SDK](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md).
