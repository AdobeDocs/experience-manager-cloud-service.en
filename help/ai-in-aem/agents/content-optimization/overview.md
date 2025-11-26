---
title: Content Optimization Agent
description: Learn how to use the Content Optimization Agent to transform how users refine and adapt assets by applying natural language instructions to create channel-ready variations.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
---

# Content Optimization Agent {#content-optimization-agent}

The Content Optimization Agent transforms how users refine and adapt assets by applying natural language instructions to create channel-ready variations. Whether generating new renditions, adjusting visual properties, changing backgrounds, or preparing assets for specific digital channels, the agent interprets user intent and performs complex editing tasks automatically. It works seamlessly with the Discovery Agent, taking the assets it finds and producing optimized variations using core [Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md) that meet brand, channel, and campaign requirements without manual design effort.

Some of the key benefits of Content Optimization include:

* **Effortless asset transformation**: Converts simple, conversational prompts into precise image operations, such as resizing, sharpening, mirroring, or recoloring, eliminating the need for specialized editing tools.

* **Channel-optimized outputs**: Quickly produces renditions tailored for specific platforms like Instagram Stories, web banners, or other marketing touchpoints, ensuring assets are ready for immediate use.

* **Creative enhancement at scale**: Applies visual adjustments and enhancements, such as background changes or graphic overlays, to support high-volume creative workflows without slowing teams down.

* **[Seamless collaboration with the Discovery Agent](/help/ai-in-aem/agents/discovery/using.md)**: Builds upon the assets identified by the Discovery Agent, enabling end-to-end asset retrieval and optimization through natural conversation.

>[!IMPORTANT]
>
>AI-generated responses may be inaccurate or misleading. Be sure you double-check suggested fixes and responses. 
>
>See also [Adobe Experience Cloud Generative AI User Guidelines](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html). 

## Prerequisites {#prerequisites-content-optimization-agent}

To generate variations or optimizations for image assets. You must have:

* A valid Dynamic Media license 

* Dynamic Media with OpenAPI enabled on AEM as a Cloud Service environment.

* The assets in [approved state](/help/assets/manage-organize-assets-view.md#manage-asset-status) in your AEM as a Cloud Service environment.


## Skills {#skills-content-optimization-agent}

The Content Optimization Agent provides the following skills:

* **Understand intent through natural language**

  The Content Optimization Agent interprets user intent from natural language prompts, accounting for channel, campaign, and audience context to determine the most relevant optimization actions.

* **Generates dynamic content variants**

   The Content Optimization Agent creates optimized variants as dynamic URLs tailored for different channels and format types.

* **Optimizes image content**

   The Content Optimization Agent applies enhancements such as format conversion, resolution adjustments, cropping, and sharpening to improve image quality.

* **Multi-variant asset optimization**

   The Content Optimization Agent can generate multiple optimized image variations from the assets returned by the Discovery Agent using a single natural language prompt, enabling users to produce channel-ready renditions quickly and efficiently.

## Personas {#personas-content-optimization-agent}

Channel Marketers, the key persona for Content Optimization Agent, can select the right high-resolution source content and request optimized formats tailored to their channels and audience segments.

Regional Marketers and Agency Workers can also use the Content Optimization Agent to quickly generate channel-ready image variations that support faster, more consistent content production.

## How to access Content Optimization Agent? {#access-content-optimization-agent}

You can access the Agents in AEM via the AI Assistant. Log on to experience.adobe.com and you can start interacting with AI Assistant by specifying your prompt in natural language using the `Ask AI Assistant anything` field:

![Access Discovery Agent](/help/ai-in-aem/agents/discovery/assets/access-discovery-agent.png)

## Common use cases and sample prompts {#use-cases-prompts}

Use Content Optimization prompts by searching for the right assets through the [Discovery Agent](/help/ai-in-aem/agents/discovery/using.md). Once the relevant images are surfaced, users can generate optimized or channel-specific variants for one or multiple assets directly from the search results. This workflow ensures high-quality inputs and consistently better optimization outcomes. [See the complete list of available optimizations](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/).

* **High-resolution rendition creation**

   The agent can generate new renditions of an asset at a specified resolution and quality level, making it easy to prepare channel-ready variations without manual editing.
   

   Sample prompt:

   Create a `2000px` rendition as `JPEG` with `80%` quality.

   Search for the right asset using the [Discovery agent](/help/ai-in-aem/agents/discovery/using.md) and then use the following prompts in case of multiple search results:

   For the 3rd search result, create a `2000px` rendition as `JPEG` with `80%` quality.

   OR

   For `Asset ID`, generate a 2000px rendition as `JPEG` with `80%` quality

* **Image enhancement**

   The agent can apply visual improvements—such as sharpening—to ensure assets look crisp and well-defined before being used across campaigns.

   Sample prompt:

   Sharpen the image.


* **Background color adjustments**

   The agent can update or replace background colors in transparent assets, supporting brand-specific color schemes or campaign-driven visual themes.

   Sample prompt:

   Change background color of the `PNG` to `#ff8932`.

* **Orientation transformations**

   The agent can flip or mirror visuals to align with layout needs or creative direction, without requiring external editing tools.

   Sample prompt:

   Mirror the image horizontally.

* **Channel-optimized renditions**

   The agent can produce renditions tailored to platform-specific requirements—such as Instagram Stories—ensuring assets meet format, ratio, and quality guidelines automatically.

   Sample Prompt:

   Create a rendition for an `Instagram` story.

* **Branded overlays and composite generation**

   The agent can apply promotional graphics, overlays, or badges to existing assets with precise placement, supporting rapid creation of campaign-ready composites.

   Sample Prompt:

   Overlay the image with `30%` discount graphics over the promotional banner, placing it `100px` from the center.

   >[!NOTE]
   >
   >Overlay positions might not be accurate.


## Optimization Results {#content-optimization-agent-results}

When you specify an optimization prompt, the Content Optimization Agent returns the enhanced asset along with convenient access options based on the asset type:

* **Images**: The response includes a thumbnail preview and options to open the Dynamic Media URL or download the optimized image.

* **PDF documents**: The response includes a thumbnail preview and options to open the Dynamic Media URL or download the optimized file.

* **Videos**: The response provides options to open the Dynamic Media URL or download the optimized video.

![Content Optimization results](/help/ai-in-aem/agents/content-optimization/assets/download-content-optimization.png)

These results make it easy to review the optimized output and immediately use it across downstream channels or workflows.

<!--


## Prompting best Practices {#prompting-best-practices-content-optimization-agent}

The following are some of the prompting best practices:

* Be explicit about the enhancement you want the Content Optimization Agent to apply. Clearly state the transformation or adjustment you expect. Precise instructions help the agent produce accurate and predictable results. For example, Instead of `Make it good quality`, specify `Create a JPEG image with 90% quality`.

* Provide detailed parameters whenever possible. The more context you give, such as dimensions, format, quality, placement, or color values, the more tailored the output is.

-->
