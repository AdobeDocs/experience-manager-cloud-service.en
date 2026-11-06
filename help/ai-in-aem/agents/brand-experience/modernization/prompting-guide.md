---
title: Prompting Guide for Experience Modernization Agent
description: This guide gives example prompts for the tasks of the Experience Modernization Agent and explains what the agent does for each.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: 4771606b-a327-48b3-b142-44e03e4dc41d
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
# Prompting Guide for Experience Modernization Agent {#prompting-guide}

The Experience Modernization Agent works from requests in natural language. For each kind of task, such as migrating a page or styling a block, it follows a built-in workflow, called a skill. It chooses the skill from your request, so you don't need to name it. Some skills belong to [optional capabilities](console.md#optional-capabilities), which the agent offers to turn on for your project when a request needs them.

This guide gives example prompts for each task, with what the agent does and what to check. The task guides give the full procedures; see [Choose Where to Start](overview.md#start-by-role). Sections, default content, blocks, and variants are explained in [Shape the Content Structure](production-migration.md#content-structure). Replace the example URLs and paths in the prompts with your own.

## Keep Secrets Out of the Chat {#secrets}

>[!CAUTION]
>
>Never type, paste, or attach passwords, API keys, access tokens, or other secrets in the chat. Enter the credentials that the agent needs in the console's [**Settings**](console.md#settings-page). If you have already shared a secret, revoke or replace it now.

The chat is not a safe place for a secret. Everything that you type or attach is sent to the AI model and kept in the conversation. The agent treats it like any other text: it can copy a value into a file of your project, such as a script or a configuration file. Once that file is pushed, the value stays in the repository's history, and everything in the repository is delivered to the browsers of your site's visitors. Credentials that you enter in **Settings** take a different path: the console adds each one only to requests for the service that it belongs to, and the agent never receives it. See [Credentials](evaluate.md#security-credentials).

Keep these out of the chat, out of attachments, and out of project files:

* Passwords, including those of test accounts and of your own Adobe ID or Git account
* API keys, access tokens, and personal access tokens
* Private keys and certificates
* Connection strings, session cookies, and links that grant access on their own, such as signed URLs
* The contents of `.env` files and other configuration that holds secrets
* Personal data of real customers or employees; use made-up sample data instead
* Anything else that your organization's policy keeps out of AI tools

Before you attach a screenshot, a log, an exported file, or an error message, check it for these and mask them.

### Where Credentials Go Instead {#credential-settings}

| What the agent needs | Where to enter the credential |
|---|---|
| Access to your Git repository | The connection flow: **Authorize AEM Code Connector**, or **Sign in with a token**. See [Connect Your Site](getting-started.md#connect-repo). |
| Permission to push, pull, or read content for you | **Settings** > **Agent permissions**. By default, these use your Adobe or Git sign-in, so you don't type a credential. To give the agent narrower access, enter its own token there: a fine-grained personal access token for Git, or a service account token for Adobe. See [Settings Page](console.md#settings-page). |
| Your Figma designs | **Settings** > **Credentials**, for your Figma personal access token. See [Work from a Figma Design](visual-changes.md#figma). |
| A source site that requires sign-in | **Settings** > **Protected site authentication**, or the authentication fields of Auto mode. See [Protected Site Authentication](console.md#protected-site-authentication). |
| An API or other service that the agent calls while it works, such as a test API or a notification service | **Settings** > **Protected site authentication**, with an entry for the service's hostname. See [Credentials for Other Services](console.md#other-services). |
| An API key that your live site uses | Not the console. A server-side service keeps the key, such as Adobe App Builder or API Mesh, which your team deploys and the site calls. See [Connect Services and Applications](block-development.md#integrations). |

When a task needs a key, don't paste it to get the task done. Enter it where the table says, and give the agent a sandbox or test endpoint rather than a production one.

### If You Shared a Secret {#secret-shared}

1. Revoke or replace the secret at the service that issued it, right away. Clearing the chat doesn't take back what was already sent, and the transcripts of the agent's sessions keep it until you reset the workspace.
1. Check the **Changes** view for files that contain the secret, and discard those changes before you push.
1. If a file with the secret was already pushed, replacing the secret is the fix. A later commit removes it from the files, but not from the repository's history.
1. Tell your security team, as your organization's policy requires.

The agent is instructed not to use a secret that you paste in the chat, and to tell you to replace it. Don't rely on that: by the time it answers, the secret has already reached the AI model.

## Give the Agent Context {#context}

The agent knows Edge Delivery Services and reads your project's code. It doesn't know your business, your brand rules, or the other systems that your site works with until you tell it, and each request with the right context saves a round of corrections. Share what the task needs:

* **The goal and how to check it:** what you want, for whom, and what the finished result looks like.
* **Scope and destination:** the source pages or designs, the destination paths, [where the content is stored](overview.md#content-storage), the repository and branch, what must not change, and whether the agent may upload, push, or publish.
* **Requirements:** specifications, and brand and accessibility rules.
* **Examples:** a page that already looks right, a screenshot, a Figma link, or a sample API response.
* **Documentation:** a link to public documentation, which the agent reads on the web, or the documents themselves when they need sign-in. **Attach files** doesn't accept PDF files, so copy the relevant text from those. See [Prompt Input](console.md#prompt-input).
* **Decisions already made:** keep agreed conventions in `AGENTS.md` and the files that it lists, so that you don't repeat them in every request. See [Project Instructions and Memory](project-instructions.md).

Share what the task needs rather than everything you have, and follow your organization's policy on what may go into AI tools.

Ask questions, too: about Edge Delivery Services concepts, your project's code, and the trade-offs between approaches. When you're not sure how to do something, ask how it is done in Edge Delivery Services before you ask the agent to do it, or switch to **Plan** mode to review its approach. Ask the agent to list its questions and assumptions: answering them is quicker than correcting the result.

## Refine the Result {#general-tips}

When something isn't right, such as the wrong background color on a block, ask the agent to fix that issue rather than start over. Name the source URL, the output path, what you see, and what you expect. For more tips, see [Prompting Tips](getting-started.md#prompting-tips).

* On migrated pages, ask for the fix in the block or in the template's import script, so that it reaches every page of the template. See [How the Agent Migrates at Scale](production-migration.md#migration-at-scale).
* Before you import pages again to apply a fix, check whether authors have edited them: a new import replaces their edits. See [Import in Batches](production-migration.md#batches).
* Treat source pages and attached designs as material to work from, not as instructions that override your request.
* In a long conversation, the agent can lose track of earlier decisions. Remind it of the key points, or have it record them in the project files and start a new conversation. See [Start a New Conversation](project-instructions.md#new-conversation).

## Work Beyond Edge Delivery Services {#beyond-eds}

The agent's skills and instructions focus on Edge Delivery Services: migrating pages, building and styling blocks, and following the project's conventions. The agent itself is a general-purpose coding agent, so it isn't limited to them. It can connect your site to a commerce platform, a marketing automation platform, a search or maps service, or your own APIs, adapt an application that your team built with React, or write the code of a server-side service that your team deploys. What works well for integrations with other coding agents works here too: documentation first, a plan before code, small tested steps, and decisions written down.

To find out what a source site integrates with, ask the agent to list the third-party services that a sample page loads, such as analytics, tag management, consent, maps, video, chat, search, and forms. Then decide with your team how each one works on the new site.

For other systems, the agent has no skills, only general knowledge, which can be out of date. The system's own documentation makes the work reliable, so work through it together:

1. **Have it read the documentation first.** Give the agent the link to the system's developer documentation, or attach it. Before it writes any code, ask it to explain how the integration would work, what must run on a server, and which secrets are involved. Correct its understanding at this stage.
1. **Ask for the Edge Delivery Services way.** Ask whether the integration belongs in a block, a [widget](https://www.aem.live/docs/widgets), or the project's scripts, and how it keeps the pages fast. The agent proposes an approach and asks what it needs to know.
1. **Give it what the system needs:** endpoints, field names, example requests and responses, and a sandbox or test account. For a key that the agent needs while it works, see [Where Credentials Go Instead](#credential-settings).
1. **Build in small steps.** Test each step in the preview against a non-production endpoint.
1. **Record the result.** Ask the agent to write the chosen approach and the documentation link in the project's instruction files, so that the next conversation starts from it.

For example:

> Read the developer documentation of [platform] at [URL], especially [topic]. Explain how our site could [goal] following Edge Delivery Services practice: what runs in the browser, what needs a server, and which secrets are involved. List your questions. Don't change any files yet.

Setting up the other system, deploying a server-side service, and storing its secrets stay with your team and that system's administrators. For the integration patterns, see [Connect Services and Applications](block-development.md#integrations).

### Example: Updates in Slack (Advanced) {#slack-updates}

A credential in **Settings**, a project skill, and a line in `AGENTS.md` can connect the agent to the tools your team already uses. One developer on the team that builds the agent set it up to post a summary in Slack each time it finished a turn, with what it had changed, and to read his replies there as further instructions. He could follow and steer a long task without keeping the console open.

1. Create a Slack app whose bot token has only the scopes for posting and reading messages. Add the bot to one private channel, or use a direct message with you.
1. In **Settings** > **Protected site authentication**, add an entry for the hostname `slack.com` with bearer authentication and the bot token. See [Credentials for Other Services](console.md#other-services).
1. Ask the agent to write a [project skill](project-instructions.md#custom-skills) that explains how to post and read messages with the Slack Web API, and to push it.
1. In `AGENTS.md`, tell the agent that a credential for `slack.com` is set up, which channel to use, and when to post, for example at the end of each turn.

The agent treats what it reads in the channel as instructions, the same as chat. Keep the channel private, with only you and the bot in it, so that only you can instruct the agent. The summaries that it posts leave the console for Slack, so follow your organization's policy on what may go there. Remove the entry in **Settings** when you no longer use it. The same pattern works for other tools with an HTTP API that accepts a fixed header.

## Site Creation and Migration Prompts {#site-migration}

A migration follows this order: [catalog the site](#site-catalog), [migrate a sample page](#migrate-a-site) of each template, [migrate the design](#design-migration), [check the result with a critique](#site-critique), then [import the template's other pages](#bulk-import). The header, navigation, and footer are [set up once](#navigation-setup) for the whole site. For the full procedure, see [Migrate a Production Site](production-migration.md).

### Migrate Pages {#migrate-a-site}

Use these prompts to import pages from an existing website. To import a first page step by step, see [Import a Page Step by Step](getting-started.md#guided-import), or, for content stored in Experience Manager authoring, [Connect the Site and Import a Page](getting-started-aem-authoring.md#continue).

* "Migrate these pages: `https://www.example.com/products/hiking`, `https://www.example.com/products/climbing`. Reuse the existing blocks. Do not upload, push, or publish."

Things to know:

* The agent decides each page's sections, default content, blocks, and variants, and reuses the project's blocks before it creates new ones. Check this structure on the first pages: authors edit it, and the bulk import repeats it. See [Shape the Content Structure](production-migration.md#content-structure).
* Content and design are separate steps. After the content import, the agent suggests **Start Design Migration**: select it, or ask for the source styling. For a new design, see [Restyle During Migration](restyling.md#during-migration).
* The page import leaves out the header, navigation, and footer. See [Set Up the Header, Navigation, and Footer](#navigation-setup).
* Each migration writes an import script for the page's template, which the [bulk import](#bulk-import) runs on the template's other pages.
* For where images go, including images served from Dynamic Media, see [Images and Documents](production-migration.md#assets).

### Plan with the Site Catalog {#site-catalog}

Use these prompts to see a site's scale, templates, and blocks before you migrate it. To start a catalog, see [Plan a Migration with the Site Catalog](site-catalog.md).

* "Find templates on `https://www.example.com`"
* "How many page types are there on `https://www.example.com`?"

### Import Pages in Bulk {#bulk-import}

Use these prompts to import the other pages of a template once its sample page is migrated and checked.

* "Run the bulk import on these pages: `https://www.example.com/blog/first-post`, `https://www.example.com/blog/second-post`."
* "Bulk import all product pages."

Things to know:

* The bulk import runs the import script that the agent wrote when it migrated the template's sample page, so migrate that page first. See [How the Agent Migrates at Scale](production-migration.md#migration-at-scale).
* Each run covers the pages of one template, because the import script is written for that template's structure.
* Import a few pages first, check them, and correct the import script before you import the full list. See [Import in Batches](production-migration.md#batches) and [Bulk Import Workflow](site-catalog.md#bulk-import).

### Capture a Source Page {#scraping-webpages}

Page migration starts by capturing the source page. Ask for it on its own to analyze a page before you migrate it.

* "Capture `https://www.example.com/products` for analysis."
* "Extract the content and metadata from `https://www.example.com/product` at mobile and desktop widths."

Things to know:

* The agent loads the page in a browser and scrolls it, so that lazy-loaded images load. For what it captures, including content that scripts insert or CSS hides, and what it can't, see [Limitations](overview.md#limitations).
* It extracts the page's title, description, Open Graph tags, JSON-LD structured data, and canonical URL.
* It saves a screenshot and copies of the images, and it normalizes links and image references. Check the images against the source, including responsive images, backgrounds, and SVG images, and check that each link still points where it should.
* Ask for a specific screen width, such as mobile or desktop. Each additional width takes longer.

### Migrate the Design {#design-migration}

Use these prompts to recreate the source site's design on the imported content.

* "Migrate the design from `https://www.example.com`"
* "Extract the design tokens"
* "Style the hero block"
* "Style all the blocks"

Things to know:

* The agent styles the whole site first. It writes the design tokens, such as fonts, colors, spacing, and heading sizes, as CSS custom properties to `styles/brand.css`. `styles/styles.css` imports that file and styles the default content: headings, paragraphs, buttons, links, and section backgrounds.
* Then it styles the blocks in parallel, each in `blocks/{name}/{name}.css`, from the tokens. Block styling therefore needs the site-wide styles first.
* If the project already has a `brand.css` or other token files, ask the agent to use them rather than extract a second set from the source.
* Say whether the request is global or for one block, and whether it should stay faithful to the source or follow a [new design](restyling.md). Check the result on real pages at desktop and mobile widths.

### How Close the Design Gets {#design-fidelity}

The agent recreates the source design: it extracts the design tokens, styles each block, then compares each block with the source and fixes the differences that it finds. See [Critique the Site](#site-critique). The result comes close to the original on the first pass, and you correct what remains by prompting.

An identical copy can't be guaranteed. Fonts, image compression, and browser rendering can differ slightly from the source, and "identical" means different things to different projects: one team measures spacing to the pixel, another checks that the brand reads the same. The source also has its own flaws, such as spacing that differs between two pages of the same template, and recreating them rarely helps the new site.

Aim for the intended design:

1. Describe each remaining difference with the page, the screen width, and what should change, and check the result in the preview. A complex design can take several rounds.
1. Fix a difference that recurs in the global styles or the block's CSS, so that the fix applies to every page.
1. Before you scale, agree with the people who sign off the site on what counts as close enough, and check it on the sample pages.

### Critique the Site {#site-critique}

Use these prompts after design migration to compare every migrated template with the source and fix the differences in one pass.

* "Critique site"
* "Validate all blocks across the migrated site"

Things to know:

* Structural differences, such as a missing heading or link, or a wrong number of rows, are fixed in the import script, and the pages are imported again. Styling differences, such as colors, spacing, and typography, are fixed in the CSS.
* The agent works layer by layer: global styles, then sections, then block content, then block CSS. It checks the result again after each layer.
* When the same issue appears on several pages that use the same block, the agent fixes the block once for all of them.
* Without `brand.css`, the agent fixes only the structure.
* The critique compares how the pages look. Check separately that authors can edit them, that interactions work, and that they are accessible; see [Limitations](overview.md#limitations). Review the coverage and the unresolved issues that the critique reports.

### Critique a Page {#page-critique}

Use these prompts to check one migrated page, for example after a site critique.

* "Critique the about page"
* "Validate the migrated page `/about` against `https://www.example.com/about`"

The agent needs the source URL and the migrated path, and it works through the same layers as the [site critique](#site-critique). Check the remaining differences in the preview.

### Critique a Block {#block-critique}

Use these prompts to check one block after design migration.

* "Critique the hero block"
* "Validate the custom-cards block"

The block must come from a page migration. The agent fixes it as in the [site critique](#site-critique).

### Create a Block from Figma {#figma-block-migration}

Use these prompts to build one block from a Figma component. [Work from a Figma Design](visual-changes.md#figma) covers the access token, the seat you need, and why to work one component at a time.

* "Create a block from this Figma component: `{Figma link}`. Reuse our design tokens."
* "Migrate the `pricing-card` component from the Figma file `{fileKey}`."

Things to know:

* In Figma, select the component and copy its link, so that the link includes the `node-id` that identifies it: `https://www.figma.com/design/{fileKey}?node-id={nodeId}`. Or give the file key and the component's name.
* The agent reads the component's structure first, which keeps large Figma files manageable, and then its design details. It adds the colors, typography, and spacing as design tokens to `styles/styles.css`, with tokens specific to the block, before it writes any CSS. It maps the component to the closest block in your project and creates a variant, writes the variant's CSS from the tokens, saves the images and icons in the console workspace, and creates sample content. It then previews the block and compares it with the Figma design.

### Redesign with Blocks from Figma {#figma-redesign-migration}

Use these prompts when a site gets a new design during migration: Figma supplies the design and the blocks, and the live site supplies the content. For the procedure and what to compare, see [Restyle During Migration](restyling.md#during-migration).

1. "Create the block collection from these Figma components: `{Figma link}`"
1. "Migrate these pages and map their content to the blocks created from Figma: `https://www.example.com/adventures`, `https://www.example.com/magazine`"

Ask for a new variant only where the blocks from Figma can't represent the source content.

### Create a New Page from Figma {#figma-new-page-from-figma}

Use this prompt when a page doesn't exist on a source site and a Figma frame or page should become a new page.

* "Migrate this Figma page to a new page at `/events`: `{Figma link}`"

Things to know:

* Select one frame or page, not an entire file, and organize it into clear page sections.
* The agent maps each section to an existing block, default content, or a new variant. Text and images come from Figma.
* A Figma frame shows how a feature looks, not where its data comes from or how it behaves. For search, calculators, personalization, or store locators, the Figma migration creates the layout. Then ask the agent to build the behavior as a [dynamic block](block-development.md#dynamic-blocks), and give it the API or data source.

### Set Up the Header, Navigation, and Footer {#navigation-setup}

Use these prompts for the header, navigation, and footer, including footer images. The page import leaves them out, because every page shares one header and one footer.

* "Set up the navigation from `https://www.example.com`"
* "Migrate the footer from `https://www.example.com`"
* "Fix the navigation menu"

Things to know, for projects that use the header and footer of the [AEM boilerplate](https://github.com/adobe/aem-boilerplate):

* The header loads the `nav` page from the content root, and the footer loads the `footer` page, unless a page's `nav` or `footer` metadata names another page. In document-based projects, the agent writes the navigation as `nav.md` in the console workspace.
* The navigation page has three sections, separated by `---`: the brand, with the logo and the link to the home page; the main menu; and tools, such as links to sign in or subscribe.
* A menu item that contains a nested list becomes a dropdown.
* A bold or italic link alone in its paragraph becomes a button, as on other pages, except the brand link: the header removes its button styling. See [Example: A Flexible Teaser Without Atomic Blocks](block-development.md#composition-example).
* If the project changed `header.js` or `footer.js`, ask the agent to check them first.
* For Experience Manager authoring, confirm where the navigation page is stored and which model it uses.

## Block Development Prompts {#block-development-capabilities}

These prompts create and change blocks, during a migration or in any project. For the procedures and checks, see [Create, Update, and Refactor Blocks](block-development.md).

### Develop a Block {#block-development}

Use these prompts to create a block or change an existing one.

* "Create a testimonials block"
* "Add a video background variant to the hero block"

Things to know:

* The agent creates test content along with the content model; see [Prompt for a Block](block-development.md#block-prompts). The test content lets you check the block, gives the pull request a page to test with PageSpeed Insights, and shows authors how to use the block.
* For a change to CSS only, the agent skips the content model but still uses test content to check the result.
* Before it creates a block, it looks for one to reuse. See [Reuse Existing Blocks](block-development.md#reuse-blocks).

### Design a Content Model {#content-modeling}

Use these prompts to design the table that authors fill in for a block. Content-driven development runs this step when it creates a block; ask for it on its own to compare options.

* "Design a content model for a testimonials block"
* "What's the best content model for this carousel?"

Things to know:

* Four patterns cover most blocks:
  * **Standalone:** one distinct element, such as a hero or a quote, in a single table.
  * **Collection:** repeating items, such as cards or carousel slides, with one row per item.
  * **Configuration:** a block whose content comes from an API or data source, such as a blog listing or search results, with key-value rows that control what it shows. See [Build a Dynamic Block](block-development.md#dynamic-blocks).
  * **Auto-blocked:** content that authors write as sections or default content and that the code turns into a block, such as tabs or YouTube embeds.
* Keep each table to a few cells and group related elements naturally, so that authors can fill it in. This is for authors: block code can read any table structure.
* Prefer block variants over configuration cells for differences in style.
* Accept flexible input, following [Postel's law](https://en.wikipedia.org/wiki/Robustness_principle): a hero block should work whether its content is in one cell, in two cells, or in separate rows.
* For Experience Manager authoring, the block also needs a model for the Universal Editor. See [Create a Block](block-development.md#create).

### Find Reference Blocks {#reference-blocks}

Use these prompts to find existing implementations to start from.

* "Find blocks similar to a pricing table"
* "What blocks are available for testimonials?"
* "Search Block Party for a tabs implementation"

Things to know:

* Start with the [Block Collection](https://www.aem.live/developer/block-collection). Adobe maintains it and checks each block for content modeling, performance, and accessibility. It covers commonly needed blocks.
* When it doesn't have what you need, search the [Block Party](https://www.aem.live/developer/block-party/). The community maintains it, with a broader range that includes experimental approaches, plugins for AEM Sidekick, build tools, and integrations. It returns only approved entries. AEM Sidekick is the browser extension that previews and publishes pages.
* Search with other names too: accordion for FAQ, carousel or slideshow for gallery, menu or header for navigation.

### Search the Documentation {#searching-documentation}

Use these prompts to find guidance on Edge Delivery Services features and implementation.

* "How do I lazy-load images in Edge Delivery Services?"
* "Search the docs for section metadata"

The agent searches the documentation and blog posts on [aem.live](https://www.aem.live). Use specific keywords, such as "block decoration", "sidekick plugin", or "metadata", rather than general ones, such as "website" or "how to build". For code to start from, ask for [reference blocks](#reference-blocks) instead. Check what it finds against your project's code and where its content is stored.

### Test Changes {#testing}

Use these prompts to test a change before you open a pull request.

* "Test the new cards block"
* "Run the tests before I open a pull request"

The agent writes a test when its value exceeds the cost of maintaining it. It keeps unit tests for logic-heavy code, such as utilities, data processing, and API integrations, because they are fast and catch regressions in reused code. Browser checks cover how a block changes the page, its interactions, and its appearance. For what to check before a pull request, see [Validate and Deliver](block-development.md#validation).

### Debug a Problem {#debugging}

Use these prompts when a block, an image, a style, or the preview doesn't work as expected. For deeper checks, the agent can turn on the Edge Delivery Services troubleshooting [optional capability](console.md#optional-capabilities).

* "Debug why images show as about:error"
* "Fix the hero block, which doesn't render"
* "Why aren't my changes showing in the preview?"

Things to know:

* The agent checks the source files, the rendered page, the block code, and the browser console, in that order. It uses the console's preview, so you don't need to run a local server.
* Common causes:
  * **Images show `about:error`:** the block's JavaScript doesn't call `createOptimizedPicture`, or calls it before it restructures the block's markup.
  * **A block doesn't render:** the block name in the content doesn't match its folder in `blocks/`, or the folder lacks the `.js` or `.css` file.
  * **CSS doesn't load:** a file path is wrong. Check the Network tab of the browser's developer tools.
  * **A change doesn't appear:** see [A Change Is Missing](troubleshooting.md#missing-change) and [Console Preview Differs from the Site](troubleshooting.md#preview-differs).
* Keep the failing URL and the error details, and retry the smallest affected scope after you fix the cause. Before you overwrite or reset work, see [Release, Recover, and Hand Over](production-migration.md#handoff).
