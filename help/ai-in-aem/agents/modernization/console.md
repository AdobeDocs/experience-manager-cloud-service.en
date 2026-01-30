---
title: Experience Modernization Console
description: Reference guide for the Experience Modernization Console interface and capabilities
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
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
>If you are interested in getting started right away with the console, check out the document [Getting Started with the Experience Modernization Agent.](/help/ai-in-aem/agents/modernization/getting-started.md)

## Capabilities {#capabilities}

Core capabilities of the console:

* Interactive chat panel with the agent and its skills
* Live AEM preview for immediate visual feedback on changes
* Content file browser and markdown viewer
* Content synchronization with [Document Authoring](https://da.live)
* Code browser and diff viewer for reviewing changes made
* GitHub integration with ability to create pull requests from changes

Developers retain full control over what ships. All changes made through the console require review and approval before deployment, ensuring governance, brand consistency, and security.

## Navigation {#navigation}

After signing into the console at [`aemcoder.adobe.io`,](https://aemcoder.adobe.io) you arrive on the home screen of the console.

![Home screen of console](assets/console-home.png)

### Menu Bar {#menu-bar}

The top menu bar provides:

* An **Open menu** button on the left to expand and collapse the detail of the left side panel
* An **Account** button on the right for switching to dark mode and signing out of the console

### Left Sidebar {#sidebar}

The left sidebar allows quick access to important views of the console.

* **[Home View](#home-view)** (house icon) - Your starting point for using the console
* **[Content View](#content-view)** (file icon) - Content that you have imported
* **[Code View](#code-view)** (`</>` icon) - Code of the site that you are working on
* **[Settings View](#settings-view)** (gear icon) - Settings of the console

## Home View {#home-view}

The **Home** view is your starting point for using the console. 

* At the top is a [prompt panel](#prompt-panel) for making requests of the console.
* Below the prompt panel are suggested prompts to use to start your project.

### Prompt Panel {#prompt-panel}

The prompt panel provides controls for interacting with the AI.

* **Plan / Execute modes** (light bulb and magic wand icons): Toggle between planning and execution modes, respectively
  * **Plan mode**: The AI analyzes requests and outlines an approach without making changes, which is useful for understanding strategy before committing.
  * **Execute mode**: The AI carries out the plan and makes actual file changes.
* **Attach files** (paperclip icon): Upload and attach files to the prompt for additional context (e.g. reference designs, screenshots, specs)
* **Settings** (gear icon): Choose to skip confirmation questions from the AI
* **Clear chat**: This resets the conversation and clears the AI's context window. Use this option when starting a new task unrelated to the previous conversation.

## Content View {#content-view}

The **Content view** provides tools for browsing and previewing content. By default the view is split into three panels, left-to-right:

* Prompt panel for interacting with the console and project
* File browser for an overview of your content files (toggle showing this panel with the chevron icon)
* Preview panel for visualizing content selected in the file browser

![Content view](assets/content-imported.png)

The preview panel offers three modes:

* **Preview** (document with magnifying glass icon) to view the rendered HTML content 
* **HTML view** (document icon) to view the underlying document authoring content structure, respectively
* **Design mode** (paintbrush icon) to select elements of the page for context for your prompt

You can always click the **Refresh preview** icon to update the preview panel.

The **Upload content** button opens a modal window to upload files to AEM Document Authoring.

* **Organization** and **Repository** field are prepopulated if your project has an `fstab.yaml` file
* File selection provides editable target paths
* Upload to JCR (for Universal Editor) is not supported

![Upload content](assets/upload-content.png)

## Code View {#code-view}

The **Code view** provides tools for browsing code and managing code changes. The view is split into three panels, left-to-right:

* Prompt panel for interacting with the console and project
* File browser for an overview of your code files or changes as diffs
* Preview panel for viewing a code file or diff selected in the file browser

![Code view](assets/code-view.png)

The preview panel offers two different modes:

* **Workspace files** to browser the code files in the current workspace
* **Git Changes** to view the diffs of files changes created by your work on the project
  * Click the `+` icon to stage the changed file
  * Click the arrow icon to discard the changed file

The **Information** icon lists your currently connected GitHub account and project.

The **GitHub actions** menu (top right) provides repository operations.

* **Connect / Reconnect**: Initiates GitHub OAuth
* **Switch Repository**: Replaces the workspace with a different repository. Any uncommitted work will be lost.
* **Switch Branch**: Switches branches within the same repository
* **Sync**: Pulls the latest changes from the remote origin
* **Push**: Opens a modal to push workspace changes to GitHub
* **Logout**: Disconnects from GitHub

When pushing changes, you must have first staged changes to include in the push. When pushing you can choose to create a new PR or push directly to the current branch

![Push changes](assets/push-changes.png)

## Settings View {#settings-view}

The settings view allows you to manage basic settings of the console.

![Settings view](assets/settings-view.png)

* **Credentials** allows you to specify a personal access token for Figma so the console can access design blocks for your project.
* **Reset workspace** reverts the console to its starting state and all un-pushed or un-uploaded changes will be lost.
