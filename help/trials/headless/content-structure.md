---
title: Create the Content Structure for Your App
description: Learn how to create the structure which serves as the foundation for all of your headless content using AEM's Content Fragment models.
hidefromtoc: yes
index: no
exl-id: ace9b9f3-8bc6-4a36-a51c-ff60cdd339ce
---

# Create the Content Structure for Your App {#content-structure}

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_overview"
>title="Create the content structure for your app"
>abstract="As you follow this series of interactive guides you learn to create a structure (known as the Content Fragment model) which serves as the foundation for your headless content."

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_overview_guide"
>title="Launch the model console"
>abstract="Let's explore how to create a reusable schema, called a Content Fragment model, for your content in Adobe Experience Manager as a Cloud Service. Watch the video to understand why this is an important step. <br><br>Launch this module in a new tab by clicking the button below and then follow this guide."
>additional-url="https://video.tv.adobe.com/v/3413261" text="Content structure intro video"

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_overview_guide_footer"
>title="Congratulations! You learned how to create a Content Fragment model to represent the structure of your headless data and took the first step to delivering omni-channel content in a scaled and standard way."
>abstract=""

## Create a Model {#create-model}

Clicking the **Launch the model console** button above opens the Content Fragment models console in a new tab. 

![The Content Fragment model console](assets/content-structure/content-fragment-model-console.png)

Think of the Content Fragment model console as your library of models, where you create new models and manage exiting models. Your console starts empty, so let's create a new model!

1. In the Content Fragment model console, click the **Create** button at the top-right of the screen to begin creating a Content Fragment model.

1. The Create Model wizard starts, which guides you. 

   ![Content Fragment model wizard](assets/content-structure/model-wizard.png)

   Provide the mandatory information.

   * **Model Title** - This is a brief description of the model and usually indicates the purpose of the model.
   * **Enable model** - This option is checked by default and must be checked to be able to create Content Fragments based on this model.

1. Once the mandatory fields are populated, click **Create** at the top-left to create the model. 

1. The **Success** dialog confirms that the model was created.

   ![Success dialog for creating a new Content Fragment model](assets/content-structure/success.png)

## Add Fields to the Model {#configure-model}

Before you can use the model, you need to define the structure of its data.

1. Click **Open** in the **Success** dialog from the previous step to open your new model in the Content Fragment model editor where you can define its fields.

1. Drag a field from the **Data Types** panel at the right of the editor and drop it onto your Content Fragment model. 

   ![Add a data type](assets/content-structure/drop-fields.png)

1. Once a data type is placed, the **Data Types** column automatically changed to the **Properties** tab, where you can define the details of the data type you just placed.

   ![The Properties tab for the data field](assets/content-structure/data-type-properties.png)

1. Once you have added all of the fields necessary for the Content Fragment model, click **Save** at the top-right of the window.

The model is saved and you return to the Content Fragment model Console where you can add more models as necessary.

![Module complete](assets/content-structure/content-fragment-model-console-populated.png)
