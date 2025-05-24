---
title: Adobe Experience Manager as a Cloud Service Content Fragments Support in the Assets HTTP API
description: Learn about support for Content Fragments in the Assets HTTP API, an important piece of Adobe Experience Manager's headless delivery feature.
feature: Content Fragments, Assets HTTP API
exl-id: d72cc0c0-0641-4fd6-9f87-745af5f2c232
role: User, Admin
---
# Content Fragments Support in the AEM Assets HTTP API {#content-fragments-support-in-aem-assets-http-api}

## Overview {#overview}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/content/assets/extending/assets-api-content-fragments.html)                  |
| AEM as a Cloud Service     | This article         |

Learn about support for Content Fragments in the Assets HTTP API, an important piece of Adobe Experience Manager's (AEM) headless delivery feature.

>[!NOTE]
>
>See [AEM APIs for Structured Content Delivery and Management](/help/headless/apis-headless-and-content-fragments.md) for an overview of the various APIs available and comparison of some of the concepts involved.
>
>The [Content Fragment and Content Fragment Model OpenAPIs](/help/headless/content-fragment-openapis.md) are also available.

>[!NOTE]
>
>The [Assets HTTP API](/help/assets/mac-api-assets.md) encompasses the:
>
>* Assets REST API
>* including support for Content Fragments
>
>The current implementation of the Assets HTTP API is based on the [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) architectural style.

>[!NOTE]
>
>For the latest information about Experience Manager APIs, visit [Adobe Experience Manager as a Cloud Service APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/).

The [Assets REST API](/help/assets/mac-api-assets.md) allows developers for Adobe Experience Manager as a Cloud Service to access content (stored in AEM) directly over the HTTP API, by way of CRUD (Create, Read, Update, Delete) operations.

The API lets you operate Adobe Experience Manager as a Cloud Service as a headless CMS (Content Management System) by providing Content Services to a JavaScript front-end application. Or any other application that can execute HTTP requests and handle JSON responses.

For example, [Single Page Applications (SPA)](/help/implementing/developing/hybrid/introduction.md), framework-based or custom, require content provided over the HTTP API, often in JSON format.

While [AEM Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html) provide a customizable API that can serve required Read operations for this purpose, and whose JSON output can be customized, they do require AEM WCM (Web Content Management) know-how for implementation. This is because they must be hosted in pages that are based on dedicated AEM templates. Not every SPA development organization has direct access to such knowledge.

This is when the Assets REST API can be used. It allows developers to access assets (for example, images and content fragments) directly, without the need to first embed them in a page, and deliver their content in serialized JSON format. 

>[!NOTE]
>
>It is not possible to customize JSON output from the Assets REST API. 

The Assets REST API also allows developers to modify content - by creating new, updating, or deleting existing assets, content fragments, and folders.

The Assets REST API:

