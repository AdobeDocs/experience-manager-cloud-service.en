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

The Experience Modernization Agent (EMA) is Adobe's AI development agent for [Edge Delivery Services (EDS)](/help/edge/overview.md). It gives you a ready-to-use EDS development environment in the browser, with nothing to install, and an agent that migrates, builds, and evolves EDS sites. Your Git repository remains the system of record for the site's code.

EDS is the AEM service that delivers websites, and it is part of AEM Sites. It serves authored content as plain semantic HTML, and the project's own CSS and JavaScript style and decorate it in the browser. If you already build with HTML, CSS, and JavaScript, most of an EDS project will look familiar. The AEM-specific parts are explained in [Understand Your Project](#project-foundations). Adobe has renamed several of these products over time. If you meet older names such as Helix, Franklin, or Crosswalk, see [Names You May See](#names).

## Introduction {#introduction}

EMA is part of the [Brand Experience Agent.](/help/ai-in-aem/agents/brand-experience/overview.md) It automates the repetitive parts of building an EDS site: importing content, mapping it to blocks, extracting the design, and writing block code. You work in the hosted Experience Modernization Console, using natural-language requests and previews. You don't need Docker or a local command-line environment. With Auto mode, in early access, EMA can also migrate a first set of pages on its own and email you when it's done.

Use EMA to move web properties from other CMSes, older AEM implementations built from Java and HTL components, or static sites onto EDS, the current AEM website stack. Consolidating there gives you:

