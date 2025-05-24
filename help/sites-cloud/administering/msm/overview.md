---
title: Reusing Content - Multi Site Manager and Live Copy
description: Get an introduction to reusing content with AEM's powerful Live Copies and the Multi Site Manager features.
feature: Multi Site Manager
role: Admin
exl-id: 22b4041f-1df9-4189-8a09-cbc0c89fbf2e
solution: Experience Manager Sites
---
# Reusing Content: Multi Site Manager and Live Copy {#multi-site-manager-and-live-copy}

The Multi Site Manager (MSM) enables you to use the same site content in multiple locations. MSM uses its Live Copy functionality to achieve this.

* With MSM you can:
  * Create content once and then
  * Reuse this content in other areas (via [Live Copies](#live-copies)) of the same or other sites.
* MSM then maintains the live relationships between your source content and its Live Copies so that:
  * When you change the source content, the source and Live Copies are synchronized.
  * You can make adjustments only to the content of the Live Copies by disconnecting the live relationship for individual sub pages and/or components.

This page provides an overview of reusing content with MSM. The following pages cover related issues in detail.

* [Creating and Synchronizing Live Copies](creating-live-copies.md)
* [Live Copy Overview Console](live-copy-overview.md)
* [Configuring Live Copy Synchronization](live-copy-sync-config.md)
* [MSM Rollout Conflicts](rollout-conflicts.md)
* [MSM Best Practices](best-practices.md)

>[!NOTE]
>
>MSM can also be used for Assets, including Content Fragments. See [Reuse Content Fragments using MSM for Assets](/help/assets/reuse-assets-using-msm.md) (only available through the Assets console).

## Possible Scenarios {#possible-scenarios}

There are many use-cases for MSM and Live Copies. Some scenarios include:

* **Multinationals - Global to Local Company**

  One typical use case that MSM supports is to reuse content in several multinational same-language sites. This allows the core content to be reused, while also permitting national variations.

  For example, the English section of the [WKND tutorial sample](/help/implementing/developing/introduction/develop-wknd-tutorial.md) is created for customers in the USA. Most of the content in this site can also be used for other WKND sites that cater to English-speaking customers of different countries and cultures. The core content remains the same over all sites, while regional adjustments can be made.

  The following structure can be used for sites for the United States and Canada. Note how `language-masters` node maintains the master copy of not only English but other language content. This content can be used as the basis for additional regional language content alongside English.

  ```xml
  /content
      |- wknd
          |- language-masters
              |- en
              |- es
              |- fr
          |- us
              |- en
              |- es
          |- ca
              |- en
              |- fr
  ```

  >[!NOTE]
  >
  >MSM does not translate the content. It is used to create the required structure and deploy the content.
  >
  >
  >See [Translating Content for Multilingual Sites](/help/sites-cloud/administering/translation/overview.md) for such an example.

* **National - Head-Office to Regional Branches**

  Alternatively a company with a network of dealers might want separate websites for its individual dealerships, each being a variation of the main site provided by the head-office. This might be for a single company with multiple regional offices, or a national franchise system comprised of a central franchisor and multiple local franchisees.

  The head office can supply the core information, whereas the regional entities can add local information, such as contact details, opening hours and events.

  ```xml
  /content
      |- head-office-berlin
      |- branch-hamburg
      |- branch-stuttgart
      |- branch-munich
      |- branch-frankfurt
  ```

* **Multiple Versions**

  MSM can create versions of a specific sub-branch. For example, a support sub-site can hold details of the different versions of a specific product, where the base information remains constant and only the updated features need to be changed:

  ```xml
  /content
      |- game-support
          |- polybius
              |- v5.0
              |- v4.0
              |- v3.0
              |- v2.0
              |- v1.0
  ```

  >[!TIP]
  >
  >In such a scenario this is the question of whether to make a straightforward copy or use Live Copies, which is a balance of:
  >
  >* How much of the core content needs updating over multiple versions.
  >
  >Against:
  >
  >* How much of the individual copies must be adjusted.

## MSM from the UI {#msm-from-the-ui}

MSM is directly accessible in the UI using various options from the appropriate console.

* **Create Site** (**Sites**)

  * MSM helps you to manage multiple websites that share common content. For example, websites are often provided for international audiences such that most of the content is common across all countries, with a subset of the content specific to the individual country. MSM lets you [create Live Copies that automatically update one or more sites based on your source site](creating-live-copies.md#creating-a-live-copy-of-a-site-from-a-blueprint-configuration). This also helps you to enforce a common base structure, use the common content across the multiple sites, maintain a common look and feel and focus efforts on managing the content that actually differs between the sites. Creating a site in this manner:
    * Requires a predefined blueprint configuration to specify the source.
    * Creates a Live Copy of the (predefined) source.
    * Provides the user with the **Rollout** button.

* **Create Live Copy** (**Sites**)

  * MSM lets you [create an ad-hoc (one-off) Live Copy of an individual page or sub-branch of a website](creating-live-copies.md#creating-a-live-copy-of-a-page). For example, duplicating a sub-branch to provide information about a new/updated version of a product. Creating a Live Copy in this manner:
    * Creates an ad-hoc Live Copy (no blueprint configuration required).
    * Can be used to (immediately) create a Live Copy of any page/branch.
    * Requires **Synchronize** (does not provide the **Rollout** button).

* **View Properties** (**Sites**)

  * Where appropriate, this option helps you [monitor your Live Copy](creating-live-copies.md#monitoring-your-live-copy) by providing information on the related **Live Copy** or **Blueprint**.

* **References** (**Sites**)

  * The [References](/help/sites-cloud/authoring/basic-handling.md#references) rail provides information about **Live Copies** together with access to appropriate actions.

* **Live Copy Overview** (**Sites**)

  * This console lets you [view and manage your blueprint and its Live Copies](live-copy-overview.md).

* **Blueprints** (**Tools** - **Sites**)

  * This console lets you [create and manage your blueprint configurations](creating-live-copies.md#creating-a-blueprint-configuration).

>[!NOTE]
>
>MSM can be used with both pages and [Experience Fragments](/help/sites-cloud/authoring/fragments/experience-fragments.md) as these fragments are part of an experience (page).

>[!NOTE]
>
>Aspects of MSM functionality are used in several other AEM features such as Launches. In these cases the Live Copy is managed by that feature.

### Terms Used {#terms-used}

As an introduction, the following table provides an overview of the main terms used with MSM. These are covered in more details in the subsequent sections and pages.

|Term|Definition|Further Details|
|---|---|---|
|Source|The original pages used as the basis for Live Copies|Synonymous with Blueprints and/or Blueprint pages|
|Live Copy|The copy (of the source), maintained by synchronization actions as defined by the rollout configurations||
Live Copy Configuration|Definition of the configuration details for a Live Copy||
|Live Relationship|Effective definition of the inheritance for a given resource that is, the connection(s) between the source and Live Copies|Ensures that changes to the source can be synchronized with the Live Copy|
|Blueprint|Synonymous with Source|Can be defined by a blueprint configuration|
|Blueprint Configuration|Predefined configuration specifying a source path|When a blueprint page is referenced in a blueprint configuration the Rollout command becomes available|
|Chapter|The sections of the blueprint to include in the Live Copy|These are generally sub-pages of the root|
|Synchronization|The generic term for the synchronization of content between the source and the Live Copies (by both **Rollout** and **Synchronize** options)||
|Rollout|Synchronizes from the source to the Live Copy|Can be triggered by an author (on a blueprint page) or by a system event (as defined by the rollout configuration)|
|Rollout Configuration|Rules that determine which properties are synchronized, how, and when||
|Synchronize|A manual request for synchronization, made from the Live Copy pages||
|Inheritance|A Live Copy page/component inherits content from its source page/component when synchronization occurs||
|Suspend|Temporarily removes the live relationship between a Live Copy and its blueprint page||
|Detach|Permanently removes the live relationship between a Live Copy and its blueprint page||
|Reset|Reset a Live Copy page to remove all inheritance cancellations and return the page to the same state as the source page|Reset affects any changes that you have made to page properties, the paragraph system and components.|
|Shallow|A Live Copy of a single page||
|Deep|A Live Copy of a page, together with its child pages||

>[!TIP]
>
>See [Extending the Multi Site Manager](/help/implementing/developing/extending/msm.md#overview-of-the-java-api) for the object names.

## Live Copies {#live-copies}

An MSM Live Copy is a copy of specific site content for which a live relationship with the original source is maintained:

* The Live Copy inherits content from its source.
* Synchronization performs the actual transfer of content when changes are made to the source.
* A Live Copy can be considered as either:
  * Shallow: a single page
  * Deep: the page, together with its child pages
* Synchronization rules, called rollout configurations, determine which properties are synchronized and when the synchronization occurs.

In the previous example, `/content/wknd/language-masters/en` is the global master site in English. To reuse the content of this site, MSM Live Copies are created:

* The content below `/content/wknd/language-masters/en` is the source.
* The content below `/content/wknd/language-masters/en` is copied below the `/content/wknd/us/en/` and `/content/wknd/ca/en` nodes. These are the Live Copies.
* Authors change pages below `/content/wknd/language-masters/en`.
* When triggered, MSM synchronizes these changes to the Live Copies.

### Live Copies - Composition {#live-copies-composition}

>[!NOTE]
>
>The diagrams and descriptions in this section represent snapshots of potential Live Copies. They are not comprehensive, but provide an overview to highlight specific characteristics.

When you initially create a Live Copy, the selected source pages are reflected on a 1:1 basis in the Live Copy. After this, new resources (pages and/or paragraphs) can also be created directly within the Live Copy, so it is useful to be aware of these variations and how they impact synchronization. Possible compositions include:

* [Live Copy with non-Live-Copy pages](#live-copy-with-non-live-copy-pages)
* [Nested Live Copies](#nested-live-copies)

The basic form of Live Copy has:

* Live Copy pages that reflect the selected source pages on a 1:1 basis.
* One configuration definition.
* A live relationship defined for every resource:
  * Link the Live Copy resource with its blueprint/source.
  * Are used when realizing inheritance and rollout.

Changes can be [synchronized](creating-live-copies.md#synchronizing-your-live-copy) according to requirements.

![Live Copy composition overview](../assets/live-copy-composition.png)

#### Live Copy with non-Live-Copy Pages {#live-copy-with-non-live-copy-pages}

When you create a Live Copy in AEM, you can see and navigate through the Live Copy branch and use normal AEM functionality on the Live Copy branch. This means that you (or a process) can create new resources (pages and/or paragraphs) inside the Live Copy. For example, a product for a particular region or country.

* Such resources have no live relationship to the source/blueprint pages and are not synchronized.
* Scenarios can occur that MSM handles as special cases. For example, when you (or a process) create a page with the same position and name in both the source/blueprint and Live Copy branches. For such situations see [MSM Rollout Conflicts](rollout-conflicts.md) for more information.

![Live Copy with non-Live Copy pages](../assets/live-copy-with-non-live-copy-pages.png)

#### Nested Live Copies {#nested-live-copies}

When you (or a process) create a [new page within an existing Live Copy](#live-copy-with-non-live-copy-pages) this new page can also be set up as a Live Copy of a different blueprint. This is known as a nested Live Copy. In nested Live Copies the behavior of the second or inner Live Copy is affected by the first or outer Live Copy in the following ways:

* A deep rollout triggered for the top-level Live Copy can be continued into the nested Live Copy.
* Any links between the sources are rewritten within the Live Copies.

For example, links that point from the second to the first blueprint are rewritten as links pointing from the nested/second Live Copy to the first Live Copy.

![Nested Live Copies](../assets/live-copy-nested.png)

>[!NOTE]
>
>If you move or rename a page within the Live Copy branch, it is treated as a nested Live Copy to enable AEM to track the relationships.

#### Stacked Live Copies {#stacked-live-copies}

A Live Copy is known as a stacked Live Copy when it is created as the child of a shallow Live Copy. It behaves in the same manner as a [nested Live Copy](#nested-live-copies).

### Source, Blueprints and Blueprint Configurations {#source-blueprints-and-blueprint-configurations}

Any page or branch of pages can be used as the source of a Live Copy. However, MSM also lets you define a blueprint configuration that specifies a source path. The benefits of using a blueprint configuration are that they:

* Allow the author to use the **Rollout** option on a blueprint. I.e. to explicitly push modifications to Live Copies that inherit from this blueprint.
* Allow the author to use **Create Site**. This allows the user to easily select languages and configure the structure of the Live Copy.
* Define a default rollout configuration for Live Copies that have a relationship with the blueprint.

The source for a Live Copy can be either regular pages or pages encompassed by a blueprint configuration. Both are valid use cases.

The source forms the blueprint for the Live Copy. The blueprint is defined when you either:

* [Create a Blueprint configuration](creating-live-copies.md#creating-a-blueprint-configuration) - The configuration defines in advance the pages to be used to create the Live Copy.
* [Create a Live Copy of a Page](creating-live-copies.md#creating-a-live-copy-of-a-page) - The pages used to create the Live Copy (the source pages) are the blueprint pages. The source page might or might not be referenced by a blueprint configuration.

### Rollout and Synchronize {#rollout-and-synchronize}

A rollout is the central MSM action that synchronizes Live Copies with their sources. You can perform rollouts manually or they can occur automatically.

* A [rollout configuration](#rollout-configurations) can be defined so that specific [events](live-copy-sync-config.md#rollout-triggers) can cause a rollout to occur automatically.
* When authoring a blueprint page you can use the **[Rollout](creating-live-copies.md#rolling-out-a-blueprint)** command to push changes to the Live Copy.
  * The **Rollout** command is available on a blueprint page that is referenced by a blueprint configuration.

  ![Rollout](../assets/live-copy-rollout.png)

* When authoring a Live Copy page you can use the **[Synchronize](creating-live-copies.md#synchronizing-a-live-copy)** command to pull changes from the source to the Live Copy.
  * The **Synchronize** command is always available on the Live Copy page regardless of whether the source/blueprint page is encompassed by a blueprint configuration.

  ![Synchronize](../assets/live-copy-synchronize.png)

### Rollout Configurations {#rollout-configurations}

A rollout configuration defines when and how a Live Copy is synchronized with the source content. A rollout configuration consists of a trigger and one or more synchronization actions:

* **Trigger** - A trigger is an event that causes the live action synchronization to occur, such as the activation of a source page. MSM defines the triggers that you can use.
* **Synchronization Actions** - Synchronization actions are performed on the Live Copy to synchronize it with the source. Example actions are copying content, ordering child nodes, and activating the Live Copy page. MSM provides several synchronization actions.

>[!NOTE]
>
>You can create custom actions for your instance using the Java API.

Rollout configurations can be reused, so that more than one Live Copy can use the same rollout configuration. Several [rollout configurations](live-copy-sync-config.md#installed-rollout-configurations) are included in a standard installation.

### Rollout Conflicts {#rollout-conflicts}

Rollouts can become complicated, especially when authors are editing content in both the source and the Live Copy. So it is useful to be aware of how AEM handles any [conflicts that might occur during rollout](rollout-conflicts.md).

### Suspending and Cancelling Inheritance and Synchronization {#suspending-and-cancelling-inheritance-and-synchronization}

Each page and component in a Live Copy is associated with its source page and component via a live relationship. The live relationship configures the synchronization of Live Copy content from the source.

You can **Suspend** the Live Copy inheritance for a Live Copy page so that you can change page properties and components. When you suspend inheritance, the page properties and components are no longer synchronized with the source.

When editing an individual page, authors can **Cancel Inheritance** for a component. When inheritance is cancelled, the live relationship is suspended and synchronization does not occur for that component. Cancelling inheritance and synchronization is useful when sub-sections of the content must be customized.

### Detaching a Live Copy {#detaching-a-live-copy}

You can also [detach a Live Copy](creating-live-copies.md#detaching-a-live-copy) from its blueprint to remove all connections.

>[!CAUTION]
>
>The Detach action is permanent and non-reversible.

The detach action permanently removes the live relationship between a Live Copy and its blueprint page. All MSM-relevant properties are removed from the Live Copy and the Live Copy pages become a standalone copy.

>[!TIP]
>
>See [Detaching a Live Copy](creating-live-copies.md#detaching-a-live-copy) for full details, including the related impact on sub- and parent pages.

## Standard Steps for Using MSM {#standard-steps-for-using-msm}

The following steps describe the standard procedure for using MSM to reuse content and synchronize changes to Live Copies.

1. Develop the content of the source site.
1. Determine the rollout configuration to use.

    1. MSM [installs several rollout configurations](live-copy-sync-config.md#installed-rollout-configurations) that can satisfy several use cases.
    1. Optionally you can [create a rollout configuration](live-copy-sync-config.md#creating-a-rollout-configuration) if necessary.

1. Determine where you need to [specify the rollout configurations to use](live-copy-sync-config.md#specifying-the-rollout-configurations-to-use) and configure as required.
1. If necessary, [create a blueprint configuration](creating-live-copies.md#creating-a-blueprint-configuration) that identifies the source content of the Live Copy.
1. [Create a Live Copy](creating-live-copies.md#creating-a-live-copy).
1. Make changes to the source content as required. You should employ the normal content review and approval process that your organization has established.
1. [Roll out](creating-live-copies.md#rolling-out-a-blueprint) the blueprint, or [synchronize the Live Copy](creating-live-copies.md#synchronizing-a-live-copy) with the changes.

## Customizing MSM {#customizing-msm}

MSM provides tools so that your implementation can adapt to the exceptional complexities that can exist when sharing content.

* **Custom Rollout Configurations** - [Create a rollout configuration](live-copy-sync-config.md#creating-a-rollout-configuration) when the installed rollout configurations do not meet your requirements. You can use any available rollout trigger and synchronization action.

<!--
* **Custom Synchronization Actions** - [Create a custom synchronization action](/help/sites-developing/extending-msm.md#creating-a-new-synchronization-action) when the installed actions do not meet your specific application requirements. MSM provides a Java API for creating custom synchronization actions.
-->

## Best Practices {#best-practices}

The [MSM Best Practices](best-practices.md) page contains important information regarding your implementation.
