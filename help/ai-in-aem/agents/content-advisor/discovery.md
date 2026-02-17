---
title: Content Discovery Job
description: Learn how to use the content discovery job to deliver relevant AEM content on demand through natural, conversational prompts for a streamlined, click-free discovery experience.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
exl-id: 676300cd-b799-4c53-a58e-043e58a2cbc5
---

# Content Discovery Job {#discovery-job}

As part of AEM's [Content Advisor Agent,](/help/ai-in-aem/agents/content-advisor/overview.md) the content discovery job delivers AEM content on demand through natural, conversational prompts for a streamlined, click-free discovery experience. It intelligently searches across Assets, Content Fragments, and Adaptive Forms to deliver relevant materials such as images, videos, PDF documents, articles, and form templates. Using natural language, you can search for content without building complex queries or applying filters in the AEM Assets interface. Based on your prompt, the job returns curated results along with asset metadata and delivery URLs, ready to be embedded in other applications.

Some of the key benefits of the content discovery job include:

* **Unified Content Discovery**: Access all types of AEM content, such as images, videos, PDF documents, articles, and forms from a single conversational interface.

* **Faster Campaign Planning**: Quickly gather visuals and forms for marketing campaigns across Emails, Web, and Social channels.

* **Enhanced Productivity**: Reduce time spent browsing repositories or filtering metadata through automated, intent-based search.

* **Consistent Content Utilization**: Ensures reuse of approved assets and fragments, maintaining brand consistency across channels.

>[!IMPORTANT]
>
>AI-generated responses may be inaccurate or misleading. Be sure you double-check suggested fixes and responses. 
>
>See also [Adobe Experience Cloud Generative AI User Guidelines.](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html) 

## Skills {#skills-discovery-agent}

The content discovery job provides the following skills:

* **Natural language content discovery**  
  The content discovery job enables users to find relevant assets, content fragments, and adaptive forms within Adobe Experience Manager (AEM) using simple natural language prompts—no complex search queries required.

* **Tag-based asset discovery** 

   The content discovery job uses natural language prompts to find assets associated with specific tags in the AEM repository, helping users quickly access content organized or not organized as per the organization's taxonomy.

* **Folder-based content discovery:**  
  The content discovery job can identify assets by interpreting natural language prompts that reference folder names in AEM. Users can simply mention the folder in their prompt, without manually navigating through the repository, significantly reducing the number of clicks needed to locate the right content.

## Personas {#personas-content-discovery}

### Campaign Managers {#campaign-managers}

The content discovery job enables campaign managers to quickly identify and reuse trusted, high-performing content for ideation.

### Channel Marketers {#channel-marketers}

The content discovery job allows channel marketers to efficiently find relevant assets to create cohesive, multi-channel experiences.

### DAM Librarians {#dam-librarians}

DAM librarians can flag assets that are missing the metadata standards set by the organization, supporting consistent governance and ensuring assets remain complete and ready for use across channels.

### Agencies and Partners {#agencies-partners}

Agencies and partners can easily find brand-approved assets within Content Hub and reuse them to accelerate creative work while staying aligned with brand standards.

## How to Access {#access}

