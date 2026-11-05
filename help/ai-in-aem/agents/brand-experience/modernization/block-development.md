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

Use the Experience Modernization Agent for ongoing Edge Delivery Services development as well as migration. Begin with the author need and real content, then choose the smallest implementation that supports them.

The agent follows Content-Driven Development (CDD) for this work. It starts from real content and from how authors will create it, and writes code after that. This keeps content models easy for authors to use and avoids blocks that only developers can fill in.

Connect the intended repository and branch, confirm modification permissions, and identify whether authors use [document-based or JCR-backed content](overview.md#content-storage). Preserve a baseline before changing shared code or content models.

## Compose Before Creating a Block {#composition}

HTML elements are the basic building units, or atoms: headings, paragraphs, links, lists, and images. Authors should use default content, the content outside blocks, for these where possible. Global styles and CSS custom properties, or design tokens, define shared typography, colors, spacing, and link/button presentation.

A block lets authors mark which content forms one component, such as a set of cards or a carousel, where the code couldn't tell it apart from the surrounding default content. In the HTML that your site serves, a block is a `div` with the block name as its class. The project's `blocks/<name>/<name>.js` and `blocks/<name>/<name>.css` decorate it in the browser. Where the code can recognize a pattern in default content, it can build the block itself, which aem.live calls [auto-blocking](https://www.aem.live/developer/markup-sections-blocks): the AEM boilerplate, for example, turns a link to a `/widgets/` page into a widget block. Keep a block lightweight and focused. A visual difference alone doesn't need a new block: CSS and JavaScript can style default content, and a variant or a section style can carry the difference.

[David's Model](https://www.aem.live/docs/davidsmodel) collects the aem.live rules for content that authors can create easily: prefer default content, avoid blocks inside blocks, keep the number of blocks and variants small, and let buttons take their style from the block or section that they are in. When a block does the same job as one in the [Block Collection](https://www.aem.live/developer/block-collection), reuse that block's content model.

Check the project's conventions before generating code:

| Need | Decision to check |
|---|---|
| Call to action (CTA) | How an authored link becomes a button (see the [example](#composition-example)), which variants exist, and how the label and destination remain editable. |
| Button group | Whether adjacent links/default content already support the grouping, or a reusable model is needed for order, wrapping, and variants. |
| Footnote | How markers, target IDs, return links, and reading order are authored and preserved. |
| Repeated content | Whether an existing cards/list block or variant represents it without extra author fields. |

Edge Delivery Services has no built-in button-group or footnote control. Each is a convention that the project's code applies to authored content, so check how your project implements it and test the rendered result.

### Example: A Flexible Teaser Without Atomic Blocks {#composition-example}

Component-based Adobe Experience Manager projects often provide a teaser component, or separate heading, image, text, and button components, so that authors can combine them. The home page of the [WKND sample site](https://wknd.site/us/en.html), for example, promotes each trip with a Core Components teaser. With Edge Delivery Services, authors write the same elements directly as default content, either in a section or in a block cell:

```text
[Image]
## Downhill Skiing Wyoming
A skier's paradise far from crowds and close to nature.
**[View trip](/adventures/downhill-skiing-wyoming)**
_[All adventures](/adventures)_
```

In the current [AEM boilerplate](https://github.com/adobe/aem-boilerplate), a link that is alone in its paragraph becomes a button when it is formatted: bold for a primary button, italic for a secondary button, and bold plus italic for an accent button. A plain link, or a link inside a sentence, remains a link. Global styles give these buttons the same appearance in default content and inside blocks.

Authors can add, remove, or reorder the heading, text, image, and links without new components. A teaser or hero block is needed only where authors must mark which elements belong together; CSS and JavaScript can place the image beside the text in default content as well. Projects can change these conventions, so ask the agent to check the project's scripts and styles before relying on them.

## Prompt for a Block {#block-prompts}

You can start with a short prompt, such as "Create a testimonials block". The agent follows content-driven development: it works out the content and content model with you before it writes code. Add context where it helps the agent match something specific:

| To show the agent | Provide |
|---|---|
| A design on an existing site | The page URL, and the section to match. |
| A design that isn't online | A screenshot or image (JPEG, PNG, GIF, or WebP), with **Attach files** in the [prompt input](console.md#prompt-input). For Figma designs, see [Figma block migration](prompting-guide.md#figma-block-migration). |
| An element in the console preview | Select it with **Inspect mode** in the [content views](console.md#content-view). The agent receives the element's HTML and its position on the page, and limits its changes to that element. |
| How authors fill in the block | Example content, the parts that are optional or repeat, and the variants you need. |

A reference page or screenshot shows the target appearance. It doesn't define what authors edit, so say that too.

### Reuse Existing Blocks {#reuse-blocks}

Before the agent creates a block, it looks for one to reuse or adapt: in your project's `blocks` folder, and in the [Block Collection](https://www.aem.live/developer/block-collection) and [Block Party](https://www.aem.live/developer/block-party/) for reference code. During migration, it also checks the [block library](#block-deliverables) that **Library URL** in [Settings](console.md#settings-page) points to.

* If your organization keeps a block library for authors, set **Library URL** to its `library.json` file.
* To reuse blocks from another repository, add them to this project's `blocks` folder first, for example by pushing them to your branch and then pulling the code into the console.
* Record your naming, variant, and content conventions in the [project instruction files](project-instructions.md#content-conventions), so that new blocks follow them.

### Build Blocks One at a Time {#iterate-blocks}

When you need several blocks, don't ask for all of them in one prompt. Build one or two representative blocks first, and check their content model, styling, and authoring. Then continue with the others, so that the decisions you made, such as names, variants, and spacing, carry over. In a migration, generate and validate the blocks of one representative template before the rest; see [Bulk Import Workflow](site-catalog.md#bulk-import).

### Set Block Behavior Before a Migration {#block-instructions}

Migration generates blocks from the content that it finds on the source pages. To steer how a block is built before the agent generates it:

* Describe it in the migration prompt, for example which source sections become one block with variants, which parts authors edit, or that a list must load its items [dynamically](#dynamic-blocks).
* Write lasting conventions in the [project instruction files](project-instructions.md#content-conventions) before you start.
* In the [site planning UI](site-catalog.md#planning-actions), correct block types and variants before you generate code. To describe how a block should behave, select it, choose **Add to chat**, and write your request.

Auto mode doesn't take instructions during a run. Refine its blocks in the console afterwards.

## Create a Block {#create}

Provide the author task, example content, desired behavior/design, target persistence, and destination test page.

1. Ask the agent to inspect existing blocks and suitable [reference implementations](prompting-guide.md#reference-blocks). Prefer reuse or a variant over a duplicate.
1. Define a content model that authors can understand. Use headings, links, images, and grouped content naturally rather than exposing CSS or implementation details as fields.
1. Create representative content first. Include long text, missing optional values, multiple items, and meaningful images/links.
1. Implement only the needed HTML decoration, CSS, and JavaScript. Reuse project tokens and shared utilities.
1. For JCR-backed projects, update the source models/component configuration and regenerate aggregates through the project workflow. A block's model defines the fields authors edit in the Universal Editor; the editor reads the model, not a table in a document, so the block is editable there only once its model defines those fields. Check conversion and authoring hints.
1. [Validate](#validation), then document an authorable example and allowed variants.

For example:

> Create a testimonials block for [authoring target]. Start from these real content examples: [paths]. Check existing blocks first. Authors need to edit quote, attribution, and optional image without layout configuration. Use our tokens. Include long text and no-image examples. Do not upload, push, or publish.

The output is reusable code, a working target-specific model where needed, and editable examples—not just a screenshot or generated files.

### What the Agent Provides With a Block {#block-deliverables}

* **Block documentation:** When migration creates a block, it generates the block from the content model found on your pages and adds a README for developers and an authoring guide for authors. Review both and keep them current when you change the block. To make later conversations follow the block's conventions, such as optional content, variants, and the sections it works in, reference them from the project's instruction files. See [Document Content Conventions](project-instructions.md#content-conventions).
* **Sample content:** The agent generates sample content for blocks so that you can preview them with realistic content. In the [site catalog](site-catalog.md#blocks-table), use **View sample** to open a block's sample page.
* **Block library:** The block library lets authors find your custom blocks and insert them into pages, with sample content that shows how each block is meant to be used. To set it up, ask the agent to generate a block library, including sample content and the library configuration, for Experience Workspace (which replaces Document Authoring) or Experience Manager authoring. Block library setup is an [optional capability](console.md#optional-capabilities) that it offers to turn on for your project. Check the result in the authoring experience. The library location is set by **Library URL** in [Settings](console.md#settings-page), which points to a `library.json` file that lists the available blocks, their variations, and example content.

## Build a Dynamic Block {#dynamic-blocks}

A dynamic block loads or computes its content in the browser, rather than showing only what authors write. Examples are a list of the latest articles, search results, or a filtered list. Ask the agent to create one after migration like any other block, or to change a migrated block to work this way. Describe:

* **The data source**, such as the site's [query index](https://www.aem.live/developer/indexing), a spreadsheet delivered as JSON, or an API.
* **What authors control**, such as the number of items, the folder to list, or the sort order. The agent models these settings as a configuration block: a two-column table of keys and values. Use it only for settings that change what the block loads or shows, and use variants for differences in style.
* **What each item shows**, and what the block shows when there are no results or the data can't load.

For example:

> Create an article-list block that shows the six newest articles from the site's query index, with image, title, and date. Authors set the number of articles and the folder to list in a key-value table. Show a short message when there are no articles. Test it on /news. Do not upload, push, or publish.

The query index includes only published pages, and only the properties that its configuration extracts, so check both before you test. [Validate](#validation) the empty and error states as well as the normal result.

## Connect Services and Applications {#integrations}

The agent writes the code that connects your site to other systems. Edge Delivery Services pages run this code in the visitor's browser, so each connection is part of a block, a widget, or the project's scripts. Give the agent the API documentation, example responses, and the agreed behavior, and test against a non-production endpoint first.

* **Applications:** A form, a search page, a store locator, or an account area has little authored content. Build it as a [widget](https://www.aem.live/docs/widgets): a self-contained application in the repository's `/widgets/` folder, which authors place on a page by inserting its link. An existing application, such as one built with React, can be adapted the same way.
* **APIs:** A block or widget calls an API from the browser. The API must accept requests from your site's domains, including the preview and live sites. If other sites must read your site's resources, configure [custom headers](https://www.aem.live/docs/custom-headers) for the paths that they need, never for all origins.
* **Secrets:** Everything in the repository is delivered to the browser, so it can't hold API keys or tokens. When an API needs a secret, call it through a server-side service that keeps the secret, such as Adobe App Builder or API Mesh, and let the block call that service.
* **Commerce:** The commerce pages add-on is built for storefronts on Adobe Commerce. It imports product detail and product listing pages as pages whose product data loads from the catalog when a visitor opens them. See [Commerce Pages](#commerce-pages).
* **Forms:** The forms add-on turns the source's forms with two or more fields into form definitions for the form block of Adobe Experience Manager Forms, and is built for organizations that license it. Where submissions go is a separate choice; see [Form Submissions](#form-submissions).
* **Analytics, tag management, and consent:** Load these scripts after the page has rendered, so that they don't slow it down. See [Keeping Your Lighthouse Score 100](https://www.aem.live/developer/keeping-it-100). With Auto mode's **Include integrations**, the agent adds the supported settings, switched off until you turn them on.

Add-ons are [optional capabilities](console.md#optional-capabilities) that the agent offers to turn on when a task needs one. Which systems connect, who owns them, and who accepts the result are project decisions. See [What Remains Project Work](evaluate.md#project-work).

### Form Submissions {#form-submissions}

Edge Delivery Services delivers a form, but it doesn't store submissions or run what follows them. On the source site, a server handled each submission, and page import can't see that server. Connecting a destination is the same work on any Edge Delivery Services site, migrated or not, and because the agent is a general-purpose coding agent, you can ask for it at any time.

#### What the Forms Add-on Does {#forms-add-on}

The forms add-on is built for organizations that license Adobe Experience Manager Forms. It prepares forms for [Edge Delivery Services for Experience Manager Forms](https://www.aem.live/developer/forms). For each source form with two or more fields, it records the fields in a form definition, a sheet saved next to the page with one row per field: its name, label, type, options, and validation. It then places a form block on the page that links to the definition. The fields and labels are content in that definition, not data held in a forms backend. Every form uses the same block, named `form`, and its definition decides what it shows, so the agent doesn't create variants of the block. The add-on saves each definition in the page's folder, named after the source form, and doesn't look for the same form on other pages. To maintain a form that several pages show in one place, ask the agent to link those pages to a single definition.

If the project has no form block yet, the add-on adds the form block of Experience Manager Forms. That block sends every submission to the [Forms Submission Service](/help/forms/forms-submission-service.md), which identifies the form by the path of its definition and stores the data in the spreadsheet linked in the definition's submit row. The add-on doesn't link a spreadsheet, and it doesn't keep the address that the source form submitted to, so connect a destination before the form goes live. See [Choose a Destination](#form-destination). The add-on itself needs no license, but the form block and the Forms Submission Service require an Experience Manager Forms license.

Without Experience Manager Forms, the add-on's field inventory is the part that still helps: it captures each form's fields, labels, types, options, and validation. The agent has no skills for other form platforms. It knows them only in general, and their APIs change, so give it the platform's current documentation and ask it to read it first. It can then build a form block that reads the same definitions and submits to your platform, or embed the form that your platform hosts. See [Work Beyond Edge Delivery Services](prompting-guide.md#beyond-eds).

The add-on reads each form from the HTML that the source server sends. A form that a script adds in the browser, such as a form embedded from a marketing platform, isn't in that HTML, so the add-on doesn't import it. Ask the agent to rebuild that form, or to embed it again from your platform.

#### Choose a Destination {#form-destination}

Lead forms belong where your teams already handle leads, in a marketing automation platform or customer relationship management (CRM) system, for example:

* Adobe Marketo Engage
* Salesforce, through Sales Cloud or Marketing Cloud Account Engagement
* Microsoft Dynamics 365
* HubSpot
* Oracle Eloqua

When submissions must reach several systems, send them to an integration platform, such as Adobe Workfront Fusion or Microsoft Power Automate, or to your own API. With Experience Manager Forms, the Forms Submission Service stores submissions in a spreadsheet or sends them by email, and submit actions that run on Experience Manager forward them to other systems, such as Marketo Engage, Workfront Fusion, Power Automate, or a REST endpoint. See [Configure Submit Actions](/help/edge/docs/forms/configure-submission-action-for-eds-forms.md).

Many of these platforms accept a submission from the browser at a form endpoint that needs no secret. If the platform's API needs a key, send the submission through a server-side service that keeps it, as described under **Secrets** above.

Tell the agent:

* **Destination:** the platform and the form, list, or campaign that receives the data, with its endpoint and documentation, or the URL of your server-side service.
* **Field mapping:** which form field goes to which platform field, which fields are required, and their formats.
* **Hidden values:** values that visitors don't enter, such as the lead source, the campaign, the page URL, and the UTM parameters of the visit.
* **Consent:** the opt-in checkboxes, their approved wording, and the link to your privacy policy.
* **Spam protection:** the method that your platform supports, such as a CAPTCHA or a hidden honeypot field.
* **After submitting:** the confirmation message or thank-you page, and what visitors see if the submission fails.
* **Testing:** a test form or sandbox, and how test entries are marked.

For example:

> First read [platform]'s documentation on form submissions at [URL]. Then connect the form on /contact to [platform] form [form ID] at [endpoint or service URL]. Map first name, last name, email, company, and country to the platform fields [field names]; email and company are required. Add hidden fields for the lead source "Website", the page URL, and the UTM parameters of the visit. Show this consent checkbox, unchecked: [approved text]. After a successful submission, show [confirmation message]; if it fails, keep the visitor's entries and show an error with a retry. Test against [sandbox]. Do not upload, push, or publish.

The agent updates the form definition and the form block's code. It can also write the code of a server-side service, which your team deploys with the secret. In the receiving platform, its administrator configures:

* The form or endpoint, with the fields it expects and their validation.
* The domains allowed to submit: your preview and live sites and your production domain.
* Spam filtering on the server. Checks in the browser help visitors fill in the form; they don't protect the platform.
* How a new submission is matched to existing contacts, so that one person doesn't become two leads.
* Lead source and campaign attribution, scoring, and routing to the right sales team.
* Confirmation emails, internal notifications, and follow-up programs.
* Consent records, and where personal data is kept and for how long.

Submit a test entry from the preview site. Check that it arrived with every field, started the expected workflow, and was marked as a test. Repeat the check on the production domain after the switch.

### Commerce Pages {#commerce-pages}

The commerce pages add-on is built for storefronts that run on Adobe Commerce. It recognizes product detail pages and product listing pages on the source site, whichever platform runs it, from signals such as product structured data, URL patterns, and page elements like a quantity field, a product grid, or filters. It rebuilds each one as a page that holds only the product's SKU, or the category's path, in a commerce block, and the surrounding content, such as banners and promotions, in standard blocks. The product data isn't imported: the commerce block loads it from the catalog each time a visitor opens the page. The agent migrates other pages with the standard workflow.

The add-on doesn't write the commerce blocks. It uses the product and listing blocks that the project already has, and otherwise expects the `product-details` and `product-list-page` blocks of the [commerce storefront boilerplate](https://experienceleague.adobe.com/en/tools/commerce-storefront/boilerplate/). Start the project from that boilerplate, and connect the storefront to your catalog, so that the imported pages show products when you check them. The add-on itself needs no license, but the storefront's drop-in components require an Adobe Commerce as a Cloud Service or Adobe Commerce Optimizer license. Adobe Commerce Optimizer can also supply the catalog when another commerce platform handles the cart, checkout, and orders. See [Backend options](https://experienceleague.adobe.com/en/tools/commerce-storefront/get-started/backends/).

For another commerce platform without Adobe Commerce Optimizer, the add-on doesn't apply. The agent has no skills for other commerce platforms, so give it the platform's current documentation and ask it to read it first. It can then build product and listing blocks that load their data from the platform's API. See [Work Beyond Edge Delivery Services](prompting-guide.md#beyond-eds).

The add-on works with [document-based persistence](overview.md#document-based). For projects with [JCR persistence](overview.md#jcr-persistence), the agent uses the standard migration, which imports what each product page shows at that moment. Decide with your team how those pages connect to the catalog.

## Update an Existing Block {#update}

Provide the block name, current examples/variants, requested change, and compatibility requirements.

1. Identify pages using the block, shared styles/utilities, and existing tests.
1. State what must remain unchanged, including existing content structures and interactions.
1. Make the change. A presentation change is CSS or JavaScript only, so it doesn't touch content models or require reimporting content.
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

There is no separate refactoring command: you ask in chat, and the agent changes the code as a developer would, within the invariants you set.

## Validate and Deliver {#validation}

Use the project's declared lint and test commands, plus browser checks on real content. Ask the agent to report the commands and results, not simply that it tested.

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
