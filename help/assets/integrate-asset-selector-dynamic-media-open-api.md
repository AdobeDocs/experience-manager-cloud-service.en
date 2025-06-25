---
title: Integrate Asset Selector with Dynamic Media open API
description: Integrate Asset selector with various Adobe, non-Adobe, and third party applications.
role: Admin, User
exl-id: b01097f3-982f-4b2d-85e5-92efabe7094d
---
# Integration for Dynamic Media with OpenAPI capabilities {#integrate-asset-selector-dynamic-media-open-apis}

<table>
    <tr>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/dm-prime-ultimate.md"><b>Dynamic Media Prime and Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/assets-ultimate-overview.md"><b>AEM Assets Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/integrate-aem-assets-edge-delivery-services.md"><b>AEM Assets integration with Edge Delivery Services</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/aem-assets-view-ui-extensibility.md"><b>UI Extensibility</b></a>
        </td>
          <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/enable-dynamic-media-prime-and-ultimate.md"><b>Enable Dynamic Media Prime and Ultimate</b></a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="/help/assets/search-best-practices.md"><b>Search Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/metadata-best-practices.md"><b>Metadata Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/product-overview.md"><b>Content Hub</b></a>
        </td>
        <td>
            <a href="/help/assets/dynamic-media-open-apis-overview.md"><b>Dynamic Media with OpenAPI capabilities</b></a>
        </td>
        <td>
            <a href="https://developer.adobe.com/experience-cloud/experience-manager-apis/"><b>AEM Assets developer documentation</b></a>
        </td>
    </tr>
</table>

Asset Selector allows you to integrate using various Adobe applications to enable them to work together seamlessly.


## Prerequisites {#prereqs-polaris}

Use the following prerequisites if you are integrating Asset Selector with Dynamic Media with OpenAPI capabilities:

