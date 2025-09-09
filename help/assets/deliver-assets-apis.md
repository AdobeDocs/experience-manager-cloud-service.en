---
title: Delivery APIs
description: Learn how to use the Delivery APIs.
role: User
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
>You can test any modifier, which is not generally available via experimental APIs. For example, </adobe/experimental/advancemodifiers-expires-YYYYMMDD/assets>
Click here to know more on how to use the [experimental APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/guides/how-to/#experimental-apis) and the [complete list of modifiers](https://developer.adobe.com/experience-cloud/experience-manager-apis/).

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
