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

### Concepts {#concepts}

### Basics {#basics}

### Ensuring data integrity and eliminating data redundancy {#data-integrity-data-redundancy}

### Performance {#performance}

## Data Modelling for AEM Headless {#data-modelling-for-aem-headless}

### Why? {#why}

To ensure that your application can consistently and efficiently request, and receive, the required content from AEM, this content must be structured.

### Introduction to How? {#how}

AEM uses Content Fragments to provide the structures needed for Headless delivery of your content to your applications.

The structure of your data model is:

* realized by the definition of your Content Fragment Model,
* used as a basis of the Content Fragments used for your content generation.

Requests for your content are made using the AEM GraphQL API, a customized implementation of the standard GraphQL API. The AEM GraphQL API allows you to perform (complex) queries on your Content Fragments, with each query being according to a specific model type. 

The content returned can then be used by your applications. 

## Creating the Structure - Content Fragment Models {#create-structure-content-fragment-models}

![Content Fragments for use with GraphQL](/help/assets/content-fragments/assets/cfm-nested-01.png "Content Fragments for use with GraphQL")

### Data Types {#data-types}

### References {#references}

### Nested Fragments {#nested-fragments}

## Using the structure to generate content - Content Fragments {#use-content-to-generate-content}

### Selecting the appropriate model {#select-model}

### Creating, and editing, structured content {#create-edit-structured-content}

## Getting Started with some Examples {#getting-started-examples}

## What's Next {#whats-next}

[Learn how to use GraphQL to access your Content Fragments content](fetch-your-content.md). 

## Additional Resources {#additional-resources}

* [Working with Content Fragments](/help/assets/content-fragments/content-fragments.md)
* [Content Fragment Models](/help/assets/content-fragments/content-fragments-models.md)
