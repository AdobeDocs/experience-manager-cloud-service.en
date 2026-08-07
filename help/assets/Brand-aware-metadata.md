---
title: Generate AI metadata using Brand Aware Metadata
description: Learn how to configure AI-powered prompts to generate metadata values for assets using Brand Aware Metadata in Adobe Experience Manager Assets.
role: Admin, User
badgeSaas: label="AEM Assets" type="Positive"
---

# Generate AI metadata using Brand Aware Metadata {#generate-ai-metadata-brand-aware}

[!DNL Adobe Experience Manager Assets] Brand Aware Metadata (BAM) enables you to configure AI-powered prompts to generate metadata values for assets.

Instead of manually populating repetitive metadata fields, BAM allows you to define prompts that guide AI to generate values for standard and custom metadata properties.

Brand Aware Metadata can be used for fields such as:

* Alt text
* Product attributes
* Asset classification
* Region
* Language

BAM uses layered prompting to generate metadata values:

* **Brand prompt** - Provides brand, campaign, and other always-on context applied to every generation.
* **Property prompt** - Defines instructions for generating values for a specific metadata property.
* **Controlled vocabulary** - Restricts AI-generated values to predefined options.

## Before you begin {#before-you-begin}

Ensure the following:

* Access to [!DNL Adobe Experience Manager Assets as a Cloud Service].
* Brand Aware Metadata enabled for your environment.
* Required permissions to access Prompt Editor and configure metadata.

## Get access to Brand Aware Metadata {#get-access-to-brand-aware-metadata}

[!DNL Brand Aware Metadata] is currently available in beta.

To request access:

1. Send an email to `aem-assets-brandawaremetadata@adobe.com`.
1. Join an introductory call to discuss your use case and the environments to enable.

# Configure Brand Aware Metadata {#configure-brand-aware-metadata}

Before creating prompts, open the Prompt Editor.

1. In [!DNL Adobe Experience Manager Assets], navigate to **[!UICONTROL Assets]**.
1. Select **[!UICONTROL Prompt Editor]**.

![Navigate to Prompt Editor](/help/assets/assets/prompt-editor.png)

The AI Metadata Prompts Manager displays the available property prompts, brand prompts, quality reports, and GenAI metrics.

![AI Metadata Prompts Manager](/help/assets/assets/ai-metadata-prompts-manager.png)

## Create a brand prompt {#create-brand-prompt}

A brand prompt provides common brand and campaign context that is applied to every metadata generation.

Use a brand prompt to define:

* Brand information.
* Campaign context.
* Tone requirements.
* Naming conventions.
* Content rules.

For example:

> We are Frescopa Coffee, currently running our Taste of Milan campaign with WKND; always append this campaign context to descriptions.

![Brand Prompts tab](/help/assets/assets/brand-prompts.png)

To create a brand prompt:

1. Open the **[!UICONTROL Brand Prompts]** tab.
1. Click **[!UICONTROL Create brand prompt]**.

 ![Create Brand Prompts](/help/assets/assets/create-brand-prompt.png)

1. In the **Prompt name** field, enter a name for the brand prompt.
1. In the **Prompt** field, enter natural language instructions that describe your brand context and always-on rules.
1. In the **Group** field, select an existing group or create a new group.
1. Click **[!UICONTROL Save]**.

You can create multiple brand prompts and organize them into groups. Brand prompts can then be associated with different processing profiles as needed.

## Create a property prompt {#create-property-prompt}

A property prompt defines instructions for generating values for a specific metadata property.

For example, you can create a property prompt to generate alt text for assets.

To create a property prompt:

1. In **[!UICONTROL Prompt Editor]**, click **[!UICONTROL Create prompt]**.
  ![Create property Prompts](/help/assets/assets/create-property-prompt.png)
1. In the **Prompt name** field, enter a name for the prompt.
1. Optional: In the **Description** field, enter a description for the prompt.
1. Optional: In the **Referenced properties** field, specify metadata properties that can be used as input when generating values.
1. Optional: In the **Group** field, select an existing group or create a new group.
1. From the **Metadata form** list, select a metadata form.

   Selecting a metadata form loads the available metadata properties.

    ![Metadata properties](/help/assets/assets/metadata-properties.png)

1. From the **Metadata property** list, select the metadata property that you want AI to populate.

1. In the **Prompt** field, enter instructions for generating the metadata value.

   For example:

   > Write concise alt text describing the main subject of the image.

1. Optional: Click **Generate preview output** to test the prompt and review the generated output.
1. Optional: Use **Suggest enhancements** to improve the prompt instructions.
1. In the **Prompt playground** section, select preview assets to evaluate how the prompt performs against sample assets.
1. Click **[!UICONTROL Save]** or **[!UICONTROL Save and close]**.

You can add the property prompt to one or more processing profiles and use the Prompt playground to refine the prompt before deploying it.

# Use referenced properties {#use-referenced-properties}

