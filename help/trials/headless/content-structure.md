---
title: Create the Content Structure for Your App
description: Learn how to create the structure which serves as the foundation for all of your headless content using AEM's Content Fragment models.
hidefromtoc: yes
index: no
exl-id: ace9b9f3-8bc6-4a36-a51c-ff60cdd339ce
---

# Create the Content Structure for Your App {#content-structure}

Content Fragments allow you to design, create, curate, and publish page-independent content. Using them you can  prepare content that is ready for use in multiple locations and over multiple channels, ideal for headless delivery. Content Fragment models are used to define the structure of this content and are the first thing you need to create in order to manage your headless content.

To help you understand how this is done, this module of AEM Trials takes you through the process with a quick, interactive tour first creating the model and then adding its structure.

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_overview"
>title="Create the content structure for your app"
>abstract="As you follow our series of interactive guides you'll learn to create the structure (also known as the content fragment model) which serves as the foundation for all of your headless content."

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_overview_guide"
>title="Launch the model editor"
>abstract="Let's explore how to create a reusable schema, called a Content Fragment model, for your content in Adobe Experience Manager as a Cloud Service. What the video to understand why this is an important step. Launch this module in a new tab by clicking the button below and then follow this guide."
>additional-url="https://video.tv.adobe.com/v/3413261" text="Content structure intro video"

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_overview_guide_footer"
>title="Launch the model editor"
>abstract="Congratulations! By creating a Content Fragment model, you took the first step to delivering omni-channel content in a scaled and standard way."

## Create a Model {#create-model}

Clicking the **Launch the model editor** button above opens the Content Fragment models console in a new tab. Think of it as your library of models, where you create new models and manage exiting models. Your console starts empty, so let's create a new model!

![The Content Fragment model console](assets/content-structure/content-fragment-model-console.png)

1. In the Content Fragment model console, click the **Create** button at the top-right of the screen to begin creating a Content Fragment model.

1. The Create Model wizard starts, which guides you through creating a Content Fragment model. 

   ![Content Fragment model wizard](assets/content-structure/model-wizard.png)

   Provide the mandatory information.

   * **Model Title** - This is a brief description of the model and usually indicates its purpose.
   * **Enable model** - This option is checked by default and must be checked to be able to create Content Fragments based on this model.

1. Once the mandatory fields are populated, click **Create** at the top-left to create the model. 

1. The **Success** dialog confirms that the model was created.

   ![Success dialog for creating a new Content Fragment model](assets/content-structure/success.png)

## Add Fields to the Model {#configure-model}

Before you can use the model, you need to define the structure of its data. Click **Open** in the **Success** dialog to open your new model to define its fields

The Content Fragment model is essentially a schema for your Content Fragments. I.e. it defines what fields/data types that the model contains. 

![The Content Fragment model Editor](assets/content-structure/model-editor.png)

1. Drag a field from the **Data Types** panel at the right of the screen and drop it onto your Content Fragment model. 

   ![Add a data type](assets/content-structure/drop-fields.png)

1. Once a data type is placed, the **Data Types** column automatically changed to the **Properties** tab, where you can define the details of the data type you just placed.

   ![The Properties tab for the data field](assets/content-structure/data-type-properties.png)

1. Use the **Properties** tab of the selected data type to define properties such as default value, maximum length, if it is a required field, etc.

1. Once you have added all of the fields necessary for the Content Fragment model, click **Save** at the top-right of the window.

The model is saved and you return to the Content Fragment model Console where you can add more models are necessary.

![Module complete](assets/content-structure/content-fragment-model-console-populated.png)

## You've Learned to Create a Content Fragment Model. {#conclusion}

Congratulations! You learned how to create a Content Fragment model to represent the structure of your headless data and took the first step to delivering omni-channel content in a scaled and standard way.

## Additional Resources {#additional-resources}

For more information about Content Fragments and AEM, consider reviewing this additional documentation.

* [Basic Handling](/help/sites-cloud/authoring/getting-started/basic-handling.md) - Documentation on how to navigate and use AEM for new users
* [Using Tags](/help/sites-cloud/authoring/features/tags.md) - Documentation on how to use tags in AEM to organize content
* [Content Fragments](/help/assets/content-fragments/content-fragments.md) -  Overview of Content Fragments and links to complete documentation on Content Fragments
* [Content Fragment Models](/help/assets/content-fragments/content-fragments-models.md) - Complete documentation on Content Fragment models
* [Content Fragment Models - Data Types](/help/assets/content-fragments/content-fragments-models.md#data-types) - Details on the various data types available for Content Fragment models
* [Content Fragment Models - Properties](/help/assets/content-fragments/content-fragments-models.md#data-types) - Details on the various properties available for Content Fragment models data types
