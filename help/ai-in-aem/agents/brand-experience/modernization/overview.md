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

The Experience Modernization Agent is Adobe's AI development agent for [Edge Delivery Services](/help/edge/overview.md). It gives you a ready-to-use development environment for these sites in the browser, with nothing to install, and an agent that migrates, builds, and evolves them, including their integrations with your other systems. Your Git repository remains the system of record for the site's code. To go straight to the guide for your role or task, see [Choose Where to Start](#start-by-role).

Edge Delivery Services is the part of Adobe Experience Manager Sites that delivers websites. It serves authored content as plain semantic HTML, and the project's own CSS and JavaScript style and decorate it in the browser. If you already build with HTML, CSS, and JavaScript, most of the project will look familiar. The parts specific to Experience Manager are explained in [Understand Your Project](#project-foundations). Adobe has renamed several of these products over time. If you meet older names such as Helix, Franklin, or Crosswalk, or short forms of these names, see [Names You May See](#names).

The Experience Modernization Agent is part of the [Brand Experience Agent](/help/ai-in-aem/agents/brand-experience/overview.md). Use it to move web properties onto Edge Delivery Services from other CMSes, from Experience Manager sites built with Java and HTL components, or from static sites. The agent reads each source page as a browser renders it, so the system behind the source doesn't matter: it works from the content and design that visitors see. Edge Delivery Services gives the new site:

* **Fast pages:** A new project from the AEM boilerplate scores 100 in Lighthouse. See [Keeping It 100](https://www.aem.live/developer/keeping-it-100).
* **Room to grow:** The platform runs multi-market, multi-language sites, the largest with more than 100,000 pages.
* **Visual authoring:** Authors edit pages in Experience Workspace, or in the Universal Editor. See [Where Content Is Stored and How Authors Edit It](#content-storage).
* **Content that crawlers can read:** The main content of each page is in the HTML that the platform serves, so search engines and AI assistants read it without running the page's scripts.

The agent rebuilds your pages on a block system that follows the architecture of Edge Delivery Services. It decomposes each page into sections and maps their content to [default content and reusable blocks](production-migration.md#content-structure). It extracts the design system into CSS design tokens for colors, fonts, and spacing, then writes the global styles and block CSS that use them. It does not clone the source markup, which would carry over any technical debt in it. Expect a close first pass that you refine by prompting and validate before you scale. See [How Close the Design Gets](prompting-guide.md#design-fidelity).

![Your site today, with its design, content, dynamic features such as news lists, search, forms, and integrations, and tags and analytics, plus the Experience Modernization Agent equals your site on Edge Delivery Services. The agent reads each page as a browser renders it, analyzes the structure into templates, sections, and blocks, imports the content into default content and blocks, and rebuilds the design as design tokens and CSS. It then compares the result with the source and iterates. After that, you ask and the agent expands, redesigns, optimizes, or integrates the site. On the new site, the design becomes design tokens, global styles, and block CSS, and authors edit the content and assets visually. News, search, forms, and integrations are rebuilt faithfully, and tags and analytics move one to one with the original.](assets/what-the-agent-does.png)

You stay in control of every change. The agent works in your own console workspace, and nothing reaches your project until you push code or upload content, or let the agent do so. See [Work Safely in an Independent Workspace](#independent-workspace).

## Why Use the Agent {#benefits}

Before anyone can judge a migration to Edge Delivery Services, a developer has a lot of repetitive work to do. They list the source pages and work out which ones share a layout. They decide how each part of a page maps to blocks and default content, then write the blocks and their styles and extract the colors and fonts. Finally, they write import scripts, import the pages, and compare them with the originals. The agent does this work with you, in one environment:

* **A first result on your own pages.** Give [Auto mode](getting-started.md#brand-trial) your website's URL, and it migrates a set of pages, including their design, and emails you when it finishes. Or give the agent pages in the console, and check the blocks, styles, and editable content that it builds in the preview. Either way, you judge the approach on your own content rather than on a sample site.
* **A plan that you can see.** The [site catalog](site-catalog.md) inventories the source site and groups its pages into templates and blocks, with screenshots. Use it to scope and size the project and to decide what to migrate first.
* **Fixes that scale.** The agent turns each correction into a change to a reusable block or import script, so a fix on one page applies to every page of that template. See [How the Agent Migrates at Scale](production-migration.md#migration-at-scale).
* **A standard project that you own.** The result is plain Edge Delivery Services code in your Git repository that follows the conventions of the AEM boilerplate and the [Block Collection](https://www.aem.live/developer/block-collection). Developers can continue in the console, in their own editor, or with other AI tools. Nothing ties the site to the Experience Modernization Agent.
* **Help after go-live.** The migration isn't the end of the agent's work. Your team keeps using it once the site is live: to apply a new brand design from Figma, build new pages from existing blocks, or track down a bug. It can also audit the site's performance, accessibility, and SEO, then fix what the audit finds. See [Restyle Sites](restyling.md), [Guided Redesign](restyling.md#guided-redesign), and [Create, Update, and Refactor Blocks](block-development.md).
* **Project knowledge that lasts.** The agent follows the conventions that you keep in `AGENTS.md` and related files in the repository, so every conversation starts with what your team has agreed. See [Project Instructions and Memory](project-instructions.md).
* **Integrations with your other systems.** The agent doesn't only migrate pages. It writes the blocks and code that connect the site to the services it relies on, such as a commerce platform, marketing tools, a maps or video service, or your own APIs. It works on them as any coding agent does. See [Integrations](block-development.md#integrations).
* **A team behind the product.** Support requests from the console go straight to the people who build the agent, and they follow up. See [The Team Behind the Agent](evaluate.md#adobe-team).

The agent doesn't replace your judgment. You decide the scope, the target design, and the content model, and you validate the result before it goes live.

## Choose Where to Start {#start-by-role}

Each guide gives the steps and checks for one goal, and builds on [Understand Your Project](#project-foundations). If your site already runs on Edge Delivery Services, you don't need a migration: [connect it](getting-started.md#existing-site), then restyle it or develop its blocks.

| Your goal | Start here |
|---|---|
| Decide whether and how your organization should use the agent, as the person who approves the architecture, security, and processes of the project | [Evaluate and Approve the Experience Modernization Agent](evaluate.md) |
| See the agent migrate your brand's own pages | [Start with Auto mode](getting-started.md#brand-trial) |
| Start a new site, or connect one that runs on Edge Delivery Services | [Start from a repository](getting-started.md#repo-start) |
| Store content on an Experience Manager author instance and edit it in the Universal Editor | [Getting started with Experience Manager authoring](getting-started-aem-authoring.md) |
| Demonstrate the agent on a few pages of a site that you are authorized to use | [Create a customer demo](getting-started.md#customer-demo) |
| Migrate a production site, as the migration lead | [Migrate a Production Site](production-migration.md) |
| Relaunch a site that runs on Experience Manager today | [Relaunch an Experience Manager site](production-migration.md#relaunch-aem-site) |
| Apply a new design, during a migration or to an existing site | [Restyle Sites](restyling.md) |
| Change how parts of a site look, as a designer or marketer whose work a developer reviews | [Make Visual Changes](visual-changes.md) |
| Create, update, or refactor blocks, or connect the site to another system | [Create, Update, and Refactor Blocks](block-development.md) |
| Record your project's conventions so that the agent and your team follow them | [Project Instructions and Memory](project-instructions.md) |
| Have Adobe engineers deliver the migration with the agent | [Delivery by Agentic Outcome Engineers](aoe-delivery.md) |

## Who Can Use the Agent {#who-can-use-ema}

You work with the agent in plain language: you describe what you want and check the result in the preview. For a first result on your own pages, that is all it takes. [Auto mode](getting-started.md#brand-trial) migrates them without step-by-step prompting, and [demo mode](getting-started.md#demo-mode) lets you try the console on a sample project.

Working on the site itself takes a little more. The agent's changes are code in a Git repository: you check them in the preview, push them to a branch, and open a pull request that a developer reviews. Some knowledge of HTML, and the willingness to learn these Git and GitHub basics, are enough to take part. The agent is a tool for tech-savvy people in any role, in marketing and design as much as in development.

That brings the people who judge a site's look best into its development. A designer or marketer who knows the brand can refine the layout, typography, and spacing of a block directly, instead of describing the change to a developer and waiting for it. They can decide which blocks authors get and how each one looks, and check the result at every screen size. Content specialists check that the content structure is easy for authors to edit; see [Shape the Content Structure](production-migration.md#content-structure). Developers build the blocks with complex behavior and the integrations, debug, and review every change before it reaches production. Technical leads scope the migration, choose the content destination, and decide when the site is ready to release.

The agent doesn't limit requests by role. Your permissions in Git and in the content destination decide what you can change outside your workspace.

### Broader Contribution, Same Production Control {#production-control}

The Experience Modernization Agent widens who can contribute to a site, not who approves what goes live. Developers stay in control of every line of code that reaches production.

That control sits in your Git provider, not in the console, so it holds however a change is made. Protect `main` with branch protection that requires a pull request approved by a developer, and don't let other contributors bypass it. Contributors then push their work with **Create new PR**, and a developer checks the result on the preview URLs that the pull request lists before merging it. If a contributor turns on **Allow LLM to use my git credentials**, the agent pushes with that contributor's access, so the same protection applies to it. Publishing content is controlled separately, by the site's publish role. For the setup, see [Control over Changes](evaluate.md#security-control).

## Understand Your Project {#project-foundations}

![The agent reads content and design from the source website, and optionally a Figma design, into your console workspace. Code is pushed from there to the Git repository and content is uploaded to the content destination. Edge Delivery Services serves both on the preview and live sites.](assets/project-architecture.png)

* **Source:** The authorized website, content, or design that you provide. The agent reads it and never changes it.
* **Console workspace:** Your own working copy of the project's code and content, where the agent makes its changes before you push or upload them. See [Work Safely in an Independent Workspace](#independent-workspace).
* **Code:** The site's Git repository and working branch that contain styles, scripts, and blocks.
* **Content destination:** Where the migrated content is stored and which editor authors use: document-based storage with Experience Workspace, or Experience Manager authoring with the Universal Editor. The source CMS doesn't decide it. See [Where Content Is Stored and How Authors Edit It](#content-storage).
* **Preview and publication:** The preview site, where you check saved content with your code, and the live site, where approved changes are released. See [How Changes Go Live](#code-content-lifecycle).

Code and content are stored and released separately, so pushing code never saves content, and uploading content never changes code. Pages are made of sections, default content, and blocks, and the content carries no styling, so the agent can give it a new design by changing only the code. For how the platform works, see the [Edge Delivery Services overview](/help/edge/overview.md) and [Markup, Sections, Blocks, and Auto Blocking](https://www.aem.live/developer/markup-sections-blocks). For how the agent structures imported content, and how you steer it, see [Shape the Content Structure](production-migration.md#content-structure).

New sites start from the [AEM boilerplate](https://github.com/adobe/aem-boilerplate). For a commerce storefront, start from the [commerce boilerplate](https://experienceleague.adobe.com/en/tools/commerce-storefront/boilerplate/) instead, because its commerce blocks are hard to add to a project later; see [Start from a Repository](getting-started.md#prepare-repo).

Edge Delivery Services runs complex enterprise websites. Its pages are standard HTML, CSS, and JavaScript, so a block can call any API from the browser, such as search, commerce, or personalization, as on any other website. Spreadsheets publish as JSON and a query index lists the site's pages, so blocks can also build listings and filters from your own content. Business logic stays in the services that own it. Each integration is project work that you specify and test, and the agent can write its block code once you have decided how it should work. See [Build a Dynamic Block](block-development.md#dynamic-blocks). The agent's skills focus on Edge Delivery Services, but it isn't limited to them: point it to another system's documentation, and work out the integration with it. See [Work Beyond Edge Delivery Services](prompting-guide.md#beyond-eds).

### Work Safely in an Independent Workspace {#independent-workspace}

The agent doesn't change your Git repository or your content destination directly. It works in a console workspace: your own working copy of the project, hosted by Adobe and not shared with other users. The workspace holds a checkout of one branch of your Git repository, and copies of the content pages that you imported, opened, or pulled.

Everything that the agent does happens there first. You can ask for a sweeping redesign, check it in the console preview, and discard what you don't want, while your repository, the authors' pages, and the live site stay unchanged. Work leaves the workspace only when you send it, in two separate operations:

* **Push code** sends the changed files that you select to your Git repository, as a commit on the current branch or as a new pull request.
* **Upload content** sends the pages that you select to Experience Workspace or the author instance, where they replace the saved versions of those pages.

[Agent permissions](console.md#settings-page) let the agent do the same for you. See [Control over Changes](evaluate.md#security-control).

The independence works in both directions: changes that others push or upload don't reach your workspace until you pull them. See [Sync Menu](console.md#sync-menu) and [Work as a Team](production-migration.md#collaboration).

### How Changes Go Live {#code-content-lifecycle}

![Code, in blue, moves down from the Experience Modernization Console: pushing puts it on your branch, where you check changes before they go live, and merging after review puts it on main, the production code. Content, in purple, moves across: uploading saves the page in the authoring environment, which is Experience Workspace or the Universal Editor; previewing puts it on the preview site, and publishing puts it on the live site. Edge Delivery Services serves both sites. Each branch's code is a row across the whole diagram, and the authoring environment, the preview site, and the live site are columns down all rows. Where a branch's row crosses the preview or live column, a URL shows that code with the previewed or published content. The live URL of main is the production site.](assets/code-content-lifecycle.png)

Code and content reach the live site in different ways:

* **Code:** Edge Delivery Services fetches your code from GitHub through the [AEM Code Sync](https://github.com/apps/aem-code-sync) app, or from another Git host through Cloud Manager ([Bring Your Own Git](https://www.aem.live/developer/byo-git)). Each branch gets its own URLs, and a change pushed to a branch shows on that branch's preview and live URLs at the same time. Code has no separate publish step: merging into `main` updates the code of the production site immediately, so check a branch on its own URLs before you merge it.
* **Content:** Authors first preview a page, which copies the saved content to the preview site on `*.aem.page`. They then publish it, which makes it live on `*.aem.live`. Authors do both from the authoring UI or from the [AEM Sidekick](https://www.aem.live/docs/sidekick) browser extension.

Preview URLs follow the pattern `https://{branch}--{repo}--{owner}.aem.page` and show previewed content. Live URLs follow the same pattern on `aem.live` and show published content. `{owner}` is the GitHub organization or user that owns the repository, and `{repo}` is the repository name. Content isn't branched: every branch shows the same pages, each with its own code. The live URL of `main` is the production site, which your own domain serves after the cutover.

### Names You May See {#names}

Adobe has renamed several of these products, and they are often abbreviated. These docs write the names in full. The table maps them to the older names and abbreviations that you meet on aem.live, in the console, in URLs, and in older articles.

| Name | What it refers to |
|---|---|
| Adobe Experience Manager (AEM) | Adobe's content management system. |
| Brand Experience Agent | The family of Experience Manager agents that the Experience Modernization Agent belongs to. |
| Experience Modernization Agent (EMA) | The agent described in these docs. |
| Experience Modernization Console | The web interface where you use the agent, at [`aemcoder.adobe.io`](https://aemcoder.adobe.io). |
| Console workspace | The working copy described in [Work Safely in an Independent Workspace](#independent-workspace). Console labels such as **Checkout to workspace** and **Your workspace is paused** refer to it. It is unrelated to Experience Workspace. |
| Edge Delivery Services (EDS) | Experience Manager's website delivery service. The architecture was originally developed as Project Helix, later code-named Franklin, and older articles use those names. The `hlx` in hostnames such as `admin.hlx.page`, the admin API, comes from Helix. |
| `*.aem.page`, `*.aem.live` | A site's preview and live URLs. Older projects and documentation may show the earlier domains, `hlx.page` and `hlx.live`. |
| AEM Sidekick | The browser extension that authors use to preview and publish pages. |
| Experience Workspace | The visual authoring UI for document-based content, at `da.live`. It replaces Document Authoring (DA), and some console labels and screens still use that name. See [Document-Based Storage](#document-based). |
| Experience Manager authoring | Edge Delivery Services with content stored in the Java Content Repository (JCR) of an Experience Manager as a Cloud Service author instance and edited in the Universal Editor. Also called AEM authoring, and previously Crosswalk. |
| IMS | Adobe's identity service, which handles sign-in with your Adobe ID. |

## Where Content Is Stored and How Authors Edit It {#content-storage}

The agent asks where the migrated content should be stored. Which repository holds the content and which editor authors use are related but separate questions. With either option, authors get a visual editor and Edge Delivery Services delivers the pages.

| | Document-based storage | Experience Manager authoring |
|---|---|---|
| Where content is stored | The document-based content repository | The JCR of your author instance |
| Visual editor | Experience Workspace | Universal Editor |
| Page delivery | Edge Delivery Services | Edge Delivery Services |

### Document-Based Storage with Experience Workspace {#document-based}

Content is stored as documents in the document-based content repository. "Document-based" describes storage only, not the authoring experience. Authors edit pages visually in [Experience Workspace](https://www.aem.live/docs/ew/about), the visual authoring UI for Edge Delivery Services, which also offers an AI assistant, collaboration, and Experience Manager Assets integration. Experience Workspace is off by default and is turned on per site or organization in the project's configuration. When you transfer an Auto mode site to a document-based destination with [**Make it yours**](getting-started.md#make-it-yours), the transfer turns it on for that site.

### Experience Manager Authoring with the Universal Editor {#jcr-persistence}

Content is stored in the Java Content Repository (JCR) of an Experience Manager as a Cloud Service author instance, a setup previously called Crosswalk. Authors edit pages with the [Universal Editor](/help/implementing/universal-editor/introduction.md), Adobe's visual editor for content on the author instance, and Edge Delivery Services still delivers the pages. HTL and Java don't render them, as they do on Experience Manager sites built with components. Template repositories for this setup, such as `aem-block-collection-xwalk`, still carry `xwalk` in their names.

These docs use *Experience Manager authoring* for this storage option, and *author instance* for the Experience Manager as a Cloud Service environment where that content is stored and edited.

### Adobe's Recommendation {#recommendation}

For any new implementation, Adobe strongly recommends document-based storage with Experience Workspace over Experience Manager authoring with the Universal Editor. This includes large websites with thousands of pages.

Document-based authoring used to mean writing pages in Microsoft Word or Google Docs, stored on SharePoint or Google Drive, which remain supported content sources, or in Document Authoring, a document-style editor. None of them offered visual page editing, so teams that needed it often chose Experience Manager authoring. Experience Workspace replaces Document Authoring and gives document-based content a visual editor. A site that uses Document Authoring can turn Experience Workspace on, and its existing content works there without a migration. That leaves little reason for a brand to avoid document-based storage. When you read an article about document-based authoring, check when it was written.

Experience Manager authoring remains fully supported. Choose it when a specific requirement depends on content staying in the JCR. For headless content, delivered through APIs rather than as web pages, the Universal Editor remains the recommended editor.

## What the Agent Can Do {#creation-migration}

You don't need to name a capability: describe the task, and the agent chooses the workflow, which it calls a skill.

| Capability | What the agent does | Learn more |
|---|---|---|
| Site catalog and planning | Discovers the source site's pages and groups them into templates and block variants, with screenshots and a report that you refine in the **Planning** view. | [Plan a Migration with the Site Catalog](site-catalog.md) |
| Page and design migration | Imports source pages into default content and blocks, extracts the design into design tokens and global styles, and rebuilds the header, navigation, and footer that every page shares. | [Migrate a Production Site](production-migration.md) |
| Bulk import | Writes an import script for each template, runs it on the template's other pages, and fixes the script for pages that differ from their source. | [How the Agent Migrates at Scale](production-migration.md#migration-at-scale) |
| Visual critique | Compares a block, a page, or the whole site with the source and fixes differences in content, structure, and styling. | [Critique the Site](prompting-guide.md#site-critique) |
| Protected source pages | Reads source pages that need a custom request header, HTTP Basic authentication, or bearer authentication. | [Protected Site Authentication](console.md#protected-site-authentication) |
| Restyling and Figma designs | Applies a new design during a migration or to an existing site, from Figma components or other references, and creates new pages from a Figma frame. | [Restyle Sites](restyling.md), [Work from a Figma Design](visual-changes.md#figma) |
| Block development and integrations | Creates, updates, and refactors blocks from real content, reuses existing blocks where they fit, and writes the code that connects the site to other systems. | [Create, Update, and Refactor Blocks](block-development.md) |
| Experience Manager authoring models | Creates the block models that the Universal Editor uses, for projects that store content on an author instance. | [Getting started with Experience Manager authoring](getting-started-aem-authoring.md) |
| Project documentation | Writes documentation for authors, developers, and administrators from the project's code and configuration. | [Project Documentation](project-documentation.md) |
| Console tour | Explains the console's views and actions when you ask "Give me a tour of the console." | [Experience Modernization Console](console.md) |

Optional add-ons extend these capabilities when a project needs them: Figma import, guided redesign (the Stardust add-on), project documentation, forms migration, commerce pages, block library setup, Edge Delivery Services troubleshooting, modern web guidance, and design craft. The agent offers to turn an add-on on when your request needs it, and you can save the choice in the repository so that it applies to the whole team. See [Optional Capabilities](console.md#optional-capabilities).

## Security and Data Handling {#security}

The agent works without receiving the credentials that you configure, each user works in a separate environment, and you decide when changes reach your Git repository and your content destination. For access and isolation, credentials, what the AI model processes, the control over each step, and where work is stored, see [Security and Data Handling](evaluate.md#security).

>[!CAUTION]
>
>That protection covers only credentials entered in the console's **Settings**. Never type, paste, or attach passwords, API keys, access tokens, or other secrets in the chat. Everything in the chat reaches the AI model, and the agent can copy it into your project's files. Make sure that everyone on the team knows this before they start prompting. See [Keep Secrets Out of the Chat](prompting-guide.md#secrets).

## Limitations {#limitations}

Use only websites and designs that you are authorized to migrate. The selected workflow must be able to reach and read the source. If the site uses bot protection, arrange access with its administrator. See [source sites with bot protection](troubleshooting.md#bot-protection).

* The agent reads each source over the internet from its hosted environment. Pages that require sign-in or a secret header can be migrated when the source accepts one of the methods in [Protected Site Authentication](console.md#protected-site-authentication). That section also says what to ask the site's administrator for when a source can't be reached this way.
* The agent loads each source page in a browser and reads it once it has rendered. That includes content that scripts insert and content that the page contains but CSS hides, such as a closed accordion panel. Content that appears only after a visitor clicks or types isn't in the page at that moment, so it isn't captured. Check such pages in the screenshots, and add the missing content after import or ask for a way to capture it.
* The agent targets Edge Delivery Services, including sites that use [Experience Manager authoring](#jcr-persistence). It does not convert a project to HTL-based publishing or an API-only/SPA delivery stack.
* Page import copies what the source page shows: its content and its design. It can't see how the source's servers produced that page. Content inheritance, reuse through content fragments, personalization rules, search, form processing, and other business logic run there, so import copies their output on that page, not the logic. The agent also rebuilds the markup rather than copying it, so the source's scripts, such as analytics and experimentation tags, don't come along. Auto mode's **Include integrations** option carries over supported analytics, tag manager, and consent settings. Decide how each of the others works on the new site; the agent can then build the blocks and code for it. See [What Remains Project Work](evaluate.md#project-work), and for forms, [Form Submissions](block-development.md#form-submissions).
* The agent's visual critique compares how the result looks with the source. Looking the same doesn't show that authors can edit the page, that interactions work, or that it is accessible and fast on real devices, so check those before you [sign off](production-migration.md#acceptance).

## Next Steps {#next-steps}

To begin, pick a guide in [Choose Where to Start](#start-by-role). For short answers to common questions, such as access, Auto mode, transfers, protected source sites, and recovery, see the [Experience Modernization Agent FAQ](faq.md). When something doesn't work as you expect, see [Troubleshooting](troubleshooting.md) or [Request Support](console.md#request-support).

To learn what changed in recent versions of the console, see the [Experience Modernization Agent release notes](/help/release-notes/modernization-agent/current.md).
