---
title: Search assets in Content Hub
description: Learn how to search assets in [!DNL Content Hub]
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 8578d7d0-32b9-4e5c-80ef-3827e358ac6c
---
# Search Assets in [!DNL Content Hub] {#search-assets}

**[!DNL Content Hub] search enables you to quickly locate approved assets in your repository and act on them immediately.** When your repository holds a large number of assets, locating the right one manually is time-consuming and inefficient. [!DNL Content Hub] search solves this by surfacing **approved assets**, so you can perform additional actions on those assets without delay — including **downloading** them for reuse, **sharing** them with collaborators, and organizing them into **collections** for streamlined project workflows.

Efficient retrieval is central to any digital asset management workflow, because the faster relevant assets are found, the sooner they can be deployed across campaigns, publications, and creative projects.

## Search Capabilities in [!DNL Content Hub] {#search-capabilities-content-hub}

[!DNL Content Hub] search offers the following capabilities to narrow down and refine your results:

- **Text-based search** — Enter keywords to locate assets by name, description, or associated content, which helps you find matching assets even when you do not know the exact file name.
- **Filters** — Apply filter criteria to reduce a broad result set to the most relevant assets. This ensures you can drill down efficiently rather than scrolling through the entire repository.
- **Tags and smart tags search** — Search by manually applied tags or AI-generated smart tags. Smart tags automatically describe asset content, so you can discover relevant assets even when they were not manually labeled.
- **File format search** — Locate assets by their specific file format, which is useful when a task requires a particular type of file, such as an image, document, or video.

By combining these capabilities, you can pinpoint the exact approved asset you need and move directly to downloading, sharing, or building collections around it.

## Prerequisites {#prerequisites}

