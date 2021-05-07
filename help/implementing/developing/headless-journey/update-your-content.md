---
title: How to Update Your Content via AEM Assets APIs
description: In this part of the AEM Headless Developer Journey, learn how to use the REST API to access and update the content of your Content Fragments.
hide: yes
hidefromtoc: yes
index: no
exl-id: 8d133b78-ca36-4c3b-815d-392d41841b5c
---
# How to Update Your Content via AEM Assets APIs {#update-your-content}

>[!CAUTION]
>
>WORK IN PROGRESS - The creation of this document is ongoing and it should not be understood as complete or definitive nor should it be used for production purposes.

In this part of the [AEM Headless Developer Journey,](overview.md) learn how to use the REST API to access and update the content of your Content Fragments.

## The Story So Far {#story-so-far}

In the previous document of the AEM headless journey, [How to Access Your Content via AEM Delivery APIs](access-your-content.md) you learned how to access your headless content in AEM via the AEM GraphQL API and you should now:

* Have a high-level understanding of GraphQL.
* Understand how the AEM GraphQL API works.
* Understand some practical sample queries.

This article builds on those fundamentals so you understand how to update your existing headless content in AEM via the REST API.

## Objective {#objective}

* **Audience**: Advanced
* **Objective**: Learn how to use the REST API to access and update the content of your Content Fragments:
  * Introduce the AEM Assets HTTP API.
  * Introduce and discuss Content Fragment support in the API.
  * Illustrate details of the API.

<!--
  * Look at sample code to see how things work in practice.
-->

## Why do You Need the Assets HTTP API for Content Fragment {#why-http-api}

In the previous stage of the Headless Journey, you learned about using the AEM GraphQL API to retrieve your content using queries.

So why is another API needed?

The Assets HTTP API does allow you to **Read** your content, but it also allows you to **Create**, **Update** and **Delete** content - actions that are not possible with the GraphQL API.

## Assets HTTP API {#assets-http-api}

The [Assets HTTP API](/help/assets/mac-api-assets.md) encompasses the:

* Assets REST API
* including support for Content Fragments

The current implementation of the Assets HTTP API is based on the **REST** architectural style.

The Assets REST API allows developers for Adobe Experience Manager as a Cloud Service to access content (stored in AEM) directly over the HTTP API, via **CRUD** operations (Create, Read, Update, Delete).

The API allows you to operate Adobe Experience Manager as a Cloud Service as a headless CMS (Content Management System) by providing Content Services to a JavaScript front end application. Or any other application that can execute HTTP requests and handle JSON responses.

For example, Single Page Applications (SPA), framework-based or custom, require content provided over an API, often in JSON format.

While AEM Core Components provide a very comprehensive, flexible and customizable API that can serve required Read operations for this purpose, and whose JSON output can be customized, they do require AEM WCM (Web Content Management) know-how for implementation as they must be hosted in pages that are based on dedicated AEM templates. Not every SPA development organization has direct access to such knowledge.

This is when the Assets REST API can be used. It allows developers to access assets (for example, images and content fragments) directly, without the need to first embed them in a page, and deliver their content in serialized JSON format. 

>[!NOTE]
>
>It is not possible to customize JSON output from the Assets REST API. 

The Assets REST API also allows developers to modify content - by creating new, updating, or deleting existing assets, content fragments and folders.

The Assets REST API:

* follows the HATEOAS principle
* implements the SIREN format

## Prerequisites {#prerequisites}

The Assets REST API is available on each out-of-the-box install of a recent Adobe Experience Manager as a Cloud Service version.

## Key Concepts {#key-concepts}

The Assets REST API offers REST-style access to assets stored within an AEM instance. 

It uses the `/api/assets` endpoint and requires the path of the asset to access it (without the leading `/content/dam`). 

* This means that to access the asset at:
  * `/content/dam/path/to/asset`
* You need to request:
  * `/api/assets/path/to/asset` 

For example, to access `/content/dam/wknd/en/adventures/cycling-tuscany`, request `/api/assets/wknd/en/adventures/cycling-tuscany.json` 

>[!NOTE]
>Access over:
>
>* `/api/assets` **does not** need the use of the `.model` selector.
>* `/content/path/to/page` **does** require the use of the `.model` selector.

The HTTP method determines the operation to be executed:

* **GET** - to retrieve a JSON representation of an asset or a folder
* **POST** - to create new assets or folders
* **PUT** - to update the properties of an asset or folder
* **DELETE** - to delete an asset or folder

>[!NOTE]
>
>The request body and/or URL parameters can be used to configure some of these operations; for example, define that a folder or an asset should be created by a **POST** request.

