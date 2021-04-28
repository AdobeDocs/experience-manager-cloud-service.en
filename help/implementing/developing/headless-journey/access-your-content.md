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

In the previous document of the AEM headless journey, [How to Model Your Content](model-your-content.md) you learned the basics of data modeling in AEM and you should now:

* Understand how to model your content structure, then realize that structure using AEM Content Fragment Models and Content Fragments:
* Recognize the concepts and terminology related to [data modeling](#data-modeling).
* Understand [why data modeling is needed for Headless content delivery](#data-modeling-for-aem-headless).
* Understand [how to realize this structure using AEM Content Fragment Models](#create-structure-content-fragment-models) (and author content with [Content Fragments](#use-content-to-author-content)).
* Understand [how to model your content](#getting-started-examples); principles with basic samples.

This article builds on those fundamentals so you understand how to access your existing headless content in AEM via API.

* **Audience**: Beginner
* **Objective**: Learn how to access the content of your Content Fragments using AEM GraphQL queries:
  * Introduce GraphQL.
  * Introduce AEM GraphQL API.
  * Dive into the details of the AEM GraphQL API.
  * Look at some sample queries to see how things work in practice.

With Adobe Experience Manager (AEM) as a Cloud Service, you can use Content Fragments, together with the AEM GraphQL API, to headlessly deliver structured content for use in your applications. The ability to customize a single API query allows you to retrieve and deliver the specific content that you want/need to render (as the response to the single API query).

>[!NOTE]
>AEM GraphQL API is a customized implementation, based on standard GraphQL.

## GraphQL - An Introduction {#graphql-introduction}

GraphQL:

* "*...is a query language for APIs and a runtime for fulfilling those queries with your existing data.*".
* "*...queries access not just the properties of one resource but also smoothly follow references between them.*".
* "*...APIs get all the data your app needs in a single request.*".
* "*...APIs are organized in terms of types and fields, not endpoints. Access the full capabilities of your data from a single endpoint.*".

See *GraphQL*.org.

### GraphQL - Queries {#graphql-queries}

GraphQL provides a query language that enables you to select content from structured objects.

### GraphQL - Schemas {#graphql-schemas}

The schemas define the structure of your content objects. 

### GraphQL - Types {#graphql-types}

Your content must be structured, according to predefined data types, so that GraphQL *understands* what to access and how. 

GraphQL is a *strongly* typed API, which means that *all* content must be clearly structured and organized by type.

## AEM and GraphQL {#aem-graphql}

GraphQL is used in various locations in AEM:

* Commerce
  * Placeholder
* Content Fragments
  * A customized API has been developed for this use-case.
  * This is the AEM GraphQL API.

## AEM GraphQL API {#aem-graphql-api}

The AEM GraphQL API allows you to perform (complex) queries on your Content Fragments.

Content Fragments are used, as the content is structured according to Content Fragment Models. 

* A Content Fragment Model is built up of one, or more, fields. 
  * Each field is defined according to a Data Type.
* AEM GraphQL Schemas are derived from the corresponding Content Fragment Models.

The content returned can then be used by your applications.

>[!NOTE]
>
>The AEM GraphQL API implementation is based on the GraphQL Java libraries.

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

### Content Fragments for use with the AEM GraphQL API {#content-fragments-use-with-aem-graphql-api}

Content Fragments can be used as a basis for GraphQL for AEM queries as:

* They enable you to design, create, curate and publish page-independent content.
* The Content Fragment Models provide the required structure by means of defined data types.
* The Fragment Reference, available when defining a model, can be used to define additional layers of structure.

### Content Fragments {#content-fragments}

Content Fragments:

* Contain structured content.

* They are based on a Content Fragment Model, which predefines the structure for the resulting fragment.
  
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

To help with designing and developing your Content Fragment Models, you can preview [JSON output](/help/assets/content-fragments/content-fragments-json-preview.md).

## AEM GraphQL Queries {#aem-graphql-queries}

## The AEM GraphiQL Interface {#aem-graphiql-interface}

## Samples of AEM GraphQL Queries {#samples-aem-graphql-queries}

## Code Samples for AEM GraphQL Queries {#code-samples-aem-graphql-queries}

## What's Next {#whats-next}

[Learn how to use the REST API to access and update the content of your Content Fragments](/help/implementing/developing/headless-journey/update-your-content.md).

## Additional Resources {#additional-resources}

* [Getting Started with AEM Headless](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/graphql/overview.html) - A short video tutorial series giving an overview of using AEM's headless features including data modeling and GraphQL
* [GraphQL.org](https://graphql.org)
  * [Schemas](https://graphql.org/learn/schema/)
  * [GraphQL Java libraries](https://graphql.org/code/#java)
* [AEM GraphQL API for use with Content Fragments](/help/assets/content-fragments/graphql-api-content-fragments.md)
  * [Learning to use GraphQL with AEM - Sample Content and Queries](/help/assets/content-fragments/content-fragments-graphql-samples.md)
  * [Authentication for Remote AEM GraphQL Queries on Content Fragments](/help/assets/content-fragments/graphql-authentication-content-fragments.md)
* [Working with Content Fragments](/help/assets/content-fragments/content-fragments.md)
  * [Content Fragment Models](/help/assets/content-fragments/content-fragments-models.md)
  * [JSON output](/help/assets/content-fragments/content-fragments-json-preview.md)
