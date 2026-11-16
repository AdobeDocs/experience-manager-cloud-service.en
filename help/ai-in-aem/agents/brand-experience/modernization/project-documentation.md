---
title: Generate Project Documentation with the Experience Modernization Agent
description: Generate guides for authors, developers, and administrators from your project's code and site configuration, and keep a handover file that people and agents can use.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: 111cc47d-085f-4cf4-81bc-332e6a31bbeb
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
# Generate Project Documentation {#project-documentation}

The Experience Modernization Agent writes guides for the people who work on your site: authors, developers, and administrators. It builds them from the project's code and, with your permission, from the site's configuration, and delivers them as PDFs that you can give to a team that takes over the project.

## What the Guides Cover {#project-handovers}

* **Project walkthrough:** how the project is set up and structured, and the conventions it follows.
* **Code organization:** how the blocks, modules, and components are organized and how they relate to each other.
* **Role-based guides:** a guide each for authors, developers, and administrators.

The guides describe what the agent can read: the code in your console workspace and, with permission to use your Adobe credentials, the site configuration from the admin API. Systems that it can't read, such as integration or CDN configuration, aren't covered.

## Prerequisites {#prerequisites}

* Your project is checked out in your console workspace.
* Project documentation is an [optional capability](console.md#optional-capabilities). If it isn't on for your project, the agent offers to turn it on when you ask for documentation, and asks you to confirm.
* To include the site configuration, you need admin access to the site, and **Allow LLM to use my Adobe credentials for admin.hlx.page, Document Authoring, and repositories hosted outside GitHub** turned on in [Settings](console.md#settings-page). The permission covers the admin API and Experience Workspace, not the Java Content Repository (JCR) of an author instance. Without it, the agent documents the code only. Ask it to list the configuration and content that it couldn't inspect, so that readers know what the guides leave out.

## Create the Documentation {#creating-documentation}

1. Ask the agent `Create documentation for this project`. Say who the guides are for, where authors edit content (Experience Workspace or the Universal Editor), and what you know about the project that the code doesn't show.
1. Provide the project's organization name if the agent asks for it.
1. When the agent asks which documentation to create, select **All**, or the guides that you need.

   ![Create documentation](assets/select-documentation.png)

1. The agent places the guides in your console workspace. Select one to view its description, then select its link to download the PDF.

   ![Documentation created](assets/documentation-created.png)

Before you share a guide, check its setup steps, content locations, commands, authoring steps, and stated limitations against the project. For document-based projects, you can also upload the PDFs with the other content in Experience Workspace.

![Admin guide](assets/admin-guide.png)

## Retain Context for People and Agents {#portable-handoff}

The PDFs describe the project at one point in time. To keep the context that the next person or conversation needs, keep a short Markdown handover file in the project's Git repository. The console doesn't generate this file; you and the agent write it.

Include:

| What | Useful detail |
|---|---|
| Project identity | Repository and branch, source URLs, [where content is stored](overview.md#content-storage), the editor that authors use (Experience Workspace or the Universal Editor), and the preview and live URLs. |
| Decisions | Agreed scope, the design reference and its version, how source content maps to blocks, project conventions, and what must not change. |
| Checked examples | Source and output paths, block examples that authors can edit, model and variant instructions, and whether authors could edit, save, and reopen them. |
| State | What exists only in the console workspace, what was uploaded, what code was pushed, and what was previewed or published. |
| Quality and gaps | Checks that were run and their results, coverage, failed or skipped pages, unfinished integrations, and who signs off. |
| Next step and recovery | The remaining task, the permissions and dependencies it needs, how to recover code, and how to recover content and assets, which is a separate process. |

For Experience Manager authoring, also record model and configuration changes, the site and DAM destinations, package import results, and what you checked in the Universal Editor. For document-based content, record where the documents are stored and any decisions about transferring or overwriting them.

Reference the file from `AGENTS.md`, so that the agent finds it when a task needs it. See [Use AGENTS.md as the Entry Point](project-instructions.md#agents-md). Never include tokens, passwords, or other secrets.

Date the file and update it when the code, models, content, or deployment change. Generated PDFs and earlier conversations go stale; neither shows what is live now.

## Troubleshooting {#troubleshooting}

When generation fails, fix the cause below, then generate the affected guide again and check it.

### "Access Denied", "Unauthorized", or "Config API Error" {#unauthorized}

The agent can't read the site configuration through the admin API. Check that you have admin access to the site and that the credentials setting in the [prerequisites](#prerequisites) is on. If you don't need the configuration, ask for code-only guides instead.

### "Project Not Found" {#not-found}

The project's repository isn't checked out in your console workspace. Connect it as described in [Connect Your Site](getting-started.md#connect-repo).
