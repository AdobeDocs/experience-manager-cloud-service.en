---
title: How to Access Your Content via AEM Delivery APIs
description: In this part of the AEM Headless Developer Journey, learn how to use GraphQL queries to access your Content Fragments content.
hide: yes
hidefromtoc: yes
index: no
exl-id: 5ef557ff-e299-4910-bf8c-81c5154ea03f
---
# How to Access Your Content via AEM Delivery APIs {#access-your-content}

>[!CAUTION]
>
>WORK IN PROGRESS - The creation of this document is ongoing and it should not be understood as complete or definitive nor should it be used for production purposes.

In this part of the [AEM Headless Developer Journey,](overview.md) you can learn how to use GraphQL queries to access the content of your Content Fragments.

## The Story So Far {#story-so-far}

In the previous document of the AEM headless journey, [How to Model Your Content](model-your-content.md) you learned the basics of data modeling in AEM, so you should now understand how to model your content structure, then realize that structure using AEM Content Fragment Models and Content Fragments:

* Recognize the concepts and terminology related to [data modeling](#data-modeling).
* Understand [why data modeling is needed for Headless content delivery](#data-modeling-for-aem-headless).
* Understand [how to realize this structure using AEM Content Fragment Models](#create-structure-content-fragment-models) (and author content with [Content Fragments](#use-content-to-author-content)).
* Understand [how to model your content](#getting-started-examples); principles with basic samples.

This article builds on those fundamentals so you understand how to access your existing headless content in AEM using the AEM GraphQL API.

* **Audience**: Beginner
* **Objective**: Learn how to access the content of your Content Fragments using AEM GraphQL queries:
  * Introduce GraphQL and the AEM GraphQL API.
  * Dive into the details of the AEM GraphQL API.
  * Look at some sample queries to see how things work in practice.

## So You'd Like to Access Your Data? {#so-youd-like-to-access-your-data}

So...you've got all this content, neatly structured (in Content Fragments), and just waiting to feed your new app. Question is - how to get it there?

What you need is a way to target specific content, select what you need and return it to your app for further processing.

With Adobe Experience Manager (AEM) as a Cloud Service, you can selectively access your Content Fragments using the AEM GraphQL API, to realize headless delivery of structured content for use in your applications. AEM GraphQL API is a customized implementation, based on standard GraphQL.

## GraphQL - An Introduction {#graphql-introduction}

GraphQL is an open-source specification that provides:

* a query language that enables you to select specific content from structured objects.
* a runtime to fulfil these queries with your structured content.

GraphQL is a *strongly* typed API. This means that *all* content must be clearly structured and organized by type, so that GraphQL *understands* what to access and how. The data fields are defined within GraphQL schemas, that define the structure of your content objects. 

GraphQL endpoints then provide the paths that respond to the GraphQL queries.

All this means that your app can accurately, reliably and efficiently select the data that it needs - just what you need when used with AEM.

>[!NOTE]
>
>See *GraphQL*.org and *GraphQL*.com.

## AEM and GraphQL {#aem-graphql}

GraphQL is used in various locations in AEM:

* Commerce
  * There are GraphQL integrations between AEM and various third-party commerce solutions, used with the extension hooks provided by the CIF Core Components.
* Content Fragments
  * A customized API has been developed for this use-case.
  * This is the AEM GraphQL API.

>[!NOTE]
>
>This step of the Headless Journey is only concerned with the AEM GraphQL API and Content Fragments.

## AEM GraphQL API {#aem-graphql-api}

The AEM GraphQL API is a customized version of the standard GraphQL API, specially configured to allow you to perform (complex) queries on your Content Fragments.

Content Fragments are used, as the content is structured according to Content Fragment Models. This fulfils a basic requirement of GraphQL.

* A Content Fragment Model is built up of one, or more, fields. 
  * Each field is defined according to a Data Type.
* Content Fragment Models are used to generate the corresponding AEM GraphQL Schemas.

To actually access GraphQL for AEM (and the content) an endpoint is used to provide the access path. 

The content returned, via the AEM GraphQL API, can then be used by your applications. 

>[!NOTE]
>
>The AEM GraphQL API implementation is based on the GraphQL Java libraries.

## Content Fragments for use with the AEM GraphQL API {#content-fragments-use-with-aem-graphql-api}

Content Fragments can be used as a basis for GraphQL for AEM schemas amd queries as:

* They enable you to design, create, curate and publish page-independent content.
* They are based on a Content Fragment Model, which predefines the structure for the resulting fragment by means of defined data types.
* The Fragment Reference, available when defining a model, can be used to define additional layers of structure.
 
### Content Fragment Models {#content-fragments-models}

These Content Fragment Models:

* Are used to generate the Schemas, once **Enabled**.

* Provide the data types and fields required for GraphQL. They ensure that your application only requests what is possible, and receives what is expected.

* The data type **Fragment References** can be used in your model to reference another Content Fragment, and so introduce additional levels of structure.

### Fragment References {#fragment-references}

The **Fragment Reference**:

* Is of particular interest in conjunction with GraphQL.

* Is a specific data type that can be used when defining a Content Fragment Model.

* References another fragment, dependent on a specific Content Fragment Model.

* Allows you to retrieve structured data.

  * When defined as a **multifeed**, multiple sub-fragments can be referenced (retrieved) by the prime fragment.

### JSON Preview {#json-preview}

To help with designing and developing your Content Fragment Models, you can preview [JSON output](/help/assets/content-fragments/content-fragments-json-preview.md) in the Content Fragment Editor.


## GraphQL Schema Generation from Content Fragments {#graphql-schema-generation-content-fragments}

GraphQL is a strongly typed API, which means that data must be clearly structured and organized by type.

The GraphQL specification provides a series of guidelines on how to create a robust API for interrogating data on a certain instance. To do this, a client needs to fetch the [Schema](#schema-generation), which contains all the types necessary for a query. 

For Content Fragments, the GraphQL schemas (structure and types) are based on **Enabled** Content Fragment Models and their data types.

>[!CAUTION]
>
>All the GraphQL schemas (derived from Content Fragment Models that have been **Enabled**) are readable through the GraphQL endpoint.
>
>This means that you need to ensure that no sensitive data is available, as it could be leaked this way; for example, this includes information that could be present as field names in the model definition.

For example, if a user created a Content Fragment Model called `Article`, then AEM generates the object `article` that is of a type `ArticleModel`. The fields within this type correspond to the fields and data types defined in the model.

1. A Content Fragment Model:

   ![Content Fragment Model for use with GraphQL](assets/cfm-graphqlapi-01.png "Content Fragment Model for use with GraphQL")

1. The corresponding GraphQL schema (output from GraphiQL automatic documentation):
   ![GraphQL Schema based on Content Fragment Model](assets/cfm-graphqlapi-02.png "GraphQL Schema based on Content Fragment Model")

   This shows that the generated type `ArticleModel` contains several [fields](#fields). 
   
   * Three of them have been controlled by the user: `author`, `main` and `referencearticle`.

   * The other fields were added automatically by AEM, and represent helpful methods to provide information about a certain Content Fragment; in this example, `_path`, `_metadata`, `_variations`. These [helper fields](#helper-fields) are marked with a preceding `_` to distinguish between what has been defined by the user and what has been auto-generated.

1. After a user creates a Content Fragment based on the Article model, it can then be interrogated through GraphQL. For examples, see the Sample Queries.md#graphql-sample-queries) (based on a sample Content Fragment structure for use with GraphQL.

In GraphQL for AEM, the schema is flexible. This means that it is auto-generated each and every time a Content Fragment Model is created, updated or deleted. The data schema caches are also refreshed when you update a Content Fragment Model.

The Sites GraphQL service listens (in the background) for any modifications made to a Content Fragment Model. When updates are detected, only that part of the schema is regenerated. This optimization saves time and provides stability.

So for example, if you:

1. Install a package containing `Content-Fragment-Model-1` and `Content-Fragment-Model-2`:
 
   1. GraphQL types for `Model-1` and `Model-2` will be generated.

1. Then modify `Content-Fragment-Model-2`:

   1. Only the `Model-2` GraphQL type will get updated.

   1. Whereas `Model-1` will remain the same. 

>[!NOTE]
>
>This is important to note in case you want to do bulk updates on Content Fragment Models through the REST api, or otherwise.

The schema is served through the same endpoint as the GraphQL queries, with the client handling the fact that the schema is called with the extension `GQLschema`. For example, performing a simple `GET` request on `/content/cq:graphql/global/endpoint.GQLschema` will result in the output of the schema with the Content-type: `text/x-graphql-schema;charset=iso-8859-1`.

### Schema Generation - Unpublished Models {#schema-generation-unpublished-models}

When Content Fragments are nested it can happen that a parent Content Fragment Model is published, but a referenced model is not.

>[!NOTE]
>
>The AEM UI prevents this happening, but if publishing is made programmatically, or with content packages, it can occur.

When this happens, AEM generates an *incomplete* Schema for the parent Content Fragment Model. This means that the Fragment Reference, which is dependent on the unpublished model, is removed from the schema.

## AEM GraphQL Endpoints {#aem-graphql-endpoints}

<!--
need details/examples
-->

An endpoint is the path used to access GraphQL for AEM. Using this path you (or your app) can:

* access the GraphQL schemas,
* send your GraphQL queries,
* receive the responses (to your GraphQL queries).

AEM allows for:

* A global endpoint - available for use by all sites.
* Tenant endpoints - that you can configure, specific to a specified site/project.

## The AEM GraphiQL Interface {#aem-graphiql-interface}

To help you directly input, and test queries, an implementation of the standard GraphiQL interface is available for use with AEM GraphQL. This can be installed with AEM.

It provides features such as syntax-highlighting, auto-complete, auto-suggest, together with a history and online documentation.

![GraphiQL Interface](assets/graphiql-interface.png "GraphiQL Interface")

<!--
new page?
-->

## Using the AEM GraphQL API {#using-aem-graphiql}

### Endpoints {#endpoints}

The repository path of the GraphQL for AEM global endpoint is:

`/content/cq:graphql/global/endpoint`

For which your app can use the following path in the request URL:

`/content/_cq_graphql/global/endpoint.json`

To enable an endpoint for GraphQL for AEM you need to:

* Enable your GraphQL Endpoint
* Publish your Endpoint

### Enabling your GraphQL Endpoint {#enabling-graphql-endpoint}

To enable a GraphQL Endpoint you first need to have an appropriate configuration in the Configuration Browser.

>[!CAUTION]
>
>If the use of content fragment models have not been enabled, the **Create** option will not be available.

To enable the corresponding endpoint:

1. Navigate to **Tools**, **Sites**, then select **GraphQL**.
1. Select **Create**.
1. The **Create new GraphQL Endpoint** dialog will open. Here you can specify:
   * **Name**: name of the endpoint; you can enter any text.
   * **Use GraphQL schema provided by**: use the dropdown to select the required site/project.

   >[!NOTE]
   >
   >The following warning is shown in the dialog:
   >
   >* *GraphQL endpoints may introduce data security and performance issues if not managed carefully. Please ensure to set appropriate permissions after creating an endpoint.*
   
1. Confirm with **Create**.
1. The **Next steps** dialog will provide a direct link to the Security console so that you can ensure that newly created endpoint has suitable permissions.

   >[!CAUTION]
   >
   >The endpoint is accessible to everyone. This can - especially on publish instances - pose a security concern, as GraphQL queries can impose a heavy load on the server.
   >
   >You can set up ACLs, appropriate to your use case, on the endpoint. 

### Publishing your GraphQL Endpoint {#publishing-graphql-endpoint}

Select the new endpoint and **Publish** to make it fully available in all environments.

>[!CAUTION]
>
>The endpoint is accessible to everyone. 
>
>On publish instances this can pose a security concern, as GraphQL queries can impose a heavy load on the server.
>
>You must set up ACLs appropriate to your use case on the endpoint. 


### AEM GraphQL Schemas {#aem-graphql-schemas}

### AEM GraphQL Data Types {#aem-graphql-data-types}

### AEM GraphQL Variables {#aem-graphql-variables}

### AEM GraphQL Directives {#aem-graphql-directives}

### AEM GraphQL Filters {#aem-graphql-filters}

### AEM GraphQL Helper Fields {#aem-graphql-helper-fields}

### AEM GraphQL Extensions {#aem-graphql-extensions}

### AEM GraphQL Authenication {#aem-graphql-authenticaion}

## AEM GraphQL API and Content Fragments {#aem-graphql-content-fragments}



## AEM GraphQL Queries {#aem-graphql-queries}

## Samples of AEM GraphQL Queries {#samples-aem-graphql-queries}

## Code Samples for AEM GraphQL Queries {#code-samples-aem-graphql-queries}

## What's Next {#whats-next}

Now that you have learned how to access and query your headless content using the AEM GraphQL API you can now [learn how to use the REST API to access and update the content of your Content Fragments](/help/implementing/developing/headless-journey/update-your-content.md).

## Additional Resources {#additional-resources}

* [GraphQL.org](https://graphql.org)
  * [Schemas](https://graphql.org/learn/schema/)
  * [GraphQL Java libraries](https://graphql.org/code/#java)
* [GraphiQL](https://graphql.org/learn/serving-over-http/#graphiql) 
* [AEM GraphQL API for use with Content Fragments](/help/assets/content-fragments/graphql-api-content-fragments.md)
  * [The Sample Content Fragment Structure](/help/assets/content-fragments/content-fragments-graphql-samples.md#content-fragment-structure-graphql)
  * [Learning to use GraphQL with AEM - Sample Content and Queries](/help/assets/content-fragments/content-fragments-graphql-samples.md)
  * [Authentication for Remote AEM GraphQL Queries on Content Fragments](/help/assets/content-fragments/graphql-authentication-content-fragments.md)
* [Content Fragments - Configuration Browser](/help/assets/content-fragments/content-fragments-configuration-browser.md)
* [Working with Content Fragments](/help/assets/content-fragments/content-fragments.md)
  * [Content Fragment Models](/help/assets/content-fragments/content-fragments-models.md)
  * [JSON output](/help/assets/content-fragments/content-fragments-json-preview.md)
* [Getting Started with AEM Headless](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/graphql/overview.html) - A short video tutorial series giving an overview of using AEM's headless features, including data modeling and GraphQL.