* **Lean, standard code:** Pages are semantic HTML, styled and decorated by your own CSS and JavaScript and served from the edge. EDS sites can reach a Lighthouse score of 100.
* **Room to grow:** EDS runs large multi-market and multi-language sites. Its largest sites have more than 100,000 pages.
* **Visual authoring:** Authors edit pages visually in Experience Workspace, or in the Universal Editor when content stays in AEM. See [Where Content Is Stored and How Authors Edit It](#content-storage).
* **Pages that AI systems can read:** AI crawlers and answer engines often read the raw HTML without running JavaScript. Because EDS serves lean semantic HTML, the migrated content is readable to them, so migration and AI readiness happen in the same step. This does not guarantee search rankings.

EMA rebuilds your pages on an EDS block system that follows EDS architecture. It decomposes each page into sections and content, maps the content to default content and reusable blocks, and extracts the design system into global styles and block CSS. It then imports further pages in bulk with the same mappings, using generated import scripts rather than having the AI model interpret every page. See [How EMA Migrates at Scale](#migration-at-scale). EMA does not clone the source markup, which would carry over the old site's technical debt. Expect a close first pass that you refine by prompting and validate before you scale.

After go-live, the same environment keeps working on the site. You can restyle it to a new brand, including from Figma designs, add blocks, update or refactor existing blocks, create pages from the established blocks, debug problems, and generate project and handover documentation. You can also connect an existing EDS project and start there, without a migration.

You stay in control of every change. Code goes to your Git repository and content goes to the authoring destination you chose. Until you push or upload them, or turn on [agent permissions](console.md#settings-page) that let the agent do so, changes stay in the console workspace, where you review and preview them and can discard what you don't want. Your permissions, repository policies, and publication workflow determine what you can change and release.

## Why Use EMA {#benefits}

Before anyone can judge a migration to EDS, a developer usually has to do a lot of repetitive work. They list the source pages and work out which ones share a layout. They decide how each part of a page becomes EDS content, then write the blocks and their styles and extract the colors and fonts. Finally, they write import scripts, import the pages, and compare them with the originals. EMA does this work with you, in one environment:

* **A first result on your own pages.** Give EMA a source page and it rebuilds it as an EDS page, with blocks, styles, and editable content, that you can check in the console's preview. You judge the approach on your own content rather than on a sample site, without setting up a local environment first.
* **A plan that you can see.** The [site catalog](site-catalog.md) inventories the source site and groups its pages into templates and blocks, with screenshots. Use it to scope and size the project and to decide what to migrate first.
* **Fixes that scale.** EMA turns each correction into a change to a reusable block or import script, so a fix on one page applies to every page of that template. See [How EMA Migrates at Scale](#migration-at-scale).
* **A standard EDS project that you own.** The result is plain EDS code in your Git repository that follows the conventions of the AEM boilerplate and the [Block Collection](https://www.aem.live/developer/block-collection). Developers can continue in EMA, in their own editor, or with other AI tools. Nothing ties the site to EMA.
* **Help after go-live.** The same agent restyles the site for a new brand, adds and refactors blocks, creates pages from existing blocks, debugs problems, and documents the project. You can start EMA on an existing EDS site without a migration.
* **Project knowledge that lasts.** EMA follows the conventions that you keep in `AGENTS.md` and related files in the repository, so every conversation starts with what your team has agreed. See [What EMA Remembers](#memory).
* **Unattended runs.** Auto mode, in early access, migrates a set of pages, including their design, without step-by-step prompting and emails you when it finishes. See [Trial Your Brand's Content](getting-started.md#brand-trial).

EMA doesn't replace your judgment. You decide the scope, the target design, and the content model, and you validate the result before it goes live.

## Choose Your Task {#choose-task}

Each row links to a task guide with the steps and the checks that tell you when you are done. If you already run an EDS site, start with restyling or block development; a migration is not required.

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
* **Content destination:** Where the migrated content is stored and which editor authors use. Adobe strongly recommends document-based persistence with Experience Workspace for new implementations. The alternative is AEM authoring with JCR persistence and the Universal Editor. The source CMS does not determine this choice. See [Where Content Is Stored and How Authors Edit It](#content-storage).
* **Preview and publication:** The EDS preview site, where you check saved content with your code, and the live site, where approved changes are released. See [How Changes Go Live](#code-content-lifecycle).

EDS supports complex enterprise websites. Search, commerce, personalization, and other integrations can require project-specific implementation and testing; they are not reasons to restrict EDS to simple or static sites.

### How EDS Pages Work {#eds-basics}

EDS stores code and content in different places. Blocks, styles, and scripts live in a Git repository. Content lives in a separate content source that authors edit. Authors can change pages without a code release, and developers can change code without touching content. It also means that pushing code never saves content, and uploading content never changes code.

When EDS renders a page, it turns the authored content into plain semantic HTML:

* **Default content** is everything outside blocks: headings, paragraphs, lists, images, and links.
* A **block** is a reusable component, such as a hero or a set of cards. In the HTML, it is a `div` with the block name as its class. The project's `blocks/<name>/<name>.js` and `blocks/<name>/<name>.css` decorate it in the browser.
* **Sections** split a page into groups of default content and blocks, for example to give part of a page a different background.

Most projects start from the [AEM boilerplate](https://github.com/adobe/aem-boilerplate), which is written in plain JavaScript and CSS.

#### How Changes Go Live {#code-content-lifecycle}

Code and content reach the live site in different ways:

* **Code:** EDS fetches your code from GitHub through the [AEM Code Sync](https://github.com/apps/aem-code-sync) app, or from another Git host through Cloud Manager ([Bring Your Own Git](https://www.aem.live/developer/byo-git)). Each branch gets its own URLs, and a change pushed to a branch shows on that branch's preview and live URLs at the same time. Code has no separate publish step: merging into `main` updates the code of the production site immediately.
* **Content:** Authors first preview a page, which copies the saved content to the preview site on `*.aem.page`. They then publish it, which makes it live on `*.aem.live`. Authors do both from the authoring UI or from the [AEM Sidekick](https://www.aem.live/docs/sidekick) browser extension.

Preview URLs follow the pattern `https://{branch}--{repo}--{owner}.aem.page`, and live URLs the same pattern on `aem.live`. `{owner}` is the GitHub organization or user that owns the repository, and `{repo}` is the repository name.

Pushing code doesn't publish content, but merging into `main` changes the live site's code straight away. Check a branch on its own URLs before you merge it.

### Names You May See {#names}

Adobe has renamed several of these products. The table maps the names that appear in these docs, the console, and URLs.

| Name | What it refers to |
|---|---|
| Brand Experience Agent | The family of AEM agents that EMA belongs to. |
| Experience Modernization Agent (EMA) | The agent described in these docs. |
| Experience Modernization Console | The web interface where you use EMA, at `aemcoder.adobe.io`. |
| Console workspace | Your project's hosted working copy in the console, where the agent imports content and changes code before you upload or push them. Labels such as **Checkout to workspace** and **Your workspace is paused** refer to it. It is unrelated to Experience Workspace. |
| Edge Delivery Services (EDS) | AEM's website delivery service. The architecture was originally developed as Project Helix, later code-named Franklin, and older articles use those names. The `hlx` in hostnames such as `admin.hlx.page`, the EDS admin API, comes from Helix. |
| `*.aem.page`, `*.aem.live` | A site's EDS preview and live URLs. Older projects and documentation may show the earlier domains, `hlx.page` and `hlx.live`. |
| AEM Sidekick | The browser extension that authors use to preview and publish EDS pages. |
| AEM Code Sync | The GitHub app that lets EDS fetch your code to serve it. |
| AEM Code Connector | The GitHub app that lets the console push changes and open pull requests in your repository. |
| Experience Workspace | The visual authoring UI for document-based EDS content, at `da.live`. It was formerly called Document Authoring (DA), and some console labels still use that name. See [Document-Based Persistence](#document-based). |
| Universal Editor | Adobe's visual editor for content stored in AEM. EDS projects with AEM authoring use it. |
| AEM authoring, JCR persistence | EDS with content stored in AEM's Java Content Repository (JCR) on an AEM as a Cloud Service author instance and edited in the Universal Editor. Previously called Crosswalk. |
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

With document-based persistence, content is stored as documents in the EDS document-based content repository. "Document-based" describes storage only, not the authoring experience. Authors edit pages visually in [Experience Workspace,](https://www.aem.live/docs/ew/about) the visual authoring UI for EDS. Experience Workspace also offers an AI assistant, collaboration, and AEM Assets integration. It is off by default and is turned on per site or organization in the project's configuration. When you transfer an Auto mode site to a document-based destination with [**Make it yours**](getting-started.md#make-it-yours), the transfer turns it on for that site.

"Document-based authoring" has meant different things over time, so check when a page or article was written:

* When Adobe introduced EDS in 2023, it meant writing pages in Google Docs or Microsoft Word, stored on Google Drive or SharePoint. These remain supported EDS content sources.
* Document Authoring (DA) is Adobe's own document editor and content repository, at `da.live`.
* Experience Workspace is DA's new name. It adds a visual canvas editor, and the content stays in the same repository.

EMA uploads and transfers document-based content to Experience Workspace at `da.live`.

>[!NOTE]
>
>The rename from Document Authoring to Experience Workspace is an upgrade, not a content migration: existing DA content stays where it is. Some console labels and screens still say **Document Authoring** or **DA**. In these docs, they refer to Experience Workspace and its repository.

### AEM Authoring with JCR Persistence {#jcr-persistence}

With AEM authoring, content is stored in AEM's Java Content Repository (JCR), on the AEM as a Cloud Service author stack. This is EDS running on top of the JCR stack, a setup previously called Crosswalk. Authors edit pages with the [Universal Editor,](/help/implementing/universal-editor/introduction.md) Adobe's visual editor for content in AEM, and EDS still delivers the pages. The pages are not rendered by HTL and Java as in traditional AEM publishing. Template repositories for this setup, such as `aem-block-collection-xwalk`, still carry `xwalk` in their names.

>[!NOTE]
>
>In these docs, *AEM authoring* names this persistence option. The *AEM author instance* is the AEM as a Cloud Service environment where that content is stored and edited.

### Adobe's Recommendation {#recommendation}

For any new EDS implementation, Adobe strongly recommends document-based persistence with Experience Workspace over AEM authoring with the Universal Editor. This includes large websites with thousands of pages.

Document-based authoring used to mean editing in Microsoft Word, Google Docs, or a document-style editor. That limited visual page editing, so teams that needed it often chose AEM authoring. Experience Workspace now gives document-based content a visual editor, so there is little reason left for a brand to avoid it.

AEM authoring with JCR persistence remains fully supported. Choose it when a specific requirement depends on content staying in the AEM repository. For headless content, delivered through APIs rather than as EDS web pages, the Universal Editor remains the recommended editor.

## How EMA Migrates at Scale {#migration-at-scale}

EMA does not send every page through the AI model. Interpreting each page separately would not scale to thousands of pages, and the model could treat similar pages slightly differently each time. Instead, the AI works out the mapping on one representative page per template, and EMA turns that mapping into code that runs on the template's other pages:

1. **Group pages into templates.** The [site catalog](site-catalog.md) groups the source site's pages into templates, which are pages that share a layout. If you migrate pages without a catalog, each page that you name starts a template of its own.
1. **Migrate a representative page.** For each template, EMA first migrates one representative page: a real page of the source site that shows the template's typical layout and, ideally, most of its blocks and variations. The site catalog proposes one for each template. If another page of the template shows more of its blocks, choose that page instead; blocks that the representative page lacks are only added later, when an imported page needs them. The AI model analyzes the representative page, maps its content to default content and blocks, and creates the blocks that it needs or reuses existing ones. This page is the worked example from which EMA builds the rest of the template.
1. **Generate an import script.** EMA writes an import script for the template. Its parsers extract each block's content from the source HTML, and its transformers clean up the page as a whole. They are JavaScript files in the project's `tools/importer/` folder, so they are versioned in Git with the rest of your code.
1. **Refine the pattern, not the page.** When you ask for a correction, EMA changes the block, parser, or transformer that produced the result instead of editing one page's output. The correction then applies to every page of the template, and later templates reuse the blocks that already exist.
1. **Import the remaining pages in bulk.** The bulk import runs the import script on the template's other pages without the AI model interpreting each one. EMA then compares the imported pages with their source pages, fixes the parsers or transformers behind pages that differ too much, and imports those pages again.

Corrections accumulate in the blocks and import scripts, so each one also improves the pages that you import next. Validate a few pages of each template before you import all of them. See the [bulk import workflow](site-catalog.md#bulk-import).

You can also change the structure that EMA builds on. In the [site planning UI](site-catalog.md#planning-actions), or by asking EMA, you can move pages to another template, create a template from a subset of pages, make one block a variant of another, or give a variant its own block. These changes update the catalog, and EMA follows them the next time it generates blocks or imports pages. They don't change pages that you already imported. To consolidate the design itself, for example from a new style guide or Figma designs, see [Restyle Sites](restyling.md). To consolidate block code, see [Refactor Without Changing the Outcome](block-development.md#refactor).

>[!NOTE]
>
>A template in EMA is a group of source pages with the same layout, which EMA uses to plan and import them. It is not the same as the `template` metadata of an EDS page, which adds a class to the page's `body` element so that the project's code can style or decorate those pages differently.

You can align the two. When the pages of an EMA template should look or behave differently from other pages on the new site, ask EMA to write matching `template` metadata into those pages and to style them in the project's code. For example:

> For the article template, set the page metadata `template` to `article` in the import script, and give article pages a narrower main column.

Because the import script sets the metadata, every article page that you import later gets it too.

## What EMA Remembers {#memory}

EMA has no memory of its own that carries over between conversations. What it knows about your project comes from three places:

* **Its built-in skills,** the workflows that Adobe provides and updates with each release.
* **The current conversation.** The console keeps your project's conversation so that you can continue it later. When a conversation gets long, the agent summarizes earlier messages to make room, and details can be lost. **Clear chat** starts a new conversation without the earlier history.
* **The files in the console workspace:** the checked-out Git repository with your code, the working copy of imported content, and temporary files from the migration.

To make EMA remember a decision or convention, write it in a file in your Git repository. EMA currently uses Claude models, which load a file named `CLAUDE.md` from the repository root at the start of every conversation. In projects created from the AEM boilerplate, `CLAUDE.md` contains one line, `see @AGENTS.md`, which loads `AGENTS.md` as well. Your project instructions belong in `AGENTS.md`, and EMA reads other project files when `AGENTS.md` or your request points to them. The model is an implementation detail that can change, so don't write instructions that depend on it. See [Project Instructions and Memory](project-instructions.md).

## Migration and Site Creation Capabilities {#creation-migration}

Skills are the agent's built-in workflows for specific kinds of tasks. You don't need to name them: describe the task, and EMA chooses the skill. The following capabilities are always available:

| Capability | What EMA does | Learn more |
|---|---|---|
| Site catalog and planning | Discovers the source site's pages, groups them into templates, and identifies their blocks and variants, with screenshots and a report. You review and adjust the result in the site planning UI. | [Site Catalog Skill](site-catalog.md) |
| Page migration | Imports a source page, maps its content to [default content and blocks](#eds-basics), and creates new blocks or reuses existing ones. | [Migrate a site or page](prompting-guide.md#migrate-a-site) |
| Design migration | Extracts the design system, such as colors, fonts, and spacing, into CSS custom properties and global styles, and styles each block to match the source. | [Design migration](prompting-guide.md#design-migration) |
| Header, navigation, and footer | Rebuilds the parts that every page shares as EDS blocks and content. | [Navigation setup](prompting-guide.md#navigation-setup) |
| Import scripts and bulk import | Writes an import script for each template and runs it on the template's other pages. It then compares the imported pages with their source pages and fixes the script for pages that differ. | [Bulk import](prompting-guide.md#bulk-import) |
| Visual critique | Compares a migrated block, page, or the whole site with the source and fixes content, structure, and styling differences. | [Block critique](prompting-guide.md#block-critique) |
| Protected source pages | Reads source pages that need a custom request header, HTTP Basic authentication, or bearer authentication. | [Protected Site Authentication](console.md#protected-site-authentication) |
| AEM authoring models | Creates the block models that the Universal Editor uses, for projects that store content in AEM. | [AEM authoring projects](getting-started-aem-authoring.md) |
| Console tour | Explains the console's views and actions. Ask "Give me a tour of the console." | [Modernization Console](console.md) |

Optional add-ons extend these capabilities when a project needs them: Figma import, Stardust guided redesign, project documentation, forms migration, commerce pages, block library setup, EDS troubleshooting, modern web guidance, and design craft. EMA offers to turn an add-on on when your request needs it, and you can save the choice in the repository so that it applies to the whole team. See [Optional Capabilities](console.md#optional-capabilities).

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
* You perform day-to-day development tasks, check the result in the console's preview, upload content to your authoring destination, and check it again on the EDS preview site.
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

To perform your request, EMA can send the following to the large language model (LLM) that it uses, currently a Claude model:

* Your prompts and instructions.
* Source page URLs, markup, and content, or exported CMS content.
* Repository code and configuration, such as blocks, styles, and site configuration.
* Design and brand references, such as Figma designs and screenshots.
* Generated content and code under review.

Adobe does not use your conversations or other customer data to train or fine-tune AI models.

### Control over Changes {#security-control}

* The agent works in your workspace. You review its changes and the preview in the console.
* Without agent permissions, code reaches your Git repository and content reaches AEM only when you use the console's synchronization actions. Optional plan mode lets you approve a plan before the agent starts.
* Treat source pages and design files as untrusted input. They can contain text that attempts to steer the agent. Review the changes before you push, preview, or publish them. Branch protection and pull request reviews in your repository still apply.

### Where Your Work Is Stored {#security-storage}

* Code that you push is stored in your Git repository, and content that you sync is stored in your AEM content repository. Their own retention and version history policies apply.

For processing locations, data retention, and compliance information, contact your Adobe account team or see the [Adobe Trust Center.](https://www.adobe.com/trust.html)

## Limitations {#limitations}

Use only websites and designs that you are authorized to migrate. The selected workflow must be able to reach and read the source. If the site uses bot protection, arrange access with its administrator. See [source sites with bot protection](getting-started.md#bot-protection).

* Pages that require sign-in or a secret header can be migrated when the source accepts a custom request header, HTTP Basic authentication, or bearer authentication. Configure the credentials in the console's [Protected Site Authentication](console.md#protected-site-authentication) settings, or in the authentication fields of Auto mode. Do not put secrets in chat. This is not intended for personally identifiable information (PII) or real end-user data.
* Sources reachable only through a VPN or blocked by a firewall remain unsupported, even with valid credentials. So do sources that require another sign-in flow, such as an interactive single sign-on (SSO) form. Ask the site administrator for an internet-reachable staging or origin host that accepts a supported method.
* Client-rendered content can be captured when available at the page URL. Content present in the DOM but hidden by CSS can also be extracted. Content requiring additional interactions needs representative checks and may need a different extraction approach.
* EMA targets EDS, including EDS with [JCR-backed AEM authoring.](#jcr-persistence) It does not convert a project to HTL-based AEM publishing or an API-only/SPA delivery stack.
* Faithful design, accessibility, performance, and functional behavior require validation. A visual similarity score is not a production acceptance criterion.
* Integrations, custom business logic, analytics, experimentation, and source-system features such as inheritance or content fragments need an explicit implementation and migration decision. Do not assume automated page import recreates them.

Auto mode is in early access and needs its own [access request](getting-started.md#brand-trial). Which [optional capabilities](console.md#optional-capabilities) are offered can depend on your account and project. Check the controls and limits shown for your account. [AOE service scope](aoe-delivery.md#scope) is agreed separately from product capabilities.

## Next Steps {#next-steps}

Choose a task above, then use [Getting Started](getting-started.md) for shared console setup. For an existing EDS project, connect its repository and start with the relevant development or restyling task; a new migration is not required.

To learn what changed in recent versions of the console, see the [Experience Modernization Agent release notes.](/help/release-notes/modernization-agent/current.md)
