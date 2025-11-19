---
title: Content Optimization Agent Overview
description: Learn what ...
feature: Edge Delivery Services, Agentic AI
role: Admin, Architect, Developer
---

# Content Optimization Agent {#content-optimization-agent}

The Content Optimization Agent transforms how users refine and adapt assets by applying natural language instructions to create channel-ready variations. Whether generating new renditions, adjusting visual properties, changing backgrounds, or preparing assets for specific digital channels, the agent interprets user intent and performs complex editing tasks automatically. It works seamlessly with the Discovery Agent, taking the assets it finds and producing optimized variations that meet brand, channel, and campaign requirements without manual design effort.

Some of the key benefits of Content Optimization include:

* **Effortless asset transformation**: Converts simple, conversational prompts into precise image operations, such as resizing, sharpening, mirroring, or recoloring, eliminating the need for specialized editing tools.

* **Channel-optimized outputs**: Quickly produces renditions tailored for specific platforms like Instagram Stories, web banners, or other marketing touchpoints, ensuring assets are ready for immediate use.

* **Creative enhancement at scale**: Applies visual adjustments and enhancements, such as background changes or graphic overlays, to support high-volume creative workflows without slowing teams down.

* **Seamless collaboration with the Discovery Agent**: Builds upon the assets identified by the Discovery Agent, enabling end-to-end asset retrieval and optimization through natural conversation.

## Prerequisites {#prerequisites-content-optimization-agent}

To generate variations or optimizations for image assets. You must have:

* A valid Dynamic Media license 

* Dynamic Media with OpenAPI enabled on AEM as a Cloud Service environment.


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

You can access AEM Business Agents via AI Assistant. Log on to experience.adobe.com and you can start interacting with AI Assistant by specifying your prompt in natural language using the `Ask AI Assistant anything` field:

![Access Discovery Agent](/help/ai-in-aem/agents/discovery/assets/access-discovery-agent.png)


## Common use cases and sample prompts {#use-cases-prompts}

* **High-resolution rendition creation**

   The agent can generate new renditions of an asset at a specified resolution and quality level, making it easy to prepare channel-ready variations without manual editing.
   

   Sample prompt:

   Create a `2000px` rendition as `JPEG` with `80%` quality.

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

   Overlay the image with `30%` discount graphics over the promotional banner, placing it `100px` from the bottom and the right edge.


## Optimization Results {#content-optimization-agent-results}




## Prompting best Practices {#prompting-best-practices-content-optimization-agent}

The following are some of the prompting best practices:

* Be explicit about the enhancement you want the Content Oprimization Agent to apply. Clearly state the transformation or adjustment you expect. Precise instructions help the agent produce accurate and predictable results. For example, Instead of `Make it good quality`, specify `Create a JPEG image with 90% quality`.

* Provide detailed parameters whenever possible. The more context you give, such as dimensions, format, quality, placement, or color values, the more tailored the output is.



