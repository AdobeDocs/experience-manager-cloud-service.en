---
title: Learn Authoring Basics
description: Learn about the concepts and mechanics of authoring content for your Headless CMS using Content Fragments.
---

# Authoring Basics for Headless with AEM {#author-headless-basics}

<!-- screenshots to be added later -->

## The Story so Far {#story-so-far}

At the beginning of the [AEM Headless Content Author Journey](overview.md) the [Introduction](introduction.md) covered the basic concepts and terminology relevant to authoring for headless.

This article builds on these so you understand how to author your own content for your AEM headless project.

## Objective {#objective}

* **Audience**: Beginner
* **Objective**: Introduce the basics of Headless CMS Authoring:
  * Introduction to authoring with AEMaaCS
  * Introduction to Content Fragments

## Basic Handling {#basic-handling}

Before you get to grips with Content Fragments, here is a (very) quick introduction to using AEM....but nothing really replaces the experience of signing in and trying to use the system.

### Author and Publish {#author-preview-publish}

An AEM installation generally consists of at least two environments:

* Author
* Publish

You log into, and use the author environment to generate your content. When ready you then publish your content so that it becomes generally available. For headless this would be to other applications, for web pages this would be to readers on the web.

For more details see the Authoring Concepts.

### Signing In {#signing-in}

As with most systems you will need to login. As an author you will be provided with:

* User (account) name
* Password
* Link to access the login screen

Your account will have been configured with any privileges that you need. If you have any issues, we recommend that you contact your in-house project support team.

### Navigation {#navigation}

The first time you log in a small online tutorial will highlight some of the main features of the user interface.

You can then use the Navigation Panel to access key areas of AEM. For Content Fragments you will be using the **Assets Console**. 

The Navigation Panel can be opened by selecting Adobe icon at the top left, followed by the small compass icon:

![Navigation panel](/help/journey-headless/author/assets/headless-journey-author-navigation-01.png)

>[!NOTE]
>Although Content Fragments are a feature of AEM **Sites**, they are found in the **Assets** console. This is a technical detail that should not affect you, but might be useful to know.

Within the console you can select folders to navigate to your Content Fragment, or the breadcrumbs (in the header) to navigate back up the tree.

![Breadcrumbs](/help/journey-headless/author/assets/headless-journey-author-navigation-02.png)

### Actions, Selecting, Viewing {#actions-selecting-viewing}

The **Assets** console has dedicated **Action Toolbars**, and **Quick Actions** that you can use after selecting a resource (for example, a folder or content fragment).

The Quick Actions are available for a single resource:

![Quick Actions](/help/journey-headless/author/assets/headless-journey-author-navigation-05.png)

The Actions Toolbar provides access to the full range of actions - applicable for the current scenario. The actions available can change; for example, dependent on your location, or whether you have selected multiple resources:

![Action Toolbar](/help/journey-headless/author/assets/headless-journey-author-navigation-06.png)

You can select the format for viewing your resources with the View Selector:

![View Selector](/help/journey-headless/author/assets/headless-journey-author-navigation-03.png)

You can view additional information about items using the Rail Selector. This also gives access to additional actions.

![Left Rail](/help/journey-headless/author/assets/headless-journey-author-navigation-04.png)

## Authoring Content Fragments {#authoring-content-fragments}

### Organizing and Navigating {#organizing-and-navigating}

Unless you have very few Content Fragments you will want to organize them - so that you (and others) can find them again.

You can do this by creating a series of folders within the Assets console. You then navigate through these folders to create, and edit your Content Fragments.

>[!NOTE]
>
>You will probably be given an initial folder where you can create your folders. 
>
>This is as some configuration details must be applied (usually by a Developer or System Administrator) to the root folder. You can read more under Apply the Configuration to your Assets Folder.

### Creating {#creating}

### Editing {#editing}

#### What you don't need to worry about {#what-you-do-not-need-to-worry-about}

OK, this might seem a slightly strange section, but once you open the Content Fragment Editor and start exploring you'll see various options that do not apply for your headless journey. So this is just a quick heads-up on what you can ignore:

* **Content Fragment Models**

  You will see the name of the Content Fragment Model at the top of the editor. This is also a link that takes you to the model editor.
  Content Fragment Models are actually vital to your Content Fragments as they define the structure that you use. HOWEVER, creating and editing them are (usually) the responsibility of another persona, the Content Architect. 

  >[!NOTE]
  >
  >If you want to learn more, you can read the AEM Headless Content Architect Journey.

* **Associated Content**

  This one is quite obvious as it's a tab in the editor.

  Content Fragments have been available in AEM for quite a few versions. Originally they were made available for "traditional" use when authoring pages....and they are still used in this context. This can involve associating assets (for example images) that although not embedded in the fragment, needs to be available to the author when authoring a page.

* **Preview**

  This is another tab in the editor and provides a technical view, primarily intended for developers.

<!-- OK, now we've cleared that up we can start on the interesting part. -->

### Publishing {#publishing}

## What's Next {#whats-next}

Now that you have learned the basics, the next step is to [Learn how about References](references.md). This will introduce and discuss the various references available, and how to create levels of structure with the Fragment References.

## Additional Resources {#additional-resources}

* [Authoring Concepts](/help/sites-cloud/authoring/getting-started/concepts.md)

* [Basic Handling](/help/sites-cloud/authoring/getting-started/basic-handling.md) - this page is primarily based on the **Sites** console, but many/most features are also relevant for authoring **Content Fragments** under the **Assets** console.

  * [Navigation Panel](/help/sites-cloud/authoring/getting-started/basic-handling.md#navigation-panel)

  * [The Header](/help/sites-cloud/authoring/getting-started/basic-handling.md#the-header)
  
  * [Action Toolbar](/help/sites-cloud/authoring/getting-started/basic-handling.md#actions-toolbar)

  * [Quick Actions](/help/sites-cloud/authoring/getting-started/basic-handling.md#quick-actions)
  
  * [Viewing and Selecting Resources](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources)
  
  * [Rail Selector](/help/sites-cloud/authoring/getting-started/basic-handling.md#rail-selector)

* [Working with Content Fragments](/help/assets/content-fragments/content-fragments.md)
 
  * [Managing Content Fragments](/help/assets/content-fragments/content-fragments-managing.md)

    * [Apply the Configuration to your Assets Folder](/help/assets/content-fragments/content-fragments-configuration-browser.md#apply-the-configuration-to-your-assets-folder)
  
    * [Creating a Content Fragment](/help/assets/content-fragments/content-fragments-managing.md#creating-a-content-fragment)
  
    * ...basically everything on this page is relevant, apart from actually creating a Content Fragment Model, and Associated Content.

  * [Variations - Authoring Content Fragments](/help/assets/content-fragments/content-fragments-variations.md)

* AEM Headless Content Architect Journey