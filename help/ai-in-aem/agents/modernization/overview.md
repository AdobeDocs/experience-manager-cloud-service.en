---
title: Experience Modernization Agent Overview
description: Learn how the Experience Modernization Agent onboards new websites into Edge Delivery Services with the help of AI.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
---

# Experience Modernization Agent Overview {#experience-modernization-agent}

Learn how the Experience Modernization Agent onboards websites into Edge Delivery Services with the help of AI.

>[!NOTE]
>
>The Experience Modernization Agent supersede the former migration skill of the [Experience Production Agent.](/help/ai-in-aem/agents/production/overview.md)

## Introduction {#introduction}

The Experience Modernization Agent unlocks the full value of Edge Delivery Services (including AEM authoring) by making website migrations and ongoing evolution fast and frictionless.

It combines [site creation and migration skills](#creation-migration) for initial onboarding and [block development skills](#block-development) for continuous experience development (style updates, template refinements, landing page creation) with the help of AI and Adobe Forward Deployed Engineers (FDEs). In addition, it offers the [Experience Modernization Console](#console) as a hosted AI-assisted development environment available to FDEs and to you, the user, directly.

## Site Creation and Migration Skill {#creation-migration}

The Experience Modernization Agent offers skills for creating new [Edge Delivery Services](/help/edge/overview.md) sites and migrating existing websites. Any new Edge Delivery Services site or migration is encouraged to take advantage of these skills.

* Accelerates website creation and migrations from months to weeks or days, dramatically reducing time-to-value for Edge Delivery Services adoption
* Transforms websites from any CMS, legacy AEM, or design systems (like Figma) into production-ready Edge Delivery Services projects
* Delivers all Edge Delivery Services promises: AI-readiness for agentic capabilities, fast performance (Core Web Vitals optimized), accessibility (WCAG 2.1 AA), responsive design across all breakpoints, and content+code agility

Detailed skills include page migration, bulk import, design extraction, navigation setup, and web scraping.

## Block Development Skills {#block-development}

The Experience Modernization Agent takes advantage of general Edge Delivery Services development skills that serve various development tasks, providing continuous value beyond initial site creation or migration.

* Follows Content-Driven Development (CDD) methodology for author-friendly content models
* Leverages the [Block Collection](https://www.aem.live/developer/block-collection) and [Block Party](https://www.aem.live/developer/block-party/) to find reference implementations and best practices
* Supports testing and debugging workflows for validating changes before deployment

Detailed skills include block development, content modeling, reference block discovery, testing, and debugging.

## Experience Modernization Console {#console}

The Experience Modernization Agent provides a hosted AI-assisted development environment for Edge Delivery Services, exposed as a web interface at [`aemcoder.adobe.io`.](https://aemcoder.adobe.io)

* The console requires no setup for users to start prompting changes immediately in natural language, making it accessible to anyone
* Rapidly perform day-to-day experience development tasks while previewing them via live AEM preview, and sync content to AEM.
* Enterprise governance is enforced as developers retain full control over what ships via usual GitHub review and approval process.

## Delivery Model {#delivery-model}

Technology alone does not guarantee outcomes. The Adobe Forward Deployed Engineer (FDE) delivery model pairs AI automation with Adobe expertise to ensure the success of migrations, providing your projects with clear scope, shared accountability, and knowledge transfer throughout the engagement.

* Adobe FDEs operate the agent alongside you, combining AI automation with expert guidance to deliver production-ready results at scale.
* This provides a strategic reset option for enterprises facing stalled implementations or legacy modernization challenges.
* The FDE model offers a faster, lower-risk path forward that leverages AI automation while ensuring governance, quality, and successful outcomes.

To further explore the Experience Modernization Agent:

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

The following requirements are not yet covered with dedicated automation skills and require manual effort.

* Strict pixel perfection 
  * Only practical design fidelity is automated
* Integrations of server or client-side third-party data/services
* Integrations of commerce or search functionality
* MarTech data layer or targeting/experimentation
* Isolation of content/experience fragments
* Multisite inheritance (MSM)
* Custom functionality (e.g. calculators, configurators)
* Custom business logic
