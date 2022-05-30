---
title: Introduction to AEM Headless
description: Learn about Adobe Experience Manager (AEM) as a Headless CMS with a combination of detailed documentation and headless journeys. Learn how features like Content Models, Content Fragments, and a GraphQL API are used to power headless experiences.
landing-page-description: Understand how to use and administer Experience Manager Headless as a Cloud Service.
exl-id: 24300499-ae9c-49d0-aa25-f51e14d9cf79
---

# Introduction to Adobe Experience Manager as a Headless CMS {#introduction-aem-headless}

Learn how to use Adobe Experience Manager (AEM) as a Headless CMS, with features such as Content Models, Content Fragments, and a GraphQL API that power headless experiences at scale.

You can read detailed documentation of the various features involved and/or follow the selection of [Headless Journeys to get an overview of the first steps](#first-steps).

## Overview {#overview}

AEM Headless is a CMS solution from Experience Manager that allows structured content (Content Fragments) in AEM to be consumed by any app over HTTP using GraphQL. Headless implementations enable delivery of experiences across platforms and channels at scale.

Headless implementation forgoes page and component management as is traditional in full stack and hybrid solutions and focuses on the creation of channel-neutral, reusable fragments of content and their cross-channel delivery. It is a modern and dynamic development pattern for implementing web experiences.

![AEM Implementation Models](assets/aem-implementation-models.png)

## Features of AEM Headless {#aem-headless-features}

AEM as a Cloud Service is a flexible tool for the headless implementation model by offering three powerful features:

1. **Content Models**
   * Content Models are structured representation of content.
   * Content Models are defined by information architects in the AEM Content Fragment Model editor.
   * Content Models serve as a basis for Content Fragments.
1. **Content Fragments**
   * Content Fragments are created based on a Content Model.
   * Created by content authors using the AEM Content Fragment editor.
   * Content Fragments are stored in AEM Assets and managed in Assets Admin UI.
1. **Content API for delivery**
   * The AEM GraphQL API supports Content Fragment delivery.
   * The AEM Assets REST API supports Content Fragment CRUD operations.
   * Direct content delivery is also possible with the [JSON export of the Content Fragment Core Component](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/components/content-fragment-component.html).

## Your First Steps with AEM Headless {#first-steps}

There are several resources available to get started with AEM's headless features. Each guide  is tailored for different use cases and audiences.

|Resource|Description|Type|Audience|Est. Time|
|---|---|---|---|---|
|[Headless Developer Journey](/help/journey-headless/developer/overview.md)|**For developers new to AEM and headless** technologies, start here for a comprehensive introduction to AEM and its headless features from the theory of headless through going live with your first headless project.|Guide|Developers **new to AEM and headless**|1 hour|
|[Headless Setup](/help/headless/setup/introduction.md)|**For experienced AEM users** who need a short summary of the key AEM headless features, check out this quick start overview.|Reference Setup|Developers, Administrators **with AEM experience**|20 minutes|
|[Headless hands-on tutorial](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/graphql/multi-step/overview.html)|**If you prefer a hands-on approach and are familiar with AEM**, this tutorial dives directly into implementing a simple headless app.|Tutorial|Developers|2 hours|
| [Headless Architect Journey](/help/journey-headless/architect/overview.md) | **For architects new to AEM and headless** technologies, start here for an introduction to the powerful, and flexible, headless features of Adobe Experience Manager as a Cloud Service, and how to model content for your project. | Guide | Architects | 1 hour |
| [Headless Authoring Journey](/help/journey-headless/author/overview.md) | **For business users new to AEM and headless** technologies, start here for an introduction to the powerful, and flexible, headless features of Adobe Experience Manager as a Cloud Service, and how to model content for your project. | Guide | Content Creators | 1 hour |
| [Headless Translation Journey](/help/journey-headless/translation/overview.md) | For those **interested in AEM's translation approach to headless**. Learn about headless technologies and how to create and update translation projects in AEM from A to Z. | Guide | Translation Specialists | 1 hour |

## Comparing Headful and Headless {#headful-headless}

This guide focuses on the full headless implementation model of AEM. However headful versus headless need not be a binary choice in AEM. Headless features can be used to manage and deliver content to multiple touch-points, while also enabling content authors to edit single page applications. All in AEM.

>[!TIP]
>
>See the document [Headful and Headless in AEM](/help/implementing/developing/headful-headless.md) for more information.