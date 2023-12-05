---
title: Using Edge Delivery Services
description: Learn how AEM as a Cloud Service can be used with Edge Delivery Services.
feature: Edge Delivery Services
exl-id: 41999302-b4c9-4f5a-b659-6e7398a3c4f4
---

# Using Edge Delivery Services {#usingedge}

With Edge Delivery, you can create rapid development environments where authors can update and publish content quickly, and new sites can be launched rapidly. To this end, you can work with multiple content sources on the same website and publishing will be seamless and streamlined regardless of you chosen source. As such, it takes only a couple of seconds to go from editing to seeing the content live on the internet.

## Finding the Right Tool {#right-tool}

Edge Delivery is decoupled from the content source and can ingest content from different content sources.

![Content sources for Edge Delivery](assets/content-sources.png)

Ingesting from multiple content sources offers maximum flexibility to the user. Adobe offers guidance to help you choose which content sources are the best fit for your project.

![Content source flexibility](assets/content-source-flexiblity.png)

There are cases where the content source is predefined or otherwise not flexible (e.g. the project can not use Sharepoint or Google Drive). But in many cases, the tool is not preordained and choice of tool is not black and white. 

Adobe's guiding principle is simplicity. Start with document-based authoring and add complexity when needed. If a tool change is needed, Crosswalk covers content migration.

## How AEM Authoring Works with Edge Delivery Services {#how-it-works}

When using Edge Delivery Services with AEM as a Cloud Service, the most fundamental fact to understand is that the content you author is persisted in AEM as a Cloud Service.

![How AEM authoring works with Edge Delivery Services](assets/how-aem-edge-works.png)

1. [The AEM authoring environment](/help/sites-cloud/authoring/getting-started/quick-start.md) is used for content management such as creating new pages, Experience Fragments, Content Fragments, etc.
   * All features of AEM are likewise available such as workflows, MSM, translation, Launches, etc.
1. [The Universal Editor](/help/implementing/universal-editor/authoring.md) is used to author the content managed in AEM.
   * The Universal Editor offers a new and modern UI for content authoring.
   * For authoring, AEM renders the HTML but includes the scripts, styles, icons and other resources from Edge Delivery.
   * Although the Universal Editor is used, all changes are persisted to AEM.
1. Content that you author with the Universal Editor and persist to AEM is published to Edge Delivery Services.
   * Content remains stored in AEM.
   * AEM renders semantic HTML that is needed for ingestion.
   * Content is published to Edge Delivery Services.
1. [Edge Delivery Services](https://www.aem.live/home) ensures a 100% Lighthouse score.


## Authoring {#authoring-edge}

With Edge Delivery, authoring is easy, fast, and flexible. You can take two different paths to authoring within the context of Edge Delivery Services:

* Document-based authoring (such as Microsoft Word or Google Docs) - [Refer to this link for more details](https://www.hlx.live/docs/authoring).
* Page Editor/Universal Editor - Contact your Adobe Sales Representative.

In the case of document-based authoring, you can work with a variety of sources such as Microsoft Word and Google Docs. Documents from these sources become pages on your website. Headings, lists, images, font elements, videos can all be transferred from the initial source into your website. You can add metadata for SEO purposes or use blocks to work with structured content and add functionality.

## Publishing {#publishing-edge}

With Edge Delivery, publishing content is seamless regardless of your content source. The process is as follows: you use the [sidekick extension](#using-sidekick) to trigger the publishing mechanism and your content will be available live on your website in a couple of seconds.

## Edge Delivery Services and GitHub {#github-edge}

Edge Delivery leverages GitHub so customers can manage and deploy code directly from their GitHub repository. For example, you can write content in either Google Docs or Microsoft Word and develop the functionality of your site by using CSS and JavaScript in GitHub. Websites are automatically created for each of your branches from content preview to production. Every resource that you put into your GitHub repository is available on your website without a build process.

## Further Reading {#further-reading}

For more details, see the following pages:

* For details on how to get started with Edge Delivery, see the [Build](https://www.hlx.live/docs/#build) section of the Edge delivery documentation.
* To understand how to author and publish content by using Edge Delivery, see the [Publish section](https://www.hlx.live/docs/authoring).
* To understand how to use the sidekick extension, see [Using the sidekick](https://www.hlx.live/docs/sidekick) page.
* For AEM authoring, see the [Authoring Concepts page](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/authoring/getting-started/concepts.html)
