---
title: Experience Modernization Agent FAQ
description: Answers to common questions about access, Auto mode, planning, blocks, source sites, Git connections, approvals, previews, recovery, and data in the Experience Modernization Agent.
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

These are answers to questions that users of the Experience Modernization Agent often ask. Each answer is short and links to the guide that explains the topic in full.

>[!TIP]
>
>Looking for a starting point for your role? Decision-makers can start with [Evaluate and Approve](evaluate.md), migration leads with [Getting Started](getting-started.md) and [Migrate a Production Site](production-migration.md), and designers with [Make Visual Changes](visual-changes.md). See [Start Here by Role](overview.md#start-by-role).

## Access and Usage {#access-usage}

### How do I get access to the console? {#get-access}

Request access to the Experience Modernization Console through your Adobe account manager. Auto mode, which is in early access, has its own access request at [`aemcoder.adobe.io/auto`](https://aemcoder.adobe.io/auto). See [Access and AI Credit Usage](getting-started.md#access).

### Can I use a new or personal Adobe ID? {#adobe-id}

You need an Adobe ID that belongs to your company's Adobe organization. A personal Adobe ID that isn't part of an organization can't use the console. If you don't have a company account, ask your Adobe account team to add you to the organization. See [Open the Experience Modernization Console](getting-started.md#open-console).

### If I can sign in to the console, is my organization licensed to use the agent? {#entitlement}

Not necessarily. Being able to sign in does not by itself establish your organization's entitlement. Contact your Adobe account team for your entitlement and commercial terms.

### Does the agent consume AI credits? {#ai-credits}

Depending on your organization's agreement, migrating pages consumes AI credits. They are counted once for each page that is uploaded to your content destination. Prompts, iterations on a page, and uploading the same page again don't add to them. See [Access and AI Credit Usage](getting-started.md#access) and Adobe's [AI credit consumption](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/overview/ai-credit-consumption) guide. For your organization's usage, contact your Adobe account team.

## Auto Mode {#auto-mode}

### What does Auto mode do? {#auto-mode-what}

Auto mode migrates pages of a website on its own, including their design. It imports the content, migrates the design, critiques the result against the source, and keeps refining it, without stopping for your review. It emails you when the run finishes. In the guided workflow, the agent instead stops after each step so that you can check it. See [Start with Auto Mode](getting-started.md#brand-trial).

### Does Auto mode move my existing repository? {#auto-mode-repository}

No. Auto mode migrates a website, starting from its URL or a list of page URLs. To work on a site that already runs on Edge Delivery Services, [connect it](getting-started.md#connect-repo) in the console.

### Can I guide how Auto mode identifies or builds blocks? {#auto-mode-guidance}

Not during a run. Once a run starts, it doesn't ask for your input; you choose its scope and options before you start. To guide block identification or styling as you go, use the guided workflow, or refine the result in the console after the run.

### How many pages does Auto mode migrate? {#auto-mode-pages}

When you are granted Auto mode access, each migration can include up to 10 pages by default. A full-site run migrates a preview of up to that many pages, not the whole site. Use **Ask for a higher limit** to request more, and import further pages later in the console. See [Auto Mode Limits](getting-started.md#auto-mode-limits).

### How long does an Auto mode run take? {#auto-mode-duration}

A run can take up to 24 hours. Auto mode is slower than a guided import of the same pages because it checks and refines its own work. You can leave the page, and you receive an email when the run finishes.

### Is the result of an Auto mode run ready for production? {#auto-mode-production}

No. A run gives you a first result to review: check which pages were migrated, and their content, links, images, and styles. Links to pages outside the run can still point to the source site. Continue in the console to import more pages and refine them. For a release, follow the [production migration guide](production-migration.md).

### What does Make it yours do? {#make-it-yours}

It transfers the code and content of a finished Auto mode run to a site that you own. The code goes to a new branch in your repository, and the pages and their media are copied to the site's content in Experience Workspace. It doesn't publish anything or merge into `main`. See [Make It Yours](getting-started.md#make-it-yours).

### Do I need to create a repository before I use Make it yours? {#make-it-yours-repository}

Yes. The destination must be an Edge Delivery Services site whose code is in a repository created from a template, such as the [AEM boilerplate](https://github.com/adobe/aem-boilerplate), on GitHub with the AEM Code Sync and AEM Code Connector apps installed, or on another Git host connected through Cloud Manager. The repository needs a `main` branch, and the site's content must be stored in Experience Workspace. See [Make It Yours](getting-started.md#make-it-yours) and [Create a New Site from the Boilerplate](getting-started.md#prepare-repo).

### Does the transfer copy redirects, metadata, permissions, or site configuration? {#transfer-scope}

No. The transfer copies code, pages, and the media that pages reference. It doesn't copy spreadsheets, such as redirects, bulk metadata, or placeholders, nor access permissions or site and organization configuration. Set these up in the destination.

## Planning and Scale {#planning-scale}

### How do I use Plan mode? {#plan-mode}

Switch the prompt input to Plan mode, with the light bulb icon, and describe your task. The agent proposes an approach and a checklist without changing files. Select **Execute plan** to carry it out. Plan mode is available at any time; you don't need to catalog a site first. See [Prompt Input](console.md#prompt-input).

### Why don't I see the Planning view? {#planning-view}

**Planning** is always in the view picker of the workspace panel, under **Project**; you don't need to turn it on. Before you catalog a site, it asks for the site's address. See [Accessing the Site Planning UI](site-catalog.md#accessing-planning-ui).

### Can I switch between several migration plans? {#several-plans}

No. The site planning UI shows one plan per console workspace, so you can't switch between plans, for example one per country site. Plan and migrate the sites one after the other. See [Accessing the Site Planning UI](site-catalog.md#accessing-planning-ui).

### Can I choose which pages to migrate? {#choose-pages}

Yes. In the console, name the pages to import, or choose templates and pages in the [site catalog](site-catalog.md). In Auto mode, provide a list of page URLs instead of a site URL.

### Can the agent migrate hundreds or thousands of pages? {#scale}

Yes. The agent groups pages into templates, migrates one representative page for each template with the AI model, and then imports the template's other pages with generated import scripts. Corrections go into the blocks and scripts, so they apply to every page of the template. See [How the Agent Migrates at Scale](overview.md#migration-at-scale).

### How should we plan a large migration? {#plan-large-migration}

Start with the [site catalog](site-catalog.md) to see the templates and how many pages each one has. Validate the representative pages before you import the rest. The console workspace holds one connected site at a time, and [switching site](getting-started.md#connect-repo) replaces it, so plan the order of sites in a program with several sites and push and upload each site's work before you switch. For your organization's AI credit entitlement, contact your Adobe account team. For assisted delivery, see [AOE Delivery](aoe-delivery.md).

## Blocks {#blocks}

### How should I ask the agent to build a block? {#block-prompt}

Start with a short prompt that names the block and what authors put in it. The agent works out the content and the content model with you before it writes code. To match a design, give the page URL and the section, attach a screenshot, or select the element in the console preview with **Inspect mode**. See [Prompt for a Block](block-development.md#block-prompts).

### Can the agent reuse our existing blocks or block library? {#reuse-blocks}

Yes. The agent first looks for a block to reuse or adapt in your project. During migration, it also checks the block library that **Library URL** in Settings points to. To reuse blocks from another repository, add them to this project first. See [Reuse Existing Blocks](block-development.md#reuse-blocks).

### Should I ask for many blocks in one prompt? {#many-blocks}

No. Build one or two representative blocks first, and check their content model, styling, and authoring. Then continue with the others, so that the decisions carry over. You can line up the next blocks in the prompt queue. See [Build Blocks One at a Time](block-development.md#iterate-blocks).

### Can the agent build a dynamic block after migration? {#dynamic-block}

Yes. Ask for it like any other block, and describe the data source, what authors control, and what each item shows. The agent models the author settings as a key-value table. See [Build a Dynamic Block](block-development.md#dynamic-blocks).

### Can I define how a block behaves before the migration? {#block-behavior}

Yes. Describe it in the migration prompt, write lasting conventions in the project instruction files, or correct block types and variants in the site planning UI before you generate code. Auto mode doesn't take instructions during a run. See [Set Block Behavior Before a Migration](block-development.md#block-instructions).

## Source Sites {#source-sites}

### Does it matter which CMS or framework the source site uses? {#source-technology}

No. The agent loads each source page in a browser and works from what it renders: the content and design that visitors see. Features that run on the source's servers, such as personalization rules, search, or form processing, aren't in the rendered page, so decide how each works on the new site. See [Limitations](overview.md#limitations).

### What if the source site uses bot protection? {#bot-protection}

Ask the site's administrator to allow access for the migration, for example by allowlisting the agent's backend addresses or by giving you a credential such as a secret header. Don't work around the protection. See [Source Sites with Bot Protection](troubleshooting.md#bot-protection).

### Can the agent migrate pages that require sign-in? {#protected-pages}

Yes, when the source accepts a custom request header, HTTP Basic authentication, or bearer authentication. Enter the credentials in the console's [Protected Site Authentication](console.md#protected-site-authentication) settings, or in Auto mode's authentication fields, never in chat. Use a scoped, read-only credential. This is not intended for personally identifiable information (PII) or real end-user data.

### Can the agent reach a site behind a VPN, a firewall, or single sign-on? {#private-sources}

No. The source must be reachable from the agent's hosted environment on the internet. It can't connect through a VPN, pass a firewall, or complete interactive sign-in such as single sign-on (SSO) or multi-factor authentication. Ask the administrator for an internet-reachable staging or origin host that accepts a supported method.

## Destinations, Git, and Sync {#destinations}

### Can the agent write content to Experience Manager authoring with the Universal Editor? {#aem-authoring}

Yes, in the guided workflow. The agent converts the pages to JCR content and uploads them to your Adobe Experience Manager as a Cloud Service author instance as a content package. See [Getting Started for Experience Manager Authoring Projects](getting-started-aem-authoring.md). Auto mode and Make it yours produce document-based content for Experience Workspace only.

### Which Git hosts can the console push to? {#git-hosts}

GitHub, and other Git hosts that are connected through Cloud Manager, such as GitHub Enterprise, GitLab, Bitbucket, or Azure DevOps. For Cloud Manager repositories, the access token needs write access to the repository code, and the console pushes a branch without opening a pull request. See [Use Another Git Host](getting-started.md#other-git).

### Do I need AEM Code Sync, AEM Code Connector, or a token? {#git-apps}

AEM Code Sync lets Edge Delivery Services read your code to serve the site; every project on GitHub needs it. AEM Code Connector lets the console connect to your GitHub repository, push code, and open pull requests. A personal access token is another way to sign in, for GitHub Enterprise or when OAuth sign-in isn't available. See [Start from a Repository](getting-started.md#repo-start) and [Connect Your Site](getting-started.md#connect-repo).

### Why can't I see my GitHub organization or repository? {#git-org-missing}

The AEM Code Connector app is usually missing from the organization or the repository, or the organization hasn't approved it yet. With a token, the console lists only repositories that you can push to. See [Git Connection Problems](troubleshooting.md#git-connection).

### Can the agent push to main or publish without my approval? {#approval}

Only if you give the agent access. Without agent permissions, code and content leave the console workspace only when you push, upload, or publish them. With **Allow LLM to use my git credentials**, the agent can push to any branch that your credentials can write to, including `main`. With the Adobe credentials permission, the console stops the agent from uploading, previewing, or publishing unless your current message asks for it or you agree when the agent asks. These are safeguards, not approval gates. To require approval, protect `main` with branch protection and limit who has the site's publish role. See [Control over Changes](evaluate.md#security-control).

### Why is Allow LLM to use my git credentials missing from Settings? {#git-credentials-missing}

The setting isn't available to you yet. The agent can still change code in the console workspace, and you push it with **Sync** > **Push** > **Code**. See [Settings Page](console.md#settings-page).

### Why does the console say that my Document Authoring session may have expired? {#session-expired}

The console shows this message both when your session has expired and when your Adobe account doesn't have write access to the site's content. Sign in again and retry. If it persists, ask the site's administrator to give the account that you use in the console write access in Experience Workspace. See [Content Writes Fail](troubleshooting.md#write-errors).

### Why does a code push work while a content upload fails? {#different-accounts}

They use different accounts. Code is pushed with your GitHub or Cloud Manager connection, and content is written with the Adobe account that you signed in with. Check that each account has access to its destination. See [Content Writes Fail](troubleshooting.md#write-errors).

### Why does Create package say Missing site configuration? {#missing-site-configuration}

In an Experience Manager authoring project, the console couldn't find the project's site path and DAM folder on the author instance. Check that the site exists on the author instance that the project's content source points to, and that your account can access it, then reload the console. If the message persists, request support. See [Upload Content](getting-started-aem-authoring.md#upload-content).

## Preview {#preview}

### Why doesn't the console preview match the live page? {#preview-mismatch}

The console preview renders the console workspace's copy of the content with the workspace's code. The preview and live sites render the saved content with the code of the branch in their URL. Content that is not uploaded or not pulled, unpushed code, another branch, or a different viewport width can explain the difference. Edge Delivery Services also removes markup that the console preview keeps, such as inline styles, `span` elements, and data attributes. See [Console Preview Differs from the Site](troubleshooting.md#preview-differs) and [How the Preview Works](console.md#how-preview-works).

### Does Refresh update the preview from Experience Workspace? {#refresh-preview}

No. **Refresh** only reloads the rendering of the console workspace copy. To replace the console's copies with the saved documents, use **Sync** > **Pull** > **Content**, which overwrites local edits to those pages. To replace a single page, delete its local copy and open the page again from the cloud icon. See [Sync Menu](console.md#sync-menu) and [Content Views](console.md#content-view).

### Can I use the console on a phone or tablet? {#mobile}

Yes. On a phone, the chat page shows only the chat, so that you can follow a long task. On a tablet, you switch between the chat and the workspace in the header. See [Menu Bar](console.md#menu-bar).

## Recovery {#recovery}

### Why does the console take a while to open my workspace? {#environment-setup}

When you first open the console, or after a reset, it sets up your console workspace, which can take up to 10 minutes. If all workspaces are in use, setup starts automatically as soon as one is available. See [Workspace Setup Takes Time or Fails](troubleshooting.md#workspace-setup).

### What if my project seems to be missing? {#missing-project}

Sign in with the same Adobe account and organization that you used before. Don't reset the workspace while you investigate, because a reset permanently deletes it. If the project is still missing, request support. See [Project Seems Missing](troubleshooting.md#missing-workspace).

### What happens to my work if I reload the page or leave? {#reload}

The chat history and the files in your console workspace are kept. After a period of inactivity, the workspace pauses; select **Wake up** to restore it. See [Open the Experience Modernization Console](getting-started.md#open-console) and [Chat Panel](console.md#chat-panel).

### How do I restore a page that was overwritten? {#restore-page}

In Experience Workspace, restore an earlier version of the document from its version history. Before a Make it yours transfer overwrites a page, it saves the page's previous state as a version named **Before Transfer**. Code changes are recovered separately, through your Git repository.

### What does Reset workspace delete? {#reset}

The console workspace's chat history, files, and session state, and the GitHub connection. Pushed code and uploaded content are not affected. See [Settings Page](console.md#settings-page).

### Why won't the agent delete pages when I ask in chat? {#delete-pages}

A safeguard in the console stops the agent from deleting files in the project's content folder, so that migrated content isn't removed by mistake. Delete local pages yourself, one at a time, with **Delete** in a content view. Uploaded, previewed, or published pages must also be removed from Experience Workspace and the preview and live sites. See [Remove Pages](troubleshooting.md#remove-pages).

### What does Failed to send message mean? {#send-failed}

The console couldn't deliver your prompt to the agent, and the message doesn't give the cause: it can be your network connection, an expired sign-in, or a temporary service problem. Send the prompt again, then reload the page if it still fails. If it persists, request support. See [Failed to Send Message](troubleshooting.md#send-failed).

## Data and Security {#data-security}

### Which AI model does the agent use? {#model}

The agent currently uses Claude models. The model is an implementation detail that can change. See [What the AI Model Processes](evaluate.md#security-model-data).

### Does the agent learn from my data? {#training}

Adobe does not use your conversations or other customer data to train or fine-tune AI models. Within your project, the agent has no memory of its own between conversations; to make it remember a decision, write it in a file in your repository. See [What the AI Model Processes](evaluate.md#security-model-data) and [What the Agent Remembers](overview.md#memory).

### What data reaches the AI model, and which systems does the agent connect to? {#data-flows}

The Experience Modernization Agent sends your prompts, source page content, repository code, design references, and the generated content and code to the AI model. It connects to your Git repository, Experience Workspace or your author instance, the source site, and Figma when you use it. The AI agent doesn't receive the credentials that you configure. See [Security and Data Handling](evaluate.md#security).

### Is there an audit log of what the agent did? {#audit-trail}

Not as a separate log in the console, but the agent's work is recorded. What it produces reaches your site only through Git or Experience Manager. Your Git history records every code change, including changes to the import scripts that define how content is imported. Experience Workspace and the author instance record content changes in their version history. To keep the conversation itself, select **Download chat** before you clear the chat; **Clear chat** can't be undone. To get one commit and one content upload per request, instruct the agent in `AGENTS.md` to commit and push to a working branch after each request, and to offer to upload the changed pages. See [Trace What the Agent Did](evaluate.md#audit-trail).

### Where can I find retention and compliance information? {#retention-compliance}

For processing locations, data retention, and compliance information, contact your Adobe account team or see the [Adobe Trust Center.](https://www.adobe.com/trust.html)

## Product Fit and Help {#product-fit}

### Do I need to be a developer to use the agent? {#audience}

No. You describe what you want in plain language and check the result in the preview. Designers, content specialists, and marketers can migrate pages, refine styling, and shape blocks, while developers review every code change before it reaches production. Authors edit content day to day in Experience Workspace, or in the Universal Editor for Experience Manager authoring. See [Who Can Use the Agent](overview.md#who-can-use-ema).

### Can several people work on the same project? {#collaboration}

Yes. Each person works in their own console workspace and shares code through pull requests in Git. The console doesn't coordinate their work, so agree who changes which blocks, templates, and pages. Content uploads have no merge: the last upload of a page replaces the previous one. See [Collaborating on a Project](overview.md#collaboration).

### Can Edge Delivery Services run complex sites, or only simple ones? {#complex-sites}

Complex enterprise sites. Each page is standard HTML, CSS, and JavaScript, so a block can call any API from the browser, such as search, commerce, or personalization, or run a complete application. Spreadsheets publish as JSON and a query index lists the site's pages, so blocks can also build listings and filters from your own content. Each integration is project work that you specify, and the agent can write the code for it. See [Understand Your Project](overview.md#project-foundations).

### How does the agent relate to Experience Workspace? {#experience-workspace}

Experience Workspace is where authors edit the document-based content that the agent uploads. From the console, **Edit in Experience Workspace** opens a page there. You work with the agent itself in the Experience Modernization Console, at [`aemcoder.adobe.io`](https://aemcoder.adobe.io). See [Content Views](console.md#content-view).

### Why can't the agent use a capability that I've heard about? {#capability-availability}

Some capabilities are optional add-ons, which are off until they're turned on for the project. When your request needs one, the agent offers to turn it on. You can also ask it which add-ons are on, or ask for one by name. Auto mode needs its own access request. The capabilities on offer can change between releases. See [Optional Capabilities](console.md#optional-capabilities).

### How do I get help? {#help}

Use **Request support** in the console. Name the affected page, what you expected, what happened instead, and when. See [Request Support](console.md#request-support).

### Where are the release notes? {#release-notes}

See the [Experience Modernization Agent release notes](/help/release-notes/modernization-agent/current.md). The console's **What's new** notice also lists the highlights of each release.
