---
title: Learn about using references in Content Fragments
description: Learn about using references in Content Fragments, for content, other fragments and other assets (media). Introduce the necessity for, and the mechanics of, nested fragments for Headless CMS Authoring.
exl-id: a65e8a5a-954b-4307-8027-ca8bac5f4261
solution: Experience Manager
feature: Headless, Content Fragments,GraphQL API
role: Admin, Architect, Developer
---
# Learn about using references in Content Fragments {#author-headless-references}

## The Story so Far {#story-so-far}

At the beginning of the [AEM Headless Content Author Journey](overview.md) the [Introduction](introduction.md) covered the basic concepts and terminology relevant to authoring for headless.

You have learned the basics of Headless CMS Authoring, with an introduction to authoring with AEMaaCS and in particular, authoring Content Fragments.

This article builds on these so you understand how to use references to author your own content for your AEM headless project.

## Objective {#objective}

* **Audience**: Advanced
* **Objective**: Introduce the use of references for Headless CMS Authoring. What sorts of references are available, and what are their purposes:

  * Content References
  * Asset/Media References
  * Fragment References
  * Improvised references from within a text block

## What are references {#what-are-references}

References are simply a mechanism for connecting your resources, be it other content, assets (as in images), or other fragments. Although very similar, there are some differences.

Some references have dedicated data-types (for example, Content References and Fragment References), whereas others are simply added as a reference within a text block (asset references and improvised references).

![Content Fragments - References](/help/sites-cloud/administering/content-fragments/assets/cf-authoring-overview.png)

## Content References {#content-references}

Content References do just that - they allow you to reference any other content. This opens a browser that lets you select the content item.

## Asset/Media References {#assets-media-references}

Assets (for example, images or media) can be referenced within a Text block by using the **Insert asset** option. This opens a browser that lets you select the asset.

![Content Fragments - Insert Asset](/help/journey-headless/author/assets/headless-journey-author-references-02.png)

## Fragment References {#fragment-references}

Again Fragment References do just that - they allow you to reference another fragment. Why this is significant needs a bit more explanation.

For example, you might have the following Content Fragment Models defined:

* City
* Company
* Person
* Awards

Seems pretty straightforward, but a Company has both a CEO and Employees....and these are all people, each defined as a Person.

And a Person can have an Award (or maybe two).

* My Company - Company
  * CEO - Person
  * Employee(s) - Person
    * Personal Award(s) - Award

And that's just for starters. Depending on the complexity, an Award could be Company-specific, or a Company could have its main office in a specific City.

Representing these interrelationships can be achieved with Fragment References, as they are understood by both you (the author) and the headless applications.

As an author you are not responsible for defining these relationships (that is done by the Content Architect when creating the Content Fragment Model), but you need to know how to recognize and edit the references.

<!--
![Content Modeling with Content Fragments](/help/journey-headless/developer/assets/headless-modeling-01.png "Content Modeling with Content Fragments")
--> 

### How to author nested fragments {#author-nested-fragment}

Authoring Fragment References is fairly straightforward (though usually the field will not be labelled as **Fragment Reference**). You can either type in the reference directly, or (more likely) select the folder icon to open a browser that lets you navigate and select the fragment you need. 

![Content Fragments - References](/help/journey-headless/author/assets/headless-journey-author-references-03.png)

The definition of the Content Fragment Model controls:

* whether you can select to add multiple references
* the model types of Content Fragments that you can select; the Content Fragment Model defines the fragment models allowed for the reference, so AEM only presents fragments based on those models.

### How to navigate nested fragments {#navigate-nested-fragment}

Using the **Structure Tree** tab of the Content Fragment Editor you can navigate through the fragments referenced by your fragment, and then through any references they may contain. Selecting a reference opens that fragment for editing.

![Content Fragment Structure Tree](/help/sites-cloud/administering/content-fragments/assets/cf-authoring-structure-tree.png)

## Ad Hoc References {#adhoc-references}

Improvised references can be added as a simple link within a block of text:

![Content Fragments - Ad Hoc References](/help/journey-headless/author/assets/headless-journey-author-references-04.png)

## What's Next {#whats-next}

Now that you have learned about references and structure in Content Fragments, the next step is to [Learn how about Metadata and Tagging](metadata-tagging.md). This will introduce and discuss how you can define metadata and tags for your Content Fragments.

## Additional Resources {#additional-resources}

* [Working with Content Fragments](/help/sites-cloud/administering/content-fragments/overview.md)
 
  * [Managing Content Fragments](/help/sites-cloud/administering/content-fragments/managing.md)

    * [Apply the Configuration to your Assets Folder](/help/sites-cloud/administering/content-fragments/setup.md#apply-the-configuration-to-your-folder)
  
    * [Creating a Content Fragment](/help/sites-cloud/administering/content-fragments/managing.md#creating-a-content-fragment)
  
  * [Authoring Content Fragments](/help/sites-cloud/administering/content-fragments/authoring.md)

  * [Content Fragment Models](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md)

    * [Content Fragment Models - Data Types](/help/sites-cloud/administering/content-fragments/content-fragment-models.md#data-types)
  
    * [Content Fragment Models - Properties](/help/sites-cloud/administering/content-fragments/content-fragment-models.md#properties)

* Getting Started Guides
  * [Creating an Assets Folder - Headless Setup](/help/headless/setup/create-assets-folder.md)

* AEM Headless Content Architect Journey

* AEM Headless Translation Journey