Only [**[!DNL Content Hub] users**](deploy-content-hub.md#onboard-content-hub-users) can perform the procedures and configuration actions described in this article. Users must first be onboarded with the appropriate [!DNL Content Hub] role, which grants the permissions required to complete these steps.

This access requirement ensures that only authorized users can perform the actions covered here, maintaining consistent governance over [!DNL Content Hub] operations. If you are unable to perform the actions in this article, confirm that you have been onboarded as a [!DNL Content Hub] user before proceeding.

## What you can search for  {#what-you-can-search}

[!DNL The Content Hub] search provides results based on: 

* **Matching text:** [!DNL The Content Hub] search allows you to search for an asset using its name or description. You can perform keyword-based search, which compares the keyword to the text available in the properties of an asset. This ensures that any asset whose name or descriptive fields contain the entered term is retrieved. 

* **Matching context:** [!DNL Content Hub] search results list contains proximate results of assets that you get based on the matching context. For example, if you type `cool` in the search bar, the assets related to `winter`, `snow`, `cold surroundings`, display in the search list. This contextual, meaning-based matching returns conceptually related assets even when the exact keyword does not appear in the asset properties. 

* **Asset information (title, tags, or smart tags):** [!DNL Content Hub] uses a smart search algorithm to rank search results as accurately and as relevantly as possible. **Metadata** is the collection of all data associated with an asset, though this data is not necessarily embedded within the asset file itself. [Metadata](#asset-properties.md) helps you further categorize assets and becomes increasingly valuable as the volume of digital information grows across a **Digital Asset Management (DAM)** system. [Learn more about configuring metadata search](/help/assets/configure-content-hub-ui-options.md##configure-metadata-search-content-hub). **Smart tags** are automatically generated descriptive labels that enrich this metadata, improving the precision of ranked results. 

* **Last modified date:** Assets modified most recently appear at the top of the search results list, ensuring the freshest content surfaces first. You can also filter by a **date range** according to your requirement, which lets you narrow results to a specific period. 

* **Usage:** The most commonly used assets appear at the top of the search list, because frequency of use signals relevance and helps you locate high-demand content faster.

* **Search history:** Click inside the search box without typing a character to view your search history. You can also remove any particular keyword from the history. The search history is saved in the **cache memory** of a web browser. As a result, if you access [!DNL Content Hub] search in a different browser or clear the browser cache, the search history is no longer available.

* **Search while you type:** [!DNL Content Hub] search provides **autocomplete suggestions** as you begin typing, which speeds up query entry, reduces spelling errors, and surfaces relevant assets before you finish typing.

## Basic search {#basic-search}

**Basic search** on [!DNL the Content Hub] lets you locate digital assets by entering a keyword and refining the results with filters. To perform a basic search, navigate to the search bar and specify the target keyword.

Navigate to the filters available in the left pane and apply them to narrow down the results. Filters restrict the result set to only the assets that match your selected criteria, because combining a keyword with attributes such as format and modification date returns a precise, relevant set of assets.

Common filter categories available in the left pane include:

- **[!UICONTROL Format]** — restrict results to a specific file type, such as **[!UICONTROL JPEG]**.
- **[!UICONTROL Modified]** — restrict results to assets changed within a specified date range.

### Example: Find JPEG images with the keyword "architect"

For example, search for all the **[!UICONTROL JPEG]** images with the keyword `architect` in them that were modified within the last year. Complete the following steps to execute this scenario:

1. Specify `architect` as the search keyword. This returns all assets whose metadata or content matches the keyword.

1. Navigate to the filters panel > **[!UICONTROL Format]** > select **[!UICONTROL JPEG]**. This limits the results to JPEG images only.

1. Navigate to **[!UICONTROL Modified]** > specify the date range covering the last year. This narrows the results to assets modified within that period, producing a focused set of JPEG images that match the keyword `architect`.

   ![Basic search](assets/basic-search.png)

## Narrow your search results using filters {#narrow-down-search-results}

The **Filters panel** searches for and narrows assets based on metadata, supporting **more than 10 predicates** at once and up to **40 fields** in the filter panel on the Search page. The Filters panel filters search results using metadata-based search predicates, allowing users to combine multiple criteria to pinpoint the exact assets they need.

Users select all applicable predicates to minimize or narrow down search results. Selecting more predicates produces a more targeted, precise result set.

### How filter logic works: within-filter vs across-filter

[!DNL Content Hub] applies two distinct matching rules depending on how selections are made:

- **Multiple options within a single filter (OR logic):** When you select multiple options within one filter, [!DNL Content Hub] displays the assets that match **any** of the options selected within that filter. This broadens the result set to include every asset satisfying at least one selected value.
- **Multiple options across different filters (AND logic):** When you select multiple options across filters, [!DNL Content Hub] displays **only** the assets that match **all** options selected across those filters. Because each additional filter must also be satisfied, combining filters progressively narrows the results.

This means adding options inside one filter widens results, while adding conditions across separate filters tightens them — giving users precise control over how broad or narrow the search becomes.

### Default filters

The default filters include:

- File format
- Approved by
- Date approved
- Expired and not expired assets
- Expiration date

Administrators can also configure which filters display in the list of filters. For more information, see [Configure [!DNL Content Hub] user interface](configure-content-hub-ui-options.md#configure-filters-content-hub).

### Filter display limits

>[!NOTE]
>
>A new filter displays on the Search page only if at least one asset in the repository matches the filter criteria. This ensures users see only filters that return usable results. The maximum number of fields available in the filter panel on the Search page is **40**.

## AI Search in [!DNL Content Hub] {#ai-search-aem-assets-content-hub}

AI Search in Adobe Experience Manager (AEM) Assets [!DNL Content Hub] is an advanced, intent-aware search capability that understands the meaning and intent behind a user's query rather than relying on exact keyword matches. AI Search uses artificial intelligence (AI) and machine learning to deliver more accurate and contextually relevant results, transforming how teams locate digital assets within large content libraries.

Unlike traditional keyword-based search, which looks for exact terms, AI Search interprets relationships between words, concepts, and user intent. As a result, users find what they are looking for—even when their query is phrased differently, contains typos, or is written in another language.

>[!IMPORTANT]
>
>If you require searching for assets using natural language with prompts such as, `find me approved jpeg assets about coffee`, Adobe recommends to use Content Discovery Agent. For more information on how to access the agent, sample prompts, and so on, see [Content Discovery Agent](/help/ai-in-aem/agents/content-advisor/discovery.md#use-cases-prompts).

### Key Benefits of AI Search

AI Search delivers the following key benefits:

* **Multilingual support**: Search across multiple languages without requiring exact translations. Users find relevant content regardless of the language in which they type their query, because AI Search matches concepts rather than literal words.

* **Handles misspellings**: Interprets typos and spelling errors and returns accurate results even with imperfect input, reducing failed searches caused by minor keystroke mistakes.

* **Understands synonyms**: Delivers results for related terms and phrases, so users do not need to guess the exact keyword. This surfaces relevant assets that a strict keyword match would otherwise miss.

* **Contextually relevant search**: Recognizes the intent behind a query, not just the exact words. This ensures that the most meaningful results rise to the top, matching what the user actually needs.

### Enabling AI Search

To enable AI Search, your environment must meet the minimum requirement:

* Minimum required AEM release version is **`25520`**.

>[!IMPORTANT]
>
>This feature is available as Limited Availability feature. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

AI Search is available for [!DNL Content Hub] environments that use the latest search stack. Adobe is rolling out the latest search stack to [!DNL Content Hub] customers in phases.

![AI Search in [!DNL Content Hub]](/help/assets/assets/ai-search-content-hub.png)

### Verifying the Latest Search Stack

To verify whether your environment uses the latest search stack, navigate to your user profile icon and click **Configurations** on [!DNL the Content Hub] User Interface. Select the **Search** tab. If you can see options to select **AI Search** or **Keyword**, then AI Search is available and your environment is running the latest search stack.

If AI Search is not yet available and you want to enable it, [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).

### Examples for AI Search in [!DNL Content Hub] {#examples-ai-search-aem-assets-content-hub}

**AI Search (Artificial Intelligence Search)** in Adobe Experience Manager (AEM) Assets [!DNL Content Hub] retrieves assets by **meaning and intent**, not just exact keyword matches. This **semantic matching** capability allows the search to understand synonyms, related concepts, alternative spellings, and even other languages, returning relevant assets that traditional metadata search would miss.

**Example Prompt**: *Woman drinking coffee*

#### How Traditional Keyword Search Works

Traditional keyword-based search looks for **exact matches** of asset metadata. For the prompt above, it searches for the literal terms **`Woman`**, **`drinking`**, and **`Coffee`**, and returns only assets whose metadata includes all of these exact terms. As a result, relevant images tagged with different but equivalent words are excluded.

#### How AI Search Works

Unlike traditional keyword-based search, **AI Search** interprets the meaning behind the prompt and matches **semantically similar words**. This ensures that assets are surfaced even when their metadata uses different vocabulary. For the prompt *Woman drinking coffee*, AI Search recognizes related terms such as:

- **`Girl`** and **`Lady`** as equivalents for **`Woman`**
- **`Cappuccino`** and **`Latte`** as equivalents for **`Coffee`**

Because AI Search evaluates conceptual similarity rather than literal string matches, it delivers broader, more relevant results and reduces the risk of overlooking suitable assets.

#### Cross-Language and Typo Tolerance

AI Search also supports **multilingual queries** and is resilient to spelling errors. You can enter the same prompt in **Spanish**, or misspell **`Woman`** as **`Wman`**, and still receive the same accurate results. This tolerance for language variation and typos makes AI Search significantly more forgiving and efficient than exact-match keyword search, streamlining asset discovery within [!DNL Content Hub].

### Enable or disable AI Search in [!DNL Content Hub] {#enable-disable-ai-search-content-hub}

Enabling or disabling AI Search in [!DNL Content Hub] uses the same procedure that verifies whether you are running the latest search stack for [!DNL Content Hub]. This means a single settings check both confirms your search stack version and controls which search mode is active.

[!DNL Content Hub] offers two selectable search modes:

- **[!UICONTROL AI Search]** — the AI-powered search experience, which represents the latest search stack for [!DNL Content Hub].
- **[!UICONTROL Keyword]** — the traditional keyword-based search, selected when AI Search is disabled.

   ![AI Search in [!DNL Content Hub]](/help/assets/assets/ai-search-content-hub.png)

Execute the following steps to enable or disable AI Search in [!DNL Content Hub]:

1. Navigate to your user profile icon and click **[!UICONTROL Configurations]**. This opens the configuration settings where search behavior is managed.

2. In the **[!UICONTROL Search]** tab, select **[!UICONTROL AI Search]** to enable AI Search for [!DNL Content Hub], or select **[!UICONTROL Keyword]** to disable it and revert to keyword-based search. Because both options appear in the same tab, this is also where you confirm which search stack is currently in use.

3. Click **[!UICONTROL Save]** to apply your selection. The chosen search mode takes effect for [!DNL Content Hub] after saving.

<!--

<table>
    <tbody>
     <tr>
      <th><strong>Search Predicate</strong></th>
      <th><strong>Description</strong></th>
      <th><strong>Properties</strong></th>
     </tr>
     <tr>
      <td> Campaigns </td>
      <td> Allows you to search using planned activity performed to take any particular action. For example, advertisement campaign run on Ferrari to know the understand the interests of people using number of clicks people perform.</td>
      <td>NA</td>
     </tr>
     <tr>
      <td> Channels </td>
      <td> Helps you to understand the path from where the asset is coming from. For example, web, social media, books, catalog, etc.</td>
      <td>NA</td>
     </tr>
     <tr>
      <td> Region </td>
      <td> Helps you to understand the location where the asset is created. For example, Japan, EMEA, Worldwide, etc.</td>
      <td>NA</td>
     </tr>
     <tr>
      <td> Keywords </td>
      <td> Keyword helps you search using terms or the words that you enter based on the topic. For example, images, low-resolution, etc.</td>
      <td>NA</td>
     </tr>
     <tr>
      <td> Timeframe </td>
      <td> Helps you search assets using timeline. For example, search by year 2024, Q3 2023, etc.</td>
      <td>NA</td>
     </tr>
     <tr>
      <td>File format</td>
      <td>Composition of an asset. The supported assets include image, document, video, printable media, and so on.</td>
      <td>
        <ul>
            <li>[!UICONTROL JPEG]</li> 
            <li>[!UICONTROL Quicktime]</li> 
            <li>[!UICONTROL PNG]</li> 
            <li>[!UICONTROL WebP]</li> 
            <li>[!UICONTROL MP4]</li> 
            <li>[!UICONTROL Plain]</li> 
            <li>[!UICONTROL PDF]</li>
            <li>[!UICONTROL SVG + XML]</li>
        </ul>
      </td>
     </tr>
     <tr>
      <td>Tags</td>
      <td>Tags help you categorize assets that can be browsed and searched more efficiently based on hierarchical taxonomies.</td>
      <td>
        <ul>
            <li>Field label</li>
            <li>Property name</li>
            <li>Path</li>
            <li>Description</li>
        </ul>
      </td>
     </tr>
     <tr>
      <td>Subject</td>
      <td>Classification of assets based on their theme. For example, colorful, hiking, outdoors.</td>
      <td>NA</td>
     </tr>
          <tr>
      <td>Last modified</td>
      <td>Search assets based on their last modification. Specify the date range using the Start date and End date fields.</td>
      <td>
        <ul>
            <li>Range text (From)</li> 
            <li>Range text (To) </li>
        </ul>
      </td>
     </tr>    
     <tr>
      <td>Asset ID</td>
      <td>Unique number that identifies the asset.</td>
      <td>NA</td>
     </tr>
     <tr>
      <td> Colors </td>
      <td> Helps you search assets using colors that are automatically identified in an asset using Adobe's AI capabilities.</td>
      <td>NA</td>
     </tr>  
    </tbody>
   </table>

-->

## Bulk search {#bulk-search}

**Bulk Search** in [!DNL Content Hub] lets you look up multiple assets simultaneously by entering a list of identifiers—such as names, file formats, colors, tags, and more—in a single query. Instead of searching assets one at a time, **Bulk Search** accelerates asset discovery by matching an entire list of values at once. This eliminates repetitive one-by-one lookups, so you retrieve every matching asset in a **single search** rather than running dozens of separate queries.

With this capability, you enter multiple values for any filter property—separated by a **delimiter** (for example, multiple SKU IDs)—and instantly retrieve all matching assets in one search operation.

### Supported delimiters

To search for multiple assets at once, enter multiple values in a single query by separating them with delimiters ` [ , | \t | \r | \n | \r\n ]`. You can also add more delimiters depending upon your use case, which is useful when your identifier lists are copied from spreadsheets or other tools that use different separators. See [Configure Bulk Search](configure-content-hub-ui-options.md#bulk-search-configuration).

### Steps to perform Bulk Search

To perform Bulk Search in [!DNL the Content Hub], execute the following steps:

1. Once Bulk Search is [configured](configure-content-hub-ui-options.md#bulk-search-configuration), the **Bulk Search** toggle appears on [!DNL the Content Hub] filter properties you configured. Enable or disable it based on your search needs.

   ![Bulk Search UI](assets/bulk-search-ui.png)

1. Add a search query containing the delimiters specified in the configuration. The search query should contain a string accompanied by multiple comma-separated values (for example, several SKU IDs separated by commas).

1. Run the search to instantly retrieve all assets that match any of the values in your query. Every matching asset is returned together in the results, allowing you to review, select, and act on the full set at once.

## Configure sorting in [!DNL Content Hub] {#configure-sorting-aem-assets-content-hub}

[!DNL Content Hub] in Adobe Experience Manager (AEM) provides out-of-the-box sorting options—default, built-in controls that let users organize asset search results without any additional setup. These standard options cover common ordering needs, such as arranging assets by name or by date.

Beyond these defaults, administrators enable **custom metadata fields** as sorting options, allowing users to sort assets based on business-specific metadata such as **Channel**, **Region**, **SKU (Stock Keeping Unit)**, or **Campaign**. Custom metadata fields are attributes defined by your organization to describe assets in ways that match how your teams actually work. Because different teams search and organize assets around different business dimensions, enabling metadata-based sorting lets each user surface the most relevant results faster—for example, marketers can order assets by campaign, while regional teams can group results by region. This reduces the time spent scrolling through unsorted results and streamlines asset discovery across large libraries.

### Prerequisites and enablement

To enable sorting in [!DNL Content Hub], confirm that your environment meets the minimum version requirement:

* **Minimum required AEM release version: `25520`.** Sorting configuration—including the ability to expose custom metadata fields as sorting options—requires this release or later. Verify your [!DNL Content Hub] environment is running AEM release version **`25520`** or newer before configuring sorting options.

Once this prerequisite is met, administrators can proceed to configure both the built-in sorting options and any custom metadata fields that align with their organization's business needs.

### Default sorting options {#default-sorting-options}

By default, [!DNL Content Hub] includes the following sorting options on [!DNL the Content Hub] home page:

* **Size** — orders assets by file size

* **Modified** — orders assets by their last-modified date

* **Name** — orders assets alphabetically by name

* **Relevance** — orders assets by their match to the active search query

>[!IMPORTANT]
>
>This feature is available as a **Limited Availability** feature, meaning access is granted on a phased, opt-in basis rather than being enabled for all deployments by default. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable this sorting feature for your deployment.

Sorting works in [!DNL Content Hub] environments that use the latest search stack. Adobe is rolling out the latest search stack to [!DNL Content Hub] customers in phases, so availability depends on where your deployment falls in that rollout.

To verify whether your deployment uses the latest search stack, follow these steps on [!DNL the Content Hub] User Interface:

1. Navigate to your **user profile icon**.

2. Click **Configurations**.

3. Select the **Search** tab.

4. Check for options to select **AI Search** or **Keyword**. If these options appear, **AI Search is available and your deployment is using the latest search stack**, because AI Search is only exposed on environments running the latest search stack.

![AI Search in [!DNL Content Hub]](/help/assets/assets/ai-search-content-hub.png)

If **AI Search** is not yet available and you want to enable it, [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).

### Add custom metadata fields as sorting options {#add-custom-metadata-fields-for-sorting}

**Administrators configure additional metadata fields to appear in the sorting menu**, extending the default sorting options with organization-specific criteria. This gives teams flexible control over how asset results are ordered, aligning the sort experience with the metadata that matters most to their workflows.

To enable a **metadata field** for sorting:

1. Click the user profile icon and select **Configurations**.
1. Navigate to the **Filters** tab.
1. Locate the metadata field that you want to enable for sorting.
1. Click the edit icon available for that particular metadata field.
1. In the Edit Filter dialog, enable the **Sorting** option.
1. Click **Confirm** and save the configuration. The updates take effect when the **Status** field value for the metadata field is displayed as `Active`, confirming the field is live and available in the sorting menu.

   ![Basic search](assets/enable-filters-sorting.png)

For example, enabling sorting for the **Channel** metadata field allows users to sort asset results using the **Channel** value. This makes it faster to group, browse, and retrieve assets by channel, improving discoverability and streamlining asset management for large libraries.

### Use custom sorting options on [!DNL the Content Hub] home page {#use-custom-sorting-options}

After you enable sorting for a metadata field, that field immediately becomes available as a sorting option on the **[!DNL Content Hub] home page**. Specifically:

* The enabled field appears in the **sorting menu** on [!DNL the Content Hub] home page.
* **Custom sorting fields** are displayed below a **separator line** in the sorting menu.
* The separator visually differentiates administrator-configured custom fields from the default, out-of-the-box sorting options, because grouping the two categories prevents confusion between system defaults and organization-specific configurations.

For example, if the **Channel** metadata field is enabled for sorting, the sorting menu displays:

* Default fields such as **Size**, **Modified**, **Name**, and **Relevance**
* A separator line
* The custom field **Channel**

![Basic search](assets/custom-sorting-options.png)

In this layout, the standard fields remain in their familiar positions at the top, while the administrator-defined **Channel** field is grouped below the separator, giving users a predictable place to look for organization-specific sorting criteria.

As a result, users can quickly distinguish standard sorting options from organization-specific, metadata-based sorting options, which reduces the time spent locating the correct sort criteria and streamlines how content is browsed and prioritized on [!DNL the Content Hub] home page.

## Do more with search {#do-more-with-search}

[!DNL The Content Hub] extends beyond search: it lets users act on assets directly from the search or preview interface, without switching to a separate screen. From your search results, you can:

- **[Download](download-assets-content-hub.md)** assets directly to your device.
- **[Share](share-assets-content-hub.md)** assets with collaborators or stakeholders.
- **[Add assets to a collection](collections-content-hub.md)** to organize and group related items.

Because these actions are available in-context, users complete common tasks without leaving the search or preview interface, streamlining the asset workflow. Select one or more assets on the search results page to reveal these options.

Learn more about [configuring assets in [!DNL the Content Hub]](configure-content-hub-ui-options.md).

## Frequently asked questions {#faqs-deploy-content-hub}

### How can I narrow down my search results in AEM Assets [!DNL Content Hub]?

You can narrow down search results in **Adobe Experience Manager (AEM) Assets [!DNL Content Hub]** by combining **text-based search**, **filters**, **tags and smart tags**, and the **filters panel**. [!DNL Content Hub] is a digital asset management (DAM) interface built to help teams quickly locate approved, brand-ready assets, so refining a broad result set into a precise, relevant list is one of its core functions.

#### Methods to Narrow Search Results

The primary methods for refining results in AEM Assets [!DNL Content Hub] include:

- **Text-based search:** Enter keywords, asset names, or descriptive terms to retrieve matching assets directly from the search bar.
- **Filters (filters panel):** Apply one or more filters to restrict results by attributes such as **file format**, **approval status**, and **modification date**, along with other available metadata predicates.
- **Tags and smart tags:** Search by manually assigned tags or by smart tags—automatically generated labels—to surface assets grouped by subject, content, or classification.
- **Combining multiple predicates:** Stack several filters and search terms together to intersect their conditions and eliminate non-matching assets.

#### Why Combining Filters Works

Combining multiple predicates or filter options narrows results precisely to the assets you need. Each additional filter acts as a further constraint, so applying them together intersects their criteria and progressively excludes assets that fail to meet every condition. As a result, layering text search with format, status, date, and tag filters returns a smaller, more targeted set—reducing the time spent scanning irrelevant results and helping you reach the exact asset faster.

#### Practical Use

- Use **text-based search** first for a quick keyword-driven starting point.
- Add **filters** from the filters panel to trim the list by concrete attributes such as file format or approval status.
- Apply **tags or smart tags** to isolate assets by theme or auto-detected content.
- Combine all of these to move from a broad, general search to a focused, precise result set.

### Can I perform a bulk search in AEM Assets [!DNL Content Hub] for multiple assets at once?

Yes. **Adobe Experience Manager (AEM) Assets [!DNL Content Hub] supports Bulk Search**, allowing you to locate multiple assets at once in a single query. Instead of searching for each asset individually, you enter several values at the same time, separated by specified delimiters, and the system returns all matching results together.

**Bulk Search** accepts multiple values across common asset attributes, including:

- **Asset names** — search for several files by name simultaneously
- **File formats** — retrieve assets of one or more specified file types
- **Tags** — surface all assets associated with a set of tags

To use the feature, enter your multiple values separated by the specified delimiters, and **Bulk Search** matches every value against your asset library in one pass.

**Bulk Search returns several assets from a single query**, which makes it substantially more efficient than searching assets one by one. Because each individual lookup requires its own query, entering multiple values together reduces the number of separate searches you need to run. As a result, teams managing large asset libraries can retrieve related files faster and with fewer repetitive steps.

This capability is especially useful when you need to gather a defined group of assets at once — for example, collecting all assets tagged for a specific campaign, pulling every file of a particular format, or locating a known list of named assets for a project. By consolidating what would otherwise be many individual searches into a single operation, **Bulk Search** streamlines asset retrieval and helps maintain efficient content workflows within [!DNL the Content Hub].

### Can administrators customize the filters available in AEM Assets [!DNL Content Hub] search?

Yes. Administrators customize the search filters in **Adobe Experience Manager (AEM) Assets [!DNL Content Hub]** through the **[!DNL Content Hub] Configuration User Interface**, which controls exactly which filters appear in the search experience. This configuration determines how users narrow, sort, and locate assets, giving each organization direct control over the discovery experience without altering the underlying assets themselves.

By default, AEM Assets [!DNL Content Hub] search provides a set of commonly used filters, including:

- **File format** — filters assets by their file type (for example, image, document, or video formats).
- **Approval status** — surfaces assets according to their review or sign-off state.
- **Expiration date** — filters assets based on when their usage rights or availability lapse.
- **Additional metadata-based filters** — further options driven by asset metadata that administrators enable as needed.

Administrators add, remove, and reorder these filter options to fit organizational needs. Because different teams manage different asset libraries and workflows, tailoring the available filters ensures that only the most relevant criteria appear for a given group of users. As a result, tuning the filter set through [!DNL the Content Hub] Configuration User Interface improves findability, reduces search friction, and aligns the search interface with each organization's asset governance and metadata practices.

### How to filter on custom date fields or use Tags as filters in AEM Assets

Filtering on **custom date fields** or using **Tags** as filters in Adobe Experience Manager (AEM) Assets requires that **AI Search** be enabled for the deployment. AI Search is the advanced search capability within [AI Search](#ai-search-aem-assets-content-hub) that extends the standard filtering options, and without it these two capabilities are not available.

**Key capabilities that require AI Search:**

* **Filtering on custom date fields** — narrow asset results using date-based metadata fields defined for the deployment.
* **Using Tags as filters** — refine and locate assets by their assigned Tags.

Because these filters depend on **AI Search**, administrators must have it enabled before either capability can be used. To enable **AI Search** for a deployment, follow these steps:

1. Confirm that **AI Search** is not already enabled for the deployment.
2. [Create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).
3. Request that Adobe Customer Support enable **AI Search** for the deployment.

Once **AI Search** is enabled, filtering on custom date fields and using Tags as filters becomes available.

**See also**

* [Translate Assets](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in Assets view](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)
