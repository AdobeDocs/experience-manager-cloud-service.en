---
title: Learn about headless content and how to localize in AEM
description: Learn headless concepts, how they map to AEM, and the theory of AEM localization.
---
# Learn about headless content and how to localize in AEM {#learn-about}

Learn headless concepts, how they map to AEM, and the theory of AEM localization.

## Objective {#objective}

This document helps you understand headless content delivery, how AEM supports headless, and how such content can be localized. After reading you should:

* Understand the basic concepts of headless content delivery.
* Be familiar with how AEM supports headless and localization.

## Full-Stack Content Delivery {#full-stack}

Ever since the rise of easy-to-use, large-scale content management systems (CMSes), organizations have leveraged them as a central location to manage messaging, branding, and communications. Using the CMS as a central point for administering experiences improved efficiency by eliminating the need to duplicate tasks in disparate systems.

![The classic full-stack CMS](/help/journey-headless/developer/assets/full-stack.png)

In a full-stack CMS, all of the functionality for manipulating content is in the CMS. Features of the system make up different components of the CMS stack. The full-stack solution has many advantages.

* There is one system to maintain.
* Content is managed centrally.
* All services of the system are integrated.
* Content authoring is seamless.

So if new channel needs to be added or support for new types of experiences is required, one (or more) new components can be inserted into the stack and there is only one place to make changes.

![Adding a new channel to the stack](/help/journey-headless/developer/assets/adding-channel.png)

The complexity of the dependencies within the stack quickly become apparent as other items in the stack  need to be adjusted to accommodate the changes.

## The Head in Headless {#the-head}

The head of any system is generally the output renderer of that system, typically in the form of a GUI or other graphical output.

When we talk about a headless CMS, the CMS manages the content and continues to deliver it to consumers. However, by only delivering the **content** in a standardized fashion, a headless CMS omits the final output rendering, leaving the **presentation** of the content to the consuming service.

![Headless CMS](/help/journey-headless/developer/assets/headless-cms.png)

The consuming services, be they AR experiences, a webshop, mobile experiences, progressive web apps (PWAs), etc., take in content from the headless CMS and provide their own rendering. They take care of providing their own heads for your content.

Omitting the head simplifies the CMS by removing complexity. Doing this also shifts the responsibility of rendering the content to the services that actually need the content and are often better suited to such rendering.

## Localizing Headless Content in AEM {#localizing-in-aem}

In addition to offering robust tools to create, manage, and deliver traditional webpages in the full-stack fashion, AEM also offers the ability to author self-contained selections of content and serve them headlessly.

The power of AEM allows it to deliver content either headlessly, full-stack, or in both models at the same time. For the localization specialist, the same set of localization tools can be applied to both types of content, giving you a unified approach for translating your content.

## What's Next {#what-is-next}

Thanks for getting started on your AEM headless localization journey! Now that you read this document you should:

* Understand the basic concepts of headless content delivery.
* Be familiar with how AEM supports headless and localization.

Build on this knowledge and continue your AEM headless localization journey by next reviewing the document [Get started with AEM headless localization](getting-started.md) where you will have an overview of how AEM manages headless content and get to know its localization tools.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the headless localization journey by reviewing the document [Get started with AEM headless localization,](getting-started.md) the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the headless journey.

* [MSM and Translation](/help/sites-cloud/administering/msm-and-translation.md) - The details of AEM's Multi-Site Manager and how it works with its translation tools
