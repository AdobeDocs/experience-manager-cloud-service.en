---
title: Learn Authoring Basics
description: Learn about the concepts and mechanics of authoring content for your Headless CMS using Content Fragments.
---

# Authoring Basics for Headless with AEM {#author-headless-basics}

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

You can do this by creating a series of folders within **Files** section of the Assets console. Select the **Create** option (top right), followed by **Create Folder**:

![Create Folder option](/help/journey-headless/author/assets/headless-journey-author-folder-01.png)

A dialog will open where you can enter the details, then confirm with **Create**:

![Create Folder dialog](/help/journey-headless/author/assets/headless-journey-author-folder-02.png)

You then navigate through these folders to create, and edit your Content Fragments.

Just in case....xou will probably be given an initial folder where you can create your folders. This is as some configuration details must be applied (usually by a Developer or System Administrator) to the root folder. This probably won't interest you, but if necessary you can check the **Configuration** in the **Cloud Services** of the folder **Properties**:

![Create Folder dialog](/help/journey-headless/author/assets/headless-journey-author-folder-03.png)

>[!NOTE]
>
>You can read more under Apply the Configuration to your Assets Folder. 

### Creating {#creating}

Creating a Content Fragment is very similar - you just use the **Content Fragment** option instead:

![Create Content Fragment option](/help/journey-headless/author/assets/headless-journey-author-content-fragment-01.png)

This time a wizard opens. The first step is to select the Content Fragment Model that your fragment will be based on:

![Create Content Fragment - select Model](/help/journey-headless/author/assets/headless-journey-author-content-fragment-02.png)

After continuing with **Next** you can supply the details for your fragment:

![Create Content Fragment - provide Name](/help/journey-headless/author/assets/headless-journey-author-content-fragment-03.png)

Confirm with **Create** and you can then **Open** your fragment in the editor.

### Editing {#editing}

When the editor first opens you'll see:

* A list of icons at the left side - this gives you access to various areas of functionality. The editor opens in the **Variations** tab, this is where most of the editing happens. You might also be interested in the **Annotations** and **Metadata** tabs.

* A header with information about the fragment, and access to various actions.

* The main editing area - this depends on the model used to create your fragment.

As examples:

* A fragment that only requires short pieces of information:
  
  ![Content Fragment Editor - My Fragment](/help/journey-headless/author/assets/headless-journey-author-content-fragment-04.png)

* A fragment that allows you to write a long section of text. Here there are additional options for managing, and formaatting the text. You can even open the text in a full screen editor (using the small screen-like icon at the right)
  
  ![Content Fragment Editor - Alaska Spirits](/help/journey-headless/author/assets/headless-journey-author-content-fragment-05.png)

Confirm your updates with either **Save** or **Save & close**.

>[!NOTE]
>
>For more details you can read Variations - Authoring Content Fragments.

#### What you don't need to worry about {#what-you-do-not-need-to-worry-about}

OK, this might seem a slightly strange section, but once you open the Content Fragment Editor and start exploring you'll see various options that do not apply for your headless journey. So this is just a quick heads-up on what you can ignore:

* **Content Fragment Models**

  You will see the name of the Content Fragment Model at the top of the editor - directly under the fragment name. This is also a link that takes you to the model editor.
  Content Fragment Models are actually vital to your Content Fragments as they define the structure that you use. HOWEVER, creating and editing them are (usually) the responsibility of another persona, the Content Architect. 

  >[!NOTE]
  >
  >If you want to learn more, you can read the AEM Headless Content Architect Journey.

* **Associated Content**

  This one is quite obvious as it's a tab in the editor.

  Content Fragments have been available in AEM for quite a few versions. Originally they were made available for "traditional" use when authoring pages....and they are still used in this context. This can involve associating assets (for example images) that although not embedded in the fragment, needs to be available to the author when authoring a page.

* **Preview**

  This is another tab in the editor and provides a technical view, primarily intended for developers.

* **Update page references**

  This action is available from the **...** (ellipses) drop down. It is not interesting for headless authors as it relates to page authoring.

### Publishing {#publishing}

<!-- needs more details -->

Once you have completed your fragment you can **Publish** it so that it is available to the headless applications.

The publish actions are available in the editor (or from the toolbar of the **Assets** console):

![Content Fragment Editor - My Fragment](/help/journey-headless/author/assets/headless-journey-author-content-fragment-06.png)

## What's Next {#whats-next}

Now that you have learned the basics, the next step is to [Learn how about References](references.md). This will introduce and discuss the various references available, and how to create levels of structure with the Fragment References - a key part of authoring for headless.

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

* Getting Started Guides
  * [Creating an Assets Folder Headless Quick Start Guide](help/implementing/developing/headless/getting-started/create-assets-folder.md)

* AEM Headless Content Architect Journey