---
title: Assets HTTP API
description: Create, read, update, delete, manage digital assets using HTTP API in [!DNL Experience Manager Assets].
contentOwner: AG
feature: Assets HTTP API
role: Developer, Architect, Admin
exl-id: a3b7374d-f24b-4d6f-b6db-b9c9c962bb8d
---
# Manage digital assets with the [!DNL Adobe Experience Manager Assets] HTTP API{#assets-http-api}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/extending/mac-api-assets.html?lang=en)                  |
| AEM as a Cloud Service     | This article         |

## Get Started with the AEM [!DNL Assets] HTTP API {#overview}

The AEM [!DNL Assets] HTTP API enables CRUD (create, read, update, and delete) operations on digital assets through a REST interface available at /`api/assets`. These operations apply to asset metadata, renditions, and comments. It includes [support for Content Fragments](/help/assets/content-fragments/assets-api-content-fragments.md).

>[!NOTE]
>
> A modernized OpenAPI implementation of the Content Fragment Management API is available. For full documentation see [Content Fragment Management API](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/sites/). It is recommended to use the new OpenAPI implementation. The existing usage of Assets HTTP API for Content Fragments should be migrated to the new Content Fragment Management OpenAPI.

To access the API:

1. Open the API service document at `https://[hostname]:[port]/api.json`.
1. Follow the [!DNL Assets] service link leading to `https://[hostname]:[server]/api/assets.json`.

The API response is a JSON file for some MIME types and a response code for all MIME types. The JSON response is optional and may not be available, for example, for PDF files. Rely on the response code for further analysis or actions.

