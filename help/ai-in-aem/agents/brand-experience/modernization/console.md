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

Reference guide for the Experience Modernization Console interface and capabilities

>[!NOTE]
>
>If you are interested in using the Experience Modernization Console, you can request access to ensure a smooth onboarding experience.

## Overview {#overview}

The Experience Modernization Console is a hosted, AI-assisted development environment for Edge Delivery Services, exposed as a web interface at [`aemcoder.adobe.io`.](https://aemcoder.adobe.io) After connecting to their GitHub project, you can immediately start prompting changes in natural language without any further setup or local environment configuration.

>[!TIP]
>
>If you are interested in getting started right away with the console, check out the document [Getting Started with the Experience Modernization Agent.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md)

## Capabilities {#capabilities}

Core capabilities of the console:

* Interactive chat panel with the agent and its skills
* Workspace and site previews for visual feedback on changes
* Content file browser and markdown viewer
* Content upload to [Document Authoring](https://da.live) or package creation and upload for [AEM authoring](getting-started-aem-authoring.md#upload-content), according to project configuration
* Code browser and diff viewer for reviewing changes made
* GitHub integration with ability to create pull requests from changes

Review changes before saving to a shared destination. The console can push to a new pull request or directly to the current branch; repository protections determine which changes require approval. Content uploads write to the authoring destination separately from code push. Optional planning is not an enforced approval gate for every operation.

For complete procedures, choose [trial or demo](getting-started.md#first-outcome), [production migration](production-migration.md), [restyling](restyling.md), or [block development](block-development.md).

## Navigation {#navigation}

After signing into the console at [aemcoder.adobe.io,](https://aemcoder.adobe.io) use the [home page](#home-page) to start work or continue in the [chat page](#chat-page). Confirm the active project and branch before making changes.

![Home screen of console](assets/console-home.png)

### Menu Bar {#menu-bar}

The top menu bar provides:

* An **Adobe Experience Manager** title on the left that links to the Home Page when clicked
* A **Request support** button where you can send details of any issues that were encountered
* An **Account** button on the right for switching to dark mode and signing out of the console

## Home Page {#home-page}

The **Home** page is your starting point for using the console.

* At the top is a [prompt input](#prompt-input) for making requests of the console.
* Below the prompt panel are suggested prompts for getting started with your project.
* A **Start chatting** button that takes you to the [chat page](#chat-page).
* A **Settings** button to access the [project settings](#settings-page) page

### Prompt Input {#prompt-input}

The prompt input provides controls for interacting with the AI.

* **Plan / Execute modes** (light bulb and magic wand icons): Toggle between planning and execution modes, respectively
  * **Plan mode**: The AI analyzes requests and outlines an approach without making changes, which is useful for understanding strategy before committing.
  * **Execute mode**: The AI performs the request and can make actual file changes.
  * Planning is optional. Before execution, state the allowed scope and whether upload, push, or publication is authorized.
* **Attach files** (paperclip icon): Upload and attach files to the prompt for additional context (e.g. reference designs, screenshots, specs)
* **Prompt queue** (clock icon): Additional prompts can be queued up to be automatically executed once the current prompt has completed.

## Chat Page {#chat-page}

The [**Chat** page](https://aemcoder.adobe.io/chat) is the main interface for interacting with Experience Modernization agent. This page is split into a resizable [chat panel](#chat-panel) and [workspace panel.](#workspace-panel)

## Chat Panel {#chat-panel}

The chat panel allows you to view and continue your conversation with the Experience Modernization agent. The chat panel includes the chat message history and a [prompt input](#prompt-input) for making additional requests of the console.

The chat panel header includes links for navigating to the [Home](#home-page) and [Settings](#settings-page) views and chat actions.

* **Chat actions**
  * **Clear chat**: This resets the conversation and clears its context. It is not a code or content rollback. Save important decisions in [project context](project-documentation.md#portable-handoff) before clearing.
  * **Download chat**: This downloads the conversation history as a markdown file.

## Workspace Panel {#workspace-panel}

The workspace panel displays working content and code for the connected project, not necessarily every remote page on the site. Its view picker determines the available actions.

### Know Which Result You Are Viewing {#preview-states}

| Result | What it establishes | What remains to check |
|---|---|---|
| Workspace content preview | The local working content renders with the current workspace code. | Upload, remote authorability, and branch preview. |
| Static design preview | A design or prototype renders. | Conversion to authorable EDS content, if required. |
| Remote authoring content | Documents or JCR pages have been saved to the target. | Edit/save/reopen, the matching code version, and preview. |
| EDS preview | Saved content renders with the code branch in that URL. | Release acceptance and publication. |
| Published site | The release is visible on the live destination. | Post-release checks and monitoring. |

### Content Views {#content-view}

The **Content views** contain multiple modes for displaying the selected page content. A collapsible file browser displays all the available page content for your site.

* **Preview** (document with magnifying glass icon) to view the rendered HTML content
* **Document view** (document icon) to view the underlying document authoring content structure, respectively
* **HTML view** (code icon) to view the raw plain html
* **Markdown view (AEM authoring)** (paragraph icon) to view the underlying markdown content structure
* **JCR XML view (AEM authoring)** (data icon) to view the resulting JCR XML content structure

![Content view](assets/content-imported.png)

The following actions are available in the content views:

* **Refresh** icon to update the preview panel rendering.
* **Responsive mode** to view the rendered HTML content in a desktop, tablet, or mobile view
* **Inspect mode** (select icon) to add elements of the page to your prompt for additional context
* **New window** (open in icon) to open the preview URL in a new tab (for a full desktop preview)
* **Delete** removes the selected page from the workspace. It does not delete remote previewed or published content.
* **Errors** button (AEM authoring) opens a modal window to view the errors on the selected page.
* **Upload content** opens the destination-specific upload or package dialog. Check destination paths and overwrite implications before proceeding.

![Upload content](assets/upload-content.png)

### Code Views {#code-view}

The **Code views** provides tools for browsing your project files and managing code changes. The view includes a file browser for an overview of your code files or changes as diffs, and a preview area for viewing the selected file or changes.

* **Files** to browse the code files in the current workspace
* **Changes** to view the diffs of files changes created by your work on the project

![Code view](assets/code-view.png)

#### File Actions {#file-actions}

* **Add to chat** adds the selected file (or selected lines  from the file) to the chat panel for context.
* **Download** download the selected file to your local file system

#### Changes Actions {#changes-actions}  

* **Add** (+ icon) to stage the changed file
* **Discard** (arrow icon) to discard the changed file
* **Delete** (trash icon) to delete the unstaged file
* **Refresh** (refresh icon) to refresh the list of changes
* **Switch Branch**: Switches branches within the same repository
* **Sync**: Pulls the latest changes from the remote origin
* **Push**: Opens a modal to push workspace changes to GitHub

Stage only the files intended for the push. Review the diff, run project checks, and choose a new PR or a current-branch push according to repository policy. Verify the resulting PR or branch commit. Pushing code does not upload content, and discarding local code does not undo remote content writes.

![Push changes](assets/push-changes.png)

Additional GitHub project actions can be performed on the [settings page](#settings-page).

### Project Views {#project-view}

The **Project views** help you plan the migration of an existing site.

* **Planning** to review and refine the templates, pages, and blocks identified by the [site catalog skill](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md)

For details, see [Site Planning UI](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md#planning-ui).

## Settings Page {#settings-page}

The [**Settings** page](https://aemcoder.adobe.io/settings) allows you to manage basic settings of the console and is broken up into the following sections.

![Settings view](assets/settings-view.png)

If you make a change to any value in any section, click **Save** to save those changes to the individual section. Click the back icon to return to your previous view.

* **Project** allows you to view and edit project settings such as managing your GitHub connection and customizing the library URL.
  * **Connect / Reconnect**: Initiates GitHub authentication
  * **Switch Repository**: Replaces the workspace with a different repository. Any uncommitted work will be lost.
  * **Logout**: Disconnects from GitHub
  * **Library URL** - This URL points to a library.json file that defines available blocks, their variations, and example content.
  * **Site base URL** - The origin URL of the website being migrated
* **Agent permissions** - Allow agent to access configuration options
  * **Allow LLM to access admin.hlx.page on my behalf** - When enabled, the AI assistant can fetch site configurations and metadata from Adobe Experience Manager using your IMS credentials.
  * **Custom IMS Token** - You can provide a custom IMS token to use instead of your default session token.
* **Credentials** allows you to specify a personal access token for Figma so the [console can access design blocks for your project.](/help/ai-in-aem/agents/brand-experience/modernization/prompting-guide.md#figma-block-migration)
  * The token requires the following read-only scopes:
    * `file_content:read`
    * `file_metadata:read`
    * `library_assets:read`
    * `library_content:read`
    * `team_library_content:read`
    * `file_dev_resources:read`
    * `projects:read`
  * [See the Figma documentation](https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens) for more information about setting up personal access tokens.
* **Support** summarizes information shared with the Adobe support team when you make a support request.
  * **Request support** - Click to initiate a request for support from Adobe without leaving the console.
* **Danger zone** contains settings that can revert your workspace.
  * **Reset workspace** - Resets the workspace to its initial state. This cannot be undone. Save needed code and content first; reset is not a remote-content recovery tool.

Figma access also depends on the token owner's access to the selected file and the capability being enabled for the project. Store tokens only in credential settings, not prompts or project documentation.
