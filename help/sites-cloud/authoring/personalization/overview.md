---
title: Personalization and Content Targeting
description: Learn how AEM can create personalized content
exl-id: b9b5dbf6-d491-48a6-99b1-19bc1b651b8c
---
# Personalization and Content Targeting {#personalization}

## Personalization and Content Targeting {#personalization-and-content-targeting}

Personalization of the web content that you provide to customers, means tailoring those experiences to their needs. This is based on the information that you have about them; for example, shopping summary, age, gender, geography amongst others. 

Your Targeting engine then *decides* which personalized content (also known as Experience) should be displayed based on the current *Audience* (also known as Segment, defined by a Rule). 

Adobe Experience Manager as a Cloud Service (AEM) provides a framework of tools for:

* authoring targeted content, for a range of audiences dependent on the available customer information
* defining the rules; used to resolve the known user information against an audience definition (segment)
* configuring your pages to present targeted personalized experiences; to render the specific content applicable to the current customer

The following overview helps you understand terms used for Personalization in AEM as a Cloud Service (with more details in the following sections):

* **Audience**
  Audiences are groups of end users that you want to target with personalized content. 

* **Segment**
  Within AEM, an audience is defined as a segment, based on rules (conditions). These are then resolved by the targeting engine to render the required content.

* **Experience**
  The experience is content that you want to be shown to an audience.

* **Activity**
  An [activity](#activities) defines the mapping of a specific segment (audience) with a specific experience. This can be either be a personalization activity, or an A/B Test activity (in the case of the AEM+Target personalization workflow).  

* **Personalized Experiences**
  A [personalized experience](#personalized-experiences) is the personalized content to be displayed to your end customer, based on the audience definition; the segment that was resolved according to the rules. 
  When creating pages you define multiple experiences, with each experience resolving to one (or more) segment. If no segment is resolved then default experience is displayed.

* **Targeting Engine** 
  The [Targeting Engine](#targeting-engine) is the platform or mechanism that decides which personalization system to use. 
  Currently AEM can use:
  * [AEM ContextHub](#aem-contexthub) (standard AEM)
  * the [Adobe Target](#adobe-target) personalization engine

  >[!CAUTION]
  >
  >A single AEM page cannot use both engines at the same time.
  >
  >You can use both engines on separate pages within the same site.

* **Offer**
  An [Offer](#offers) is the content that appears at a location on a page for an experience. Its best to use different offers for different experiences to maximize the effectiveness of the content for your audiences.  AEM component(teaser, hero, image) or the Experience Fragment(XF) that is created in AEM and will be personalized for a user 

* **Targeting Mode**
  When authoring, this is the editing mode used to activate, and configure, the components for personalization.
  You can [Author targeted content](/help/sites-cloud/authoring/personalization/targeted-content.md) using the Targeting mode of AEM. Targeting mode and the Target component provide tools for creating content for the experiences of your marketing activities.

<!--
* **Experience Fragment**
  A grouped set of components that make up an experience. 
  Experience Fragments are made of content and presentation to create an experience; they can be used directly when page authoring. They can be thought of as a sub-set of an AEM page. They allow content authors to reuse content across channels, including Sites pages and third party systems.  
  For an personalization example, a Title, Image, Description, and Call To Action Button can be combined to form a teaser experience. Using Experience Fragments is a key part of using Adobe Target personalization.

* **Content Fragment**
  Presentation-agnostic pieces of content. When using these for page authoring you need to format them on the page. Content Fragments are often used for headless delivery.
-->

## Activities {#activities}

Activities define and organize your marketing efforts. Activities comprise the audiences that you are targeting, and the period of time when the targeting is applied.

For example, your product catalog may include teasers that focus attention on seasonal products. The Summer Sports activity defines the marketing segments that the teasers target during summer months.

Activities also identify the [targeting engine](#targeting-engine) that your pages use.

Use the [Activities console](/help/sites-cloud/authoring/personalization/activities.md) to create and manage the activities for your brands. You can also create activities as you [author targeted content](/help/sites-cloud/authoring/personalization/targeted-content.md).

## Personalized Experiences {#personalized-experiences}

For each activity, you define one or more experiences that identify the audiences that you are targeting. AEM enables you to control the content that comprises each experience.

Audiences are based on marketing segments that are created either in AEM or Adobe Target. When a visitor opens a web page, the page logic determines the audience to which they belong and displays the content that you have created for that audience.

For example, an activity defines experiences for two separate audiences: women over the age of 30 and women under the age of 30. The women's page of a web site might display different products for each experience.

You define experiences for an activity. You can use the [Activities console](/help/sites-cloud/authoring/personalization/activities.md#adding-editing-an-activity-using-the-activities-console) or [Targeting mode](/help/sites-cloud/authoring/personalization/targeted-content.md#adding-and-removing-experiences-using-targeting-mode) to add experiences to an activity.

## Offers {#offers}

An offer is content that appears at a location on a page for an experience. Use different offers for different experiences to maximize the effectiveness of the content for your audiences.

For example, the women's page of a sample web site can use offers as the teaser image that appears at the top of the page. A different offer is used as the teaser for the Female Over 30 experience and for the Female Under 30 experience.

Use [Experience Fragments](/help/sites-cloud/authoring/fundamentals/experience-fragments.md#personalization-experience-fragment) to create offers that you can use in multiple experiences. Create single-use offers or add offers from an offer library when [authoring targeted content](/help/sites-cloud/authoring/personalization/targeted-content.md).

<!--
Use the [Offers console](/help/sites-cloud/authoring/personalization/offers.md) to create offers that you can use in multiple experiences. Create single-use offers or add offers from an offer library when [authoring targeted content](/help/sites-cloud/authoring/personalization/targeted-content.md).
-->

## Targeting Engine {#targeting-engine}

The targeting engine is the mechanism that drives the logic for targeted content. [Activities](/help/sites-cloud/authoring/personalization/activities.md) are configured to use one of two targeting engines that are available: AEM and Adobe Target.

### AEM ContextHub {#aem-contexthub}

AEM provides the built-in targeting engine ContextHub that processes page requests and determines the content to display. When using the AEM targeting engine, you are limited to using segments that are created in AEM for defining the audiences of your experiences.

### Adobe Target {#adobe-target}

The Adobe Target targeting engine causes information gathered from page visits to be tracked in Adobe Target.

* When using this targeting engine, you use the segments that you import from Adobe Target to define the audiences for your experiences.
* Activities that use the Adobe Target engine are [synchronized to Target](/help/sites-cloud/authoring/personalization/activities.md#synchronizing-activities-with-adobe-target).

You can use this engine when you have [integrated with Adobe Target](/help/sites-cloud/integrating/integration-adobe-target-ims.md).

### How to set up your personalized content {#how-to-setup-personalized-content}

There are various definitions required for delivering your personalized content:

1. Configure the audiences.

   1. Define the segment, according to rules.

1. Author the selection of experiences that you want shown to the various audiences.

1. Personalize these experiences, by targeting them to the specific audiences (segments).