>[!NOTE]
>
>All the API calls related to uploading or updating assets or binaries in general (like renditions) is deprecated for [!DNL Experience Manager] as a [!DNL Cloud Service] deployment. For uploading binaries, use [direct binary upload APIs](developer-reference-material-apis.md#asset-upload) instead.

## Manage content fragments {#content-fragments}

A [Content Fragment](/help/assets/content-fragments/content-fragments.md) is a structured asset that stores text, numbers, and dates. As there are several differences to `standard` assets (such as images or documents), some additional rules apply to handling Content Fragments.

For more information, see [Content Fragments support in the [!DNL Experience Manager Assets] HTTP API](/help/assets/content-fragments/assets-api-content-fragments.md).

>[!NOTE]
>
>See [AEM APIs for Structured Content Delivery and Management](/help/headless/apis-headless-and-content-fragments.md) for an overview of the various APIs available and comparison of some of the concepts involved.
>
>The [Content Fragment and Content Fragment Model OpenAPIs](/help/headless/content-fragment-openapis.md) are also available.

## Examine the data model {#data-model}

The [!DNL Assets] HTTP API primarily exposes two elements: folders and standard assets. It also provides detailed elements for custom data models used in Content Fragments. For more details, see Content Fragment data models. See [Content Fragment data models](/help/assets/content-fragments/assets-api-content-fragments.md#content-models-and-content-fragments) for further information.

>[!NOTE]
>
>The [Content Fragment and Content Fragment Model OpenAPIs](/help/headless/content-fragment-openapis.md) are also available.

### Manage folders {#folders}

Folders are like directories as in the traditional file systems. Folders can contain assets, subfolders, or both. Folders have the following components:

**Entities**: The entities of a folder are its child elements, which can be folders and assets.

**Properties**:

* `name`: The folder's name (the last segment of the URL path, without the extension).
* `title`: An optional title displayed in place of the folder name.

>[!NOTE]
>
>Some properties of folder or asset are mapped to a different prefix. The `jcr` prefix of `jcr:title`, `jcr:description`, and `jcr:language` are replaced with `dc` prefix. Hence in the returned JSON, `dc:title` and `dc:description` contain the values of `jcr:title` and `jcr:description`, respectively.

**Links** Folders expose three links:

* `self`: A link to the folder itself.
* `parent`: A link to the parent folder.
* `thumbnail` (Optional): A link to a folder thumbnail image.

### Manage assets {#assets}

In [!DNL Experience Manager] an asset contains the following elements:

* **Properties and metadata:** Descriptive information about the asset.
* **Binary file:** The originally uploaded file.
* **Renditions:** Multiple configured renditions (such as, images in various sizes, different video encodings, or extracted pages from PDFs/Adobe InDesign files).
* **Comments (optional):** User-provided remarks.

For information about elements in Content Fragments see [Content Fragments Support in Experience Manager Assets HTTP API](/help/assets/content-fragments/assets-api-content-fragments.md).

>[!NOTE]
>
>The [Content Fragment and Content Fragment Model OpenAPIs](/help/headless/content-fragment-openapis.md) are also available.

In [!DNL Experience Manager] a folder has the following components:

* Entities: The children of assets are its renditions.
* Properties.
* Links.

## Explore available API operations {#available-features}

The [!DNL Assets] HTTP API includes the following features:

* [Retrieve a folder listing](#retrieve-a-folder-listing).
* [Create a folder](#create-a-folder).
* [Create an asset (deprecated)](#create-an-asset)
* [Update asset binary (deprecated)](#update-asset-binary).
* [Update asset metadata](#update-asset-metadata).
* [Create an asset rendition](#create-an-asset-rendition).
* [Update an asset rendition](#update-an-asset-rendition).
* [Create an asset comment](#create-an-asset-comment).
* [Copy a folder or asset](#copy-a-folder-or-asset).
* [Move a folder or asset](#move-a-folder-or-asset).
* [Delete a folder, asset, or rendition](#delete-a-folder-asset-or-rendition).

>[!NOTE]
>
>For the ease of readability the following examples omit the complete cURL notations. The notation correlates with [Resty](https://github.com/micha/resty) which is a script wrapper for cURL.

<!-- TBD: The Console Manager is not available now. So how to configure the below? 

**Prerequisites**

* Go to `https://[aem_server]:[port]/system/console/configMgr`.
* Navigate to **Adobe Granite CSRF Filter**.
* Make sure the property **Filter Methods** includes: POST, PUT, DELETE.
-->

## Retrieve a folder listing {#retrieve-a-folder-listing}

Retrieves a Siren representation of an existing folder and of its child entities (subfolders or assets).

**Request**: `GET /api/assets/myFolder.json`

**Response codes**: The response codes are:

* 200 - OK - success.
* 404 - NOT FOUND - folder does not exist or is not accessible.
* 500 - INTERNAL SERVER ERROR - if something else goes wrong.

**Response**: The class of the entity returned is an asset or a folder. The properties of contained entities are a subset of the full set of properties of each entity. To obtain a full representation of the entity, clients should retrieve the contents of the URL pointed to by the link with a `rel` of `self`.

## Create a folder {#create-a-folder}

Creates a `sling`: `OrderedFolder` at the given path. If `*` is provided instead of a node name, the servlet uses the parameter name as node name. The request accepts either of the following: 

* A Siren representation of the new folder 
* A set of name-value pairs, encoded as `application/www-form-urlencoded` or `multipart`/ `form`- `data`. These are useful to create a folder directly from an HTML form. 

Also, properties of the folder can be specified as URL query parameters.

An API call fails with a `500` response code if the parent node of the provided path does not exist. A call returns a response code `409` if the folder exists.

**Parameters**: `name` is the folder name.

**Request**

* `POST /api/assets/myFolder -H"Content-Type: application/json" -d '{"class":"assetFolder","properties":{"title":"My Folder"}}'`
* `POST /api/assets/* -F"name=myfolder" -F"title=My Folder"`

**Response codes**: The response codes are:

* 201 - CREATED - on successful creation.
* 409 - CONFLICT - if folder exists.
* 412 - PRECONDITION FAILED - if root collection cannot be found or accessed.
* 500 - INTERNAL SERVER ERROR - if something else goes wrong.

## Create an asset {#create-an-asset}

Asset creation is not supported via this HTTP API. For asset creation, use the [asset upload](developer-reference-material-apis.md) API.

## Update an asset binary {#update-asset-binary}

See [asset upload](developer-reference-material-apis.md) for information on how to update asset binaries. You cannot update an asset binary using the HTTP API.

## Update metadata of an asset {#update-asset-metadata}

This operation updates the asset's metadata. When updating properties in the `dc:` namespace, the corresponding `jcr:` property is updated. However, the API does not sync the properties under the two namespaces.

**Request**: `PUT /api/assets/myfolder/myAsset.png -H"Content-Type: application/json" -d '{"class":"asset", "properties":{"dc:title":"My Asset"}}'`

**Response codes**: The response codes are:

* 200 - OK - if Asset has been updated successfully.
* 404 - NOT FOUND - if Asset could not be found or accessed at the provided URI.
* 412 - PRECONDITION FAILED - if root collection cannot be found or accessed.
* 500 - INTERNAL SERVER ERROR - if something else goes wrong.

## Create an asset rendition {#create-an-asset-rendition}

Create a rendition for an asset. If request parameter name is not provided, the file name is used as rendition name.

**Parameters**: The parameters are:

`name`: for the rendition name.
`file`: The binary file for the rendition as a reference. 

**Request**

* `POST /api/assets/myfolder/myasset.png/renditions/web-rendition -H"Content-Type: image/png" --data-binary "@myRendition.png"`
* `POST /api/assets/myfolder/myasset.png/renditions/* -F"name=web-rendition" -F"file=@myRendition.png"`

**Response codes**

* 201 - CREATED - if Rendition has been created successfully.
* 404 - NOT FOUND - if Asset could not be found or accessed at the provided URI.
* 412 - PRECONDITION FAILED - if root collection cannot be found or accessed.
* 500 - INTERNAL SERVER ERROR - if something else goes wrong.

## Update an asset rendition {#update-an-asset-rendition}

Updates respectively replace an asset rendition with the new binary data.

**Request**: `PUT /api/assets/myfolder/myasset.png/renditions/myRendition.png -H"Content-Type: image/png" --data-binary @myRendition.png`

**Response codes**: The response codes are:

* 200 - OK - if Rendition has been updated successfully.
* 404 - NOT FOUND - if Asset could not be found or accessed at the provided URI.
* 412 - PRECONDITION FAILED - if root collection cannot be found or accessed.
* 500 - INTERNAL SERVER ERROR - if something else goes wrong.

## Add a comment on an asset {#create-an-asset-comment}

**Parameters**: The parameters are `message` for the message body of the comment and `annotationData` for the Annotation data in JSON format.

**Request**: `POST /api/assets/myfolder/myasset.png/comments/* -F"message=Hello World." -F"annotationData={}"`

**Response codes**: The response codes are:

* 201 - CREATED - if Comment has been created successfully.
* 404 - NOT FOUND - if Asset could not be found or accessed at the provided URI.
* 412 - PRECONDITION FAILED - if root collection cannot be found or accessed.
* 500 - INTERNAL SERVER ERROR - if something else goes wrong.

## Copy a folder or an asset {#copy-a-folder-or-asset}

Copies a folder or asset available at the provided path to a new destination.

**Request Headers**: The parameters are:

* `X-Destination` - a new destination URI within the API solution scope to copy the resource to.
* `X-Depth` - either `infinity` or `0`. Using `0` only copies the resource and its properties and not its children.
* `X-Overwrite` - Use `F` to prevent overwriting an asset at the existing destination.

**Request**: `COPY /api/assets/myFolder -H"X-Destination: /api/assets/myFolder-copy"`

**Response codes**: The response codes are:

* 201 - CREATED - if folder/asset has been copied to a non-existing destination.
* 204 - NO CONTENT - if the folder/asset has been copied to an existing destination.
* 412 - PRECONDITION FAILED - if a request header is missing.
* 500 - INTERNAL SERVER ERROR - if something else goes wrong.

## Move a folder or an asset {#move-a-folder-or-asset}

Moves a folder or asset at the given path to a new destination.

**Request Headers**: The parameters are:

* `X-Destination` - a new destination URI within the API solution scope to copy the resource to.
* `X-Depth` - either `infinity` or `0`. Using `0` only copies the resource and its properties and not its children.
* `X-Overwrite` - Use either `T` to forcibly delete an existing resources or `F` to prevent overwriting an existing resource.

**Request**: `MOVE /api/assets/myFolder -H"X-Destination: /api/assets/myFolder-moved"`

**Response codes**: The response codes are:

* 201 - CREATED - if folder/asset has been copied to a non-existing destination.
* 204 - NO CONTENT - if the folder/asset has been copied to an existing destination.
* 412 - PRECONDITION FAILED - if a request header is missing.
* 500 - INTERNAL SERVER ERROR - if something else goes wrong.

## Delete a folder, an asset, or a rendition {#delete-a-folder-asset-or-rendition}

Deletes a resource (-tree) at the provided path.

**Request**

* `DELETE /api/assets/myFolder`
* `DELETE /api/assets/myFolder/myAsset.png`
* `DELETE /api/assets/myFolder/myAsset.png/renditions/original`

**Response codes**: The response codes are:

* 200 - OK - if folder has been deleted successfully.
* 412 - PRECONDITION FAILED - if root collection cannot be found or accessed.
* 500 - INTERNAL SERVER ERROR - if something else goes wrong.

## Follow best practices and note limitations {#tips-limitations}

* Assets and their renditions become unavailable via the [!DNL Assets] web interface and the HTTP API when the [!UICONTROL Off Time] is reached. The API returns a 404 error if the [!UICONTROL On Time] is in the future or [!UICONTROL Off Time] is in the past.

* The Assets HTTP API returns only a subset of metadata. The namespaces are hardcoded and only those namespaces are returned. For complete metadata, see the asset path `/jcr_content/metadata.json`.

* Some properties of folder or asset are mapped to a different prefix when updated using APIs. The `jcr` prefix of `jcr:title`, `jcr:description`, and `jcr:language` are replaced with `dc` prefix. Hence in the returned JSON, `dc:title` and `dc:description` contain the values of `jcr:title` and `jcr:description`, respectively.

**Explore related resources**

* [Translate Assets](translate-assets.md)
* [Assets supported file formats](file-format-support.md)
* [Search assets](search-assets.md)
* [Connected assets](use-assets-across-connected-assets-instances.md)
* [Asset reports](asset-reports.md)
* [Metadata schemas](metadata-schemas.md)
* [Download assets](download-assets-from-aem.md)
* [Manage metadata](manage-metadata.md)
* [Search facets](search-facets.md)
* [Manage collections](manage-collections.md)
* [Bulk metadata import](metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)

>[!MORELIKETHIS]
>
>* [Developer reference docs for [!DNL Assets]](/help/assets/developer-reference-material-apis.md)
