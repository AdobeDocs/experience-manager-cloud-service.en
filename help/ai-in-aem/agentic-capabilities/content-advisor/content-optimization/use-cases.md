---
title: Content Optimization Agentic Capabilities Overview
description: Learn how the Content Optimization Agentic Capabilities in AEM collaborates with Coworker Chat to help you refine and adapt assets by applying natural language instructions to create channel-ready variations.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Content Optimization Agentic Capabilities {#content-optimization-agentic-capabilites}

The Content Optimization Agentic Capability of Adobe Experience Manager (AEM) as a Cloud Service collaborates with [Coworker Chat](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/overview) to transform how users refine and adapt assets by applying natural language instructions to create channel-ready variations. Whether generating new renditions, adjusting visual properties, changing backgrounds, or preparing assets for specific digital channels, the Content Optimization Agentic Capability interprets user intent and performs complex editing tasks automatically. It works seamlessly with [the Content Discovery agentic capability,](/help/ai-in-aem/agentic-capabilities/content-advisor/discovery/use-cases.md) taking the assets it finds and producing optimized variations using core [Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md) that meet brand, channel, and campaign requirements without manual design effort.

Some of the key benefits of the Content Optimization Agentic Capability include:

* **Effortless asset transformation**: Converts simple, conversational prompts into precise image operations, such as resizing, sharpening, mirroring, or recoloring, eliminating the need for specialized editing tools.

* **Channel-optimized outputs**: Quickly produces renditions tailored for specific platforms like Instagram Stories, web banners, or other marketing touchpoints, ensuring assets are ready for immediate use.

* **Creative enhancement at scale**: Applies visual adjustments and enhancements, such as background changes or graphic overlays, to support high-volume creative workflows without slowing teams down.

* **[Seamless collaboration with the Content Discovery agentic capability](/help/ai-in-aem/agentic-capabilities/content-advisor/discovery/use-cases.md)**: Builds upon the assets identified by the Content Discovery agentic capability, enabling end-to-end asset retrieval and optimization through natural conversation.

>[!IMPORTANT]
>
>AI-generated responses may be inaccurate or misleading. Be sure you double-check suggested fixes and responses. 
>
>See also [Adobe Experience Cloud Generative AI User Guidelines.](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html)


## Prerequisites {#prerequisites-content-optimization-agentic-capability}

To generate variations or optimizations for image assets. You must have:

* A valid Dynamic Media license 

* Dynamic Media with OpenAPI enabled on AEM as a Cloud Service environment.

* The assets in [approved state](/help/assets/manage-organize-assets-view.md#manage-asset-status) in your AEM as a Cloud Service environment.

## Skills {#skills-content-optimization-agentic-capability}

The Content Optimization Agentic Capability provides the following skills:

* **Understand intent through natural language**

  The Content Optimization Agentic Capability interprets user intent from natural language prompts, accounting for channel, campaign, and audience context to determine the most relevant optimization actions.

* **Generates dynamic content variants**

   The Content Optimization Agentic Capability creates optimized variants as dynamic URLs tailored for different channels and format types.

* **Optimizes image content**

   The Content Optimization Agentic Capability applies enhancements such as format conversion, resolution adjustments, cropping, and sharpening to improve image quality.

* **Multi-variant asset optimization**

   The Content Optimization Agentic Capability can generate multiple optimized image variations from the assets returned by the Content Discovery Agentic Capability using a single natural language prompt, enabling users to produce channel-ready renditions quickly and efficiently.

## Personas {#personas-content-optimization-agentic-capability}

Channel marketers, the key persona for Content Optimization Agentic Capability, can select the right high-resolution source content and request optimized formats tailored to their channels and audience segments.

Regional marketers and agency workers can also use the Content Optimization Agentic Capability to quickly generate channel-ready image variations that support faster, more consistent content production.

## How to Access {#access-content-optimization-agentic-capability}

You can access the Content Optimization Agentic Capabilities via the [Coworker Chat](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/overview).

## Common Use Cases and Sample Prompts {#use-cases-prompts}

Use the Content Optimization Agentic Capability by searching for the right assets through the [Content Discovery agentic capability](/help/ai-in-aem/agentic-capabilities/content-advisor/discovery/use-cases.md). Once the relevant images are surfaced, users can generate optimized or channel-specific variants for one or multiple assets directly from the search results. Alternatively, users can generate variants by specifying the asset UUID or asset path in the prompt, without needing to perform a prior search. This workflow ensures high-quality inputs and consistently better optimization outcomes. [See the complete list of available optimizations](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/) for more information.

* **High-resolution rendition creation**

   The Content Optimization Agentic Capability can generate new renditions of an asset at a specified resolution and quality level, making it easy to prepare channel-ready variations without manual editing.
   

   Sample prompt:

   * Create a `2000px` rendition as `JPEG` with `80%` quality.

   Search for the right asset using the [Content Discovery agentic capability](/help/ai-in-aem/agentic-capabilities/content-advisor/discovery/use-cases.md) and then use the following prompts in case of multiple search results:

   * For the 3rd search result, create a `2000px` rendition as `JPEG` with `80%` quality.

     OR

   * For `Asset ID`, generate a 2000px rendition as `JPEG` with `80%` quality

* **Image enhancement**

   The Content Optimization Agentic Capability can apply visual improvements—such as sharpening—to ensure assets look crisp and well-defined before being used across campaigns.

   Sample prompt:

   * Sharpen the image.


* **Background color adjustments**

   The Content Optimization Agentic Capability can update or replace background colors in transparent assets, supporting brand-specific color schemes or campaign-driven visual themes.

   Sample prompt:

   * Change background color of the `PNG` to `#ff8932`.

* **Orientation transformations**

   The Content Optimization Agentic Capability can flip or mirror visuals to align with layout needs or creative direction, without requiring external editing tools.

   Sample prompt:

   * Mirror the image horizontally.

* **Channel-optimized renditions**

   The Content Optimization Agentic Capability can produce renditions tailored to platform-specific requirements—such as Instagram Stories—ensuring assets meet format, ratio, and quality guidelines automatically.

   Sample Prompt:

   * Create a rendition for an `Instagram` story.

* **Branded overlays and composite generation**

   The Content Optimization Agentic Capability can apply promotional graphics, overlays, or badges to existing assets with precise placement, supporting rapid creation of campaign-ready composites.

   Sample Prompt:

   * Overlay the image with `30%` discount graphics over the promotional banner, placing it `100px` from the center.

   >[!NOTE]
   >
   >Overlay positions might not be accurate.

* **Asset delivery**

   The Content Optimization Agentic Capability can generate delivery and download URLs for approved assets, including high-resolution image renditions, PDF documents, and video assets. For videos, it supports adaptive streaming and progressive download URLs.

   Sample prompts

   * Give me a 2x DPR version of this image.
   * Give me a download link for this asset.
   * Get the streaming URL for this video.
   * Get the progressive download URL for this video.
   * Get the delivery URL for this PDF.

<!--

* **Dynamic Media template personalization**

   The Content Optimization Agentic Capability can work with Dynamic Media templates to generate parameterized URLs and personalized variants. It can also discover and parameterize layers in a PSD template and generate multiple personalized variants using values from a CSV file.

   Sample prompts

   * Generate a template URL with `headline="Summer Sale"`.
   * Auto-parameterize this PSD template.
   * Generate variants from this template using my CSV.

   -->

## Optimization Results {#content-optimization-agentic-capability-results}

When you specify an optimization prompt, the Content Optimization Agentic Capability returns the enhanced asset along with convenient access options based on the asset type:

* **Images**: The response includes a thumbnail preview and options to open the Dynamic Media URL or download the optimized image.

* **PDF documents**: The response includes a thumbnail preview and options to open the Dynamic Media URL or download the optimized file.

* **Videos**: The response provides options to open the Dynamic Media URL or download the optimized video.

![Content Optimization results](/help/ai-in-aem/agentic-capabilities/content-advisor/content-optimization/assets/coworker-content-optimization-results.png)

These results make it easy to review the optimized output and immediately use it across downstream channels or workflows.


## Limitations {#limitations-content-optimization}

* Setting background color is not supported.

<!--


## Prompting best Practices {#prompting-best-practices-content-optimization-agent}

The following are some prompting best practices:

* Be explicit about the enhancement you want the content optimization agent to apply. Clearly state the transformation or adjustment you expect. Precise instructions help the agent produce accurate and predictable results. For example, Instead of `Make it good quality`, specify `Create a JPEG image with 90% quality`.

* Provide detailed parameters whenever possible. The more context you give, such as dimensions, format, quality, placement, or color values, the more tailored the output is.

-->
