---
title: How to Access Your Content via AEM Delivery APIs
description: In this part of the AEM Headless Developer Journey, learn how to use GraphQL queries to access your Content Fragments content.
exl-id: 1adecc69-5f92-4007-8a2a-65bf1e960645
solution: Experience Manager
feature: Headless, Content Fragments,GraphQL API
role: Admin, Architect, Developer
---
# How to Access Your Content via AEM Delivery APIs {#access-your-content}

In this part of the [AEM Headless Developer Journey](overview.md), you can learn how to use GraphQL queries to access the content of your Content Fragments and feed it to your app (headless delivery).

## The Story So Far {#story-so-far}

In the previous document of the AEM headless journey, [How to Model Your Content](model-your-content.md) you learned the basics of content modeling in AEM, so you should now understand how to model your content structure, then realize that structure using AEM Content Fragment Models and Content Fragments:

* Recognize the concepts and terminology related to content modeling.
* Understand why content modeling is needed for Headless content delivery.
* Understand how to realize this structure using AEM Content Fragment Models (and author content with Content Fragments.
* Understand how to model your content; principles with basic samples.

This article builds on those fundamentals so you understand how to access your existing headless content in AEM using the AEM GraphQL API.

* **Audience**: Beginner
* **Objective**: Learn how to access the content of your Content Fragments using AEM GraphQL queries:
  * Introduce GraphQL and the AEM GraphQL API.
  * Dive into the details of the AEM GraphQL API.
  * Look at some sample queries to see how things work in practice.

## So You Would Like to Access Your Content? {#so-youd-like-to-access-your-content}

So...you have got all this content, neatly structured (in Content Fragments), and just waiting to feed your new app. Question is - how to get it there?

What you need is a way to target specific content, select what you need and return it to your app for further processing.

With Adobe Experience Manager (AEM) as a Cloud Service, you can selectively access your Content Fragments, using the AEM GraphQL API, to return only the content that you need. This means you can realize headless delivery of structured content for use in your applications.

>[!NOTE]
>
>AEM GraphQL API is a customized implementation, based on the standard GraphQL API specification.

## GraphQL - An Introduction {#graphql-introduction}

GraphQL is an open-source specification that provides:

* a query language that enables you to select specific content from structured objects.
* a runtime to fulfill these queries with your structured content.

GraphQL is a strongly-typed API. This means that *all* content must be clearly structured and organized by type, so that GraphQL *understands* what to access and how. The data fields are defined within GraphQL schemas, that define the structure of your content objects.

GraphQL endpoints then provide the paths that respond to the GraphQL queries.

All this means that your app can accurately, reliably and efficiently select the content that it needs - just what you need when used with AEM.

>[!NOTE]
>
>See *GraphQL*.org and *GraphQL*.com.

<!--
## AEM and GraphQL {#aem-graphql}

GraphQL is used in various locations in AEM; for example:

* Content Fragments
  * A customized API has been developed for this use-case (Headless Delivery to your app).
    * This is the AEM GraphQL API.
* Commerce
  * AEM Commerce consumes data from a Commerce platform via GraphQL.
  * There are GraphQL integrations between AEM and various third-party commerce solutions, used with the extension hooks provided by the CIF Core Components.
    * This does not use the AEM GraphQL API.

>[!NOTE]
>
>This step of the Headless Journey is only concerned with the AEM GraphQL API and Content Fragments.
-->

## AEM GraphQL API {#aem-graphql-api}

The AEM GraphQL API is a customized version based on the standard GraphQL API specification, specially configured to allow you to perform (complex) queries on your Content Fragments.

Content Fragments are used, as the content is structured according to Content Fragment Models. This fulfills a basic requirement of GraphQL.

* A Content Fragment Model is built up of one, or more, fields.
  * Each field is defined according to a Data Type.
* Content Fragment Models are used to generate the corresponding AEM GraphQL Schemas.

To actually access GraphQL for AEM (and the content) an endpoint is used to provide the access path.

The content returned, via the AEM GraphQL API, can then be used by your applications.

To help you directly input, and test queries, an implementation of the standard GraphiQL interface is also available for use with AEM GraphQL (this can be installed with AEM). It provides features such as syntax-highlighting, auto-complete, auto-suggest, together with a history and online documentation.

>[!NOTE]
>
>The AEM GraphQL API implementation is based on the GraphQL Java libraries.

<!--
### Use Cases for Author and Publish Environments {#use-cases-author-publish-environments}

The use cases for the AEM GraphQL API can depend on the type of AEM as a Cloud Service environment:

* Publish environment; used to: 
  * Query content for JS application (standard use-case)

* Author environment; used to: 
  * Query content for "content management purposes":
    * GraphQL in AEM as a Cloud Service is currently a read-only API.
    * The REST API can be used for CR(u)D operations.
-->

## Content Fragments for use with the AEM GraphQL API {#content-fragments-use-with-aem-graphql-api}

Content Fragments can be used as a basis for GraphQL for AEM schemas and queries as:

* They enable you to design, create, curate and publish page-independent content that can be delivered headlessly.
* They are based on a Content Fragment Model, which pre-defines the structure for the resulting fragment using a selection of data types.
* Additional layers of structure can be achieved with the Fragment Reference data type, available when defining a model.

### Content Fragment Models {#content-fragments-models}

These Content Fragment Models:

* Are used to generate the Schemas, once **Enabled**.
* Provide the data types and fields required for GraphQL. They ensure that your application only requests what is possible, and receives what is expected.
* The data type **Fragment References** can be used in your model to reference another Content Fragment, and so introduce additional levels of structure.

### Fragment References {#fragment-references}

**Fragment Reference** and **Fragment Reference UUID**:

* Are specific data types available when defining a Content Fragment Model.
* References another fragment, dependent on a specific Content Fragment Model.
* Lets you create, and then retrieve, structured data.

  * When defined as a **multifeed**, multiple sub-fragments can be referenced (retrieved) by the prime fragment.

## Actually Using the AEM GraphQL API {#actually-using-aem-graphiql}

### Initial Setup {#initial-setup}

Before starting with queries on your content you need to:

* Enable your endpoint
  * Use Tools > General > GraphQL
  * [Enabling your GraphQL Endpoint](/help/headless/graphql-api/graphql-endpoint.md)
    * This will also enable the GraphiQL IDE.
  
### Sample Structure {#sample-structure}

To actually use the AEM GraphQL API in a query, we can use the two very basic Content Fragment Model structures:

* Company
  * Name - Text
  * CEO (Person) - Fragment Reference
  * Employees (Persons) - Fragment Reference(s)
* Person
  * Name - Text
  * First Name - Text

As you can see, the CEO and Employees fields, reference the Person fragments.

The fragment models are used:

* when creating the content in the Content Fragment Editor
* to generate the GraphQL schemas that you will query

### Where to Test Your Queries {#where-to-test-your-queries}

The queries can be entered in the GraphiQL interface. You can access the query editor from either: 

* **Tools** > **General** > **GraphQL Query Editor**
* directly; for example, `http://localhost:4502/aem/graphiql.html`

![GraphiQL Interface](assets/graphiql-interface.png "GraphiQL Interface")

### Getting Started with Queries {#getting-Started-with-queries}

A straightforward query is to return the name of all entries in the Company schema. Here you request a list of all company names:

```xml
query {
  companyList {
    items {
      name
    }
  }
}
```

A slightly more complex query is to select all persons that do not have a name of "Jobs". This will filter all persons for any that do not have the name Jobs. This is achieved with the EQUALS_NOT operator (there are many more):

```xml
query {
  personList(filter: {
    name: {
      _expressions: [
        {
          value: "Jobs"
          _operator: EQUALS_NOT
        }
      ]
    }
  }) {
    items {
      name
      firstName
    }
  }
}
```

You can also build up more complex queries. For example, query for all companies that have at least one employee with the name of "Smith". This query illustrates filtering for any person of name "Smith", returning information from across the nested fragments:

```xml
query {
  companyList(filter: {
    employees: {
      _match: {
        name: {
          _expressions: [
            {
              value: "Smith"
            }
          ]
        }
      }
    }
  }) {
    items {
      name
      ceo {
        name
        firstName
      }
      employees {
        name
        firstName
      }
    }
  }
}
```

For the full details of using the AEM GraphQL API, together with configuring the necessary elements, you can reference:

* Learning to use GraphQL with AEM
* The Sample Content Fragment Structure
* Learning to use GraphQL with AEM - Sample Content and Queries

## What's Next {#whats-next}

Now that you have learned how to access and query your headless content using the AEM GraphQL API you can now [learn how to use the REST API to access and update the content of your Content Fragments](update-your-content.md).

## Additional Resources {#additional-resources}

* [Adobe Experience Manager as a Cloud Service APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/)
* [GraphQL.org](https://graphql.org)
  * [Schemas](https://graphql.org/learn/schema/)
  * [Variables](https://graphql.org/learn/queries/#variables)
  * [GraphQL Java libraries](https://graphql.org/code/#java)
* [GraphiQL](https://graphql.org/learn/serving-over-http/#graphiql)
* [Learning to use GraphQL with AEM](/help/headless/graphql-api/content-fragments.md)
  * [Enabling your GraphQL Endpoint](/help/headless/graphql-api/graphql-endpoint.md)
  * [Installing the AEM GraphiQL interface](/help/headless/graphql-api/graphiql-ide.md)
* [The Sample Content Fragment Structure](/help/headless/graphql-api/sample-queries.md#content-fragment-structure-graphql)
* [Learning to use GraphQL with AEM - Sample Content and Queries](/help/headless/graphql-api/sample-queries.md)
  * [Sample Query - A Single Specific City Fragment](/help/headless/graphql-api/sample-queries.md#sample-single-specific-city-fragment)
  * [Sample Query for Metadata - List the Metadata for Awards titled GB](/help/headless/graphql-api/sample-queries.md#sample-metadata-awards-gb)
  * [Sample Query - All Cities with a Named Variation](/help/headless/graphql-api/sample-queries.md#sample-cities-named-variation)
* [Enable Content Fragment Functionality in Configuration Browser](/help/sites-cloud/administering/content-fragments/setup.md#enable-content-fragment-functionality-configuration-browser)
* [Working with Content Fragments](/help/sites-cloud/administering/content-fragments/overview.md)
  * [Content Fragment Models](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md)
  * [JSON output](/help/assets/content-fragments/content-fragments-json-preview.md)
* [Understand Cross-Origin Resource Sharing (CORS)](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/security/understand-cross-origin-resource-sharing.html#understand-cross-origin-resource-sharing-(cors))
* [GraphQL Persisted Queries - enabling caching in the Dispatcher](/help/headless/deployment/dispatcher-caching.md)
* [Generating Access Tokens for Server Side APIs](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md)
* [Getting Started with AEM Headless](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/graphql/overview.html) - A short video tutorial series giving an overview of using AEM's headless features, including content modeling and GraphQL.
