---
title: Content Discovery Agentic Capabilities Overview
description: Learn how the Content Discovery Agentic Capabilities collaborates with Coworker Chat to deliver AEM content on demand through natural, conversational prompts for a streamlined, click-free discovery experience.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Content Discovery Agentic Capabilities {#content-discovery-agentic-capabilites}

The Content Discovery Agentic Capability of Adobe Enterprise Manager (AEM) as a Cloud Service collaborates with [Coworker Chat](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/overview) to deliver AEM content on demand through natural, conversational prompts for a streamlined, click-free discovery experience. It intelligently searches across Assets to deliver relevant materials such as images, videos, and PDF documents. Using natural language, you can search for content without building complex queries or applying filters in the AEM Assets interface. Based on your prompt, the agentic capability returns curated results along with asset metadata and delivery URLs, ready to be embedded in other applications.

Some of the key benefits of the Content Discovery Agentic Capability include:

* **Unified Content Discovery**: Access all types of AEM content, such as images, videos, and PDF documents from a single conversational interface.

* **Faster Campaign Planning**: Quickly gather visuals and forms for marketing campaigns across Emails, Web, and Social channels.

* **Enhanced Productivity**: Reduce time spent browsing repositories or filtering metadata through automated, intent-based search.

* **Consistent Content Utilization**: Ensures reuse of approved assets and fragments, maintaining brand consistency across channels.

>[!IMPORTANT]
>
>AI-generated responses may be inaccurate or misleading. Be sure you double-check suggested fixes and responses. 
>
>See also [Adobe Experience Cloud Generative AI User Guidelines.](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html) 

## Skills {#skills-discovery-agentic-capability}

The Content Discovery Agentic Capability provides the following key skills:

* **Natural language content discovery**  

  The Content Discovery Agentic Capability enables users to find relevant assets within Adobe Experience Manager (AEM) using simple natural language prompts—no complex search queries required.

* **Metadata-based asset discovery** 

   The Content Discovery Agentic Capability uses natural language prompts to find assets based on metadata available for assets in AEM. Users can discover assets using metadata such as tags, author or publisher email IDs, published or modified dates, MIME type, asset type, status, custom metadata properties defined in metadata forms in Assets view or Admin view, and so on. See [Common Use Cases and Sample Prompts](#use-cases-prompts) for complete list.

   You can also combine multiple metadata filters within a single prompt to refine search results.

* **Folder-based content discovery:**  
  The Content Discovery Agentic Capability can identify assets by interpreting natural language prompts that reference folder names in AEM. Users can simply mention the folder in their prompt, without manually navigating through the repository, significantly reducing the number of clicks needed to locate the right content.

## Personas {#personas-content-discovery}

### Campaign Managers {#campaign-managers}

The Content Discovery Agentic Capability enables campaign managers to quickly identify and reuse trusted, high-performing content for ideation.

### Channel Marketers {#channel-marketers}

The Content Discovery Agentic Capability allows channel marketers to efficiently find relevant assets to create cohesive, multi-channel experiences.

### DAM Librarians {#dam-librarians}

DAM librarians can flag assets that are missing the metadata standards set by the organization, supporting consistent governance and ensuring assets remain complete and ready for use across channels.

### Agencies and Partners {#agencies-partners}

Agencies and partners can easily find brand-approved assets within Content Hub and reuse them to accelerate creative work while staying aligned with brand standards.

## How to Access {#access}

You can access the Content Discovery Agentic Capability via the [Coworker Chat](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/overview).

## Common Use Cases and Sample Prompts {#use-cases-prompts}

**Metadata-based asset discovery**

The Content Discovery Agentic Capability uses natural language prompts to find assets based on metadata available for assets in AEM. Users can discover assets using the following metadata properties: Tags, Created by Email ID, Modified by Email ID, Published by Email ID, Created Date, Modified Date, Published Date, MIME type, Asset Type, Status, file format, file size, image width, image height, and multiple metadata filters within a single prompt.

The Content Discovery Agentic Capability also searches the custom properties available in metadata schemas for Admin view and metadata forms for Assets view. You can modify your prompts accordingly to search values available within those custom asset properties.

>[!NOTE]
>
>To improve discovery performance, index relevant custom metadata properties. Indexed properties enable the agentic capability to retrieve matching content faster when users include those properties in their prompts.

Sample prompts:

* **Search based on tags**: Show images tagged `office` in folder `WKND`.
* **Search based on file format, asset type, asset status and Published by Email ID**: Show images in `.PNG` format that are `approved` and `published by <user email ID>`.
* **Search based on file format, asset type, asset status and Created by Email ID**: Show videos in `.mp4` format that are approved and `created by <user email ID>`.
* **Search based on file format, asset type, asset status and Created Date**: Show images in `.PNG` format that are created after January 1, 2025 and `published by <user email ID>`.
* **Search based on MIME type, Created Date, and Published by Email ID**: Show `image/jpeg` created after `January 1, 2025` and `published by <user email ID>`.
* **Search for assets with missing metadata**: Show assets created in the last 90 days with `<Name of metadata property including custom properties>` is blank.
* **Search for assets using file size, image width, and image height**: Show images larger than 5 MB with width greater than 2000 pixels and height greater than 1200 pixels.

**Natural language support for custom metadata**

The Content Discovery Agentic Capability supports querying custom metadata properties defined in metadata schemas. You can reference metadata values directly in your prompts without needing to specify them using a strict key-value format. The agentic capability interprets intent and matches relevant metadata fields automatically.

Sample prompts:

* **Finding assets which have a property value is not set**: Find me assets whose campaign Name is not set (the property must be indexed for appropriate results).
* **Finding assets which have a property value set**: Find me assets whose campaign Name is set (the property must be indexed for appropriate results).
* **Finding assets which have a property value set to X**: Find me assets whose campaign Name is Coffee-day.
* **Finding assets which have a property value set to set of values X, Y**: Find me assets whose campaign Name is Coffee-day along with those whose campaign Name is tea-day.
* **Showing the value of a particular property field**: Get me coffee assets also show me the campaign name of these assets.
* **Find assets which match a date based property condition**: Get me assets whose license is not expired.

**Folder-based content discovery**

The Content Discovery Agentic Capability can identify assets by interpreting natural language prompts that reference folder names in AEM. Users can simply mention the folder in their prompt, without manually navigating through the repository, significantly reducing the number of clicks needed to locate the right content.

Sample prompts:

* Are there any svgs in folder `WKND`?
* Show assets modified after `Nov 1 2025` in folder `WKND`.
* List `lifestyle` images in folder `WKND`.

**Additional questions to enable folder-based content discovery**

When a folder name is included in a prompt (without the full asset path), the Content Discovery Agentic Capability first checks for a matching folder at the root path `/content/dam/<folder-name>`.

If a matching folder is not found at the root-level, the agentic capability suggests alternative folder paths where the specified folder name exists in the repository. This helps users quickly identify the correct location without manually browsing the folder structure.

For example, the path `/content/dam/<folder-name>` was not found. Did you mean one of these?

* Option 1
* Option 2

**Semantic asset discovery**

The Content Discovery Agentic Capability can find assets based on concepts, moods, and visual themes using semantic matching. This enables users to describe the content they are looking for without relying on exact filenames, tags, or metadata values.

Sample prompts:

* Find me morning coffee lifestyle images.

**Format-based asset discovery**

The Content Discovery Agentic Capability can identify assets that meet specific quality requirements, such as file format, allowing users to quickly locate product visuals that are ready for high-quality delivery and reuse across channels.

Sample prompts:

* Find product packaging PNG images.

**Orientation-based content discovery**

The Content Discovery Agentic Capability can filter assets by recognizing visual attribute, such as the presence of people and the orientation of an image. This allows users to quickly narrow down content to the most relevant visuals without manually applying multiple filters in AEM.

Sample prompts:

* Show assets with person in landscape orientation.

**Expanding search results**

The Content Discovery Agentic Capability returns the top 20 most relevant results per content type for a prompt. If additional matching results are available, users can request the next set by entering a follow-up prompt such as `show me more`. The agentic capability then retrieves the next set of results from the original search, allowing users to progressively explore larger result sets without refining the prompt.


**Sorting search results**

The Content Discovery Agentic Capability allows users to sort search results directly within their natural language prompts. Users can specify sorting criteria such as modified date, created date, or asset name, and choose ascending or descending order.

Sample prompts:

* Find mountain images sorted by modified date in descending order (shows the most recently modified assets first).
* Show mountain images sorted by name in ascending order (shows the image names starting with letter A first followed by B, and so on).

**Filename-based asset discovery**

The Content Discovery Agentic Capability can find assets using an exact or partial filename, allowing users to locate known or partially known assets without navigating the DAM repository.

Sample prompts:

* Find assets with `Morning Muse` in the filename.

**Asset count and inventory**

The Content Discovery Agentic Capability can count assets based on criteria such as asset type, folder, approval status, or metadata values. This enables users to quickly understand the composition of a result set or asset repository.

Sample prompts:

* How many approved PDFs are in the campaign folder?

**Explore metadata values**

The Content Discovery Agentic Capability can discover the distinct values available for a metadata field across assets, enabling users to explore available classifications and refine subsequent searches.

Sample prompts:

* What Coffee Blend values exist in the products folder?

**Post-processing search results**

After assets are returned, users can continue working with the existing result set by filtering, grouping, sorting, or comparing the returned assets without starting a new search.

Sample prompts:

* From those results, show only the JPEGs.

**Dynamic Media delivery URLs**

The Content Discovery Agentic Capability can provide optimized Dynamic Media delivery URLs for approved assets, enabling users to retrieve delivery-ready references directly from their discovery results.

Sample prompts:

* Get the delivery URL for `Morning Muse Capsules.png`.


**Metadata completeness audit**

The Content Discovery Agentic Capability helps users identify assets with missing metadata fields, making it easier to find incomplete asset metadata and address gaps before assets are used or published.

Sample prompts:

* Which assets are missing descriptions?

**Approval readiness check**

The Content Discovery Agentic Capability helps users identify assets that do not have an approval status, enabling teams to find assets that may require review before go-live.

Sample prompts:

* Which Frescopa videos have no approval status?

**Large file identification**

The Content Discovery Agentic Capability helps users identify and rank assets by file size, making it easier to find large assets for storage review.

Sample prompts:

* Show me the largest assets in the DAM.

**Duplicate detection**

The Content Discovery Agentic Capability provides limited support for identifying potential duplicate assets. Duplicate detection is based on:

1. **Filename matching** — Searches for assets with the same or similar filename, for example, `WKND Brand Guidelines.pdf` and `WKND Brand Guidelines (1).pdf`.
2. **File size comparison** — When two assets have the exact same byte count, they are likely to be byte-for-byte duplicates.

Sample prompts:

* Are these `coffee-capsules.png` files duplicates?

<!--

**Performance-aware asset recommendations**

The Content Discovery Agentic Capability surfaces asset performance data in search and recommendation results, helping users identify relevant content based on how assets perform on AEM Sites. Performance signals such as average click-through rate (CTR), page views, and view counts provide additional context when evaluating and refining asset results.

Sample prompts:

* Show high-performing assets by view count.
* Show assets on popular pages by page views.
* Show high-engagement assets by CTR.

-->

**Next Best Action Suggestions**

The Content Discovery Agentic Capability proactively suggests relevant follow-up actions based on the current search results. The suggestions take into account factors such as folder structure, approval status, file formats, result count, and applied filters, helping users refine, broaden, or continue exploring their results without determining the next prompt themselves.

Suggested actions can include filtering by folder, format, date range, or approval status; getting counts or breakdowns; retrieving more information about a specific asset; generating delivery or download URLs; exploring metadata values; and paging through additional results.

Sample prompts:

* Filter to only approved assets.
* Show only JPEGs from these results.
* Which assets are missing descriptions?
* Show all assets in this folder.
* What other Coffee Blend values exist?
* Find more results — next page.
* Get the Dynamic Media delivery URL for asset #2.
* Get a download link for this asset.

<!--

### AEM Sites pages {#content-discovery-agent-aem-sites-pages}

The Content Discovery agent helps users quickly locate relevant AEM Sites pages by interpreting natural language prompts that reference page topics, campaigns, or other contextual keywords. The agent performs a full-text search based on the keywords in the prompt to identify matching pages in the AEM repository, eliminating the need to manually browse through the Sites structure.

Sample Prompts:

* Find all AEM Sites pages for the summer campaign.

* Find AEM Sites pages with a Coffee theme.

### Content Fragments {#discovery-agent-use-cases-content-fragments}

The Content Discovery Agent helps users quickly locate the right Content Fragments by interpreting natural language references to campaign names, product brands, publication status, and recent creation activity. It allows teams to surface campaign-ready fragments and view brand-specific content, all without manually browsing through folders or applying multiple filters in AEM.

Sample prompts:

* Show content fragments for creating WKND offer campaign.

* Show the content fragment for americano beverage.

* Show me all published content fragments for WKND beverages.

* List all content fragments created in last 2 weeks.

### Forms {#discovery-agent-use-cases-forms}

The Content Discovery Agent helps you quickly find adaptive forms using natural language prompts. It searches through form content and metadata to find matches based on keywords from your prompts. This means you can successfully discover relevant forms even if your search terms are not in the form's title or description.

Sample prompts:

* Show me all loan application forms.
* Find forms to apply for a agent.
* Find contact forms.
* I'm looking for employee onboarding forms.
* Show me credit card application forms.

Note: Form discovery currently supports Edge Delivery Services forms only and tag-based search is not available for forms at this time.

-->

## Search Results {#content-discovery-agentic-capability-search-results}

### Assets {#content-discovery-agentic-capability-search-results-assets}

The Content Discovery Agentic Capability returns the top results for each query, sorted by relevance to ensure that the exact matches appear first. The agentic capability combines metadata-driven queries with semantic search to assemble a focused set of likely matches, then uses an LLM to rank them based on user intent. This blended approach delivers accurate, context-aware results without depending entirely on a direct keyword match.

Each result is displayed as an asset card, displaying the asset name and preview. You can view the search results in a card view or a list view. Click **View all** to view the complete list of results, up to a maximum of 10 assets.

Click the More options icon (...) adjacent to each asset card to either download the asset or view asset metadata.

Asset metadata includes asset path, Format, Size, Dimensions, Description, Created Date and the creator, modified date along with the user who modified the asset, and download link. If an asset is in approved state, the results also include [Dynamic Media with OpenAPI URL](/help/assets/dynamic-media-open-apis-overview.md).

![Search assets using Coworker content discovery agentic capability](/help/ai-in-aem/agentic-capabilities/content-advisor/discovery/assets/coworker-content-discovery-agentic-capability-results.png)

>[!NOTE]
>
>The [Dynamic Media URL](/help/assets/dynamic-media/dynamic-media.md) field displays in the search results only if the asset is published and you have a valid Dynamic Media license. Similarly, [Dynamic Media with OpenAPI URL](/help/assets/dynamic-media-open-apis-overview.md) field displays only if you have a valid Dynamic Media license and Dynamic Media with OpenAPI is enabled for your AEM as a Cloud Service instance.

<!--

### Content Fragments {#discovery-agent-search-results-content-fragments}

The content discovery agent provides full-text search capabilities for Content Fragments, returning the top results that best match the specified prompt. Each result includes Content Fragment name along with key metadata fields such as Content Fragment path, creator, creation date, variations, last modifier, and last modified date fields.

![Search Content Fragments using content discovery agent](/help/ai-in-aem/agents/content-advisor/assets/search-content-fragments-discovery-agent.png)

You can click the Content Fragment path to seamlessly navigate to the Content Fragment location within AEM.

-->

## Content Discovery Agentic Capability availability within Content Hub {#content-discovery-agentic-capability-availability-within-content-hub}

You can now access the Content Discovery Agentic Capability directly from the Content Hub interface. This feature is available for Content Hub environments that use the latest search stack, which also provides [AI Search](/help/assets/search-assets-content-hub.md#ai-search-aem-assets-content-hub) and sorting capabilities. Adobe is rolling out the latest search stack to Content Hub customers in phases. If AI Search is available in your Content Hub interface, you can use the Content Discovery Agentic Capability.

To view if [AI Search](/help/assets/search-assets-content-hub.md#enable-disable-ai-search-content-hub) is available, navigate to your user profile icon and click **Configurations** on the Content Hub User Interface. Select the **Search** tab. If you can see options to select **AI Search** or **Keyword**, AI Search is available and you are using the latest search stack.

![AI Search in Content Hub](/help/assets/assets/ai-search-content-hub.png)


If AI Search is not yet available and you want to enable Content Discovery Agentic Capability within Content Hub, [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

<!--

## What's New in Content Discovery Agent {#whats-new-content-discovery-agent}

### Performance-Aware Asset Recommendations {#performance-aware-asset-recommendations}

Content Discovery Agent now surfaces asset performance data directly in search and recommendation results, helping teams prioritize content that drives engagement on AEM Sites.
When you search for assets via the AI Assistant, Content Discovery Agent enriches its natural-language search results with real-time performance signals pulled from AEM Sites analytics — average CTR, page views, and view counts — so you can see not just which assets match your query, but which of those are actually working for your audience.

What's New:

* Performance context on every result set. Alongside the usual asset previews (name, format, thumbnail), Content Discovery Agent now surfaces an aggregate performance summary for the returned assets — for example, `These assets average a 9.0% CTR`.

* One-click performance filters. Suggested follow-up prompts let you instantly refine results by performance thresholds without re-typing a query:

   * Show high-performing assets (by view count)

   * Show assets on popular pages (by page views)

   * Show high-engagement assets (by CTR)

* Grounded in real usage data. Recommendations are backed by first-party AEM Sites analytics, not just metadata or tagging relevance — so `best asset for this campaign` now factors in how similar assets have actually performed in live experiences.

>[!IMPORTANT]
>
>This feature is available as Limited Availability feature. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

### Discovery skill— Next Best Action Suggestions {#discovery-skill}

Discovery skill now proactively suggests relevant follow-up actions after every search result, helping you dig deeper into your assets without having to guess the right query.
After returning any set of assets, Discovery Agent now analyzes the result context — folder structure, approval status, file formats, result count, and applied filters — and surfaces a contextual `Here are some things you can do next` list, so your next step is one click away instead of a blank prompt.

>[!IMPORTANT]
>
>This skill is available only in Coworker.

What's New:

* Context-aware suggestions, not generic ones. The suggested actions change based on what is actually in the result set. If some assets are still pending approval, Content Discovery Agent surfaces that directly (`Show the 7 images that are not yet approved`). If a result set spans multiple folders, it suggests narrowing by the folder holding the most assets. If there are more results than shown, it offers to page through them.

* Common next actions surfaced automatically, including:

   * Filtering by folder, format, date range, or approval status

   * Getting a count or breakdown by format or folder

   * Drilling into a specific asset by number (`tell me more about #4`)

   * Generating a download link for any asset in the result set

   * Exporting the full result set as a CSV table

   * Paging to the next set of results when more are available

* Precise, actionable phrasing. Suggestions reference real numbers from your data (for example, `Filter to only images in /content/dam/frescopa/en/stock/ — that folder holds 91 of your images`) rather than generic prompts, so you know exactly what each option will return before selecting it.

**Why it matters**

Instead of knowing what to ask for next, you get a running set of relevant, data-backed suggestions after every interaction — turning a single search into a guided exploration of your asset library. This is especially useful for large repositories.

>[!IMPORTANT]
>
>This feature is available as Limited Availability feature. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

-->

## Prompting Best Practices {#prompting-best-practices-content-discovery-agentic-capability}

Specify concise details in your natural language prompts so that the Content Discovery agentic capability can return accurate and relevant results. The more clearly you describe what you are looking for, the better the agentic capability can refine and narrow the output. For example, you can:

* Define asset metadata such as tags, folder names, creation dates, publish status, author names in your prompts to filter assets.

* Use your organization-specific metadata, such as categories (running shoes, electronics), seasons (autumn, spring), events (black Friday, product launch), and channels (Web, Email, Print) to further filter content.

## Limitations {#limitations-discovery-agentic-capability}

* The Content Discovery Agentic Capability supports dimension-based prompts only for image and SVG format types. For example, `Find images wider than 1080px`.


* Editing or writing metadata is not supported (Use [OneAEM MCP](/help/ai-in-aem/mcp-support/using-mcp-with-aem-as-a-cloud-service.md)).

* Creating or deleting assets is not supported (Use AEM Assets author)

