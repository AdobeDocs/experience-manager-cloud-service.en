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
* Be able to determine your integration level
* Be able to define your project in terms of scope and the chosen integration level

## AEM Basics {#aem-basics}

Before you can define your headless project within AEM, it is important to understand some basic AEM concepts.

### Author Instance {#author}

At its simplest, AEM consists of an author instance and a [publish instance](#publish) which work together to create, manage, and publish your content.

Content begins on the author instance. This is where you content authors create their content. The author environment offers various tools for authors to create, organize, and reuse their content.

### Publish Instance {#publish}

Once content is created in the author instance, it must be published to be available to other services to consume. A publish instance contains all content that has been published.

### Replication {#replication}

Replication is the act of transferring content from the author instance to the publish instance. This is done automatically by AEM when an author or other user with appropriate rights publishes content.

### Repository {#repository}

All content is stored in a JCR-compliant repository. For the repository, everything is content. This means all content, code, and assets for your project are stored in the repository.

Content authors do not need to understand how their content is stored, but developers may need to access the repository directly on occasion. There are a number of ways to access information from the repository including REST and GraphQL APIs among others.

### Packages {#packages}

Because the repository contains all content for your project, including code, it must be simple to introduce new content created by your development team. Packages are self-contained, deployable units of content which can be easily installed in your repository. Packages allow for simple deployment of new code and other content as part of a development project.

### AEM Basics Summary {#aem-basics-summary}

At its simplest level, creating headless experiences in AEM requires the following steps:

1. Your developers will create their customizations and deploy them to the repository as packages.
1. Your content authors will create your headless content in the author instance.
1. When this content is ready, it is replicated to the publish instance. APIs can then be called to retrieve this content.

## AEM Headless Basics {#aem-headless-basics}

The headless capabilities of AEM are based on a few key features. These will be explained in detail in later parts of the journey. It is important now only to know what they do and what they are called.

>[!TIP]
>
>If you are alredy familiar with AEM, you can review the [Headless Getting Started Guides](/help/implementing/developing/headless/introduction.md) for a compact but thorough introduction to all of the important headless features in AEM.

### Content Fragment Models {#content-fragment-models}

Content Fragment Models define the structure of the data and content that you will create and manage in AEM. They serve as a kind of scaffolding for your content. When choosing to create content, your authors will select from the Content Fragment Models you define, which guides them in creating content.

### Content Fragments {#content-fragments}

Content Fragments allow you to design, create, curate, and publish page-independent content. They allow you to prepare content ready for use in multiple locations and over multiple channels.

Content fragments contain structured content and can be delivered in JSON format.

### GraphQL and REST APIs {#apis}

To modify your content headlessly, AEM offers two robust APIs.

* [The GraphQL API](/help/assets/content-fragments/graphql-api-content-fragments.md) allows you to create requests to access and deliver Content Fragments.
* [The Assets REST API](/help/assets/content-fragments/assets-api-content-fragments.md) allows you to create and modify Content Fragments (and other assets).

## Headless Integration Levels {#integration-levels}

AEM supports many levels of headless integration. Understanding which level is appropriate for your use case is an important part of defining your project.

### You already have an external consume of headless content such as a singe page application (SPA). {#already-have-a-spa}

Let us assume that your basic requirement is at a minimum to deliver content from AEM to an existing, external service.

#### Level 1: Content Fragment Integration {#level-1}

This level of integration allows your content authors to create content in AEM and deliver it heedlessly to any number of external services using GraphQL or to edit them from external services using the Assets API.

In this model, AEM is only used for creating and serving the content through the use of AEM Content Fragments. Rendering and interaction with the content is delegated to the consuming external application, often a single-page application (SPA).

#### Level 2: Embed the SPA in AEM {#level-2}

This level of integration builds on the first level, but also allows the external application (SPA) to be embedded in AEM so that the content authors can view the content in the context of the external application within AEM. The application can also support limited editing of the external application within AEM.

This level has the advantage of allowing content authors to flexibly author content in AEM in a headful way, with their content presented in-context with an embedded external SPA, while still delivering the content headlessly.

#### Level 3: Embed and Fully Enable SPA in AEM {#level-3}

This level of integration builds on level two by enabling most content in the external SPA to be editable within AEM.

### You do not yet have an external consumer of the headless content such as a single page application (SPA). {#do-not-have-a-spa}

If your goal is to create a new SPA that headlessly consumes content from AEM, you can use features such as Content Fragments to manage your headless content, and also build a SPA with AEM's SPA Editor framework.

Using the SPA Editor, the SPA not only consumes content from AEM, but is also fully editable within AEM by your content authors giving you both the flexibility of headless delivery and in-context editing within AEM.

## Requirements and Prerequisites {#requirements-prerequisites}

There are a number of requirements before you begin your headless AEM project.

### Knowledge {#knowledge}

* GraphQL
* Development experience creating SPAs with React or Angular frameworks
* Basic AEM skills creating Content Fragments and using the editor

### Tools {#tools}

* Sandbox access for testing deploying your project
* Local development instance for data modeling and testing
* Existing external SPA (optional, depending on [what integration level](#integration-level) is required for your project)

## Defining Your Project {#defining-your-project}

For any successful project, it is important to clearly define not only the requirements of the project, but also the roles and responsibilities.

### Scope {#scope}

It is very important to have a clearly defined scope for the project. Scope informs acceptance criteria and allows you to establish a definition of done.

The first question you need to ask yourself is "What am I trying to achieve with AEM Headless?" The answer should in general be that you have or will have in the future an experience application that you’ve built with your own development tools not in conjunction with AEM. This experience application could be a mobile app, a web site, or any other end-user customer facing experience application. The goal for using AEM Headless is to feed your experience application with content that is created, stored, and managed in AEM with state-of-the-art APIs that would call AEM Headless to fetch content or even fully CRUD content directly from your experience application. If this is not what you are looking to do, you probably want to [go back to the AEM top level documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service.html) and find the section that better suits what you want to accomplish.

### Roles and Responsibilities {#roles-responsibilities}

The roles for any individual project will vary, but important ones to consider in the content of AEM headless development are:

* [Administrator](#administrator)
* [Content Author](#content-author)
* [Content Modeler](#content-modeler)
* [Developer](#developer)

#### Administrator {#administrator}

The administrator is responsible for the base setup and configuration of your system. For example the administrator will set up your organization within the Adobe user management system, referred to Identity Management System (IMS). The administrator will be the first user from the organization to receive an email invitation from Adobe once your organization has been created by Adobe within IMS. The administrator will have the ability to login to IMS and add users of other personas.

Once the users are configured by the administrator, they will be granted the permissions to access all the AEM resources to accomplish their work as contributors to delivering the experience application using AEM Headless.

The administrator should be the user who sets up AEM and prepares the runtime environment to enable [content authors](#content-author) to create and update content and [developers](#developer) to use APIs that fetch or modify content for their experience applications.

#### Content Author {#content-author}

Content authors create and manage the content that is delivered headlessly by AEM. Content authors use AEM features such as Content Fragments and the Assets Console to manage their content.

Content authors should keep in mind the following best practices.

#### Plan for Localization {#localization}

Plan for translation and localization at the very beginning of the project. Consider "Internationalization Project Manager" as a separate persona whose responsibility it is to define what content should be translated and what not, and what translated content may be modified by regional or local content producers.

Create a plan on what content localization you will need.

* Do you just need different languages or also language to adopt to regional specifics?
* Do you need rich media content like images or videos to be different for different locales?

Be clear about you content update workflow. What is the approval process that the system needs to support?

Note that your [content hierarchy](#content-hierarchy) can be leveraged to make localization easier.

##### Leverage the Content Hierarchy {#content-hierarchy}

Folder hierarchy can address two major concerns with regards to content management:

* Localization - AEM manages localization of content by maintaining copies of content in locale-specific folders.
* Organization - Folders are used to define a content hierarchy required to support localization needs as well as logically manage Content Fragments.

AEM allows for a very flexible content structure and any hierarchy can be arbitrarily large. However it is important to realize that any changes in folder structure may have unintended consequences for existing queries that rely on the content path. Therefore a well-defined hierarchy that is set out clearly in advance, can be extremely helpful to your content authors.

Folders can also be restricted to only allow certain types of content (based on Content Fragment Models). It is generally recommended to always explicitly specify which models are allowed for all folders in the hierarchy. Specifying allowed content for a given folder:

* Prevents content authors from authoring content that do not belong in the folder.
* Optimizes the content creation process by filtering the types of content allowed in the folder during creation to only show valid types of content.

By creating an appropriate content structure, it becomes easier to coordinate headless content authoring across channels in order to maximize content reuse. Leveraging content across multiple channels will greatly improve content production efficiency and change management.

##### Establish Good Naming Conventions {#naming-conventions}

Content Fragment names must be descriptive for content authors. AEM transparently handles escaping and/or truncating the names used IDs at the repository level. Therefore the logical names provided by the content authors should always be readable and represent the contents.

* Bad Name: `cta_btn_1`
* Good Name: `Call To Action Button`

##### Don't Overextend Content Nesting {#content-nesting}

[Content Fragments](#content-fragments) are used in AEM to create headless content. AEM supports up to ten levels of content nesting for Content Fragments. However it is important to keep in mind that AEM will need to iteratively resolve each reference defined in the parent Content Fragment, then check if there are any child references in all siblings. These operations can add up quickly and become a performance concern.

As a general rule-of-thumb, Content Fragment references should not be nested beyond five levels.

#### Content Modeler {#content-modeler}

Content modelers analyze the requirements for the data that needs to be delivered headlessly and defines the structure for this data. These structures are called [Content Fragment Models](#content-fragment-models) in AEM. Content Fragment Models are used as the basis for the Content Fragments that the content authors create.

A useful approach when defining Content Fragment Models, is to create models that map to the UX components of the application(s) that will consume the content.

Because the content authors interact with the models on a continual basis as they create new content, aligning the models to the UX helps them to visualize the resulting digital experience. Taking this alignment a step further, you can assign icons to the Content Fragment Models that represent the UX element so the authors can intuitively select the right model based on visual cues.

#### Developer {#developer}

Developers are responsible for joining together the content being created headlessly in AEM to the consumer of that content, which can often be a single-page application (SPA), progressive web app (PWA), web shop, or other service external to AEM.

GraphQL serves as the "glue" between AEM and the consumers of headless content. GraphQL is the language that queries AEM for the necessary content.

Developers should keep in mind a few basic recommendations as they plan their queries:

* Queries should never rely on a fixed path (`ByPath`) to retrieve Content Fragments.
  * [Content authors have complete control on content fragment hierarchy](#content-hierarchy) and could make changes that would break such a query.
  * Queries should instead opt for content fragment model references with dynamic query parameters to filter the results to generate the desired payload.
* For best query performance, always use persisted queries in AEM. These are discussed later in the journey.
* GraphQL is designed to be declarative following the motto ["Ask for exactly what you need, and get exactly that."](https://graphql.org) This means that when creating GraphQL queries, always avoid `select *`-type queries that you might create in a relational database.

### Performance Requirements {#performance-requirements}

For any project to be a success, performance must be considered before any content is created.

You must understand your users/visitors expectations and design for those. Set service level objectives (SLOs) and measure them to understand if you meet your user's expectations.

#### Traffic Patterns {#traffic-patterns}

To understand traffic and traffic patterns start with gathering what you know from the past and then project to the expected growth over the next few years. Some of the most important variables to consider:

* How many API calls per hour/day/month do you expect and is there potential for spikes and seasonality?
* How many different content authors are there?
* How many content authors do you anticipate working concurrently?
* What is the frequency of content updates?
* How many content models are needed?
* How many instances of models will be needed?

#### Update Frequency {#update-frequency}

Quite often different sections of experiences have different frequencies of content updates. Understanding this is important to be able to fine tune CDN and cache configurations. This is also important input for the [Content Modelers](#content-modeler) as they design models to represent your content. Consider:

* Must some types of content expire after a certain period?
* Are there elements that are user-specific and thus can't be cached?

## What's Next {what-is-next}

You should continue your AEM headless journey by next reviewing the document [Path to Your First Experience Using AEM Headless](path-to-first-experience.md) where you will learn how to set up the necessary tools and how to begin thinking about modeling your data in AEM.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the headless development journey by reviewing the document [Path to Your First Experience Using AEM Headless,](path-to-first-experience.md) the following are some additional resources that do a deeper dive on some concepts mentioned in this document.

* [An Introduction to the Architecture of Adobe Experience Manager as a Cloud Service](/help/core-concepts/architecture.md) - Understand AEM as a Cloud Service's structure
* [Headless Development Getting Started Guide](/help/implementing/developing/headless/introduction.md) - A quick tour of Content Models, Content Fragments, GraphQL and how AEM delivers your content headlessly
* [Headful and Headless in AEM](/help/implementing/developing/headful-headless.md) - Understanding the different levels of integration possible with headless in AEM
* [SPA Introduction and Walkthrough](/help/implementing/developing/hybrid/introduction.md) - A quick guide to fully-editable single-page applications in AEM
