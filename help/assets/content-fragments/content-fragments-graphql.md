---
title: Headless Content Delivery using Content Fragments with GraphQL
description: Learn how to use Content Fragments in Adobe Experience Manager (AEM) as a Cloud Service with GraphQL for Headless Content Delivery.
---

# Headless Content Delivery using Content Fragments with GraphQL {#headless-content-delivery-using-content-fragments-with-graphQL}

>[!CAUTION]
>
>The AEM GraphQL API for Content Fragments Delivery is available on request. 
>
>Please reach out to [Adobe Support](https://experienceleague.adobe.com/?lang=en&support-solution=General#support) to enable the API for your AEM as a Cloud Service program.

With Adobe Experience Manager (AEM) as a Cloud Service, you can use Content Fragments, together with the AEM GraphQL API (a customized implementation, based on standard GraphQL), to deliver structured content for use in your applications.

## Headless CMS {#headless-cms}

A Headless Content Management System (CMS) is:

* "*A headless content management system, or headless CMS, is a back-end only content management system (CMS) built from the ground up as a content repository that makes content accessible via an API for display on any device.*

  *The term “headless” comes from the concept of chopping the “head” (the front end, i.e. the website) off the “body” (the back end, i.e. the content repository).*"

  See [Wikipedia](https://en.wikipedia.org/wiki/Headless_content_management_system).

In terms of authoring Content Fragments in AEM this means that:

* You can use Content Fragments to author content that is not primarily intended to be directly published (1:1) on formatted pages.

* The content of your Content Fragments will be structured in a predetermined manner - according to the Content Fragment Models. This simplifies access for your applications, which will further process your content. 

>[!NOTE]
>
>See [Headless and AEM](/help/implementing/developing/headless/introduction.md) for an introduction to Headless Development for AEM Sites as a Cloud Service.

## GraphQL - An Overview {#graphql-overview}

GraphQL is:

* "*...a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.*". 

  See [GraphQL.org](https://graphql.org)

* "*...an open spec for a flexible API layer. Put GraphQL over your existing backends to build products faster than ever before....*". 

  See [Explore GraphQL](https://www.graphql.com). "*Explore GraphQL is maintained by the Apollo team. Our goal is to give developers and technical leaders around the world all of the tools they need to understand and adopt GraphQL.*". 

The [AEM GraphQL API](#aem-graphql-api) allows you to perform (complex) queries on your [Content Fragments](/help/assets/content-fragments/content-fragments.md); with each query being according to a specific model type. The content returned can then be used by your applications. 

### GraphQL Terminology {#graphql-terminology}

GraphQL uses the following:

* **[Queries](https://graphql.org/learn/queries/)**
  
* **[Schemas and Types](https://graphql.org/learn/schema/)** - using these, GraphQL presents the types and operations allowed for the GraphQL for AEM implementation.
  
* **[Fields](https://graphql.org/learn/queries/#fields)**

* **GraphQL Endpoint** - the path in AEM that responds to GraphQL queries, and provides access to the GraphQL schemas.

See the [(GraphQL.org) Introduction to GraphQL](https://graphql.org/learn/) for comprehensive details, including the [Best Practices](https://graphql.org/learn/best-practices/).

### GraphQL Query Types {#graphql-query-types}

With GraphQL you can perform queries for either:

* **Single entry**
  
* **[List of entries](https://graphql.org/learn/schema/#lists-and-non-null)**

## AEM GraphQL API {#aem-graphql-api}

For [Adobe Experience as a Cloud Experience, a customized implementation of the standard GraphQL API](/help/assets/content-fragments/graphql-api-content-fragments.md) has been implemented. 

The AEM GraphQL API implementation is based on the [GraphQL Java libraries](https://graphql.org/code/#java).

## Content Fragments for use with the AEM GraphQL API {#content-fragments-use-with-aem-graphql-api}

[Content Fragments](#content-fragments) can be used as a basis for GraphQL for AEM queries as:

* They enable you to design, create, curate and publish page-independent content.
* The [Content Fragment Models](#content-fragments-models) provide the required structure by means of defined data types.
* The [Fragment Reference](#fragment-references), available when defining a model, can be used to define additional layers of structure.

![Content Fragments for use with GraphQL](assets/cfm-nested-01.png "Content Fragments for use with GraphQL")

### Content Fragments {#content-fragments}

Content Fragments:

* Contain structured content.

* They are based on a [Content Fragment Model](#content-fragments-models), which predefines the structure for the resulting fragment.
  
### Content Fragment Models {#content-fragments-models}

These [Content Fragment Models](/help/assets/content-fragments/content-fragments-models.md):

* Provide the data types and fields required for GraphQL. They ensure that your application only requests what is possible, and receives what is expected.

* The data type **[Fragment References](#fragment-references)** can be used in your model to reference another Content Fragment, and so introduce additional levels of structure.

### Fragment References {#fragment-references}

The **[Fragment Reference](/help/assets/content-fragments/content-fragments-models.md#fragment-reference-nested-fragments)**:

* Is of particular interest in conjunction with GraphQL.

* Is a specific data type that can be used when defining a Content Fragment Model.

* References another fragment, dependent on a specific Content Fragment Model.

* Allows you to retrieve structured data.

  * When defined as a **multifeed**, multiple sub-fragments can be referenced (retrieved) by the prime fragment.

### JSON Preview {#json-preview}

To help with designing and developing your Content Fragment Modesl, you can preview [JSON output](/help/assets/content-fragments/content-fragments-json-preview.md).

## Learning to use GraphQL with AEM - Sample Content and Queries {#learn-graphql-with-aem-sample-content-queries}

See [Learning to use GraphQL with AEM - Sample Content and Queries](/help/assets/content-fragments/content-fragments-graphql-samples.md) for an introduction to using the AEM GraphQL API.

## Tutorial - Getting Started with AEM Headless and GraphQL

Looking for a hands-on tutorial? Check out [Getting Started with AEM Headless and GraphQL](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/graphql/overview.html) end-to-end tutorial illustrating how to build-out and expose content using AEM’s GraphQL APIs and consumed by an external app, in a headless CMS scenario.