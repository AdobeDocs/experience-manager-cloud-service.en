---
title: Learn Authoring Basics
description: Learn about the concepts and mechanics of authoring content for your Headless CMS using Content Fragments.
exl-id: 3eca973f-b210-41bb-98da-ecbd2bae9803
solution: Experience Manager
feature: Headless, Content Fragments,GraphQL API
role: Admin, Architect, Developer
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

### Author, Preview, and Publish {#author-preview-publish}

An AEM installation generally consists of three environments:

* Author
* Publish
* Preview

You log into, and use the author environment to generate your content. When ready you then publish your content so that it becomes generally available. For headless this would be to other applications, for web pages this would be to readers on the web.

For more details see the Authoring Concepts.

From the **Content Fragments** console, you can also publish to the **Preview Service**, for testing and previewing, prior to Publish. See Publishing and Previewing a Fragment.

### Signing In {#signing-in}

As with most systems, you need to log on. As an author you are provided with:

* User (account) name
* Password
* Link to access the login screen

Your account will have been configured with any privileges that you need. If you have any issues, Adobe recommends that you contact your in-house project support team.

### Navigation {#navigation}

The first time you log in a small online tutorial will highlight some of the main features of the user interface.

You can then use the Navigation Panel to access key areas of AEM. For Content Fragments, you use the **Content Fragments** console (for some actions you will also use the **Assets** console). 

The Navigation Panel can be opened by selecting the Adobe icon at the top left, followed by the small compass icon.

<!--
The Navigation Panel can be opened by selecting Adobe icon at the top left, followed by the small compass icon:

![Navigation panel](/help/journey-headless/author/assets/headless-journey-author-navigation-01.png)
--> 

>[!NOTE]
>Although Content Fragments are a feature of AEM **Sites**, they are saved as **Assets**. This is a technical detail that should not affect you, but might be useful to know.

Within the console you can select folders in the left panel to navigate to your Content Fragment. You can also filter and/or search.

![Content Fragments console](/help/sites-cloud/administering/content-fragments/assets/cf-managing-console-filter.png)

### Actions, Selecting, Viewing {#actions-selecting-viewing}

In the **Content Fragments** console a range of actions are available for your content fragments from the toolbar:

<!-- ![Console actions](assets/cfm-managing-cf-console-01.png) -->

* **Open in Assets**
* **Create**
* The **Referenced By** column also provides a direct link to show all parent references of that fragment; including referencing Content Fragments, Experience Fragments and pages.
* Hovering over the folder name will show the JCR path.

After selection of your fragment all appropriate actions are available:

<!-- ![Console actions - fragment selected](assets/cfm-managing-cf-console-selected-01.png) -->

* **Open**
* **Publish** (and **Unpublish**)
* **Copy**
* **Move**
* **Rename**
* **Delete**

>[!NOTE]
>
>Actions such as Publish, Unpublish, Delete, Move, Rename, Copy, trigger an asynchronous job. The progress of that job can be monitored via the AEM Async Jobs UI.

<!--
The **Assets** console has dedicated **Action Toolbars**, and **Quick Actions** that you can use after selecting a resource (for example, a folder or content fragment).

The Quick Actions are available for a single resource, see **Basel** in the example below:

![Quick Actions](/help/journey-headless/author/assets/headless-journey-author-navigation-05.png)

The Actions Toolbar provides access to the full range of actions - applicable for the current scenario. The actions available can change; for example, dependent on your location, or whether you have selected multiple resources:

![Action Toolbar](/help/journey-headless/author/assets/headless-journey-author-navigation-06.png)

You can select the format for viewing your resources with the View Selector:

![View Selector](/help/journey-headless/author/assets/headless-journey-author-navigation-03.png)

You can view additional information about items using the Rail Selector. This also gives access to additional actions.

![Left Rail](/help/journey-headless/author/assets/headless-journey-author-navigation-04.png)
--> 

## Authoring Content Fragments {#authoring-content-fragments}

So, that was a very quick introduction to the AEM User Interface (UI), but hopefully you have had a chance to try it out. Now we get down to your real interest - Content Fragments for Headless.

We'll have to go through things from start to finish, but your instance might already have folders and/or fragments created, and these might be in different locations. The principles are the same.

### Organizing and Navigating {#organizing-and-navigating}