The exact format of supported requests is defined in the API Reference documentation. 

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
   <td>Supported use-case(s)</td>
   <td>General purpose.</td>
   <td><p>Optimized for consumption in a Single Page Application (SPA), or any other (content consuming) context.</p> <p>Can also contain layout information.</p> </td>
  </tr>
  <tr>
   <td>Supported operations</td>
   <td><p>Create, Read, Update, Delete.</p> <p>With additional operations depending on the entity type.</p> </td>
   <td>Read-only.</td>
  </tr>
  <tr>
   <td>Access</td>
   <td><p>Can be accessed directly.</p> <p>Uses the <code>/api/assets </code>endpoint, mapped to <code>/content/dam</code> (in the repository).</p> 
   <p>An example path would look like: <code>/api/assets/wknd/en/adventures/cycling-tuscany.json</code></p>
   </td>
    <td><p>Needs to be referenced through an AEM component on an AEM page.</p> <p>Uses the <code>.model</code> selector to create the JSON representation.</p> <p>An example path would look like:<br/> <code>/content/wknd/language-masters/en/adventures/cycling-tuscany.model.json</code></p> 
   </td>
  </tr>
  <tr>
   <td>Security</td>
   <td><p>Multiple options are possible.</p> <p>OAuth is proposed; can be configured separately from standard setup.</p> </td>
   <td>Uses AEM's standard setup.</td>
  </tr>
  <tr>
   <td>Architectural remarks</td>
   <td><p>Write access will typically address an author instance.</p> <p>Read may also be directed to a publish instance.</p> </td>
   <td>As this approach is read-only, it will typically be used for publish instances.</td>
  </tr>
  <tr>
   <td>Output</td>
   <td>JSON-based SIREN output: verbose, but powerful. Allows for navigating within the content.</td>
   <td>JSON-based proprietary output; configurable through Sling Models. Navigating the content structure is hard to implement (but not necessarily impossible).</td>
  </tr>
 </tbody>
</table>

### Security {#security}

If the Assets REST API is used within an environment without specific authentication requirements, AEM's CORS filter needs to be configured correctly.

>[!NOTE]
>
>For further information see:
>
>* CORS/AEM explained
>* Video - Developing for CORS with AEM
>

In environments with specific authentication requirements, OAuth is recommended.

## Available Features {#available-features}

Content Fragments are a specific type of Asset, see Working with Content Fragments.

For further information about features available through the API see:

* The Assets REST API  
* Entity Types, where the features specific to each supported type (as relevant to Content Fragments) are explained 

### Paging {#paging}

The Assets REST API supports paging (for GET requests) via the URL parameters:

* `offset` - the number of the first (child) entity to retrieve
* `limit` - the maximum number of entities returned

The response will contain paging information as part of the `properties` section of the SIREN output. This `srn:paging` property contains the total number of (child) entities ( `total`), the offset and the limit ( `offset`, `limit`) as specified in the request.

>[!NOTE]
>
>Paging is typically applied on container entities (i.e. folders or assets with renditions), as it relates to the children of the requested entity.

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

The Assets REST API exposes access to the properties of a folder; for example its name, title, etc. Assets are exposed as child entities of folders, and sub-folders.

>[!NOTE]
>
>Depending on the asset type of the child assets and folders the list of child entities may already contain the full set of properties that defines the respective child entity. Alternatively, only a reduced set of properties may be exposed for an entity in this list of child entities.

### Assets {#assets}

If an asset is requested, the response will return its metadata; such as title, name and other information as defined by the respective asset schema.

The binary data of an asset is exposed as a SIREN link of type `content`.

Assets can have multiple renditions. These are typically exposed as child entities, one exception being a thumbnail rendition, which is exposed as a link of type `thumbnail` ( `rel="thumbnail"`).

### Content Fragments {#content-fragments}

A Content Fragment is a special type of asset. They can be used to access structured data, such as texts, numbers, dates, amongst others.

As there are several differences to *standard* assets (such as images or audio), some additional rules apply to handling them.

#### Representation {#representation}

Content fragments:

* Do not expose any binary data.
* Are completely contained in the JSON output (within the `properties` property).

* Are also considered atomic, i.e. the elements and variations are exposed as part of the fragment's properties vs. as links or child entities. This allows for efficient access to the payload of a fragment.

#### Content Models and Content Fragments {#content-models-and-content-fragments}

Currently the models that define the structure of a content fragment are not exposed through an HTTP API. Therefore the *consumer* needs to know about the model of a fragment (at least a minimum) - although most information can be inferred from the payload; as data types, etc. are part of the definition.

To create a new content fragment, the (internal repository) path of the model has to be provided.

#### Associated Content {#associated-content}

Associated content is currently not exposed.

## Using the Assets REST API {#using-aem-assets-rest-api}

For the details of using the AEM Assets REST API, you can reference:

* Adobe Experience Manager Assets HTTP API
* Content Fragments Support in AEM Assets HTTP API
  
## What's Next {#whats-next}

Now that you have completed this part of the AEM Headless Developer Journey, you should:

* Understand the AEM Assets HTTP API.
* Understand how Content Fragments are supported in this API.

<!--
* Have experience with sample code and know how the API works in practice.
-->

You should continue your AEM headless journey by next reviewing the document [How to Put It All Together - Your App and Your Content in AEM Headless](put-it-all-together.md) where you learn how to take your AEM Headless project and prepare it for going live.

## Additional Resources {#additional-resources}

* [REST](https://en.wikipedia.org/wiki/Representational_state_transfer)
* [HATEOAS principle](https://en.wikipedia.org/wiki/HATEOAS)
* [SIREN format](https://github.com/kevinswiber/siren)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Content Fragments REST API](/help/assets/content-fragments/assets-api-content-fragments.md)
  * [API Reference](/help/assets/content-fragments/assets-api-content-fragments.md#api-reference)
* [Working with Content Fragments](/help/assets/content-fragments/content-fragments.md)
* [AEM Core Components](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/introduction.html)
* [CORS/AEM explained](https://helpx.adobe.com/experience-manager/kt/platform-repository/using/cors-security-article-understand.html)
* [Video - Developing for CORS with AEM](https://helpx.adobe.com/experience-manager/kt/platform-repository/using/cors-security-technical-video-develop.html)

