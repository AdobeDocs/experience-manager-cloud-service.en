---
title: Assets HTTP API
description: Learn about the implementation, data model, and features of Assets HTTP API. Use Assets HTTP API to perform various tasks around assets.
contentOwner: AG
---

# Assets HTTP API {#assets-http-api}

## Overview {#overview}

The Assets HTTP API allows for create-read-update-delete (CRUD) operations on Assets, including binary, metadata, renditions, and comments, together with structured content using AEM Content Fragments. It is exposed at `/api/assets` and is implemented as REST API. It includes [support for Content Fragments](content-fragments/content-fragments.md).

To access the API:

1. Open the API service document at `https://[hostname]:[port]/api.json`.
1. Follow the Assets service link leading to `https://[hostname]:[server]/api/assets.json`.

The API response is a JSON file for some mime types and a response code for all mime types. The JSON response is optional and may not be available, for example for PDF files. Rely on the response code for further analysis or actions.

After the [!UICONTROL Off Time], an asset and its renditions are not available either via the Assets web interface or through the HTTP API. The API returns 404 error message if the [!UICONTROL On Time] is in the future or [!UICONTROL Off Time] is in the past.

>[!NOTE]
>
>All the API calls related to uploading or updating assets or binaries in general (like renditions) is depreated for AEM as a Cloud Service deployment. For uploading binaries, please use [direct binary upload APIs](developer-reference-material-apis.md#asset-upload-technical) instead.

## Content Fragments {#content-fragments}

A [content fragment](content-fragments/content-fragments.md) is a special type of asset. It can be used to access structured data, such as texts, numbers, dates, amongst others. As there are several differences to `standard` assets (such as images or documents), some additional rules apply to handling content fragments.

For further information see [Content Fragments Support in the AEM Assets HTTP API](content-fragments/content-fragments.md).

## Data model {#data-model}

The Assets HTTP API exposes two major elements, folders and assets (for standard assets).

Additionally, it exposes more detailed elements for the custom data models that describe structured content in Content Fragments. See [Content Fragment Data Models](content-fragments/content-fragments.md) for further information.

### Folders {#folders}

Folders are like directories in traditional file systems. They are containers for other folders or asserts. Folders have the following components:

**Entities**: The entities of a folder are its child elements, which can be folders and assets.

**Properties**:
* `name`  -- Name of the folder. This is the same as the last segment in the URL path without the extension
* `title` -- Optional title of the folder which can be displayed instead of its name

>[!NOTE]
>
>Some properties of folder or asset are mapped to a different prefix. The `jcr` prefix of `jcr:title`, `jcr:description`, and `jcr:language` are replaced with `dc` prefix. Hence in the returned JSON, `dc:title` and `dc:description` contain the values of `jcr:title` and `jcr:description`, respectively.

**Links** Folders expose three links:
* `self`: Link to itself
* `parent`: Link to the parent folder
* `thumbnail`: (Optional) link to a folder thumbnail image

### Assets {#assets}

In AEM an assets contains the following elements:

* The properties and metadata of the asset
* Multiple renditions such as the original rendition (which is the originally uploaded asset), a thumbnail and various other renditions. Additional renditions may be images of different sizes, different video encodings, or extracted pages from PDF or InDesign.
* Optional comments

For information about elements in Content Fragments see [Content Fragments Support in AEM Assets HTTP API](content-fragments/content-fragments.md).

In AEM a folder has the following components:

* Entities: The children of Assets are its renditions.
* Properties
* Links

The Assets HTTP API provides the following features:

* Retrieve a folder listing
* Create a folder
* Create an asset (deprecated)
* Update asset binary (deprecated)
* Update asset metadata
* Create an asset rendition
* Update an asset rendition
* Create an asset comment
* Copy a folder or asset
* Move a folder or asset
* Delete a folder, asset, or rendition

>[!NOTE]
>
>For the ease of readability the following examples omit the full cURL notation. In fact the notation does correlate with [Resty](https://github.com/micha/resty) which is a script wrapper for cURL.

<!-- TBD: The Console Manager is not available now. So how to configure the below? 

**Prerequisites**

* Go to `https://[aem_server]:[port]/system/console/configMgr`.
* Navigate to **Adobe Granite CSRF Filter**.
* Make sure the property **Filter Methods** includes: POST, PUT, DELETE.
-->

## Retrieve a folder listing {#retrieve-a-folder-listing}

Retrieves a Siren representation of an existing folder and of its child entities (subfolders or assets).

**Request**

```
GET /api/assets/myFolder.json
```

**Response codes**

```
200 - OK - success
404 - NOT FOUND - folder does not exist or is not accessible
500 - INTERNAL SERVER ERROR - if something else goes wrong
```

**Response**

The class of the entity returned is assets/folder.

Properties of contained entities are a subset of the full set of properties of each entity. In order to obtain a full representation of the entity, clients should retrieve the contents of the URL pointed to by the link with a `rel` of `self`.

## Create a folder {#create-a-folder}

Creates a new `sling`: `OrderedFolder` at the given path. If a &#42; is given instead of a node name the servlet will use the parameter name as node name. Accepted as request data is either a Siren representation of the new folder or a set of name-value pairs, encoded as `application/www-form-urlencoded` or `multipart`/ `form`- `data`, useful for creating a folder directly from an HTML form. Additionally, properties of the folder can be specified as URL query parameters.

The operation will fail with a `500` response code if the parent node of the given path does not exist. If the folder already exists a `409` response code is returned.

**Parameters**

* `name` - Folder name

**Request**

```
POST /api/assets/myFolder -H"Content-Type: application/json" -d '{"class":"assetFolder","properties":{"title":"My Folder"}}'
```

or

```
POST /api/assets/* -F"name=myfolder" -F"title=My Folder"
```

**Response codes**

```
201 - CREATED - on successful creation
409 - CONFLICT - if folder already exist
412 - PRECONDITION FAILED - if root collection cannot be found or accessed
500 - INTERNAL SERVER ERROR - if something else goes wrong
```

## Create an asset {#create-an-asset}

See [asset upload](developer-reference-material-apis.md) for information on how to create an asset using APIs. Creating an asset using the HTTP API is deprecated.

## Update an asset binary {#update-asset-binary}

See [asset upload](developer-reference-material-apis.md) for information on how to update asset binaries using APIs. Updating an asset binary using the HTTP API is deprecated.

## Update metadata of an asset {#update-asset-metadata}

Updates the Asset metadata properties.

**Request**

```
PUT /api/assets/myfolder/myAsset.png -H"Content-Type: application/json" -d '{"class":"asset", "properties":{"dc:title":"My Asset"}}'
```

**Response codes**

```
200 - OK - if Asset has been updated successfully
404 - NOT FOUND - if Asset could not be found or accessed at the provided URI
412 - PRECONDITION FAILED - if root collection cannot be found or accessed
500 - INTERNAL SERVER ERROR - if something else goes wrong
```

## Create an asset rendition {#create-an-asset-rendition}

Creates a new asset rendition for an asset. If request parameter name is not provided the file name is used as rendition name.

**Parameters**

* `name` - Rendition name
* `file` - File reference

**Request**

```
POST /api/assets/myfolder/myasset.png/renditions/web-rendition -H"Content-Type: image/png" --data-binary "@myRendition.png"
```

or

```
POST /api/assets/myfolder/myasset.png/renditions/* -F"name=web-rendition" -F"file=@myRendition.png"
```

**Response codes**

```
201 - CREATED - if Rendition has been created successfully
404 - NOT FOUND - if Asset could not be found or accessed at the provided URI
412 - PRECONDITION FAILED - if root collection cannot be found or accessed
500 - INTERNAL SERVER ERROR - if something else goes wrong
```

## Update an asset rendition {#update-an-asset-rendition}

Updates respectively replaces an asset rendition with the new binary data.

**Request**

```
PUT /api/assets/myfolder/myasset.png/renditions/myRendition.png -H"Content-Type: image/png" --data-binary @myRendition.png
```

**Response codes**

```
200 - OK - if Rendition has been updated successfully
404 - NOT FOUND - if Asset could not be found or accessed at the provided URI
412 - PRECONDITION FAILED - if root collection cannot be found or accessed
500 - INTERNAL SERVER ERROR - if something else goes wrong
```

## Create an asset comment {#create-an-asset-comment}

Creates a new asset comment.

**Parameters**

* `message` - Message
* `annotationData` - Annotation data (JSON)

**Request**

```
POST /api/assets/myfolder/myasset.png/comments/* -F"message=Hello World." -F"annotationData={}"
```

**Response codes**

```
201 - CREATED - if Comment has been created successfully
404 - NOT FOUND - if Asset could not be found or accessed at the provided URI
412 - PRECONDITION FAILED - if root collection cannot be found or accessed
500 - INTERNAL SERVER ERROR - if something else goes wrong
```

## Copy a folder or an asset {#copy-a-folder-or-asset}

Copies a folder or asset at the given path to a new destination.

**Request Headers**

```
X-Destination - a new destination URI within the API solution scope to copy the resource to
X-Depth - either 'infinity' or '0'. The value '0' only copies the resource and its properties, no children.
X-Overwrite - 'F' to prevent overwriting an existing destination
```

**Request**

```
COPY /api/assets/myFolder -H"X-Destination: /api/assets/myFolder-copy"
```

**Response codes**

```
201 - CREATED - if folder/asset has been copied to a non-existing destination
204 - NO CONTENT - if the folder/asset has been copied to an existing destination
412 - PRECONDITION FAILED - if a request header is missing or
500 - INTERNAL SERVER ERROR - if something else goes wrong
```

## Move a folder or an asset {#move-a-folder-or-asset}

Moves a folder or asset at the given path to a new destination.

**Request Headers**

```
X-Destination - a new destination URI within the API solution scope to copy the resource to
X-Depth - either 'infinity' or '0'. The value '0' only copies the resource and its properties, no children.
X-Overwrite - either 'T' to force deletion of existing resources or 'F' to prevent overwriting an existing resource.
```

**Request**

```
MOVE /api/assets/myFolder -H"X-Destination: /api/assets/myFolder-moved"
```

**Response codes**

```
201 - CREATED - if folder/asset has been copied to a non-existing destination
204 - NO CONTENT - if the folder/asset has been copied to an existing destination
412 - PRECONDITION FAILED - if a request header is missing or
500 - INTERNAL SERVER ERROR - if something else goes wrong
```

## Delete a folder, an asset, or a rendition {#delete-a-folder-asset-or-rendition}

Deletes a resource (-tree) at the given path.

**Request**

```
DELETE /api/assets/myFolder
```

or

```
DELETE /api/assets/myFolder/myAsset.png
```

or

```xml
DELETE /api/assets/myFolder/myAsset.png/renditions/original
```

**Response codes**

```
200 - OK - if folder has been deleted successfully
412 - PRECONDITION FAILED - if root collection cannot be found or accessed
500 - INTERNAL SERVER ERROR - if something else goes wrong
```

