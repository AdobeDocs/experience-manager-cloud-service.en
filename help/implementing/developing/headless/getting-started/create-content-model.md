---
title: Creating Content Fragment Models
description: Content Fragment Models define the structure of the content you will create and serve using AEM's headless capabilities.
---

# Creating Content Fragment Models {#creating-content-fragment-models}

Content Fragment Models define the structure of the content you will create and serve using AEM's headless capabilities.

## What are Content Fragment Models? {#what-are-content-fragment-models}

[Now that you have created a configuration,](create-configuration.md) you can use it to create Content Fragment Models.

Content Fragment Models define the structure of the data and content that you will create and manage in AEM. They serve as a kind of scaffolding for your content. When choosing to create content, your authors will select from the Content Fragment Models you define, which guides them in creating content.

## How to Create a Content Fragment Model {#how-to-create-a-content-fragment-model}

An information architect would perform these tasks only sporadically as new models are required. For the purposes of this getting started guide, we only need to create one model.

1. Log into AEM as a Cloud Service and from the main menu select **Tools -&gt; Assets -&gt; Content Fragment Models**.
1. Tap or click on the folder that was made by creating your configuration.
   ![The models folder](../assets/models-folder.png)
1. Tap or click **Create**.
1. Provide a **Model Title** and **Description**.
   ![Create a model](../assets/models-create.png)
1. In the confirmation window, tap or click **Open** to configure your model.
   ![Confirmation window](../assets/models-confirmation.png)
1. Using the **Content Fragment Model Editor**, build your Content Fragment Model by dragging and dropping fields from the **Data Types** column.
   ![Drag and drop fields](../assets/models-drag-and-drop.png)
1. Once you place a field, you must configure its properties. The editor will automatically switch to the **Properties** tab for the added field where you can provide the mandatory fields.
   ![Configure properties](../assets/models-configure-properties.png)
1. When you are finished building your model, tap or click **Save**.

You can create multiple models. Models can reference other models. Use configurations to organize your models.

## Next Steps {#next-steps}

Now that you have defined the structures of your Content Fragments, you can move on to the third part of the getting started guide and [create folders where you will store the fragments themselves.](create-assets-folder.md)

>![TIP]
>
>For complete details about Content Fragment Models, see the [Content Fragment Models documentation](/help/assets/content-fragments/content-fragments-models.md)