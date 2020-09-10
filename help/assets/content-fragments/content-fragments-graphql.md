---
title: Content Delivery using Content Fragments with GraphQL
description: Learn how to use Content Fragments in Adobe Experience Manager (AEM) as a Cloud Service with GraphQL for Content Delivery.
---

# Content Delivery using Content Fragments with GraphQL {#content-delivery-using-content-fragments-with-graphQL}

With Adobe Experience Manager (AEM) as a Cloud Service, you can use Content Fragments, together with GraphQL, to deliver structured content for use in your applications.

## GraphQL - An Overview {#graphql-overview}

GraphQL is:

* "*...a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.*". 

  See [GraphQL.org](https://graphql.org)

* "*...an open spec for a flexible API layer. Put GraphQL over your existing backends to build products faster than ever before....*". 

  See [Explore GraphQL](https://www.graphql.com). "*Explore GraphQL is maintained by the Apollo team. Our goal is to give developers and technical leaders around the world all of the tools they need to understand and adopt GraphQL.*". 

GraphQL allows you to perform (complex) queries on your [Content Fragments](/help/assets/content-fragments/content-fragments.md); with each query being according to a specific model type. The content returned can then be used by your applications. 

### GraphQL Terminology {#graphql-terminology}

GraphQL uses the following:

* **[Queries](https://graphql.org/learn/queries/)**
  
* **[Schemas and Types](https://graphql.org/learn/schema/)**
  
* **[Fields](https://graphql.org/learn/queries/#fields)**

See the [(GraphQL.org) Introduction to GraphQL](https://graphql.org/learn/) for comprehensive details, including the [Best Practices](https://graphql.org/learn/best-practices/).

### GraphQL Query Types {#graphql-query-types}

With GraphQL you can perform queries for either:

* **Single entry**
  
* **[List of entries](https://graphql.org/learn/schema/#lists-and-non-null)**

## Content Fragments for use with GraphQL {#content-fragments-overview}

[Content Fragments](#content-fragments) can be used as a basis for GraphQL queries as:

* The [Content Fragment Models](#content-fragments-models) provide the required structure by means of defined data types.
* The [Fragment Reference](#fragment-references), available when defining a model, can be used to define additional layers of structure.

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
| CEO | Fragment Reference (single) | [Person](#person) |
| Employees | Fragment Reference (multifield) | [Person](#person) |

#### Person {#person}

The fields:

| Field Name | Data Type | Reference |
|--- |--- |--- |
| Name | Single line text | |
| First name | Single line text | |
| Awards | Fragment Reference (multifield) | [Award](#award) |

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

The following fragments are used for the appropriate model. 

#### Company {#company}

* Apple
  * CEO: 0Steve Jobs
  * Employees: Duke Marsh and Max Caulfield
* Little Pony Inc.
  * CEO: Adam Smith
  * Employees: Lara Croft and Cutter Slade
* NextStep Inc.
  * CEO: Steve Jobs
  * Employees: Joe Smith and Abe Lincoln

#### Person {#person}

* Abe Lincoln
* Adam Smith
* Cutter Slade
  * Awards: Gameblitz and Gamestar
* Duke Marsh
* Joe Smith
* Lara Croft
  * Awards: Gamestar
* Max Caulfield
  * Awards: Gameblitz
* Steve Jobs

#### Award {#award}

* Gameblitz Award
* Gamestar Award
* Oscar

#### City {#city}

* Basel
  * Country: Switzerland
  * Population: 172258
  * Categories: city:emea
* Berlin
  * Country: Germany
  * Population: 3669491
  * Categories: city:capital and city:emea
* Bucharest
  * Country: Romania
  * Population: 1821000
  * Categories: city:capital and city:emea
* San Francisco
  * Country: USA
  * Population: 883306
  * Categories: city:na
* San Jose
  * Country: USA
  * Population: 102635
  * Categories: city:na
* Stuttgart
  * Country: Germany
  * Population: 634830
  * Categories: city:emea
* Zurich
  * Country: Switzerland
  * Population: 415367
  * Categories: city:capital and city:emea

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

### Sample Query - All Cities {#sample-all-cities}

**Sample Query**

```xml
query {
  citys {
    name
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