You can access the content discovery job in AEM via the AI Assistant. Log on to [`experience.adobe.com`](https://experience.adobe.com) and you can start interacting with AI Assistant by specifying your prompt in natural language using the search box:

![Access content discovery job](/help/ai-in-aem/agents/content-advisor/assets/access-discovery-agent.png)

For information on the MCP endpoint to access content discovery job, contact Adobe Support.

## Common Use Cases and Sample Prompts {#use-cases-prompts}

### Assets {#discovery-agent-use-cases-assets}

**Tag-based asset discovery** 

   The content discovery job uses natural language prompts to find assets associated with specific tags in the AEM repository, helping users quickly access content organized according to their organization's taxonomy.

   Sample prompt:

   Show images tagged `office` in folder `WKND`.

**Folder-based content discovery:**  
  The content discovery job can identify assets by interpreting natural language prompts that reference folder names in AEM. Users can simply mention the folder in their prompt, without manually navigating through the repository, significantly reducing the number of clicks needed to locate the right content.

  Sample prompts:

* Are there any svgs in folder `WKND`?
* Show assets modified after `Nov 1 2025` in folder `WKND`.
* List `lifestyle` images in folder `WKND`.

**Format-based asset discovery**

The content discovery job can identify assets that meet specific quality requirements, such as file format, allowing users to quickly locate product visuals that are ready for high-quality delivery and reuse across channels.

Sample prompt:

Find product packaging PNG images.

**Orientation-based content discovery**

The content discovery job can filter assets by recognizing visual attribute, such as the presence of people and the orientation of an image. This allows users to quickly narrow down content to the most relevant visuals without manually applying multiple filters in AEM.

Sample prompt:
   
Show assets with person in landscape orientation.

### Content Fragments {#discovery-job-use-cases-content-fragments}

The content discovery job helps users quickly locate the right Content Fragments by interpreting natural language references to campaign names, product brands, publication status, and recent creation activity. It allows teams to surface campaign-ready fragments and view brand-specific content, all without manually browsing through folders or applying multiple filters in AEM.

Sample prompts:

* Show content fragments for creating WKND offer campaign.

* Show the content fragment for americano beverage.

* Show me all published content fragments for WKND beverages.

* List all content fragments created in last 2 weeks.

### Forms {#discovery-job-use-cases-forms}

The content discovery job helps you quickly find adaptive forms using natural language prompts. It searches through form content and metadata to find matches based on keywords from your prompts. This means you can successfully discover relevant forms even if your search terms are not in the form's title or description.

Sample prompts:

* Show me all loan application forms.
* Find forms to apply for a job.
* Find contact forms.
* I'm looking for employee onboarding forms.
* Show me credit card application forms.

Note: Form discovery currently supports Edge Delivery Services forms only and tag-based search is not available for forms at this time.

## Search Results {#discovery-job-search-results}

### Assets {#discovery-job-search-results-assets}

The content discovery job returns the top results for each query, sorted by relevance to ensure that the exact matches appear first. The job combines metadata-driven queries with semantic search to assemble a focused set of likely matches, then uses an LLM to rank them based on user intent. This blended approach delivers accurate, context-aware results without depending entirely on a direct keyword match.

Each result includes asset name along with key asset metadata such as the asset path, creator, creation date, title, description, format, last modifier, last modified date, file size, dimensions, [Dynamic Media URL](/help/assets/dynamic-media/dynamic-media.md), and associated tags. If an asset is in approved state, the results also include [Dynamic Media with OpenAPI URL](/help/assets/dynamic-media-open-apis-overview.md). 

You can click the asset path to seamlessly navigate to the asset location within AEM.

![Search assets using content discovery job](/help/ai-in-aem/agents/content-advisor/assets/search-results-discovery-agent.png)

You can use these asset details to quickly evaluate if an asset meets the requirements without navigating to each asset to view these details.

>[!NOTE]
>
>The [Dynamic Media URL](/help/assets/dynamic-media/dynamic-media.md) field displays in the search results only if the asset is published and you have a valid Dynamic Media license. Similarly, [Dynamic Media with OpenAPI URL](/help/assets/dynamic-media-open-apis-overview.md) field displays only if you have a valid Dynamic Media license and Dynamic Media with OpenAPI is enabled for your AEM as a Cloud Service instance.

### Content Fragments {#discovery-agent-search-results-content-fragments}

The content discovery job provides full-text search capabilities for Content Fragments, returning the top results that best match the specified prompt. Each result includes Content Fragment name along with key metadata fields such as Content Fragment path, creator, creation date, variations, last modifier, and last modified date fields.

![Search Content Fragments using content discovery job](/help/ai-in-aem/agents/content-advisor/assets/search-content-fragments-discovery-agent.png)

You can click the Content Fragment path to seamlessly navigate to the Content Fragment location within AEM.

## Prompting Best Practices {#prompting-best-practices-discovery-job}

Specify concise details in your natural language prompts so that the job can return accurate and relevant results. The more clearly you describe what you are looking for, the better the job can refine and narrow the output. For example, you can:

* Define asset metadata such as tags, folder names, creation dates, publish status, author names in your prompts to filter assets.

* Use your organization-specific metadata, such as categories (running shoes, electronics), seasons (autumn, spring), events (black Friday, product launch), and channels (Web, Email, Print) to further filter content.

## Limitations {#limitations-discovery-job}

The content discovery job supports dimension-based prompts only for image and SVG format types. For example, `Find images wider than 1080px`.
