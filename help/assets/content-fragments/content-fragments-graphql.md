---
title: Content Delivery using Content Fragments with GraphQL
description: Learn how to use Content Fragments in Adobe Experience Manager (AEM) as a Cloud Service with GraphQL for Content Delivery.
---

# Content Delivery using Content Fragments with GraphQL {#content-delivery-using-content-fragments-with-graphQL}

With Adobe Experience Manager (AEM) as a Cloud Service, you can use Content Fragments, together with GraphQL for AEM (a customized implementation, based on standard GraphQL), to deliver structured content for use in your applications.

## GraphQL - An Overview {#graphql-overview}

GraphQL is:

* "*...a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.*". 

  See [GraphQL.org](https://graphql.org)

* "*...an open spec for a flexible API layer. Put GraphQL over your existing backends to build products faster than ever before....*". 

  See [Explore GraphQL](https://www.graphql.com). "*Explore GraphQL is maintained by the Apollo team. Our goal is to give developers and technical leaders around the world all of the tools they need to understand and adopt GraphQL.*". 

[GraphQL for AEM](#graphql-for-aem) allows you to perform (complex) queries on your [Content Fragments](/help/assets/content-fragments/content-fragments.md); with each query being according to a specific model type. The content returned can then be used by your applications. 

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

## GraphQL for AEM {#graphql-for-aem}

For [Adobe Experience as a Cloud Experience, a customized implementation of the standard GraphQL API](/help/assets/content-fragments/graphql-api-content-fragments.md) has been implemented. 

The GraphQL for AEM implementation is based on the [GraphQL Java libraries](https://graphql.org/code/#java).

## Content Fragments for use with GraphQL for AEM {#content-fragments-use-with-graphql-for-aem}

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

See:

* A [sample Content Fragment structure](#content-fragment-structure-graphql) 

* And some [sample GraphQL queries](#graphql-sample-queries), based on the sample content fragment structure (Content Fragment Models and related Content Fragments).

## A Sample Content Fragment Structure for use with GraphQL {#content-fragment-structure-graphql}

For a simple example we need:

* One, or more, [Sample Content Fragment Models](#sample-content-fragment-models-schemas) - form the basis for the GraphQL schemas

* [Sample Content Fragments](#sample-content-fragments) based on the above models

### Sample Content Fragment Models (Schemas) {#sample-content-fragment-models-schemas}

For the sample queries, we will use the following Content Models, and their interrelationships (references ->):

* [Company](#company)
  -> [Person](#person)
  &nbsp;&nbsp;&nbsp;&nbsp;-> [Award](#award)

* [City](#city)

#### Company {#company}

The basic fields defining the comparny are:

| Field Name | Data Type | Reference |
|--- |--- |--- |
| Company Name | Single line text | |
| CEO | Fragment Reference (single) | [Person](#person) |
| Employees | Fragment Reference (multifield) | [Person](#person) |

#### Person {#person}

The fields defining a person, who can also be an employee:

| Field Name | Data Type | Reference |
|--- |--- |--- |
| Name | Single line text | |
| First name | Single line text | |
| Awards | Fragment Reference (multifield) | [Award](#award) |

#### Award {#award}

The fields defining an award are:

| Field Name | Data Type | Reference |
|--- |--- |--- |
| Shortcut/ID | Single line text | |
| Title | Single line text | |

#### City {#city}

The fields for defining a city are:

| Field Name | Data Type | Reference |
|--- |--- |--- |
| Name | Single line text | |
| Country | Single line text | |
| Population | Number | |
| Categories | Tags | |

### Sample Content Fragments {#sample-content-fragments}

The following fragments are used for the appropriate model. 

#### Company {#company}

| Company Name | CEO | Employees |
|--- |--- |--- |
| Apple | Steve Jobs | Duke Marsh<br>Max Caulfield |
| Little Pony Inc. | Adam Smith | Lara Croft<br>Cutter Slade |
| NextStep Inc. | Steve Jobs | Joe Smith<br>Abe Lincoln |

#### Person {#person}

| Name | First Name | Awards |
|--- |--- |--- |
| Lincoln | Abe | |
| Smith | Adam | |
| Slade | Cutter | Gameblitz<br>Gamestar |
| Marsh | Duke | | 
| Smith | Joe | |
| Croft | Lara | Gamestar |
| Caulfield | Max | Gameblitz |
| Jobs | Steve | |

#### Award {#award}

| Shortcut/ID | Title |
|--- |--- |
| GB | Gameblitz |
| GS | Gamestar |
| OSC | Oscar |

#### City {#city}

| Name | Country | Population | Categories |
|--- |--- |--- |--- |
| Basel | Switzerland | 172258 | city:emea |
| Berlin | Germany | 3669491 | city:capital<br>city:emea |
| Bucharest | Romania | 1821000 | city:capital<br>city:emea |
| San Francisco | USA | 883306 | city:na |
| San Jose | USA | 102635 | city:na |
| Stuttgart | Germany | 634830 | city:emea |
| Zurich | Switzerland | 415367 | city:capital<br>city:emea |

## GraphQL for AEM - Some Extensions {#graphql-some-extensions}

The basic operation of queries with GraphQL for AEM adhere to the standard GraphQL specification. For GraphQL queries with AEM there are a few extensions:

* If you require a single result:
  * use the model name; eg city

* If you expect a list of results:
  * add a trailing "s"; e.g. citys

* If you want to use a logical OR:
  * use " _logOp: OR"

* Logical AND also exists, but is (often) implicit

* You can query on field names that correspond to the fields within the Content Fragment Model

* In addition to the fields from your model, there are some system generated fields (preceeded by underscore):

  * `_path` : the path to your Content Fragement within the repository
  
  * `_variations` : to reveal specific Variations within your Content Fragment

  * `_metadata` : to reveal metadata for your fragment

## GraphQL - Sample Queries {#graphql-sample-queries}

See the sample queries for illustrations of create queries, together with sample results.

>[!NOTE]
>
>Depending on your instance you can directly access the Graph*i*QL interface for submitting and testing queries.
>
>For example: `http://localhost:4502/content/graphiql.html`

### Sample Query - All Available Schemas and Datatypes {#sample-all-schemes-datatypes}

This will return all types for all available schemas.

**Sample Query**

```xml
{
  __schema {
    types {
      name
      description
    }
  }
}
```

**Sample Result**

```xml
{
  "data": {
    "__schema": {
      "types": [
        {
          "name": "ArrayMode",
          "description": null
        },
        {
          "name": "AwardModel",
          "description": null
        },
        {
          "name": "AwardModelArrayFilter",
          "description": null
        },
        {
          "name": "AwardModelFilter",
          "description": null
        },
        {
          "name": "Boolean",
          "description": "Built-in Boolean"
        },

...more results...

        {
          "name": "__Field",
          "description": null
        },
        {
          "name": "__InputValue",
          "description": null
        },
        {
          "name": "__Schema",
          "description": "A GraphQL Introspection defines the capabilities of a GraphQL server. It exposes all available types and directives on the server, the entry points for query, mutation, and subscription operations."
        },
        {
          "name": "__Type",
          "description": null
        },
        {
          "name": "__TypeKind",
          "description": "An enum describing what kind of type a given __Type is"
        }
      ]
    }
  }
}
```

### Sample Query - Full Details of a Company's CEO and Employees {#sample-full-details-company-ceos-employees}

Using the structure of the nested fragments, this query returns the full details of a company's CEO and all its employees.

**Sample Query**

```xml
query {
  companys {
    items {
      name
      ceo {
        _path
        name
        firstName
        awards {
        id
          title
        }
      }
      employees {
       name
        firstName
       awards {
         id
          title
        }
      }
    }
  }
}
```

**Sample Results**

```xml
{
  "data": {
    "companys": [
      {
        "name": "Apple Inc.",
        "ceo": {
          "_path": "/content/dam/persons/steve-jobs",
          "name": "Jobs",
          "firstName": "Steve",
          "awards": []
        },
        "employees": [
          {
            "name": "Marsh",
            "firstName": "Duke",
            "awards": []
          },
          {
            "name": "Caulfield",
            "firstName": "Max",
            "awards": [
              {
                "id": "GB",
                "title": "Gameblitz"
              }
            ]
          }
        ]
      },
      {
        "name": "Little Pony, Inc.",
        "ceo": {
          "_path": "/content/dam/persons/adam-smith",
          "name": "Smith",
          "firstName": "Adam",
          "awards": []
        },
        "employees": [
          {
            "name": "Croft",
            "firstName": "Lara",
            "awards": [
              {
                "id": "GS",
                "title": "Gamestar"
              }
            ]
          },
          {
            "name": "Slade",
            "firstName": "Cutter",
            "awards": [
              {
                "id": "GB",
                "title": "Gameblitz"
              },
              {
                "id": "GS",
                "title": "Gamestar"
              }
            ]
          }
        ]
      },
      {
        "name": "NextStep Inc.",
        "ceo": {
          "_path": "/content/dam/persons/steve-jobs",
          "name": "Jobs",
          "firstName": "Steve",
          "awards": []
        },
        "employees": [
          {
            "name": "Smith",
            "firstName": "Joe",
            "awards": []
          },
          {
            "name": "Lincoln",
            "firstName": "Abraham",
            "awards": []
          }
        ]
      }
    ]
  }
}
```

### Sample Query - All Information about All Cities {#sample-all-information-all-cities}

To retrieve all information about all cities, you can use the very basic query:
**Sample Query**

```xml
{
  citys
    items
}
```

When executed, the system will automatically expand the query to include all fields:

```xml
{
  citys {
    items {
      _path
      name
      country
      population
    }
  }
}
```

**Sample Results**

```xml
{
  "data": {
    "citys": [
      {
        "_path": "/content/dam/cities/basel",
        "name": "Basel",
        "country": "Switzerland",
        "population": 172258
      },
      {
        "_path": "/content/dam/cities/berlin",
        "name": "Berlin",
        "country": "Germany",
        "population": 3669491
      },
      {
        "_path": "/content/dam/cities/bucharest",
        "name": "Bucharest",
        "country": "Romania",
        "population": 1821000
      },
      {
        "_path": "/content/dam/cities/san-francisco",
        "name": "San Francisco",
        "country": "USA",
        "population": 883306
      },
      {
        "_path": "/content/dam/cities/san-jose",
        "name": "San Jose",
        "country": "USA",
        "population": 1026350
      },
      {
        "_path": "/content/dam/cities/stuttgart",
        "name": "Stuttgart",
        "country": "Germany",
        "population": 634830
      },
      {
        "_path": "/content/dam/cities/zurich",
        "name": "Zurich",
        "country": "Switzerland",
        "population": 415367
      }
    ]
  }
}
```

### Sample Query - Names of All Cities {#sample-names-all-cities}

This is a straightforward query to return the `name`of all entries in the `city`schema.

**Sample Query**

```xml
query {
  citys {
    items {
      name
    }
  }
}
```

**Sample Results**

```xml
{
  "data": {
    "citys": [
      {
        "name": "Basel"
      },
      {
        "name": "Berlin"
      },
      {
        "name": "Bucharest"
      },
      {
        "name": "San Francisco"
      },
      {
        "name": "San Jose"
      },
      {
        "name": "Stuttgart"
      },
      {
        "name": "Zurich"
      }
    ]
  }
}
```

### Sample Query - A Single City Fragment {#sample-single-city-fragment}

This is a query to return the details of a single fragment entries at a specific location in the repository.

**Sample Query**

```xml
{
  city (_path: "/content/dam/cities/berlin") {
    _path
    name
    country
    population
    categories

  }
}
```

**Sample Results**

```xml
{
  "data": {
    "city": {
      "_path": "/content/dam/cities/berlin",
      "name": "Berlin",
      "country": "Germany",
      "population": 3669491,
      "categories": [
        "city:capital",
        "city:emea"
      ]
    }
  }
}
```

### Sample Query - All Cities with a Named Variation {#sample-cities-named-variation}

If you create a new variation, named "Berlin Centre" (`berlin_centre`), for the `city` Berlin, then you can use a query to return details of the variation.

**Sample Query**

```xml
{
  citys (variation: "berlin_centre") {
    items {
      _path
      name
      country
      population
      categories
    }
  }
}
```

**Sample Results**
```xml
{
  "data": {
    "citys": [
      {
        "_path": "/content/dam/cities/berlin",
        "name": "Berlin",
        "country": "Germany",
        "population": 3669491,
        "categories": [
          "city:capital",
          "city:emea"
        ]
      }
    ]
  }
}
```

### Sample Query - All Persons that have a name of "Jobs" or "Smith" {#sample-all-persons-jobs-smith}

This will filter all `persons` for any that have the name `Jobs`or `Smith`.
**Sample Query**

```xml
query {
  persons(filter: {
    name: {
      _logOp: OR
      _expressions: [
        {
          value: "Jobs"
        },
        {
          value: "Smith"
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

**Sample Results**

```xml
{
  "data": {
    "persons": [
      {
        "name": "Smith",
        "firstName": "Adam"
      },
      {
        "name": "Smith",
        "firstName": "Joe"
      },
      {
        "name": "Jobs",
        "firstName": "Steve"
      }
    ]
  }
}
```

### Sample Query - All cities located in Germany or Switzerland with a population between 400000 and 999999 {#sample-all-cities-d-ch-population}

Here a combination of fields are filtered on. An `AND` (implicit) is used to select the `population`range, while an `OR` (explicit) is used to select the required cities.

**Sample Query**

```xml
query {
  citys(filter: {
    population: {
      _expressions: [
        {
          value: 400000
          _operator: GREATER_EQUAL
        }, {
          value: 1000000
          _operator: LOWER
        }
      ]
    },
    country: {
      _logOp: OR
      _expressions: [
        {
          value: "Germany"
        }, {
          value: "Switzerland"
        }
      ]
    }
  }) {
    items {
      name
      population
      country
    }
  }
}
```

**Sample Results**

```xml
{
  "data": {
    "citys": [
      {
        "name": "Stuttgart",
        "population": 634830,
        "country": "Germany"
      },
      {
        "name": "Zurich",
        "population": 415367,
        "country": "Switzerland"
      }
    ]
  }
}
```

### Sample Query for Nested Content Fragments - All companies that have at least one employee that has a name of "Smith" {#sample-companies-employee-smith}

This query illustrates filtering for any `person` of `name` "Smith", returning information from across two nested fragments - `company` and `employee`.

**Sample Query**

```xml
query {
  companys(filter: {
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

**Sample Results**

```xml
{
  "data": {
    "companys": [
      {
        "name": "NextStep Inc.",
        "ceo": {
          "name": "Jobs",
          "firstName": "Steve"
        },
        "employees": [
          {
            "name": "Smith",
            "firstName": "Joe"
          },
          {
            "name": "Lincoln",
            "firstName": "Abraham"
          }
        ]
      }
    ]
  }
}
```

### Sample Query for Nested Content Fragments - All companies where all employees have won the "Gamestar" award {#sample-all-companies-employee-gamestar-award}

This query illustrates filtering across three nested fragments - `company`, `employee`, and `award`.

**Sample Query**

```xml
query {
  companys(filter: {
    employees: {
      _apply: ALL
      _match: {
        awards: {
          _match: {
            id: {
              _expressions: [
                {
                  value: "GS"
                  _operator:EQUALS
                }
              ]
            }
          }
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
        awards {
          id
          title
        }
      }
    }
  }
}
```

**Sample Results**

```xml
{
  "data": {
    "companys": [
      {
        "name": "Little Pony, Inc.",
        "ceo": {
          "name": "Smith",
          "firstName": "Adam"
        },
        "employees": [
          {
            "name": "Croft",
            "firstName": "Lara",
            "awards": [
              {
                "id": "GS",
                "title": "Gamestar"
              }
            ]
          },
          {
            "name": "Slade",
            "firstName": "Cutter",
            "awards": [
              {
                "id": "GB",
                "title": "Gameblitz"
              },
              {
                "id": "GS",
                "title": "Gamestar"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

### Sample Query for Metadata - List the Metadata for Awards titled GB {#sample-metadata-awards-gb}

This query illustrates filtering across three nested fragments - `company`, `employee`, and `award`.

**Sample Query**

```xml
query {
  awards(filter: {
      id: {
        _expressions: [
          {
            value:"GB"
          }
        ]
    }
  }) {
    items {
      _metadata {
        stringMetadata {
          name,
          value
        }
      }
      id
      title
    }
  }
}
```

**Sample Results**

```xml
{
  "data": {
    "awards": [
      {
        "_metadata": {
          "stringMetadata": [
            {
              "name": "title",
              "value": "Gameblitz Award"
            },
            {
              "name": "description",
              "value": ""
            }
          ]
        },
        "id": "GB",
        "title": "Gameblitz"
      }
    ]
  }
}
```