Unless you have very few Content Fragments you will want to organize them - so that you (and others) can find them again.

#### Creating a Folder {#creating-folder}

You can do this by creating a series of folders within **Files** section of the **Assets** console. Select the **Create** option (top right), followed by **Folder**:

![Create Folder option](/help/journey-headless/author/assets/headless-journey-author-folder-01.png)

A dialog opens where you can enter the details, then confirm with **Create**:

![Create Folder dialog](/help/journey-headless/author/assets/headless-journey-author-folder-02.png)

#### Using Paths and Tags to limit Content Fragment Models available in the Folder {#tags-paths-for-models-in-folder}

This section is slightly more advanced. You do not really need it if you are just starting out and trying things, but it is *very* useful when you have many fragments. So it is good to know about - even if you do not use it quite yet.

Your Content Architect will have created all the Content Fragment Models required for your current project, and maybe some other projects too. To help keep things simple for yourself, and other authors, you can limit the list of models available for a specific folder.

After creating your folder you can open the folder **Properties**. Here there are various tabs with information, and configuration details, about the folder. In particular for Content Fragments, you can use the **Policies** tab to define specific paths and/or tags for this folder. This limits the Content Fragment Models available for use in the folder as it means that Content Fragment Models must meet these requirements before they can be used to generate fragments in this folder.

![Create Folder Properties - Policies](/help/journey-headless/author/assets/headless-journey-author-folder-04.png)

>[!NOTE]
>
>You can read further details under Content Fragment Models - Allowing Content Fragment Models on your Assets Folder.

You then navigate through these folders to create, and edit your Content Fragments.

#### Just in case - Folder Cloud Services Configuration {#cloud-services-folder}

Just in case...

You will probably be given an initial folder where you can create your folders. This is as some configuration details must be applied (usually by a Developer or System Administrator) to the root folder. This probably won't interest you, but if necessary you can check the **Configuration** in the **Cloud Services** of the folder **Properties**:

![Create Folder Properties - Configuration](/help/journey-headless/author/assets/headless-journey-author-folder-03.png)

>[!NOTE]
>
>You can read more under Apply the Configuration to your Assets Folder. 

### Creating a Content Fragment {#creating-fragment}

In the **Content Fragments** console you can use **Create** to open the **New Content Fragment** dialog:

![Content Fragments console - Creating a new fragment](/help/sites-cloud/administering/content-fragments/assets/cfc-console-create.png)

Specify the:

* **Location**
* **Content Fragment model**
* **Title**
* **Name**
* **Description**

Then confirm with either **Create** or **Create and open**.

### Editing a Fragment {#editing-fragment}

You can open a fragment immediately after creating it, or by selecting it from the Content Fragments console (also from the Assets console).

>[!NOTE]
>
>Content Fragments are a Sites feature, but are stored as **Assets**. 
>
>There are two editors for authoring Content Fragments. 
>
>* The new editor, primarily accessed from the **Content Fragments** console.
>* The original editor, primarily accessed from the **Assets** console. 

When the editor first opens you see:

* top toolbar: for key information, and actions
  * a link to the Content Fragment Console (Home icon)
  * information about the model, and folder
  * links to Preview; if the Default Preview URL Pattern is configured for the model
  * Publish, and Unpublish actions
  * an option to show all **Parent References** (link icon)
  * the fragment **Status**, and last saved information
  * a toggle to switch to the original (Assets-based) editor
* left panel: shows the **Variations** for the Content Fragment, and its **Fields**:
  * these links can be used to navigate the Content Fragment structure
* right panel: presents tabs showing the properties (metadata) and tags, information about the version history, and information related to any language copies
  * in the **Properties** tab you can update the **Title** and **Description** for the fragment, or **Variation**
* central panel: shows the actual fields, and content, of the selected variation
  * allows you to edit the content
  * if **Tab Placeholder** fields are defined within the model they are shown here, and can be used for navigating

As example, a fragment can:

* Require multiple pieces of information, some with a specific type. For headless content, references are key (you learn about these later in your journey).

* Allow you to write a long section of text. Here there are additional options for managing, and formatting the text. You can even open the individual text fields in a full screen editor (using the small screen-like icon at the right)
  
![Content Fragment Editor - Alaska Spirits](/help/sites-cloud/administering/content-fragments/assets/cf-authoring-overview.png)

