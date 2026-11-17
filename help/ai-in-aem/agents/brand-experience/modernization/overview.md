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

The Experience Modernization Agent is Adobe's AI development agent for [Edge Delivery Services](/help/edge/overview.md) and is part of the [Brand Experience Agent](/help/ai-in-aem/agents/brand-experience/overview.md). It gives you a ready-to-use development environment in your browser, with nothing to install.

You can begin by migrating a site's content and design, then keep working with the agent to integrate third-party systems, redesign the site, refactor its blocks, or extend how it works. Developers can build integrations and complex behavior, while designers and marketers refine the site's appearance by prompting rather than writing CSS or JavaScript. The [knowledge you need](#who-can-use-ema) depends on the work.

<!-- markdownlint-disable-next-line MD033 -->
<a id="start-by-role"></a>

To see a first result on your own pages, [try Auto mode](getting-started.md#brand-trial). It's the best way to evaluate Adobe Experience Manager with your own website's content and design. Give it your site's URL; it migrates a set of pages and emails you when it finishes.

## Move Your Site to Edge Delivery Services {#benefits}

Use the agent to move web properties onto Edge Delivery Services from other CMSes, from Experience Manager sites built with Java components, or from static sites.

![Three panels show your source site's design, content, dynamic features, and tags, the Experience Modernization Agent's migration and comparison steps, and the resulting site on Edge Delivery Services. A separate sixth step shows further expansion, redesign, optimization, and integration on request.](assets/what-the-agent-does.png)

The diagram above traces the migration from your source site to a site your team can keep evolving on Edge Delivery Services. The left panel shows the source site's design, content, and dynamic features as visitors see them, plus its tags and analytics. By default, the agent uses the rendered pages from your current site as the source for the migration, unless you instruct the agent to perform a redesign, possibly providing design files such as [Figma designs](visual-changes.md#figma).

The right panel shows the intended result: the complete site carried over, with its dynamic features rebuilt and its analytics, tag manager, and consent settings back in place. The migration's objective is to help your team to make full use of what Edge Delivery Services offers:

* **Rapid development:** A standard and lean web development setup that is familiar to developers and their agents, making them most efficient.
* **Agentic visual authoring:** Authors assemble pages from branded blocks in [Experience Workspace](https://www.aem.live/docs/ew/about) or the [Universal Editor](/help/implementing/universal-editor/introduction.md), and can also prompt content changes.
* **Fast, crawlable pages:** The platform serves fast, semantic HTML to help improve search and AI visibility. See [Keeping It 100](https://www.aem.live/developer/keeping-it-100).
* **Room to grow:** The platform runs some of the largest multi-market, multi-language sites, with complex integrations.

To reach that objective, the agent automates much of following steps:

1. **Read each page.** Page import works from what the browser renders. If a source requires sign-in, configure [Protected Site Authentication](console.md#protected-site-authentication). For bot protection, arrange authorized access with the site's administrator: they can allowlist the agent's backend addresses, or you can use an accessible staging or origin host with the same content. If only page discovery is blocked, provide the URLs directly. See [Source Sites with Bot Protection](troubleshooting.md#bot-protection).
1. **Analyze the structure.** The [site catalog](site-catalog.md) inventories pages and groups them into templates, sections, and blocks, with screenshots. Review the groupings, set the scope, choose the target design and content model, and decide what to migrate first.
1. **Import the content.** For each template, the agent analyzes a sample page and maps it to [default content and reusable blocks](production-migration.md#content-structure). It imports the sample as an editable page and generates import scripts that apply the mapping to other pages in that template.
1. **Rebuild the design.** The agent extracts CSS design tokens for colors, fonts, and spacing, then writes the global styles and block CSS that use them. It rebuilds the markup rather than cloning source code and its technical debt.
1. **Compare, refine, and validate.** The agent compares the rebuilt page with its source and iterates on your prompts. Refine the mapping and design, then validate each sample before scaling with the generated scripts. Corrections to a reusable block or import script apply across pages in that template. The [production migration guide](production-migration.md) covers batches, checks, release, and handover.
1. **Expand, redesign, optimize, and integrate.** After migration, prompt the agent to rebuild dynamic features or add integrations. Auto mode can carry over supported analytics, tag manager, and consent settings; see [What Page Import Can Read and Carry Over](#limitations). For a few pages to show stakeholders, follow [Create a Customer Demo](getting-started.md#customer-demo). If you want Adobe engineers to operate the agent with your team, see [Delivery by Agentic Outcome Engineers](aoe-delivery.md).

### What Page Import Can Read and Carry Over {#limitations}

Use only websites and designs that you are authorized to migrate. The selected workflow must be able to reach and read the source. If the site uses bot protection, arrange access with its administrator. See [source sites with bot protection](troubleshooting.md#bot-protection).

* The agent reads each source over the internet from its hosted environment. Pages that require sign-in or a secret header can be migrated when the source accepts one of the methods in [Protected Site Authentication](console.md#protected-site-authentication). That section also says what to ask the site's administrator for when a source can't be reached this way.
* The agent loads each source page in a browser and reads it once it has rendered. That includes content that scripts insert and content that the page contains but CSS hides, such as a closed accordion panel. Content that appears only after a visitor clicks or types isn't in the page at that moment, so it isn't captured. Check such pages in the screenshots, and add the missing content after import or ask for a way to capture it.
* The agent targets Edge Delivery Services, including sites that use [Experience Manager authoring](#jcr-persistence). It does not convert a project to HTL-based publishing or an API-only/SPA delivery stack.
* Page import copies what the source page shows: its content and its design. It can't see how the source's servers produced that page. Content inheritance, reuse through content fragments, personalization rules, search, form processing, and other business logic run there, so import copies their output on that page, not the logic. The agent also rebuilds the markup rather than copying it, so the source's scripts, such as analytics and experimentation tags, don't come along. Auto mode's **Include integrations** option carries over supported analytics, tag manager, and consent settings. Decide how each of the others works on the new site; the agent can then build the blocks and code for it. See [What Remains Project Work](evaluate.md#project-work), and for forms, [Form Submissions](block-development.md#form-submissions).
* The agent's visual critique compares how the result looks with the source. Looking the same doesn't show that authors can edit the page, that interactions work, or that it is accessible and fast on real devices, so check those before you [sign off](production-migration.md#acceptance).

## How Your Site Is Built and Updated {#project-foundations}

The result is a standard project that you own: HTML, CSS, and JavaScript in your Git repository, following the conventions of the AEM boilerplate and the [Block Collection](https://www.aem.live/developer/block-collection), with content stored separately for authors to edit. Developers can continue in the console, in their own editor, or with other AI tools.

![The source website and optional Figma design feed the agent in Experience Modernization, which also contains the Workspace. Purple content rows cross blue code columns. Upload, preview, and publish lead upward to the live site; push and merge lead rightward to the main branch. Adobe Experience Manager encloses authoring and delivery, while a separate Git frame encloses code management. The main branch's live URL is the production site.](assets/code-content-lifecycle-architecture.png)

The source website supplies the content and design. You can add a Figma design as a new target for the whole site or part of it. The agent reads these sources without changing them, and builds the result in its console workspace.

Git stores the site's styles, scripts, and blocks. Your branch holds code to review; `main` holds production code. The authoring environment stores the content. Edge Delivery Services combines that content with code from the branch shown by each preview or live URL.

Pages are made of sections, default content, and blocks, and the content carries no styling, so the agent can give it a new design by changing only the code. For how the platform works, see the [Edge Delivery Services overview](/help/edge/overview.md) and [Markup, Sections, Blocks, and Auto Blocking](https://www.aem.live/developer/markup-sections-blocks). For how the agent structures imported content, and how you steer it, see [Shape the Content Structure](production-migration.md#content-structure).

New sites start from the [AEM boilerplate](https://github.com/adobe/aem-boilerplate). For a commerce storefront, start from the [commerce boilerplate](https://experienceleague.adobe.com/en/tools/commerce-storefront/boilerplate/) instead, because its commerce blocks are hard to add to a project later; see [Start from a Repository](getting-started.md#prepare-repo).

### Work Safely in an Independent Workspace {#independent-workspace}

The agent doesn't change your Git repository or your content destination directly. It works in a console workspace: your own working copy of the project, hosted by Adobe and not shared with other users. The workspace holds a checkout of one branch of your Git repository, and copies of the content pages that you imported, opened, or pulled.

Everything that the agent does happens there first. You can ask for a sweeping redesign, check it in the console preview, and discard what you don't want, while your repository, the authors' pages, and the live site stay unchanged. Work leaves the workspace only when you send it, in two separate operations:

* **Push code** sends the changed files that you select to your Git repository, as a commit on the current branch or as a new pull request.
* **Upload content** sends the pages that you select to Experience Workspace or the author instance, where they replace the saved versions of those pages.

[Agent permissions](console.md#settings-page) let the agent do the same for you. See [Control over Changes](evaluate.md#security-control).

The independence works in both directions: changes that others push or upload don't reach your workspace until you pull them. See [Sync Menu](console.md#sync-menu) and [Work as a Team](production-migration.md#collaboration).

### Where Content Is Stored and How Authors Edit It {#content-storage}

The agent asks where the migrated content should be stored. Which repository holds the content and which editor authors use are related but separate questions. The source CMS doesn't decide the destination. With either option, authors get a visual editor and Edge Delivery Services delivers the pages.

| | Document-based storage | Experience Manager authoring |
|---|---|---|
| Where content is stored | The document-based content repository | The JCR of your author instance |
| Visual editor | Experience Workspace | Universal Editor |
| Page delivery | Edge Delivery Services | Edge Delivery Services |

#### Document-Based Storage with Experience Workspace {#document-based}

Content is stored as documents in the document-based content repository. "Document-based" describes storage only, not the authoring experience. Authors edit pages visually in [Experience Workspace](https://www.aem.live/docs/ew/about), the visual authoring UI for Edge Delivery Services, which also offers an AI assistant, collaboration, and Experience Manager Assets integration. Experience Workspace is off by default and is turned on per site or organization in the project's configuration. When you transfer an Auto mode site to a document-based destination with [**Make it yours**](getting-started.md#make-it-yours), the transfer turns it on for that site.

#### Experience Manager Authoring with the Universal Editor {#jcr-persistence}

Content is stored in the Java Content Repository (JCR) of an Experience Manager as a Cloud Service author instance, a setup previously called Crosswalk. Authors edit pages with the [Universal Editor](/help/implementing/universal-editor/introduction.md), Adobe's visual editor for content on the author instance, and Edge Delivery Services still delivers the pages. HTL and Java don't render them, as they do on Experience Manager sites built with components. Template repositories for this setup, such as `aem-block-collection-xwalk`, still carry `xwalk` in their names.

These docs use *Experience Manager authoring* for this storage option, and *author instance* for the Experience Manager as a Cloud Service environment where that content is stored and edited.

#### Adobe's Recommendation {#recommendation}

For any new implementation, Adobe strongly recommends document-based storage with Experience Workspace over Experience Manager authoring with the Universal Editor. This includes large websites with thousands of pages.

Document-based authoring used to mean writing pages in Microsoft Word or Google Docs, stored on SharePoint or Google Drive, which remain supported content sources, or in Document Authoring, a document-style editor. None of them offered visual page editing, so teams that needed it often chose Experience Manager authoring. Experience Workspace replaces Document Authoring and gives document-based content a visual editor. A site that uses Document Authoring can turn Experience Workspace on, and its existing content works there without a migration. That leaves little reason for a brand to avoid document-based storage. When you read an article about document-based authoring, check when it was written.

Experience Manager authoring remains fully supported. Choose it when a specific requirement depends on content staying in the JCR. For headless content, delivered through APIs rather than as web pages, the Universal Editor remains the recommended editor.

### How Changes Go Live {#code-content-lifecycle}

In the diagram, blue columns show code branches and purple rows show content states. Pushing code never saves content, and uploading content never changes code.

* **Code:** Edge Delivery Services fetches your code from GitHub through the [AEM Code Sync](https://github.com/apps/aem-code-sync) app, or from another Git host through Cloud Manager ([Bring Your Own Git](https://www.aem.live/developer/byo-git)). Each branch gets its own URLs, and a change pushed to a branch shows on that branch's preview and live URLs at the same time. Code has no separate publish step: after review, merging into `main` updates the code of the production site immediately, so check a branch on its own URLs before you merge it.
* **Content:** Authors first preview a page, which copies the saved content to the preview site on `*.aem.page`. They then publish it, which makes it live on `*.aem.live`. Authors do both from the authoring UI or from the [AEM Sidekick](https://www.aem.live/docs/sidekick) browser extension.

Preview URLs follow the pattern `https://{branch}--{repo}--{owner}.aem.page` and show previewed content. Live URLs follow the same pattern on `aem.live` and show published content. `{owner}` is the GitHub organization or user that owns the repository, and `{repo}` is the repository name. Content isn't branched: every branch shows the same pages, each with its own code. The live URL of `main` is the production site, which your own domain serves after the cutover.

## Keep Developing the Site {#creation-migration}

The migration isn't the end of the agent's work. Your team can apply a new brand design from Figma, build new pages from existing blocks, or track down a bug. It can also audit performance, accessibility, and SEO, then fix what the audit finds. See [Restyle Sites](restyling.md), [Guided Redesign](restyling.md#guided-redesign), and [Create, Update, and Refactor Blocks](block-development.md). If your site already runs on Edge Delivery Services, [connect it](getting-started.md#existing-site) and start here without a migration.

Blocks can call APIs for search, commerce, personalization, maps, video, or your own services, as on any other website. Spreadsheets publish as JSON and a query index lists the site's pages, so blocks can also build listings and filters from your own content. Business logic stays in the services that own it. Specify and test each integration, and the agent can write its block code once you have decided how it should work. See [Build a Dynamic Block](block-development.md#dynamic-blocks) and [Connect Services and Applications](block-development.md#integrations).

The agent's built-in workflows focus on Edge Delivery Services, but its work isn't limited to them. Point it to another system's documentation and work out the integration with it, as described in [Work Beyond Edge Delivery Services](prompting-guide.md#beyond-eds). The [capability reference](capabilities.md) groups the built-in workflows and optional add-ons in one place; you describe the task, and the agent chooses the workflow.

The conventions that you keep in `AGENTS.md` and related files stay with the repository, so later conversations start with what your team has agreed. See [Project Instructions and Memory](project-instructions.md). To prepare documentation for authors, developers, and administrators, use [Generate Project Documentation](project-documentation.md).

### Who Can Use the Agent {#who-can-use-ema}

You work with the agent in plain language: describe what you want and check the result in the preview. Auto mode needs no step-by-step prompting. To explore the console on a sample project instead, use [demo mode](getting-started.md#demo-mode).

Working on the site itself takes a little more. The agent's changes are code in a Git repository: you check them in the preview, push them to a branch, and open a pull request that a developer reviews. Some knowledge of HTML, and the willingness to learn these Git and GitHub basics, are enough to take part. The agent is a tool for tech-savvy people in any role, in marketing and design as much as in development.

A designer or marketer who knows the brand can refine the layout, typography, and spacing of a block directly, instead of describing the change to a developer and waiting for it. They can decide which blocks authors get and how each one looks, and check the result at every screen size; see [Make Visual Changes](visual-changes.md). Content specialists check that the content structure is easy for authors to edit; see [Shape the Content Structure](production-migration.md#content-structure). Developers build complex behavior and integrations, debug, and review changes before production. Technical leads scope the migration, choose the content destination, and decide when the site is ready to release.

The agent doesn't limit requests by role. Your permissions in Git and in the content destination decide what you can change outside your workspace.

#### Broader Contribution, Same Production Control {#production-control}

The Experience Modernization Agent widens who can contribute to a site, not who approves what goes live. Developers stay in control of every line of code that reaches production.

That control sits in your Git provider, not in the console, so it holds however a change is made. Protect `main` with branch protection that requires a pull request approved by a developer, and don't let other contributors bypass it. Contributors then push their work with **Create new PR**, and a developer checks the result on the preview URLs that the pull request lists before merging it. If a contributor turns on **Allow LLM to use my git credentials**, the agent pushes with that contributor's access, so the same protection applies to it. Publishing content is controlled separately, by the site's publish role. For the setup, see [Control over Changes](evaluate.md#security-control).

## Security and Data Handling {#security}

The agent works without receiving the credentials that you configure, each user works in a separate environment, and you decide when changes reach your Git repository and your content destination. For access and isolation, credentials, what the AI model processes, the control over each step, and where work is stored, see [Security and Data Handling](evaluate.md#security).

For your organization's architecture, security, and process review, use [Evaluate and Approve the Experience Modernization Agent](evaluate.md). That guide also introduces [the team behind the agent](evaluate.md#adobe-team). Support requests from the console reach the people who build it, who follow up with you.

>[!CAUTION]
>
>That protection covers only credentials entered in the console's **Settings**. Never type, paste, or attach passwords, API keys, access tokens, or other secrets in the chat. Everything in the chat reaches the AI model, and the agent can copy it into your project's files. Make sure that everyone on the team knows this before they start prompting. See [Keep Secrets Out of the Chat](prompting-guide.md#secrets).

## Next Steps {#next-steps}

For short answers to common questions, such as access, Auto mode, transfers, protected source sites, and recovery, see the [Experience Modernization Agent FAQ](faq.md). When something doesn't work as you expect, see [Troubleshooting](troubleshooting.md) or [Request Support](console.md#request-support).

To learn what changed in recent versions of the console, see the [Experience Modernization Agent release notes](/help/release-notes/modernization-agent/current.md).
