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

EDS is the AEM service that delivers websites. It serves authored content as plain semantic HTML, and the project's own CSS and JavaScript style and decorate it in the browser. If you already build with HTML, CSS, and JavaScript, most of an EDS project will look familiar. The AEM-specific parts are explained in [Understand Your Project](#project-foundations).

## Introduction {#introduction}

EMA is part of the [Brand Experience Agent.](/help/ai-in-aem/agents/brand-experience/overview.md) It automates repetitive work: importing content, mapping it to blocks, styling, and development. You work in a hosted console, using natural-language requests and previews. You don't need Docker or a local command-line environment.

EMA exists to help you move your web properties onto the current AEM website stack: EDS, with content that authors edit visually in Experience Workspace. That is where you get the full value of the platform: fast pages, lean HTML, CSS, and JavaScript code, reusable blocks, and a site that you can keep changing with the agent's help after launch. EMA also supports EDS with AEM authoring when your project needs it. See [Where Content Is Stored and How Authors Edit It](#content-storage).

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

An EMA task touches several separate parts of a project. Keep them apart when you start:

* **Source:** The authorized website, content, or design that you provide.
* **Code:** The EDS Git repository and working branch that contain styles, scripts, and blocks.
* **Content destination:** Where the migrated content is stored and which editor authors use. Adobe strongly recommends document-based persistence with Experience Workspace for new implementations; AEM authoring with JCR persistence and the Universal Editor is the alternative. See [Where Content Is Stored and How Authors Edit It](#content-storage). The source CMS does not determine this choice.
* **Preview and publication:** Where you verify the result and, separately, where you release approved changes.

EDS supports complex enterprise websites. Search, commerce, personalization, and other integrations can require project-specific implementation and testing; they are not reasons to restrict EDS to simple or static sites.

### How EDS Pages Work {#eds-basics}

EDS stores code and content in different places. Blocks, styles, and scripts live in a Git repository. Content lives in a separate content source that authors edit. Authors can change pages without a code release, and developers can change code without touching content. It also means that pushing code never saves content, and uploading content never changes code.

When EDS renders a page, it turns the authored content into plain semantic HTML:

* **Default content** is everything outside blocks: headings, paragraphs, lists, images, and links.
* A **block** is a reusable component, such as a hero or a set of cards. In the HTML, it is a `div` with the block name as its class. The project's `blocks/<name>/<name>.js` and `blocks/<name>/<name>.css` decorate it in the browser.
* **Sections** split a page into groups of default content and blocks, for example to give part of a page a different background.

Most projects start from the [AEM boilerplate](https://github.com/adobe/aem-boilerplate), which is written in plain JavaScript and CSS. You check changes on the preview site, served on `*.aem.page`. Publishing releases them to the live site on `*.aem.live`.

### Names You May See {#names}

Adobe has renamed several of these products. The table maps the names that appear in these docs, the console, and URLs.

| Name | What it refers to |
|---|---|
| Brand Experience Agent | The family of AEM agents that EMA belongs to. |
| Experience Modernization Agent (EMA) | The agent described in these docs. |
| Experience Modernization Console | The web interface where you use EMA, at `aemcoder.adobe.io`. |
| Edge Delivery Services (EDS) | AEM's website delivery service. It was earlier called Project Helix and then Franklin, which is why some hostnames, such as `admin.hlx.page`, contain `hlx`. |
| Experience Workspace | The visual authoring UI for document-based EDS content, at `da.live`. It was formerly called Document Authoring (DA), and some console labels still use that name. |
| Universal Editor | Adobe's visual editor for content stored in AEM. EDS projects with AEM authoring use it. |
| AEM authoring, JCR persistence | EDS with content stored in AEM's Java Content Repository (JCR) on an AEM as a Cloud Service author instance. |
| IMS | Adobe's identity service, which handles sign-in with your Adobe ID. |

## Where Content Is Stored and How Authors Edit It {#content-storage}

EMA asks where the migrated content should be stored. This is a question about persistence: which repository holds the content. Which editor authors use is a separate question. With either option, authors get a visual editor and EDS delivers the pages.

| | Document-based persistence | AEM authoring with JCR persistence |
|---|---|---|
| Where content is stored | The EDS document-based content repository | AEM's JCR, on the AEM as a Cloud Service author stack |
| Visual editor | Experience Workspace | Universal Editor |
| Page delivery | EDS | EDS |
| Recommendation | Strongly recommended for new implementations, including large sites | Fully supported; choose it when a requirement depends on content staying in the AEM repository |

### Document-Based Persistence with Experience Workspace {#document-based}

With document-based persistence, content is stored as documents in the EDS document-based content repository. "Document-based" describes storage only, not the authoring experience. Authors edit pages visually in [Experience Workspace,](https://www.aem.live/docs/ew/about) the visual authoring UI for EDS. Experience Workspace also offers an AI assistant, collaboration, and AEM Assets integration. It is off by default and is turned on per site or organization. Google Docs and SharePoint remain supported EDS content sources.

>[!NOTE]
>
>Experience Workspace is the new name of Document Authoring (DA). The change is an upgrade, not a content migration: existing DA content stays where it is, and the editor still runs at `da.live`. Some console labels and screens still say **Document Authoring** or **DA**. In these docs, they refer to the same document-based repository and its editor.

### AEM Authoring with JCR Persistence {#jcr-persistence}

With AEM authoring, content is stored in AEM's Java Content Repository (JCR), on the AEM as a Cloud Service author stack. This is EDS running on top of the JCR stack. Authors edit pages with the [Universal Editor,](/help/implementing/universal-editor/introduction.md) Adobe's visual editor for content in AEM, and EDS still delivers the pages. The pages are not rendered by HTL and Java as in traditional AEM publishing. Template repositories for this setup, such as `aem-block-collection-xwalk`, use `xwalk` (crosswalk) in their names.

>[!NOTE]
>
>In these docs, *AEM authoring* names this persistence option. The *AEM author instance* is the AEM as a Cloud Service environment where that content is stored and edited.

### Adobe's Recommendation {#recommendation}

For any new EDS implementation, Adobe strongly recommends document-based persistence with Experience Workspace over AEM authoring with the Universal Editor. This includes large websites with thousands of pages.

Document-based authoring used to mean editing in Microsoft Word, Google Docs, or a document-style editor. That limited visual page editing, so teams that needed it often chose AEM authoring. Experience Workspace now gives document-based content a visual editor, so there is little reason left for a brand to avoid it.

AEM authoring with JCR persistence remains fully supported. Choose it when a specific requirement depends on content staying in the AEM repository. For headless content, delivered through APIs rather than as EDS web pages, the Universal Editor remains the recommended editor.

## Benefits {#benefits}

EMA shortens the work of adopting [Edge Delivery Services](/help/edge/overview.md) and of changing your site afterward.

* Import representative pages, refine reusable mappings, then apply them to further pages.
* Use natural language to request changes and inspect the resulting content and code.
* Reuse EDS content and block patterns rather than reproduce unnecessary source-system complexity.
* Continue development in the connected repository and authoring environment.

## Site Creation and Migration Skills {#creation-migration}

Skills are the agent's built-in workflows for specific kinds of tasks. Use the creation and migration skills for any new EDS site or migration.

* Imports content from reachable source pages and maps it to [default content and blocks.](#eds-basics)
* Separates content migration from faithful design migration or a deliberate redesign.
* Supports document-based and AEM authoring projects through their respective setup and delivery workflows.

Detailed skills include page migration, bulk import, design extraction, navigation setup, and web scraping.

## Figma-Based Migrations and Page Creation {#figma}

In addition to live-site migrations, EMA can use Figma as a design source. To use these capabilities, set up your Figma details in [the Experience Modernization Console.](/help/ai-in-aem/agents/brand-experience/modernization/console.md)

### Redesign Migration Using Figma-Derived Blocks {#figma-redesign}

When you migrate an existing website into a redesigned experience, the agent [first creates the redesigned block collection from Figma components.](/help/ai-in-aem/agents/brand-experience/modernization/prompting-guide.md#figma-redesign-migration) It then runs site migration against the live source website and maps source content into those Figma-derived blocks.

* **Figma** is the target design and block-library source.
* **The live website** remains the source of content.
* Content is validated against the source website; visual output is validated against the Figma-derived design system.

### Create a New Page from Figma {#figma-new-page}

When a page does not exist on a source website, the agent [generates a new EDS page directly from a Figma frame or page.](/help/ai-in-aem/agents/brand-experience/modernization/prompting-guide.md#figma-new-page-from-figma) It maps Figma sections to existing blocks, default content, or new variants. Text and assets come from Figma.

For details on these workflows, individual Figma block migration, and prompting tips, see the [Prompting Guide for the Experience Modernization Agent.](/help/ai-in-aem/agents/brand-experience/modernization/prompting-guide.md)

## Block Development Capabilities {#block-development}

EMA uses general EDS development capabilities, so it remains useful after the initial site creation or migration.

* Follows Content-Driven Development (CDD): it starts from real content and the author's needs, then writes code, which keeps content models author-friendly.
* Uses the Adobe-maintained [Block Collection](https://www.aem.live/developer/block-collection) and the community-driven [Block Party](https://www.aem.live/developer/block-party/) to find reference implementations and best practices.
* Supports testing and debugging workflows for validating changes before deployment.

Detailed capabilities include block development, content modeling, reference block discovery, testing, and debugging.

## Experience Modernization Console {#console}

The Experience Modernization Console is EMA's web-based, AI-assisted development environment for EDS, at [`aemcoder.adobe.io`.](https://aemcoder.adobe.io)

* The console requires no local setup, so you can start prompting changes in natural language right away.
* You perform day-to-day development tasks, check them in a live AEM preview, and save content to your authoring destination.
* The console supports enterprise governance through standard GitHub review workflows.
* The AI agent works without receiving the credentials that you configure. See [Security and Data Handling.](#security)

The self-service Experience Modernization Console is generally available. You can request access to ensure a smooth onboarding experience.

To get started with the console:

* For document-based persistence with Experience Workspace, recommended for new implementations, [use the getting started guide.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md)
* For AEM authoring with JCR persistence and the Universal Editor, [use the AEM authoring guide.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started-aem-authoring.md)

## Project Documentation Skill {#project-documentation}

[Generate project documentation](project-documentation.md) for authors, developers, and administrators. Review its coverage against the connected code and accessible configuration. Record remaining work and validated examples for the next person or agent.

## Site Catalog Skill {#site-catalog}

The site catalog skill analyzes discovered pages, groups them into templates (pages that share a layout) and block variants, and provides screenshots and a report for review. Discovery and analysis can be partial. The skill helps:

* **Anyone starting a migration project** to establish an inventory of page layouts, block variants, locales, and pages per template, then reconcile it with the agreed site scope
* **Teams doing bulk imports** to identify which pages share the same layout, manually import and perfect the representative pages first, then bulk-import all remaining pages for that template
* **Project leads and stakeholders** to understand the scope of the effort

For details, see [Site Catalog Skill.](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md)

## Agentic Outcome Engineer (AOE) Delivery {#aoe-delivery}

For complex migrations or accelerated outcomes, Adobe offers Agentic Outcome Engineer (AOE) delivery. In this optional service, Adobe engineers operate EMA on your behalf and combine its automation with engineering work and expert guidance to deliver production-ready results. For details, see [AOE Delivery of the Experience Modernization Agent.](/help/ai-in-aem/agents/brand-experience/modernization/aoe-delivery.md)

If you are interested in the AOE model for your next migration:

* Contact your Adobe representative or account team to start scoping and scheduling.
* Adobe confirms eligibility, estimates the engagement, and proposes an engagement plan.

## Security and Data Handling {#security}

EMA lets the AI agent work on your site without giving it the credentials that you configure, and you decide when changes reach your repositories and AEM.

### Access and Isolation {#security-access}

* You sign in to the console with your Adobe ID. Every request is authenticated with Adobe Identity Management Services (IMS).
* Each user works in a separate backend environment with its own workspace storage. Your workspace is not shared with other users.
* AEM and your Git provider continue to enforce their own permissions for any code or content that EMA writes.

### Credentials {#security-credentials}

* The AI agent does not receive the credentials that you configure in the console. Tokens for GitHub, Cloud Manager Git repositories, Document Authoring, Figma, and protected source sites are held outside the agent's environment. A separate component adds each credential only to requests for the service it belongs to. The same applies to the credential used to call the AI model.
* [Agent permissions](console.md#settings-page) are off until you turn them on. Turning one on lets the agent act with that access, for example to push to your repository, without seeing the credential. Use scoped, least-privilege tokens.
* Store credentials only in the console's settings. Do not put secrets in prompts, chat, source content, repository files, or project documentation. The agent reads these, and they can be sent to the AI model.

### What the AI Model Processes {#security-model-data}

To perform your request, EMA can send the following to the large language model (LLM):

* Your prompts and instructions.
* Source page URLs, markup, and content, or exported CMS content.
* Repository code and configuration, such as blocks, styles, and site configuration.
* Design and brand references, such as Figma designs and screenshots.
* Generated content and code under review.

Adobe does not use customer data to train or fine-tune LLMs.

### Control over Changes {#security-control}

* The agent works in your workspace. You review its changes and the preview in the console.
* Without agent permissions, code reaches your Git repository and content reaches AEM only when you use the console's synchronization actions. Optional plan mode lets you approve a plan before the agent starts.
* Treat source pages and design files as untrusted input. They can contain text that attempts to steer the agent. Review the changes before you push, preview, or publish them. Branch protection and pull request reviews in your repository still apply.

### Encryption and Storage {#security-storage}

* Data is encrypted in transit using TLS 1.2 or later, and at rest using AES 256-bit encryption.
* Code that you push is stored in your Git repository, and content that you sync is stored in your AEM content repository. Their own retention and version history policies apply.

For processing locations, data retention, and compliance information, contact your Adobe account team or see the [Adobe Trust Center.](https://www.adobe.com/trust.html)

## Limitations {#limitations}

Use only websites and designs that you are authorized to migrate. The selected workflow must be able to reach and read the source. If the site uses bot protection, arrange access with its administrator. See [source sites with bot protection](getting-started.md#bot-protection).

* In the console, **Protected site authentication** in [Settings](console.md#settings-page), where available, lets the agent reach password-protected source sites using basic, bearer, or custom-header credentials. Auto mode offers its own authentication fields. Neither establishes access to VPN-only sources. Use the credential controls offered by your workflow; do not put secrets in chat.
* Client-rendered content can be captured when available at the page URL. Content present in the DOM but hidden by CSS can also be extracted. Content requiring additional interactions needs representative checks and may need a different extraction approach.
* EMA targets EDS, including EDS with [JCR-backed AEM authoring.](#jcr-persistence) It does not convert a project to HTL-based AEM publishing or an API-only/SPA delivery stack.
* Faithful design, accessibility, performance, and functional behavior require validation. A visual similarity score is not a production acceptance criterion.
* Integrations, custom business logic, analytics, experimentation, and source-system features such as inheritance or content fragments need an explicit implementation and migration decision. Do not assume automated page import recreates them.

Access to auto mode and optional design capabilities can differ from access to the console. Check the controls and limits shown for your account. [AOE service scope](aoe-delivery.md#scope) is agreed separately from product capabilities.

## Next Steps {#next-steps}

Choose a task above, then use [Getting Started](getting-started.md) for shared console setup. For an existing EDS project, connect its repository and start with the relevant development or restyling task; a new migration is not required.

To learn what changed in recent versions of the console, see the [Experience Modernization Agent release notes.](/help/release-notes/modernization-agent/current.md)