Referenced properties allow prompts to use additional asset metadata or file path information as context while generating metadata.

For example, referenced properties can provide:

* Product values
* Campaign information
* Dates
* Existing metadata values

![Referenced properties](/help/assets/assets/referenced-properties.png)

To add referenced properties:

1. In the property prompt editor, add one or more referenced properties.
1. Define how AI should use the referenced values in the prompt.
1. Preview the generated output using **[!UICONTROL Prompt Playground]**.

# Configure controlled vocabulary {#configure-controlled-vocabulary}

Controlled vocabulary keeps AI-generated values within existing dropdown or taxonomy values.

Use controlled vocabulary for metadata fields that have predefined values.

![Controlled vocabulary](/help/assets/assets/controlled-vocabulary.png)

To configure controlled vocabulary:

1. Open the controlled vocabulary section for the selected metadata property.
1. Add descriptions explaining when each value should be used.
1. Configure the property prompt.
1. Preview the generated values using **[!UICONTROL Prompt Playground]**.

>[!NOTE]
>
>A field can use either generative output or controlled vocabulary. Combining both options for the same field is currently not supported.

# Enhance prompts using Prompt Enhancer {#prompt-enhancer}

Prompt Enhancer converts simple prompts into structured prompts with suggested improvements.

To enhance a prompt:

1. Enter a prompt for the metadata property.
1. Click **[!UICONTROL Suggest Enhancements]**.
 ![Prompt Enhancer](/help/assets/assets/suggest-enhancement.png)

1. Review the suggested improvements and confidence metrics.
  ![Prompt Enhancer suggestion](/help/assets/assets/prompt-enhancement-suggestion.png)

1. Apply the enhancement if required.

# Test prompts using Prompt Playground {#test-prompts-using-playground}

Prompt Playground allows you to test prompts against sample assets before applying them to your asset library.

>[!NOTE]
>
>Prompt Playground only previews generated values. Metadata is not written to assets during testing.

![Prompt Playground](/help/assets/assets/prompt-playground.png)

To test a prompt:

1. Scroll to **[!UICONTROL Prompt Playground]** in the property prompt editor.
1. Select one or more preview assets.
1. Click **[!UICONTROL Generate]**.
1. Review the generated values and confidence score.
1. Refine the prompt if required.

# Apply AI metadata at scale {#apply-ai-metadata-at-scale}

After creating a prompt, associate it with a processing profile so that the prompt can be applied during asset processing workflows.

1. In the **Prompt list**, select the property prompt that you want to use.
1. Click **[!UICONTROL Add to Processing Profile]** from the action bar.
1. Select the processing profile where you want to use the prompt.
1. Save the configuration.

Once associated with a processing profile, the prompt can be executed when processing existing assets or automatically when new assets are uploaded to configured folders.

![Processing profile with Brand Aware Metadata prompts](/help/assets/assets/add-processing-file.png)

Brand Aware Metadata supports the following processing workflows:

* Reprocess existing assets to populate metadata.
* Automatically process newly uploaded assets.

## Apply BAM to existing assets {#apply-bam-to-existing-assets}

Reprocess a folder to populate metadata for assets that already exist in your DAM.

To apply Brand Aware Metadata to existing assets:

1. Navigate to the folder that contains the assets.
1. Select the folder.
 ![Reprocess assets using a processing profile](/help/assets/assets/reprocess-assets.png)

1. Apply the required processing profile.
  ![Reprocess assets tab](/help/assets/assets/reprocess-tab.png)
1. Start the reprocessing operation.
1. Wait for processing to complete.
1. Open an asset and verify that the configured metadata fields are populated.

## Process new assets automatically {#process-new-assets}

Configure a folder to automatically process newly uploaded assets using a Brand Aware Metadata processing profile.

To automatically process new assets:

1. Open the folder configuration.
1. Associate the required Brand Aware Metadata processing profile.
1. Save the configuration.
1. Upload new assets to the configured folder.
1. Verify that metadata is generated after processing completes.

## Verify generated metadata {#verify-generated-metadata}

After processing completes:

1. Open the processed asset.
1. Click **[!UICONTROL Properties]**.
1. Review the metadata fields configured in the processing profile.
1. Verify that the generated values match the expected output.

# Limitations {#limitations}

[!DNL Brand Aware Metadata] is currently available in beta.

Keep the following considerations in mind before applying BAM at scale:

* BAM evaluates images only. To use additional information such as another metadata field value or file path information, configure referenced properties.

* Processing overwrites existing metadata values. There is currently no option to populate only empty fields.

* BAM uses a general-purpose GPT model. Highly specialized recognition, such as identifying an exact product SKU, may not always produce reliable results.

* Brand Guidelines configured in governance are not automatically applied during metadata generation. Include brand context directly in the brand prompt.

* For dropdown and taxonomy-backed fields, use controlled vocabulary to restrict generated values to existing options.