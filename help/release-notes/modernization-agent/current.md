---
title: Experience Modernization Agent Release Notes
description: Release notes for the Experience Modernization Agent (EMA) and its console, with all releases on one page, newest first.
feature: Release Information
role: Admin
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: ed762d86-a04b-452b-a08f-86359bb8ff27
    internal-label: Configuration and operations
subfeature_v2:
  - id: c21ccc2b-e0c8-4853-bf41-f12259ed93f8
    internal-label: Release information
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---

# Experience Modernization Agent Release Notes {#release-notes}

This page lists the user-facing changes in each release of the Experience Modernization Agent (EMA) and its console, newest first. Release numbers are release dates in the format year.month.day. Each release has its own heading that you can link to directly.

>[!TIP]
>
>The console also summarizes the highlights of the latest release in a **What's new** notice at the top of the page. To learn what the agent does and how to start, see the [Experience Modernization Agent overview.](/help/ai-in-aem/agents/brand-experience/modernization/overview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## 2026.11.02 Release {#release-2026-11-02}

### What's New {#release-2026-11-02-what-is-new}

* **Guided review of your migration plan:** When planning finishes, the agent offers to **Review scoping results**. It first fixes clear issues itself, such as moving outliers, merging look-alike block variants, and correcting names, and tells you what it changed. It then walks you through the remaining decisions one at a time. Choose **Autopilot** at the start, or **Finish for me** on any step, to let it complete the review alone. Items it is still unsure about are left unchanged and flagged in its report. See [Review the catalog.](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md#review-catalog)
* **Page limits for Auto mode migrations:** Before you start an Auto mode migration, the page shows how many pages each migration can include for your account. If your account allows it, you can choose how many pages a full-site migration includes. See [Auto mode limits.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md#auto-mode-limits)

### Other Improvements {#release-2026-11-02-other-improvements}

* Chat, Home, and Settings now fit phone and tablet screens.
* The chat input has been updated and keeps its existing features.
* A **Demo site** button in the header now explains, before you start working, that work in the demo site isn't saved. See [Demo mode.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md#demo-mode)
* Planning progress now shows the current step.
* Site discovery is more reliable.
* Prompt hints no longer flag suggested prompts that you send unchanged or only extend. Rewording a suggestion triggers the usual checks.
* Agent guidance uses plain language instead of internal migration terms.
* Long task lists scroll within the chat, and you can expand or collapse the pending tasks.
* Preview now uses the site configuration to find the correct code repository.
* The agent recognizes requests to restore or preview a page in Experience Workspace (which replaces Document Authoring), and explains when writing to remote content is not allowed.
* Conversations with many screenshots no longer fail. Older screenshots are shortened automatically.
* **Upload to AEM** for AEM authoring projects fails less often.

## 2026.10.28 Release {#release-2026-10-28}

### What's New {#release-2026-10-28-what-is-new}

* **Plan your migration:** Planning is available to all console users, with a new start screen, live discovery progress, and controls to stop and resume without starting over. See [Site catalog.](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md)
* **Live page import status:** Track each page's import progress, open its preview from your migration plan, and generate code for only the blocks you select. See [Bulk import.](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md#bulk-import)
* **Prompt hints and prompt recall:** The console can suggest a clearer prompt before you send it, and you decide whether to use the hint. In an empty prompt input, use the up and down arrow keys to recall previous prompts. See [Prompt input.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#prompt-input)

### Other Improvements {#release-2026-10-28-other-improvements}

* Large projects stay responsive while you browse files, review changes, preview pages, and check sync status.
* Page imports are more reliable and no longer save an access-error screen as the content of a page.
* Sites that send large response headers now load in the preview.
* Browser actions that stop responding now time out after ten minutes, so the agent can continue.
* When you [request support,](/help/ai-in-aem/agents/brand-experience/modernization/console.md#request-support) you can include selected excerpts of the conversation.

## 2026.10.23 Release {#release-2026-10-23}

### What's New {#release-2026-10-23-what-is-new}

* **Improved site catalog:** Cataloging breaks pages into the blocks that an author actually edits, groups pages with the same layout into one template, and checks the results after scoping. Block mapping uses visual analysis, which produces fewer variants, cleaner templates, and cleaner screenshots. Your manual splits and moves are kept when you run it again. See [Site catalog.](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md)
* **Pull content from Experience Workspace:** The **Sync** menu has a **Pull** section. **Pull** > **Content** downloads your Experience Workspace (which replaces Document Authoring) pages over the workspace copies and keeps pages that exist only in the workspace. **Pull** > **Code** replaces the **Pull** button of the code view. See [Sync menu.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#sync-menu)

### Other Improvements {#release-2026-10-23-other-improvements}

* Pushing content shows a progress bar, and push and pull tell you when your Experience Workspace session has expired.
* Local images in header and footer pages now upload to Experience Workspace correctly, and the upload tells you which images need fixing.
* Uploads and Settings explain when your AEM environment is hibernated and link to the Developer Console.
* Long tasks, such as generating code for many blocks, no longer fail to send, and very large workspaces no longer freeze.
* When the agent uploads a page directly to Experience Workspace, the preview shows the same version.

## 2026.10.21 Release {#release-2026-10-21}

### What's New {#release-2026-10-21-what-is-new}

* **Support for the latest Edge Delivery Services content backend:** You can upload, download, preview, and publish content on sites that use the latest content backend, and transfer Auto mode projects to them with **Make it yours**. See [Make it yours.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md#make-it-yours)
* **Block confidence:** The **Blocks** view of planning has a sortable **Confidence** column that shows which blocks need your review, and marks the blocks that you have confirmed. See [Blocks table.](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md#blocks-table)

### Other Improvements {#release-2026-10-21-other-improvements}

* Blocks with hundreds of instances open faster and load more instances as you scroll.
* While the agent works, the chat shows an animated indicator with an elapsed time.
* Work in progress resumes automatically after a service restart, and stopped tasks stay stopped.
* Content edits stay in your workspace until you upload them or explicitly ask the agent to update Experience Workspace.
* Saving agent permissions, site authentication, or credentials in [Settings](/help/ai-in-aem/agents/brand-experience/modernization/console.md#settings-page) shows **Applying...** until the change takes effect. Signing out of GitHub fully revokes the agent's access.

## 2026.10.16 Release {#release-2026-10-16}

### What's New {#release-2026-10-16-what-is-new}

* **Auto mode for sites that require sign-in:** Auto mode can migrate sites that require sign-in, using a user name and password, a bearer token, or a custom header. The credentials are sent only to that site and are not stored. See [Start with Auto mode.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md#brand-trial)

### Other Improvements {#release-2026-10-16-other-improvements}

* Page migrations produce better results.
* Cataloging sites with more than 1,000 pages completes reliably, and the chat tells you when page analysis is interrupted and resumed.
* Very tall pages keep their blocks when page templates are detected.
* Cataloging pages from an uploaded URL list shows its completion summary for the correct site.

## 2026.10.08 Release {#release-2026-10-08}

### What's New {#release-2026-10-08-what-is-new}

* **Block variant instances:** Planning shows the instances of each block variant. See [Variant instances.](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md#variant-instances)
* **Transfers overwrite existing pages by default:** When you transfer an Auto mode site, existing pages are overwritten by default. You can change this before you start the transfer. See [Make it yours.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md#make-it-yours)
* **Feedback on Auto mode runs:** Give feedback on an Auto mode run directly in the console.

### Other Improvements {#release-2026-10-08-other-improvements}

* Switching sites works after a workspace reset.
* Transfers to Bring Your Own Git sites and to repoless sites now complete.
* Task progress appears reliably during runs.

## 2026.10.05 Release {#release-2026-10-05}

### What's New {#release-2026-10-05-what-is-new}

* **Block sample content:** EMA generates sample content for blocks so that you can preview them with realistic content. See [Block deliverables.](/help/ai-in-aem/agents/brand-experience/modernization/block-development.md#block-deliverables)

### Other Improvements {#release-2026-10-05-other-improvements}

* Scope reports of large sites load page by page with server-side search, so they open faster.
* Switching sites after a transfer shows the content of the new site.
* Section metadata is applied when previewing pages.
* Previews of large repositories no longer run out of memory when they start.

## 2026.09.29 Release {#release-2026-09-29}

### What's New {#release-2026-09-29-what-is-new}

* **Blocks view in planning:** Switch the planning dashboard, templates, and pages to a **Blocks** view that groups every variant under its block, with its code status and actions to generate, classify, rename, or regroup blocks. See [Blocks table.](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md#blocks-table)
* **Live progress for long-running tasks:** Tasks such as block code generation show a live progress summary in the chat task card.

### Other Improvements {#release-2026-09-29-other-improvements}

* Block and variant changes that you make in the catalog are kept when the site is analyzed again.
* The site catalog, project knowledge, and other skills are no longer blocked from reading their reference files or saving project settings.
* Pressing **Stop** on an unresponsive agent frees it, so the conversation can continue.
* Signing in with a personal Adobe ID now explains that an Adobe organization is required.

## 2026.09.28 Release {#release-2026-09-28}

### What's New {#release-2026-09-28-what-is-new}

* **Early access to auto migration:** You can sign up with your Adobe account to request early access to auto migration.
* **Review failed URLs:** See which pages failed during site scope, why they failed, and when. See [Failed URLs.](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md#failed-urls)

### Other Improvements {#release-2026-09-28-other-improvements}

* Site scope analyzes every discovered URL instead of a sample, and completes its analysis more reliably.
* Branch names that would break preview links are blocked, and a shorter name is suggested.
* Switching sites no longer risks overwriting the content of the active site.
* Chat attachments stay with their messages when the chat history is reloaded.

## 2026.09.24 Release {#release-2026-09-24}

### What's New {#release-2026-09-24-what-is-new}

* **Newer AI model:** Chats and site migrations run on a newer, more capable AI model.

### Other Improvements {#release-2026-09-24-other-improvements}

* Projects with large folders outside the content folder no longer slow down or stall the workspace.

## 2026.09.23 Release {#release-2026-09-23}

### Other Improvements {#release-2026-09-23-other-improvements}

* Branch names that would exceed the length limit of preview URLs are blocked, and a shorter name is suggested, instead of breaking the preview.
* Content uploads now correctly change from pending to synced.
* Your GitHub connection persists across workspace restarts.
* Section metadata renders correctly again.

## 2026.09.17 Release {#release-2026-09-17}

### What's New {#release-2026-09-17-what-is-new}

* **Rename block variants:** Block variants keep a stable identity when the catalog is regenerated, so a renamed variant keeps its name and type. See [Planning actions.](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md#planning-actions)
* **Act on several items at once:** Select multiple templates or pages and apply an AI action to all of them at once. See [Planning actions.](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md#planning-actions)
* **Create a page from a Figma design:** A suggested prompt on the **Home** page starts building a page from a Figma design. See [Create a new page from Figma.](/help/ai-in-aem/agents/brand-experience/modernization/prompting-guide.md#figma-new-page-from-figma)
* **Optional design skills:** Guided redesign is available as an optional add-on, so projects that don't need it stay lighter. See [Optional capabilities.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#optional-capabilities)

### Other Improvements {#release-2026-09-17-other-improvements}

* Switching between sites no longer wipes your workspace content. The content of each site is backed up and restored when you switch back.
* Migrations with very large commit descriptions commit reliably, and the preview retries automatically if it fails to start.

## 2026.09.10 Release {#release-2026-09-10}

### Other Improvements {#release-2026-09-10-other-improvements}

* Large attachments and long pasted text no longer stall the chat.
* Browser actions recover automatically if the connection drops during a task.
* The site catalog detects blocks correctly on pages with cookie banners.
* Page and template screenshots display again in the site scope view.

## 2026.09.09 Release {#release-2026-09-09}

### What's New {#release-2026-09-09-what-is-new}

* **Planning fills in as it runs:** When you run a site scope, the planning view shows templates and pages as they are produced. You can sort the tables, attach a template or page to the chat as context, and run an action from a row. See [Site catalog.](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md)
* **Page screenshots in template views:** Template tables show a screenshot and title for each page, so you can check template groupings at a glance.
* **Purpose-built block code:** Migration generates each block from the content model discovered for your pages, and delivers a README and an authoring guide with every block it creates. See [Block deliverables.](/help/ai-in-aem/agents/brand-experience/modernization/block-development.md#block-deliverables)

### Other Improvements {#release-2026-09-09-other-improvements}

* Resetting the workspace stops the running agent, so old chat history, tasks, and files don't reappear.

## 2026.09.01 Release {#release-2026-09-01}

### What's New {#release-2026-09-01-what-is-new}

* **Bring Your Own Git:** Connect a site whose code is hosted on GitLab, Bitbucket, or Azure DevOps through Cloud Manager, in addition to GitHub. See [Connect your site.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md#connect-repo)

### Other Improvements {#release-2026-09-01-other-improvements}

* Re-running a site migration preserves your earlier template work, and blocked or failed page captures are reported as errors.

## 2026.08.27 Release {#release-2026-08-27}

### What's New {#release-2026-08-27-what-is-new}

* **More reliable header, navigation, and footer migration:** Header, navigation, and footer migration checks text, visual appearance, breakpoints, and accessibility against the source.

## 2026.08.26 Release {#release-2026-08-26}

### What's New {#release-2026-08-26-what-is-new}

* **Bulk preview and publish:** Preview and publish many pages at once with live progress. The job continues and reports the status of each page if you navigate away. See [Content views.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#content-view)
* **Automatic template grouping:** Migration analyzes your pages and groups them into templates automatically.
* **Branch status before pulling:** See how many commits your branch is ahead of or behind the remote before you pull.

### Other Improvements {#release-2026-08-26-other-improvements}

* Long chat sessions stay responsive as the history grows.
* A previous session can no longer post its answer into the chat after you switch repositories or demos.

## 2026.08.20 Release {#release-2026-08-20}

### What's New {#release-2026-08-20-what-is-new}

* **Protected site authentication:** In Settings, add basic, bearer, or custom-header credentials so that the agent can reach password-protected source sites. The credentials are never exposed to the AI model. See [Protected Site Authentication.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#protected-site-authentication)
* **Transfer to an existing site:** Site transfer can target an existing Edge Delivery Services site instead of always creating a new one.

### Other Improvements {#release-2026-08-20-other-improvements}

* The chat no longer answers from an earlier session after you switch demos or repositories.
* Large uploads resume automatically after your computer wakes from sleep.

## 2026.08.13 Release {#release-2026-08-13}

### What's New {#release-2026-08-13-what-is-new}

* **Custom block library from chat:** Ask the agent to generate a block library for your custom blocks, including sample content and library configuration, for Experience Workspace (which replaces Document Authoring) or AEM authoring. See [Block deliverables.](/help/ai-in-aem/agents/brand-experience/modernization/block-development.md#block-deliverables)

### Other Improvements {#release-2026-08-13-other-improvements}

* You no longer need to reconnect GitHub manually when your access token expires.
* Large branch switches and slow checkouts no longer freeze the workspace.
* Content and images are correct for sites whose content location differs from the site name.
* Migrations complete noticeably faster.

## 2026.08.06 Release {#release-2026-08-06}

### What's New {#release-2026-08-06-what-is-new}

* **Office documents in chat:** Attach Word, PowerPoint, and Excel files to the chat. The agent receives their text and embedded images. See [Prompt input.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#prompt-input)
* **Better Figma page migration:** Card artwork, hidden carousel and tab slides, and large hero images migrate from Figma more accurately. See [Create a new page from Figma.](/help/ai-in-aem/agents/brand-experience/modernization/prompting-guide.md#figma-new-page-from-figma)
* **Import completeness check:** Imports are checked for missing or extra content, flagging pages that need attention before and after a bulk import.

### Other Improvements {#release-2026-08-06-other-improvements}

* The site transfer page explains how to create an Edge Delivery Services site if you don't have one yet.
* Questions from the agent include an **Other** option, so you can answer in your own words.
* Sites that share a repository load their own Experience Workspace content.
* Previews are more reliable under load.

## 2026.07.29 Release {#release-2026-07-29}

### What's New {#release-2026-07-29-what-is-new}

* **Modern web best practices:** The agent applies Google's Modern Web Guidance when it writes or edits CSS and client-side JavaScript.
* **Media copied during transfer:** Transferring content to Experience Workspace also copies the images and media that the pages reference. See [Make it yours.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md#make-it-yours)

### Other Improvements {#release-2026-07-29-other-improvements}

* Previews stay stable under heavy use.
* Preview styling renders correctly.
* Preview links open correctly for catalog-based projects.
* The **Changes** tab no longer shows internal tool output.
* For AEM authoring projects, content-mapping problems are shown in the JCR XML view.

## 2026.07.20 Release {#release-2026-07-20}

### What's New {#release-2026-07-20-what-is-new}

* **One Sync button:** Push code and upload content from one global **Sync** button. See [Sync menu.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#sync-menu)
* **Background Experience Workspace uploads:** Uploads run in the background with live progress, so the console stays responsive.
* **Faster inspect mode:** Turn the inspect mode of the preview on and off without reloading the preview. See [Content views.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#content-view)

### Other Improvements {#release-2026-07-20-other-improvements}

* Connecting to large AEM authoring sites no longer times out.
* Git operations recover automatically instead of getting stuck.
* Index pages use `/` instead of `/index` in AEM preview and publish URLs.

## 2026.07.14 Release {#release-2026-07-14}

### What's New {#release-2026-07-14-what-is-new}

* **Transfer page:** Use the new **Transfer** page to move a project's code and content to another Edge Delivery Services site. See [Make it yours.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md#make-it-yours)
* **Automatic preview and publish for AEM authoring:** AEM authoring projects can be previewed and published automatically after upload.
* **Guided AEM Code Connector setup:** If the AEM Code Connector GitHub app isn't installed, the console detects it and walks you through installing it. See [Connect your site.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md#connect-repo)
* **Editable suggested prompts:** Suggested prompts on the **Home** page fill the prompt input so that you can edit them before sending, and Figma prompts are easier to find. See [Home page.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#home-page)

### Other Improvements {#release-2026-07-14-other-improvements}

* The Experience Workspace preview and publish dialog keeps its status when you switch content views.
* Downloaded chat history includes timestamps and session information.

## 2026.07.09 Release {#release-2026-07-09}

### What's New {#release-2026-07-09-what-is-new}

* **Responsive preview:** The preview defaults to a **Responsive** viewport that fills the panel and reflows as you resize it. **Desktop**, **Tablet**, and **Mobile** remain available. See [Content views.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#content-view)
* **Agent uploads to Experience Workspace (opt-in):** The option in Settings that lets the agent use your Adobe credentials also covers Experience Workspace, so the agent can upload pages without you pasting a token into the chat. See [Settings.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#settings-page)
* **Edit in Experience Workspace:** An **Edit** button opens the current page in Experience Workspace in a new tab. See [Content views.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#content-view)
* **Next-step suggestions:** The chat suggests next steps below the latest answer of the agent.

### Other Improvements {#release-2026-07-09-other-improvements}

* Images render on pages synced from Experience Workspace.
* [**Request support**](/help/ai-in-aem/agents/brand-experience/modernization/console.md#request-support) works even when your workspace is unavailable.
* The conversation context is preserved if the agent restarts during a conversation.

## 2026.07.03 Release {#release-2026-07-03}

### What's New {#release-2026-07-03-what-is-new}

* **Agent use of your Git credentials (opt-in):** An option in Settings lets the agent use your Git credentials. A warning explains the access that this grants before you turn it on. See [Settings.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#settings-page)
* **Optional plugins:** Core skills are always available, and extended skills are optional plugins. The agent suggests a plugin when it is relevant and asks before enabling it, which keeps the assistant lighter and faster. See [Optional capabilities.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#optional-capabilities)

### Other Improvements {#release-2026-07-03-other-improvements}

* File downloads are more reliable.
* Git operations are more stable. Returning to a repository opens the branch of the preview URL of the site instead of `main`.

## 2026.06.23 Release {#release-2026-06-23}

### What's New {#release-2026-06-23-what-is-new}

* **Next-step prompt suggestions:** After a few chat turns, the agent suggests follow-up prompts. Skills also suggest next steps at transitions, such as starting design migration after content import.
* **Branch-aware Experience Workspace links:** Preview and publish links use your active branch instead of always `main`.
* **Figma migration for AEM authoring:** Figma block migration supports AEM authoring projects and generates the required block definitions. See [Figma block migration.](/help/ai-in-aem/agents/brand-experience/modernization/prompting-guide.md#figma-block-migration)

### Other Improvements {#release-2026-06-23-other-improvements}

* Content views update automatically after the agent changes files, and imported pages appear in the page list without reloading the browser.
* Experience Workspace preview and publish no longer report false failures.

## 2026.06.15 Release {#release-2026-06-15}

### What's New {#release-2026-06-15-what-is-new}

* **More faithful design migration:** Improved content import and block detection identify, reuse, and structure content as reusable blocks, and design migration matches the layout and styling of source pages more closely.
* **GitHub Enterprise and personal access tokens:** Connect to GitHub Enterprise and authenticate with a personal access token. See [Connect your site.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md#connect-repo)
* **Separate chat sessions per repository:** Each connected repository has its own agent session, so context no longer carries over when you switch repositories.

## 2026.06.03 Release {#release-2026-06-03}

### What's New {#release-2026-06-03-what-is-new}

* **Redesigned console:** Resizable chat and content panels, redesigned toolbars, an HTML view, simpler chat messages, and a tour of the console that you can request in the chat. See [Experience Modernization Console.](/help/ai-in-aem/agents/brand-experience/modernization/console.md)
* **Demo site for new users:** First-time users start with a preloaded demo site. Pushing code and uploading content are unavailable in the demo site. Use **Switch site** to work on your own site. See [Demo mode.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md#demo-mode)

### Other Improvements {#release-2026-06-03-other-improvements}

* Error screens show a reference ID that you can include when you request support.

## 2026.05.25 Release {#release-2026-05-25}

### What's New {#release-2026-05-25-what-is-new}

* **Dynamic Media and Scene7 images:** Images served by Adobe Dynamic Media or Scene7 are migrated as responsive images, with their parameters preserved.
* **Header and footer migration:** Dedicated skills migrate site headers and footers and check their appearance before completion.

## 2026.05.20 Release {#release-2026-05-20}

### What's New {#release-2026-05-20-what-is-new}

* **Site catalog and scoping:** Generate page templates and a scoping report for a site, covering URL discovery, page grouping, template clustering, and block cataloging. See [Site catalog.](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md)

## 2026.05.12 Release {#release-2026-05-12}

### What's New {#release-2026-05-12-what-is-new}

* **Work kept across branches:** Your conversation and working content are saved when you switch branches, and restored when you return to the same repository.
* **Download existing content:** Download content from Experience Workspace and AEM authoring sources to work on it in the console.
* **Improved design migration:** Design migration sets up global brand styles and reuses CSS variables across global and block styles. See [Restyling.](/help/ai-in-aem/agents/brand-experience/modernization/restyling.md)

### Other Improvements {#release-2026-05-12-other-improvements}

* The accessibility of the console has been improved.
* The site connection dialog accepts full preview URLs, including paths.

## 2026.03.26 Release {#release-2026-03-26}

### What's New {#release-2026-03-26-what-is-new}

* **Plan mode:** The agent can outline an approach without changing files. Review the plan, then execute it or start a new plan. See [Prompt input.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#prompt-input)
* **Project knowledge skills:** New skills help with project handover, administration, authoring guides, and development guides. See [Project documentation.](/help/ai-in-aem/agents/brand-experience/modernization/project-documentation.md)
