---
title: Experience Modernization Console
description: Reference guide for the Experience Modernization Console interface and capabilities
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
---

# Experience Modernization Console {#console-reference}

The Experience Modernization Console is a hosted, AI-assisted development environment for Edge Delivery Services, exposed as a web interface at [`aemcoder.adobe.io`.](https://aemcoder.adobe.io) After connecting to their GitHub project, you can immediately start prompting changes in natural language without any further setup or local environment configuration.

>[!NOTE]
>
>If you are interested in using the Experience Modernization Console, you can request access to ensure a smooth onboarding experience.

Core capabilities of the console:

* Interactive chat panel with the agent and its skills
* Live AEM preview for immediate visual feedback on changes
* Content file browser and markdown viewer
* Content synchronization with [Document Authoring](https://da.live)
* Code browser and diff viewer for reviewing changes made
* GitHub integration with ability to create pull requests from changes

Developers retain full control over what ships. All changes made through the console require review and approval before deployment, ensuring governance, brand consistency, and security.

## Prompt Panel {#prompt-panel}

The prompt panel on the left side of the interface provides controls for interacting with the AI.

* **Plan / Execute modes** (light bulb and wizard icons): Toggle between planning and execution modes, respectively
  * **Plan mode**: The AI analyzes requests and outlines an approach without making changes, which is useful for understanding strategy before committing.
  * **Execute mode**: The AI carries out the plan and makes actual file changes.
* **Attach files** (paperclip icon): Upload and attach files to the prompt for additional context (e.g. reference designs, screenshots, specs)
* **Clear chat**: This resets the conversation and clears the AI's context window. Use this option when starting a new task unrelated to the previous conversation.

## Content View {#content-view}

The **Content view** (file icon in the left sidebar) provides tools for browsing and previewing content.

* **Expand / Collapse file browser** (chevrons): Toggle the file browser panel
* **Preview / HTML toggle** (preview and HTML icons): Switch between viewing the rendered HTML preview and the underlying document authoring content structure, respectively
* **Upload content**: Opens a modal to upload files to AEM Document Authoring
  * Includes destination fields (organization, repository), file selection, and editable target paths
  * Upload to JCR (for Universal Editor) is not yet supported

## GitHub Commands {#github-commands}

The GitHub icon menu (top right in Code view) provides repository operations.

* **Connect / Reconnect**: Initiates GitHub OAuth
* **Switch Repository**: Replaces the workspace with a different repository. Any uncommitted work will be lost.
* **Switch Branch**: Switches branches within the same repository
* **Sync**: Pulls the latest changes from the remote origin
* **Push**: Opens a modal to push workspace changes to GitHub
  * Choose to create a new PR or push directly to the current branch
  * Untracked files must be staged first (click the "+" button next to the file).
* **Logout**: Disconnects from GitHub
