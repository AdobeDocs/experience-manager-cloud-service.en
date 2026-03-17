---
title: Content Discovery Agent
description: Learn how to use the content discovery agent to deliver relevant AEM content on demand through natural, conversational prompts for a streamlined, click-free discovery experience.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
exl-id: 676300cd-b799-4c53-a58e-043e58a2cbc5
---

# Content Discovery Agent {#discovery-agent}

As part of AEM's [Content Advisor Agent,](/help/ai-in-aem/agents/content-advisor/overview.md) the content discovery agent delivers AEM content on demand through natural, conversational prompts for a streamlined, click-free discovery experience. It intelligently searches across Assets, Content Fragments, AEM Sites pages, and Adaptive Forms to deliver relevant materials such as images, videos, PDF documents, articles, and form templates. Using natural language, you can search for content without building complex queries or applying filters in the AEM Assets interface. Based on your prompt, the agent returns curated results along with asset metadata and delivery URLs, ready to be embedded in other applications.

Some of the key benefits of the content discovery agent include:

* **Unified Content Discovery**: Access all types of AEM content, such as images, videos, PDF documents, articles, pages, and forms from a single conversational interface.

* **Faster Campaign Planning**: Quickly gather visuals and forms for marketing campaigns across Emails, Web, and Social channels.

* **Enhanced Productivity**: Reduce time spent browsing repositories or filtering metadata through automated, intent-based search.

* **Consistent Content Utilization**: Ensures reuse of approved assets and fragments, maintaining brand consistency across channels.

