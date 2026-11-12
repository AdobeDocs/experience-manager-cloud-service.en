---
title: Make Visual Changes with the Experience Modernization Agent
description: How designers and other visual contributors change the look of an Edge Delivery Services site with the Experience Modernization Agent, including Inspect mode, references, Figma, and handing changes over for review.
feature: Edge Delivery Services, Agentic AI
role: User
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
---

# Make Visual Changes with the Experience Modernization Agent {#visual-changes}

This guide is for designers and others who change how a site looks: colors, fonts, spacing, and the layout of its blocks. You describe a change to the Experience Modernization Agent in the Experience Modernization Console, check it in the preview, and send it to a developer for review. The agent writes the code, so you don't need to write CSS or JavaScript. Your changes reach the site through its Git repository, though, so you need the basics: you push your work to a branch and hand it over in a pull request. If these terms are new to you, see [Words Used in This Guide](#glossary).

## Before You Start {#before-you-start}

Ask the person who leads the project for the following:

* **Access to the console.** You sign in with your Adobe ID. See [Open the Experience Modernization Console](getting-started.md#open-console).
* **The site to work on.** You connect the site's Git repository to your console workspace, and you need write access to the repository to do so. See [Connect Your Site](getting-started.md#connect-repo).
* **Your part of the work.** Agree which blocks, pages, or styles are yours, so that no one else changes the same files at the same time. See [Start with One Person, Then Divide the Work](production-migration.md#divide-work).
* **How to hand over.** Most teams protect the main branch so that a developer reviews every change. Ask whether you push with **Create new PR**. See [Hand Over for Review](#hand-over).
* **For Figma designs, a Figma seat that can read files.** See [Work from a Figma Design](#figma).

Your work stays in your own console workspace until you push it. Nothing that you try in the preview reaches the live site by itself.

>[!CAUTION]
>
>Never type or paste passwords, access tokens, or other secrets in the chat, and check screenshots and files for them before you attach them. Everything in the chat reaches the AI model, and the agent can copy it into the site's files. Your Figma token goes only in **Settings** > **Credentials**. See [Keep Secrets Out of the Chat](prompting-guide.md#secrets).

## What You Can Change {#what-you-can-change}

On an Edge Delivery Services site, authors write the content and the code decides how it looks. A visual change therefore changes the site's code, mostly its CSS, and leaves the content that authors entered as it is. You don't need to import or upload pages again.

Each part of the code reaches a different part of the site. Before you ask for a change, decide how far it should reach:

| What you change | Example request | What it affects |
|---|---|---|
| Site-wide styles | "Use our brand blue for all links and buttons." | Every page. Colors, fonts, and spacing are stored as design tokens, named values such as `--link-color` in the global styles. |
| Default content | "Increase the space below all second-level headings." | Headings, text, lists, images, and buttons outside blocks, on every page. |
| A block | "Give the cards block rounded corners and a subtle shadow." | Every page where the block appears. |
| A block variant | "Add a dark variant of the cards block." | Only the blocks that authors mark with the variant, such as **Cards (dark)**. |
| A section style | "Add a section style with a light gray background." | Only the sections that authors give that style in their section metadata. |
| A page template | "On adventure pages, show the hero image at full width." | Only the pages whose metadata names that template. |

Variants, section styles, and templates take effect only where authors apply them. Ask the agent to apply one to the page that you're working on, so that you can see it, and tell the authors when to use it.

Some requests go beyond the look of the site. Adding a field that authors fill in, changing how a block's content is structured, or adding behavior such as a carousel changes the block's content model or its logic. Describe what you need, and leave these decisions to the developer. See [Create, Update, and Refactor Blocks](block-development.md).

## Limit a Change to Some Pages {#impact}

A change to a block or to the global styles changes every page that uses them. Before you ask for one, ask the agent where the block or style is used, for example "Which pages in my workspace use the cards block?"

When a change should apply to some pages only, ask for one of these instead:

* A **block variant**, when only some instances of a block should look different.
* A **section style**, when a part of a page, such as a highlighted area, needs its own look.
* A **page template**, when a type of page, such as all product pages, needs its own look.

## Show What You Mean {#references}

A picture is often more precise than a description. Use **Attach files** (paperclip icon) in the prompt to attach:

* A screenshot of the result that you want, or of the problem, with a sentence about what to look at.
* Pages of the brand's style guide, as images or as a Word or PowerPoint file.

You can also point to a page of the site that already looks right: "Make the cards on `/adventures` look like the cards on `/magazine`." Use only designs and reference sites that your team is allowed to use.

The agent doesn't remember brand rules between conversations. Once a rule is settled, such as button styles or heading sizes, ask the agent to write it in the project's instruction files, so that it follows the rule in every conversation. See [Project Instructions and Memory](project-instructions.md#organize).

## Work from a Figma Design {#figma}

The agent can read a design from Figma through the Figma import add-on. It turns the design's colors, typography, spacing, and variables into the site's design tokens, and its components into blocks or block variants.

1. In Figma, [create a personal access token](https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens) with the read-only scopes listed in the console's [**Credentials** settings](console.md#settings-page).
1. In the console, open **Settings**, enter the token under **Credentials**, and select **Save**. A new token can take a couple of minutes to take effect.
1. In Figma, select one component or frame and copy its link. The link includes a `node-id` that identifies your selection.
1. In the console, send a prompt with the link, such as "Update the teaser block to match this Figma component: `{Figma link}`. Reuse our existing design tokens."

Things to know:

* **One component or frame at a time.** The agent builds one block from a component, or one page from a frame. Check each result before you send the next link. See [Create a Block from Figma](prompting-guide.md#figma-block-migration) and [Create a New Page from Figma](prompting-guide.md#figma-new-page-from-figma).
* **Your token, your files.** The personal access token reads every Figma file that you can open, and nothing else. Figma issues it and sets its limits. Each person stores their own token. It has nothing to do with design tokens, the colors and spacing that the agent reads from the design.
* **Your Figma seat.** You need a Dev or Full Figma seat; see [Figma and Design Systems](evaluate.md#figma). If the console reports a Figma API error with status 429, the token has reached Figma's [rate limit](https://developers.figma.com/docs/rest-api/rate-limits/).
* **The add-on.** Figma import is an [optional capability](console.md#optional-capabilities). If it isn't on for your project, the agent offers to turn it on.
* **Design tokens.** Compare the new tokens with the existing ones. Where a Figma value only differs slightly from an existing token, decide which one to keep rather than keep both.

For what your organization approves before people use Figma with the agent, see [Figma and Design Systems](evaluate.md#figma).

## Make Your First Change {#first-change}

1. Open a page in the console's preview panel.
1. In the **Viewport** menu, choose the width that you want to check: **Desktop**, **Tablet**, or **Mobile**.
1. Turn on **Inspect mode** with the select icon in the preview panel.
1. Select the element that you want to change, such as a heading, an image, or a button. The element is added to your prompt: the agent receives its HTML and its position on the page, and limits its changes to that element.
1. Describe the change and how far it should reach, then send the prompt. For example: "Make this button use our primary style, here and on every page."
1. When the agent finishes, select **Refresh preview** if the preview hasn't updated. Check the result at each **Viewport** size.
1. If something isn't right, say what you see, such as "On mobile, the text touches the image." Ask for one change at a time, and check it before you ask for the next one.

To undo a change, ask the agent to revert it. To drop all unpushed changes to a file, open the **Changes** view and select **Discard** next to the file. See [Changes Actions](console.md#changes-actions).

If the agent still doesn't get a change right after a few attempts, ask your developer, or select **Request support** in the menu bar and describe what you asked for and what you see. Your request reaches the team that builds the agent. When a conversation isn't going well, the console may also offer help under **Need a hand?** See [Request Support](console.md#request-support).

### Example Prompts {#example-prompts}

* "Make all headings use the heading font from the attached style guide."
* "Give the cards in the cards block equal height, with their buttons aligned at the bottom."
* "Add a `dark` variant of the teaser block with white text on our dark brand color, and apply it to the second teaser on `/adventures`."
* "Add a `highlight` section style with a light background and more space above and below, and use it for the newsletter section on the home page."
* "On mobile, stack the columns and put the image above the text."
* "Which pages in my workspace use the hero block? Show me how each one looks after this change."
* "Write the button styles that we agreed on into the project's instruction files."

## Check Before You Hand Over {#check}

* Check every **Viewport** size, especially **Mobile**.
* Check other pages that use the same block, style, or template, not only the page that you worked on.
* Check how the design handles real content: long headings, short ones, missing images, and lists with many items.
* Check that text stays readable against its background. You can ask the agent: "Check the color contrast of text in the teaser block against WCAG AA."
* After you push, open the preview URLs listed in the pull request and check the pages there. See [Console Preview Differs from the Site](troubleshooting.md#preview-differs).

## Hand Over for Review {#hand-over}

1. Push your code with **Create new PR**, as described in [Push Code Changes](getting-started.md#push-code-changes). Stage only the files that belong to your change, and describe it in a plain sentence, such as "Rounded corners and shadow for cards."
1. Select **View PR** in the notification, and send the pull request's link to the developer who reviews it.

To make the changes that the reviewer asks for, keep working on the same branch and push with **Push to current branch**; the pull request updates.

Your change reaches the live site when the developer merges it. If you also changed text or images on a page, that is a content change: it reaches the site only when the page is uploaded and published. Agree with the authors who does that. See [Coordinate Content Changes](production-migration.md#share-content).

## Words Used in This Guide {#glossary}

| Term | Meaning |
|---|---|
| Block | A component of a page, such as cards, a teaser, or a carousel. Each block has its own CSS and JavaScript. |
| Block variant | An alternative look of a block, which authors choose by adding a name in parentheses, such as **Cards (dark)**. |
| Default content | Headings, text, lists, images, and links that aren't in a block. |
| Section | A part of a page that groups blocks and default content. Authors can give a section a style in its section metadata. |
| Template | A type of page, such as an article or a product page, named in the page's metadata. |
| Design token | A named value for a color, font, or spacing, stored as a CSS custom property, such as `--link-color`. |
| Branch | A separate line of work in the Git repository. The live site uses the `main` branch. |
| Pull request | A request to merge your branch into another branch, which a developer reviews before merging. |
| Preview | The console's rendering of your workspace. After you push, each branch also has its own preview URL. |

Sections, blocks, and default content are explained in more depth under [Shape the Content Structure](production-migration.md#content-structure).
