---
title: Create the Content Structure for Your App
description: Learn how to create the structure which serves as the foundation for all of your headless content using AEM's Content Fragment models.
hidefromtoc: yes
index: no
---

# Create the Content Structure for Your App {#content-structure}

Learn how to create the structure which serves as the foundation for all of your headless content using AEM's Content Fragment models by following the in-product learning module. This document serves as a supplement of the interactive tour, covering the same steps and linking to additional resources where appropriate.

Content Fragments allow you to design, create, curate, and publish page-independent content. Using them you can  prepare content that is ready for use in multiple locations and over multiple channels, ideal for headless delivery. Content Fragment models are used to define the structure of this content and are the first thing you need to create in order to manage your headless content.

To help you understand how this is done, this module of AEM Trials takes you through the process with a quick, interactive tour first creating the model and then adding its structure. 

## The Content Fragment Model Console {#content-fragment-model-console}

You start on the Content Fragment models console. The Content Fragment console can be thought of as your library of models. You use the console to create new models and manage exiting models. Your console starts empty, so let's create a new one!

![The Content Fragment model console](assets/content-structure/content-fragment-model-console.png)

If you wish to navigate to the Content Fragment model yourself outside of the in-app guidance, it is found using the Adobe icon at the top-left of the page. This opens the global navigation of AEM. From here, you choose the **Tools** tab and then **General** -&gt; **Content Fragment Models**.

>[!TIP]
>
>If you would like to know more about navigation in AEM, see the [Additional Resources section](#additional-resources) of this document for more information on AEM basic handling.
 
## Create a Model {#create-model}

Once you are in the Content Fragment model console, you can create a new model to represent your own headless content.

1. In the Content Fragment model console, click the **Create** button at the top-right of the screen to begin creating a Content Fragment model.

1. The Create Model wizard starts, which guides you through creating a Content Fragment model. 

   ![Content Fragment model wizard](assets/content-structure/model-wizard.png)

   Provide the mandatory information.

   * **Model Title** - This is a brief description of the model, and usually indicates its purpose.
   * **Enable model** - This option is checked by default and must be checked to be able to create Content Fragments later based on this model.

   You can also choose to add a longer **Description** to the model as well as **Tags** to categorize it and differentiate it for your users later within the Content Fragment model console.

   >[!TIP]
   >
   >If you are interested in how tags can organize your content, see the [Additional Resources section](#additional-resources) of this document for more information on tagging in AEM.

1. Once the mandatory fields are populated, you click **Create** at the top-left to create the model. 

1. The **Success** dialog confirms that the model was created.

   ![Success dialog for creating a new Content Fragment model](assets/content-structure/success.png)

1. Before you can use the model, you also need to define the structure of its data. Click **Open** in the dialog to open it and continue defining the model.

## Add Fields to the Model {#configure-model}

The Content Fragment model is essentially a schema for your Content Fragments. I.e. it defines what fields/data types that the model contains. 

![The Content Fragment model Editor](assets/content-structure/model-editor.png)

Using the Content Fragment model editor, you can define fields for the Content Fragment model using a drag-and-drop interface.

1. Drag a field from the **Data Types** panel at the right of the screen and drop it onto your Content Fragment model. There are multiple data types to choose from such as a single-line text, multi-line text, number, and references to other fragments.

   ![Add a data type](assets/content-structure/drop-fields.png)

   >[!TIP]
   >
   >If you would like more information about the data types available to you, see the [Additional Resources section](#additional-resources) of this document for the detailed Content Fragment models documentation.

1. Once a data type is placed, the **Data Types** column automatically changed to the **Properties** tab, where you can define the details of the data type you just placed.

   ![The Properties tab for the data field](assets/content-structure/data-type-properties.png)

    Properties of the model may include the name of the field, the type of field, the length of the field, if it is mandatory, etc.

1. Use the **Properties** tab of the selected data type to define properties such as default value, maximum length, if it a required field, etc.

   >[!TIP]
   >
   >If you would like more information about the properties available to you, see the [Additional Resources section](#additional-resources) of this document for the detailed Content Fragment models documentation.

1. Once you have added all of the fields necessary for the Content Fragment model, click **Save** at the top-right of the window.

1. This saves the model and returns you to the Content Fragment model Console where you can add more models are necessary.

![Module complete](assets/content-structure/content-fragment-model-console-populated.png)

## You've Learned to Create a Content Fragment Model {#conclusion}

In this module, you learned how to create a Content Fragment model to represent the structure of your headless data. First you created the model and then populated it with data types and their related properties, thereby defining a schema for your headless content.

## Next Steps {#next-steps}

Now that you have your own Content Fragment model, continue on to the module [Create New Content](create-content.md) to use your new Content Fragment model to create headless content.

## Additional Resources {#additional-resources}

For more information about Content Fragments and AEM, consider reviewing this additional documentation.

* [Content Fragment Models](/help/assets/content-fragments/content-fragments-models.md) - Complete documentation on Content Fragment models
* [Content Fragments](/help/assets/content-fragments/content-fragments.md) - Complete documentation on Content Fragments
* [Basic Handling](/help/sites-cloud/authoring/getting-started/basic-handling.md) - Documentation on how to navigate and use AEM for new users
* [Using Tags](/help/sites-cloud/authoring/features/tags.md) - Documentation on how to use tags in AEM to organize content