>[!VIDEO](https://video.tv.adobe.com/v/3479983)

>[!IMPORTANT]
>
>AI-generated responses may be inaccurate or misleading. Be sure you double-check suggested fixes and responses. 
>
>See also [Adobe Experience Cloud Generative AI User Guidelines.](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html) 

## Skills {#skills-discovery-agent}

The content discovery agent provides the following skills:

* **Natural language content discovery**  

  The Content Discovery agent enables users to find relevant assets, content fragments, adaptive forms, and AEM Sites pages within Adobe Experience Manager (AEM) using simple natural language prompts—no complex search queries required.

* **Metadata-based asset discovery** 

   The Content Discovery agent uses natural language prompts to find assets based on metadata available for assets in AEM. Users can discover assets using metadata such as tags, author or publisher email IDs, published or modified dates, MIME type, asset type, status, custom metadata properties defined in metadata forms in Assets view or Admin view, and so on. See [Common Use Cases and Sample Prompts](#use-cases-prompts) for complete list.

   You can also combine multiple metadata filters within a single prompt to refine search results.

* **Folder-based content discovery:**  
  The content discovery agent can identify assets by interpreting natural language prompts that reference folder names in AEM. Users can simply mention the folder in their prompt, without manually navigating through the repository, significantly reducing the number of clicks needed to locate the right content.

## Personas {#personas-content-discovery}

### Campaign Managers {#campaign-managers}

The content discovery agent enables campaign managers to quickly identify and reuse trusted, high-performing content for ideation.

### Channel Marketers {#channel-marketers}

The content discovery agent allows channel marketers to efficiently find relevant assets to create cohesive, multi-channel experiences.

### DAM Librarians {#dam-librarians}

DAM librarians can flag assets that are missing the metadata standards set by the organization, supporting consistent governance and ensuring assets remain complete and ready for use across channels.

### Agencies and Partners {#agencies-partners}

Agencies and partners can easily find brand-approved assets within Content Hub and reuse them to accelerate creative work while staying aligned with brand standards.

## How to Access {#access}

You can access the content discovery agent in AEM via the AI Assistant. Log on to [`experience.adobe.com`](https://experience.adobe.com) and you can start interacting with AI Assistant by specifying your prompt in natural language using the search box:

![Access content discovery agent](/help/ai-in-aem/agents/content-advisor/assets/access-discovery-agent.png)

For information on the MCP endpoint to access content discovery agent, contact Adobe Support.

## Common Use Cases and Sample Prompts {#use-cases-prompts}

### Assets {#discovery-agent-use-cases-assets}

**Metadata-based asset discovery** 

   The Content Discovery agent uses natural language prompts to find assets based on metadata available for assets in AEM. Users can discover assets using the following metadata properties: Tags, Created by Email ID, Modified by Email ID, Published by Email ID, Created Date, Modified Date, Published Date, MIME type, Asset Type, Status, file format, file size, image width, image height, and multiple metadata filters within a single prompt.

   The Content Discovery Agent also searches the custom properties available in metadata schemas for Admin view and metadata forms for Assets view. You can modify your prompts accordingly to search values available within those custom asset properties.

   >[!NOTE]
   >
   >To improve discovery performance, index relevant custom metadata properties. Indexed properties enable the agent to retrieve matching content faster when users include those properties in their prompts.


   Sample prompts:

   * **Search based on tags**: Show images tagged `office` in folder `WKND`.
   * **Search based on file format, asset type, asset status and Published by Email ID**: Show images in `.PNG` format that are `approved` and `published by <user email ID>`.
   * **Search based on file format, asset type, asset status and Created by Email ID**: Show videos in `.mp4` format that are approved and `created by <user email ID>`.
   * **Search based on file format, asset type, asset status and  Created Date**: Show images in `.PNG` format that are created after January 1, 2025 and `published by <user email ID>`
   * **Search based on MIME type, Created Date, and Published by Email ID**: Show `image/jpeg` created after `January 1, 2025` and `published by <user email ID>`.
   * **Search based on file format and custom metadata properties**: Show images in `.JPEG` format that have `Product SKU ID as <SKU value>`.

   * **Search for assets with missing metadata**: Show assets created in the last 90 days with `<Name of metadata property including custom properties>` is blank.

   * **Search for assets using file size, image width, and image height**: Show images larger than 5 MB with width greater than 2000 pixels and height greater than 1200 pixels.


**Folder-based content discovery:**  
  The Content Discovery Agent can identify assets by interpreting natural language prompts that reference folder names in AEM. Users can simply mention the folder in their prompt, without manually navigating through the repository, significantly reducing the number of clicks needed to locate the right content.

  Sample prompts:

* Are there any svgs in folder `WKND`?
* Show assets modified after `Nov 1 2025` in folder `WKND`.
* List `lifestyle` images in folder `WKND`.

**Additional questions to enable folder-based content discovery**

When a folder name is included in a prompt (without the full asset path), the Content Discovery Agent first checks for a matching folder at the root path `/content/dam/<folder-name>`. 

If a matching folder is not found at the root-level, the agent suggests alternative folder paths where the specified folder name exists in the repository. This helps users quickly identify the correct location without manually browsing the folder structure.

For example, the path `/content/dam/<folder-name>` was not found. Did you mean one of these?

* Option 1

* Option 2

**Format-based asset discovery**

The content discovery agent can identify assets that meet specific quality requirements, such as file format, allowing users to quickly locate product visuals that are ready for high-quality delivery and reuse across channels.

Sample prompt:

Find product packaging PNG images.

**Orientation-based content discovery**

The content discovery agent can filter assets by recognizing visual attribute, such as the presence of people and the orientation of an image. This allows users to quickly narrow down content to the most relevant visuals without manually applying multiple filters in AEM.

Sample prompt:
   
Show assets with person in landscape orientation.

**Expanding search results**

The Content Discovery Agent returns the top 20 most relevant results per content type for a prompt. If additional matching results are available, users can request the next set by entering a follow-up prompt such as `show me more`. The agent then retrieves the next set of results from the original search, allowing users to progressively explore larger result sets without refining the prompt.

**Finding similar assets**

The Content Discovery Agent allows users to find assets similar to a specific result returned in the search results. After the agent displays the top results for a prompt, you can request similar assets by referencing the position of an item in the results list. For example, a prompt such as `find assets similar to the 3rd result` instructs the agent to identify and return other relevant assets related to that item. This helps users quickly discover related content without creating a new search prompt.

**Sorting search results**

The content discovery agent allows users to sort search results directly within their natural language prompts. Users can specify sorting criteria such as modified date, created date, or asset name, and choose ascending or descending order.

Sample prompts:

* Find mountain images sorted by modified date in descending order (shows the most recently modified assets first).

* Show mountain images sorted by name in ascending order (shows the image names starting with letter A first followed by B, and so on).

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

## Search Results {#discovery-agent-search-results}

### Assets {#discovery-agent-search-results-assets}

The content discovery agent returns the top results for each query, sorted by relevance to ensure that the exact matches appear first. The agent combines metadata-driven queries with semantic search to assemble a focused set of likely matches, then uses an LLM to rank them based on user intent. This blended approach delivers accurate, context-aware results without depending entirely on a direct keyword match.

Each result includes asset name along with key asset metadata such as the asset path, creator, creation date, title, description, format, last modifier, last modified date, file size, dimensions, [Dynamic Media URL](/help/assets/dynamic-media/dynamic-media.md), and associated tags. If an asset is in approved state, the results also include [Dynamic Media with OpenAPI URL](/help/assets/dynamic-media-open-apis-overview.md). 

You can click the asset path to seamlessly navigate to the asset location within AEM.

![Search assets using content discovery agent](/help/ai-in-aem/agents/content-advisor/assets/search-results-discovery-agent.png)

You can use these asset details to quickly evaluate if an asset meets the requirements without navigating to each asset to view these details.

>[!NOTE]
>
>The [Dynamic Media URL](/help/assets/dynamic-media/dynamic-media.md) field displays in the search results only if the asset is published and you have a valid Dynamic Media license. Similarly, [Dynamic Media with OpenAPI URL](/help/assets/dynamic-media-open-apis-overview.md) field displays only if you have a valid Dynamic Media license and Dynamic Media with OpenAPI is enabled for your AEM as a Cloud Service instance.

### Content Fragments {#discovery-agent-search-results-content-fragments}

The content discovery agent provides full-text search capabilities for Content Fragments, returning the top results that best match the specified prompt. Each result includes Content Fragment name along with key metadata fields such as Content Fragment path, creator, creation date, variations, last modifier, and last modified date fields.

![Search Content Fragments using content discovery agent](/help/ai-in-aem/agents/content-advisor/assets/search-content-fragments-discovery-agent.png)

You can click the Content Fragment path to seamlessly navigate to the Content Fragment location within AEM.

## Prompting Best Practices {#prompting-best-practices-discovery-agent}

Specify concise details in your natural language prompts so that the agent can return accurate and relevant results. The more clearly you describe what you are looking for, the better the agent can refine and narrow the output. For example, you can:

* Define asset metadata such as tags, folder names, creation dates, publish status, author names in your prompts to filter assets.

* Use your organization-specific metadata, such as categories (running shoes, electronics), seasons (autumn, spring), events (black Friday, product launch), and channels (Web, Email, Print) to further filter content.

## Limitations {#limitations-discovery-agent}

* The Content Discovery Agent supports dimension-based prompts only for image and SVG format types. For example, `Find images wider than 1080px`.

* Content Hub administrators can access the Content Discovery Agent using the Content Hub portal, however, the results are retrieved only from the AEM author instance. Content Hub Limited users cannot currently get the benefits of the Content Discovery Agent (Coming Soon).

* Find Similar capability works only for images with [Smart Tags enhancements](/help/assets/ai-generated-metadata-assets-view.md).
