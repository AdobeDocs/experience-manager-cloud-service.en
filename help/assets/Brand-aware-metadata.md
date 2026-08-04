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

![Brand Aware Metadata workflow showing layered prompting](TODO)

## Before you begin {#before-you-begin}

Ensure the following:

* Access to [!DNL Adobe Experience Manager Assets as a Cloud Service].
* Brand Aware Metadata enabled for your environment.
* Required permissions to access Prompt Editor and configure metadata.

>[!NOTE]
>
>[PLACEHOLDER: Add access requirements, permissions, and environment details.]

## Get access to Brand Aware Metadata {#get-access-to-brand-aware-metadata}

[!DNL Brand Aware Metadata] is currently available in beta.

To request access:

1. Send an email to `aem-assets-brandawaremetadata@adobe.com`.
1. Join an introductory call to discuss your use case and the environments to enable.

# Configure Brand Aware Metadata {#configure-brand-aware-metadata}

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

![Manage brand prompts option in Prompts Manager](TODO)

To create a brand prompt:

1. In [!DNL Prompts Manager], select **[!UICONTROL Manage brand prompts]**.

   ![Manage brand prompts](TODO)

1. Enter natural language instructions describing your brand context and always-on rules.

   ![Brand prompt configuration](TODO)

1. Click **[!UICONTROL Save]**.

You can create multiple brand prompts and attach them to different processing profiles.

## Create a property prompt {#create-property-prompt}

A property prompt defines instructions for generating values for a specific metadata property.

For example, you can create a property prompt to generate alt text for assets.

![AI Metadata Prompt Editor](TODO)

To create a property prompt:

1. In [!DNL Prompt Editor], create a new property prompt.

1. Enter a name for the prompt.

1. Select a metadata form.

   Selecting a metadata form loads the available metadata properties that can be populated.

   ![Select metadata form](TODO)

1. Select the metadata property that you want AI to generate values for.

   ![Select metadata property](TODO)

1. Enter prompt instructions.

   For example:

   > Write concise alt text describing the main subject of the image.

1. Click **[!UICONTROL Save]**.

1. Preview the generated values in [!UICONTROL Prompt Playground] and refine the prompt as required.

## Metadata forms and metadata schemas {#metadata-forms-and-schemas}

[PLACEHOLDER: Add details explaining metadata form and metadata schema behavior.]

# Use referenced properties {#use-referenced-properties}

Referenced properties allow prompts to use additional asset metadata or file path information as context while generating metadata values.

Teams can use referenced properties to provide additional context such as:

* Product values.
* Campaign information.
* Dates.
* Existing metadata values.

![Referenced properties configuration](TODO)

To add referenced properties:

1. In the property prompt editor, add referenced properties.

1. Define how AI should use the referenced values in the prompt.

1. Preview the generated output in [!UICONTROL Prompt Playground].

# Configure controlled vocabulary {#configure-controlled-vocabulary}

Controlled vocabulary helps keep AI-generated values within existing dropdown or taxonomy values.

Use controlled vocabulary for metadata fields that have a predefined set of values.

![Controlled vocabulary editor](TODO)

To configure controlled vocabulary:

1. In the property prompt for a constrained field, open the controlled vocabulary section.

1. Add descriptions explaining when each value should be used.

1. Configure the field's property prompt.

1. Preview the generated values in [!UICONTROL Prompt Playground].

>[!NOTE]
>
>A field can use either generative output or controlled vocabulary. Both options cannot be combined for the same field.

# Enhance prompts using Prompt Enhancer {#prompt-enhancer}

Prompt Enhancer helps convert simple prompts into structured prompts with suggested improvements.

![Prompt Enhancer suggestions](TODO)

To enhance a prompt:

1. Add a prompt for your metadata property.

1. Select **[!UICONTROL Suggest Enhancements]**.

1. Review the suggested improvements and confidence metrics.

1. Apply the enhancement if required.

# Test prompts using Prompt Playground {#test-prompts-using-playground}

[!UICONTROL Prompt Playground] allows you to test prompts against sample assets before applying them to your asset library.

>[!NOTE]
>
>No metadata is written to assets when using [!UICONTROL Prompt Playground].

![Prompt Playground interface](TODO)

To test a prompt:

1. In the property prompt editor, scroll to [!UICONTROL Prompt Playground].

1. Select sample assets.

1. Click **[!UICONTROL Generate]**.

1. Review generated values and confidence scores.

1. Refine the prompt if required.

# Apply AI metadata at scale {#apply-ai-metadata-at-scale}

After validating prompts in [!UICONTROL Prompt Playground], apply Brand Aware Metadata through an AEM processing profile.

A processing profile can contain multiple property prompts that populate metadata fields when the profile runs.

![Processing profile with Brand Aware Metadata prompts](TODO)

## Apply BAM to existing assets {#apply-bam-to-existing-assets}

You can apply BAM to existing assets by reprocessing folders with a BAM-enabled processing profile.

![Reprocessing assets using processing profile](TODO)

To reprocess existing assets:

[PLACEHOLDER: Add validated processing steps after hands-on testing.]

## Process new assets automatically {#process-new-assets}

Configure folders to automatically process new assets using a BAM-enabled processing profile.

![Process assets on arrival configuration](TODO)

To process new assets:

[PLACEHOLDER: Add validated process-on-arrival steps after hands-on testing.]

# Limitations {#limitations}

[!DNL Brand Aware Metadata] is currently available in beta.

Keep the following considerations in mind before applying BAM at scale:

* BAM evaluates images only. To use additional information such as another metadata field value or file path details, configure referenced properties.

* Processing can overwrite existing metadata values. There is currently no option to populate only empty fields.

* BAM uses a general-purpose GPT model. Highly specialized recognition, such as identifying exact product SKUs, may not always provide reliable results.

* Brand Guidelines configured in governance are not automatically applied to BAM generations. Add brand context directly to the brand prompt.

* For dropdown and taxonomy-backed fields, use controlled vocabulary to restrict AI-generated values to existing options.