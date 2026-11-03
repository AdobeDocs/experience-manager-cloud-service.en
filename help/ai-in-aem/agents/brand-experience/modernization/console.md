---
title: Experience Modernization Console
description: Reference guide for the Experience Modernization Console interface and capabilities
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: 43d8c124-fc87-4cec-a91d-ab12255ae321
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

# Experience Modernization Console {#console-reference}

The Experience Modernization Console is the web interface for the Experience Modernization Agent (EMA): the browser UI where you work with EMA. This reference describes its views, controls, and settings. The console works on a hosted copy of your project, which these docs call the console workspace. It is unrelated to Experience Workspace, the authoring UI; see [Names You May See](overview.md#names).

>[!NOTE]
>
>To use the Experience Modernization Console, request access through your Adobe account manager. See [Access and AI Credit Usage](getting-started.md#access).

## Overview {#overview}

The Experience Modernization Console is a hosted, AI-assisted development environment for Edge Delivery Services (EDS), at [`aemcoder.adobe.io`.](https://aemcoder.adobe.io) The page header shows the title **Adobe Experience Manager**. After you connect your GitHub project, you can start prompting changes in natural language without any further setup or local environment configuration. If you are new to the console, ask the agent in the chat for a tour of the console.

>[!TIP]
>
>If you are interested in getting started right away with the console, check out the document [Getting Started with the Experience Modernization Agent.](getting-started.md)

## Capabilities {#capabilities}

Core capabilities of the console:

* Interactive chat panel, where you describe tasks to the agent and its skills in natural language
* Previews of the console workspace and of the EDS preview site, so that you can check changes visually before and after you upload them
* Content file browser and [content views](#content-view) that show a page as a rendered preview, a document, Markdown, JCR XML, or HTML, so that you can check its content structure and conversion as well as its appearance
* Content upload to the document-based repository that authors edit in [Experience Workspace](https://www.aem.live/docs/ew/about), or package creation and upload for [AEM authoring](getting-started-aem-authoring.md#upload-content), according to project configuration. Experience Workspace was formerly called Document Authoring, and the console still uses that name in some labels. See [Where Content Is Stored and How Authors Edit It](overview.md#content-storage).
* Code browser and diff viewer, so that you can review exactly what changed before you push
* GitHub integration with the ability to create pull requests from changes, so that agent changes go through your usual code review
* [Site planning](#project-view), to inventory a source site and group its pages into templates before you migrate
* [Optional capabilities](#optional-capabilities) that you turn on per project when a task needs them

Review changes before saving to a shared destination. A code push is a Git commit to your repository; a content upload writes to Experience Workspace or AEM authoring. They are separate operations. The console pushes to a new pull request or directly to the current branch, so your repository's branch protection decides which changes need review. Plan mode changes how the agent works in the conversation, not what the repository or the site accepts. See [Control over Changes](overview.md#security-control).

For complete procedures, choose [a way to start](getting-started.md#first-outcome), [production migration](production-migration.md), [restyling](restyling.md), or [block development](block-development.md).

## Navigation {#navigation}

After signing into the console at [aemcoder.adobe.io,](https://aemcoder.adobe.io) use the [home page](#home-page) to start work or continue in the [chat page](#chat-page). Confirm the active project and branch before making changes.

![Home screen of console](assets/console-home.png)

### Menu Bar {#menu-bar}

The top menu bar provides:

* An **Adobe Experience Manager** title on the left that links to the Home Page when clicked
* A **Demo site** button when you are working in the [demo site](getting-started.md#demo-mode). It explains that work there isn't saved and that the demo can't push code to GitHub or content to Experience Workspace. Use **Switch site** to connect your own site.
* A **Request support** button where you can send details of any issues that were encountered. See [Request support](#request-support).
* An **Account** button on the right for switching to dark mode and signing out of the console

The console also shows notices at the top of the page, such as service status and [**What's new**](#whats-new) for the latest release. Chat, Home, and Settings adapt to phone and tablet screens. On a phone, the chat page shows only the chat. On a tablet, it shows one panel at a time; switch between the chat and the workspace in the header. On wider screens, both panels show side by side.

## Home Page {#home-page}

The **Home** page is your starting point for using the console.

* At the top is a [prompt input](#prompt-input) for making requests of the console.
* Below the prompt panel are suggested prompts for getting started with your project.
* A **Start chatting** button that takes you to the [chat page](#chat-page).
* A **Settings** button to access the [project settings](#settings-page) page

### Prompt Input {#prompt-input}

The prompt input provides controls for interacting with the AI.

* **Plan / Execute modes** (light bulb and magic wand icons): Toggle between planning and execution modes, respectively.
  * **Plan mode**: The agent analyzes your request and proposes an approach without changing files. It ends with a plan that includes a checklist of steps. Use it for multi-page, shared-code, or otherwise risky changes, so that you can review and adjust the approach before anything changes. Select **Execute plan** to switch to Execute mode and carry out the plan, or start a new one. Plan mode is available at any time, including before you plan or catalog a site. Only you switch modes; the agent can't switch them itself.
  * **Execute mode**: The agent performs the request and can make actual file changes.
  * Planning is optional and is not an enforced approval gate. Before execution, state the allowed scope and whether upload, push, or publication is authorized.
* **Attach files** (paperclip icon): Upload and attach files to the prompt for additional context, such as reference designs, screenshots, or specifications. The agent sees attached images in JPEG, PNG, GIF, or WebP format. You can also attach Word, PowerPoint, and Excel files; the agent receives their text and embedded images.
* **Prompt queue** (clock icon): Additional prompts can be queued up to be automatically executed once the current prompt has completed, so that you can line up follow-up tasks without waiting.
* **Previous prompts**: In an empty prompt input, use the up and down arrow keys to recall earlier prompts. A draft you have started is not overwritten.
* **Prompt hints**: Where enabled, the console points out when a prompt is missing details, such as the page or the result you expect, and can suggest a clearer prompt. You decide whether to use the hint. Prompts suggested by the console are not flagged unless you reword them. Configure hints under **Prompt coach** in [Settings](#settings-page).

## Chat Page {#chat-page}

The [**Chat** page](https://aemcoder.adobe.io/chat) is the main interface for interacting with EMA. This page is split into a resizable [chat panel](#chat-panel) and [workspace panel.](#workspace-panel)

## Chat Panel {#chat-panel}

The chat panel allows you to view and continue your conversation with EMA. The chat panel includes the chat message history and a [prompt input](#prompt-input) for making additional requests of the console.

The chat panel header includes links for navigating to the [Home](#home-page) and [Settings](#settings-page) views and chat actions.

* **Chat actions**
  * **Clear chat**: This starts a new conversation without the earlier history. It is not a code or content rollback. Before clearing, ask EMA to record important decisions in the [project instruction files](project-instructions.md) that it reads in every conversation.
  * **Download chat**: This downloads the conversation history as a markdown file.

The conversation is saved with your console workspace. When you reload the page or return later, the chat history reloads. Prompts that you recall with the arrow keys last only as long as the browser tab.

### Optional Capabilities {#optional-capabilities}

Core skills, such as site planning, page migration, bulk import, and header, navigation, and footer migration, are always available. Other capabilities are optional add-ons. Each add-on is off by default and is turned on per project, which keeps the agent lighter and faster for projects that don't need it.

* When your request needs an add-on, EMA offers to turn it on and asks for your confirmation first. The add-on is available from your next message.
* You can also ask for an add-on directly, for example "Enable the forms migration capability", or describe your task and accept EMA's offer.
* To see which add-ons are on, ask EMA, for example "Which add-ons are enabled for this project?" To turn one off, ask EMA in the same way. The Settings page has no add-on controls yet.

| Add-on | ID | What it is for |
|---|---|---|
| Figma import | `excat-figma@excat-extended` | Migrating blocks and creating pages from Figma designs. See [Figma block migration](prompting-guide.md#figma-block-migration). |
| Guided redesign (Stardust) | `stardust@excat-extended` | Redesigning several pages of a site to a new design direction, step by step, and checking the result. See [Guided Redesign](restyling.md#guided-redesign). |
| Design craft | `impeccable@excat-extended` | Applying frontend design-quality guidance, such as typography, spacing, and visual hierarchy, to design work. Turned on automatically with guided redesign, and usable on its own. |
| Project documentation | `project-management@excat-extended` | Generating project and handover documentation as PDF guides. See [Project documentation](project-documentation.md). |
| Forms migration | `forms-excat@excat-extended` | Migrating AEM Forms-based forms to EDS forms. |
| Commerce pages | `excat-commerce@excat-extended` | Detecting product detail and product listing pages and migrating them into commerce page templates. |
| Block library setup | `excat-block-library@excat-extended` | Setting up the library that authors use to find and insert your blocks. See [Block deliverables](block-development.md#block-deliverables). |
| EDS troubleshooting | `excat-support@excat-extended` | Diagnosing EDS problems on demand, such as blocks that don't render or changes that don't appear. See [Debugging](prompting-guide.md#debugging). |
| Modern web guidance | `modern-web-guidance@excat-extended` | Applying current web-platform best practices, for example for fonts, loading performance, accessibility, and layout, when the agent writes CSS and JavaScript. |

The add-ons on offer can change between releases. If EMA says that it can't do something, ask whether an add-on covers it.

#### Turn On Add-ons for the Whole Project {#persist-add-ons}

EMA saves the add-ons that you turn on in the `.agents/settings.json` file at the root of your repository. The file lists each add-on by its ID:

```json
{
  "enabledPlugins": {
    "excat-figma@excat-extended": true,
    "forms-excat@excat-extended": true
  }
}
```

Push this file with your code. Every workspace that checks out the repository, including your team members' workspaces and new conversations, then starts with the same add-ons, without asking for them again. You can also ask EMA to change the file, or edit it in your Git repository and pull the change into the console. To turn an add-on off, set its value to `false` or remove its line. A change takes effect from your next message.

## Workspace Panel {#workspace-panel}

The workspace panel displays working content and code for the connected project, not necessarily every remote page on the site. Its view picker determines the available actions.

### Know Which Result You Are Viewing {#preview-states}

| Result | What it establishes | What remains to check |
|---|---|---|
| Console preview of workspace content | The working content renders with the current code in the console workspace. | Upload, remote authorability, and EDS preview. |
| Static design preview | A design or prototype renders. | Conversion to authorable EDS content, if required. |
| Remote authoring content | Documents in Experience Workspace or JCR pages on the AEM author instance have been saved. | Edit/save/reopen, the matching code version, and preview. |
| EDS preview site (`*.aem.page`) | Saved content renders with the code branch in that URL. | Release acceptance and publication. |
| Published site (`*.aem.live`) | The release is visible on the live destination. | Post-release checks and monitoring. |

### Content Views {#content-view}

The **Content views** show the selected page in different forms, so that you can check each aspect of the result. A collapsible file browser displays all the available page content for your site.

* **Preview** (document with magnifying glass icon) renders the selected page from the console workspace. Use it to check the page as visitors see it.
* **Document view** (document icon) shows the underlying document-based content structure. Use it to check how content is organized into sections, blocks, and default content.
* **HTML view** (code icon) shows the raw HTML. Use it to debug rendering and block decoration.
* **Markdown view (AEM authoring)** (paragraph icon) shows the underlying Markdown content structure. Use it to check the content before conversion.
* **JCR XML view (AEM authoring)** (data icon) shows the resulting JCR XML content structure. Use it to check what will be imported into the AEM author instance.

![Content view](assets/content-imported.png)

The following actions are available in the content views:

* **Refresh** icon to reload the preview panel's rendering of the console workspace copy. It doesn't fetch content from Experience Workspace; to replace the console's copies with the saved documents, use **Sync** > **Pull** > **Content**.
* **Viewport** menu to view the rendered page at **Responsive** width (the default, which fills the panel) or at a fixed **Desktop**, **Tablet**, or **Mobile** size
* **Inspect mode** (select icon) to add elements of the page to your prompt for additional context. The agent receives the selected element's HTML and its position on the page, and limits its changes to that element.
* **New window** (open in icon) to open the preview URL in a new tab (for a full desktop preview)
* **Edit in Experience Workspace** (document-based projects) opens the selected page in the Experience Workspace visual editor, the `da.live` canvas, in a new tab, previewed with the console workspace's current branch. If the page has local changes that are not yet uploaded to Experience Workspace, the console first offers **Upload & Edit**, so that you don't edit an older version. AEM authoring projects use the Universal Editor instead.
* **Delete** removes the selected page from the console workspace, one page at a time. It can't be undone, and it does not delete uploaded, previewed, or published content. See [Remove Pages](getting-started.md#remove-pages).
* **Errors** button (AEM authoring) opens a modal window to view the errors on the selected page.
* **Upload content** opens the destination-specific upload or package dialog. Check destination paths and overwrite implications before proceeding.

![Upload content](assets/upload-content.png)

After an upload to Experience Workspace (Document Authoring), the results dialog shows which files were uploaded and lets you preview, or preview and publish, the uploaded pages on the EDS preview and live sites. This runs as a tracked job: it continues if you leave the dialog, and **View Details** in the notification reopens its results. Retry failed pages from the results. If no page previews successfully, nothing is published.

Content changes made by the agent stay in the console workspace until you upload them or explicitly ask the agent to update Experience Workspace. Turning on [agent permissions](#settings-page) does not approve uploads or publication.

### Sync Menu {#sync-menu}

The **Sync** button in the workspace header shows a badge with the number of pending changes. Open it to move content and code between the console workspace and their remote locations: Experience Workspace or the AEM author instance for content, and your Git repository for code.

|Section|Item|What it does|
|---|---|---|
|**Push**|**Content**|Uploads pending pages to Experience Workspace (Document Authoring) or the AEM author instance. It does not commit anything to Git. Shows how many pages are pending, or **Up to date**, and a progress bar while pushing.|
|**Push**|**Code**|Opens **Stage changes** and then **Push changes** for the changed files; see [Changes actions](#changes-actions). Requires the [AEM Code Connector](https://github.com/apps/aem-code-connector) GitHub app; the menu offers **Install AEM Code Connector** if it is missing.|
|**Pull**|**Content**|Downloads your Experience Workspace (Document Authoring) pages over the console workspace copies, including local edits. Pages that exist only in the console workspace are kept. This cannot be undone.|
|**Pull**|**Code**|Pulls the latest code from GitHub. Unavailable while the console workspace has uncommitted files; push or discard them first.|

Sync is disabled in the demo site. Push and pull tell you when your Experience Workspace (Document Authoring) session has expired.

### Code Views {#code-view}

The **Code views** provides tools for browsing your project files and managing code changes. The view includes a file browser for an overview of your code files or changes as diffs, and a preview area for viewing the selected file or changes.

* **Files** to browse the code files in the current workspace
* **Changes** to view the diffs of files changes created by your work on the project

>[!NOTE]
>
>The file views don't show files and folders at the root of the repository whose names start with a dot, such as `.github/`, `.claude/`, or `.hlxignore`. The exceptions are `.gitignore`, `.agents/`, and folders that EMA manages. You can't stage or push changes to hidden items from the console. To change them, edit them in GitHub or in a local clone, then pull the code into the console.

![Code view](assets/code-view.png)

#### File Actions {#file-actions}

* **Add to chat** adds the selected file (or selected lines  from the file) to the chat panel for context.
* **Download** download the selected file to your local file system

#### Changes Actions {#changes-actions}  

* **Add** (+ icon) to stage the changed file
* **Discard** (arrow icon) to discard the changed file
* **Delete** (trash icon) to delete the unstaged file
* **Refresh** (refresh icon) to refresh the list of changes
* **Switch branch**: Switches branches within the same repository

To push code, use **Sync** > **Push** > **Code** in the [Sync menu](#sync-menu). The **Stage changes** dialog lets you choose the files, and the **Push changes** dialog asks for a commit message and whether to create a new pull request or push to the current branch; see [Push Code Changes](getting-started.md#push-code-changes) for what each option does. To pull the latest code, use **Sync** > **Pull** > **Code**. Code actions are unavailable in the demo site, when GitHub is not connected, or until the AEM Code Connector is installed; the console tells you which applies. Pushed code shows on that branch's preview and live URLs straight away, and merging into `main` changes the live site's code immediately. See [How Changes Go Live](overview.md#code-content-lifecycle).

Stage only the files intended for the push. Review the diff, run project checks, and choose a new PR or a current-branch push according to repository policy. Verify the resulting PR or branch commit. Pushing code does not upload content, and discarding local code does not undo remote content writes.

![Push changes](assets/push-changes.png)

Additional GitHub project actions can be performed on the [settings page](#settings-page).

### Project Views {#project-view}

The **Project views** help you plan the migration of an existing site.

* **Planning** to review and refine the templates, pages, and blocks identified by the [site catalog skill](site-catalog.md), so that you can migrate one representative page per template and validate it before you import the rest

For details, see [Site Planning UI](site-catalog.md#planning-ui).

## Settings Page {#settings-page}

The [**Settings** page](https://aemcoder.adobe.io/settings) allows you to manage basic settings of the console and is broken up into the following sections.

![Settings view](assets/settings-view.png)

If you make a change to any value in any section, click **Save** to save those changes to the individual section. For agent permissions, site authentication, and credentials, the button shows **Applying...** until the change takes effect. Click the back icon to return to your previous view.

* **Project** allows you to view and edit project settings such as managing your GitHub connection and customizing the library URL.
  * **Connect / Reconnect**: Initiates GitHub authentication
  * **Switch site**: Replaces the console workspace with a different site and repository. Any uncommitted work will be lost.
  * **Logout**: Disconnects from GitHub and revokes the agent's access to your GitHub credentials
  * **Library URL** - This URL points to a `library.json` file that defines the blocks available to authors, their variations, and example content.
  * **Site base URL** - The origin URL of the website being migrated
* **Agent permissions** - Control what the agent may access on your behalf. Each permission is off until you turn it on and save it. The agent uses a permission without receiving the credential itself. See [Security and Data Handling.](overview.md#security)
  * **Allow LLM to use my Adobe credentials for admin.hlx.page, Document Authoring, and repositories hosted outside GitHub** - In the **Adobe IMS permissions (admin.hlx.page & Document Authoring)** section. When enabled, the agent can read site configuration and metadata, read Experience Workspace (Document Authoring) content, and push to and pull from repositories hosted outside GitHub, using your Adobe credentials. `admin.hlx.page` is the EDS admin API; `hlx` comes from Helix, the project name under which the EDS architecture was developed. This does not approve publishing: EMA blocks the agent's uploads, previews, and publication when your current message doesn't ask for them. The check reads your message, so it can't catch every phrasing; limit who can publish with the site's publish role.
  * **Custom IMS Token (optional)** - Provide a token to use instead of your session token. IMS is Adobe's identity service, which issues the token for your Adobe ID session. Prefer a service account token over a personal token where possible.
  * **Allow LLM to use my git credentials** - Where available, lets the agent push to and pull from your GitHub repositories on your behalf. If you don't see this setting, it isn't available to you yet; push the agent's changes yourself with **Sync** > **Push** > **Code**. When it's on, the agent can push to any repository and branch that your GitHub credentials can write to, including `main`. Your repository's branch protection still applies. This grants elevated access; use a scoped token if offered.
* **Credentials** allows you to specify a personal access token for Figma so the [console can access design blocks for your project.](prompting-guide.md#figma-block-migration)
  * The token requires the following read-only scopes:
    * `file_content:read`
    * `file_metadata:read`
    * `library_assets:read`
    * `library_content:read`
    * `team_library_content:read`
    * `file_dev_resources:read`
    * `projects:read`
  * [See the Figma documentation](https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens) for more information about setting up personal access tokens.
* **Protected site authentication** - Configure a custom request header, HTTP Basic authentication, or bearer authentication so that the agent can read source pages that require sign-in or a secret header. See [Protected Site Authentication](#protected-site-authentication) for setup instructions.
* **Prompt coach** - Where available, controls the [prompt hints](#prompt-input) shown when a prompt is missing details, such as the page or the result you expect.
  * **Show prompt hints** turns the hints on or off.
  * Further options can check prompts on your device, which downloads a model to your browser. Turning such an option off removes the downloaded model.
* **Support** summarizes information shared with the Adobe support team when you make a support request.
  * **Request support** - Click to initiate a [support request](#request-support) without leaving the console.
* **Danger zone** contains settings that can revert your console workspace.
  * **Reset workspace** - Permanently deletes the console workspace's chat history, files, and session state, and disconnects GitHub. To confirm, you type `delete everything`. This cannot be undone. Code that you pushed and content that you uploaded stay in their remote locations, but unpushed and unuploaded work is lost. Save needed code and content first; reset is not a remote-content recovery tool.

Figma access also depends on the token owner's access to the selected file and the capability being enabled for the project. Store tokens only in credential settings, not prompts or project documentation.

### Protected Site Authentication {#protected-site-authentication}

Many sites show some pages only to signed-in visitors, keep a staging copy behind a password, or have a CDN that only lets through requests carrying a secret header. Use **Protected site authentication** to let the agent read such a source site when it accepts a custom request header, HTTP Basic authentication, or bearer authentication. You can then migrate those pages the same way as public pages.

The source site must be reachable from the agent's hosted environment on the internet and configured to accept the authentication method you provide. This feature does not provide access through a VPN, does not bypass a firewall, and does not complete interactive sign-in flows such as single sign-on (SSO) forms or multi-factor authentication. If your source is only reachable on a private network, ask its administrator for an internet-reachable staging or origin host that accepts one of the supported methods.

>[!IMPORTANT]
>
>This functionality is not intended for use with personally identifiable information (PII) or real end-user data. Use source content and test accounts that do not contain this data.

To configure access:

1. Open **Settings** in the Experience Modernization Console and find **Protected site authentication**.
1. Click **Add site**.
1. Enter the **Site hostname**, such as `staging.example.com`. Enter only the hostname, without `https://` or a URL path.
1. Select an **Authentication type** and enter the corresponding values.

   | Authentication type | Values to enter |
   | --- | --- |
   | Custom header | **Header name** and **Header value**, as required by your source website. For example, the header name might be `X-API-Key`. |
   | Basic (username & password) | **Username** and **Password** for HTTP Basic authentication. |
   | Bearer authentication | The bearer token accepted by your source website. |

1. Click **Save** in the **Protected site authentication** section. The section shows **Applying...** until the change takes effect, which can take up to about two minutes.
1. Ask the agent to scrape or migrate the source website using its URL as usual.

![Protected site authentication settings with example custom header and HTTP Basic authentication entries](assets/protected-site-authentication.png)

Once saved, credentials are added to outbound requests to the matching hostname only and are not shared with the AI model. Enter credentials only in these settings, not in chat prompts. Content retrieved from the source website is used by the agent for the requested task.

Use scoped, least-privilege credentials, preferably a dedicated account with read-only access to the source content. Each hostname can be configured only once. Configure additional hostnames separately if the source website loads protected content from other hosts, such as an asset domain.

Verify one representative protected page before you start a catalog or batch run, and check that captures show the page content rather than a sign-in page.

To remove access, click **Remove site** for the entry and then click **Save**. Remove the entry when the migration is complete.

### Request Support {#request-support}

Use **Request support** in the menu bar or on the Settings page to contact the Adobe support team.

1. Optionally choose a **Topic**, such as layout or design, missing content, or an agent that seems stuck.
1. Describe what went wrong, in up to 2,000 characters. Don't include passwords or tokens. To help support reproduce the problem, name the affected page, what you expected, what happened instead, and when.
1. Optionally select recent prompts from the conversation to attach, so that support can see what you asked.
1. Send the request.

The request shares your name, email address, session ID, project name, and preview URL with the support team. Before your console workspace is set up, it shares only your name, email address, and organization.

## What's New and Release Notes {#whats-new}

When a new version of the console is released, a **What's new** notice at the top of the page lists its highlights. Expand it to see the list, or dismiss it. It reappears for the next release.

For details of each release, see the [Experience Modernization Agent release notes.](/help/release-notes/modernization-agent/current.md)
