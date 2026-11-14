---
title: Brand Aware Metadata Best Practices
description: Learn Brand Aware Metadata best practices in AEM Assets through a WKND example, from tags and schema fields to brand prompts, vocabularies, and QA.
hidefromtoc: 'yes'
role: Admin, User
badgeSaas: label="AEM Assets" type="Positive"
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
---

# Brand Aware Metadata best practices: a WKND tutorial {#brand-aware-metadata-best-practices}

Complete, accurate metadata is what makes assets findable, reusable, and accessible. Producing it takes real effort. For every asset, someone has to understand the content, know the business context, and fill in descriptions, classifications, and other fields in a way that follows your brand's rules and taxonomy. Generic AI capabilities describe what is visible in an asset, but they cannot know your brand voice, your campaigns, your approved vocabulary, or details that exist only in other systems.

[!DNL Brand Aware Metadata] (BAM) in [!DNL Adobe Experience Manager Assets] generates values for your own metadata properties, such as free-text descriptions, alt text, tag-based classifications, and dropdown selections, using brand context, approved values, and existing metadata. The quality of the generated metadata, however, depends directly on how you set it up.

This article applies Adobe's recommended best practices to a complete, end-to-end example for **WKND**, a fictitious adventure-travel brand. You prepare the metadata model, write and refine prompts, add brand and business context, and validate the results before you scale. By the end, four brand-specific properties are generated automatically for every asset in a campaign folder.

As part of this tutorial, you configure and generate the following properties for all assets in a campaign folder:

| Property | Field type | Why it is hard to fill in |
|---|---|---|
| Alt Text | Free text | Needs the brand's voice, not a generic caption. |
| Activity Type | Controlled vocabulary (tags) | Needs WKND's own terms, including niche ones. |
| Region | Controlled vocabulary (dropdown) | Cannot be read from the pixels at all. |
| Campaign | Controlled vocabulary (dropdown) | Pure business context. |

Along the way, you use five BAM capabilities: **[!UICONTROL Prompt Playground]**, **[!UICONTROL Prompt Enhancer]**, **brand prompts**, **controlled vocabulary**, and **referenced properties**.

>[!NOTE]
>
>This article builds on [Generate Brand Aware Metadata](/help/assets/brand-aware-metadata.md), which describes each BAM capability in detail. [!DNL Brand Aware Metadata] is currently available in beta.

## Best practices at a glance {#best-practices-at-a-glance}

The following table lists Adobe's recommended best practices for Brand Aware Metadata, in the order in which you first apply them in this tutorial.

