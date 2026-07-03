---
title: Delivery APIs
description: Learn how to use the Delivery APIs.
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 806ca38f-2323-4335-bfd8-a6c79f6f15fb
---
# Delivery  APIs {#delivery-apis}

All [approved assets](approve-assets.md) available in the Experience Manager assets repository can be [searched](search-assets-api.md) and then delivered to integrated downstream applications using a Delivery URL.

Any changes made to approved assets in DAM, including version updates and metadata modifications, are automatically reflected in the delivery URLs. With a short Time-to-Live (TTL) value of 10 minutes configured for assets delivery via CDN, updates become visible across all authoring and published interfaces in under 10 minutes.

The following image illustrates the available delivery URLs: 

![Delivery APIs](assets/delivery-url.png)

The following table illustrates the usage of the various available Delivery APIs:

|Delivery API | Description |
|---|---|
| [Web-optimized binary representation of the asset in requested output format](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat) |Returns the web-optimized binary representation of the asset in requested output format based on the asset ID sent in the request. In addition, you can define various image modifiers, such as width, height, rotate, flip, quality, crop, format, and [smart crop](/help/assets/dynamic-media/image-profiles.md). See the [API details](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat) for supported formats and image modifiers.<br>Adobe recommends using this API for all image format types.|
| [Web-optimized binary representation of the asset](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAsset) |Convenience API that applies defaults to a web-optimized binary representation of the asset returned in the response. The defaults include a standard JPEG/WEBP format, quality => 65, and width => 1024. |
|[Original uploaded binary of the asset](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetOriginal) |Returns the originally uploaded binaries for the asset. Adobe recommends using this API for document format types and SVG images. |
|[Pre-generated rendition of the asset available on AEM Assets authoring environment](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetRendition) |Returns the asset rendition's bitstream available on AEM Assets authoring environment based on asset ID and rendition name sent in the request. |
| [Asset metadata](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetMetadata) |Returns the properties associated with an asset, such as, title, description, CreateDate, ModifyDate, and so on.|
| [Player container for the video asset](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/videoPlayerDelivery) |Returns the player container for the video asset. You can  embed the player in to an iframe HTML element and play the video.|
| [Playback manifests in the selected output format](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/videoManifestDelivery) | Returns the playback manifest file for the specified video asset in the selected output format. You must build a custom player capable of adaptive streaming through HLS or DASH protocols to be able to pull the playback manifest file and play the video.|

