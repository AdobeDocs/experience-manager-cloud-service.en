---
title: Project Instructions and Memory for the Experience Modernization Agent
description: Learn what the Experience Modernization Agent remembers, and how to give it lasting project instructions with AGENTS.md and other Markdown files in your Git repository.
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

# Project Instructions and Memory {#project-instructions}

The Experience Modernization Agent knows only what is in the current conversation and in the files of your project. To make it follow your project's conventions in every conversation, write them in Markdown files in your Git repository. This article explains how the agent uses those files and how to organize them so that it works efficiently.

Everything up to [Start a New Conversation](#new-conversation) applies to every project. [Custom skills](#custom-skills) are an advanced option that most projects don't need.

## What the Agent Remembers {#memory}

| Source | What it contains | How long it lasts |
|---|---|---|
| Built-in skills | The agent's workflows for migration, design, block development, documentation, and other tasks. | Provided by Adobe and updated with each release. |
| Current conversation | Your requests, the agent's answers, and what it read and changed. | The console keeps your project's conversation so that you can continue it. When a conversation gets long, earlier messages are summarized and details can be lost. **Clear chat** starts a new conversation without the earlier history. |
| Files in the console workspace | The checked-out Git repository, the working copy of imported content, and temporary migration files. | The workspace is a working copy. Code that you push stays in your Git repository, and content that you upload stays in your content destination. |

The agent does not keep a separate memory of your preferences or of earlier conversations. Anything that it should know in every conversation must be in a file that it reads. Because the files are in your Git repository, they also help the other developers on the project and any other AI tools that they use with it.

## Use AGENTS.md as the Entry Point {#agents-md}

`AGENTS.md` is a Markdown file at the root of the repository. It follows an [open format](https://agents.md/) that many AI coding agents read.

The agent currently uses Claude models, which load a file named `CLAUDE.md` from the repository root at the start of every conversation. The best practice, which the [AEM boilerplate](https://github.com/adobe/aem-boilerplate) follows, is a `CLAUDE.md` file with this single line:

```text
see @AGENTS.md
```

The `@` reference makes the agent load `AGENTS.md` together with `CLAUDE.md` and keep it in its context while it works. Write your project instructions in `AGENTS.md` and leave `CLAUDE.md` as this one line. Your instructions then stay in the open format that other AI tools also read, and the setup keeps working if the model behind the agent changes. That model is an implementation detail, so don't write instructions that depend on it.

Projects created from the current AEM boilerplate, for document-based content or for Experience Manager authoring, include both files, and their `AGENTS.md` contains general Edge Delivery Services coding rules. Keep both files. If your project was created before the boilerplate included them, ask the agent to add them from the current boilerplate. To check what it loaded, start a new conversation and ask which project instructions it has.

Add a short section for your project to `AGENTS.md`:

* What the site is, its source, and its [content destination](overview.md#content-storage).
* The few rules that apply to almost every task.
* An index of the other instruction files, with a note on when to read each one.

Keep `AGENTS.md` short. The agent carries all of it in every conversation, so every line takes up room that it could use for the task. Long, general text also makes it harder for the agent to tell which rules matter.

### Change How the Agent Answers {#reply-style}

How the agent writes its answers is a convention like any other, so you can set it in `AGENTS.md`. For example, if you don't want it to end each answer by suggesting next steps, or you want shorter answers, say so:

```markdown
## How to answer
- Keep answers short: what you changed, where, and anything that needs my decision.
- Don't suggest next steps unless I ask for them.
- Answer in German. Keep code, file names, and commit messages in English.
```

These instructions shape the text of the agent's answers. The suggestions that the console shows under **Next steps** are generated separately, so they still appear, and you can ignore them.

## Organize Further Instruction Files {#organize}

Put details in separate files, grouped in a folder when there are several of them. For example:

```text
AGENTS.md                    Entry point: project summary and an index of the files below
project/
  blocks.md                  Blocks, their variants, and how authors fill them
  sections-and-templates.md  Section styles and page template conventions
  design.md                  Design tokens, typography, spacing, and brand rules
  content.md                 Content, naming, URL, and asset conventions
  decisions.md               Agreed decisions, with dates and reasons
```

Reference each file from `AGENTS.md`. The agent opens a referenced file when the task needs it, so you don't need to name the file in every prompt:

```markdown
## Project Instructions

This project migrates the WKND sample site to Edge Delivery Services. Content is document-based and edited in Experience Workspace.

Read these files when the task needs them:

| File | Read when |
|---|---|
| `project/blocks.md` | Creating, changing, or using a block |
| `project/sections-and-templates.md` | Building or styling sections or page templates |
| `project/design.md` | Changing colors, typography, spacing, or other styles |
| `project/content.md` | Importing, writing, or restructuring content |
| `project/decisions.md` | Before changing an agreed convention |

When we agree on a new convention, update the matching file in the same change.
```

Follow these guidelines:

* **One topic per file.** When a file grows long, split it by topic. The agent then reads only what the current task needs and keeps more of its context for the work itself.
* **Say when to read a file.** A one-line description in the index is enough for the agent to decide.
* **Point to the code.** The code is the reference for how something is implemented. Describe the intent and the conventions, and name the file that implements them rather than copying code.
* **No secrets.** These files are part of your repository. Never put passwords, tokens, or other credentials in them.

Edge Delivery Services serves files that are committed to the repository unless they are excluded in the `.hlxignore` file. The AEM boilerplate's `.hlxignore` excludes Markdown files and files whose names start with a dot. Write instruction files in Markdown so that they stay excluded; files in other formats, such as JSON or plain text, could otherwise be requested from the site's URLs. The console doesn't show `.hlxignore`, so if you need to change it, edit it in GitHub or in a local clone.

## Document Content Conventions {#content-conventions}

Authors work best with lean content structures: a heading, some text, an image, and a link, without extra fields. To keep the content that simple, the implementation relies on conventions, such as which content is optional or how the position of an element changes its role. Authors, developers, and the agent can only follow those conventions if they are written down. [David's Model](https://www.aem.live/docs/davidsmodel) describes the general rules for such structures; reference it from your content conventions and write down only your project's own decisions.

Conventions that are worth documenting include:

* **Content variations of a block.** For a teaser, for example: whether the image and the call to action are optional, how authors choose a larger or smaller title, and whether a short paragraph before the title becomes an eyebrow, a small label above the title.
* **Block variants.** Which variants exist and when to use each one.
* **Section styles.** Which [section](overview.md#eds-basics) styles exist, such as a dark background or a narrow column, what they do, and which blocks work inside them. Some sections may expect a specific block to achieve a particular effect.
* **Page templates.** Content conventions that pages of a template must follow, for example an article page that starts with a hero and ends with related links.
* **Coding, design, and content rules.** Naming, design tokens, brand rules, URL and asset conventions, and anything else that a new team member would need to know.

An entry for one block can be as short as this:

```markdown
### Teaser

Promotes one page or offer.

| Content | Required | Convention |
|---|---|---|
| Image | No | Without an image, the text spans the full width. |
| Eyebrow | No | A short paragraph before the heading becomes the eyebrow. |
| Title | Yes | Heading 2 for the standard size, Heading 3 for a compact teaser. |
| Text | No | One or two short paragraphs. |
| Links | No | A bold link becomes a primary button, an italic link a secondary button. |

Variants: `dark` (light text on a dark background).
Works in sections: default, `dark`, and `narrow`.
```

When migration creates a block, the agent also writes a README for developers and an authoring guide for authors. See [What the Agent Provides With a Block](block-development.md#block-deliverables). Reference those files from your index rather than repeating them.

## Let the Agent Maintain the Files {#maintain}

You don't need to write these files by hand. Ask the agent to create and update them, then review them as you would review code.

* **Create the first version** once the first templates and blocks exist:

  > Document this project's blocks, variants, section styles, page templates, and design tokens from the code and the imported content. Put each topic in its own short file under `project/`, and add an index with when to read each file to `AGENTS.md`.

* **Keep them current.** Add a standing rule to `AGENTS.md`, such as the last line of the example above, so that the agent updates the files whenever it creates or changes a block, section style, or template.
* **Check them.** The agent can record a convention that it assumed rather than one that you agreed. Correct anything that is wrong, and ask from time to time:

  > Check the files under `project/` against the current code and content. Fix statements that are out of date, and split any file that has grown too long.

* **Push them with the code** so that your team and future conversations get the same instructions.

## Leave a Record of Each Request {#trace}

The console keeps no audit log of the agent's actions. What the agent produces reaches your site through your Git repository or Adobe Experience Manager, so your Git history and the version history of your content are the record. See [Trace What the Agent Did](evaluate.md#audit-trail). To make that record easy to follow, add a standing rule to `AGENTS.md` so that each request leaves its own commit and content upload:

```markdown
## After Each Request

- Commit your changes with a message that summarizes my request.
- Push the commit to the `develop` branch. Never push to `main`.
- If pages changed, list them and ask whether to upload them to Experience Workspace.
```

* **Pushing** needs **Allow LLM to use my git credentials**, or the Adobe credentials permission for repositories connected through Cloud Manager. See [Settings Page](console.md#settings-page). If the permission isn't available to you, push yourself with **Sync** > **Push** > **Code** after each request.
* **Uploading** needs the Adobe credentials permission. The console lets the agent upload content only when your message asks for it or you agree when it asks, so the rule has the agent ask, and your answer approves the upload. For content on the author instance, upload the pages yourself.
* **The working branch** keeps the agent's pushes away from the live site's code. A developer reviews the changes and merges them into `main` with a pull request, as described in [Broader Contribution, Same Production Control](overview.md#production-control).

## Start a New Conversation {#new-conversation}

Because the agent loads `AGENTS.md` automatically, a new conversation starts with your project instructions, and it finds the other files through the index. Start a new conversation with **Clear chat** when a conversation has become long or has drifted from the task. Before you clear it, ask the agent to save what matters:

> Before I clear the chat, record the decisions and conventions that we agreed in this conversation in the project files, and list what you changed.

Clearing removes the earlier messages and can't be undone. To keep the conversation, select **Download chat** first.

For a full handover to another person or team, see [Retain Context for People and Agents](project-documentation.md#portable-handoff).

## Advanced: Custom Skills {#custom-skills}

Most projects don't need custom skills. The agent's built-in skills cover migration, design, block development, and documentation, and they improve with each release. See the [release notes](/help/release-notes/modernization-agent/current.md).

A skill is a set of instructions for one kind of task, often step by step. It works like a section of `AGENTS.md`, with one difference: the agent reads a skill only when it performs that task, instead of carrying it in every conversation. Consider a custom skill when:

* Instructions for one recurring task make `AGENTS.md` long.
* The agent keeps struggling with a specific, repeated task and needs precise steps, for example extracting images from an unusual gallery on the source site or handling embedded videos.

To add a custom skill:

1. Ask the agent to create the skill in its own folder under `.claude/skills/`, such as `.claude/skills/gallery-images/SKILL.md`. The file starts with a short header that gives the skill a `name` and a `description` of when to use it. The steps, the checks that show the task succeeded, and a short example follow.
1. Push the skill. The console's file views hide folders whose names start with a dot and can't stage them, so ask the agent to commit and push the skill, with **Allow LLM to use my git credentials** turned on in [**Settings**](console.md#settings-page). Without that permission, add the file in GitHub or in a local clone, then pull the code into the console.
1. Test the skill in a new conversation. Ask for it by name, such as "Use the gallery-images skill to import this page". To check that the agent found it, ask it to read the skill and tell you its name and description. A list of the agent's skills covers its built-in skills, so it doesn't show whether yours loaded.

The header of `SKILL.md` looks like this:

```markdown
---
name: gallery-images
description: Extract the images of the source site's photo galleries, which a script loads. Use when importing pages that contain a gallery.
---
```

You don't need to list the skill in `AGENTS.md`. The agent sees the description of every skill in the folder and reads a skill when a task matches it, so describe precisely when to use it.

A good way to write a skill is to ask the agent for it right after it has completed the task correctly:

> Write a skill in `.claude/skills/gallery-images/SKILL.md` that captures how you just extracted the gallery images, including the checks you used. Then commit and push it.

Custom skills don't replace or change the agent's built-in skills. When a new release handles a task natively, remove the custom skill that covered it.

### Why .claude/skills {#skills-location}

Claude-based agents, like the one that the console currently runs, discover skills on their own in a `.claude/skills/` folder at the root of the repository. A skill there loads natively: the agent sees only the skill's short description until a task matches it, can be asked for it by name, and applies settings from the skill's header, such as which tools it may use. This works more reliably than a visible folder such as `skills/` that `AGENTS.md` indexes, where the agent has to read the index and decide to open the file.

The folder's name starts with a dot, which has two effects:

* Your site doesn't serve it. The AEM boilerplate's `.hlxignore` file excludes files and folders whose names start with a dot.
* The console's [file views](console.md#code-view) don't show it. To review a skill, ask the agent to show it, or open it in GitHub.

If your project already has skills in a visible folder that `AGENTS.md` indexes, they keep working. To have them load natively, ask the agent to move them to `.claude/skills/`, add the header, and remove the index lines.