| Best practice | Where you apply it |
|---|---|
| Scope each controlled-vocabulary field to only its relevant set of allowed values. | [Step 2: Create the tag hierarchy](#create-tag-hierarchy) and [Step 3: Add the fields to a metadata schema](#add-fields-to-metadata-schema) |
| Use brand prompts for global context, and scope them to processing profiles for folder-level control. | [Step 4: Apply the schema and a processing profile](#apply-schema-and-profile), [Step 7: Add a brand prompt](#add-brand-prompt), and [Step 10: Derive the campaign](#derive-campaign) |
| Structure prompts one-to-one with properties, and organize them around the property, not individual values. | [Step 5: Create a property prompt](#create-property-prompt) |
| Iterate in Prompt Playground before you touch real assets, then use Prompt Enhancer to tighten the prompt. | [Step 5: Create a property prompt](#create-property-prompt) and [Step 6: Refine the prompt](#refine-prompt-with-enhancer) |
| Constrain output with controlled vocabulary, and start with as little definition as possible. | [Step 8: Constrain with controlled vocabulary](#constrain-with-controlled-vocabulary) and [Step 9: Add referenced properties](#add-referenced-properties) |
| Use referenced properties to build on existing metadata. | [Step 9: Add referenced properties](#add-referenced-properties) |
| Build a quality gate before scaling: sample, review in the quality report, and route by confidence. | [Step 11: Validate on a sample, then scale](#validate-and-scale) |
| Use BAM for deterministic fields too, but weigh the credit cost. | [Additional best practices](#additional-best-practices) |

## Example scenario: WKND {#example-scenario}

The WKND content team manages thousands of trip photos. Photographers upload assets from [!DNL Adobe Bridge], and trip details arrive from [!DNL Adobe Workfront]. Before the marketing team can find and use an asset, it needs alt text, an activity type, a region, and a campaign. Today, a librarian fills in those fields manually.

This tutorial uses two sample assets, both stored in `/content/dam/wknd/campaigns/winter-backcountry-2027`:

| | Asset A | Asset B |
|---|---|---|
| File | `WKND_ALP-BC-07_0412.jpg` | `WKND_TET-SB-02_0198.jpg` |
| Image content | Three skiers on climbing skins, crossing a snowy ridgeline at sunrise, wearing avalanche packs. | A rider carving down an untouched powder slope, with no lifts or other gear visible. |
| Shoot brief (from [!DNL Workfront]) | "Guided three-day ski-touring itinerary, Mont Blanc massif, intermediate pace." | "Two-day splitboard weekend, Teton Range, Wyoming. Intermediate." |
| Why it is useful | Clear visual signals. | Visually ambiguous, so it needs context. |

>[!NOTE]
>
>The generated values shown in this article are representative examples. Your results can vary because AI output is not deterministic.

<!-- TODO: verify. Replace the example outputs with values captured from a BAM-enabled environment before publishing. -->

## Prerequisites {#prerequisites}

Ensure the following:

* Access to [!DNL Adobe Experience Manager Assets as a Cloud Service] with [!DNL Brand Aware Metadata] enabled. To request access, see [Get access to Brand Aware Metadata](/help/assets/brand-aware-metadata.md#get-access-to-brand-aware-metadata).
* Administrator permissions, or the permissions required to create tags, [edit metadata schemas](/help/assets/metadata-schemas.md#Permissions-required-to-edit-metadata-schemas), create processing profiles, and access **[!UICONTROL Prompt Editor]**.
* The folder `/content/dam/wknd/campaigns/winter-backcountry-2027` with a few sample assets.

## Step 1: Review the baseline metadata for an asset {#review-baseline-metadata}

Before you configure BAM, look at what you start with, so that you can measure the improvement later.

1. In the [!DNL Assets] user interface, navigate to the `winter-backcountry-2027` folder.
1. Select Asset A and click **[!UICONTROL Properties]**.
1. Review the generic [Smart Tags](/help/assets/smart-tags.md) already applied to the asset. Typically, they look like `snow`, `mountain`, `skiing`, `person`, and `sky`.
1. Note that the alt text, activity type, region, and campaign fields are not yet available in the asset properties. You add these fields in the next steps.

To fill in those fields manually, a librarian reads the shoot brief, opens the tag picker, finds the right activity, picks a region from the list, writes alt text, and picks a campaign. That work is repeated for every asset.

**Checkpoint, the baseline:** Generic tags describe pixels. None of the four WKND fields are populated, and filling them in manually takes several minutes per asset.

<!-- TODO: verify. Optionally replace "several minutes" with a measured time for one asset. -->

## Step 2: Create the tag hierarchy for Activity field {#create-tag-hierarchy}

Execute the following steps to create a tag hierarchy for the Activity field.

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL General]** > **[!UICONTROL Tagging]**.
1. Click **[!UICONTROL Create]** > **[!UICONTROL Create Namespace]**, enter the following values, and click **[!UICONTROL Create]**:
   * **[!UICONTROL Title]**: `WKND`
   * **[!UICONTROL Name]**: `wknd`
1. Select the `WKND` namespace, click **[!UICONTROL Create]** > **[!UICONTROL Create Tag]**, and create a tag with the **[!UICONTROL Title]** `Activity` and the **[!UICONTROL Name]** `activity`. This tag is the root of the activity branch.
1. Select the `Activity` tag and create the following category tags under it. Then select each category tag and create its child tags:

   | Category tag | Child tags |
   |---|---|
   | Snow Sports | Backcountry Skiing, Resort Skiing, Snowboarding, Splitboarding |
   | Climbing | Alpine Climbing, Sport Climbing, Bouldering |
   | Water Sports | Surfing, Sea Kayaking, Stand-Up Paddleboarding |
   | Cycling | Gravel Riding, Mountain Biking |
   | Camp & Trek | Backpacking |

1. [Publish the tags](/help/sites-cloud/administering/tags.md#publishing-tags) if your assets are also used on publish.

The result is a branch at `/content/cq:tags/wknd/activity`. For detailed instructions on the tagging console, see [Administering tags](/help/sites-cloud/administering/tags.md#creating-new-tags).

>[!TIP]
>
>Give each tag a clear, descriptive title. Modern models map content to a well-named set of values accurately, often without any additional definition.

>[!VIDEO](https://video.tv.adobe.com/v/3508318)

## Step 3: Add the brand fields to the metadata schema {#add-fields-to-metadata-schema}

In this step, you add the four WKND fields to the metadata schema, plus a field for the shoot brief that [!DNL Workfront] provides.

>[!IMPORTANT]
>
>Configure the schema fields and their allowed values **before** you create prompts. A property prompt loads its properties and controlled vocabulary values using the metadata form.

### Create the WKND schema {#create-wknd-schema}

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Schemas]**.
1. Select the `default` schema form, click **[!UICONTROL Copy]**, and name the copy `WKND`. Alternatively, click **[!UICONTROL Create]** to start a new form. For details, see [Add a metadata schema form](/help/assets/metadata-schemas.md#add-a-metadata-schema-form).
1. Select the `wknd` form and click **[!UICONTROL Edit]**.
1. In the **[!UICONTROL Metadata Schema Form Editor]**, click **+** to add a tab and name it `WKND`. Adding a dedicated tab keeps the brand fields together on the asset **[!UICONTROL Properties]** page.

Next, drag the following components from the **[!UICONTROL Build Form]** tab to the `WKND` tab:

* [Single Line Text](#add-alt-text-field) for Alt Text field
* [Standard Tags](#add-activity-type-field) for Activity Type field
* [Dropdown](#add-region-field) for Region field
* [Dropdown](#add-campaign-field) for Campaign field

>[!NOTE]
>
>Use a custom namespace prefix such as `wknd:` in **[!UICONTROL Map to property]**. A custom namespace keeps brand-specific properties separate from standard properties and makes them easy to identify when you configure prompts and referenced properties.

### Add the Alt text field {#add-alt-text-field}

1. Drag a **[!UICONTROL Single Line Text]** component to the tab.
1. Click the field and configure the following options using the **Settings** tab:
   * **[!UICONTROL Field Label]**: `Alt text`
   * **[!UICONTROL Map to property]**: `./jcr:content/metadata/Iptc4xmpCore:AltTextAccessibility`
   * **[!UICONTROL Description]**: `Accessible description of the image, under 125 characters.`

<!-- TODO: verify. The demo script specifies a multi-line text field for alt text. Confirm the component name available in the Build Form tab. -->

### Add the Activity type field {#add-activity-type-field}

1. Drag a **[!UICONTROL Standard Tags]** component to the tab.
1. Click the field and configure the following options using the **Settings** tab:
   * **[!UICONTROL Field Label]**: `Activity type`
   * **[!UICONTROL Map to property]**: `./jcr:content/metadata/wknd:activity`
   * **[!UICONTROL Root Path]**: `/content/cq:tags/wknd/activity`

Setting the root path is the key best practice for tag fields. The field, and BAM, then see only the activity branch rather than the entire tag tree.

### Add the Region field {#add-region-field}

1. Drag a **[!UICONTROL Dropdown]** component to the tab.
1. Click the field and configure the following options using the **Settings** tab:
   * **[!UICONTROL Field Label]**: `Region`
   * **[!UICONTROL Map to property]**: `./jcr:content/metadata/wknd:region`
1. Under **[!UICONTROL Choices]**, Select **Add Manually** and click **[!UICONTROL Add Choice]** for each option and enter the following option text and values:

   | Option text | Value |
   |---|---|
   | European Alps | `european-alps` |
   | Rocky Mountains | `rocky-mountains` |
   | Pacific Northwest | `pacific-northwest` |
   | Patagonia | `patagonia` |
   | Scandinavia | `scandinavia` |
   | Iceland | `iceland` |
   | New Zealand | `new-zealand` |
   | Southeast Asia | `southeast-asia` |

### Add the Campaign field {#add-campaign-field}

1. Drag a **[!UICONTROL Dropdown]** component to the tab.
1. Click the field and configure the following options using the **Settings** tab:
   * **[!UICONTROL Field Label]**: `Campaign`
   * **[!UICONTROL Map to property]**: `./jcr:content/metadata/wknd:campaign`
1. Under **[!UICONTROL Choices]**, Select **Add Manually** and click **[!UICONTROL Add Choice]** for each option and enter the following option text and values:

   | Option text | Value |
   |---|---|
   | Winter Backcountry 2027 | `winter-backcountry-2027` |
   | Summer Surf Camps 2027 | `summer-surf-camps-2027` |
   | Gravel & Grit 2027 | `gravel-and-grit-2027` |
   | Everyday Explorer (evergreen) | `everyday-explorer` |

### Add the Shoot brief field {#add-shoot-brief-field}

1. Drag a **[!UICONTROL Single Line Text]** component to the tab.
1. Configure the following settings:
   * **[!UICONTROL Field Label]**: `Shoot brief`
   * **[!UICONTROL Map to property]**: `./jcr:content/metadata/wknd:shootBrief`
1. In **[!UICONTROL Rules]** tab, Select **[!UICONTROL Disable Edit]**, because [!DNL Workfront] writes this value upstream.

Adding this field to the form is optional. BAM can reference a property even when it does not appear on the form. Displaying it, however, helps reviewers see the context that BAM used. Make a note of the exact property name, `wknd:shootBrief`, because you type it when you configure referenced properties in Step 9.

Click **[!UICONTROL Save]** to save the schema.

>[!VIDEO](https://video.tv.adobe.com/v/3508328)

<!-- TODO: screenshot. Replace with a capture of the WKND tab showing the five fields and the Activity type root path setting. -->

**Why this matters:** A field scoped to a small, relevant set of values is faster and less error-prone for anyone picking a value manually. It also makes BAM more accurate, because the model chooses from a short list instead of reasoning over an entire enterprise taxonomy.

## Step 4: Apply the metadata schema and a processing profile to the campaign folder {#apply-schema-and-profile}

When you apply metadata schema to a folder, the fields included in the metadata schema display on the asset **[!UICONTROL Properties]** page for all assets within that folder. Once you have created the WKND metadata schema and configured the fields, you must apply the metadata schema to the `/content/dam/wknd/campaigns/winter-backcountry-2027` folder.

### Apply the metadata schema {#apply-metadata-schema}

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Schemas]**.
1. Select the `wknd` schema and click **[!UICONTROL Apply to Folders]**.
1. Select `/content/dam/wknd/campaigns/winter-backcountry-2027` and click **[!UICONTROL Apply]**. If the folder already uses another schema, click **[!UICONTROL Overwrite]**.
1. Open Asset A, click **[!UICONTROL Properties]**, and confirm that the `WKND` tab displays the new fields.

For details, see [Apply folder-specific metadata](/help/assets/metadata-schemas.md#applying-folder-specific-metadata).

The processing profile determines which BAM prompts run for the assets in a folder. You can associate multiple property prompts to a processing profile and similarly associate a processing profile with a brand prompt as well. When the brand prompt and the property prompt have the same processsing profile assigned to them, the metadata for a field is automatically generated based on the property prompt as well as the brand prompt. 

### Create and apply a processing profile {#create-processing-profile}

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Processing Profiles]**.
1. Click **[!UICONTROL Create]**, name the profile `WKND Winter Backcountry 2027`, and click **[!UICONTROL Save]**. For details, see [Create a standard profile](/help/assets/asset-microservices-configure-and-use.md#create-standard-profile).
1. Select the profile, click **[!UICONTROL Apply Profile to Folders]**, select the `winter-backcountry-2027` folder, and click **[!UICONTROL Apply]**.

Only one processing profile can be applied to a folder, and it applies to all subfolders unless a subfolder has its own profile. For details, see [Use processing profiles to process assets](/help/assets/asset-microservices-configure-and-use.md#use-profiles).

>[!TIP]
>
>Plan your folder structure around metadata context. Because each processing profile can carry one brand prompt, the folder hierarchy becomes the mechanism that routes context to assets. For example, a `/campaigns/winter-backcountry-2027` folder and a `/campaigns/summer-surf-camps-2027` folder can each carry their own campaign context.

## Step 5: Create a property prompt and test it in Prompt Playground {#create-property-prompt}

Start with one property and a short, plain-language prompt. Do not try to populate several fields from one prompt.

1. In [!DNL Assets], switch to **[!UICONTROL Admin view]** and navigate to **[!UICONTROL Assets]** > **[!UICONTROL Brand-Aware Metadata]**.
1. Click **[!UICONTROL Create property prompt]**.
1. Configure the following fields:
   * **[!UICONTROL Prompt name]**: `WKND alt text`
   * **[!UICONTROL Group]**: create a group named `WKND`, so that all WKND prompts stay together.
   * **[!UICONTROL Metadata form]**: `WKND`
   * **[!UICONTROL Metadata property]**: `Iptc4xmpCore:AltTextAccessibility`. [The dropdown menu just displays the properties that you configured while defining the properties for WKND schema](#create-wknd-schema).
1. In the **[!UICONTROL Prompt]** field, enter:

   ```
   Write alt text for this image. One sentence, under 125 characters.
   Describe what the people are doing and where.
   Don't start with "Image of" or "Photo of".
   ```

1. In the **[!UICONTROL Prompt Playground]** section, select Asset A as a preview asset, then click **[!UICONTROL Generate preview output]**.
1. Review the generated value and its confidence score.
1. Click **[!UICONTROL Save]**.

>[!NOTE]
>
>* The **[!UICONTROL Metadata form]** list displays only metadata forms defined in **[!UICONTROL Admin view]**.
>* The **[!UICONTROL Description]** field helps you organize prompts but does not affect generation. Put all instructions in the **[!UICONTROL Prompt]** field.
>* Prompt Playground previews results without writing anything to your assets and without consuming generation credits.


**Example output:** "A breathtaking view of skiers trekking up a stunning snow-covered ridge at sunrise."

**Checkpoint, accurate but generic:** The caption is correct and took a single prompt. However, it sounds like every other AI caption. It uses hype words and says nothing about WKND's voice.

## Step 6: Refine the prompt with Prompt Enhancer {#refine-prompt-with-enhancer}

A first draft is rarely your best prompt. [!UICONTROL Prompt Enhancer] rewrites a plain-language prompt into a tighter, better-structured version for you to review.

1. Navigate to **[!UICONTROL Assets]** > **[!UICONTROL Brand-Aware Metadata]** > **[!UICONTROL Prompt List]**. Select the `WKND alt text` prompt and click **Edit**.
1. Click **[!UICONTROL Suggest enhancements]**.
1. Review the suggested rewrite and its confidence metrics. You can apply it, edit it, or discard it. Nothing changes until you apply it.

   An example of a suggested rewrite:

   ```
   Write alt text for this image, for screen-reader users.
   - Format: one sentence, under 125 characters.
   - Content: say what the people are doing and where.
   - Style: start with the subject. Don't begin with "Image of" or "Photo of".
   ```

1. Click **[!UICONTROL Apply enhanced prompt]**.
1. Click **[!UICONTROL Generate preview output]** again. In the Prompt Playground section, select preview assets to evaluate how the prompt performs against sample assets.
1. Click **[!UICONTROL Save]**.

**Example output:** "Skiers trek up a snow-covered ridge at sunrise."

**Checkpoint, tighter but still not WKND:** The caption is cleaner and follows the format rules more reliably. Prompt Enhancer improves how the prompt is written, but it does not know your brand. A brand prompt provides that context.

>[!VIDEO](https://video.tv.adobe.com/v/3508329)

>[!TIP]
>
>* Run Prompt Enhancer on each property prompt as you write it, then confirm the results in Prompt Playground before you scale.
>* Keep prompts concise. Long prompts consume more input tokens and are more likely to contain contradictory instructions that reduce accuracy.

## Step 7: Add global context with a brand prompt {#add-brand-prompt}

A brand prompt holds context that applies to all property prompts in a processing profile, so you write it once. Use a brand prompt for any higher-level context, such as voice, global rules, naming conventions, or campaign details.

1. Navigate to **[!UICONTROL Assets]** > **[!UICONTROL Brand-Aware Metadata]** > **[!UICONTROL Brand Prompts]** and click **[!UICONTROL Create brand prompt]**.
1. In **[!UICONTROL Prompt name]**, specify `WKND Winter Backcountry 2027`, and in **[!UICONTROL Group]**, select `WKND`.
1. In the **[!UICONTROL Prompt]** field, enter:

   ```
   You are generating metadata for WKND, an adventure-travel brand that runs
   guided trips for people who want real outdoor experiences without the
   elitism. Voice: warm, plainspoken, inclusive. Never hyped.
   Avoid clichés and superlatives such as "breathtaking", "stunning", "epic",
   "majestic". Describe what people are doing, not how they look.
   Mention the key gear when it is visible.
   Always write in US English. Never invent place names or gear brands that
   aren't visible or provided.

   Folder context: assets in this folder support the Winter Backcountry 2027
   campaign, which promotes guided backcountry ski and splitboard trips for
   intermediate riders.
   ```

1. Click **[!UICONTROL Save]**.
1. Associate the brand prompt with the [WKND Winter Backcountry 2027 processing profile](#create-processing-profile). A brand prompt has a one-to-one relationship with a processing profile, and processing profiles apply at the folder level, so this context applies to every asset in the `winter-backcountry-2027` folder.
1. Add the `WKND alt text` property prompt to the same processing profile. In the prompt list, select the prompt and click **[!UICONTROL Add to Processing Profile]**. For details, see [Apply AI metadata using processing profiles](/help/assets/brand-aware-metadata.md#apply-ai-metadata-at-scale).
1. Open the `WKND alt text` prompt, confirm that the brand prompt is selected, and click **[!UICONTROL Generate preview output]** for Asset A. You have not changed the property prompt.

<!-- TODO: verify. Confirm the exact control used to associate a brand prompt with a processing profile, and add a screenshot. -->

**Example output:** "Three skiers on climbing skins trek along a snowy ridgeline at sunrise, wearing avalanche packs."

**Checkpoint, same prompt, now on brand:** The hype is gone. The caption is plain and specific, and it mentions the gear that matters. The property prompt did not change. The brand prompt did the work.

>[!VIDEO](https://video.tv.adobe.com/v/3508330)

>[!TIP]
>
>To see exactly what BAM sends to the model, click the more options (**...**) icon in the prompt playground for any of the preview assets and select **[!UICONTROL View prompt]**. The brand prompt is prepended to the property prompt, and the file name and file path are included by default.

## Step 8: Constrain a field with controlled vocabulary {#constrain-with-controlled-vocabulary}

For a governed field, such as a tag or dropdown field, bind the prompt to a controlled vocabulary, so that BAM selects only from your approved values rather than generating free text. Free text does not match your taxonomy and breaks faceted search and reporting. BAM matches each generated value to the value stored in AEM for you.

Start with as little definition as possible. Then run the prompt to learn how much help the model actually needs.

1. Click **[!UICONTROL Create prompt]** and configure the following fields:
   * **[!UICONTROL Prompt name]**: `WKND Activity Type`
   * **[!UICONTROL Group]**: `WKND`
   * **[!UICONTROL Metadata form]**: `WKND`
   * **[!UICONTROL Metadata property]**: `wknd:activity`

   Because `Activity type` is a tag field, the editor displays the controlled vocabulary builder with a tag selector instead of a free-text output.
1. Select whether the property returns a **single value** or **multiple values**. For this example, select a single value.

   As a best practice, select Multiple values only in case of tags. Multiple values is not a recommended option for a dropdown field. 

1. Add the approved values. The tag selector shows only the tags under the root path that you configured in [Step 3](#add-activity-type-field). Select the leaf tags under `Snow Sports`, `Climbing`, `Water Sports`, `Cycling`, and `Camp & Trek`. Select the option to return **Bottom-level tags only**, so that BAM does not return a category tag such as `Snow Sports`. You can also click **Add all** to add all tags created under **Activity**.
1. Leave the value definitions empty for now. In the **Additional text to append** field, specify:

   ```
   Select the activity shown in this image.
   ```

   The **Controlled vocabulary** field displays the values based on what you specify in the **Additional text to append** field and what tag values you select in the Value Definitions section.  

1. In **[!UICONTROL Prompt Playground]**, select Asset A and Asset B, then click **[!UICONTROL Generate preview output]**.

   A highlighted result in the preview indicates a value that matches the controlled vocabulary. A value that is not highlighted is free text and not the values that match the defined controlled vocabulary.
1. Click **[!UICONTROL Save]**.

**Example output:** Asset A returns **Backcountry Skiing**, a valid WKND value with no additional guidance. 

Asset B returns **Snowboarding**. It is close but not what WKND wants. The image shows a rider carving down a powder slope, and a split snowboard looks like any other snowboard from this angle. The pixels do not contain the answer.

**Checkpoint, pixels alone hit a ceiling:** For Asset B, the model chose a valid and reasonable value, but not the value that WKND wants. A split snowboard looks like any other snowboard from this angle. Describing the image in more detail does not fix this, because the missing information is not in the image.

>[!VIDEO](https://video.tv.adobe.com/v/3508331)

>[!IMPORTANT]
>
>* If you add new tags or dropdown options later, add them to the prompt's controlled vocabulary as well. Existing prompts do not pick up new values automatically.
>* A metadata property can use either generative output or controlled vocabulary, not both.

## Step 9: Add context with referenced properties {#add-referenced-properties}

BAM runs after all other metadata extraction is complete. By the time BAM runs, the asset already carries embedded metadata, such as fields set in [!DNL Adobe Bridge], and metadata written by upstream systems, such as [!DNL Workfront]. Every WKND shoot starts as a [!DNL Workfront] project, so each asset arrives with the `wknd:shootBrief` property. A referenced property lets a prompt read that existing metadata.

### Refine the Activity type prompt {#refine-activity-type}

1. Open the `WKND Activity Type` prompt.
1. In the **[!UICONTROL Referenced properties]** field, type `wknd:shootBrief`. Enter the exact property name used in **[!UICONTROL Map to property]**. You can reference a property even if it does not appear on the metadata form.
1. Specify the following in the **Additional text to append** field:

   ```
   Select the activity shown in this image.
   Use the shoot brief as a supporting signal when the image alone is
   ambiguous. If the brief and the image disagree, trust the image.
   ```

1. The model can still confuse two adjacent values, so add a short definition to only the value that needs it. In the controlled vocabulary, add the following value definition for **Splitboarding**. There is a separate text box adjacent to each controlled vocabulary option, the Value Definition that defines when to prefer any particular option over another in case of a confusion.

   ```
   Backcountry snowboarding on a board that splits into two skis for the
   climb. Choose this when the shoot brief mentions a splitboard.
   ```

   Write definitions that explain how similar values differ, rather than repeating general context.
1. In **[!UICONTROL Prompt Playground]**, select Asset B and click **[!UICONTROL Generate preview output]**.
1. Click **[!UICONTROL Save]**.

**Example output:** Asset B returns **Splitboarding**.

>[!TIP]
>
>You can also click **[!UICONTROL Suggest enhancements]** to improve value definitions, not only the main prompt.

### Create the Region prompt {#create-region-prompt}

1. Click **[!UICONTROL Create prompt]** and configure the following fields:
   * **[!UICONTROL Prompt name]**: `WKND Region`
   * **[!UICONTROL Group]**: `WKND`
   * **[!UICONTROL Metadata form]**: `WKND`
   * **[!UICONTROL Metadata property]**: `wknd:region`
   * **[!UICONTROL Referenced properties]**: `wknd:shootBrief`
1. Select a single value, and add all eight regions from the dropdown.
1. In the prompt field, enter:

   ```
   Select the region where this image was taken.
   Use the location in the shoot brief. Choose only from the available
   regions. If the brief gives no usable location, leave the field empty.
   ```

1. In **[!UICONTROL Prompt Playground]**, select Asset A and Asset B, then click **[!UICONTROL Generate preview output]**.
1. Click **[!UICONTROL Save]**, and add the prompt to the `WKND Winter Backcountry 2027` processing profile.

**Example output:**

* Asset A: **European Alps**, because the brief mentions the Mont Blanc massif.
* Asset B: **Rocky Mountains**, because the brief mentions the Teton Range, Wyoming.

**Checkpoint, business context, not pixels:** No image contains the words "Mont Blanc" or "Teton Range," and a generic tagger cannot produce a region at all. BAM read both the pixels and the shoot brief, then mapped a place name to WKND's own region list.

>[!VIDEO](https://video.tv.adobe.com/v/3508332)

>[!TIP]
>
>Treat referenced values as a supporting signal, not as the single source of truth. This matters most when the referenced data was itself generated by AI or is outside your control. The instruction "If the brief and the image disagree, trust the image" prevents an incorrect upstream value from overriding what is visible.

## Step 10: Derive the campaign from folder context {#derive-campaign}

The campaign is not in the image or in the file name. It comes from the brand prompt that is tied to the folder through the processing profile.

1. Click **[!UICONTROL Create prompt]** and configure the following fields:
   * **[!UICONTROL Prompt name]**: `WKND Campaign`
   * **[!UICONTROL Group]**: `WKND`
   * **[!UICONTROL Metadata form]**: `Wknd`
   * **[!UICONTROL Metadata property]**: `wknd:campaign`
1. Select a single value, and add the four campaigns from the dropdown.
1. In the **Additional text to append** field, specify:

   ```
   Select the campaign this asset supports. Use the campaign described in
   the brand context. If the asset doesn't fit it, select
   "Everyday Explorer (evergreen)".
   ```

1. In **[!UICONTROL Prompt Playground]**, select Asset A and Asset B, then click **[!UICONTROL Generate preview output]**.
1. Click **[!UICONTROL Save]**, and add the prompt to the `WKND Winter Backcountry 2027` processing profile.

**Example output:** **Winter Backcountry 2027** for both assets.

**Checkpoint, context that lives in the folder:** If you put similar assets in a `summer-surf-camps-2027` folder whose processing profile has its own brand prompt, the same campaign prompt returns a different response.

>[!VIDEO](https://video.tv.adobe.com/v/3508343)

## Step 11: Validate on a sample, then scale {#validate-and-scale}

Generating metadata at scale is only as trustworthy as your review process. Do not go straight from a working prototype to your whole library. Build a quality gate first.

1. Confirm that the brand prompt and the four property prompts (`WKND alt text`, `WKND activity type`, `WKND region`, and `WKND campaign`) are associated with the `WKND Winter Backcountry 2027` processing profile.
1. **Start with a small, representative sample.** Select about 20 existing assets in the folder, then click **[!UICONTROL Reprocess Assets]**. For details, see [Apply BAM to existing assets](/help/assets/brand-aware-metadata.md#apply-bam-to-existing-assets).
1. Upload one new asset to the folder, and verify that it is processed automatically with the same profile.
1. Open a processed asset, click **[!UICONTROL Properties]**, and review the values on the `WKND` tab.
1. In **[!UICONTROL Prompt Editor]**, open the quality report. Filter by date range and by lower confidence, so that you spot-check the assets the model was least sure about instead of reviewing every asset.
1. Refine the prompts if required, and repeat the sample run.
1. Get organizational sign-off. Treat approval of AI usage as a planned step, because it is frequently the real gate on going live. Start with the fields you are most confident in, and expand from there.
1. Reprocess the rest of the folder.

<!-- TODO: verify. Confirm the quality report label, location, and filter names, and add a screenshot. -->

>[!NOTE]
>
>* Quality report data is updated overnight and includes assets processed the previous day.
>* Processing overwrites existing values in the target properties. To keep existing values in a multi-value field, see [Additional best practices](#additional-best-practices).
>* Playground output sets your expectation for production. If a production run behaves differently from the playground, stop and reconcile the difference before you scale.

## Compare the results {#compare-results}

The following table compares Asset A before and after BAM:

| Property | Manual or generic tagging | BAM with WKND context |
|---|---|---|
| Alt text | "Skiing on a snowy mountain," or a caption full of hype words. | "Three skiers on climbing skins trek along a snowy ridgeline at sunrise, wearing avalanche packs." |
| Activity type | "Skiing," which is not a WKND value. | **Backcountry Skiing** |
| Region | Cannot be determined from pixels. | **European Alps** |
| Campaign | Cannot be determined from pixels. | **Winter Backcountry 2027** |
| Effort per asset | Several minutes by hand. | One configured prompt set, reused for every asset. |

In summary:

* **One plain-language prompt per property replaces manual tagging for every asset.** You wrote each prompt once, tested it in Prompt Playground, tightened it with Prompt Enhancer, and reused it across the folder.
* **The output is business context, not only a description of pixels.** The brand prompt supplied WKND's voice and campaign. The controlled vocabulary kept values within WKND's taxonomy. The referenced property supplied the location and the niche activity that no image could show.

## Additional best practices {#additional-best-practices}

* **Organize prompts around the property, not individual values.** Avoid value-centric rules, such as "if the product is a dress, tag it dress." Write one prompt per property and express when each value applies through controlled vocabulary definitions. This approach keeps your prompt library manageable and helps the model distinguish adjacent values, such as a coat and a jacket.
* **Append values by referencing the property itself.** BAM overwrites target properties by default. To add to a multi-value field, such as keywords or tags, reference the target property in the prompt and instruct the model to return the existing values plus the new ones.
* **Weigh the credit cost of deterministic fields.** Some values are derivable from a rule, such as extracting a product code from a file name, mapping a folder path to a region, or applying a constant value. BAM can generate these values, but each generation consumes credits. Use BAM when the convenience of staying in the product outweighs the cost, and be mindful of large batches.
* **Iterate before you scale.** Test in Prompt Playground, enhance, test again, then move to a small sample of real assets. Treat Prompt Playground as a mandatory first step, not an optional convenience.

## Related articles {#related-articles}

* [Generate Brand Aware Metadata](/help/assets/brand-aware-metadata.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Administering tags](/help/sites-cloud/administering/tags.md)
* [Use asset microservices and processing profiles](/help/assets/asset-microservices-configure-and-use.md)
* [Smart Tags](/help/assets/smart-tags.md)
