---
title: Getting Started with AEM Headless as a Cloud Service
description: In this part of the AEM Headless Developer Journey, learn about AEM Headless prerequisites.
---

# Getting Started with AEM Headless as a Cloud Service {#getting-started}

In this part of the [AEM Headless Developer Journey,](#overview.md) learn about AEM Headless prerequisites.

## Objective {#objective}

This document helps you understand AEM Headless in the context of your own project. After reading you should:

* Understand the basics of AEM's headless features
* Know the prerequisites for using AEM's headless features
* Be able to determine your integration model
* Be able to define your project in terms of scope and the chosen integration model

## AEM Basics {#aem-basics}

Before you can define your headless project within AEM, it is important to understand some basic AEM concepts.

### Author {#author}

At its simplest, AEM consists of an author instance and a [publish instance](#publish) which work together to create, manage, and publish your content.

Content begins on the author instance. This is where you content authors create their content. The author environment offers various tools for authors to create, organize, and refuse their content.

### Publish {#publish}

Once content is created in the author instance, it must be published to be available to other services to consume. A publish instance contains all content that has been published.

### Replication {#replication}

Replication is the act of transferring content from the author instance to the publish instance.

### Repository {#repository}

All content is stored in a JCR-compliant repository. For the repository, everything is content. This means all content, code, and assets for your project are stored in the repository.

Content authors do not need to understand how their content is stored, but developers may need to access the repository directly on occasion. There are a number of ways to access information from the repository including REST and GraphQL APIs among others.

### Packages {#packages}

Because the repository contains all code for your project, it must be simple to introduce new code. Packages contain code which can be deployed to your repository. Packages can also contain other content as well.

### AEM Basics Summary {#aem-basics-summary}

At its simplest level, creating headless experiences in AEM requires the following steps:

1. Your developers will create their customizations and deploy them to the repository as packages.
1. Your content authors will create your headless content in the author instance.
1. When this content is ready, it is replicated to the publish instance. APIs can then be called to retrieve this content.

## Headless Integration Levels {#integration-levels}

AEM supports many levels of headless integration. Understanding which models is appropriate for your use case is important for defining your project.

### You already have an external consume of headless content such as a singe page application (SPA). {#already-have-a-spa}

Let us assume that your basic requirement is at a minimum to deliver content from AEM to an existing, external service.

#### Level 1: Content Fragment Integration {#level-1}

This level of integration allows your content authors to create content in AEM and deliver it heedlessly to any number of external services using GraphQL or to edit them from external services using the Assets API.

In this model, AEM is only used for creating and serving the content through the use of AEM Content Fragments. Rendering and interaction with the content is delegated to the consuming application, often a single-page application (SPA).

#### Level 2: Embed the SPA in AEM {#level-2}

This level of integration builds on the first level, but also allows the external application (SPA) to be embedded in AEM so that the content authors can view the content in the context of the external application. The application can also support limited editing of the external application within AEM.

This level has the advantage of allowing content authors to flexibly author some content in AEM in a headless way, while still delivering other content headlessly.

#### Level 3: Embed and Fully Enable SPA in AEM {#level-3}

This level of integration builds on level two by enabling most content in the external SPA to be editable within AEM.

### You do not yet have an external consumer of the headless content such as a single page application (SPA). {#do-not-have-a-spa}

If your goal is to create a new SPA that headlessly consumes content from AEM, you can use features such as Content Fragments to manage your headless content, and also build a SPA with AEM's SPA Editor framework.

Using the SPA Editor, the SPA not only consumes content from AEM, but is also fully editable within AEM by your content authors.

## Requirements and Prerequisites {#requirements-prerequisites}

There are a number of requirements before you begin your headless AEM project.

### Knowledge {#knowledge}

* GraphQL
* Development experience creating SPAs with React or Angular frameworks
* Basic AEM skills creating Content Fragments and using the editor

### Tools {#tools}

* Sandbox access for testing deploying your project
* Local development instance for data modeling and testing
* Existing external SPA (optional, depending on [what integration level](#integration-level) is chosen)

## Defining Your Project {#defining-your-project}

For any successful project, it is important to clearly define not only the requirements of the project, but also the roles and responsibilities.

### Scope {#scope}

It is very important to have a clearly defined scope for the project. Scope informs acceptance criteria and allows you to establish a definition of done.

### Roles and Responsibilities {#roles-responsibilities}

tbd

### Performance Requirements {#performance-requirements}

tbd

## What's Next {what-is-next}

You should continue your AEM headless journey by next reviewing the document [Path to Your First Experience Using AEM Headless](path-to-first-experience.md) where you will learn how to set up the necessary tools and how to begin thinking about modeling your data in AEM.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the headless development journey by reviewing the document [Path to Your First Experience Using AEM Headless,](path-to-first-experience.md) the following are some additional resources that do a deeper dive on some concepts mentioned in this document.

* [An Introduction to the Architecture of Adobe Experience Manager as a Cloud Service](/help/core-concepts/architecture.md) - Understand AEM as a Cloud Service's structure
* [Headless Development Getting Started Guide](/help/implementing/developing/headless/introduction.md) - A quick tour of Content Models, Content Fragments, GraphQL and how AEM delivers your content headlessly
* [Headful and Headless in AEM](/help/implementing/developing/headful-headless.md) - Understanding the different levels of integration possible with headless in AEM
* [SPA Introduction and Walkthrough](/help/implementing/developing/hybrid/introduction.md) - A quick guide to fully-editable single-page applications in AEM
