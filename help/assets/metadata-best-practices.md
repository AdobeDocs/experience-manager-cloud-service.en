---
title: Metadata best practices: Plan, build, and govern
description: Plan, build, and govern metadata in AEM Assets with action-oriented best practices, whether you are starting from scratch or bringing assets from another system including Brand-Aware Metadata.
role: User, Admin
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: d90519df-55a6-4e23-81ad-ff2365d71c0d
feature: Metadata, Best Practices
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---
<!--
 Keywords to focus on:
metadata best practices
aem metadata 
experience manager metadata
-->

# Metadata best practices: Plan, build, and govern {#metadata-best-practices-guide}

Metadata is the structured information that describes every digital asset, such as images, videos, graphics, and documents. It is what makes assets discoverable, retrievable, governable, and reusable at scale.

Metadata does more than describe a file. It captures business context, records how and where an asset is intended to be used, and connects assets to the campaigns, products, and regions they support. People can often infer this context by looking at an asset. AI features and agents cannot. They rely on accurate, consistent metadata to find the right asset, understand what it is for, and make correct decisions about it.

Many organizations start with little or no structured metadata, while others bring inconsistent metadata from a previous system. In either case, a model that is planned up front and enforced over time keeps your repository searchable as it grows. A model that is added as an afterthought produces inconsistent values, cluttered forms, and assets that nobody can find.

This article walks you through the metadata journey in [!DNL Experience Manager Assets] in the order you perform it:

