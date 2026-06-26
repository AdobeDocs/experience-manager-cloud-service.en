---
title: Experience Modernization Agent Overview
description: Learn how the Experience Modernization Agent onboards new websites into Edge Delivery Services with the help of AI.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: c23a6f55-2ba8-4290-b7e8-06cad5de0fc8
---

# Experience Modernization Agent Overview {#experience-modernization-agent}

Learn how the Experience Modernization Agent onboards websites into Edge Delivery Services with the help of AI.

## Introduction {#introduction}

[As part of the Brand Experience Agent,](/help/ai-in-aem/agents/brand-experience/overview.md) the Experience Modernization Agent accelerates onboarding to Edge Delivery Services by automating website migrations and foundational site setup.

It combines [site creation and migration skills](#creation-migration) for initial website onboarding and [block development capabilities](#block-development) to support site creation and migration workflows. In addition, it offers the [Experience Modernization Console](#console) as a web-based AI-assisted development environment available to you directly. While users can operate the agent directly through that console, developers retain full control over what ships.

For complex or high-priority migrations, Adobe offers the [Agentic Outcome Engineer (AOE) delivery model,](#aoe-delivery) an engineering-led service designed to deliver production-ready Edge Delivery sites using the Experience Modernization Agent.

## Benefits {#benefits}

The Experience Modernization Agent accelerates the time to value for [Edge Delivery Services](/help/edge/overview.md) adoption and gives you the agility to adapt your brand's web experience.

* **High velocity**: AI automation handles repetitive migration work (content import, block mapping, design system application), compressing migration timelines compared to traditional approaches
* **Efficiency-Focussed**: Automation reduces repetitive work, allowing teams to focus on higher-value implementation work
* **Accessible to anyone**: Natural language requests make website changes accessible to less technical users, with live preview to validate changes instantly
* **Enterprise governance**: Developers maintain full authority over what goes live through review workflows integrated with GitHub
* **Post-migration flexibility**: Enables teams to extend and refine migrated sites using Edge Delivery Services patterns

## Site Creation and Migration Skills {#creation-migration}

The Experience Modernization Agent offers skills for creating new Edge Delivery Services sites and migrating existing websites. Any new Edge Delivery Services site or migration is encouraged to take advantage of these skills.

* Accelerates website creation and migrations from months to weeks or days, dramatically reducing time-to-value for Edge Delivery Services adoption
* Supports migrations from a wide range of CMS platforms, legacy AEM, or design systems (like Figma) into production-capable Edge Delivery Services projects
* Supports best practices for performance, accessibility, and responsive design aligned with Edge Delivery Services guidance

Detailed skills include page migration, bulk import, design extraction, navigation setup, and web scraping.

## Figma-Based Migrations and Page Creation {#figma}

In addition to live-site migrations, the Experience Modernization Agent can use Figma as a design source. To use these capabilities, set up your Figma details in [the Experience Modernization Console.](/help/ai-in-aem/agents/brand-experience/modernization/console.md)

### Redesign Migration Using Figma-Derived Blocks {#figma-redesign}

When you are migrating an existing website into a redesigned experience, the agent [first establishes the redesigned block collection from Figma components,](/help/ai-in-aem/agents/brand-experience/modernization/prompting-guide.md#figma-redesign-migration) and then runs site migration against the live source website and maps source content into those Figma-derived blocks.

* **Figma** is the target design and block-library source.
* **The live website** remains the source of content.
* Content is validated against the source website; visual output is validated against the Figma-derived design system.

### Create a New Page from Figma {#figma-new-page}

When a page does not already exist on a source website, the agent [generates a new Edge Delivery Services page directly from a Figma frame or page,](/help/ai-in-aem/agents/brand-experience/modernization/prompting-guide.md#figma-new-page-from-figma) mapping Figma sections to existing blocks, default content, or new variants. Text and assets come from Figma.

For details on these workflows, individual Figma block migration, and prompting tips, see the [Prompting Guide for the Experience Modernization Agent.](/help/ai-in-aem/agents/brand-experience/modernization/prompting-guide.md)

## Block Development Capabilities {#block-development}

The Experience Modernization Agent takes advantage of general Edge Delivery Services development capabilities that serve various development tasks, providing continuous value beyond initial site creation or migration.

* Follows Content-Driven Development (CDD) methodology for author-friendly content models
* Leverages the [Block Collection](https://www.aem.live/developer/block-collection) and [Block Party](https://www.aem.live/developer/block-party/) to find reference implementations and best practices
* Supports testing and debugging workflows for validating changes before deployment

Detailed capabilities include block development, content modeling, reference block discovery, testing, and debugging.

## Experience Modernization Console {#console}

The Experience Modernization Agent provides a web-based AI-assisted development environment for Edge Delivery Services, exposed as a web interface at [`aemcoder.adobe.io`.](https://aemcoder.adobe.io)

* The console requires no local setup for users to start prompting changes immediately in natural language.
* Rapidly perform day-to-day experience development tasks while previewing them via live AEM preview, and sync content to AEM.
* The console supports enterprise governance through standard GitHub review workflows.

The self-service Experience Modernization Console is generally available. Interested users can request access to ensure a smooth onboarding experience.

Get started with the Experience Modernization Console!

* If you are modernizing your site by targeting Document Authoring, [get started here.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md)
* If you are modernizing your site by targeting AEM authoring, [get started here.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started-aem-authoring.md)

## Project Documentation Skill {#project-documentation}

Recognizing the time-intensive nature of project handovers, [the project documentation skill](/help/ai-in-aem/agents/brand-experience/modernization/project-documentation.md) can automatically generate comprehensive documentation once authoring and development work is complete.

## Site Catalog Skill {#site-catalog}

The site catalog skill crawls an existing website, catalogs all page templates and block variants, captures screenshots of every template and block, and generates an interactive HTML report bundle for review. This skill is valuable to: 

* **Anyone starting a migration project** in order to get a complete inventory of page layouts, block variants, locales, and pages-per-template before writing any code, so teams can plan accurately and surface complexity early
* **Teams doing bulk imports** to identify which pages share the same layout, manually import and perfect the representative pages first, then bulk-import all remaining pages for that template
* **Project leads and stakeholders** to understand the scope of the effort

Please see the document [Site Catalog Skill](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md) for more information.

## Agentic Outcome Engineer (AOE) Delivery {#aoe-delivery}

For complex migrations or accelerated outcomes, Adobe offers the Agentic Outcome Engineer (AOE) delivery. This is an optional service where Adobe engineers operate the Experience Modernization Agent on your behalf, combining AI automation with expert guidance to deliver production-ready results at scale. For details on AOE delivery, please see the document [AOE Delivery of the Experience Modernization Agent.](/help/ai-in-aem/agents/brand-experience/modernization/aoe-delivery.md)

If you are interested in the AOE model for your next migration:

* Please contact your Adobe representative or account team to initiate scoping and scheduling.
* Adobe will confirm eligibility, estimate the engagement, and propose an engagement plan.

## Limitations {#limitations}

The following use cases require additional implementation effort in addition to the skills of the Experience Modernization Agent.

The scraping skill does not support the following sources.

* Intranet or protected sources such as content behind authentication, VPNs, or firewalls that is not accessible
  * As an alternative, use [SLICC](https://www.sliccy.com) which can leverage the authentication context from your browser to access protected sources.
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

