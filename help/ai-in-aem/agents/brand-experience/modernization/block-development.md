---
title: Create, Update, and Refactor Blocks with the Experience Modernization Agent
description: Develop lightweight Edge Delivery Services blocks from author needs and real content, and preserve compatibility when updating or refactoring them.
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

# Create, Update, and Refactor Blocks {#block-development}

Use the Experience Modernization Agent (EMA) for ongoing Edge Delivery Services (EDS) development as well as migration. Begin with the author need and real content, then choose the smallest implementation that supports them.

EMA follows Content-Driven Development (CDD) for this work. It starts from real content and from how authors will create it, and writes code after that. This keeps content models easy for authors to use and avoids blocks that only developers can fill in.

Connect the intended repository and branch, confirm modification permissions, and identify whether authors use [document-based or JCR-backed content](overview.md#content-storage). Preserve a baseline before changing shared code or content models.

## Compose Before Creating a Block {#composition}

HTML elements are the basic building units, or atoms: headings, paragraphs, links, lists, and images. Authors should use default content, the content outside blocks, for these where possible. Global styles and CSS custom properties, or design tokens, define shared typography, colors, spacing, and link/button presentation.

A block adds a reusable content structure or behavior where default content is insufficient. In the HTML that EDS serves, a block is a `div` with the block name as its class. The project's `blocks/<name>/<name>.js` and `blocks/<name>/<name>.css` decorate it in the browser. Keep a block lightweight and focused; a visual difference alone does not always need a new block.

Check the project's conventions before generating code:

| Need | Decision to check |
|---|---|
| Call to action (CTA) | How an authored link becomes a button (see the [example](#composition-example)), which variants exist, and how the label and destination remain editable. |
| Button group | Whether adjacent links/default content already support the grouping, or a reusable model is needed for order, wrapping, and variants. |
| Footnote | How markers, target IDs, return links, and reading order are authored and preserved. |
| Repeated content | Whether an existing cards/list block or variant represents it without extra author fields. |

These are project conventions, not universal EMA authoring controls. Do not invent a button-group or footnote UI. Check the actual content model and rendered result.

### Example: A Flexible Teaser Without Atomic Blocks {#composition-example}

Component-based AEM projects often provide a teaser component, or separate heading, image, text, and button components, so that authors can combine them. The home page of the [WKND sample site for AEM](https://wknd.site/us/en.html), for example, promotes each trip with a Core Components teaser. In EDS, authors write the same elements directly as default content, either in a section or in a block cell:

```text
[Image]
## Downhill Skiing Wyoming
A skier's paradise far from crowds and close to nature.
**[View trip](/adventures/downhill-skiing-wyoming)**
_[All adventures](/adventures)_
```

In the current [AEM boilerplate](https://github.com/adobe/aem-boilerplate), a link that is alone in its paragraph becomes a button when it is formatted: bold for a primary button, italic for a secondary button, and bold plus italic for an accent button. A plain link, or a link inside a sentence, remains a link. Global styles give these buttons the same appearance in default content and inside blocks.

Authors can add, remove, or reorder the heading, text, image, and links without new components. A teaser or hero block is needed only for layout or behavior that default content cannot provide, such as placing the image beside the text. Projects can change these conventions, so ask EMA to check the project's scripts and styles before relying on them.

## Prompt for a Block {#block-prompts}

You can start with a short prompt, such as "Create a testimonials block". EMA follows content-driven development: it works out the content and content model with you before it writes code. Add context where it helps EMA match something specific:

| To show EMA | Provide |
|---|---|
| A design on an existing site | The page URL, and the section to match. |
| A design that isn't online | A screenshot or image (JPEG, PNG, GIF, or WebP), with **Attach files** in the [prompt input](console.md#prompt-input). For Figma designs, see [Figma block migration](prompting-guide.md#figma-block-migration). |
| An element in the console preview | Select it with **Inspect mode** in the [content views](console.md#content-view). EMA receives the element's HTML and its position on the page, and limits its changes to that element. |
| How authors fill in the block | Example content, the parts that are optional or repeat, and the variants you need. |

A reference page or screenshot shows the target appearance. It doesn't define what authors edit, so say that too.

### Reuse Existing Blocks {#reuse-blocks}

Before EMA creates a block, it looks for one to reuse or adapt: in your project's `blocks` folder, and in the [Block Collection](https://www.aem.live/developer/block-collection) and [Block Party](https://www.aem.live/developer/block-party/) for reference code. During migration, it also checks the [block library](#block-deliverables) that **Library URL** in [Settings](console.md#settings-page) points to.

* If your organization keeps a block library for authors, set **Library URL** to its `library.json` file.
* To reuse blocks from another repository, add them to this project's `blocks` folder first, for example by pushing them to your branch and then pulling the code into the console.
* Record your naming, variant, and content conventions in the [project instruction files](project-instructions.md#content-conventions), so that new blocks follow them.

### Build Blocks One at a Time {#iterate-blocks}

When you need several blocks, don't ask for all of them in one prompt. Build one or two representative blocks first, and check their content model, styling, and authoring. Then continue with the others, so that the decisions you made, such as names, variants, and spacing, carry over. In a migration, generate and validate the blocks of one representative template before the rest; see [Bulk Import Workflow](site-catalog.md#bulk-import).

### Set Block Behavior Before a Migration {#block-instructions}

Migration generates blocks from the content that it finds on the source pages. To steer how a block is built before EMA generates it:

* Describe it in the migration prompt, for example which source sections become one block with variants, which parts authors edit, or that a list must load its items [dynamically](#dynamic-blocks).
* Write lasting conventions in the [project instruction files](project-instructions.md#content-conventions) before you start.
* In the [site planning UI](site-catalog.md#planning-actions), correct block types and variants before you generate code. To describe how a block should behave, select it, choose **Add to chat**, and write your request.

Auto mode doesn't take instructions during a run. Refine its blocks in the console afterwards.

## Create a Block {#create}

Provide the author task, example content, desired behavior/design, target persistence, and destination test page.

1. Ask EMA to inspect existing blocks and suitable [reference implementations](prompting-guide.md#reference-blocks). Prefer reuse or a variant over a duplicate.
1. Define a content model that authors can understand. Use headings, links, images, and grouped content naturally rather than exposing CSS or implementation details as fields.
1. Create representative content first. Include long text, missing optional values, multiple items, and meaningful images/links.
1. Implement only the needed HTML decoration, CSS, and JavaScript. Reuse project tokens and shared utilities.
1. For JCR-backed projects, update the source models/component configuration and regenerate aggregates through the project workflow. A block's model defines the fields authors edit in the Universal Editor. Check conversion and authoring hints. A document table alone does not establish a working Universal Editor model.
1. [Validate](#validation), then document an authorable example and allowed variants.

For example:

> Create a testimonials block for [authoring target]. Start from these real content examples: [paths]. Check existing blocks first. Authors need to edit quote, attribution, and optional image without layout configuration. Use our tokens. Include long text and no-image examples. Do not upload, push, or publish.

The output is reusable code, a working target-specific model where needed, and editable examples—not just a screenshot or generated files.

### What EMA Provides With a Block {#block-deliverables}

* **Block documentation:** When migration creates a block, it generates the block from the content model found on your pages and adds a README for developers and an authoring guide for authors. Review both and keep them current when you change the block. To make later conversations follow the block's conventions, such as optional content, variants, and the sections it works in, reference them from the project's instruction files. See [Document Content Conventions](project-instructions.md#content-conventions).
* **Sample content:** EMA generates sample content for blocks so that you can preview them with realistic content. In the [site catalog](site-catalog.md#blocks-table), use **View sample** to open a block's sample page.
* **Block library:** The block library lets authors find your custom blocks and insert them into pages, with sample content that shows how each block is meant to be used. To set it up, ask EMA to generate a block library, including sample content and the library configuration, for Experience Workspace (formerly Document Authoring) or AEM authoring. Block library setup is an [optional capability](console.md#optional-capabilities) that EMA offers to turn on for your project. Check the result in the authoring experience. The library location is set by **Library URL** in [Settings](console.md#settings-page), which points to a `library.json` file that lists the available blocks, their variations, and example content.

## Build a Dynamic Block {#dynamic-blocks}

A dynamic block loads or computes its content in the browser, rather than showing only what authors write. Examples are a list of the latest articles, search results, or a filtered list. Ask EMA to create one after migration like any other block, or to change a migrated block to work this way. Describe:

* **The data source**, such as the site's [query index](https://www.aem.live/developer/indexing), a spreadsheet delivered as JSON, or an API.
* **What authors control**, such as the number of items, the folder to list, or the sort order. EMA models these settings as a configuration block: a two-column table of keys and values. Use it only for settings that change what the block loads or shows, and use variants for differences in style.
* **What each item shows**, and what the block shows when there are no results or the data can't load.

For example:

> Create an article-list block that shows the six newest articles from the site's query index, with image, title, and date. Authors set the number of articles and the folder to list in a key-value table. Show a short message when there are no articles. Test it on /news. Do not upload, push, or publish.

The query index includes only published pages, and only the properties that its configuration extracts, so check both before you test. [Validate](#validation) the empty and error states as well as the normal result.

## Update an Existing Block {#update}

Provide the block name, current examples/variants, requested change, and compatibility requirements.

1. Identify pages using the block, shared styles/utilities, and existing tests.
1. State what must remain unchanged, including existing content structures and interactions.
1. Make the bounded change. For presentation-only changes, avoid changing models or regenerating content.
1. Test the changed behavior and the unaffected variants on representative content.
1. If an incompatible model change is necessary, agree how existing content will be migrated and who accepts the authoring impact before applying it.

For example:

> Update `cards` so the approved secondary-link variant works on [test paths]. Preserve existing default and image variants and their authored content. Check keyboard interaction and mobile wrapping. Do not rewrite other pages or upload content.

Hand over the changed behavior, affected variants, author instructions, and any required content changes.

## Refactor Without Changing the Outcome {#refactor}

Refactoring improves implementation while preserving agreed behavior. It is not the same as regrouping a catalog, redesigning a block, or migrating its content model.

1. Name the code to improve and the reason, such as duplicated decoration logic.
1. Record invariants: content model, appearance, responsive behavior, accessibility, public selectors/API contracts, and integrations to preserve.
1. Establish baseline examples and existing tests. Check uses of shared code and styles before consolidating them.
1. Ask for the smallest refactor that meets the goal. Keep any necessary behavior/model change explicit and separate.
1. Compare before and after across affected pages and variants, run the project checks, and inspect the diff.

For example:

> Refactor duplicated card-decoration logic in [blocks/files]. Preserve authored models, output semantics, appearance, link behavior, keyboard access, and analytics hooks. Use [paths] as regression examples. Report compatibility risks and test results. Do not migrate content or push changes.

This is a development request, not a dedicated refactoring button or guaranteed automatic conversion.

## Validate and Deliver {#validation}

Use the project's declared lint and test commands, plus browser checks on real content. Ask EMA to report the commands and results, not simply that it tested.

Check:

* All affected variants and content edge cases.
* Desktop/mobile layout, long content, and image behavior.
* Keyboard access, focus, semantics, labels, and reading order.
* Existing interactions and integrations.
* Author edit/save/reopen and preview on the selected persistence target when models or content change.
* Relevant performance checks and no new browser errors.

If a check fails, retain the failing example and fix the smallest affected layer. Distinguish stale preview/code-branch problems from model or implementation failures. Re-run the failing check and relevant regressions.

Review the diff, stage only intended files, and [push through the repository policy](getting-started.md#push-code-changes). Upload test or production content only when authorized; a code push does not save it. Once merged into `main`, the block code applies to every page on the live site that uses the block; see [How Changes Go Live](overview.md#code-content-lifecycle).

For recovery, revert code through Git and restore changed remote content separately. Keep compatible old examples until any required content migration is accepted.

Use the [project handover](project-documentation.md#portable-handoff) to retain changed files, models, examples, validation results, remaining risks, and the recovery approach for the next person or agent.
