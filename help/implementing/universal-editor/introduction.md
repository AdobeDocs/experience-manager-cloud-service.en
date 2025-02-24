---
title: Universal Editor Introduction
description: The Universal Editor is a modern visual authoring tool designed to empower your marketing organization to produce impactful web experiences. 
exl-id: d4fc2384-a0f5-4a6f-9572-62749786be4c
feature: Developing
role: Admin, Architect, Developer
---

# Universal Editor Introduction {#introduction}

The Universal Editor is a modern visual authoring tool designed to empower your marketing organization to produce impactful web experiences. 

## Overview {#overview}

The Universal Editor is a versatile visual editor that is part of Adobe Experience Manager Sites. It enables authors to perform what-you-see-is-what-you-get (WYSIWYG) editing of any headless or headful experience. It offers:

* **Instant Editing**: Authors can edit content directly within the preview experience, eliminating the need to locate and navigate to individual content sources.  
* **Visual Editing**: While making changes, authors instantly see how they affect the actual visitor experience, minimizing friction. 
* **Discoverable Options**: Clearly labeled options and an intuitive UI empower authors to configure metadata and compose layouts with ease. 
* **Non-Technical**: No specialized expertise is required to make edits, while corporate brand guidelines are automatically enforced, facilitating the scaling of content tasks across your organization. 
* **Integration and Extensibility**: Fully integrated with AEM, the Universal Editor’s flexible [extension points](#extensibility) allow all essential tools to be unified within a single, cohesive interface. From AI-powered features to custom extensions tailored to your unique business needs, it empowers teams to streamline workflows and enhance productivity effortlessly.

In summary:

* **Authors benefit** from the Universal Editor’s flexibility as it supports the same consistent visual editing for all forms of AEM content.
* **Developers benefit** from Universal Editor’s versatility as it supports true decoupling of the implementation.

Being a true editor-as-a-service and is overall more flexible, the Universal Editor intends to eventually supersede the [Page Editor.](/help/sites-cloud/authoring/page-editor/introduction.md)

## Supported Architectures {#supported-architectures}

The Universal Editor supports the following two primary AEM setups: 

1. **[Edge Delivery Services](/help/edge/overview.md)**: This is the preferred approach for its simplicity, faster time-to-value, and enhanced performance.
1. **[Headless Implementations](/help/headless/introduction.md)**: If you have an existing headless project or specific requirements for decoupled rendering, the Universal Editor allows enterprise-grade visual editing without the need to refactor the entire project. It is compatible with virtually any architecture (SSR, CSR), web framework (Next.js, React, Astro, etc.), and hosting models ("bring your own app").

>[!TIP]
>
>Please see the document [Universal Editor Use Cases and Learning Paths](/help/implementing/universal-editor/use-cases.md) for more details on the supported architectures.

## Supported AEM Versions {#aem-versions}

The Universal Editor is supported by:

* AEM as a Cloud Service (release `2023.8.13099` or higher)
* AEM 6.5 (service pack 21 or 22 plus a feature pack)

This documentation is for using the Universal Editor with AEM as a Cloud Service. For using the Universal Editor with AEM 6.5, [please see the AEM 6.5 documentation.](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/developing/headless/universal-editor/introduction)

## Features {#features}

The Universal Editor offers many features to supports a wide range of use cases for efficient content management.

* **[WYSIWYG](/help/sites-cloud/authoring/universal-editor/authoring.md)**: Perform what-you-see-is-what-you-get editing of any form of web content, including plain text, rich text, media, and metadata.
* **[Composition](/help/sites-cloud/authoring/universal-editor/authoring.md#editing-content)**: Create, edit, reorder, nest, or delete content blocks of various types (titles, buttons, teasers, sections, embed, etc.).
* **[Layout](/help/sites-cloud/authoring/universal-editor/templates.md)**: Utilize page templates, apply visual styles, and compose layouts with blocks like columns, carousels, and accordions.
* **[Device Simulation](/help/sites-cloud/authoring/universal-editor/navigation.md#emulator)**: Preview and optimize content for different visitor devices while editing.
* **Omnichannel**: Reuse both structured and unstructured content across multiple channels.
* **[Localization](/help/sites-cloud/authoring/universal-editor/inheritance.md)**: Streamline content translation workflows and efficiently handle localized content inheritance with Multi-Site Manager.
* **Consistency**: Ensure compliance with brand guidelines and maintain uniformity across all content.
* **Security**: [Enforce access control](/help/implementing/universal-editor/authentication.md), protect content integrity, and track changes with [robust versioning.](/help/sites-cloud/authoring/sites-console/page-versions.md)
* **[Publishing](/help/sites-cloud/authoring/universal-editor/publishing.md)**: Integrate review, approval, and publication workflows directly within the editor.
* **Unified**: Fully integrates with AEM tools like the [Sites Console,](/help/sites-cloud/authoring/sites-console/introduction.md) [Content Fragment Editor,](/help/sites-cloud/administering/content-fragments/overview.md) and many more, providing a cohesive authoring experience.

## Extensibility {#extensibility}

The Universal Editor is not only very capable out-of-the-box, but offers a number of extension possibilities.

* **Extensions** are numerous and ready-made to support requirements such as supporting workflows, generating variations, and enabling experimentation to name a few.
* **An Extensible UI** allows you to create your own extensions using the same underlying frameworks that the ready-made extensions leverage enabling ultimate flexibility to adapt to your project needs.
* **Extension Points** such as blocks, custom data types, and events allow for seamless integration of custom business requirements beyond the UI.

>[!TIP]
>
>For more information on the extensibility of the Universal Editor, please see the document [Extending the Universal Editor.](/help/implementing/universal-editor/extending.md)

## Universal Editor and the Content Fragment Editor {#universal-editor-content-fragment-editor}

At first glance, it might seem like the Universal Editor and the Content Fragment Editor provide similar editing capabilities. However, these editors offer very different capabilities and they accomplish different jobs of the marketing practitioner.

### Content Fragment Editor {#content-fragment-editor} 

A marketing practitioner wants to create content without having to care about its layout, so that it can be reused in numerous contexts of the experience.

* The underlying job to accomplish is to scale the content strategy.

### Universal Editor {#universal-editor}

A marketing practitioner wants to create content that is tailored to the layout of a given context to deliver an exceptional experience.

* The underlying job to accomplish is to convincingly connect with the readers.

## Limitations {#limitations}

As you explore the Universal Editor and move forward implementing it in your own projects, please keep the following limitations in mind.

* No more than 25 AEM resources (Content Fragments, pages, Experience Fragments, Assets, etc.) should be references as instrumentation on a single page.
* AEM as a Cloud Service and [AEM 6.5](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/developing/headless/universal-editor/introduction) are the only supported AEM backends.
* Release `2023.8.13099` or higher is required for AEM as a Cloud Service.
* Content authors must have their own individual Experience Cloud accounts.
* As part of AEM, the Universal Editor [supports the same desktop browsers as AEM.](/help/overview/supported-platforms.md)
  * Mobile versions of these browsers are not supported.

{{ue-ip-allow-lists}}

## Next Steps {#next-steps}

Please see the document [Universal Editor Use Cases and Learning Paths](/help/implementing/universal-editor/use-cases.md) to learn more about common use cases for the Universal Editor and to discover the right documentation resources to support you in your project.
