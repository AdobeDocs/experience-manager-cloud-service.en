---
title: Experience Modernization Agent FAQ
description: Answers to common questions about access, Auto mode, planning, blocks, source sites, Git connections, approvals, recovery, and data in the Experience Modernization Agent.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: c9cfe838-9ea3-417c-aa26-01411ad5d612
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

# Experience Modernization Agent FAQ {#faq}

Short answers to questions that users of the Experience Modernization Agent often ask, each with a link to the guide that covers it. For error messages and things that don't work as expected, see [Troubleshooting](troubleshooting.md). For the guides that fit your role, see [Start Here by Role](overview.md#start-by-role).

## Access and Usage {#access-usage}

### How do I get access to the console? {#get-access}

Through your Adobe account team. You can sign up for Auto mode yourself at [`aemcoder.adobe.io/auto`](https://aemcoder.adobe.io/auto). See [Access and AI Credit Usage](getting-started.md#access).

### I belong to several Adobe organizations. Which workspace do I get? {#organizations}

One per organization. Projects and chats stay in the organization where you created them; to reach another organization's, sign out and choose its profile when you sign in again. See [Open the Experience Modernization Console](getting-started.md#open-console).

### Can I use a new or personal Adobe ID? {#adobe-id}

Only if it belongs to your company's Adobe organization. Your Adobe account team can add you to it. See [Open the Experience Modernization Console](getting-started.md#open-console).

### If I can sign in to the console, is my organization licensed to use the agent? {#entitlement}

Not necessarily. Your Adobe account team confirms your organization's entitlement and commercial terms. See [Access and AI Credit Usage](getting-started.md#access).

### Does the agent consume AI credits? {#ai-credits}

Depending on your organization's agreement, yes: for pages uploaded to your content destination, not for prompts. Auto mode runs don't consume them. See [Access and AI Credit Usage](getting-started.md#access) for what counts, and ask your Adobe account team about your organization's usage.

### Can I use the console on a phone or tablet? {#mobile}

Yes. The console adapts its layout to smaller screens, so that you can follow a long task on a phone. See [Menu Bar](console.md#menu-bar).

## Auto Mode {#auto-mode}

### What does Auto mode do? {#auto-mode-what}

It migrates pages of a website, including their design, without stopping for your review: it imports them, compares the result with the source, refines it, and emails you when it's done. The guided workflow in the console stops after each step instead. See [Start with Auto Mode](getting-started.md#brand-trial).

### Does Auto mode move my existing repository? {#auto-mode-repository}

No. Auto mode migrates a website, starting from its URL or a list of page URLs. To work on a site that already runs on Edge Delivery Services, [connect it](getting-started.md#connect-repo) in the console.

### Can I guide how Auto mode identifies or builds blocks? {#auto-mode-guidance}

Not during a run: you set its scope and options before it starts. To guide block identification or styling as you go, use the [guided workflow](getting-started.md#guided-import), or refine the result in the console after the run.

### How many pages does Auto mode migrate? {#auto-mode-pages}

Up to 10 per migration by default, so a full-site run gives you a preview of the site, not all of it. Select **Ask for a higher limit** to request more, or import further pages in the console later. See [Auto Mode Limits](getting-started.md#auto-mode-limits).

### How long does an Auto mode run take? {#auto-mode-duration}

Up to 24 hours. Checking and refining its own work makes it slower than a guided import of the same pages. See [Start with Auto Mode](getting-started.md#brand-trial).

### Is the result of an Auto mode run ready for production? {#auto-mode-production}

No. It's a first result to review; [Start with Auto Mode](getting-started.md#brand-trial) lists what to check. Continue in the console to import more pages and refine them, and for a release, follow the [production migration guide](production-migration.md).

### What does Make it yours do? {#make-it-yours}

It moves a finished run to a site that you own: the code to a new branch of your repository, and the pages and their media to your site's content in Experience Workspace. Nothing is published or merged into `main`. See [Make It Yours](getting-started.md#make-it-yours).

### Do I need to create a repository before I use Make it yours? {#make-it-yours-repository}

Yes. The destination is an Edge Delivery Services site of your own, whose content is stored in Experience Workspace. See [Make It Yours](getting-started.md#make-it-yours) for its requirements, and [Create a New Site from the Boilerplate](getting-started.md#prepare-repo) to set one up.

### Does the transfer copy redirects, metadata, permissions, or site configuration? {#transfer-scope}

No. Only code, pages, and the media that the pages reference are transferred. Set up spreadsheets such as redirects, bulk metadata, and placeholders, as well as permissions and configuration, in the destination. See [Make It Yours](getting-started.md#make-it-yours).

## Planning and Scale {#planning-scale}

### How do I use Plan mode? {#plan-mode}

Switch the prompt input to Plan mode, with the light bulb icon, and describe your task. The agent proposes an approach and a checklist without changing files, and **Execute plan** carries it out. Plan mode works at any time, without a site catalog, and has nothing to do with the **Planning** view. See [Prompt Input](console.md#prompt-input).

### Why don't I see the Planning view? {#planning-view}

**Planning** is always in the view picker of the workspace panel, under **Project**; you don't need to turn it on. It shows the site catalog, the inventory of templates, pages, and blocks that you review before migrating. Before you catalog a site, it asks for the site's address. See [Open the Planning View](site-catalog.md#accessing-planning-ui).

### Can I switch between several migration plans? {#several-plans}

No. The **Planning** view shows one plan per console workspace, so you can't switch between plans, for example one per country site. Plan and migrate the sites one after the other. See [Open the Planning View](site-catalog.md#accessing-planning-ui).

### Can I choose which pages to migrate? {#choose-pages}

Yes. In the console, name the pages to import, or choose templates and pages in the [site catalog](site-catalog.md). In Auto mode, provide a list of page URLs instead of a site URL.

### Can the agent migrate hundreds or thousands of pages? {#scale}

Yes. The agent migrates a sample page for each template, and then generates import scripts that bring in the template's other pages. Fixes go into those scripts and the blocks, so they reach every page of the template. See [How the Agent Migrates at Scale](production-migration.md#migration-at-scale).

### How should we plan a large migration? {#plan-large-migration}

Catalog the site, sign off a sample page for each template, and only then import the rest. For a site too large to catalog at once, the agent proposes how to divide it; see [Invoking](site-catalog.md#invoking). A console workspace holds one site at a time, so in a program with several sites, push and upload each site's work before you [switch site](getting-started.md#connect-repo). For assisted delivery, see [AOE Delivery](aoe-delivery.md).

## Blocks {#blocks}

### How should I ask the agent to build a block? {#block-prompt}

Start with a short prompt that names the block and what authors put in it. The agent works out the content and the content model with you before it writes code. To match a design, give the page URL and the section, attach a screenshot, or select the element in the console preview with **Inspect mode**. See [Prompt for a Block](block-development.md#block-prompts).

### Can the agent reuse our existing blocks or block library? {#reuse-blocks}

Yes. The agent first looks for a block to reuse or adapt in your project. During migration, it also checks the block library that **Library URL** in Settings points to. To reuse blocks from another repository, add them to this project first. See [Reuse Existing Blocks](block-development.md#reuse-blocks).

### Should I ask for many blocks in one prompt? {#many-blocks}

No. The decisions that you make on the first blocks carry over to the next, so build them one at a time. See [Build Blocks One at a Time](block-development.md#iterate-blocks).

### Can the agent build a dynamic block after migration? {#dynamic-block}

Yes. Ask for it like any other block, and describe the data source, what authors control, and what each item shows. The agent models the author settings as a key-value table. See [Build a Dynamic Block](block-development.md#dynamic-blocks).

### Can I define how a block behaves before the migration? {#block-behavior}

Yes: in the migration prompt, in the project instruction files for conventions that last, or in the **Planning** view before code is generated. See [Set Block Behavior Before a Migration](block-development.md#block-instructions).

### Where do form submissions go after migration? {#form-submissions}

Wherever you choose. Edge Delivery Services doesn't store submissions, and the source's processing doesn't come with the page. For organizations that license Adobe Experience Manager Forms, the forms add-on migrates each form to the Forms block, which by default sends submissions to the Forms Submission Service. For another system, such as a marketing automation platform, the agent builds the form and that platform's administrator sets up the receiving side. See [Form Submissions](block-development.md#form-submissions).

### Does the commerce pages add-on work with platforms other than Adobe Commerce? {#commerce-platforms}

It's built for Adobe Commerce. It recognizes product pages on any source site, but the pages that it creates need Adobe Commerce as a Cloud Service or Adobe Commerce Optimizer, which can supply the catalog when another platform handles checkout. Without either, the agent can build product and listing blocks that call your platform's API. See [Commerce Pages](block-development.md#commerce-pages).

## Source Sites {#source-sites}

### Does it matter which CMS or framework the source site uses? {#source-technology}

No. The agent works from the rendered page, not from the source's code or CMS. Features that run on the source's servers, such as personalization rules, search, or form processing, aren't in the rendered page, so decide how each works on the new site. See [Limitations](overview.md#limitations).

### Can I relaunch a site that runs on Adobe Experience Manager today? {#relaunch-aem-site}

Yes. The agent treats it like any other source, and leaves the source site and your other Experience Manager sites unchanged. Components, experience fragments, and inherited content arrive as their output on each page. See [Relaunch a Site That Runs on Experience Manager](production-migration.md#relaunch-aem-site).

### What if the source site uses bot protection? {#bot-protection}

Arrange access with the site's administrator, and don't work around the protection. See [Source Sites with Bot Protection](troubleshooting.md#bot-protection) for the options.

### Can the agent migrate pages that require sign-in? {#protected-pages}

Yes, when the source accepts one of the authentication methods that the console supports. Store a read-only credential in the console's settings, or in Auto mode's authentication fields, never in the chat. See [Protected Site Authentication](console.md#protected-site-authentication) for the methods.

### Can the agent reach a site behind a VPN, a firewall, or single sign-on? {#private-sources}

No. The agent reaches a source only over the internet, from its hosted environment, and it can't complete an interactive sign-in such as single sign-on (SSO) or multi-factor authentication. Ask the site's administrator for a staging or origin host that the agent can reach; see [Protected Site Authentication](console.md#protected-site-authentication).

## Destinations and Git {#destinations}

### Can the agent write content to Experience Manager authoring with the Universal Editor? {#aem-authoring}

Yes, in the guided workflow. The agent converts the pages to JCR content and uploads them to your Adobe Experience Manager as a Cloud Service author instance as a content package. See [Getting Started for Experience Manager Authoring Projects](getting-started-aem-authoring.md). Auto mode and Make it yours produce document-based content for Experience Workspace only.

### Which Git hosts can the console push to? {#git-hosts}

GitHub, and any Git host that Cloud Manager connects, such as GitHub Enterprise, GitLab, Bitbucket, or Azure DevOps. See [Use Another Git Host](getting-started.md#other-git).

### Do I need AEM Code Sync, AEM Code Connector, or a token? {#git-apps}

AEM Code Sync on every GitHub project, so that your site can read its code, and AEM Code Connector for the console to push. A personal access token replaces the connector's sign-in for GitHub Enterprise, or when OAuth sign-in isn't available. See [Start from a Repository](getting-started.md#repo-start).

### Can the agent push to main or publish without my approval? {#approval}

Only if you turn on its permissions in **Settings** > **Agent permissions**: with Git access, it can push even to `main`. Without them, code and content leave the console workspace only when you push, upload, or publish them yourself. To require approval, protect `main` and limit who has the site's publish role, because the console's own checks are safeguards, not approval gates. See [Control over Changes](evaluate.md#security-control).

## Recovery {#recovery}

### What happens to my work if I reload the page or leave? {#reload}

It stays: the chat history and the files in your console workspace are kept. If the workspace has paused in the meantime, see [Open the Experience Modernization Console](getting-started.md#open-console).

### How do I restore a page that was overwritten? {#restore-page}

Restore an earlier version from the document's version history in Experience Workspace. A page that Make it yours overwrote has a version named **Before Transfer**. Code is recovered through Git. See [Make It Yours](getting-started.md#make-it-yours).

## Data and Security {#data-security}

### Can I give the agent a password or API key in the chat? {#secrets-in-chat}

No. The chat reaches the AI model, and the agent can copy what you write into files that your site serves to every visitor. Enter credentials in the console's **Settings** instead, and revoke any secret that you've already shared. See [Keep Secrets Out of the Chat](prompting-guide.md#secrets).

### How can the agent call an API that needs a key while it works? {#api-credentials}

Add the key in **Settings** > **Protected site authentication** as an entry for the API's hostname, and tell the agent that it's there. The console attaches it to the agent's requests, so the AI model never sees it. See [Credentials for Other Services](console.md#other-services).

### Can the agent use its own token instead of my account? {#agent-tokens}

Yes. Under **Settings** > **Agent permissions**, enter an Adobe service account's token in **Custom IMS Token** and, where the Git permission is available, a scoped personal access token in **Custom Git Token**. See [Settings Page](console.md#settings-page).

### Which AI model does the agent use? {#model}

The agent currently uses Claude models. The model is an implementation detail that can change. See [What the AI Model Processes](evaluate.md#security-model-data).

### Does the agent learn from my data? {#training}

No. Adobe doesn't train AI models on your data; see [What the AI Model Processes](evaluate.md#security-model-data). Between conversations, the agent knows only what is written in your project's files; see [What the Agent Remembers](project-instructions.md#memory).

### What data reaches the AI model, and which systems does the agent connect to? {#data-flows}

The model receives your prompts, the source pages, the repository's code, design references, and what the agent generates. The agent connects to your Git repository, your content destination, the source site, Figma when you use it, and the services that you set up credentials for, without receiving those credentials. See [Security and Data Handling](evaluate.md#security).

### Is there an audit log of what the agent did? {#audit-trail}

Not as a separate log, but the agent's work is recorded. Everything that it produces reaches your site through Git, which records each code change, or through Experience Workspace or the author instance, which keep each page's versions. To keep a conversation, select **Download chat** before you clear it. See [Trace What the Agent Did](evaluate.md#audit-trail).

### Where can I find retention and compliance information? {#retention-compliance}

From your Adobe account team and the [Adobe Trust Center](https://www.adobe.com/trust.html). For what the console itself keeps, see [Where Your Work Is Stored](evaluate.md#security-storage).

### Can I give the agent health data? {#hipaa}

No. The agent is a developer tool that your site's visitors never reach, so the only health data that it sees is what you give it: keep real patient and user data out of it, including the pages that you migrate. See [Health Data and HIPAA](evaluate.md#security-hipaa), which also links the Experience Manager services that can process protected health information (PHI).

## Product Fit and Help {#product-fit}

### Do I need to be a developer to use the agent? {#audience}

Not for a first result: Auto mode migrates your pages without step-by-step prompting. To change the site, you describe what you want in plain language, but you need some HTML and the basics of Git and GitHub, because changes reach production through pull requests. Authors edit content without Git. See [Who Can Use the Agent](overview.md#who-can-use-ema).

### Can several people work on the same project? {#collaboration}

Yes, each in their own console workspace, sharing code through pull requests. The console doesn't coordinate them, and the last upload of a page replaces earlier ones, so agree who works on what. See [Work as a Team](production-migration.md#collaboration).

### Can Edge Delivery Services run complex sites, or only simple ones? {#complex-sites}

Complex enterprise sites. Pages are standard HTML, CSS, and JavaScript, so a block can call any API or run a complete application, and spreadsheets and the query index give blocks your own data. See [Understand Your Project](overview.md#project-foundations).

### Is the agent limited to Edge Delivery Services? {#beyond-eds}

No. Its skills focus on Edge Delivery Services, but it is a general-purpose coding agent: it can also adapt an existing application or write a server-side service for your team to deploy. For a system that it has no skills for, start by giving it that system's documentation. See [Work Beyond Edge Delivery Services](prompting-guide.md#beyond-eds).

### Can the agent build integrations with other systems? {#integrations}

Yes: the blocks and code that connect your site to commerce platforms, marketing technology, search, or your own APIs. Page import doesn't carry the source's scripts over, so plan each integration as project work. See [Connect Services and Applications](block-development.md#integrations).

### Can we teach the agent our own procedures? {#custom-skills}

Yes. Write your conventions in `AGENTS.md`. For a recurring task that needs precise steps, add a project skill in `.claude/skills/<skill-name>/SKILL.md`; the agent reads it when a task matches its description. Its folder's name starts with a dot, which changes how you push it. See [Advanced: Custom Skills](project-instructions.md#custom-skills).

### Can I change how the agent answers? {#reply-style}

Yes. Write how you want answers in `AGENTS.md`, for example shorter answers, another language, or no suggested next steps. See [Change How the Agent Answers](project-instructions.md#reply-style).

### How does the agent relate to Experience Workspace? {#experience-workspace}

Experience Workspace is where authors edit the document-based content that the agent uploads; **Edit in Experience Workspace** in the console opens a page there. The agent itself works in the console, on the site's code and on importing content. Experience Workspace has its own [assistant](https://www.aem.live/docs/ew/authoring/assistant) for the content open in the editor. See [Content Views](console.md#content-view).

### Why can't the agent use a capability that I've heard about? {#capability-availability}

Some capabilities are optional add-ons, which are off until they're turned on for the project. When your request needs one, the agent offers to turn it on. You can also ask it which add-ons are on, or ask for one by name. See [Optional Capabilities](console.md#optional-capabilities).

### How do I get help? {#help}

Select **Request support** in the console, or **Get help** on the Auto mode pages; see [Request Support](console.md#request-support) for what to include. To meet experts or the product team, see [The Team Behind the Agent](evaluate.md#adobe-team).

### Where are the release notes? {#release-notes}

See the [Experience Modernization Agent release notes](/help/release-notes/modernization-agent/current.md). In the console, **What's new** shows the highlights of each release.
