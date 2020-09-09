---
title: Content Delivery using Content Fragments with GraphQL
description: Learn how to use Content Fragments in Adobe Experience Manager (AEM) as a Cloud Service with GraphQL for Content Delivery.
---

# Content Delivery using Content Fragments with GraphQL {#Content Delivery using Content Fragments with GraphQL}

With Adobe Experience Manager (AEM) as a Cloud Service, you can use Content Fragments, together with GraphQL, to deliver content for use in your applications.

## The Fundamentals {#the-fundamentals}

As a quick introduction, the following fundamentals are introduced.

### GraphQL {#graphql}

GraphQL is:

* "*...a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.*". 

  See [GraphQL.org](https://graphql.org)

* "*...an open spec for a flexible API layer. Put GraphQL over your existing backends to build products faster than ever before....*". 

  See [Explore GraphQL](https://www.graphql.com). "*Explore GraphQL is maintained by the Apollo team. Our goal is to give developers and technical leaders around the world all of the tools they need to understand and adopt GraphQL.*". 

GraphQL allows you to perform (complex) queries on your [Content Fragments](/help/assets/content-fragments/content-fragments.md); with each query being according to a specific model type. The content returned can then be used by your applications. 

#### GraphQL Terminology {#graphql-terminology}

GraphQL uses the following:

* **[Queries](https://graphql.org/learn/queries/)**
  
* **[Schemas and Types](https://graphql.org/learn/schema/)**
  
* **[Fields](https://graphql.org/learn/queries/#fields)**

See the [(GraphQL.org) Introduction to GraphQL](https://graphql.org/learn/) for comprehensive details, including the [Best Practices](https://graphql.org/learn/best-practices/).

#### GraphQL Query Types {#graphql-query-types}

With GraphQL you can perform queries for either:

* **Single entry**
  
* **[List of entries](https://graphql.org/learn/schema/#lists-and-non-null)**

### Content Fragments {#content-fragments}
Content fragments:

* Contain structured content.

* They are based on a [Content Fragment Model](#content-fragments-models), which predefines the structure for the resulting fragment.
  
* [Can be nested](/help/assets/content-fragments/content-fragments-models.md#nested-content-fragments), using either of the following data types:
  * **Content Reference** 
    * This provides a simple reference to another fragment.
  * **[Fragment Reference](#fragment-references)** 
    * This references another fragment - dependent on a specific model.

### Content Fragment Models {#content-fragments-models}

These [Content Fragment Models](/help/assets/content-fragments/content-fragments-models.md):

* Provide the data types and fields required for GraphQL to ensure that your application only requests what is possible, and receives what is expected.

* The data type **[Fragment References](#fragment-references)** can be used in your model to define additional levels of structure.

### Fragment References {#fragment-references}

The **[Fragment Reference](/help/assets/content-fragments/content-fragments-models.md#fragment-reference)**:

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

* One, or more, [Sample Content Fragment Models](#sample-content-fragment-models)

* [Sample Content Fragments](#sample-content-fragments) based on the above models

### Sample Content Fragment Models {#sample-content-fragment-models}

If we consider the following Content Models, and their interrelationships (references ->):

* [Company](#company)
  -> [Person](#person)
  &nbsp;&nbsp;&nbsp;&nbsp;-> [Award](#award)

* [City](#city)

#### Company {#company}

The fields:

| Field Name | Data Type | Reference |
|--- |--- |--- |
| Company Name | Single line text | |
| CEO | Fragment Reference | [Person](#person) |
| Employees | Fragment Reference | [Person](#person) |

#### Person {#person}

The fields:

| Field Name | Data Type | Reference |
|--- |--- |--- |
| Name | Single line text | |
| First name | Single line text | |
| Awards | Fragment Reference | [Award](#award) |

#### Award {#award}

The fields:

| Field Name | Data Type | Reference |
|--- |--- |--- |
| Shortcut/ID | Single line text | |
| Title | Single line text | |

#### City {#city}

The fields:

| Field Name | Data Type | Reference |
|--- |--- |--- |
| Name | Single line text | |
| Country | Single line text | |
| Population | Number | |
| Categories | Tags | |

### Sample Content Fragments {#sample-content-fragments}

## GraphQL - Sample Queries {#graphql-sample-queries}

### Sample Query - All Available Schemas and Datatypes {#sample-all-schemes-datatypes}

This will return all available schemas and datatypes.

**Sample Query**

```xml
{
  __schema {
    types {
      name
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
          "name": "ArrayMode"
        },
        {
          "name": "AwardModel"
        },
        {
          "name": "AwardModelArrayFilter"
        },
        {
          "name": "AwardModelFilter"
        },
        {
          "name": "Boolean"
        },

...more results...

       {
          "name": "__InputValue"
        },
        {
          "name": "__Schema"
        },
        {
          "name": "__Type"
        },
        {
          "name": "__TypeKind"
        }
      ]
    }
  }
}
```

### Sample Query - All Persons that have a name of "Jobs" or "Smith" {#sample-all-persons-jobs-smith}

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
    name
    firstName
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
    name
    population
    country
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
