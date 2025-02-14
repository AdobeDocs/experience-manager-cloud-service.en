---
title: AEM Headless CMS Developer Journey
description: Learn about headless development using Adobe Experience Manager (AEM) as a Headless CMS. Learn how to use features like Content Models, Content Fragments, and a GraphQL API to power headless content delivery.
landing-page-description: Get an understanding of headless content delivery and implementation. Learn more about developing your strategy within your business. 
exl-id: d14a1e30-dd04-49a8-8cda-27c80a4bb0f5
solution: Experience Manager
feature: Headless, Content Fragments,GraphQL API
role: Admin, Architect, Developer
---
# AEM Headless CMS Developer Journey {#aem-headless-developer-journey}

Welcome to the documentation for developers who are new to Adobe Experience Manager headless CMS!

Learn about the powerful and flexible headless features, their capabilities, and how to use them on your first headless development project. This journey provides you with all the information you need to develop your first headless application.

{{headless-trials-promotion}}

>[!CONTEXTUALHELP]
>id="aemcloud_headless_developer_resources"
>title="AEM Headless developer resources and advanced documentation"
>abstract="Everything you need to learn about AEM headless CMS and build and ship better applications and faster experiences."
>additional-url="https://experienceleague.adobe.com/landing/experience-manager/headless/developer.html" text="AEM Headless developer resources"

## Introduction {#introduction}

The Headless implementation of AEM uses Content Fragments Models and Content Fragments to focus on the creation of structured, channel-neutral, and reusable fragments of content and their cross-channel delivery. To achieve this it forgoes page and component management as is traditional in full stack solutions. It is a modern and dynamic development pattern for implementing digital experiences.

This guide leads you through headless implementation topics in AEM so when you are done you can:

* Have a full understanding of what headless content delivery is and its benefits.
* Understand AEM's headless features and how they work together to deliver a headless experience.
* Take the first steps implementing your first AEM headless project.

>[!TIP]
>
> If you prefer to **learn by doing** and have existing knowledge of AEM, visit the AEM Headless tutorials, which are organized by API and framework and are available in the [Additional Resources section](#additional-resources) at the end of this document.

## Audience {#audience}

This journey is designed for the developer persona, laying out the requirements, steps, and approach of an AEM Headless project from a developer's perspective. The journey defines additional personas with which the developer must interact for a successful project, but the point-of-view for the journey is that of the developer.

The following are the personas that interact in this journey.

|Persona|Description|Role in This Journey|
|---|---|---|
|Developer (target audience)|Has experience developing headless applications which consume content from different sources|Target audience of this journey|
|Content Author|Creates and manages content that is delivered headlessly|Content Authors create content that the developer delivers headlessly.|
|Administrator|Manages the base setup and configuration of AEM|The developer works with the administrator to make configuration changes needed for development.|
|Content Architect|Analyzes the requirements for the data that must be delivered headlessly and defines the structure for this data|Developers work with the content architect to understand the structure of the data and requirements for delivering it headlessly.|

## The Headless Developer Journey {#the-journey}

We will cover many topics in this journey, which will provide you with the foundational knowledge of headless in AEM.

Although you can go directly to a particular part of the journey, many concepts are built on ones in previous articles. Adobe recommends that you start at the beginning and progress sequentially.

|#|Article|Description|
|---|---|---|
|0|AEM Headless Developer Journey|This document|
|1|[Learn about CMS Headless Development](learn-about.md)|Learn about Headless Technology and when to use it.|
|2|[Getting Started with AEM Headless as a Cloud Service](getting-started.md)|Learn about AEM Headless prerequisites|
|3|[Path to your first experience using AEM Headless](path-to-first-experience.md)|Setup your development environment and learn how to integrate a simple app with AEM Headless|
|4|[How to model your content](model-your-content.md)|Learn how to model your content structure.|
|5|[How to access your content via AEM delivery APIs](access-your-content.md)|Learn how to use GraphQL queries to access your Content Fragments content.|
|6|[How to update your content via AEM Assets APIs](update-your-content.md)|Learn how to use REST API to access and update your Content Fragments content.|
|7|[How to put it all together - your app and your content in AEM Headless](put-it-all-together.md)|Learn how to take your AEM Project and prepare it for going live with the AEM Headless SDK.|
|8|[How to go live with your headless application](go-live.md)|Learn how to deploy the application live and take your local code in Git and move it to Cloud Manager Git for CI/CD pipeline.|
|9|[Optional - How to create single page applications (SPAs) with AEM](create-spa.md)|Explore how to combine headful and headless delivery and learn how you can create editable SPAs using AEM's SPA Editor framework.|

{style="table-layout:auto"}

## What's Next {#what-is-next}

Get started by checking out the next article: [Learn about CMS Headless Development](learn-about.md),

### Choose Your Own Adventure {#choose-your-path}

Do you prefer to learn at your own pace? Check out these options:

* If you prefer to continue to **learn about headless concepts and AEM's headless technologies**, you should continue your AEM headless journey as recommended by next reviewing the document [How to Model Your Content as AEM Content Models](model-your-content.md) where you learn how to model your content structure in AEM.
* If you prefer to **learn by doing**, you can jump to the [Getting Started with AEM Headless hands-on tutorial](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/graphql/multi-step/overview.html) where you will jump directly into AEM Headless development by implementing a simple project to expose AEM headless content.

## Additional Resources {#additional-resources}

Documentation journeys show you how AEM solves a business problem by providing a narrative that guides you through related processes and features. A journey illustrates how multiple features work together to serve a single business need.

Check out these additional journeys for more information on how AEM's powerful features work together.

* The [AEM Developer Portal](https://experienceleague.adobe.com/landing/experience-manager/headless/developer.html)
* [AEM Headless tutorials](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/overview.html) - If you prefer to learn by doing and have existing knowledge of AEM, take our hands-on tutorials organized by API and framework, that explore creating and using applications built on AEM Headless.
* [AEM Headless Translation Journey](/help/journey-headless/translation/overview.md) - This documentation journey gives you a broad understanding of headless technology, how AEM serves headless content, and how you can translate it.
* [Headless Authoring Journey](/help/journey-headless/author/overview.md) - Start here for a guided journey through the powerful and flexible headless features of AEM, their capabilities, and how to model your content on your first headless project.
* [Headless Architect Journey](/help/journey-headless/architect/overview.md) - Start here for an introduction to the powerful, and flexible, headless features of Adobe Experience Manager as a Cloud Service, and how to model content for your project.
* [AEM as a Cloud Service technical documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service.html) - If you already have a firm understanding of AEM and headless technologies, check out our in-depth technical docs.
  * [Introduction to AEM as a Headless CMS](/help/headless/introduction.md)