* [Communication methods](/help/assets/overview-asset-selector.md#prereqs)
* To access Dynamic Media with OpenAPI capabilities, you must have licenses for:
    * Assets repository (for example, Experience Manager Assets as a Cloud Service).
    * AEM Dynamic Media.
* Only [approved assets](/help/assets/approve-assets.md) are available for use ensuring brand consistency.

## Integration for Dynamic Media with OpenAPI capabilities {#adobe-app-integration-polaris}

Integration of Asset Selector with Dynamic Media OpenAPI process involves various steps that includes creating a customized dynamic media URL or ready to pick dynamic media URL, etc.

### Integrate Asset Selector for Dynamic Media with OpenAPI capabilities {#integrate-dynamic-media}

The `rootPath` and `path` properties should not be a part of the Dynamic Media with OpenAPI capabilities. Instead, you can configure the `aemTierType` property. Following is the syntax of configuration:

```
aemTierType:[1: "delivery"]
```

This configuration allows you to view all the approved assets without folders or as a flat structure. For more information, navigate to `aemTierType` property under [Asset Selector properties](/help/assets/asset-selector-properties.md).


### Create a Dynamic Delivery URL from approved assets {#create-dynamic-media-url}

Once you set up Asset Selector, a schema of objects is used to create a Dynamic Delivery URL from the selected assets.
For example, a schema of one object from an array of objects that is received upon the selection of an asset:

```
{
"dc:format": "image/jpeg",
"repo:assetId": "urn:aaid:aem:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
"repo:name": "image-7.jpg",
"repo:repositoryId": "delivery-pxxxx-exxxxxx.adobe.com",
...
}
```

All the selected assets are carried by `handleSelection` function that acts as a JSON object. For example, `JsonObj`. The dynamic delivery URL is created by combining the below carriers:

| Object | JSON |
|---|---|
|Host | `assetJsonObj["repo:repositoryId"]`|
|API root | `/adobe/assets` |
|asset-id | `assetJsonObj["repo:assetId"]`|
|seo-name |`assetJsonObj["repo:name"].split(".").slice(0,-1).join(".")`|
|format|`.jpg`|

#### Approved assets delivery API specification {#approved-assets-delivery-api-specification}

URL format:
`https://<delivery-api-host>/adobe/assets/<asset-id>/as/<seo-name>.<format>?<image-modification-query-parameters>`

Where,

* Host is `https://delivery-pxxxxx-exxxxxx.adobe.com`
* API root is `"/adobe/assets"`
* `<asset-id>` is Asset identifier
* `as` is the constant part of open API specification indicating what the asset be referred as
* `<seo-name>` is name of an asset
* `<format>` is the output format
* `<image modification query parameters>` as supported by the approved assets' delivery API specification

#### Approved assets Original Rendition delivery API {#approved-assets-delivery-api}

The dynamic delivery URL possesses the following syntax:
`https://<delivery-api-host>/adobe/assets/<asset-id>/original/as/<seo-name>`, where,

* Host is `https://delivery-pxxxxx-exxxxxx.adobe.com`
* API root for Original Rendition Delivery is `"/adobe/assets"`
* `<asset-id>` is asset identifier
* `/original/as` is the constant part of open API specification indicating what the original rendition be referred as
* `<seo-name>`is name of the asset that may or may not have an extension

### Ready to pick dynamic delivery URL {#ready-to-pick-dynamic-delivery-url}

All the selected assets are carried by `handleSelection` function that acts as a JSON object. For example, `JsonObj`. The dynamic delivery URL is created by combining the below carriers:

| Object | JSON |
|---|---|
|Host | `assetJsonObj["repo:repositoryId"]`|
|API root | `/adobe/assets` |
|asset-id | `assetJsonObj["repo:assetId"]`|
|seo-name |`assetJsonObj["repo:name"]`|

Below are the two ways to traverse the JSON object:

![Dynamic delivery url](assets/dynamic-delivery-url.png)

* **Thumbnail:** Thumbnails can be images and assets are PDF, video, images, and so on. Although, you can use the height and width attributes of an asset's thumbnail as the dynamic delivery rendition.
The following set of renditions can be used for the PDF type assets:
Once a pdf is selected in sidekick, the selection context offers the below information. Below is the way to traverse the JSON object:

    <!--![Thumbnail dynamic delivery url](image-1.png)-->

    You can refer to `selection[0].....selection[4]` for the array of rendition link from the above screenshot. For example, the key properties of one of the thumbnail renditions include: 
    
    ```
    { 
        "height": 319, 
        "width": 319, 
        "href": "https://delivery-pxxxxx-exxxxx.adobeaemcloud.com/adobe/assets/urn:aaid:aem:8560f3a1-d9cf-429d-a8b8-d81084a42d41/as/algorithm design.jpg?width=319&height=319", 
        "type": "image/webp" 
    } 
    ```

In the above screenshot, the delivery URL of the PDF's original rendition needs to be incorporated in the target experience if PDF is required and not its thumbnail. For example, `https://delivery-pxxxxx-exxxxx.adobeaemcloud.com/adobe/assets/urn:aaid:aem:8560f3a1-d9cf-429d-a8b8-d81084a42d41/original/as/algorithm design.pdf`

* **Video:** You can use video player URL for the video type assets which uses an embedded iFrame. You can use the following array renditions in the target experience:
    <!--![Video dynamic delivery url](image.png)-->
   
    ```
    { 
        "height": 319, 
        "width": 319, 
        "href": "https://delivery-pxxxxx-exxxxx.adobeaemcloud.com/adobe/assets/urn:aaid:aem:2fdef732-a452-45a8-b58b-09df1a5173cd/as/DragDrop.2.jpg?width=319&height=319", 
        "type": "image/webp" 
    } 
    ```

    You can refer to `selection[0].....selection[4]` for the array of rendition link from the above screenshot. For example, the key properties of one of the thumbnail renditions include:

    The code snippet in the above screenshot is an example of a video asset. It includes renditions links array. The `selection[5]` in the excerpt is the example of image thumbnail which can be used as the placeholder of video thumbnail in the target experience. The `selection[5]` in the renditions' array is for the video player. This serves an HTML, and can be set as `src` of the iframe. It supports adaptive bitrate streaming which is web-optimized delivery of the video. 
    
    In the above example, the video player URL is `https://delivery-pxxxxx-exxxxx.adobeaemcloud.com/adobe/assets/urn:aaid:aem:2fdef732-a452-45a8-b58b-09df1a5173cd/play` 

### Configure custom filters {#configure-custom-filters-dynamic-media-open-api}

Asset Selector for Dynamic Media with OpenAPI capabilities allows you to configure custom properties and the filters based on them. The `filterSchema` property is used to configure such properties. The customization can be exposed as `metadata.<metadata bucket>.<property name>.` against which the filters can be configured, where,

* `metadata` is the information of an asset
* `embedded` is the static parameter used for configuration, and
* `<propertyname>` is the filter name that you are configuring

For the configuration, properties that are defined at `jcr:content/metadata/` level are exposed as `metadata.<metadata bucket>.<property name>.` for the filters that you want to configure.

For example, in Asset Selector for Dynamic Media with OpenAPI capabilities, a property on `asset jcr:content/metadata/client_name:market` is converted into `metadata.embedded.client_name:market` for filter configuration.

To get the name, a one-time activity must be done. Make a search API call for the asset and get the property name (the bucket, essentially).

### Asset Selector user interface for Dynamic Media with OpenAPI capabilities {#interface-dynamic-media-open-api}

After integration with the Adobe's Micro-Frontend Asset Selector, you can see the assets only structure of all the approved assets available in Experience Manager assets repository. 

![Dynamic Media with OpenAPI capabilities UI](assets/polaris-ui.png)

* **A**: Hide/Show panel
* **B**: Assets
* **C**: Sorting
* **D**: Filters
* **E**: Search bar
* **F**: Sorting in ascending or descending order
* **G**: Cancel Selection
* **H**: Select single or multiple assets

>[!NOTE]
>
>Folders are only supported when connecting to author repository, and not Dynamic Meda with OpenAPI repository.

>[!MORELIKETHIS]
>
>* [Integrate Asset Selector with various applications](/help/assets/integrate-asset-selector.md)
>* [Asset Selector properties](/help/assets/asset-selector-properties.md)
>* [Asset Selector customizations](/help/assets/asset-selector-customization.md)
