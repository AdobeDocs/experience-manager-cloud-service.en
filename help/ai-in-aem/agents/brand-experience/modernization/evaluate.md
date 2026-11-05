---
title: Evaluate and Approve the Experience Modernization Agent
description: What a technical decision-maker needs to approve the Experience Modernization Agent for Edge Delivery Services projects, including team impact, the Adobe team behind the agent, systems and data, security, review, scale, Figma, and remaining project work.
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

This page is for the person who approves how a team builds on, or migrates to, Adobe Experience Manager Edge Delivery Services with the Experience Modernization Agent: an architect, technical lead, or platform owner who may never use the agent personally. It explains what changes for your team, how Adobe's team works with yours, which systems and data the agent touches, how changes are reviewed, how the work scales, and what remains project work.

For what Edge Delivery Services is and how a project fits together, see [Understand Your Project](overview.md#project-foundations). A result on your own pages tells you more than any description, so ask a team member to [start with Auto mode](getting-started.md#brand-trial) or to [import a page step by step](getting-started.md#guided-import) while you read.

## What Changes for Your Team {#team-impact}

Without the agent, a migration to Edge Delivery Services starts with weeks of developer work before anyone can judge the result: listing the source pages, grouping them by layout, mapping their content to blocks, writing block code and styles, and writing import scripts. The agent does that repetitive work with your team, in a hosted environment with nothing to install.

* **Your team decides and reviews; the agent produces.** People set the scope, the content model, the target design, and the integrations, and they accept the result. The agent writes the code, imports the content, and compares the result with the source.
* **More people contribute directly.** Designers, content specialists, and marketers who know some HTML and the basics of Git make changes by describing them in plain language. Developers keep control of what reaches production by reviewing those changes as pull requests. See [Broader Contribution, Same Production Control](overview.md#production-control).
* **Effort grows with layouts, not pages.** A correction changes a reusable block or import script rather than one page, so it applies to every page of the same layout. See [How the Migration Scales](#scale).
* **The result is a standard project.** The code is plain HTML, CSS, and JavaScript in your Git repository, following the conventions of the AEM boilerplate. The site doesn't depend on the agent at run time, and developers can continue in their own editor or with other AI tools.
* **Project knowledge stays in the repository.** The conventions that your team agrees on live in `AGENTS.md` and related files, which the agent and new team members both follow. See [Project Instructions and Memory](project-instructions.md).

### What the Agent Does and What Your Team Does {#responsibilities}

| Area | What the agent does | What your team does |
|---|---|---|
| Inventory and scope | Discovers pages from the sitemap and links, groups them into templates, and reports blocks and locales. See [Site Catalog](site-catalog.md). | Reconciles the result with your own inventory, and decides what to migrate, redirect, or retire. |
| Content model | Maps each template's content to sections, default content, and blocks. | Checks that authors can edit the result easily, and agrees the conventions. See [David's Model](https://www.aem.live/docs/davidsmodel). |
| Design | Extracts colors, fonts, and spacing into CSS custom properties, and styles blocks to match the source or a new design, including one in Figma. | Approves the target design, and checks responsive behavior and accessibility. |
| Content import | Writes an import script for each template, imports the pages in bulk, and compares them with their source pages. | Validates representative pages, reviews the import scripts as code, and accepts the imported pages. |
| Images and documents | Uploads the images that a page uses together with the page. Leaves Dynamic Media images on Dynamic Media. | Checks alt text, image quality, and linked documents such as PDFs. See [Images and Documents](production-migration.md#assets). |
| URLs and search metadata | Carries over page titles, descriptions, and social images. Derives each page's path from its source URL. | Decides the URL policy, and has the redirects, sitemaps, and language alternates built and checked. See [URLs, Redirects, and Search Metadata](production-migration.md#urls-seo). |
| Integrations | Writes the blocks and code that call your APIs and services, for any system with a documented API, as a general-purpose coding agent does. Optional add-ons migrate forms and commerce pages. | Decides how each integration works, provides API access and documentation, and accepts the result. See [Connect Services and Applications](block-development.md#integrations). |
| Review and release | Prepares code changes as pull requests that list preview URLs. | Developers review and merge, authors preview and publish, and the project lead runs acceptance and cutover. |
| After go-live | Restyles the site, adds and refactors blocks, debugs, and documents the project. | Owns the site, its code, its content, and its operations. |

## The Team Behind the Agent {#adobe-team}

How people find information on the web is changing. More of them ask an AI assistant instead of browsing, and the assistant answers from what it reads on the brand's own site. At the same time, an agent can change a site's content, design, and code together, so a change that once needed a project can now take hours. Edge Delivery Services and the Experience Modernization Agent are built for both shifts, and they keep changing as the shifts continue. The [release notes](/help/release-notes/modernization-agent/current.md) list each change.

When you choose the agent, you also choose the team that builds it and the direction that it takes. That team's mission is to help you move to Edge Delivery Services, get the most out of Experience Manager, and use agentic development tools to build sites that stay relevant as AI changes how people find them. The same team works on how agentic tools can make each web experience better for the people who use it, so its work with you doesn't end at the migration.

When changes are cheap, the hard part is deciding what to change, keeping it governed, and giving the agent the right brand, design, and business context. That knowledge sits with your teams and systems. Adobe's team helps you connect it to the platform:

* **A first result on your own pages.** [Auto mode](getting-started.md#brand-trial) migrates a first set of your pages, so that you judge the approach on your own content. For complex migrations, Adobe engineers can operate the agent with your team. See [AOE Delivery](aoe-delivery.md).
* **Current as the product changes.** The console's **What's new** notice lists the highlights of each release. To apply a change to your own site, review your architecture, or discuss a need that the agent doesn't meet yet, ask your Adobe customer success manager or account team for a meeting with subject-matter experts and the product team.
* **Your experience shapes the product.** The product team exchanges expertise with customers and partners, and works with some of them on new capabilities. What you report feeds into what the team fixes and builds next.

The quickest way to reach the team is from the console itself. When something doesn't work as you expect, use **Request support**, or **Get help** on the Auto mode pages. Your message goes straight to the team that builds the agent, which looks into it and follows up by email. See [Request Support](console.md#request-support) and, for what a request shares, [Support Requests](#security-support).

Adobe's team works the same way with implementation partners. With Adobe and your partner working together, the site keeps improving after the migration instead of ending with it.

## Systems and Data Flow {#systems}

The agent works in a hosted environment and reaches your systems only through connections that people set up and permissions that they grant.

| System | Role | How the agent reaches it | What controls access |
|---|---|---|---|
| Experience Modernization Console | The hosted environment at `aemcoder.adobe.io` where people work with the agent. | Each user signs in with an Adobe ID that belongs to your company's Adobe organization, and works in a separate environment. | Adobe enables access through your account team. |
| AI model | Interprets requests, source pages, and designs, and writes code and content. Currently a Claude model. | The console sends it what a request needs. See [What the AI Model Processes](#security-model-data). | Adobe. Customer data isn't used to train models. |
| Git repository | The system of record for the site's code, on GitHub or on another Git host connected through Cloud Manager. | Each user connects their own Git account, which needs write access to the repository. On GitHub, the AEM Code Connector app lets the console push. | Your Git provider's permissions and branch protection. |
| Content destination | Stores the pages and images: Experience Workspace, or the author instance with Experience Manager authoring. | A person uploads content, or the agent does when that person has turned on the permission and asks for it. | Write access to the content, and the site's publish role. |
| Source site | The content and design to migrate. | The agent loads pages in a browser as a visitor would, with credentials for protected pages where configured. | The site's owner, through authorization, bot protection, and access to protected pages. |
| Figma (optional) | The target design, or the design of new pages. | Each user stores their own Figma personal access token in the console. | Figma's file permissions and the token owner's access. See [Figma and Design Systems](#figma). |
| Edge Delivery Services | Serves the preview and live sites. | Fetches code from the repository and content from the content destination. | The site's configuration, and its author and publish roles. |

## Security and Data Handling {#security}

The console lets the agent work on your site without giving it the credentials that you configure, and you decide when changes reach your Git repository and your content destination.

### Access and Isolation {#security-access}

* You sign in to the console with your Adobe ID. Every request is authenticated with Adobe Identity Management Services (IMS). Your Adobe account team manages your organization's access.
* Each user works in a separate backend environment with its own workspace storage, one in each Adobe organization that they sign in with. The console creates the environment when the user first signs in and pauses it when it's idle. Your workspace is not shared with other users.
* The console has no project roles. Anyone with access can ask the agent for any change in their own workspace. Experience Manager and your Git provider continue to enforce their own permissions for any code or content that leaves the workspace.

### Credentials {#security-credentials}

* The AI agent does not receive the credentials that you configure in the console. Tokens for GitHub, Cloud Manager Git repositories, Experience Workspace, Figma, and protected source sites are held outside the agent's environment. A separate component adds each credential only to requests for the service it belongs to. The same applies to the credential used to call the AI model.
* Credentials belong to the user who configures them, not to the project. Each team member connects their own Git account and stores their own Figma token.
* [Agent permissions](console.md#settings-page) are off until you turn them on. Turning one on lets the agent act with that access, for example to push to your repository, without seeing the credential. By default, a permission uses the user's own sign-in. To narrow what the agent can reach, enter a token for it instead: a fine-grained personal access token scoped to the repositories it needs, or the token of an Adobe service account.
* Other services that the agent calls while it works, such as a test API, get their credential the same way, from an entry in **Protected site authentication** for the service's hostname. See [Credentials for Other Services](console.md#other-services).
* Store credentials only in the console's settings. Do not put secrets in prompts, chat, source content, repository files, or project documentation. The agent reads these, and they can be sent to the AI model.
* Make this part of onboarding. People who are new to coding agents may paste a password or key into the chat to get a task done. Ask everyone who uses the console to read [Keep Secrets Out of the Chat](prompting-guide.md#secrets) first, and tell them what your organization's policy allows them to share with AI tools. The agent is instructed not to use a secret pasted in the chat and to ask for it to be replaced. That doesn't undo the exposure: the secret has already reached the AI model, and it must be revoked or replaced.

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
| Upload content | You, with **Upload content** or **Sync** > **Push** > **Content**. For Experience Workspace, also the agent, but only with the Adobe credentials permission and when your message asks for it or you agree when the agent asks. | Write access to the site's content in Experience Workspace, or on the author instance. |
| Preview and publish | You, from the upload results dialog, Experience Workspace, or the AEM Sidekick. The agent, only with the Adobe credentials permission and when your message asks for it. | The site's author and publish roles on Edge Delivery Services, where [authentication for authors](https://www.aem.live/docs/authentication-setup-authoring) is set up. |

* The console's own checks are safeguards, not approval gates. Optional plan mode lets you approve a plan before the agent starts. The console also stops the agent from uploading, previewing, or publishing unless your current message asks for it or you agree when the agent asks, but it can't detect every way of making such a request. Neither check stops a person with access from pushing or publishing.
* With a Git permission, the agent can push to any branch that your credentials can write to, including `main`. A push to `main` changes the live site's code.
* To require review, enforce it where the change lands. Protect `main` with [branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) that requires a reviewed pull request, push with **Create new PR**, and limit who can publish with the site's [publish role](https://www.aem.live/docs/authentication-setup-authoring). Turn on agent permissions only when a task needs them.
* Treat source pages and design files as untrusted input. They can contain text that attempts to steer the agent. Review the changes before you push, preview, or publish them.

#### Content Push Permissions {#content-push-permissions}

When you upload content using your Adobe sign-in, the destination enforces your account's permissions. For document-based content edited in Experience Workspace, you need write access to the destination content. For Experience Manager authoring, you need permission to write pages and assets at the selected paths on the author instance. Signing in to the console doesn't grant those rights.

When you turn on the agent's Adobe credentials permission, its content pushes to the document-based content repository use your account's access. Asking the agent to upload doesn't bypass the destination's permissions. For Experience Manager authoring, upload the content yourself through the console; direct agent uploads aren't supported.

If a document-based upload uses a configured fallback account because your sign-in is unavailable or authentication fails, the destination enforces that account's permissions instead. The same applies when you explicitly configure a service account for the agent. Confirm which account is used before relying on your personal permissions to limit changes.

### Where Your Work Is Stored {#security-storage}

* Code that you push is stored in your Git repository, and content that you upload is stored in Experience Workspace or on your author instance. Their own retention and version history policies apply.
* Work that you haven't pushed or uploaded exists only in your console workspace. **Reset workspace** in the [settings](console.md#settings-page) deletes it permanently.

For processing locations, data retention, and compliance information, contact your Adobe account team or see the [Adobe Trust Center.](https://www.adobe.com/trust.html)

### Support Requests {#security-support}

A support request goes to the Adobe team that builds the agent. With the topic and description that the sender writes, it shares:

* The sender's name, email address, and Adobe user and organization IDs.
* The session ID, project name, and preview URL, and the Git host for GitHub Enterprise.
* Any recent prompts that the sender chooses to attach. None is attached by default.

Together, these details give the team everything it needs to find the session's conversation and logs and diagnose the problem. On the Auto mode pages, **Get help** shares only the sender's name and email address with their message. Ask users not to include passwords, tokens, or personal data in the description. See [Request Support](console.md#request-support).

## Review and Governance {#governance}

Every change reaches your site through systems that already have review controls. Set them up before more people contribute:

1. **Code:** Protect `main` with branch protection that requires a reviewed pull request. Contributors push with **Create new PR**. The pull request lists the number of changed files and preview URLs of affected pages on the new branch, so that a developer can check the result before merging. See [Broader Contribution, Same Production Control](overview.md#production-control).
1. **Import scripts:** The scripts that import content are JavaScript files in the repository's `tools/importer/` folder. Review them like other code, because they decide the structure of every imported page.
1. **Content:** Authors preview and publish pages. Limit who can publish with the site's [publish role](https://www.aem.live/docs/authentication-setup-authoring).
1. **Agent permissions:** Keep the permissions that let the agent push, upload, or publish turned off unless a task needs them. When one is on, the agent acts with that user's access, and the same controls apply.
1. **Acceptance:** Agree the acceptance criteria before the migration starts, covering coverage, authoring, function, accessibility, performance, and search. A page that looks like its source isn't accepted until authors can edit it and it works. See [Accept the Result](production-migration.md#acceptance).

Optional plan mode lets a user approve the agent's plan before it changes files. It helps each person work carefully, but your organization's approval happens in the controls above.

### Trace What the Agent Did {#audit-trail}

The console keeps no separate audit log, but the agent's work doesn't go unrecorded. What the agent produces reaches your site only through your Git repository or through Experience Manager, and both keep a history:

* **Code is the primary record.** Blocks, styles, and import scripts are all code, and the import scripts define how the content of every imported page is structured. Your Git history records each change to them.
* **Content changes are recorded with the content.** Experience Workspace keeps a version history of each document, and the author instance keeps its own page versions.
* **The conversation shows what was asked.** **Download chat** saves the conversation as a Markdown file. Download it before you select **Clear chat**, which removes the messages and can't be undone. See [Chat Panel](console.md#chat-panel).

The record is easiest to follow when each request to the agent ends in its own commit and, where pages changed, its own content upload. Ask for this in the project's `AGENTS.md`. See [Leave a Record of Each Request](project-instructions.md#trace).

* **Commit and push after each request.** With the matching [agent permission](console.md#settings-page) turned on, the agent pushes on its own. Have it push to a working branch rather than to `main`, so that its changes still reach production through a reviewed pull request.
* **Offer the content upload.** The agent uploads content only when your message asks for it or you agree when it asks. Have it list the changed pages at the end of each request and ask whether to upload them, so that one answer approves the upload. For content on the author instance, people upload the pages themselves.

Each request then leaves one commit and one upload: a step-by-step record of what the agent changed, which reviewers read in tools that they already use. Work that is never pushed or uploaded stays in the console workspace and doesn't reach your site.

## Team and Phases {#team-model}

A project with the agent starts with one person and then widens:

* One developer or technical lead sets up the project and lays the foundation: the global styles, the first blocks, and the import scripts of the first templates.
* Content and authoring specialists check that the content model is easy to edit before the team imports at scale.
* Once the blocks are agreed, the team divides the work by block, template, or expertise. Designers refine the styling, and developers build the integrations. See [Start with One Person, Then Divide the Work](overview.md#divide-work).
* Developers review every code change. The project lead runs acceptance and release.

For who does what in each phase of a migration, see [Phases and Roles](production-migration.md#phases). For what each kind of expertise contributes, see [Who Can Use the Agent](overview.md#who-can-use-ema).

## How the Migration Scales {#scale}

* **The platform:** Edge Delivery Services runs large multi-market and multi-language sites. Its largest sites have more than 100,000 pages.
* **The agent:** The AI model works out the mapping on one representative page of each template, and the bulk import then runs the template's import script on its other pages without the model interpreting each one. A site of 5,000 pages that share 12 layouts is mostly the work of 12 templates. A page with a layout of its own counts as a template of its own. See [How the Agent Migrates at Scale](overview.md#migration-at-scale). To size the work from the first templates, see [Estimate Before You Commit](production-migration.md#estimate).
* **The team:** Each person works in their own console workspace, and the console doesn't coordinate them yet. Divide the work so that people change different files and pages. See [Collaborating on a Project](overview.md#collaboration).
* **Several sites:** A console workspace holds one connected site at a time. In a program with several sites, plan their order, and push and upload each site's work before you switch. To relaunch sites that run on Experience Manager today, see [Relaunch a Site That Runs on Experience Manager](production-migration.md#relaunch-aem-site).
* **Assisted delivery:** For complex migrations, Adobe engineers can operate the agent for you. See [AOE Delivery](aoe-delivery.md).

## Where Content Is Stored {#content-destination}

Before the migration, decide where content is stored and which editor authors use. For new implementations, including large sites, Adobe strongly recommends document-based persistence, edited visually in Experience Workspace. Experience Manager authoring, with content stored in the JCR of the author instance and edited in the Universal Editor, remains fully supported when a requirement depends on content staying in the JCR. The source CMS doesn't determine the choice, and Edge Delivery Services delivers the pages either way. See [Where Content Is Stored and How Authors Edit It](overview.md#content-storage).

## Figma and Design Systems {#figma}

Figma can be the source of a new design. The agent reads a Figma file the way a developer reads a design handoff, and turns it into code. It reaches Figma through the Figma import add-on, which gives it a Model Context Protocol (MCP) server that reads files through Figma's API:

* **Variables and styles become design tokens.** Through the MCP server, the agent reads the variables and styles of the selected design, such as colors, typography, and spacing, and uses them to reproduce the design accurately. It writes them as CSS custom properties in the project's global styles. These properties are the site's design tokens. They live in the code, not in a separate token export, so designers and developers review them like any other change.
* **Components become blocks or variants.** From a Figma link, the agent builds one block or component at a time, and maps it to an existing block where one fits, often as a variant. See [Figma Block Migration](prompting-guide.md#figma-block-migration).
* **Figma and a live site work together.** In a [redesign migration](overview.md#figma-redesign), the Figma components define the blocks and the live site provides the content. To [create a page](overview.md#figma-new-page) that the source site lacks, a Figma frame provides both the design and the content.

What to approve:

* **Access:** Each person who uses Figma with the agent creates a Figma personal access token with read-only scopes and stores it in the console's [settings](console.md#settings-page). This access token is a Figma credential, unrelated to the design tokens above: Figma issues and governs it, including its scopes and the limits below. There is no organization-wide Figma connection. A personal access token can't be limited to specific files: it reads every file that its owner can open. The token is added to the MCP server's requests to Figma, and the agent never receives it.
* **Seats and rate limits:** Figma limits how often a token can read files, based on the token owner's seat and the plan that owns the file. With a View or Collab seat, a token can read files through Figma's API only a few times a month, so people who use Figma with the agent need a Dev or Full seat. See Figma's [rate limits](https://developers.figma.com/docs/rest-api/rate-limits/).
* **Data:** For the selected frame or component, the agent sends its structure, a screenshot, its variables, and its text to the AI model. See [What the AI Model Processes](#security-model-data).
* **Who does the work:** Designers can direct it themselves. See [Make Visual Changes](visual-changes.md#figma).

## Costs and Entitlement {#costs}

Signing in to the console doesn't establish your organization's entitlement. Depending on your agreement, migrating pages consumes AI credits. They are counted once for each page that is uploaded to your content destination, not per prompt, so iterating on a page and uploading it again don't add to them. See [Access and AI Credit Usage](getting-started.md#access), and contact your Adobe account team for your entitlement, usage, and commercial terms.

## What Remains Project Work {#project-work}

The agent is a development agent: what can be built on Edge Delivery Services can be built with it. A migration copies what the source pages show, though, not the systems behind them. The agent rebuilds the site: its pages, blocks, styles, and the code that calls your services. Approval and publishing workflows, the back-end systems behind integrations, and how your teams work on the new site remain your organization's work. These needs require a decision from your team before the agent can build them:

| Need | What import gives you | What to decide, then build with the agent |
|---|---|---|
| Shared content, such as a banner or disclaimer on many pages | A copy on each page | Which content to keep once and include as a fragment, and the block that includes it. |
| Several languages or markets | Pages at their source paths, with their locale folders | The URL structure, the language alternates in the sitemap, and how translation and inheritance between markets work for your authors. See [Translation and Localization](https://www.aem.live/docs/translation-and-localization). |
| Personalization, search, and account features | Each page's output at the time of import | The service that provides the logic, and the blocks that call it. |
| Forms | The form's fields, with the forms add-on | The system that receives submissions, such as your marketing automation platform or customer relationship management (CRM) system, and the workflows that follow. The add-on is built for organizations that license Adobe Experience Manager Forms, and its form block requires that license. See [Form Submissions](block-development.md#form-submissions). |
| Commerce | Product detail and listing pages, with the commerce pages add-on for storefronts on Adobe Commerce. The product data loads from the catalog, not from the imported page. | The storefront setup and its Adobe Commerce license, or, for another commerce platform, the blocks that call its API. See [Commerce Pages](block-development.md#commerce-pages). |
| Analytics, tag management, and consent | With Auto mode's **Include integrations**, the supported settings, switched off until you turn them on | Which tags load, and when, so that the pages stay fast. |
| Redirects, sitemaps, and canonical URLs | Page titles, descriptions, and social images | The URL policy and its configuration. See [URLs, Redirects, and Search Metadata](production-migration.md#urls-seo). |

For source access, interactive content, and other boundaries of the import, see [Limitations](overview.md#limitations).

## Next Steps {#next-steps}

* See a result on your own content: [Start with Auto mode](getting-started.md#brand-trial).
* Plan a migration: [Migrate a Production Site](production-migration.md).
* Talk to the people who build the agent: ask your Adobe customer success manager or account team for a meeting with subject-matter experts and the product team. See [The Team Behind the Agent](#adobe-team).
* Read short answers to common questions: [Experience Modernization Agent FAQ](faq.md).
