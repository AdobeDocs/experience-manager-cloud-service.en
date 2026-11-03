---
title: Experience Modernization Agent Overview
description: Use the Experience Modernization Agent to create, migrate, restyle, and develop Edge Delivery Services websites.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: c23a6f55-2ba8-4290-b7e8-06cad5de0fc8
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: f2d27a5f-0d67-4d85-8a24-86a8d8a3574b
    internal-label: Developer tools
  - id: ac5ecfc1-cc78-4ecc-a90a-0362685062ce
    internal-label: AI Tools
subfeature_v2:
  - id: f88183b7-5ea5-436c-ac46-96b53f0281ea
    internal-label: Edge Delivery Services
  - id: f1710108-e0d1-47e5-9952-1888729a03da
    internal-label: Agentic AI
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---

# Experience Modernization Agent Overview {#experience-modernization-agent}

Use the Experience Modernization Agent (EMA) to create, migrate, restyle, and develop websites on [Edge Delivery Services (EDS)](/help/edge/overview.md).

## Introduction {#introduction}

[As part of the Brand Experience Agent,](/help/ai-in-aem/agents/brand-experience/overview.md) EMA automates repetitive content import, block mapping, styling, and development work. You work in a hosted console, using natural-language requests and previews. No local Docker or command-line environment is required.

EMA also works on existing EDS projects after migration. You can refine a design, create or update blocks, and refactor code. Your permissions, repository policies, and publication workflow determine what you can change and release.

## Choose Your Task {#choose-task}

| Your goal | Start here | Done when |
|---|---|---|
| Demonstrate a few customer pages | [Create a customer demo](getting-started.md#customer-demo) | The selected branded pages and demo paths work, with unfinished behavior identified. |
| Try EDS and EMA with your brand's content | [Trial your own content](getting-started.md#brand-trial) | You can make a useful edit, retain the work, and return to it. |
| Migrate a production site | [Production migration](production-migration.md) | The agreed inventory, authoring, integrations, and release checks are accepted. |
| Apply a new design during migration | [Restyle during migration](restyling.md#during-migration) | Source content is preserved in the approved target design. |
| Restyle an existing EDS site | [Restyle an existing site](restyling.md#existing-site) | The affected pages adopt the design without unintended content or behavior changes. |
| Create, update, or refactor blocks | [Block development](block-development.md) | Reusable code and authorable examples pass the agreed checks. |

A successful automated run or attractive preview is not, by itself, a production-ready site. Use the completion checks for your task.

## Understand Your Project {#project-foundations}

Keep these identities separate when you start a task:

* **Source:** The authorized website, content, or design that you provide.
* **Code:** The EDS repository and working branch that contain styles, scripts, and blocks.
* **Content destination:** Either document-based persistence, used with Experience Workspace/Document Authoring, or AEM authoring with JCR persistence and the Universal Editor. The source CMS does not determine this choice.
* **Preview and publication:** Where you verify the result and, separately, where you release approved changes.

EDS supports complex enterprise websites. Search, commerce, personalization, and other integrations can require project-specific implementation and testing; they are not reasons to restrict EDS to simple or static sites.

## Benefits {#benefits}

The Experience Modernization Agent accelerates the time to value for [Edge Delivery Services](/help/edge/overview.md) adoption and gives you the agility to adapt your brand's web experience.

* Import representative pages, refine reusable mappings, then apply them to further pages.
* Use natural language to request changes and inspect the resulting content and code.
* Reuse EDS content and block patterns rather than reproduce unnecessary source-system complexity.
* Continue development in the connected repository and authoring environment.

## Site Creation and Migration Skills {#creation-migration}

The Experience Modernization Agent offers skills for creating new Edge Delivery Services sites and migrating existing websites. Any new Edge Delivery Services site or migration is encouraged to take advantage of these skills.

* Imports content from reachable source pages and maps it to default content and blocks.
* Separates content migration from faithful design migration or a deliberate redesign.
* Supports document-based and AEM authoring projects through their respective setup and delivery workflows.

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

[Generate project documentation](project-documentation.md) for authors, developers, and administrators. Review its coverage against the connected code and accessible configuration. Record remaining work and validated examples for the next person or agent.

## Site Catalog Skill {#site-catalog}

The site catalog skill analyzes discovered pages, groups templates and block variants, and provides screenshots and a report for review. Discovery and analysis can be partial. This skill is valuable to:

* **Anyone starting a migration project** to establish an inventory of page layouts, block variants, locales, and pages per template, then reconcile it with the agreed site scope
* **Teams doing bulk imports** to identify which pages share the same layout, manually import and perfect the representative pages first, then bulk-import all remaining pages for that template
* **Project leads and stakeholders** to understand the scope of the effort

Please see the document [Site Catalog Skill](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md) for more information.

## Agentic Outcome Engineer (AOE) Delivery {#aoe-delivery}

For complex migrations or accelerated outcomes, Adobe offers the Agentic Outcome Engineer (AOE) delivery. This is an optional service where Adobe engineers operate the Experience Modernization Agent on your behalf, combining AI automation with expert guidance to deliver production-ready results at scale. For details on AOE delivery, please see the document [AOE Delivery of the Experience Modernization Agent.](/help/ai-in-aem/agents/brand-experience/modernization/aoe-delivery.md)

If you are interested in the AOE model for your next migration:

* Please contact your Adobe representative or account team to initiate scoping and scheduling.
* Adobe will confirm eligibility, estimate the engagement, and propose an engagement plan.

## Limitations {#limitations}

Use only websites and designs that you are authorized to migrate. The selected workflow must be able to reach and read the source. If the site uses bot protection, arrange access with its administrator. See [source sites with bot protection](getting-started.md#bot-protection).

* In the console, **Protected site authentication** in [Settings](console.md#settings-page), where available, lets the agent reach password-protected source sites using basic, bearer, or custom-header credentials. Auto mode offers its own authentication fields. Neither establishes access to VPN-only sources. Use the credential controls offered by your workflow; do not put secrets in chat.
* Client-rendered content can be captured when available at the page URL. Content present in the DOM but hidden by CSS can also be extracted. Content requiring additional interactions needs representative checks and may need a different extraction approach.
* EMA targets EDS, including EDS with JCR-backed authoring. It does not convert a project to HTL-based AEM publishing or an API-only/SPA delivery stack.
* Faithful design, accessibility, performance, and functional behavior require validation. A visual similarity score is not a production acceptance criterion.
* Integrations, custom business logic, analytics, experimentation, and source-system features such as inheritance or content fragments need an explicit implementation and migration decision. Do not assume automated page import recreates them.

Access to auto mode and optional design capabilities can differ from access to the console. Check the controls and limits shown for your account. [AOE service scope](aoe-delivery.md#scope) is agreed separately from product capabilities.

## Next Steps {#next-steps}

Choose a task above, then use [Getting Started](getting-started.md) for shared console setup. For an existing EDS project, connect its repository and start with the relevant development or restyling task; a new migration is not required.

To learn what changed in recent versions of the console, see the [Experience Modernization Agent release notes.](/help/release-notes/modernization-agent/current.md)