* follows the [HATEOAS principle](https://en.wikipedia.org/wiki/HATEOAS)

* implements the [SIREN format](https://github.com/kevinswiber/siren)

## Prerequisites {#prerequisites}

The Assets REST API is available on each out-of-the-box install of a recent Adobe Experience Manager as a Cloud Service version.

## Key Concepts {#key-concepts}

The Assets REST API offers [REST](https://en.wikipedia.org/wiki/Representational_state_transfer)-style access to assets stored within an AEM instance. 

It uses the `/api/assets` endpoint and requires the path of the asset to access it (without the leading `/content/dam`). 

* This means that to access the asset at:
  * `/content/dam/path/to/asset`
* Request:
  * `/api/assets/path/to/asset` 

For example, to access `/content/dam/wknd/en/adventures/cycling-tuscany`, request `/api/assets/wknd/en/adventures/cycling-tuscany.json` 

>[!NOTE]
>Access over:
>
>* `/api/assets` **does not** need the use of the `.model` selector.
>* `/content/path/to/page` **does** require the use of the `.model` selector.

The HTTP method determines the operation to be executed:

* **GET** - to retrieve a JSON representation of an asset or a folder
* **POST** - to create assets or folders
* **PUT** - to update the properties of an asset or folder
* **DELETE** - to delete an asset or folder

>[!NOTE]
>
>The request body and/or URL parameters can be used to configure some of these operations; for example, define that a folder or an asset should be created by a **POST** request.

The exact format of supported requests is defined in the [API Reference](/help/assets/content-fragments/assets-api-content-fragments.md#api-reference) documentation. 

>[!NOTE]
>
>The [Content Fragment and Content Fragment Model OpenAPIs](/help/headless/content-fragment-openapis.md) are also available.

### Transactional Behavior {#transactional-behavior}

All requests are atomic.

This means that subsequent (`write`) requests cannot be combined into a single transaction that could succeed or fail as a single entity.

### AEM (Assets) REST API versus AEM Components {#aem-assets-rest-api-versus-aem-components}

<table>
 <thead>
  <tr>
   <td>Aspect</td>
   <td>Assets REST API<br/> </td>
   <td>AEM Component<br/> (components using Sling Models)</td>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>Supported use-cases</td>
   <td>General purpose.</td>
   <td><p>Optimized for consumption in a Single Page Application (SPA), or any other (content consuming) context.</p> <p>It can also contain layout information.</p> </td>
  </tr>
  <tr>
   <td>Supported operations</td>
   <td><p>Create, Read, Update, Delete.</p> <p>With additional operations, depending on the entity type.</p> </td>
   <td>Read-only.</td>
  </tr>
  <tr>
   <td>Access</td>
   <td><p>It can be accessed directly.</p> <p>Uses the <code>/api/assets </code>endpoint, mapped to <code>/content/dam</code> (in the repository).</p> 
   <p>An example path would look like: <code>/api/assets/wknd/en/adventures/cycling-tuscany.json</code></p>
   </td>
    <td><p>It must be referenced through an AEM component on an AEM page.</p> <p>Uses the <code>.model</code> selector to create the JSON representation.</p> <p>An example path would look like:<br/> <code>/content/wknd/language-masters/en/adventures/cycling-tuscany.model.json</code></p> 
   </td>
  </tr>
  <tr>
   <td>Security</td>
   <td><p>Multiple options are possible.</p> <p>OAuth is proposed; can be configured separately from the standard setup.</p> </td>
   <td>Uses AEM's standard setup.</td>
  </tr>
  <tr>
   <td>Architectural remarks</td>
   <td><p>Write access typically addresses an Author instance.</p> <p>Read may also be directed to a Publish instance.</p> </td>
   <td>Because this approach is read-only, it is typically used for Publish instances.</td>
  </tr>
  <tr>
   <td>Output</td>
   <td>JSON-based SIREN output: verbose, but powerful. It allows for navigating within the content.</td>
   <td>JSON-based proprietary output; configurable through Sling Models. Navigating the content structure is hard to implement (but not necessarily impossible).</td>
  </tr>
 </tbody>
</table>

### Security {#security}

If the Assets REST API is used within an environment without specific authentication requirements, AEM's CORS filter must be configured correctly.

>[!NOTE]
>
>For more information,  see:
>
>* [CORS/AEM explained](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/security/understand-cross-origin-resource-sharing.html)
>* [Video - Developing for CORS with AEM (04:06)](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/security/develop-for-cross-origin-resource-sharing.html)
>

In environments with specific authentication requirements, OAuth is recommended.

## Available Features {#available-features}

Content Fragments are a specific type of Asset, see [Working with Content Fragments](/help/assets/content-fragments/content-fragments.md).

For more information about features available through the API see:

* The [Assets REST API](/help/assets/mac-api-assets.md)  
* [Entity Types](/help/assets/content-fragments/assets-api-content-fragments.md#entity-types), where the features specific to each supported type (as relevant to Content Fragments) are explained 

>[!NOTE]
>
>The [Content Fragment and Content Fragment Model OpenAPIs](/help/headless/content-fragment-openapis.md) are also available.

### Paging {#paging}

The Assets REST API supports paging (for GET requests) by way of the URL parameters:

* `offset` - the number of the first (child) entity to retrieve
* `limit` - the maximum number of entities returned

The response contains paging information as part of the `properties` section of the SIREN output. This `srn:paging` property contains the total number of (child) entities ( `total`), the offset, and the limit ( `offset`, `limit`) as specified in the request.

>[!NOTE]
>
>Paging is typically applied on container entities (that is, folders or assets with renditions), as it relates to the children of the requested entity.

#### Example: Paging {#example-paging}

`GET /api/assets.json?offset=2&limit=3`

```json
...
"properties": {
    ...
    "srn:paging": {
        "total": 7,
        "offset": 2,
        "limit": 3
    }
    ...
}
...
```

## Entity Types {#entity-types}

### Folders {#folders}

Folders act as containers for assets and other folders. They reflect the structure of the AEM content repository.

The Assets REST API exposes access to the properties of a folder. For example, its name, and title. Assets are exposed as child entities of folders and subfolders.

>[!NOTE]
>
>Depending on the asset type of the child assets and folders, the list of child entities may already contain the full set of properties that defines the respective child entity. Alternatively, only a reduced set of properties may be exposed for an entity in this list of child entities.

### Assets {#assets}

If an asset is requested, the response returns its metadata; such as title, name, and other information as defined by the respective asset schema.

The binary data of an asset is exposed as a SIREN link of type `content`.

Assets can have multiple renditions. These are typically exposed as child entities, one exception being a thumbnail rendition, which is exposed as a link of type `thumbnail` ( `rel="thumbnail"`).

### Content Fragments {#content-fragments}

A [content fragment](/help/assets/content-fragments/content-fragments.md) is a special type of asset. They can be used to access structured data, such as texts, numbers, dates, among others.

As there are several differences to *standard* assets (such as images or audio), some additional rules apply to handling them.

#### Representation {#representation}

Content fragments:

* Do not expose any binary data.
* Are contained in the JSON output (within the `properties` property).

* They are also considered atomic. That is, the elements and variations are exposed as part of the fragment's properties vs. as links or child entities. This allows for efficient access to the payload of a fragment.

#### Content Models and Content Fragments {#content-models-and-content-fragments}

Currently the models that define the structure of a content fragment are not exposed through an HTTP API. Therefore, the *consumer* must know about the model of a fragment (at least a minimum) - although most information can be inferred from the payload; as data types, and so on, are part of the definition.

To create a content fragment, the (internal repository) path of the model has to be provided.

#### Associated Content {#associated-content}

Associated content is not exposed.

## Using {#using}

Usage can differ depending on whether you are using an AEM Author or Publish environment, together with your specific use case.

* It is recommended that creation is bound to an Author instance ([and currently there is no means to replicate a fragment to publish using this API](/help/assets/content-fragments/assets-api-content-fragments.md#limitations)).
* Delivery is possible from both, as AEM serves requested content in JSON format only.

  * Storage and delivery from an AEM Author instance should suffice for behind-the-firewall, media library applications.

  * For live web delivery, an AEM Publish instance is recommended.

>[!CAUTION]
>
>The Dispatcher configuration on AEM cloud instances might block access to `/api`.

>[!NOTE]
>
>See the [API Reference](/help/assets/content-fragments/assets-api-content-fragments.md#api-reference). In particular, [Adobe Experience Manager Assets API - Content Fragments](https://developer.adobe.com/experience-manager/reference-materials/cloud-service/javadoc/assets-api-content-fragments/index.html).
>
>The [Content Fragment and Content Fragment Model OpenAPIs](/help/headless/content-fragment-openapis.md) are also available.

## Limitations {#limitations}

There are a few limitations:

* **Content fragment models are currently not supported**: they cannot be read or created. To be able to create or update an existing content fragment, developers have to know the correct path to the content fragment model. Currently the only method to get an overview of these is through the administration UI.
* **References are ignored**. Currently there are no checks on whether an existing content fragment is referenced. Therefore, for example, deleting a content fragment might result in issues on a page that contains a reference to the deleted Content Fragment.
* **JSON data type** The REST API output of the *JSON data type* is *string-based output*.

## Status Codes and Error Messages {#status-codes-and-error-messages}

The following status codes can be seen in the relevant circumstances:

* **200** (OK)

  Returned when:

  * requesting a content fragment by way of `GET`
  * successfully updating a content fragment by way of `PUT`

* **201** (Created)

  Returned when:

  * successfully creating a content fragment by way of `POST`

* **404** (Not found)

  Returned when:

  * the requested content fragment does not exist

* **500** (Internal server error)

  >[!NOTE]
  >
  >This error is returned:
  >
  >* when an error that cannot be identified with a specific code has happened
  >* when the given payload was not valid

  The following lists common scenarios when this error status is returned, together with the error message (monospace) generated:

  * Parent folder does not exist (when creating a content fragment by way of `POST`)
  * No content fragment model is supplied (cq:model is missing), cannot be read (due to an invalid path or a permission problem) or there is no valid fragment model:

    * `No content fragment model specified`
    * `Cannot create a resource of given model '/foo/bar/qux'`

  * The content fragment could not be created (potentially a permission problem):

    * `Could not create content fragment`

  * Title and or description could not be updated:

    * `Could not set value on content fragment`

  * Metadata could not be set:

    * `Could not set metadata on content fragment`

  * Content element could not be found or could not be updated

    * `Could not update content element`
    * `Could not update fragment data of element`

  The detailed error messages are returned in the following manner:

  ```xml
  {
    "class": "core/response",
    "properties": {
      "path": "/api/assets/foo/bar/qux",
      "location": "/api/assets/foo/bar/qux.json",
      "parentLocation": "/api/assets/foo/bar.json",
      "status.code": 500,
      "status.message": "...{error message}.."
    }
  }
  ```

## API Reference {#api-reference}

See here for detailed API references:

* [Adobe Experience Manager Assets API - Content Fragments](https://developer.adobe.com/experience-manager/reference-materials/cloud-service/javadoc/assets-api-content-fragments/index.html)

* [Assets HTTP API](/help/assets/mac-api-assets.md)

  * [Available Features](/help/assets/mac-api-assets.md#available-features)

* The [Content Fragment and Content Fragment Model OpenAPIs](/help/headless/content-fragment-openapis.md) are also available.

## Additional Resources {#additional-resources}

For more information, see:

* [Assets HTTP API documentation](/help/assets/mac-api-assets.md)
* [AEM Gem session: OAuth](https://experienceleague.adobe.com/docs/events/experience-manager-gems-recordings/gems2014/aem-oauth-server-functionality-in-aem.html)
