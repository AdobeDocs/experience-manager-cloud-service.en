---
title: Evaluate and Approve the Experience Modernization Agent
description: What a technical decision-maker needs to approve the Experience Modernization Agent for Edge Delivery Services projects, including team impact, the Adobe team behind the agent, systems and data, security and review, Figma, and remaining project work.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
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

# Evaluate and Approve the Experience Modernization Agent {#evaluate}

This page is for the person who approves the Experience Modernization Agent for a team that builds or migrates Adobe Experience Manager sites on Edge Delivery Services: an architect, technical lead, or platform owner who may never use the agent personally. It explains what changes for your team, the three ways to run a migration, how Adobe's team works with yours, which systems and data the agent touches, how changes are controlled and traced, and what remains project work.

For what Edge Delivery Services is and how a project fits together, see [Understand Your Project](overview.md#project-foundations). A result on your own pages tells you more than any description, so ask a team member to [start with Auto mode](getting-started.md#brand-trial) or to [import a page step by step](getting-started.md#guided-import) while you read.

## What Changes for Your Team {#team-impact}

Without the agent, a migration to Edge Delivery Services starts with weeks of developer work before anyone can judge the result: listing the source pages, grouping them by layout, mapping their content to blocks, writing block code and styles, and writing import scripts. The agent does that repetitive work with your team, in a hosted environment with nothing to install.

* **Your team decides and reviews; the agent produces.** People set the scope, the content model, the target design, and the integrations, and they accept the result. The agent writes the code, imports the content, and compares the result with the source.
* **More people contribute directly.** Designers, content specialists, and marketers who know some HTML and the basics of Git make changes by describing them in plain language. Developers keep control of what reaches production by reviewing those changes as pull requests. See [Broader Contribution, Same Production Control](overview.md#production-control).
* **Effort grows with layouts, not pages.** A correction changes a reusable block or import script rather than one page, so it applies to every page of the same layout. A site of 5,000 pages that share 12 layouts is mostly the work of 12 templates. See [How the Agent Migrates at Scale](production-migration.md#migration-at-scale), and to size the work from the first templates, [Estimate Before You Commit](production-migration.md#estimate).
* **The result is a standard project.** The code is plain HTML, CSS, and JavaScript in your Git repository, following the conventions of the AEM boilerplate. The site doesn't depend on the agent at run time, and developers can continue in their own editor or with other AI tools.
* **Project knowledge stays in the repository.** The conventions that your team agrees on live in `AGENTS.md` and related files, which the agent and new team members both follow. See [Project Instructions and Memory](project-instructions.md).

### What the Agent Does and What Your Team Does {#responsibilities}

| Area | What the agent does | What your team does |
|---|---|---|
| Inventory and scope | Discovers pages from the sitemap and links, groups them into templates, and reports blocks and locales. See [Site Catalog](site-catalog.md). | Reconciles the result with your own inventory, and decides what to migrate, redirect, or retire. |
| Content model | Maps each template's content to sections, default content, and blocks. | Checks that authors can edit the result easily, and agrees the conventions. See [David's Model](https://www.aem.live/docs/davidsmodel). |
| Design | Extracts colors, fonts, and spacing into CSS custom properties, and styles blocks to match the source or a new design, including one in Figma. | Approves the target design, and checks responsive behavior and accessibility. |
| Content import | Writes an import script for each template, imports the pages in bulk, and compares them with their source pages. | Validates sample pages, reviews the import scripts as code because they decide the structure of every imported page, and accepts the imported pages. |
| Images and documents | Uploads the images that a page uses together with the page. Leaves Dynamic Media images on Dynamic Media. | Checks alt text, image quality, and linked documents such as PDFs. See [Images and Documents](production-migration.md#assets). |
| URLs and search metadata | Carries over page titles, descriptions, and social images. Derives each page's path from its source URL. | Decides the URL policy, and has the redirects, sitemaps, and language alternates built and checked. See [URLs, Redirects, and Search Metadata](production-migration.md#urls-seo). |
| Integrations | Writes the blocks and code that call your APIs and services, for any system with a documented API, as a general-purpose coding agent does. Optional add-ons migrate forms and commerce pages. | Decides how each integration works, provides API access and documentation, and accepts the result. See [Connect Services and Applications](block-development.md#integrations). |
| Review and release | Prepares code changes as pull requests that list preview URLs. | Developers review and merge, and authors preview and publish. The project lead agrees the criteria for signing off the result before the migration starts, then signs it off and runs cutover. See [Check and Sign Off](production-migration.md#acceptance). |
| After go-live | Restyles the site, adds and refactors blocks, debugs, and documents the project. | Owns the site, its code, its content, and its operations. |

For who leads each phase of a migration, see [Phases and Roles](production-migration.md#phases). Several people can work on one project, each in their own console workspace; see [Work as a Team](production-migration.md#collaboration).

## Choose How the Migration Runs {#approaches}

The same agent can run a migration in three ways. They differ in who drives the agent and who answers for the result. All three produce a standard Edge Delivery Services project, with code in a Git repository and content that authors edit, so you can move from one to the next: transfer an Auto mode result to your own site and continue in the console, or continue with the agent yourself after an engagement with Agentic Outcome Engineers.

| Approach | Choose it when | What your team does |
|---|---|---|
| [Auto mode](getting-started.md#brand-trial) | You want a first result on a few of your own pages with little effort, for example to judge the approach or to show it to stakeholders. | Gives Auto mode the site's URL or a list of pages, and reviews the result when its email arrives. Auto mode applies default choices and doesn't ask for input during the run. To take the result to production, a developer transfers it to a site that you own with [**Make it yours**](getting-started.md#make-it-yours). |
| [The console, driven by your developers](getting-started.md#repo-start) | Your developers want to set the implementation choices themselves: block design, content model, and integrations. | Prompts the agent step by step, checks each page in the preview, and reviews the agent's code changes before merging them. See [Migrate a Production Site](production-migration.md), and for what enforces review, [Control over Changes](#security-control). |
| [Agentic Outcome Engineers](aoe-delivery.md) | You want Adobe engineers to operate the agent with your team, against a scope, outcome, and timeline agreed up front. | Agrees the engagement with your Adobe account team, reviews deliverables at the agreed checkpoints, and takes over the site at the hand-over. |

## The Team Behind the Agent {#adobe-team}

When you choose the agent, you also choose the team that builds it and the direction that it takes. How people find information on the web is changing: more of them ask an AI assistant, which answers from what it reads on the brand's own site. And an agent can change a site's content, design, and code together, so a change that once needed a project can take hours. The team's mission is to help you move to Edge Delivery Services, get the most out of Experience Manager, and use agentic development tools to build sites that stay relevant as these shifts continue. Its work with you doesn't end at the migration, and the agent keeps changing; the [release notes](/help/release-notes/modernization-agent/current.md) list each change.

When changes are cheap, the hard part is deciding what to change, keeping it governed, and giving the agent the right brand, design, and business context. That knowledge sits with your teams and systems. Adobe's team helps you connect it to the platform:

* **Engineers who can run the migration with you.** For a complex migration, Adobe's Agentic Outcome Engineers can operate the agent with your team and hand the site over to it. See [Choose How the Migration Runs](#approaches).
* **Current as the product changes.** The console's **What's new** notice lists the highlights of each release. To apply a change to your own site, review your architecture, or discuss a need that the agent doesn't meet yet, ask your Adobe customer success manager or account team for a meeting with subject-matter experts and the product team.
* **Your experience shapes the product.** The product team exchanges expertise with customers and partners, and works with some of them on new capabilities. What you report feeds into what the team fixes and builds next.

To reach the team from the console, use **Request support**, or **Get help** on the Auto mode pages. Your message goes straight to the team that builds the agent, which looks into it and follows up by email. See [Request Support](console.md#request-support) and, for what a request shares, [Support Requests](#security-support).

Adobe's team works the same way with implementation partners, so that with your partner the site keeps improving after the migration.

## Systems and Data Flow {#systems}

The agent works in a hosted environment and reaches your systems only through connections that people set up and permissions that they grant.

| System | Role | How the agent reaches it | What controls access |
|---|---|---|---|
| Experience Modernization Console | The hosted environment at `aemcoder.adobe.io` where people work with the agent. | Each user signs in with an Adobe ID that belongs to your company's Adobe organization, and works in a separate environment. | Adobe enables access through your account team. Signing in doesn't establish your organization's entitlement. See [Access and AI Credit Usage](getting-started.md#access). |
| AI model | Interprets requests, source pages, and designs, and writes code and content. Currently a Claude model. | The console sends it what a request needs. See [What the AI Model Processes](#security-model-data). | Adobe. Customer data isn't used to train models. |
| Git repository | The system of record for the site's code, on GitHub or on another Git host connected through Cloud Manager. | Each user connects their own Git account, which needs write access to the repository. On GitHub, the AEM Code Connector app lets the console push. | Your Git provider's permissions and branch protection. |
| Content destination | Stores the pages and images: Experience Workspace, or the author instance with Experience Manager authoring. Decide which before the migration; see [Where Content Is Stored and How Authors Edit It](overview.md#content-storage). | A person uploads content, or the agent does when that person has turned on the permission and asks for it. | Write access to the content, and the site's publish role. |
| Source site | The content and design to migrate. | The agent loads pages in a browser as a visitor would, with credentials for protected pages where configured. | The site's owner, who authorizes the migration and controls access to the site. |
| Figma (optional) | The target design, or the design of new pages. | Each user stores their own Figma personal access token in the console. | Figma's file permissions and the token owner's access. See [Figma and Design Systems](#figma). |
| Edge Delivery Services | Delivers the site: the preview site on `aem.page` and the live site on `aem.live`. | Fetches code from the repository and content from the content destination. | The site's configuration, and its author and publish roles. |

## Security and Data Handling {#security}

The console lets the agent work on your site without giving it the credentials that you configure, and you decide when changes reach your Git repository and your content destination.

### Access and Isolation {#security-access}

* You sign in to the console with your Adobe ID. Every request is authenticated with Adobe Identity Management Services (IMS).
* Each user works in a separate backend environment with its own workspace storage, one in each Adobe organization that they sign in with. The console creates the environment when the user first signs in and pauses it when it's idle.
* The console has no project roles. Anyone with access can ask the agent for any change in their own workspace. Experience Manager and your Git provider continue to enforce their own permissions for any code or content that leaves the workspace.

### Credentials {#security-credentials}

* The AI agent does not receive the credentials that you configure in the console. Tokens for GitHub, Cloud Manager Git repositories, Experience Workspace, Figma, and protected source sites are held outside the agent's environment. A separate component adds each credential only to requests for the service it belongs to. The same applies to the credential used to call the AI model.
* Credentials belong to the user who configures them, not to the project. Each team member connects their own Git account and stores their own Figma token.
* [Agent permissions](console.md#settings-page) are off until you turn them on. Turning one on lets the agent act with that access, for example to push to your repository, without seeing the credential. By default, a permission uses the user's own sign-in. To narrow what the agent can reach, enter a token for it instead: a fine-grained personal access token scoped to the repositories it needs, or the token of an Adobe service account.
* Other services that the agent calls while it works, such as a test API, get their credential the same way, from an entry in **Protected site authentication** for the service's hostname. See [Credentials for Other Services](console.md#other-services).
* Store credentials only in the console's settings, never in prompts, chat, source content, or project files: the agent reads these and can send them to the AI model. Make this part of onboarding, because people who are new to coding agents may paste a password or key into the chat to get a task done. Ask everyone who uses the console to read [Keep Secrets Out of the Chat](prompting-guide.md#secrets) first, and tell them what your organization's policy allows them to share with AI tools.

### What the AI Model Processes {#security-model-data}

To perform your request, the agent can send the following to the large language model (LLM) that it uses, currently a Claude model:

* Your prompts and instructions.
* Source page URLs, markup, and content, or exported CMS content.
* Repository code and configuration, such as blocks, styles, and site configuration.
* Design and brand references, such as Figma designs and screenshots.
* Generated content and code under review.

Adobe does not use your conversations or other customer data to train or fine-tune AI models.

### Control over Changes {#security-control}

The agent works in your console workspace, where you review its changes and the preview. Work reaches your site in separate steps, and each step has its own control:

| Step | Who can do it | What controls it |
|---|---|---|
| Push code to your Git repository | You, with **Sync** > **Push** > **Code**. The agent, only if you turn on **Allow LLM to use my git credentials** for GitHub, or the Adobe credentials permission for repositories connected through Cloud Manager. | Your repository's permissions and branch protection. The console doesn't check branch rules itself. |
| Upload content | You, with **Upload content** or **Sync** > **Push** > **Content**. For Experience Workspace, also the agent, with the Adobe credentials permission and at your request. | Write access to the site's content in Experience Workspace, or on the author instance. |
| Preview and publish | You, from the upload results dialog, Experience Workspace, or the AEM Sidekick. The agent, with the Adobe credentials permission and at your request. | The site's author and publish roles on Edge Delivery Services, where [authentication for authors](https://www.aem.live/docs/authentication-setup-authoring) is set up. |

* The console's own checks are safeguards, not approval gates. Optional plan mode lets you approve a plan before the agent starts. The console also stops the agent from uploading, previewing, or publishing unless your current message asks for it or you agree when the agent asks, but it can't detect every way of making such a request. Neither check stops a person with access from pushing or publishing.
* With a Git permission, the agent can push to any branch that your credentials can write to, including `main`. A push to `main` changes the live site's code.
* To require review, enforce it where the change lands. Protect `main` with [branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) that requires a reviewed pull request, push with **Create new PR**, and limit who can publish with the site's [publish role](https://www.aem.live/docs/authentication-setup-authoring). The pull request lists the changed files and the preview URLs of affected pages, so that a developer checks the result before merging. Set these controls up before more people contribute, and turn on agent permissions only when a task needs them. See [Broader Contribution, Same Production Control](overview.md#production-control).
* Treat source pages and design files as untrusted input. They can contain text that attempts to steer the agent. Review the changes before you push, preview, or publish them.

#### Content Push Permissions {#content-push-permissions}

When you upload content using your Adobe sign-in, the destination enforces your account's permissions. For document-based content edited in Experience Workspace, you need write access to the destination content. For Experience Manager authoring, you need permission to write pages and assets at the selected paths on the author instance. Signing in to the console doesn't grant those rights.

When you turn on the agent's Adobe credentials permission, its content pushes to the document-based content repository use your account's access. Asking the agent to upload doesn't bypass the destination's permissions. For Experience Manager authoring, upload the content yourself through the console; direct agent uploads aren't supported.

If a document-based upload uses a configured fallback account because your sign-in is unavailable or authentication fails, the destination enforces that account's permissions instead. The same applies when you explicitly configure a service account for the agent. Confirm which account is used before relying on your personal permissions to limit changes.

### Trace What the Agent Did {#audit-trail}

The console keeps no separate audit log, but the agent's work doesn't go unrecorded. What the agent produces reaches your site only through your Git repository or through Experience Manager, and both keep a history:

* **Code is the primary record.** Your Git history records each change to blocks, styles, and import scripts, and the import scripts define the structure of every imported page.
* **Content changes are recorded with the content.** Experience Workspace keeps a version history of each document, and the author instance keeps its own page versions.
* **The conversation shows what was asked.** **Download chat** saves the conversation as a Markdown file. Download it before you select **Clear chat**, which removes the messages and can't be undone. See [Chat Panel](console.md#chat-panel).

The record is easiest to follow when each request to the agent ends in its own commit, pushed to a working branch rather than to `main`, and, where pages changed, its own content upload, which the agent offers and a person approves. Ask for this in the project's `AGENTS.md`; see [Leave a Record of Each Request](project-instructions.md#trace). Reviewers then read what the agent changed, request by request, in tools that they already use.

### Where Your Work Is Stored {#security-storage}

* Code that you push is stored in your Git repository, and content that you upload is stored in Experience Workspace or on your author instance. Their own retention and version history policies apply.
* Work that you haven't pushed or uploaded exists only in your console workspace, along with the chat history and the transcripts of the agent's sessions. **Clear chat** removes the messages from the chat panel but keeps the transcripts. To delete the open project's work in the console workspace, including the transcripts, use [**Reset workspace**](console.md#settings-page).

For processing locations, data retention, and compliance information, contact your Adobe account team or see the [Adobe Trust Center](https://www.adobe.com/trust.html).

### Health Data and HIPAA {#security-hipaa}

The Experience Modernization Agent is a developer tool for migrating and building sites. Your site's visitors never reach it: Edge Delivery Services serves the published site, and visitors' requests don't pass through the console or the agent. Never give the agent real end-user data, such as patient records or your users' credentials, and don't migrate pages that display such data. Whatever you give the agent can reach the AI model; see [What the AI Model Processes](#security-model-data). For which Experience Manager services can process protected health information (PHI) under the Health Insurance Portability and Accountability Act (HIPAA), see [HIPAA readiness for Adobe Experience Manager as a Cloud Service](/help/compliance/hipaa/hipaa-readiness.md).

### Support Requests {#security-support}

A support request goes to the Adobe team that builds the agent. With the topic and description that the sender writes, it shares:

* The sender's name, email address, and Adobe user and organization IDs.
* The session ID, project name, and preview URL, and the Git host for GitHub Enterprise.
* Any recent prompts that the sender chooses to attach. None is attached by default.

These details let the team find the session's conversation and logs. Before the sender's console workspace is set up, a request shares only the name, email address, and organization. On the Auto mode pages, **Get help** shares only the sender's name and email address with their message. Ask users not to include passwords, tokens, or personal data in the description. See [Request Support](console.md#request-support).

## Figma and Design Systems {#figma}

Figma can be the source of a new design. With the Figma import add-on, the agent reads the selected component or frame through Figma's API, using a Model Context Protocol (MCP) server, the way a developer reads a design handoff. It writes the design's variables and styles, such as colors, typography, and spacing, as CSS custom properties in the project's global styles. These properties are the site's design tokens. They live in the code, not in a separate token export, so designers and developers review them like any other change. For how designers work from Figma with the agent, see [Work from a Figma Design](visual-changes.md#figma).

What to approve:

* **Access:** Each person who uses Figma with the agent creates a Figma personal access token with read-only scopes and stores it in the console's [settings](console.md#settings-page). Figma issues and governs this access token, which has nothing to do with design tokens. There is no organization-wide Figma connection, and a personal access token can't be limited to specific files: it reads every file that its owner can open.
* **Seats and rate limits:** Figma limits how often a token can read files, based on the token owner's seat and the plan that owns the file. With a View or Collab seat, a token can read files through Figma's API only a few times a month, so people who use Figma with the agent need a Dev or Full seat. See Figma's [rate limits](https://developers.figma.com/docs/rest-api/rate-limits/).
* **Data:** For the selected frame or component, the agent sends its structure, a screenshot, its variables, and its text to the AI model. See [What the AI Model Processes](#security-model-data).

## What Remains Project Work {#project-work}

The agent is a development agent: what can be built on Edge Delivery Services can be built with it. A migration copies what the source pages show, though, not the systems behind them. The agent rebuilds the site: its pages, blocks, styles, and the code that calls your services. Approval and publishing workflows, the back-end systems behind integrations, and how your teams work on the new site remain your organization's work. These needs require a decision from your team before the agent can build them:

| Need | What import gives you | What to decide, then build with the agent |
|---|---|---|
| Shared content, such as a banner or disclaimer on many pages | A copy on each page | Which content to keep once and include as a fragment, and the block that includes it. |
| Several languages or markets | Pages at their source paths, with their locale folders | The URL structure, the language alternates in the sitemap, and how translation and inheritance between markets work for your authors. See [Translation and Localization](https://www.aem.live/docs/translation-and-localization). |
| Personalization, search, and account features | Each page's output at the time of import | The service that provides the logic, and the blocks that call it. |
| Forms | The form's fields, with the forms add-on for organizations that license Experience Manager Forms | The system that receives submissions, such as your marketing automation platform or customer relationship management (CRM) system, and the workflows that follow. See [Form Submissions](block-development.md#form-submissions). |
| Commerce | Product detail and listing pages that load their product data from the catalog, with the commerce pages add-on for storefronts on Adobe Commerce | The storefront setup and its Adobe Commerce license, or, for another commerce platform, the blocks that call its API. See [Commerce Pages](block-development.md#commerce-pages). |
| Analytics, tag management, and consent | With Auto mode's **Include integrations**, the supported settings, switched off until you turn them on | Which tags load, and when, so that the pages stay fast. |
| Redirects, sitemaps, and canonical URLs | Page titles, descriptions, and social images | The URL policy and its configuration. See [URLs, Redirects, and Search Metadata](production-migration.md#urls-seo). |

For source access, interactive content, and other boundaries of the import, see [Limitations](overview.md#limitations).

## Next Steps {#next-steps}

* See a result on your own content: [Start with Auto mode](getting-started.md#brand-trial).
* Plan a migration: [Migrate a Production Site](production-migration.md).
* Talk to the people who build the agent: see [The Team Behind the Agent](#adobe-team).
* Read short answers to common questions: [Experience Modernization Agent FAQ](faq.md).
