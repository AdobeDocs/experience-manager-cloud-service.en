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

With Adobe Experience Manager (AEM) as a Cloud Service, you can use Content Fragments, together with the AEM GraphQL API, to realize headless delivery of structured content for use in your applications.

>[!NOTE]
>AEM GraphQL API is a customized implementation, based on standard GraphQL.

## GraphQL - An Introduction {#graphql-introduction}

### GraphQL {#graphql}

GraphQL is an open-source specification that provides:

* a query language that enables you to select specific content from structured objects.
* a runtime to fulfil these queries with your structured content.

GraphQL is a *strongly* typed API. This means that *all* content must be clearly structured and organized by type, so that GraphQL *understands* what to access and how. The data fields are defined within GraphQL schemas, that define the structure of your content objects. 

GraphQL endpoints then provide the paths that respond to the GraphQL queries.

All this means that your app can accurately, reliably and efficiently select the data that it needs - just what you need when used with AEM.

>[!NOTE]
>
>See *GraphQL*.org and *GraphQL*.com.

### AEM and GraphQL {#aem-graphql}

GraphQL is used in various locations in AEM:

* Commerce
  * There are GraphQL integrations between AEM and various third-party commerce solutions, used with the extension hooks provided by the CIF Core Components.
* Content Fragments
  * A customized API has been developed for this use-case.
  * This is the AEM GraphQL API.

>[!NOTE]
>
>Currently, this step of the Headless Journey is only concerned with the AEM GraphQL API and Content Fragments.

### AEM GraphQL API {#aem-graphql-api}

The AEM GraphQL API is a customized version of the standard GraphQL API, specially configured to allow you to perform (complex) queries on your Content Fragments.

Content Fragments are used, as the content is structured according to Content Fragment Models. This fulfils a basic requirement of GraphQL.

* A Content Fragment Model is built up of one, or more, fields. 
  * Each field is defined according to a Data Type.
* Content Fragment Models are used to generate the corresponding AEM GraphQL Schemas.

The content returned can then be used by your applications.

>[!NOTE]
>
>The AEM GraphQL API implementation is based on the GraphQL Java libraries.

### Content Fragments for use with the AEM GraphQL API {#content-fragments-use-with-aem-graphql-api}

Content Fragments can be used as a basis for GraphQL for AEM queries as:

* They enable you to design, create, curate and publish page-independent content.
* They are based on a Content Fragment Model, which predefines the structure for the resulting fragment by means of defined data types.
* The Fragment Reference, available when defining a model, can be used to define additional layers of structure.
 
#### Content Fragment Models {#content-fragments-models}

These Content Fragment Models:

* Are used to generate the Schemas, once **Enabled**.

* Provide the data types and fields required for GraphQL. They ensure that your application only requests what is possible, and receives what is expected.

* The data type **Fragment References** can be used in your model to reference another Content Fragment, and so introduce additional levels of structure.

#### Fragment References {#fragment-references}

The **Fragment Reference**:

* Is of particular interest in conjunction with GraphQL.

* Is a specific data type that can be used when defining a Content Fragment Model.

* References another fragment, dependent on a specific Content Fragment Model.

* Allows you to retrieve structured data.

  * When defined as a **multifeed**, multiple sub-fragments can be referenced (retrieved) by the prime fragment.

#### JSON Preview {#json-preview}

To help with designing and developing your Content Fragment Models, you can preview [JSON output](/help/assets/content-fragments/content-fragments-json-preview.md) in the Content Fragment Editor.

### AEM GraphQL Endpoints {#aem-graphql-endpoints}

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

### The AEM GraphiQL Interface {#aem-graphiql-interface}

An implementation of the standard GraphiQL interface is available for use with AEM GraphQL. This can be installed with AEM.

This interface allows you to directly input, and test, queries. It provides features such as syntax-highlighting, auto-complete, auto-suggest, together with a history and online documentation.

![GraphiQL Interface](assets/graphiql-interface.png "GraphiQL Interface")

## Using the AEM GraphQL API {#using-aem-graphiql}

### Endpoints {#endpoints}

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
  * [Learning to use GraphQL with AEM - Sample Content and Queries](/help/assets/content-fragments/content-fragments-graphql-samples.md)
  * [Authentication for Remote AEM GraphQL Queries on Content Fragments](/help/assets/content-fragments/graphql-authentication-content-fragments.md)
* [Working with Content Fragments](/help/assets/content-fragments/content-fragments.md)
  * [Content Fragment Models](/help/assets/content-fragments/content-fragments-models.md)
  * [JSON output](/help/assets/content-fragments/content-fragments-json-preview.md)
* [Getting Started with AEM Headless](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/graphql/overview.html) - A short video tutorial series giving an overview of using AEM's headless features, including data modeling and GraphQL.
