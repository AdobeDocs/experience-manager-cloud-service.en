---
title: How to Model Your Content as AEM Data Models
description: In this part of the AEM Headless Developer Journey, learn how to model your content for AEM Headless delivery using Data Modelling with Content Fragment Models and Content Fragments.
---

# How to Model Your Content as AEM Data Models {#model-your-content}

>[!CAUTION]
>
>WORK IN PROGRESS

In this part of the [AEM Headless Developer Journey](#overview.md), you can learn how to model your content structure. Then realize that structure for Adobe Experience Manager (AEM) using Content Fragments Models and Content Fragments, for reuse across channels.

* **Audience**: Beginner
* **Objective**: Learn how to model your content structure, then realize that structure using AEM Content Fragment Models and Content Fragments:
  * Introduce concepts and terminology related to [data modelling](#data-modelling).
  * Learn [why data modelling is needed for Headless content delivery](#data-modelling-for-aem-headless).
  * Learn [how to realize this structure using AEM Content Fragment Models](#create-structure-content-fragment-models) (and generate content with [Content Fragments](#use-content-to-generate-content)).
  * Learn [how to model your content](#getting-started-examples); principles with basic samples.

## Data Modelling {#data-modelling}

*It's a big bad world out there*. 

Maybe, maybe not, but it's certainly a big ***complicated*** world out there and data modelling is used to define a simplified representation of a very (very) small sub-section, using the specific information that is needed for a certain purpose.

For example:

There are many Schools, but they all have various things in common:

* A Location
* A Head Teacher
* Many Teachers
* Many members of non-teaching staff
* Many pupils
* Many ex-teachers
* Many ex-pupils
* Many classrooms
* Many (many) books
* Many (many) pieces of equipment
* Many extra-curriculum activities
* and so on....

Even in such a small example the list can seem endless. But if you simply want your application to perform a simple task, you need to limit the information to the essentials. 

For example, advertising special events for all schools in the area:

* School Name
* School Location
* Head Teacher
* Type of Event
* Date of Event
* Teacher Organizing the Event

### Concepts {#concepts}

What you want to describe are referred to as **Entities** - basically the "things" that we want to store information about.

The information that we want to store about them are the **Attributes**, such as Name, and Qualifications for the teachers. 

Then there are various **Relationships** between the entities. For example, usually a school only has one head teacher, and many teachers (and usually the head teacher is also a teacher).

The process of analyzing and defining this information, together with the relationships between them, is called **Data Modelling**.

### Basics {#basics}

Often you need to start by drawing up a **Conceptual Schema** that describes the entities and their relationships. Usually this is high-level (conceptual).

After this is stable you can translate the models into a **Logical Schema** that describes the entities, together with the attributes, and the relationships. At this level you should examine the definitions closely to eliminate duplication and optimize your design.

>[!NOTE]
>
>Sometimes these two steps are merged, often depending on the complexity of your scenario.

For example, do you need separate entities for `Head Teacher` and `Teacher`, or simply an additional attribute on the `Teacher` model? 

### Ensuring data integrity and eliminating data redundancy {#data-integrity-data-redundancy}

>[!NOTE]
>To be continued....

### Performance {#performance}

>[!NOTE]
>To be continued....

## Data Modelling for AEM Headless {#data-modelling-for-aem-headless}

Data Modelling is a set of established techniques, often used when developed relationship databases, so what does it mean for AEM Headless?

### Why? {#why}

To ensure that your application can consistently and efficiently request and receive the required content from AEM, this content must be structured. 

This means that your application knows in advance the form of response and therefore, how to process it. This is much easier than receiving free-form content, which has to be parsed to determine what it contains and therefore, how it can be used.

### Introduction to How? {#how}

AEM uses Content Fragments to provide the structures needed for Headless delivery of your content to your applications.

The structure of your data model is:

* realized by the definition of your Content Fragment Model,
* used as a basis of the Content Fragments used for your content generation.

>[!NOTE]
>
>The Content Fragment Models are also used as the basis of the AEM GraphQL Schemas, used for retrieving your content - more about that in a later session.

Requests for your content are made using the AEM GraphQL API, a customized implementation of the standard GraphQL API. The AEM GraphQL API allows you to perform (complex) queries on your Content Fragments, with each query being according to a specific model type. 

The content returned can then be used by your applications. 

## Creating the Structure - Content Fragment Models {#create-structure-content-fragment-models}

Content Fragment Models provide various mechanisms that allow you to define the structure of your content. 

A Content Fragment Model describes an entity.

Within a model:

1. **Data Types** allow you to define the individual attributes.
   For example, define the field holding a teacher's name as **Text** and their years of service as **Number**.
1. The data types **Content Reference** and **Fragment Reference** allow you to create relationships to other content within AEM.
1. The **Fragment Reference** data type allows you to realise multiple levels of structure by nesting your Content Fragments (according to the model type). This is vital for your data modelling.

For example:
![Content Modelling with Content Fragments](assets/headless-modelling-01.png "Content Modelling with Content Fragments")

### Data Types {#data-types}

AEM provides the following data types for you to model your content:

* Single line text
* Multi line text
* Number
* Boolean
* Date and time
* Enumeration
* Tags
* Content Reference
* Fragment Reference
* JSON Object

### References and Nested Content {#references-nested-content}

Two data types provide references to content outside a specific fragment:
* **Content Reference**
  This provides a simple reference to other content of any type.
  For example, you can reference an image at a specified location.

* **Fragment Reference**
  This provides references to other Content Fragments. 
  This type of reference is used to create nested content, introducing the relationships needed to model your content.
  The data type can be configured to allow fragment authors to:
  * Edit the referenced fragment directly.
  * Create a new content fragment, based on the appropriate model

## Using the structure to generate content - Content Fragments {#use-content-to-generate-content}

>[!NOTE]
>To be continued....

### Selecting the appropriate model {#select-model}

### Creating, and editing, structured content {#create-edit-structured-content}

## Getting Started with some Examples {#getting-started-examples}

## What's Next {#whats-next}

[Learn how to use GraphQL to access and retrieve your Content Fragments content](fetch-your-content.md). 

## Additional Resources {#additional-resources}

* [Working with Content Fragments](/help/assets/content-fragments/content-fragments.md)
* [Content Fragment Models](/help/assets/content-fragments/content-fragments-models.md)
* [AEM GraphQL Schemas](/help/implementing/developing/headless-journey/fetch-your-content.md)
