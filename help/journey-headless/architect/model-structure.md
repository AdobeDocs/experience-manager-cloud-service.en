---
title: Learn about Creating Content Fragment Models in AEM
description: Learn about the concepts and mechanics of modeling content for your Headless CMS using Content Fragments Models.
exl-id: fdfa79d3-fbed-4467-a898-c1b2678fc0cb
solution: Experience Manager
feature: Headless, Content Fragments,GraphQL API
role: Admin, Architect, Developer
---
# Learn about Creating Content Fragment Models in AEM {#architect-headless-content-fragment-models}

## The Story so Far {#story-so-far}

At the beginning of the [AEM Headless Content Author Journey](overview.md) the [Content Modeling Basics for Headless with AEM](basics.md) covered the basic concepts and terminology relevant to authoring for headless.

This article builds on these principles so that you understand how to create your own Content Fragment Models for your AEM headless project.

## Objective {#objective}

* **Audience**: Beginner
* **Objective**: the concepts and mechanics of modeling content for your Headless CMS using Content Fragments Models.

## Creating Content Fragment Models {#creating-content-fragment-models}

Then the Content Fragments Models can be created and the structure defined.

1. In the Content Fragment Console, select the panel for Content Fragment Models.

1. Navigate to the folder appropriate to your configuration, or subconfiguration.

1. Use **Create** to open the **New Content Fragment Model** dialog.

   ![Title and description](/help/sites-cloud/administering/content-fragments/assets/cf-managing-content-fragment-models-create.png)

1. Complete the details

1. Use **Create** to save the empty model, or **Create and open**.

## Defining Content Fragment Models {#defining-content-fragment-models}

When you first open a new model you see - a large (fairly) blank space in the middle, a long list of **Data Types** at the left, and **Properties** (empty at the start, as they are for the selected field) at the right:

![Empty Model](/help/sites-cloud/administering/content-fragments/assets/cf-cfmodels-empty-model.png)

So - what's to be done?

You can either:

* Drag a data type from the left panel to the required location for a field in the middle panel.
* Select the + icon by a Data Type to add it to the bottom of the field list.
* Select Add in the middle panel and then the required data type from the resulting drop down list to add a field to the bottom of the list.

You are already defining your model!

After you add a data type you are required to define the **Properties** for that field. These properties depend on the type being used. For example:

![Data Properties](/help/sites-cloud/administering/content-fragments/assets/cf-cfmodels-field-properties.png)

### Your Content Authors {#your-content-authors}

Your content authors do not see the actual Data Types and Properties that you have used to create your models. This means that you might have to provide help and information on how they complete specific fields. For basic information you can use the Field Label and Default Value, but more complex cases project specific documentation might need to be considered.

>[!NOTE]
>
>See Additional Resources - Content Fragment Models.

## Managing Content Fragment Models {#managing-content-fragment-models}

<!-- needs more details -->

Managing your Content Fragment Models involves:

* Enabling (or disabling) them - this makes them available for authors when creating Content Fragments.
* Deleting - deletion is always needed, but you need to be aware of deleting a model that is already used for Content Fragments; in particular fragments that are already published.

## Publishing {#publishing}

<!-- needs more details -->

Content fragment models need to be published when/before any dependent content fragments are published.

>[!NOTE]
>
>If an author tries to publish a content fragment for which the model has not yet been published, a selection list indicates this, and the model is published with the fragment.

As soon as a model is published it is *locked* into a READ-ONLY mode on author. This aims to prevent changes that would result in errors to existing GraphQL schemas and queries, especially on the publish environment. It is indicated in the console by **Locked**. 

When the model is **Locked** (in READ-ONLY mode), you can see the contents and structure of models but you cannot edit them directly; though you can manage **Locked** models from either the console, or the model editor.

## What's Next {#whats-next}

Now that you have learned the basics, the next step is to start creating your own Content Fragment Models.

## Additional Resources {#additional-resources}

* [Authoring Concepts](/help/sites-cloud/authoring/author-publish.md)

* [Basic Handling](/help/sites-cloud/authoring/basic-handling.md) - this page is primarily based on the **Sites** console, but many/most features are also relevant for navigating to, and taking action on, **Content Fragment Models** under the **General** console.

* [Working with Content Fragments](/help/sites-cloud/administering/content-fragments/overview.md)
 
  * [Content Fragment Models](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md)

    * [Defining your Content Fragment Model](/help/sites-cloud/administering/content-fragments/content-fragment-models.md)

    * [Enabling or Disabling a Content Fragment Model](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md#enabling-disabling-a-content-fragment-model)

    * [Allowing Content Fragment Models on your Assets Folder](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md#allowing-content-fragment-models-assets-folder)

    * [Deleting a Content Fragment Model](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md#deleting-a-content-fragment-model)

    * [Publishing a Content Fragment Model](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md#publishing-a-content-fragment-model)

    * [Unpublishing a Content Fragment Model](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md#unpublishing-a-content-fragment-model)

    * [Locked Content Fragment Models](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md#locked-content-fragment-models)

* Getting Started Guides
  
  * [Creating Content Fragment Models Headless Setup](/help/headless/setup/create-content-model.md)