* **[Plan your metadata model](#plan-your-metadata-model):** decide what metadata you need, how it maps from your current system, and who governs it.
* **[Build and maintain your metadata](#build-maintain-your-metadata):** build that model in [!DNL Experience Manager Assets], populate it automatically and in bulk, and keep it accurate over time.

Each best practice lists the exact actions to perform. Where [!DNL Brand-Aware Metadata] (BAM) can achieve the same outcome with AI, a **Brand-Aware Metadata** note links to the corresponding step in [Brand-Aware Metadata best practices](/help/assets/brand-aware-metadata-best-practices.md).

## Best practices at a glance {#best-practices-at-a-glance}

| # | Best practice | Phase |
|---|---|---|
| 1 | [Agree on why you need metadata, and who it serves](#define-strategy) | Plan your metadata model|
| 2 | [How will your users search? Build your fields from that](#design-fields-from-search) | Plan your metadata model|
| 3 | [Decide what users edit, only see, or never see](#classify-and-group-fields) | Plan your metadata model|
| 4 | [Map every legacy property before you move it](#map-legacy-properties) | Plan your metadata model|
| 5 | [Replace free text with controlled vocabularies](#define-controlled-vocabularies) | Plan your metadata model|
| 6 | [Who owns your metadata? Set up governance](#set-up-governance) | Plan your metadata model|
| 7 | [Build your tag taxonomy](#build-tag-taxonomy) | Build and maintain your metadata|
| 8 | [Build and apply a custom metadata schema](#build-metadata-schema) | Build and maintain your metadata|
| 9 | [Apply metadata at ingestion](#apply-metadata-at-ingestion) | Build and maintain your metadata|
| 10 | [Generate metadata with AI](#generate-metadata-with-ai) | Build and maintain your metadata|
| 11 | [Update metadata in bulk](#update-metadata-in-bulk) | Build and maintain your metadata|
| 12 | [Improve searchability](#improve-searchability) | Build and maintain your metadata|
| 13 | [Validate, share, and review metadata](#validate-share-review) | Build and maintain your metadata|

## Metadata fundamentals {#metadata-fundamentals}

Metadata records the defining attributes of each asset, such as its name, type, location in the repository, modified date, and associated tags. Together, these fields turn an unstructured collection of files into an organized, searchable library. Effective metadata management:

* **Streamlines asset management**, because consistently described assets are located and organized faster than by browsing folders.
* **Improves searchability and accessibility**, because descriptive tags and standardized fields let users retrieve the exact asset they need and avoid duplicate work.
* **Supports version control**, because modified dates and status fields make it clear which version of an asset is current.

Apply metadata at the point of ingestion rather than after you have your assets available within AEM Assets. Metadata applied at upload keeps the library accurate and reduces the effort required to maintain it over time.

Metadata falls into three categories. Use them later to [group your fields](#classify-and-group-fields).

| Type | What it describes | Examples | How it is typically populated in [!DNL Experience Manager Assets] |
|---|---|---|---|
| **Technical** | The intrinsic characteristics of the file that systems need to store, render, and process it. | File size, format (JPEG, PNG, TIFF, MP4, MOV), resolution (PPI or DPI), dimensions, color mode (RGB or CMYK). | Extracted automatically at upload from embedded XMP, IPTC, and Exif data. Users rarely edit these fields. |
| **Informational** (descriptive) | The meaning and context of the asset, which drives discovery and comprehension. | Title, description, caption, keywords, tags, subject classification. For example, a product launch video with the keywords *Marketing*, *Product launch*, and *Promo*, and the caption "Introducing our latest product." | Entered by users, set by rules, or generated by Smart Tags and [!DNL Brand-Aware Metadata]. |
| **Administrative** | The operational and governance information needed to manage the asset over its lifecycle. | Owner or rights holder, usage rights and licensing, expiration date, permissions, version history, audit details. | Entered by users or synced from upstream systems, such as a rights management or work management system. |

For details about metadata standards, encoding, and how [!DNL Experience Manager] stores metadata, see [Manage metadata of your digital assets](/help/assets/manage-metadata.md).

## Plan your metadata model {#plan-your-metadata-model}

Settle these six decisions before you move any assets. Each one is easy to implement earlier in the metadata management process but really expensive to fix after you start building your metadata in AEM.

### 1. Agree on why you need metadata, and who it serves {#define-strategy}

* **Set objectives and purpose:** write the result you expect, such as "Marketers find approved campaign images in under a minute," and why each field earns its place.
* **Plan access:** list who uses the metadata and where, such as the Admin view, Assets view, Content Hub, or a downstream system through an API.
* **Map the content journey:** from brief to expiry, note which metadata is created at each stage, by whom, and in which system.
* **Bring stakeholders in early:** get top-down sponsorship from creative, marketing, legal, localization, and IT, and keep them updated on objectives, progress, milestones, and challenges.

>[!TIP]
>
>**With Brand-Aware Metadata:** While you plan properties for your metadata schema, evaluate if those properties can be automatically generated using Brand-Aware Metadata. Start with one property and a short, plain-language prompt. Do not try to populate several fields from one prompt. For more information, see [Create a property prompt and test it in Prompt Playground](brand-aware-metadata-best-practices.md#create-property-prompt).

### 2. How will your users search? Build your fields from that {#design-fields-from-search}

* **Work backward from filters:** a request such as "approved spring campaign images for EMEA" gives you the *Status*, *Campaign*, and *Region* fields.
* **Export and audit what you have:** for each property, check whether it is populated, searched on, or duplicated. For assets already in [!DNL Experience Manager Assets], use [Export metadata](/help/assets/metadata-import-export.md#export-metadata).
* **Merge duplicates:** combine properties that store the same thing, such as *Photographer*, *Creator*, and *Shot by*.
* **Keep forms short:** keep only the fields users need, and list unneeded default properties to remove in [practice 8](#build-metadata-schema). Short forms get filled in accurately.

>[!TIP]
>
>**With Brand-Aware Metadata:** After evaluating what fields you can automatically generate using Brand-aware metadata, tie those property fields to brand prompts. Brand prompt provides higher-level context, such as voice, global rules, naming conventions, or campaign details. The properties that you generate have the higher-level context during generation ensuring more accuracy and hence enhanced search. For more information, see [Add global context with a brand prompt](brand-aware-metadata-best-practices.md#add-brand-prompt).

### 3. Decide what users edit, only see, or never see {#classify-and-group-fields}

* **Editable:** users provide or correct the value. Prefer a dropdown or tags field.
* **Read-only:** a system, rule, integration, or AI sets the value, such as *Legacy IDs* or dimensions. Select **[!UICONTROL Disable Edit]** on the field.
* **Hidden:** only systems need the value. Store it on the asset, but leave it off the form.
* **Group into future tabs:** sort fields into informational, technical, and administrative groups, such as *Brand*, *Technical*, and *Rights*, as described in [Metadata fundamentals](#metadata-fundamentals).


### 4. Map every legacy property before you move it {#map-legacy-properties}

* **Build a mapping sheet:** for each target property, record the source property, transformation, and source system, such as a PIM or [!DNL Adobe Workfront]. This lineage helps auditing and troubleshooting.
* **Define merge and split rules:** *Shot by* and *Photographer* merge into `dc:creator`, and a *Location* of `Chamonix, France` splits into *City* and *Country*.
* **Keep legacy IDs searchable:** combine old ID fields into one read-only *Legacy IDs* field.
* **Use standards first:** map common fields to [!DNL Dublin Core], IPTC, and XMP properties. Put everything else in your own namespace, such as `wknd:`, and avoid [reserved namespaces](/help/assets/metadata-schemas.md#reserved-namespaces). See [Encoding standards](/help/assets/manage-metadata.md#encoding-standards).

>[!TIP]
>
>**With Brand-Aware Metadata:** Various properties, such as a shoot brief used in the BAM tutorial, can give BAM context that the image alone lacks and can be of good value while automatically generating properties. See [Add context with referenced properties](/help/assets/brand-aware-metadata-best-practices.md#add-referenced-properties).

### 5. Replace free text with controlled vocabularies {#define-controlled-vocabularies}

* **Pick a control for each editable field:** use tags for hierarchical or shared values, a dropdown for a short flat list, and rules for values derived from a file name or folder path. Use free text only for values unique to each asset, such as a description.
* **Write the approved values:** give each value a one-line definition of when it applies and how it differs from similar values.
* **Scope and deduplicate:** each field offers only its own values, and each concept has exactly one term, not *Snowboard*, *snow-board*, and *Snowboarding*.
* **Set naming conventions:** prefer descriptive names, such as `product_launch`, over sequential names, such as `campaign_image_001`.

>[!TIP]
>
>**With Brand-Aware Metadata:** Your value definitions become BAM's controlled vocabulary definitions. See [Constrain a field with controlled vocabulary](/help/assets/brand-aware-metadata-best-practices.md#constrain-with-controlled-vocabulary). When you generate values for the fields with controlled vocabularies using BAM, it automatically tries to ensure that one of the defined values gets assigned to the field.

### 6. Who owns your metadata? Set up governance {#set-up-governance}

* **Write the rules:** define who can create fields, tags, and dropdown values, and how changes are requested and approved.
* **Set quality standards:** define required fields, accepted formats, such as dates, and a target completeness rate.
* **Assign owners:** name an owner for each property and vocabulary, and designate the system of record for shared properties.
* **Plan permissions and reviews:** decide who can edit schemas, tags, and metadata (see [permissions](/help/assets/metadata-schemas.md#Permissions-required-to-edit-metadata-schemas)), and schedule reviews as in [practice 13](#validate-share-review).

>[!TIP]
>
>**With Brand-Aware Metadata:** Decide who approves AI usage, who maintains prompts, and how generated values are spot-checked. See [Validate on a sample, then scale](/help/assets/brand-aware-metadata-best-practices.md#validate-and-scale).

## Build and maintain your metadata {#build-maintain-your-metadata}

Use these practices to turn your plan into configuration in [!DNL Experience Manager Assets], then populate and maintain the metadata. Ideally, configure practices 7 to 9 before you bulk-ingest assets, so that the assets are processed against the final model.

### 7. Build your tag taxonomy {#build-tag-taxonomy}

Tags implement your controlled vocabularies and are managed centrally through the [AEM Tagging Framework](/help/implementing/developing/introduction/tagging-framework.md).

**Actions:**

1. Go to **[!UICONTROL Tools]** > **[!UICONTROL General]** > **[!UICONTROL Tagging]**.
1. Click **[!UICONTROL Create]** > **[!UICONTROL Create Namespace]**, and create a namespace for your organization, for example, `wknd`.
1. Within the namespace, create one parent tag per tags field, for example, `activity`.
1. Under each parent tag, create the category and value tags from [practice 5](#define-controlled-vocabularies). Use the one-line definitions as tag descriptions.

For detailed steps, see [Creating new tags](/help/sites-cloud/administering/tags.md#creating-new-tags). To manage tags from the Assets view, see [Manage tags in Assets view](/help/assets/tagging-management-assets-view.md).

>[!VIDEO](https://video.tv.adobe.com/v/3508353)


### 8. Build and apply a custom metadata schema {#build-metadata-schema}

A custom metadata schema defines the fields on the asset [!UICONTROL Properties] page. It turns the fields, groups, and controls from your plan into a form that users can complete quickly and accurately.

**Actions:**

1. **Create the schema.**
   1. Go to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Schemas]**.
   1. Select the `default` form, click **[!UICONTROL Copy]**, and enter a name for your schema, for example, `wknd`.
   1. Select the new schema, and click **[!UICONTROL Edit]**.
1. **Create a tab for each group.** Click `+` to add a tab, and rename it in the **[!UICONTROL Settings]** tab with a group name from [practice 3](#classify-and-group-fields). Delete or rename the default **[!UICONTROL Basic]** and **[!UICONTROL Advanced]** tabs if they do not fit your model, and remove the irrelevant default fields that you identified in [practice 2](#design-fields-from-search). See [Add or delete a tab in the schema form](/help/assets/metadata-schemas.md#add-delete-a-tab-in-the-schema-form).
1. **Add a component for each field.** From the **[!UICONTROL Build Form]** tab, drag the component that matches the control type you chose in [practice 5](#define-controlled-vocabularies):
   * **[!UICONTROL Standard Tags]** for tags fields. In **[!UICONTROL Settings]**, set the root path to the parent tag, for example, `/content/cq:tags/wknd/activity`, so that the field shows only its own values.
   * **[!UICONTROL Dropdown]** for short, flat lists. Add each value under **[!UICONTROL Choices]**.
   * **[!UICONTROL Single Line Text]** or **[!UICONTROL Multi Value Text]** for free text.
   * **[!UICONTROL Date]** or **[!UICONTROL Number]** for dates and numeric values.
1. **Configure each component** in the **[!UICONTROL Settings]** tab:
   * **[!UICONTROL Field Label]:** the name that users see.
   * **[!UICONTROL Map to property]:** the property from your mapping sheet, for example, `./jcr:content/metadata/wknd:region`. Map only one field to a given property. See [Adding and mapping a custom metadata field](/help/assets/metadata-schemas.md#adding-and-mapping-a-custom-metadata-field).
   * **[!UICONTROL Disable Edit]:** select it for every read-only field from [practice 3](#classify-and-group-fields), such as *Legacy IDs*.
   * **[!UICONTROL Required]:** select it for every field that your quality standards require. See [Defining mandatory metadata](/help/assets/metadata-schemas.md#defining-mandatory-metadata).
   * **[!UICONTROL Description]** and **[!UICONTROL Placeholder]:** add short guidance that tells users what to enter.
1. **Add conditional fields where needed.** Show fields or values only when they apply, for example, codec and duration fields only for videos, or city values based on the selected country. See [Cascading metadata](/help/assets/cascading-metadata.md).
1. Click **[!UICONTROL Save]**.
1. **Apply the schema to folders.** Select the schema, click **[!UICONTROL Apply to Folders]**, select the top-level folder, and click **[!UICONTROL Apply]**. Subfolders inherit the schema unless a different schema is applied to them. See [Apply folder-specific metadata](/help/assets/metadata-schemas.md#applying-folder-specific-metadata).
1. **Verify the form.** Open an asset in the folder, click **[!UICONTROL Properties]**, and confirm that the tabs and fields appear as planned.

For all components and settings, see [Metadata schemas](/help/assets/metadata-schemas.md). To describe folders rather than assets, see [Folder metadata schema](/help/assets/folder-metadata-schema.md).

>[!VIDEO](https://video.tv.adobe.com/v/3508354)

### 9. Apply metadata at ingestion {#apply-metadata-at-ingestion}

Metadata applied automatically at upload is complete and consistent from day one, and it removes repetitive manual entry. Use metadata profiles for default values and processing profiles for computed metadata.

**Actions:**

1. **Set default values with a metadata profile.**
   1. Go to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Profiles]**, and click **[!UICONTROL Create]**.
   1. Enter a title, for example, `WKND winter defaults`, and click **[!UICONTROL Submit]**.
   1. Add a component for each property that shares a value across the folder, for example, the rights holder or campaign. Set **[!UICONTROL Map to property]** and **[!UICONTROL Default Value]**.
   1. Click **[!UICONTROL Done]**, then apply the profile to the folder.

   See [Metadata profiles](/help/assets/metadata-profiles.md).

1. **Generate metadata with a processing profile.**
   1. Go to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Processing Profiles]**, and create a profile.
   1. Add the metadata tasks you need, and use MIME type filters so that each task runs only on the right file formats.
   1. Apply the profile to the folder. Only one processing profile can be applied to a folder, so add all tasks for that folder to the same profile.

   See [Custom metadata using processing profile](/help/assets/manage-metadata.md#metadata-compute-service) and [Use processing profiles to process assets](/help/assets/asset-microservices-configure-and-use.md#use-profiles).

1. **Test with a few uploads.** Upload sample assets to the folder and confirm that the default and generated values appear on the [!UICONTROL Properties] page.


### 10. Generate metadata with AI {#generate-metadata-with-ai}

AI removes most manual tagging. Smart Tags describe what is visible in an asset. [!DNL Brand-Aware Metadata] goes further and generates values in your own fields, in your brand's language, and from your controlled vocabularies.

**Actions:**

1. **Use Smart Tags for generic visual keywords.** Confirm that Smart Tags are enabled and that new uploads receive tags. See [Smart Tags](/help/assets/smart-tags.md).
1. **Block unwanted Smart Tags.** In the Assets view, go to **[!UICONTROL Settings]** > **[!UICONTROL Blocked Tags]**, click **[!UICONTROL Add blocked tag]**, enter the terms that must never be applied, such as competitor names or off-brand words, and click **[!UICONTROL Add]**. See [Add tags to blocklist](/help/assets/tagging-management-assets-view.md#blocklist-essentials).
1. **Moderate Smart Tags on key assets.** Remove inaccurate tags and promote the most relevant tags. See [Manage Smart Tags and asset searches](/help/assets/smart-tags.md#manage-smart-tags-and-searches).
1. **Use [!DNL Brand-Aware Metadata] for business fields.** For fields such as alt text, product category, activity type, region, or campaign, create one property prompt per field, add a brand prompt for shared context, constrain values with controlled vocabulary, and test in Prompt Playground before you process assets. See [Generate Brand-Aware Metadata](/help/assets/brand-aware-metadata.md).

>[!TIP]
>
>**With Brand-Aware Metadata:** Follow the complete journey from the first property prompt to folder-derived values:
>
>* [Create a property prompt and test it in Prompt Playground](/help/assets/brand-aware-metadata-best-practices.md#create-property-prompt)
>* [Refine the prompt with Prompt Enhancer](/help/assets/brand-aware-metadata-best-practices.md#refine-prompt-with-enhancer)
>* [Add global context with a brand prompt](/help/assets/brand-aware-metadata-best-practices.md#add-brand-prompt)
>* [Constrain a field with controlled vocabulary](/help/assets/brand-aware-metadata-best-practices.md#constrain-with-controlled-vocabulary)
>* [Add context with referenced properties](/help/assets/brand-aware-metadata-best-practices.md#add-referenced-properties)
>* [Derive the campaign from folder context](/help/assets/brand-aware-metadata-best-practices.md#derive-campaign)

### 11. Update metadata in bulk {#update-metadata-in-bulk}

Bulk updates record shared values uniformly across a set of assets and eliminate the variation that creeps in when values are entered one asset at a time.

**Actions:**

1. **Edit metadata for many assets at once.**
   1. Go to the folder or collection, and select the assets.
   1. Click **[!UICONTROL Properties]**. The page shows the fields that the selected assets have in common.
   1. Enter the shared values.
   1. To add values to multi-value fields without removing existing values, select **[!UICONTROL Append mode]**. Without it, new values replace existing values. Append mode does not apply to single-value fields.
   1. Click **[!UICONTROL Save & Close]**.

   See [Manage metadata of your digital assets](/help/assets/manage-metadata.md#manage-assets-metadata).

   >[!VIDEO](https://video.tv.adobe.com/v/3508355)

1. **Edit metadata for search results.** To update assets across folders that match common criteria, search for them first, then update the results. See [Bulk update metadata properties](/help/assets/search-assets.md#metadata-updates).
1. **Import metadata from a CSV file.** Use this method for values from your mapping sheet in [practice 4](#map-legacy-properties).
   1. In the Assets user interface, click **[!UICONTROL Create]** > **[!UICONTROL Metadata]**.
   1. Click **[!UICONTROL Select File]**, and select the CSV file.
   1. Set the batch size, field separator, multi-value delimiter, and asset path column name, then click **[!UICONTROL Import]**.
   1. Open a few assets and verify the imported values.

   Run large imports during low-usage periods. See [Import and export asset metadata in bulk](/help/assets/metadata-import-export.md).

1. **Check accuracy and completeness after each bulk update.** For example, verify that author names and keywords on a set of PDF documents are correct and complete.


### 12. Improve searchability {#improve-searchability}

Metadata delivers value only when users can search and filter on it. Prioritize the fields that directly support search and retrieval, and expose them where users search.

**Actions:**

1. **Elevate keywords for priority assets.** Boosted keywords make an asset appear at the top of results for those terms.
   1. Select the asset, and click **[!UICONTROL Properties]**.
   1. On the **[!UICONTROL Advanced]** tab, under **[!UICONTROL Elevate for search keywords]**, click **[!UICONTROL Add]**.
   1. Enter a keyword, and click **[!UICONTROL Add]**. Add more keywords and arrange them in order of priority.
   1. Click **[!UICONTROL Save & Close]**.
   1. Search with one of the keywords, and confirm that the asset appears among the top results.

      >[!VIDEO](https://video.tv.adobe.com/v/3508356)

   You must use the `default` metadata schema to elevate search keywords. See [Boost search in Experience Manager](https://experienceleague.adobe.com/docs/experience-manager-learn/assets/search-and-discovery/search-boost.html).

1. **Add search facets for your key fields.** Turn the filters from [practice 2](#design-fields-from-search) into filters in the search panel.
   1. Go to **[!UICONTROL Tools]** > **[!UICONTROL General]** > **[!UICONTROL Search Forms]**.
   1. Select **[!UICONTROL Assets Admin Search Rail]**, and click **[!UICONTROL Edit]**.
   1. Drag a predicate, such as a **[!UICONTROL Tags]** predicate or **[!UICONTROL Options]** predicate, to the form, and set its property name to your custom property, for example, `jcr:content/metadata/wknd:region`.
   1. Click **[!UICONTROL Done]**.

   See [Search facets](/help/assets/search-facets.md).

1. **Add custom fields for context-specific search.** If users need to search by criteria that standard fields do not cover, such as project details or copyright information, add a custom field to the schema as described in [practice 8](#build-metadata-schema). See [How to edit or add metadata](/help/assets/meta-edit.md).

For more ways to tune search, see [Search best practices](/help/assets/search-best-practices.md).

### 13. Validate, share, and review metadata {#validate-share-review}

Metadata quality degrades without ongoing attention, as new content types, campaigns, and teams arrive. Validate regularly, distribute responsibility across the content supply chain, and adapt the model to evolving business needs.

**Actions:**

1. **Find assets with missing required metadata.** In search, open the **[!UICONTROL Filters]** panel, expand **[!UICONTROL Metadata Validation]**, and select **[!UICONTROL Invalid]**. Assign the results to their owners for completion.
1. **Spot-check controlled values.** Export metadata for a folder and check that tags and dropdown fields contain only approved values. See [Export metadata](/help/assets/metadata-import-export.md#export-metadata).
1. **Share metadata responsibility across stages.** Capture metadata where it originates instead of asking a single team to enter it at upload. For example, integrate [!DNL Experience Manager Assets] with [!DNL Adobe Workfront] so that project details sync to linked assets and update automatically when they change in [!DNL Workfront]. See [Integration with Adobe Workfront](/help/assets/workfront-integrations.md).
1. **Track usage of each property.** Review which properties users fill in and filter on, and which they ignore. Prioritize the fields that contribute most to search and retrieval, and reconsider the rest.
1. **Review and update the model on a schedule.** At the cadence you defined in [practice 6](#set-up-governance), add, retire, or merge fields, update tags and dropdown values, and update form guidance. Communicate each change to stakeholders.

>[!TIP]
>
>**With Brand-Aware Metadata:** Before you scale AI generation, validate on a small sample, review the quality report, and get sign-off. When you add tags or dropdown values later, update the controlled vocabulary in each related prompt, because new values are not added to existing prompts automatically. See [Validate on a sample, then scale](/help/assets/brand-aware-metadata-best-practices.md#validate-and-scale) and [Constrain a field with controlled vocabulary](/help/assets/brand-aware-metadata-best-practices.md#constrain-with-controlled-vocabulary).

## Frequently asked questions {#frequently-asked-questions}

### How are custom fields bulk updated? {#custom-fields-bulk-update}

Admin View in Adobe Experience Manager Assets provides CSV metadata import and export for bulk updates to custom properties. Export metadata from the asset folder, edit the relevant property values, and import the CSV with the asset paths identifying the assets to update. Register custom namespaces before importing properties that use them. The CSV import supports a configurable multi-value delimiter, with a vertical bar as the default. This alternative uses Admin View rather than the standard Assets View bulk editor.

### Can reprocessing overwrite edited metadata? {#reprocessing-overwrite-edited-metadata}

Yes. Full or metadata-only reprocessing in Adobe Experience Manager Assets can overwrite manually edited properties when a metadata profile is reapplied or embedded XMP metadata is extracted again and updates the same properties. Review curated values such as Title, Description, and Alt Text before reprocessing. Assets View provides Advanced options to select the processing work required. Avoid unnecessary metadata extraction, and review selected processing profiles and post-processing workflows for additional metadata updates.

## Related articles {#related-articles}

* [Manage metadata of your digital assets](/help/assets/manage-metadata.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Metadata profiles](/help/assets/metadata-profiles.md)
* [Import and export asset metadata in bulk](/help/assets/metadata-import-export.md)
* [Cascading metadata](/help/assets/cascading-metadata.md)
* [Smart Tags](/help/assets/smart-tags.md)
* [Generate Brand-Aware Metadata](/help/assets/brand-aware-metadata.md)
* [Brand-Aware Metadata best practices](/help/assets/brand-aware-metadata-best-practices.md)
* [Search facets](/help/assets/search-facets.md)
* [Search best practices](/help/assets/search-best-practices.md)
* [Asset reports](/help/assets/asset-reports.md)
