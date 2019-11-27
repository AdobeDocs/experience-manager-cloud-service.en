---
title: Authoring Concepts
seo-title: Authoring Concepts
description: Concepts of authoring in AEM
seo-description: Concepts of authoring in AEM
contentOwner: Chris Bohnert
products: SG_EXPERIENCEMANAGER/6.5/SITES
topic-tags: introduction
content-type: reference
---

# Authoring Concepts {#authoring-concepts}

An AEM installation generally consists of at least two environments:

* Author
* Publish

These interact to enable you to make content available on your website so that your visitors can access it.

The author environment provides the mechanisms for creating, updating, and reviewing this content before actually publishing it:

* An author creates and reviews the content. Content can be of many different types such as pages, assets, publications, etc.
* This content will, at some point, be published to your website.

![Diagram of author, publisher, and dispatchers](/help/sites-cloud/authoring/assets/author-publish.png)

On the author environment the functionality of AEM is made available through AEM's authoring UI. For the publish environment you design the entire look-and-feel of the interface made available to your users.

>[!NOTE]
>
>AEM itself is used to publish the AEM documentation.

## Author Environment {#author-environment}

The author works in what is known as the **author environment**. This provides an easy to use interface (graphical user interface (GUI or UI)) for creating the content. It requires the author to login, using an account that has been assigned the appropriate access rights.

>[!NOTE]
>
>Your account needs the appropriate access rights to create, edit or publish content.

Depending on how your instance and your personal access rights are configured you can perform many tasks on your content, including (amongst others):

* Generating new content or edit existing content on a page
* Using predefined templates to create new content pages
* Creating, editing, and managing your assets and collections
* Moving, copying, and deleting content pages, assets, etc.
* Publishing (or un-publishing) pages, assets, etc.

Additionally, there are administrative tasks that help you manage your content:

* Workflows that control how changes are managed such as enforcing a review before publication
* Projects that coordinate individual tasks

>[!NOTE]
>
>AEM is also [administered](/help/sites-cloud/administering/home.md) from the author environment.

## Publish Environment {#publish-environment}

When ready, your site's content is published to the **publish environment**. Here the website's pages are made available to the intended audience in accordance with the look-and-feel of the designed interface.

>[!NOTE]
>
>Unfortunately there is sometimes an overlap in the terminology used. This can happen with:
>
>* **Publish / Unpublish**
>  These are the primary terms for the actions that make your content publicly available on your publish environment (or not).
>
>* **Activate / Deactivate**
>  These terms are synonymous with publish/un-publish, and are avoided in this documentation, but you may still hear them used by experienced AEM users or developers.
>
>* **Replicate / Replication**
>  These are the technical terms used to indicate the movement of data (e.g. page content, files, code, user comments) from one environment to another. I.e. when publishing AEM replicates the data to the publish instance. Such terminology is usually only used by developers.
>

## Dispatcher {#dispatcher}

To optimize performance for visitors to your website, the **[dispatcher](/help/implementing/dispatcher/dispatcher-cloud.md)** implements load balancing and caching.
