---
title: Create the Content Structure for Your App
description: Learn how to use AEM's Content Fragment models to create your content structure, which serves as the foundation for your headless content.
hidefromtoc: yes
index: no
exl-id: ace9b9f3-8bc6-4a36-a51c-ff60cdd339ce
---

# Create the Content Structure for Your App {#content-structure}

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_overview"
>title="Create the content structure for your app"
>abstract="As you follow this series of interactive guides you learn to create a structure (known as the Content Fragment model) which serves as the foundational structure for your headless content."

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_overview_guide"
>title="Launch the model console"
>abstract="Let's explore how to create a reusable schema, called a Content Fragment model, for your content in Adobe Experience Manager as a Cloud Service. Watch the video to understand why this is an important step. <br><br>In this learning module we'll use a travel site as our example and walk through creating a model that represents a trip.<br><br>Launch this module in a new tab by clicking the button below and then follow this guide."
>additional-url="https://video.tv.adobe.com/v/3413261" text="Content structure intro video"

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_overview_guide_footer"
>title="Congratulations! You learned how to create a Content Fragment model to represent the structure of your headless data and took the first step to delivering omni-channel content in a scaled and standard way."
>abstract=""

## Create a Model {#create-model}

The Content Fragment model console opens in a new tab. Think of the Content Fragment model console as your library of models, where you create new models and manage existing models.

For our example, we will create a model that represents the data structure of a trip that is featured on a travel website. We will refer to a trip using this model as an **Adventure**.

1. Click the **Create** button at the top-right of the screen to begin creating a Content Fragment model.

1. The Create Model wizard starts, which guides you through creating your model. Provide the mandatory information.

   * **Model Title** - This is a brief label of the model and usually indicates the purpose of the model. We will call our new model `Adventure`.
   * **Enable model** - This option is checked by default and must be checked to be able to create Content Fragments based on this model.

1. Once the mandatory fields are populated, click **Create** at the top-left to create the model. 

1. The **Success** dialog confirms that the model was created. Click **Open** in the dialog to open your new Content Fragment Model in the editor in a new tab. Then continue on to the next step to adding data fields to your model.

![Steps two and three of creating a Content Fragment model](assets/do-not-localize/create-model.png)

## Using the Model Editor {#configure-model}

We now have a model called **Adventure**, but it has no details like duration, destination, activities, etc. Before you can use your model, you need to define the structure of its data. 

The Content Fragment Model editor is where you configure the data types and properties that define the content of your model.

>[!TIP]
>
>It’s important to follow the naming schemas in the following instructions since we will refer to these specific names in later modules.

1. Drag a **Single line text** field from the **Data Types** panel at the right of the editor and drop it onto your Content Fragment model. 

1. Once a data type is placed, the **Data Types** column automatically changed to the **Properties** tab, where you can define the details of the data type you just placed. For this first field, we want to store the title of the trip or adventure. Enter the following properties.

   * **Render As:** **Text Field** - When you create an adventure, this field will store the title of the adventure.
   * **Field Label:** `Title` - This is the label that is displayed for this field when creating a new adventure.

1. Once you define the properties of the field you can switch back to the **Data Types** tab in the right panel and add additional fields by dragging and dropping.

In this way, you can add as many fields as necessary to your model to support whatever kind of data structure you may need. The types of data fields vary, but the process of adding them to your model remains the same.

Continue on to the next section to add the fields necessary to complete and save the **Adventure** model

![Steps one, two, and three of adding fields to the model](assets/do-not-localize/define-model-fields.png)

## Add Fields to the Model {#additional-fields}

You already have a field for the title of the adventure. Now you need to add fields to capture the description, price, and a representative image of the adventure.

>[!TIP]
>
>The **Adventure** model is based on the WKND sample site for AEM. You can [visit the site here](https://wknd.site/us/en/adventures/yosemite-backpacking.html) to see content that uses the **Adventure** model.

Follow the same steps as above to add these additional fields. The only difference are the properties you need to set.

1. Add a field to store the description of the adventure by dragging and dropping a **Multi line text** field and enter the following properties:

   * **Render As:** **Text Area** - When you create an adventure, this field will store a brief description of the trip.
   * **Field Label:** `Description` - This is the label that is displayed for this field when creating a new adventure.

1. Add a field to store the price of the adventure by dragging and dropping a **Single line text** field and enter the following properties:

   * **Render As:** **Text field** - When you create an adventure, this field will store the price of the trip.
   * **Field Label:** `Price` - This is the label that is displayed for this field when creating a new adventure.

1. Add a field to store an image representing the trip. Images in AEM are stored as another type of content called **Assets**. So to create a field for them you need to drag and drop a **Content Reference** field that will reference the asset of the image.

   * **Render As:** **Content Reference** - When you create an adventure, this field will point to the image asset representing this trip.
   * **Field Label:** `Image` - This is the label that is displayed for this field when creating a new adventure.

1. Once you have added all of the fields necessary for the Content Fragment model, click **Save** at the top-right of the window.

1. The model is saved and you return to the Content Fragment model Console.
