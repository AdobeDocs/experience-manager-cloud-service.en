---
title: Authoring Concepts
description: Learn the concepts of authoring in AEM, using the author, preview and publish environments.
exl-id: ee9e4952-e075-4398-b31f-d7886153efff
---

# Authoring Concepts {#authoring-concepts}

An AEM installation generally consists of at least two environments:

* Author
* Publish

These environments interact to let you make content available on your website so that your visitors can access it.

The author environment provides the mechanisms for creating, updating, and reviewing this content before actually publishing it:

* An author creates and reviews the content. Content can be of many different types, including pages, assets, and publications.
* This content will, at some point, be published to your website.

![Diagram of author, publisher, and dispatchers](/help/sites-cloud/authoring/assets/author-publish.png)

On the author environment, the functionality of AEM is made available through AEM's authoring user interface. For the publish environment, you design the entire look-and-feel of the interface made available to your users.

{{edge-delivery-authoring}}

## Author Environment {#author-environment}

The author works in what is known as the **author environment**. This environment provides an easy to use interface (graphical user interface (GUI or UI)) for creating the content. It requires the author to log on, using an account that is assigned the appropriate access rights.

>[!NOTE]
>
>Your account needs the appropriate access rights to create, edit, or publish content.

Depending on how your instance and your personal access rights are configured you can perform many tasks on your content, including (among others):

* Generating new content or edit existing content on a page
* Using predefined templates to create content pages
* Creating, editing, and managing your assets and collections
* Moving, copying, and deleting content pages, and assets.
* Publishing (or unpublishing) pages, and assets.

Also, there are administrative tasks that help you manage your content:

* Workflows that control how changes are managed such as enforcing a review before publication
* Projects that coordinate individual tasks

>[!NOTE]
>
>AEM is also administered from the author environment.

## Previewing Content {#previewing-content}

AEM also offers a Sites preview service that lets developers and content authors preview a website's final experience before it reaches the publish environment and is available publicly.

See [Previewing Content](/help/sites-cloud/authoring/fundamentals/previewing-content.md) for further details.

## Publish Environment {#publish-environment}

When ready, your site's content is published to the **publish environment**. Here the website's pages are made available to the intended audience in accordance with the look-and-feel of the designed interface.

For more information about publishing and unpublishing pages, see the document [Publishing Pages](/help/sites-cloud/authoring/fundamentals/publishing-pages.md).

## Dispatcher {#dispatcher}

To optimize performance for visitors to your website, the **[Dispatcher](/help/implementing/dispatcher/overview.md)** implements load balancing and caching.
