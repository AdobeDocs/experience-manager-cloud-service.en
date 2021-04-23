---
title: How to Access Your Content via AEM Delivery APIs
description: In this part of the AEM Headless Developer Journey, learn how to use GraphQL queries to access your Content Fragments content.
hide: yes
hidefromtoc: yes
index: no
---

# How to Access Your Content via AEM Delivery APIs {#access-your-content}

>[!CAUTION]
>
>WORK IN PROGRESS - The creation of this document is ongoing and it should not be understood as complete or definitive nor should it be used for production purposes.

In this part of the [AEM Headless Developer Journey,](#overview.md) learn how to use GraphQL queries to access the content of your Content Fragments.

## The Story So Far {#story-so-far}

In the previous document of the AEM headless journey, [How to Model Your Content](model-your-content.md) you learned the basics of data modeling in AEM and you should now:

* Understand important planning considerations for designing your content.
* Understand the steps to implement headless depending on your integration level requirements.
* Set up the necessary tools and AEM configurations.
* Know best practices to make your headless journey smooth, keep content generation efficient, and ensure content is delivered quickly.

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

GraphQL is:

* "*...a query language for APIs and a runtime for fulfilling those queries with your existing data.*".

  See *GraphQL*.

### GraphQL - Types {#graphql-types}

### GraphQL - Schemas {#graphql-schemas}

### GraphQL - Queries {#graphql-queries}

## AEM and GraphQL {#aem-graphql}

GraphQL is used in various locations in AEM:

* Commerce
  * Placeholder
* Content Fragments
  * A customized API has been developed for this use-case.
  * This is the AEM GraphQL API.

## AEM GraphQL API {#aem-graphql-api}

For Adobe Experience as a Cloud Experience, a customized implementation of the standard GraphQL API has been developed.

The AEM GraphQL API allows you to perform (complex) queries on your Content Fragments; with each query being according to a specific model type. The content returned can then be used by your applications.

>[!NOTE]
>
>The AEM GraphQL API implementation is based on the GraphQL Java libraries.

### AEM GraphQL API and Content Fragments {#aem-graphql-content-fragments}

## Content Fragments for use with the AEM GraphQL API {#content-fragments-use-with-aem-graphql-api}

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

## What's Next {#whats-next}

[Learn how to use the REST API to access and update the content of your Content Fragments](/help/implementing/developing/headless-journey/update-your-content.md).

## Additional Resources {#additional-resources}

* [GraphQL.org](https://graphql.org)
  * [Schemas](https://graphql.org/learn/schema/)
  * [GraphQL Java libraries](https://graphql.org/code/#java)
* [AEM GraphQL API for use with Content Fragments](/help/assets/content-fragments/graphql-api-content-fragments.md)
  * [Learning to use GraphQL with AEM - Sample Content and Queries](/help/assets/content-fragments/content-fragments-graphql-samples.md)
  * [Authentication for Remote AEM GraphQL Queries on Content Fragments](/help/assets/content-fragments/graphql-authentication-content-fragments.md)
* [Working with Content Fragments](/help/assets/content-fragments/content-fragments.md)
  * [Content Fragment Models](/help/assets/content-fragments/content-fragments-models.md)
  * [JSON output](/help/assets/content-fragments/content-fragments-json-preview.md)
