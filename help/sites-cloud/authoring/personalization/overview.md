---
title: Personalization and Content Targeting
description: Learn how you can create personalized, targeted content with AEM
exl-id: b9b5dbf6-d491-48a6-99b1-19bc1b651b8c
solution: Experience Manager Sites
feature: "Authoring, Personalization"
role: User
---

# Personalization and Content Targeting {#personalization-and-content-targeting}

Personalization of the web content that you provide to customers, means tailoring those experiences to their interests and needs. You can do this based on the information that you have about them; for example, shopping summary, age, gender, geography, among others. 

With Adobe Experience Manager as a Cloud Service (AEM) you can create a selection of content, then specify which audiences (groups of end-users) see each individual experience. This means that you are targeting your personalized experiences at specific audiences.

When your reader is online, your targeting engine will review the information available about the end-user and compare it against the experience definitions. The engine then *"decides"* which personalized experience should be displayed. 

AEM provides a framework of tools for:

* Authoring targeted content, suitable for a range of audiences, dependent on the available customer information.
* Defining the rules used to resolve the known user information against an audience definition.
* Configuring your pages to present targeted personalized experiences; to render the specific content applicable to the current end-user.

The following overview presents some of the terms used for personalization in AEM as a Cloud Service, followed by a recommended order of action.

## Experience {#experience}

An experience is content that you want to be shown to your end-users.

## Personalized Experience {#personalized-experience}

A personalized experience is an experience that is shown to a limited audience. The audience is defined by you, and the content is only shown when the information known about the current end-user corresponds to that audience definition. 

When creating pages you define multiple experiences, with each experience resolving to one (or more) audience(s). If no audience is resolved, then the default experience is displayed.

### Offer {#offer}

An offer is a personalized experience, often available for a limited time period. 

For example, a page from a sample website can use offers as the teaser image that appears at the top of the page. A Person Over 30 and a Person under 30 can see different offers as the experience teaser.

## Audience {#audience}

An audience is a group of end-users that you want to target with personalized content. When a visitor opens a web page, the page-logic determines the audience to which they belong based on known information. Based on that assessment AEM displays the content that you have created for that audience.

Audiences are based on marketing segments. They are created either in AEM or Adobe Target; you can create Adobe Target audiences directly in AEM using the Audiences console. 

### Segment {#segment}

Within AEM ContextHub, an audience is defined as a segment, based on rules (conditions). These are then resolved to render the required content.

## Activity {#activity}

An activity:

* defines the mapping of a specific audience (segment) with a specific experience 
* defines the period of time for which the targeting is applied
* identifies the [targeting engine](#targeting-engine) that your pages use

The activity can be either a personalization activity, or an A/B Test activity (in the case of the AEM and Adobe Target personalization workflow).

For example, an activity could define experiences for two separate audiences: people over the age of 30, and people under the age of 30. A page of your web site might then display different products for each audience.

Or, as another example, your product catalog may include teasers that focus attention on seasonal products. So a Summer Sports activity might define the audiences that the teasers target during summer months.

Use the [Activities console](/help/sites-cloud/authoring/personalization/activities.md) to create and manage the activities for your [Brands](#brand). You can also create activities as you author your [targeted content](/help/sites-cloud/authoring/personalization/targeted-content.md) with [Targeting mode](/help/sites-cloud/authoring/personalization/targeted-content.md#adding-and-removing-experiences-using-targeting-mode).

### Brand {#brand}

A Brand holds a selection of marketing activities and areas.

When you create a brand using the Activities console, it also appears in the Offers console.

### Area {#area}

An area is a subdivision of a Brand.

## Targeting Mode {#targeting-mode}

When authoring, this is the editing mode used to activate, and configure, the components for personalization.

You can [Author targeted content](/help/sites-cloud/authoring/personalization/targeted-content.md) using the Targeting mode of AEM. Targeting mode and the Target component provide tools for creating content for the experiences of your marketing activities.

## Experience Fragment {#experience-fragments}

A grouped set of components that make up an experience. 

[Experience Fragments](/help/sites-cloud/authoring/fragments/content-fragments.md#personalization-experience-fragment) are made of content and information (styling, and so on) to create an experience; they can be used directly when page authoring. They can be thought of as a subset of an AEM page. They allow content authors to reuse content across channels, including Sites pages and third-party systems.  

For a personalization example, a Title, Image, Description, and Call To Action Button can be combined to form a teaser experience. Using Experience Fragments is a key part of using Adobe Target personalization.

## Targeting Engine {#targeting-engine}

The targeting engine is the mechanism that resolves the logic for targeted content. [Activities](/help/sites-cloud/authoring/personalization/activities.md) are configured to use one of two targeting engines that are available: AEM and Adobe Target.

The Targeting Engine is the platform or mechanism that decides which personalization system to use. 

Currently AEM can use:

* [AEM ContextHub](#aem-contexthub) (standard AEM)
* the [Adobe Target](#adobe-target) personalization engine

>[!CAUTION]
>
>A single AEM page cannot use both engines at the same time.
>
>You can use both engines on separate pages within the same site.

### AEM ContextHub {#aem-contexthub}

AEM provides the built-in targeting engine [ContextHub](/help/implementing/developing/personalization/contexthub.md) that processes page requests and determines the content to display. When using the AEM targeting engine, you are limited to using segments that are created in AEM for defining the audiences of your experiences.

### Adobe Target {#adobe-target}

The [Adobe Target](/help/sites-cloud/integrating/integrating-adobe-target.md) targeting engine causes information gathered from page visits to be tracked in Adobe Target.

* When using this targeting engine, you use the segments that you import from Adobe Target to define the audiences for your experiences.
* Activities that use the Adobe Target engine are [synchronized to Target](/help/sites-cloud/authoring/personalization/activities.md#synchronizing-activities-with-adobe-target).

You can use this engine when you have [integrated with Adobe Target](/help/sites-cloud/integrating/integrating-adobe-target.md).

## How to set up your personalized content {#how-to-setup-personalized-content}

There are various steps and definitions required for delivering your personalized content:

1. Setup your Targeting Engine by either:

   1. Configuring [ContextHub](/help/implementing/developing/personalization/configuring-contexthub.md)
   1. Integrating with [Adobe Target](/help/sites-cloud/integrating/integrating-adobe-target.md)

1. Configure the audiences.

   1. Depending on your targeting engine, define the [Target audience](https://experienceleague.adobe.com/docs/target/using/audiences/target.html) or [ContextHub segment](/help/sites-cloud/authoring/personalization/contexthub-segmentation.md), together with the rules.

1. Create your [Brand and Activities](/help/sites-cloud/authoring/personalization/activities.md).

1. Author the selection of experiences that you want shown to the various audiences.

1. Personalize these experiences, by [targeting](/help/sites-cloud/authoring/personalization/targeted-content.md) them to the specific audiences (segments).