>[!IMPORTANT]
>
>You can test any modifier, which is not generally available via experimental APIs. For example, `</adobe/experimental/advancemodifiers-expires-YYYYMMDD/assets>`
>Click here to know more on how to use the [experimental APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/guides/how-to/#experimental-apis) and the [complete list of modifiers](https://developer.adobe.com/experience-cloud/experience-manager-apis/).

Dynamic Media with OpenAPI capabilities also supports long form videos. The videos can support upto 50 GB and 2 hours.

For information on the available Dynamic Media offerings and their capabilities, see [Dynamic Media Prime and Ultimate](/help/assets/dynamic-media/dm-prime-ultimate.md).

>[!NOTE]
>
>DM Prime customers can use basic image modifiers, including rotate, crop, flip, height, width, and quality. Smart Imaging does not support AVIF for DM Prime customers.

## Delivery APIs endpoints {#delivery-apis-endpoint}

The API endpoints vary for each delivery API. For example, the API endpoint for `Web-optimized binary representation of the asset in the requested output format` API is:
`https://delivery-pXXXX-eYYYY.adobeaemcloud.com/adobe/assets/{assetId}/as/{seoName}.{format}`

The delivery domain is similar in structure to the Experience Manager author environment's domain. The only difference is replacing the term `author` with `delivery`.

`pXXXX` refers to the program ID

`eYYYY` refers to the environment ID

See [API details](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#tag/Assets) for more information.

## Delivery APIs request method {#delivery-api-request-method}

GET

## Delivery APIs header {#deliver-assets-api-header}

You need to provide the following details while defining a header in the Delivery APIs header:

```java
headers: {
      'If-None-Match': 'string',
      Authorization: 'Bearer <YOUR_JWT_HERE>'
    }
```

To invoke the Delivery APIs, an IMS token is required in the `Authorization` details to deliver a restricted asset. The IMS token is fetched from a technical account. See [Fetch the AEM as a Cloud Service Credentials](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/generating-access-tokens-for-server-side-apis) to create a new technical account. See [Generating the access token](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/generating-access-tokens-for-server-side-apis) to generate the IMS token and use it appropriately in the Delivery APIs request header.


To view request samples, response samples, and response codes, see [Delivery APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat).

## Frequently Asked Questions {#delivery-apis-faqs}

### What are the Dynamic Media with OpenAPI Delivery APIs and what do they enable? {#delivery-apis-overview}

The Dynamic Media with OpenAPI Delivery APIs enable approved assets stored in Adobe Experience Manager Assets to be delivered to integrated downstream applications via a Delivery URL. Seven distinct APIs are available covering image delivery, original binary delivery, pre-generated rendition delivery, asset metadata retrieval, video player embedding, and video playback manifest delivery. Any changes made to approved assets in DAM — including version updates and metadata modifications — are automatically reflected in the delivery URLs without requiring republishing or manual intervention.

### How quickly do asset updates appear in Delivery API URLs after changes in AEM Assets? {#delivery-api-ttl-updates}

Updates to approved assets in AEM Assets are visible across all authoring and published interfaces in under 10 minutes. Dynamic Media with OpenAPI Delivery APIs use a short Time-to-Live value of 10 minutes configured for asset delivery via CDN. This means version updates, metadata modifications, and other changes made to approved assets in the DAM automatically propagate to delivery URLs within 10 minutes without requiring manual cache invalidation.

### Which Delivery API should I use for delivering image assets? {#delivery-api-image-recommendation}

The Web-optimized binary representation of the asset in requested output format API is the recommended API for all image format types. This API returns the web-optimized binary representation of the asset in the requested output format based on the asset ID sent in the request. It supports various image modifiers including width, height, rotate, flip, quality, crop, format, and smart crop. For document format types and SVG images, the Original uploaded binary of the asset API is recommended instead.

### What image modifiers are supported by the Web-optimized binary representation Delivery API? {#delivery-api-image-modifiers}

The Web-optimized binary representation of the asset in requested output format API supports image modifiers including width, height, rotate, flip, quality, crop, format, and smart crop. These modifiers can be defined as parameters in the delivery URL request to transform the asset at delivery time without modifying the original asset stored in AEM Assets. 

### What does the convenience Web-optimized binary representation Delivery API return by default? {#delivery-api-defaults}

The convenience Web-optimized binary representation of the asset API applies defaults to the asset returned in the response. The default values are JPEG or WEBP format, quality of 65, and width of 1024 pixels. This API is suitable when specific output format or modifier control is not required and a standard web-optimized rendition is sufficient for the downstream application.

### Which Delivery API should I use for documents and SVG images? {#delivery-api-documents-svg}

The Original uploaded binary of the asset API is the recommended API for document format types and SVG images. This API returns the originally uploaded binary for the asset without applying web optimization transformations. For all other image format types, the Web-optimized binary representation API in the requested output format is recommended.

### How do I retrieve pre-generated renditions of an asset using the Delivery APIs? {#delivery-api-pre-generated-renditions}

The Pre-generated rendition of the asset available on AEM Assets authoring environment API returns the bitstream of a specific rendition based on the asset ID and rendition name sent in the request. The rendition must already exist on the AEM Assets authoring environment before it can be retrieved using this API. This API is distinct from the web-optimized binary API which generates the output on demand using image modifiers.

### How do I embed and play a video asset using the Delivery APIs? {#delivery-api-video-player}

The Player container for the video asset API returns a player container for a video asset that can be embedded into an iframe HTML element to enable in-page video playback. For scenarios requiring custom player implementations with adaptive streaming, the Playback manifests in the selected output format API returns the playback manifest file for the specified video asset in HLS or DASH format. A custom player capable of adaptive streaming through HLS or DASH protocols must be built to consume the manifest file and play the video.

### What is the maximum video file size and duration supported by Dynamic Media with OpenAPI Delivery APIs? {#delivery-api-video-limits}

Dynamic Media with OpenAPI Delivery APIs support long-form videos up to 50 GB in file size and up to 2 hours in duration. These limits apply to video assets delivered via the Player container and Playback manifests Delivery APIs.

### How is the Delivery API endpoint URL structured? {#delivery-api-endpoint-structure}

The Delivery API endpoint URL for the web-optimized binary representation in the requested output format follows this structure: https://delivery-pXXXX-eYYYY.adobeaemcloud.com/adobe/assets/{assetId}/as/{seoName}.{format}. The delivery domain is structured similarly to the AEM author environment domain — the only difference is replacing the term author with delivery. In the URL, pXXXX refers to the program ID and eYYYY refers to the environment ID. All Delivery APIs use the HTTP GET request method.

### What authentication is required to call the Dynamic Media with OpenAPI Delivery APIs? {#delivery-api-authentication}

Calling the Dynamic Media with OpenAPI Delivery APIs requires an IMS token in the Authorization header to deliver restricted assets. The header must include two fields: If-None-Match as a string value, and Authorization as a Bearer token containing the IMS token. The IMS token is fetched from a technical account created using the AEM as a Cloud Service Credentials workflow. The technical account must be set up and the access token generated before invoking any Delivery API.

### What are experimental Delivery APIs and how do I access them? {#delivery-api-experimental}

Experimental Delivery APIs allow testing of image modifiers that are not yet generally available. Experimental APIs are accessed using a URL path format that includes the modifier and an expiry date — for example: /adobe/experimental/advancemodifiers-expires-YYYYMMDD/assets. The complete list of available experimental modifiers is documented on Adobe Developer Console. Experimental APIs are intended for testing purposes and are subject to change before general availability.

### What image modifier capabilities are available for Dynamic Media Prime customers compared to Dynamic Media Ultimate? {#delivery-api-prime-vs-ultimate-modifiers}

Dynamic Media Prime customers can use basic image modifiers including rotate, crop, flip, height, width, and quality via the Delivery APIs. Smart Imaging is available for Dynamic Media Prime customers with the exception that AVIF format is not supported for Smart Imaging on Dynamic Media Prime. Dynamic Media Ultimate customers have access to the full range of image modifiers and Smart Imaging capabilities including AVIF format support.