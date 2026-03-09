---
title: Experience Modernization Agent Overview
description: Learn how the Experience Modernization Agent onboards new websites into Edge Delivery Services with the help of AI.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
exl-id: c23a6f55-2ba8-4290-b7e8-06cad5de0fc8
---

# Experience Modernization Agent Overview {#experience-modernization-agent}

Learn how the Experience Modernization Agent onboards websites into Edge Delivery Services with the help of AI.

## Introduction {#introduction}

[As part of the Brand Experience Agent,](/help/ai-in-aem/agents/brand-experience/overview.md) The Experience Modernization Agent unlocks the full value of Edge Delivery Services (including AEM authoring) by making website migrations and ongoing evolution fast and frictionless.

It combines [site creation and migration skills](#creation-migration) for initial website onboarding and [block development capabilities](#block-development) for continuous experience development (style updates, template refinements, landing page creation). In addition, it offers the [Experience Modernization Console](#console) as a hosted AI-assisted development environment available to you directly. While users can operate the agent directly through that console, developers retain full control over what ships.

Additionally, to ensure the success  of complex migrations, Adobe offers the [Agentic Outcome Engineer (AOE) Delivery Model](#delivery-model). This option can be used as an accelerator or as a tactical service to help unblock specific project challenges.

## Benefits {#benefits}

The Experience Modernization Agent accelerates the time to value for [Edge Delivery Services](/help/edge/overview.md) adoption and gives you the agility to adapt your brand's web experience.

* **High velocity**: AI automation handles repetitive migration work (content import, block mapping, design system application), compressing months of effort into weeks
* **Cost-effective**: Automation handles repetitive work, freeing professional services for high-value tasks like integrations and strategic decisions
* **Accessible to anyone**: Natural language requests make website changes accessible to less technical users, with live preview to validate changes instantly
* **Enterprise governance**: Developers maintain full authority over what goes live through review workflows integrated with GitHub
* **Continuous value**: The agent supports ongoing site evolution, including style updates, template refinements, and landing page creation

## Site Creation and Migration Skills {#creation-migration}

The Experience Modernization Agent offers skills for creating new Edge Delivery Services sites and migrating existing websites. Any new Edge Delivery Services site or migration is encouraged to take advantage of these skills.

* Accelerates website creation and migrations from months to weeks or days, dramatically reducing time-to-value for Edge Delivery Services adoption
* Transforms websites from any CMS, legacy AEM, or design systems (like Figma) into production-ready Edge Delivery Services projects
* Delivers all Edge Delivery Services promises: AI-readiness for agentic capabilities, fast performance (Core Web Vitals optimized), accessibility (WCAG 2.1 AA), responsive design across all breakpoints, and content+code agility

Detailed skills include page migration, bulk import, design extraction, navigation setup, and web scraping.

## Block Development Capabilities {#block-development}

The Experience Modernization Agent takes advantage of general Edge Delivery Services development capabilities that serve various development tasks, providing continuous value beyond initial site creation or migration.

* Follows Content-Driven Development (CDD) methodology for author-friendly content models
* Leverages the [Block Collection](https://www.aem.live/developer/block-collection) and [Block Party](https://www.aem.live/developer/block-party/) to find reference implementations and best practices
* Supports testing and debugging workflows for validating changes before deployment

Detailed capabilities include block development, content modeling, reference block discovery, testing, and debugging.

## Experience Modernization Console {#console}

The Experience Modernization Agent provides a hosted AI-assisted development environment for Edge Delivery Services, exposed as a web interface at [`aemcoder.adobe.io`.](https://aemcoder.adobe.io)

* The console requires no local setup for users to start prompting changes immediately in natural language.
* Rapidly perform day-to-day experience development tasks while previewing them via live AEM preview, and sync content to AEM.
* Enterprise governance is enforced as developers retain full control over what ships via usual GitHub review and approval process.

The self-service Experience Modernization Console is generally available. Interested users can request access to ensure a smooth onboarding experience.

## Delivery Model {#delivery-model}

For complex migrations or accelerated outcomes, Adobe offers the Agentic Outcome Engineer (AOE) delivery model. This is an optional service where Adobe engineers operate the AI tooling on your behalf. For details on this delivery model, please see the document [Delivery Model of the Experience Modernization Agent.](/help/ai-in-aem/agents/brand-experience/modernization/delivery-model.md)

If you are interested in the AOE model for your next migration:

* Please contact your Adobe representative or account team to initiate scoping and scheduling.
* Adobe will confirm eligibility, estimate the engagement, and propose an engagement plan.

## Limitations {#limitations}

The following use cases require additional implementation effort in addition to the skills of the Experience Modernization Agent.

The scraping tool does not support the following sources.

* Intranet or protected sources such as content behind authentication, VPNs, or firewalls that is not accessible
* Complex dynamic content such as content requiring sophisticated user interaction to appear in the DOM.
  * Client-side rendered content is supported if the content is accessible via a specific URL.
  * Elements hidden via CSS but present in the DOM like tabs, accordions or carousels are also supported.

The agent does not support the following targets.

* AEM publish environments where sites use HTL-based delivery
  * The skills target Edge Delivery Services only.
* Headless delivery patterns such as API-only or SPA-based delivery (e.g., Next.js)

The following requirements are not covered by dedicated automation skills and require manual effort.

* Strict pixel perfection 
  * Only practical design fidelity is automated
* Integrations of server or client-side third-party data/services
* Integrations of commerce or search functionality
* MarTech data layer or targeting/experimentation
* Isolation of content/experience fragments
* Multisite inheritance (MSM)
* Custom functionality (e.g. calculators, configurators)
* Custom business logic

## Next Steps {#next-steps}

Get started by migrating a site using the document [Getting Started with the Experience Modernization Agent.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md)
