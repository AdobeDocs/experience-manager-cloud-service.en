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

The Experience Modernization Agent is Adobe's AI development agent for [Edge Delivery Services](/help/edge/overview.md). It gives you a ready-to-use development environment for these sites in the browser, with nothing to install, and an agent that migrates, builds, and evolves them. Your Git repository remains the system of record for the site's code.

Edge Delivery Services is the part of Adobe Experience Manager Sites that delivers websites. It serves authored content as plain semantic HTML, and the project's own CSS and JavaScript style and decorate it in the browser. If you already build with HTML, CSS, and JavaScript, most of the project will look familiar. The parts specific to Experience Manager are explained in [Understand Your Project](#project-foundations). Adobe has renamed several of these products over time. If you meet older names such as Helix, Franklin, or Crosswalk, or short forms of these names, see [Names You May See](#names).

## Introduction {#introduction}

The Experience Modernization Agent is part of the [Brand Experience Agent.](/help/ai-in-aem/agents/brand-experience/overview.md) It automates the repetitive parts of building a site: importing content, mapping it to blocks, extracting the design, and writing block code. You work in the hosted Experience Modernization Console, using natural-language requests and previews. You don't need Docker or a local command-line environment. You don't need to be a developer either: designers, content specialists, and marketers can work on the site too. See [Who Can Use the Agent](#who-can-use-ema). With Auto mode, in early access, the agent can also migrate a first set of pages on its own and email you when it's done.

Use the agent to move web properties onto Edge Delivery Services, the current Experience Manager website stack, from other CMSes, from older implementations built from Java and HTL components, or from static sites. The agent reads each source page as a browser renders it, so the system behind the source doesn't matter: it works from the content and design that visitors see. Consolidating on the platform gives you:

* **Fast pages from lean code:** Edge Delivery Services serves the content as finished semantic HTML from a CDN, and your own CSS and JavaScript style it, with no framework to download first. A page loads in three phases: what the first section needs, then the rest of the project's code, and third-party tags last. That is why a new project from the AEM boilerplate scores 100 in Lighthouse. See [Keeping It 100](https://www.aem.live/developer/keeping-it-100).
* **Room to grow:** The platform runs large multi-market and multi-language sites. Its largest sites have more than 100,000 pages.
* **Visual authoring:** Authors edit pages visually in Experience Workspace, or in the Universal Editor when content is stored in Experience Manager. See [Where Content Is Stored and How Authors Edit It](#content-storage).
* **Pages that AI systems can read:** AI crawlers and answer engines often read the raw HTML without running JavaScript. Because the platform serves the content in the HTML itself, the migrated content is readable to them, so migration and AI readiness happen in the same step.

The agent rebuilds your pages on a block system that follows the architecture of Edge Delivery Services. It decomposes each page into sections and content, maps the content to default content and reusable blocks, and extracts the design system into global styles and block CSS. It then imports further pages in bulk with the same mappings, using generated import scripts rather than having the AI model interpret every page. See [How the Agent Migrates at Scale](#migration-at-scale). It does not clone the source markup, which would carry over the old site's technical debt. Expect a close first pass that you refine by prompting and validate before you scale.

After go-live, the same environment keeps working on the site. You can restyle it to a new brand, including from Figma designs, add blocks, update or refactor existing blocks, create pages from the established blocks, debug problems, and generate project and handover documentation. You can also connect an existing Edge Delivery Services project and start there, without a migration.

You stay in control of every change. The agent works in your own console workspace, where you review and preview its changes and discard what you don't want. Nothing reaches your project until you push code to your Git repository or upload content to the authoring destination that you chose, or turn on [agent permissions](console.md#settings-page) that let the agent do so. Your permissions, repository policies, and publication workflow determine what you can change and release. See [Work Safely in an Independent Workspace](#independent-workspace).

## Start Here by Role {#start-by-role}

People in different roles need different parts of these docs. Start with the guide for your role, and follow its links when you need more detail.

| Your role | Start here | Then read |
|---|---|---|
| **Decision-maker:** You approve the architecture, security, and processes of the project, and may not use the agent yourself. | [Evaluate and Approve the Experience Modernization Agent](evaluate.md) | [Broader Contribution, Same Production Control](#production-control), [Where Content Is Stored](#content-storage), [How the Agent Migrates at Scale](#migration-at-scale), [Figma and Design Systems](evaluate.md#figma), [Limitations](#limitations) |
| **Migration lead:** You set up the project and run the migration, and you may be new to Edge Delivery Services. | [Understand Your Project](#project-foundations), then [Getting Started](getting-started.md) | [Migrate a Production Site](production-migration.md) and its [phases](production-migration.md#phases), [Site Catalog](site-catalog.md), [Create, Update, and Refactor Blocks](block-development.md), [Project Instructions and Memory](project-instructions.md) |
| **Visual contributor:** You change how the site looks, and a developer reviews your work. | [Make Visual Changes](visual-changes.md) | [Inspect mode](getting-started.md#inspect-mode), [Restyle Sites](restyling.md), [Figma prompts](prompting-guide.md#figma-block-migration) |

## Why Use the Agent {#benefits}

Before anyone can judge a migration to Edge Delivery Services, a developer usually has to do a lot of repetitive work. They list the source pages and work out which ones share a layout. They decide how each part of a page maps to blocks and default content, then write the blocks and their styles and extract the colors and fonts. Finally, they write import scripts, import the pages, and compare them with the originals. The agent does this work with you, in one environment:

* **A first result on your own pages.** Give the agent a source page and it rebuilds it on Edge Delivery Services, with blocks, styles, and editable content, that you can check in the console's preview. You judge the approach on your own content rather than on a sample site, without setting up a local environment first.
* **A plan that you can see.** The [site catalog](site-catalog.md) inventories the source site and groups its pages into templates and blocks, with screenshots. Use it to scope and size the project and to decide what to migrate first.
* **Fixes that scale.** The agent turns each correction into a change to a reusable block or import script, so a fix on one page applies to every page of that template. See [How the Agent Migrates at Scale](#migration-at-scale).
* **A standard project that you own.** The result is plain Edge Delivery Services code in your Git repository that follows the conventions of the AEM boilerplate and the [Block Collection](https://www.aem.live/developer/block-collection). Developers can continue in the console, in their own editor, or with other AI tools. Nothing ties the site to the Experience Modernization Agent.
* **Help after go-live.** The same agent restyles the site for a new brand, adds and refactors blocks, creates pages from existing blocks, debugs problems, and documents the project. You can also start on an existing Edge Delivery Services site without a migration.
* **Project knowledge that lasts.** The agent follows the conventions that you keep in `AGENTS.md` and related files in the repository, so every conversation starts with what your team has agreed. See [What the Agent Remembers](#memory).
* **Unattended runs.** Auto mode, in early access, migrates a set of pages, including their design, without step-by-step prompting and emails you when it finishes. See [Start with Auto Mode](getting-started.md#brand-trial).

The agent doesn't replace your judgment. You decide the scope, the target design, and the content model, and you validate the result before it goes live.

## Who Can Use the Agent {#who-can-use-ema}

The agent works from requests in plain language: you describe what you want, check the result in the preview, and it writes the code and content. What you need is expertise in the part of the site that you work on, and enough technical literacy to judge the result and follow these guides.

The person who knows an aspect of the site best is often the best person to direct the agent on it:

| Expertise | What you can do with the agent |
|---|---|
| Business and marketing | Migrate a few of your own pages, judge Edge Delivery Services on your content, and ask for corrections. Auto mode migrates pages without step-by-step prompting. |
| Visual and UX design | Refine layouts, typography, colors, spacing, and responsive behavior against the brand's style guide. A designer who knows the brand rules often directs visual changes more precisely than a developer. |
| Content and authoring | Decide how pages break down into sections, default content, and blocks, and check that authors find the result easy to edit. See [How Edge Delivery Services Works](#eds-basics). |
| Development | Build blocks with complex behavior, integrate APIs and services, debug, refactor, and review every code change before it reaches production. |
| Architecture and project leadership | Scope the migration, choose the content destination and integrations, divide the work, and decide when the site is ready to release. |

Many people combine several of these. The agent doesn't limit requests by role. Your permissions in Git and in the content destination decide what you can change outside your workspace.

### Broader Contribution, Same Production Control {#production-control}

The Experience Modernization Agent widens who can contribute to a site, not who approves what goes live. Developers stay in control of every line of code that reaches production.

That control sits in your Git provider, not in the console, so it holds however a change is made. The agent writes standard Edge Delivery Services code and pushes it to your repository, where the repository's rules apply. When people other than developers work on the code:

1. Protect `main` with [branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) that requires a pull request approved by a developer, and don't let other contributors bypass it.
1. Contributors push their work with **Create new PR**, which puts it on a new branch with a pull request. For repositories connected through Cloud Manager, the console pushes the branch, and you open the pull request with your Git provider's tools.
1. A developer reviews the pull request, checks the result on the preview URLs that it lists, and merges it.

If a contributor turns on **Allow LLM to use my git credentials**, the agent pushes with that contributor's access, so the same protection applies to it. Publishing content is controlled separately, by the site's publish role. See [Control over Changes](evaluate.md#security-control).

## Choose Your Task {#choose-task}

Each row links to a task guide with the steps and the checks that tell you when you are done. If your site already runs on Edge Delivery Services, [connect it](getting-started.md#existing-site), then start with restyling or block development; a migration is not required.

| Your goal | Start here | Done when |
|---|---|---|
| Demonstrate a few customer pages | [Create a customer demo](getting-started.md#customer-demo) | The selected branded pages and demo paths work, with unfinished behavior identified. |
| Try Edge Delivery Services and the agent with your brand's content | [Start with Auto mode](getting-started.md#brand-trial), or [start from a repository](getting-started.md#repo-start) | You can make a useful edit, retain the work, and return to it. |
| Start a new site, or connect one that runs on Edge Delivery Services | [Start from a repository](getting-started.md#repo-start) | Your site is connected in the console, and a change you asked for is saved and previewed. |
| Migrate a production site | [Production migration](production-migration.md) | The agreed inventory, authoring, integrations, and release checks are accepted. |
| Apply a new design during migration | [Restyle during migration](restyling.md#during-migration) | Source content is preserved in the approved target design. |
| Restyle an existing site | [Restyle an existing site](restyling.md#existing-site) | The affected pages adopt the design without unintended content or behavior changes. |
| Change how parts of a site look, as a designer whose work a developer reviews | [Make visual changes](visual-changes.md) | The change works at every screen size, and a developer has the pull request. |
| Create, update, or refactor blocks | [Block development](block-development.md) | Reusable code and authorable examples pass the agreed checks. |

An automated run or a preview shows how the pages look. The completion checks of your task establish the rest: that authors can edit the pages, that integrations work, and that the site is ready to release. To find the guides for your role, see [Start Here by Role](#start-by-role).

## Understand Your Project {#project-foundations}

Each task touches several separate parts of a project. Keep them apart when you start:

* **Source:** The authorized website, content, or design that you provide.
* **Console workspace:** Your own working copy of the project's code and content, where the agent makes its changes before you push or upload them. See [Work Safely in an Independent Workspace](#independent-workspace).
* **Code:** The site's Git repository and working branch that contain styles, scripts, and blocks.
* **Content destination:** Where the migrated content is stored and which editor authors use. Adobe strongly recommends document-based persistence with Experience Workspace for new implementations. The alternative is Experience Manager authoring with JCR persistence and the Universal Editor. The source CMS does not determine this choice. See [Where Content Is Stored and How Authors Edit It](#content-storage).
* **Preview and publication:** The preview site, where you check saved content with your code, and the live site, where approved changes are released. See [How Changes Go Live](#code-content-lifecycle).

Edge Delivery Services runs complex enterprise websites. Its pages are standard HTML, CSS, and JavaScript, so a block can call any API from the browser, such as search, commerce, or personalization, as on any other website. Spreadsheets publish as JSON and a query index lists the site's pages, so blocks can also build listings and filters from your own content. Business logic stays in the services that own it. Each integration is project work that you specify and test, and the agent can write its block code once you have decided how it should work. See [Build a Dynamic Block](block-development.md#dynamic-blocks).

### How Edge Delivery Services Works {#eds-basics}

Code and content are stored in different places. Blocks, styles, and scripts live in a Git repository. Content lives in a separate content source that authors edit. Authors can change pages without a code release, and developers can change code without touching content. It also means that pushing code never saves content, and uploading content never changes code.

When Edge Delivery Services renders a page, it turns the authored content into plain semantic HTML:

* **Default content** is everything outside blocks: headings, paragraphs, lists, images, and links.
* A **block** is a reusable component, such as a hero or a set of cards. In the HTML, it is a `div` with the block name as its class. The project's `blocks/<name>/<name>.js` and `blocks/<name>/<name>.css` decorate it in the browser.
* **Sections** split a page into groups of default content and blocks, for example to give part of a page a different background.

Content and styling are separate concerns. The content is a plain document of headings, text, images, and links, grouped into sections and blocks; with Experience Manager authoring, the same structure is stored in the JCR. The project's CSS and JavaScript decide how that content looks and behaves. In the browser, the JavaScript can restructure the page's markup however a design needs it, and a block can even run a complete web application, such as a search or a calculator; see [Widgets](https://www.aem.live/docs/widgets). Any design can therefore be built on the same content without restructuring it. The agent can change both, but they stay independent: a new design is a code change, and editing content needs no code change.

Keep the content structure semantic and simple, because authors work with it every day. Use default content wherever it works. Add a block only where authors need to mark which content forms a component, such as a set of cards, because the code can't infer it from default content. Avoid blocks inside blocks, and keep the number of blocks and variants small. [David's Model](https://www.aem.live/docs/davidsmodel) explains these and other content-modeling rules, and the agent applies them when it maps imported content to default content and blocks.

Most projects start from the [AEM boilerplate](https://github.com/adobe/aem-boilerplate), which is written in plain JavaScript and CSS.

### Work Safely in an Independent Workspace {#independent-workspace}

The agent doesn't change your Git repository or your content destination directly. It works in a console workspace: your own working copy of the project, hosted by Adobe and not shared with other users. The workspace holds a checkout of one branch of your Git repository, and copies of the content pages that you imported, opened, or pulled.

Everything that the agent does happens there first. You can ask for a sweeping redesign, check it in the console preview, and discard what you don't want, while your repository, the authors' pages, and the live site stay unchanged. Work leaves the workspace only when you send it, in two separate operations:

* **Push code** sends the changed files that you select to your Git repository, as a commit on the current branch or as a new pull request.
* **Upload content** sends the pages that you select to Experience Workspace or the author instance, where they replace the saved versions of those pages.

[Agent permissions](console.md#settings-page) let the agent do the same for you. See [Control over Changes](evaluate.md#security-control).

The independence works in both directions: changes that others push or upload don't reach your workspace until you pull them. See [Sync Menu](console.md#sync-menu) and [Collaborating on a Project](#collaboration).

### How Changes Go Live {#code-content-lifecycle}

Code and content reach the live site in different ways:

* **Code:** Edge Delivery Services fetches your code from GitHub through the [AEM Code Sync](https://github.com/apps/aem-code-sync) app, or from another Git host through Cloud Manager ([Bring Your Own Git](https://www.aem.live/developer/byo-git)). Each branch gets its own URLs, and a change pushed to a branch shows on that branch's preview and live URLs at the same time. Code has no separate publish step: merging into `main` updates the code of the production site immediately.
* **Content:** Authors first preview a page, which copies the saved content to the preview site on `*.aem.page`. They then publish it, which makes it live on `*.aem.live`. Authors do both from the authoring UI or from the [AEM Sidekick](https://www.aem.live/docs/sidekick) browser extension.

Preview URLs follow the pattern `https://{branch}--{repo}--{owner}.aem.page`, and live URLs the same pattern on `aem.live`. `{owner}` is the GitHub organization or user that owns the repository, and `{repo}` is the repository name.

Pushing code doesn't publish content, but merging into `main` changes the live site's code straight away. Check a branch on its own URLs before you merge it.

### Names You May See {#names}

Adobe has renamed several of these products, and they are often abbreviated. These docs write the names in full. The table maps them to the older names and abbreviations that you meet on aem.live, in the console, in URLs, and in older articles.

| Name | What it refers to |
|---|---|
| Adobe Experience Manager (AEM) | Adobe's content management system. Edge Delivery Services is part of Experience Manager Sites. |
| Brand Experience Agent | The family of Experience Manager agents that the Experience Modernization Agent belongs to. |
| Experience Modernization Agent (EMA) | The agent described in these docs. |
| Experience Modernization Console | The web interface where you use the agent, at `aemcoder.adobe.io`. |
| Console workspace | Your project's hosted working copy in the console, where the agent imports content and changes code before you upload or push them. Labels such as **Checkout to workspace** and **Your workspace is paused** refer to it. It is unrelated to Experience Workspace. |
| Edge Delivery Services (EDS) | Experience Manager's website delivery service. The architecture was originally developed as Project Helix, later code-named Franklin, and older articles use those names. The `hlx` in hostnames such as `admin.hlx.page`, the admin API, comes from Helix. |
| `*.aem.page`, `*.aem.live` | A site's preview and live URLs. Older projects and documentation may show the earlier domains, `hlx.page` and `hlx.live`. |
| AEM Sidekick | The browser extension that authors use to preview and publish pages. |
| AEM Code Sync | The GitHub app that lets Edge Delivery Services fetch your code to serve it. |
| AEM Code Connector | The GitHub app that lets the console push changes and open pull requests in your repository. |
| Experience Workspace | The visual authoring UI for document-based content, at `da.live`. It was formerly called Document Authoring (DA), and some console labels still use that name. See [Document-Based Persistence](#document-based). |
| Universal Editor | Adobe's visual editor for content stored in Experience Manager. Projects with Experience Manager authoring use it. |
| Experience Manager authoring, JCR persistence | Edge Delivery Services with content stored in the Java Content Repository (JCR) of an Experience Manager as a Cloud Service author instance and edited in the Universal Editor. Also called AEM authoring, and previously Crosswalk. |
| IMS | Adobe's identity service, which handles sign-in with your Adobe ID. |

## Where Content Is Stored and How Authors Edit It {#content-storage}

The agent asks where the migrated content should be stored. This is a question about persistence: which repository holds the content. Which editor authors use is a separate question. With either option, authors get a visual editor and Edge Delivery Services delivers the pages.

| | Document-based persistence | Experience Manager authoring with JCR persistence |
|---|---|---|
| Where content is stored | The document-based content repository | The JCR of your author instance |
| Visual editor | Experience Workspace | Universal Editor |
| Page delivery | Edge Delivery Services | Edge Delivery Services |
| Recommendation | Strongly recommended for new implementations, including large sites | Fully supported; choose it when a requirement depends on content staying in the JCR |

### Document-Based Persistence with Experience Workspace {#document-based}

With document-based persistence, content is stored as documents in the document-based content repository. "Document-based" describes storage only, not the authoring experience. Authors edit pages visually in [Experience Workspace,](https://www.aem.live/docs/ew/about) the visual authoring UI for Edge Delivery Services. Experience Workspace also offers an AI assistant, collaboration, and Experience Manager Assets integration. It is off by default and is turned on per site or organization in the project's configuration. When you transfer an Auto mode site to a document-based destination with [**Make it yours**](getting-started.md#make-it-yours), the transfer turns it on for that site.

"Document-based authoring" has meant different things over time, so check when a page or article was written:

* When Adobe introduced Edge Delivery Services in 2023, it meant writing pages in Google Docs or Microsoft Word, stored on Google Drive or SharePoint. These remain supported content sources.
* Document Authoring (DA) is Adobe's own document editor and content repository, at `da.live`.
* Experience Workspace is DA's new name. It adds a visual canvas editor, and the content stays in the same repository.

Uploads and transfers of document-based content go to Experience Workspace at `da.live`.

>[!NOTE]
>
>The rename from Document Authoring to Experience Workspace is an upgrade, not a content migration: existing DA content stays where it is. Some console labels and screens still say **Document Authoring** or **DA**. In these docs, they refer to Experience Workspace and its repository.

### Experience Manager Authoring with JCR Persistence {#jcr-persistence}

With this option, content is stored in the Java Content Repository (JCR) of an Experience Manager as a Cloud Service author instance. This is Edge Delivery Services running on top of the JCR stack, a setup previously called Crosswalk. Authors edit pages with the [Universal Editor,](/help/implementing/universal-editor/introduction.md) Adobe's visual editor for content on the author instance, and the platform still delivers the pages. The pages are not rendered by HTL and Java as in traditional Experience Manager publishing. Template repositories for this setup, such as `aem-block-collection-xwalk`, still carry `xwalk` in their names.

>[!NOTE]
>
>In these docs, *Experience Manager authoring* names this persistence option. The *author instance* is the Experience Manager as a Cloud Service environment where that content is stored and edited.

### Adobe's Recommendation {#recommendation}

For any new implementation, Adobe strongly recommends document-based persistence with Experience Workspace over Experience Manager authoring with the Universal Editor. This includes large websites with thousands of pages.

Document-based authoring used to mean editing in Microsoft Word, Google Docs, or a document-style editor. That limited visual page editing, so teams that needed it often chose Experience Manager authoring. Experience Workspace now gives document-based content a visual editor, so there is little reason left for a brand to avoid it.

Experience Manager authoring with JCR persistence remains fully supported. Choose it when a specific requirement depends on content staying in the JCR. For headless content, delivered through APIs rather than as web pages, the Universal Editor remains the recommended editor.

## How the Agent Migrates at Scale {#migration-at-scale}

The agent does not send every page through the AI model. Interpreting each page separately would not scale to thousands of pages, and the model could treat similar pages slightly differently each time. Instead, the AI works out the mapping on one representative page per template, and the agent turns that mapping into code that runs on the template's other pages:

1. **Group pages into templates.** The [site catalog](site-catalog.md) groups the source site's pages into templates, which are pages that share a layout. If you migrate pages without a catalog, each page that you name starts a template of its own.
1. **Migrate a representative page.** For each template, the agent first migrates one representative page: a real page of the source site that shows the template's typical layout and, ideally, most of its blocks and variations. The site catalog proposes one for each template. If another page of the template shows more of its blocks, choose that page instead; blocks that the representative page lacks are only added later, when an imported page needs them. The AI model analyzes the representative page, maps its content to default content and blocks, and creates the blocks that it needs or reuses existing ones. This page is the worked example for the rest of the template.
1. **Generate an import script.** The agent writes an import script for the template. Its parsers extract each block's content from the source HTML, and its transformers clean up the page as a whole. They are JavaScript files in the project's `tools/importer/` folder, so they are versioned in Git with the rest of your code.
1. **Refine the pattern, not the page.** When you ask for a correction, the agent changes the block, parser, or transformer that produced the result instead of editing one page's output. The correction then applies to every page of the template, and later templates reuse the blocks that already exist.
1. **Import the remaining pages in bulk.** The bulk import runs the import script on the template's other pages without the AI model interpreting each one. The agent then compares the imported pages with their source pages, fixes the parsers or transformers behind pages that differ too much, and imports those pages again.

Corrections accumulate in the blocks and import scripts, so each one also improves the pages that you import next. Validate a few pages of each template before you import all of them. See the [bulk import workflow](site-catalog.md#bulk-import).

You can also change the structure that the agent builds on. In the [site planning UI](site-catalog.md#planning-actions), or by asking in chat, you can move pages to another template, create a template from a subset of pages, make one block a variant of another, or give a variant its own block. These changes update the catalog, and the agent follows them the next time it generates blocks or imports pages. They don't change pages that you already imported. To consolidate the design itself, for example from a new style guide or Figma designs, see [Restyle Sites](restyling.md). To consolidate block code, see [Refactor Without Changing the Outcome](block-development.md#refactor).

>[!NOTE]
>
>A template in the console is a group of source pages with the same layout, which the agent uses to plan and import them. It is not the same as the `template` page metadata, which adds a class to the page's `body` element so that the project's code can style or decorate those pages differently.

You can align the two. When the pages of one of these templates should look or behave differently from other pages on the new site, ask the agent to write matching `template` metadata into those pages and to style them in the project's code. For example:

> For the article template, set the page metadata `template` to `article` in the import script, and give article pages a narrower main column.

Because the import script sets the metadata, every article page that you import later gets it too.

## What the Agent Remembers {#memory}

The agent has no memory of its own that carries over between conversations. What it knows about your project comes from three places:

* **Its built-in skills,** the workflows that Adobe provides and updates with each release.
* **The current conversation.** The console keeps your project's conversation so that you can continue it later. When a conversation gets long, the agent summarizes earlier messages to make room, and details can be lost. **Clear chat** starts a new conversation without the earlier history.
* **The files in the console workspace:** the checked-out Git repository with your code, the working copy of imported content, and temporary files from the migration.

To make the agent remember a decision or convention, write it in a file in your Git repository. It currently uses Claude models, which load a file named `CLAUDE.md` from the repository root at the start of every conversation. In projects created from the AEM boilerplate, `CLAUDE.md` contains one line, `see @AGENTS.md`, which loads `AGENTS.md` as well. Your project instructions belong in `AGENTS.md`, and the agent reads other project files when `AGENTS.md` or your request points to them. The model is an implementation detail that can change, so don't write instructions that depend on it. See [Project Instructions and Memory](project-instructions.md).

## Collaborating on a Project {#collaboration}

Several people can work on the same project with the agent, each in their own [console workspace](#independent-workspace). They share code through Git and content through the content destination. The console has no features yet for coordinating them: it doesn't show who is working on what, and it doesn't merge two people's changes to the same page. Agree who works on what, and keep talking to each other.

Scope matters more with an agent than without one. A single request can change many files, so when two people change the same blocks or styles at the same time, someone has to resolve conflicts across many files by hand.

### Start with One Person, Then Divide the Work {#divide-work}

The first steps of a project lay the foundation that everything else builds on: the global styles, the first blocks, and the import scripts of the first templates. Let one person set them up. Before you divide the work, check that the blocks fit representative content and are easy for authors to use. [David's Model](https://www.aem.live/docs/davidsmodel) explains what makes a good content model for Edge Delivery Services.

Once the team agrees on the blocks, divide the work so that people change different files:

* **By block:** One person refines the cards block while another builds a carousel.
* **By template:** Each person refines the import script of a different template. See [How the Agent Migrates at Scale](#migration-at-scale).
* **By expertise:** A designer refines the styling of existing blocks while a developer builds an integration.

Don't give two people the same block, the global styles, or the same import script at the same time unless they agree how to coordinate.

### Share Code in Small Steps {#share-code}

1. Agree on a shared branch, such as `main` or a development branch. Each person switches their workspace to it with **Switch branch** in the [Code view](console.md#changes-actions).
1. Keep each request to the agent focused on one block, template, or task. Push the result as soon as it works, with **Create new PR**: the console pushes your changes to a new branch, opens a pull request into the shared branch, and leaves your workspace on the new branch.
1. Review and merge pull requests often. Small changes conflict less and are quicker to review, and a pull request that stays open for days collects conflicts.
1. Before you start a new task, switch back to the shared branch with **Switch branch** and pull it with **Sync** > **Pull** > **Code**, so that you build on everyone's merged work.

Pulling code requires a workspace without uncommitted files, so push or discard your changes first. If someone changed the same lines as you, the console cancels the pull and leaves your work as it was. See [If Someone Else Changed the Branch](getting-started.md#push-conflicts).

Small, frequent pushes also give the team a readable history of what the agent changed and why. To get one commit per request, see [Leave a Record of Each Request](project-instructions.md#trace).

### Coordinate Content Changes {#share-content}

Content has no merge. Your workspace holds copies of the pages, and an upload replaces the page in the content destination with your copy. If two people change the same page, the last upload wins, and the other person's changes are lost. Give each page, or set of pages, to one person at a time.

To get pages that others uploaded into your workspace:

* Open a page that shows a cloud icon in the [content view](console.md#content-view). The console downloads it into your workspace.
* In document-based projects, select **Sync** > **Pull** > **Content** to download every page from Experience Workspace. It replaces your local copies, including edits that you haven't uploaded, so upload the edits that you want to keep first.

### Change Content Structure in the Import Scripts {#import-scripts}

During a migration, the content comes from the source site, and the import scripts decide its structure. When you change how content is structured, such as which content becomes a block or how a page splits into sections, ask the agent to change the import script too, not only the imported pages. The import script is code, so the change is reviewed and merged like any other, and the next import applies it to every page of the template. This is also what lets the migration scale to many pages.

An edit to a single page doesn't carry over. The agent tells you that such an edit is local, and importing the template again overwrites it.

Once authors start editing the migrated pages in the content destination, their pages become the source of truth. Importing or uploading those pages again from a workspace overwrites the authors' work, so agree with the authors first.

## Migration and Site Creation Capabilities {#creation-migration}

Skills are the agent's built-in workflows for specific kinds of tasks. You don't need to name them: describe the task, and the agent chooses the skill. The following capabilities are always available:

| Capability | What the agent does | Learn more |
|---|---|---|
| Site catalog and planning | Discovers the source site's pages, groups them into templates, and identifies their blocks and variants, with screenshots and a report. You review and adjust the result in the site planning UI. | [Site Catalog Skill](site-catalog.md) |
| Page migration | Imports a source page, maps its content to [default content and blocks](#eds-basics), and creates new blocks or reuses existing ones. | [Migrate a site or page](prompting-guide.md#migrate-a-site) |
| Design migration | Extracts the design system, such as colors, fonts, and spacing, into CSS custom properties and global styles, and styles each block to match the source. | [Design migration](prompting-guide.md#design-migration) |
| Header, navigation, and footer | Rebuilds the parts that every page shares as blocks and content. | [Navigation setup](prompting-guide.md#navigation-setup) |
| Import scripts and bulk import | Writes an import script for each template and runs it on the template's other pages. It then compares the imported pages with their source pages and fixes the script for pages that differ. | [Bulk import](prompting-guide.md#bulk-import) |
| Visual critique | Compares a migrated block, page, or the whole site with the source and fixes content, structure, and styling differences. | [Block critique](prompting-guide.md#block-critique) |
| Protected source pages | Reads source pages that need a custom request header, HTTP Basic authentication, or bearer authentication. | [Protected Site Authentication](console.md#protected-site-authentication) |
| Experience Manager authoring models | Creates the block models that the Universal Editor uses, for projects that store content on an author instance. | [Experience Manager authoring projects](getting-started-aem-authoring.md) |
| Console tour | Explains the console's views and actions. Ask "Give me a tour of the console." | [Modernization Console](console.md) |

Optional add-ons extend these capabilities when a project needs them: Figma import, guided redesign (the Stardust add-on), project documentation, forms migration, commerce pages, block library setup, Edge Delivery Services troubleshooting, modern web guidance, and design craft. The agent offers to turn an add-on on when your request needs it, and you can save the choice in the repository so that it applies to the whole team. See [Optional Capabilities](console.md#optional-capabilities).

## Figma-Based Migrations and Page Creation {#figma}

In addition to live-site migrations, the agent can use Figma as a design source. Through the Figma import add-on, it reads the design and turns its colors, typography, spacing, and variables into the site's CSS custom properties, and its components into blocks or variants. Each person who uses Figma stores their own Figma personal access token in the console's [settings](console.md#settings-page). For what to approve, such as access, Figma seats, and the data sent to the AI model, see [Figma and Design Systems](evaluate.md#figma). Designers can start with [Make Visual Changes](visual-changes.md#figma).

### Redesign Migration Using Figma-Derived Blocks {#figma-redesign}

When you migrate an existing website into a redesigned experience, the agent [first creates the redesigned block collection from Figma components.](prompting-guide.md#figma-redesign-migration) It then runs site migration against the live source website and maps source content into those Figma-derived blocks.

* **Figma** is the target design and block-library source.
* **The live website** remains the source of content.
* Content is validated against the source website; visual output is validated against the Figma-derived design system.

### Create a New Page from Figma {#figma-new-page}

When a page does not exist on a source website, the agent [generates a new page directly from a Figma frame or page.](prompting-guide.md#figma-new-page-from-figma) It maps Figma sections to existing blocks, default content, or new variants. Text and assets come from Figma.

For details on these workflows, individual Figma block migration, and prompting tips, see the [Prompting Guide for the Experience Modernization Agent.](prompting-guide.md)

## Block Development Capabilities {#block-development}

With or without a migration, the agent works on the project the way a developer does: it reads and changes the files in the repository, runs the project's linting and tests, and checks the result in the preview. An Edge Delivery Services project is plain HTML, CSS, and JavaScript, so this covers everything the site does, from a CSS tweak to a block that calls an API or runs a complete application.

* It follows Content-Driven Development (CDD): it starts from real content and from how authors will create it, then writes the code, which keeps content models easy for authors.
* Before it writes a new block, it looks for one to reuse in your project, in the Adobe-maintained [Block Collection](https://www.aem.live/developer/block-collection), and in the community-driven [Block Party](https://www.aem.live/developer/block-party/).
* It tests and debugs its changes in the console preview before you push them.

For the procedures, see [Create, Update, and Refactor Blocks](block-development.md). For example prompts, see the [prompting guide](prompting-guide.md#block-development-capabilities).

## Experience Modernization Console {#console}

The Experience Modernization Console is the agent's web-based, AI-assisted development environment for Edge Delivery Services, at [`aemcoder.adobe.io`.](https://aemcoder.adobe.io)

* The console requires no local setup, so you can start prompting changes in natural language right away.
* You perform day-to-day development tasks, check the result in the console's preview, upload content to your authoring destination, and check it again on the preview site.
* The console supports enterprise governance through standard GitHub review workflows.
* The AI agent works without receiving the credentials that you configure. See [Security and Data Handling.](evaluate.md#security)

The self-service Experience Modernization Console is generally available. You can request access to ensure a smooth onboarding experience.

To get started with the console:

* For document-based persistence with Experience Workspace, recommended for new implementations, [use the getting started guide.](getting-started.md)
* For Experience Manager authoring with JCR persistence and the Universal Editor, [use the guide for that option.](getting-started-aem-authoring.md)

## Project Documentation Skill {#project-documentation}

[Generate project documentation](project-documentation.md) for authors, developers, and administrators. Review its coverage against the connected code and accessible configuration. Record remaining work and validated examples for the next person or agent.

## Site Catalog Skill {#site-catalog}

The site catalog skill analyzes discovered pages, groups them into templates (pages that share a layout) and block variants, and provides screenshots and a report for review. It discovers the pages that the sitemap lists or that links lead to, so check the result against your own inventory. The skill helps:

* **Anyone starting a migration project** to establish an inventory of page layouts, block variants, locales, and pages per template, then reconcile it with the agreed site scope
* **Teams doing bulk imports** to identify which pages share the same layout, manually import and perfect the representative pages first, then bulk-import all remaining pages for that template
* **Project leads and stakeholders** to understand the scope of the effort

For details, see [Site Catalog Skill.](site-catalog.md)

## Agentic Outcome Engineer (AOE) Delivery {#aoe-delivery}

For complex migrations or accelerated outcomes, Adobe offers Agentic Outcome Engineer (AOE) delivery. In this optional service, Adobe engineers operate the agent on your behalf and combine its automation with engineering work and expert guidance to deliver production-ready results. For details, see [AOE Delivery of the Experience Modernization Agent.](aoe-delivery.md)

If you are interested in the AOE model for your next migration:

* Contact your Adobe representative or account team to start scoping and scheduling.
* Adobe confirms eligibility, estimates the engagement, and proposes an engagement plan.

## Security and Data Handling {#security}

The agent works without receiving the credentials that you configure, each user works in a separate environment, and you decide when changes reach your Git repository and your content destination. For access and isolation, credentials, what the AI model processes, the control over each step, and where work is stored, see [Security and Data Handling](evaluate.md#security).

## Limitations {#limitations}

Use only websites and designs that you are authorized to migrate. The selected workflow must be able to reach and read the source. If the site uses bot protection, arrange access with its administrator. See [source sites with bot protection](troubleshooting.md#bot-protection).

* Pages that require sign-in or a secret header can be migrated when the source accepts a custom request header, HTTP Basic authentication, or bearer authentication. Configure the credentials in the console's [Protected Site Authentication](console.md#protected-site-authentication) settings, or in the authentication fields of Auto mode. Do not put secrets in chat. This is not intended for personally identifiable information (PII) or real end-user data.
* Sources reachable only through a VPN or blocked by a firewall remain unsupported, even with valid credentials. So do sources that require another sign-in flow, such as an interactive single sign-on (SSO) form. Ask the site administrator for an internet-reachable staging or origin host that accepts a supported method.
* The agent loads each source page in a browser and reads it once it has rendered. That includes content that scripts insert and content that the page contains but CSS hides, such as a closed accordion panel. Content that appears only after a visitor clicks or types isn't in the page at that moment, so it isn't captured. Check such pages in the screenshots, and add the missing content after import or ask for a way to capture it.
* The agent targets Edge Delivery Services, including sites that use [Experience Manager authoring with the JCR.](#jcr-persistence) It does not convert a project to HTL-based publishing or an API-only/SPA delivery stack.
* Page import copies what the source page shows: its content and its design. It can't see how the source's servers produced that page. Content inheritance, reuse through content fragments, personalization rules, search, form processing, and other business logic run there, so import copies their output on that page, not the logic. The agent also rebuilds the markup rather than copying it, so the source's scripts, such as analytics and experimentation tags, don't come along. Auto mode's **Include integrations** option carries over supported analytics, tag manager, and consent settings. Decide how each of the others works on the new site; the agent can then build the blocks and code for it. See [What Remains Project Work](evaluate.md#project-work).
* The agent's visual critique compares how the result looks with the source. Looking the same doesn't show that authors can edit the page, that interactions work, or that it is accessible and fast on real devices, so check those as part of [acceptance](production-migration.md#acceptance).

Auto mode is in early access and needs its own [access request](getting-started.md#brand-trial). The [optional capabilities](console.md#optional-capabilities) on offer can change between releases. Check the controls and limits shown for your account. [AOE service scope](aoe-delivery.md#scope) is agreed separately from product capabilities.

## Next Steps {#next-steps}

Choose a task above, then use [Getting Started](getting-started.md) for shared console setup. For an existing Edge Delivery Services project, connect its repository and start with the relevant development or restyling task; a new migration is not required. If you are deciding whether your team should use the agent, read [Evaluate and Approve the Experience Modernization Agent](evaluate.md).

For short answers to common questions, such as access, Auto mode, transfers, protected source sites, and recovery, see the [Experience Modernization Agent FAQ](faq.md).

To learn what changed in recent versions of the console, see the [Experience Modernization Agent release notes.](/help/release-notes/modernization-agent/current.md)