>[!NOTE]
>
>Project specific documentation might be required to help authors with details of how to successfully complete some fields. 
>
>See Content Fragments Models - Data Types and Properties for generic details.

Confirm your updates with either **Save** or **Save & close**.

>[!NOTE]
>
>For more details you can read Variations - Authoring Content Fragments.

#### What you (probably) do not need to worry about {#what-you-probably-do-not-need-to-worry-about}

OK, this might seem a slightly strange section, but as soon as you open the Content Fragment Editor and start exploring you can see various options that (probably) do not apply for your headless journey as a Content Author. So this is just a quick heads-up on what you should be able ignore in the headless context:

* **Content Fragment Models**

  You can see the name of the Content Fragment Model in the right panel of the editor. This is also a link that takes you to the model editor.
  Content Fragment Models are actually vital to your Content Fragments as they define the structure that you use. However, creating and editing them is (usually) the responsibility of another persona, the Content Architect. 

  >[!NOTE]
  >
  >If you want to learn more, you can read the AEM Headless Content Architect Journey.

### Publishing {#publishing}

<!-- needs more details -->

Once you have completed your fragment you can **Publish** it so that it is available to the headless applications.

The publish actions are available in the editor:

![Content Fragment Editor - My Fragment](/help/journey-headless/author/assets/headless-journey-author-content-fragment-06.png)

>[!NOTE]
>
>You can also publish your fragment from either the **Assets** or **Content Fragments** console.

## What's Next {#whats-next}

Now that you have learned the basics, the next step is to [Learn how about References](references.md). This will introduce and discuss the various references available, and how to create levels of structure with the Fragment References - a key part of authoring for headless.

## Additional Resources {#additional-resources}

* [Authoring Concepts](/help/sites-cloud/authoring/author-publish.md)

* [Basic Handling](/help/sites-cloud/authoring/basic-handling.md) - this page is primarily based on the **Sites** console, but many/most features are also relevant for authoring **Content Fragments** under the **Assets** console.

  * [Navigation Panel](/help/sites-cloud/authoring/basic-handling.md#navigation-panel)

  * [The Header](/help/sites-cloud/authoring/basic-handling.md#the-header)
  
  * [Action Toolbar](/help/sites-cloud/authoring/basic-handling.md#actions-toolbar)

  * [Quick Actions](/help/sites-cloud/authoring/basic-handling.md#quick-actions)
  
  * [Viewing and Selecting Resources](/help/sites-cloud/authoring/basic-handling.md#viewing-and-selecting-resources)
  
  * [Rail Selector](/help/sites-cloud/authoring/basic-handling.md#rail-selector)

* [Working with Content Fragments](/help/sites-cloud/administering/content-fragments/overview.md)
 
  * [Managing Content Fragments](/help/sites-cloud/administering/content-fragments/managing.md)

  * [Apply the Configuration to your Assets Folder](/help/sites-cloud/administering/content-fragments/setup.md#apply-the-configuration-to-your-folder)
  
  * [Creating a Content Fragment](/help/sites-cloud/administering/content-fragments/managing.md#creating-a-content-fragment)
  
  * [Authoring Content Fragments](/help/sites-cloud/administering/content-fragments/authoring.md)

  * Publishing

    * From the editor, or **Assets** console

      * [Quick Publish](/help/assets/manage-publication.md#quick-publish)

      * [Manage Publication](/help/assets/manage-publication.md#manage-publication) 

    * From the **Content Fragments** Console

      * [Publishing and Previewing a Content Fragment](/help/sites-cloud/administering/content-fragments/managing.md#publishing-and-previewing-a-fragment)

  * [Content Fragment Models](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md)

    * [Content Fragment Models - Data Types](/help/sites-cloud/administering/content-fragments/content-fragment-models.md#data-types)
  
    * [Content Fragment Models - Properties](/help/sites-cloud/administering/content-fragments/content-fragment-models.md#properties)

    * [Content Fragment Models - Allowing Content Fragment Models on your Assets Folder](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md#allowing-content-fragment-models-assets-folder)

* [Content Fragments - original editor, from the Assets Console](/help/assets/content-fragments/content-fragments-variations.md)

* Getting Started Guides
  * [Creating an Assets Folder Headless Setup](/help/headless/setup/create-assets-folder.md)

* AEM Headless Content Architect Journey

* AEM Headless Translation Journey
