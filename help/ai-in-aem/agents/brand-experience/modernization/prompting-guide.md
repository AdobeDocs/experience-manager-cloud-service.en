---
title: Prompting Guide for Experience Modernization Agent
description: This guide provides tips for effective prompting of the Experience Modernization Agent and describes what its skills do.
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

The Experience Modernization Agent (EMA) uses skills: built-in workflows for specific kinds of tasks, such as migrating a page or styling a block. The agent selects the appropriate skill from your natural-language request, so you don't need to name it. Some skills belong to [optional capabilities](console.md#optional-capabilities), which EMA offers to turn on for your project when a request needs them.

This guide provides tips for effective prompting and describes what the skills do. For the EDS terms used here, such as blocks, default content, and sections, see [How EDS Pages Work](overview.md#eds-basics).

## Choose a Task {#choose-task}

Use the task guides for the full procedure and acceptance checks. The prompts below are starting points, not commands that bypass project permissions or review.

| Task | Procedure |
|---|---|
| Customer demo pages | [Demo recipe](getting-started.md#customer-demo) |
| Useful trial with brand-owned content | [Start with Auto mode](getting-started.md#brand-trial) if your account has access, or [start from an EDS repository](getting-started.md#repo-start) |
| Production site, either persistence target | [Production migration](production-migration.md) |
| New design during migration | [Restyle during migration](restyling.md#during-migration) |
| Restyle an existing EDS project | [Existing-site restyle](restyling.md#existing-site) |
| Create, update, or refactor blocks | [Block development recipes](block-development.md) |

Name the source URLs/design nodes, destination paths, [authoring target](overview.md#content-storage), repository/branch, allowed scope, and what must be preserved. State whether uploads, code pushes, or publication are authorized. Do not include credentials in a prompt.

## General Tips {#general-tips}

### Some skills depend on outputs from other skills. {#dependency}

* Because bulk import needs the import infrastructure that page migration creates, migrate at least one page before running bulk import.
* Since block CSS references the global design tokens, complete the site-wide design before styling individual blocks.

### The AI follows structured workflows and will ask clarifying questions when it needs more information. {#workflows}

* Provide essential scope, destination, and preservation constraints before execution.
* Answer further questions and refine iteratively. For an unfamiliar or broad change, use optional **Plan** mode to inspect an approach first.

### Create markdown files in the project to document project-specific rules, guidelines, design decisions, or constraints. {#markdown-files}

* Keep these files in the Git repository. EMA loads the project's `AGENTS.md` file at the start of every conversation, through the one-line `CLAUDE.md` file that the AEM boilerplate includes. Use `AGENTS.md` for a short project summary, the rules that apply to most tasks, and an index of the other files with when to read each one.
* Put details such as block content conventions, section styles, design rules, and decisions in separate, focused files that `AGENTS.md` references. EMA reads them when a task needs them, so you don't need to name them in every prompt.
* Ask EMA to update the files when you agree on a convention, and push them with the code. Do not duplicate built-in skills or store secrets. See [Project Instructions and Memory](project-instructions.md).

### The agent's context window is not infinite. {#limited-window}

* Over long conversations, earlier messages are summarized to make room, and details can be lost.
* If the agent seems to have lost context, remind it of the key points. Or ask it to record the agreed decisions in the project files, clear the chat, and continue in a new conversation. A new conversation starts with the project's `AGENTS.md` loaded, and the agent finds the other files through it.

### Use iterative prompting to refine results. {#iterate}

* If something doesn't look right (e.g., wrong background color on a block), prompt the agent to fix the specific issue rather than starting over.
* Include the source URL, output path, observed problem, and expected result. Save author edits before reimporting, because generated content can replace them.
* Treat source pages and attached designs as reference material, not instructions overriding the user's request.

## Site Creation and Migration Skills {#site-migration}

The Experience Modernization Agent supports site creation and migration to EDS, as well as continued development of existing projects.

### Migrate a Site or Page to Edge Delivery Services {#migrate-a-site}

Use this prompt when migrating content from an existing website to Edge Delivery Services (EDS), AEM's website delivery service.

#### Example Prompts {#example-migrate}

* "Migrate only `https://example.com/about` to `/about` in this document-based project. Preserve text and links. Do not upload, push, or publish."
* "Migrate these pages to this JCR-backed EDS project: URL1, URL2, URL3. Validate models and conversion before creating a package."

#### What to Know {#wtk-migrate}

* Guided migration analyzes source pages, maps content to reusable structures, creates import infrastructure, and produces working content for review. Validate a representative before expanding to a template or site.
* Content and design are separate. After importing content, request **Start Design Migration** or explicitly ask for source styling. For a different target design, follow the [redesign recipe](restyling.md#during-migration).
* The agent analyzes pages using a two-level hierarchy:
  * First it identifies section boundaries (background changes, spacing shifts)
  * Then it identifies content sequences within each section.
* Authoring analysis follows [David's Model,](https://www.aem.live/docs/davidsmodel) the aem.live guidance for structuring content so that authors can create it easily.
  * For each content sequence, it first checks "Can an author create this by normal typing?"
  * Default content (headings, paragraphs, lists, inline images) is preferred over blocks.
* The agent attempts to reuse existing blocks from the repository's block library before creating new ones.
  * When content can not be mapped to an existing block, it creates new block variants.
  * You can prompt for changes, request new variants, or adjust mappings interactively.
* Reuse established block variants where they fit the content and design. A variant that looks right can still structure content differently from what authors expect, so check the authored result.
* Header, navigation, and footer are excluded from page migration. These are handled by dedicated skills.
* Each migration creates import infrastructure (page templates, block parsers, transformers) for future bulk imports.
* Image handling can preserve source Dynamic Media URLs, including older Scene7 URLs, for both persistence targets. Scene7 is the earlier name of Dynamic Media. Verify access, intended transformations, and delivery in the target rather than assuming every source image has been copied.

### Site Catalog {#site-catalog}

Use this prompt to analyze an existing website in order to understand its scale, templates, and block variants before starting a migration. The results can be used for [bulk imports.](#bulk-import)

#### Example Prompts {#example-prompts-site-catalog}

* "Scope site `https://example.com`"
* "Find templates on `https://example.com`"
* "Catalog site `https://example.com`"
* "How many page types are there on `https://example.com`"
* "What are the layouts on `https://example.com`"

For details on the site catalog skill, please see the document [Site Catalog Skill.](site-catalog.md)

### Bulk Import {#bulk-import}

Use this prompt to import many pages of the same template after completing an [initial single-page migration.](#migrate-a-site)

#### Example Prompts {#example-prompts-bulk-import}

* "Run the bulk import on these pages: URL1, URL2, URL3."
* "Run bulk import on all product pages."
* "Bulk import these blog pages: URL1, URL2."

#### What to Know {#wtk-bulk-import}

* Bulk import depends on import infrastructure created during a prior single-page migration.
  * This includes page templates (section structure), transformers (site-wide DOM cleanup), and parsers (block-specific HTML to table conversion).
* You must migrate at least one representative page per template before bulk import can run.
* Bulk import reuses the structure and mappings established during single-page migration.
  * It does not infer templates from scratch.
* Transformers operate on the entire DOM before and after parsing. Parsers operate at the individual block level.
* All parsers are validated before bulk import can proceed.
* One template corresponds to one bulk import configuration.
  * The import script is written for one template's structure, so each run covers pages of one template.

#### Typical Workflow {#typical-workflow}

The recommended workflow is iterative: validate on a small set first, then scale up.

1. **Run a single-page migration first.** - Migrate one representative page for the template you plan to bulk import.
   * This creates the required import infrastructure.
1. **Run the bulk import on a small set of pages.** - Ask the agent to run the bulk import and provide a short list of URLs that follow the same template.
1. **Review and refine the results.** - Inspect the imported pages.
   * If anything looks incorrect, ask the agent to adjust parsers, transformers, or import logic.
1. **Scale up.** - When results look correct, provide the full list of URLs.
   * The agent will reuse the same import logic and run bulk import at scale.

### Scraping Webpages {#scraping-webpages}

Use this prompt to extract content, metadata, and images from an authorized source URL for analysis or migration.

#### Example Prompts {#example-scraping}

* "Scrape this page for analysis: `https://example.com`"
* "Extract content from `https://example.com/product`"

#### What to Know {#wtk-scraping}

* This prompt is usually invoked automatically as the first step of page migration.
* Content hidden via CSS is captured too if present in the DOM.
* The extraction workflow loads the page in a browser, so it captures content that scripts insert, and it scrolls the page so that lazy-loaded images load. Content that appears only after a click or typing isn't in the page at that moment. Check the screenshot and add what's missing.
* Check the extracted image assets and formats against the source, including responsive images, backgrounds, and SVGs.
* Metadata is extracted including title, description, Open Graph tags, JSON-LD structured data, canonical URL.
* Source markup and image references can be normalized during extraction. Check that the selected rendition, links, and image meaning remain correct.
* Sanitized document paths are generated (lowercase with no `.html` extension).
* The following outputs are produced:
  * `screenshot.png`
  * `cleaned.html` (no scripts/styles)
  * `metadata.json`
  * `images/` folder with local copies
* Users can ask about screenshot dimensions and request specific device sizes (mobile, desktop) for content extraction.
* Extracting content at multiple breakpoints increases processing time.

### Design Migration {#design-migration}

Use this prompt to extract and apply visual design from a source site to Edge Delivery Services.

#### Example Prompts {#example-design}

* "Migrate the design from `https://example.com`"
* "Extract design tokens"
* "Style the hero block"
* "Style all the blocks"

#### What to Know {#wtk-design}

* Design migration has two phases:
  1. Phase 1 (site-wide) generates `styles/brand.css` and `styles/styles.css`:
     * `brand.css` contains design tokens as CSS custom properties (fonts, colors, spacing, heading sizes).
     * `styles.css` imports `brand.css` and applies the tokens to default content (headings, paragraphs, buttons, links, section backgrounds).
     * If your project already has a `brand.css`, prompt the agent to use it instead of extracting from the source.
  1. Phase 2 styles individual blocks in parallel and creates block-specific CSS in `/blocks/{name}/{name}.css`, referencing the tokens from `brand.css`.
* Block styling (phase 2) requires site-wide design (phase 1) to be complete first.
* Existing projects may use different token files. Ask the agent to use them rather than create a second set of tokens.
* State whether the request is global, block-specific, faithful to the source, or a redesign. Check the result on real pages at desktop and mobile widths. The design is CSS applied to the imported content, so a fix in `brand.css` or a block's CSS applies to every page that uses it.

### Block Critique {#block-critique}

Use this prompt to validate and refine individual migrated blocks and ensure visual accuracy against the original website.

#### Example Prompts {#example-block-critique}

* "Critique hero block"
* "Validate block custom-cards"

#### What to Know {#wtk-block-critique}

* Block critique compares a migrated block with its source and can apply content or styling fixes. It compares how they look, so it doesn't show that authors can edit the block or that its interactions work. Check those separately.
* The skill requires the block to have been created by page migration first.
* Critique detects and fixes both **content/structural issues** and **styling issues**:
  * Content/structural: missing headings, paragraphs, links, wrong table row/cell count — fixed by updating parsers and reimporting.
  * Styling: CSS differences in colors, spacing, typography, layout — fixed by updating block CSS.
* The fix cascade runs in order: global styles → section transformers → content/structural parsers → block CSS. Each layer is reimported and re-assessed before moving to the next.
* Use the block critique after [design migration](#design-migration) is complete.

### Site Critique {#site-critique}

Use this prompt to validate all migrated blocks across your site in a single pass, ideal for multi-page migrations.

#### Example Prompts {#example-site-critique}

* "Critique site"
* "Validate all blocks across the migrated site"

#### What to Know {#wtk-site-critique}

* Site critique checks migrated blocks across templates. Review the reported coverage and unresolved issues.
* It applies the same fix cascade as block critique (global styles → section transformers → content/structural parsers → block CSS), but across all pages simultaneously.
* Fixes are deduplicated — if the same issue appears on multiple pages using the same block, the fix is applied once.
* If `brand.css` does not exist yet, critique runs in content-structural-only mode (fixing parsers and transformers without styling).
* Site critique is the recommended approach after design migration for multi-page projects.
* The following workflow is recommended:
  1. Migrate pages (single or bulk).
  1. Run design migration.
  1. Run `critique site` to validate and auto-fix remaining gaps across all templates.

### Page Critique {#page-critique}

Use this prompt to validate a single migrated page for visual fidelity against the original website.

#### Example Prompts {#example-page-critique}

* "Critique the about page"
* "Validate the migrated page against `https://example.com/about`"

#### What to Know {#wtk-page-critique}

* Page critique checks a single page using the same layers: global styles, sections, content, and block styling. Inspect remaining differences rather than accept a numerical threshold.
* Requires the source page URL and the migrated path (e.g., "/about") as input.
* Use page critique for single-page refinement after site critique, or for targeted validation.
* For multi-page projects, [use site critique](#site-critique) instead — it handles all pages and deduplicates fixes automatically.

### Figma Block Migration {#figma-block-migration}

Use this prompt to migrate a block from Figma design to Edge Delivery Services.

Note that you must set up your Figma details in [the Experience Modernization Console](console.md) to use this prompt. Figma import is an [optional capability](console.md#optional-capabilities). If it is not on for your project, EMA offers to turn it on.

#### Example Prompts {#example-figma}

* "Migrate the block `https://figma.com/design/{fileKey}?node-id={nodeId}` to Edge Delivery Services"
* "Migrate `{blockName}` from `https://figma.com/file/{fileKey}` to Edge Delivery Services"

#### What to Know {#wtk-figma}

* This skill migrates one block at a time, not entire pages or full Figma files.
* For best results:
  * Select the specific block you want to migrate in Figma and copy its link (with `node-id`) or name.
  * Provide the `node-id` parameter in the URL to target the exact block.
* When you run this skill, the following steps are performed automatically in the hosted environment:
  1. **Block structure discovery** — The agent reads the Figma node to understand layers and components.
  1. **Global style extraction** — The agent pulls colors, typography, and spacing into `styles/styles.css` as CSS custom properties (design tokens).
  1. **Block-specific style creation** — The agent creates additional CSS custom properties specific to the block being migrated.
  1. **Mapping to existing blocks** — The agent identifies the closest matching block in your project's block library and creates a custom variant.
  1. **CSS generation** — The agent writes styles that reference the extracted CSS custom properties, ensuring design consistency.
  1. **Asset download** — The agent saves images and icons from Figma to the console workspace.
  1. **Edge Delivery Services content generation** — The agent creates the markdown file following Edge Delivery Services block structure
  1. **Output validation** — The agent previews the result and performs visual comparison against the original Figma design.
* The skill first reads metadata (step 1) to understand structure, and then extracts detailed design context (steps 2-5).
  * This phased approach prevents issues with large or complex Figma files.
* This skill takes a styles-first approach.
  * All styles are extracted as CSS custom properties (design tokens) before any CSS is written.
  * This ensures the migrated block stays consistent with your design system.
* The prompt requires the Figma URL (with `fileKey` and optional `node-id`) or a Figma file key directly as input.

### Redesign Migration Using Figma-Derived Blocks {#figma-redesign-migration}

Use this prompt when an existing website is being migrated into a redesigned experience.

In this workflow, you first create the target block collection from Figma. The site migration then runs against the live source website and maps source content into the blocks that were created from Figma.

* **Figma** is the target design and block-library source.
* **The live website** remains the source of content.

#### Example Prompts {#example-figma-redesign}

1. Create the block collection from Figma:

   * "Create the Edge Delivery Services block collection from these Figma components: `https://figma.com/design/{fileKey}?node-id={nodeId}`"

1. Migrate source content into those blocks:

   * "Migrate these pages and map the content to the Figma-derived block collection: URL1, URL2, URL3"

#### What to Know {#wtk-figma-redesign}

* Figma is used first to establish the redesigned block set.
* Site migration then maps real website content into that block set.
* **Content validation** is done against the source website.
* **Visual validation** is done against the Figma-derived block collection and design system.
* New block variants should be created only when existing Figma-derived blocks cannot represent the source content.

#### Recommended Workflow {#figma-redesign-workflow}

1. Identify the Figma components needed for the redesigned site.
1. Migrate those components into Edge Delivery Services blocks or variants.
1. Review the generated block collection and design tokens.
1. Run site migration on representative source pages.
1. Map source content into the Figma-derived blocks.
1. Validate content against the source website.
1. Validate visual output against the target Figma design.
1. Refine blocks or mappings, then scale to more pages.

### Create a New Page from Figma {#figma-new-page-from-figma}

Use this prompt when the page does not already exist on a source website and a Figma page or frame should drive creation of a new Edge Delivery Services page.

#### Example Prompts {#example-figma-new-page}

* "Migrate this Figma page to Edge Delivery Services: `https://figma.com/design/{fileKey}?node-id={nodeId}`"

#### What to Know {#wtk-figma-new-page}

* This prompt works best with a **specific Figma frame or page**, not an entire file.
* The frame should be organized into **clear page sections**.
* Sections are mapped to existing blocks, default content, or new variants.
* Text and assets come from Figma.
* A Figma frame shows how a feature looks, not where its data comes from or how it behaves. For search, calculators, personalization, or store locators, the Figma migration creates the layout. Then ask EMA to build the behavior as a [dynamic block](block-development.md#dynamic-blocks), and give it the API or data source.

### Navigation Setup {#navigation-setup}

Use this prompt to set up or migrate the site header, navigation, and footer. EMA migrates them, including footer images, with dedicated skills, separately from page import, so that every page shares one header and one footer.

#### Example Prompts {#example-navigation}

* "Set up navigation from `https://example.com`"
* "Migrate the footer from `https://example.com`"
* "Fix the navigation menu"

#### What to Know {#wtk-navigation}

* The standard header implementation uses three sections. Check the project's `header.js` before applying this convention:
  1. **Brand** (section 1): Logo and primary branding link
  1. **Sections** (section 2): Main navigation menu with optional dropdowns
  1. **Tools** (section 3): Utility links (subscribe, login, cart)
* Document-based migration commonly creates `nav.md` at the content root. Confirm the remote navigation location and, for JCR-backed projects, its model and page configuration.
* Sections are separated by (`---`) markers.
* Bold items (`**Text**`) with nested lists create dropdowns.
* Navigation links can render as buttons when the project's button decoration applies to them. In the current boilerplate, this happens to a bold or italic link that is alone in its paragraph.
  * Check the project's `header.js`. The standard header removes button styling from the brand link.

## Block Development Capabilities {#block-development-capabilities}

These prompts are used for creating and evolving blocks, providing continuous value beyond initial site creation or migration.

### Block Development {#block-development}

Use this prompt to create new blocks or modify existing ones.

#### Example Prompts {#example-block-development}

* "Create a testimonials block"
* "Add a video background variant to the hero block"

#### What to Know {#wtk-block-development}

* The agent's development guidance follows Content-Driven Development (CDD): define the content and how authors create it first, then write the code.
  * It will ask about content models and test content before writing code.
* The CDD philosophy is that author needs come before developer needs.
  * Content models must be intuitive for authors, even if that means more complex decoration code.
* Creating test content first provides:
  * Immediate testing capability
  * PR validation links for PageSpeed Insights (PSI) checks
  * Living documentation for authors
  * Discovery of edge cases that code-first approaches miss
* The agent will check your project's existing blocks, then search for similar blocks in the [Block Collection](https://www.aem.live/developer/block-collection) and [Block Party](https://www.aem.live/developer/block-party/) before implementing, to find patterns and reusable code. To point it to your own block library, or to give it a reference page or screenshot, see [Prompt for a Block](block-development.md#block-prompts).
* Skip CDD only for trivial CSS-only tweaks (but still identify test content for validation).

### Content Modeling {#content-modeling}

Use this prompt to design the table structure that authors work with when creating block content.

#### Example Prompts {#example-modeling}

* "Design a content model for a testimonials block"
* "What's the best content model for this carousel?"

#### What to Know {#wtk-modeling}

* Useful content-model patterns include:
  * **Standalone:** Distinct visual/narrative elements (hero, blockquote)
    * Single table with block content
  * **Collection:** Repeating semi-structured content (cards, carousel)
    * Table with repeating row pattern
  * **Configuration:** API-driven or dynamic content where config controls display (blog listing, search results)
    * Table with key-value config rows. See [Build a Dynamic Block](block-development.md#dynamic-blocks).
  * **Auto-Blocked:** Complex structures that authors create as sections/default content, then get transformed (tabs, YouTube embeds)
* Keep authored tables to a few cells and group related elements naturally, so they are easy to author. This guideline is for authors; block code can read any table structure.
* For JCR-backed authoring, also define and validate the component models, mappings, and generated configuration. See [block development](block-development.md#create).
* Prefer block variants over config cells for styling differences.
* [Follow Postel's Law](https://en.wikipedia.org/wiki/Robustness_principle): Be flexible about input structure.
  * A hero block should work whether content is in one cell, split across two cells, or in separate rows.
* This skill is usually invoked automatically by Content-Driven Development during block creation.

### Finding Reference Blocks {#reference-blocks}

Use this prompt to look for existing implementations to use as starting points.

#### Example Prompts {#example-reference}

* "Find blocks similar to a pricing table"
* "What blocks are available for testimonials?"
* "Search Block Party for a tabs implementation"

#### What to Know {#wtk-reference}

* The [Block Collection](https://www.aem.live/developer/block-collection) is Adobe-maintained and vetted for best practices, excellent content modeling, high performance, and accessibility.
  * It is limited to commonly-needed blocks. Start here.
* The [Block Party](https://www.aem.live/developer/block-party/) is community-driven and offers a broader variety including experimental approaches.
  * It also includes plugins for the AEM Sidekick, the browser extension used to preview and publish EDS pages, as well as build tools (webpack, vite, sass) and integrations.
  * Use when the Block Collection doesn't have what you need.
* Think about alternative names when searching
  * FAQ = accordion
  * Gallery = carousel/slideshow
  * Navigation = menu/header
* The Block Party only returns approved/curated entries.

### Searching Documentation {#searching-documentation}

Use this prompt to find information about Edge Delivery Services features or implementation guidance.

#### Example Prompts {#example-documentation}

* "How do I implement lazy loading in Edge Delivery Services?"
* "Search the docs for section metadata"

#### What to Know {#wtk-documentation}

* It searches the [aem.live](https://aem.live) documentation (docs and blog posts) specifically.
* Use specific keywords ("block decoration","sidekick plugin","metadata") rather than generic terms ("aem","website","how to build").
* For code examples and reference implementations, use "find reference blocks" instead.
* Verify the returned documentation against the project's actual implementation and authoring target.

### Testing {#testing}

Use this prompt to validate code changes before opening a pull request.

#### Example Prompts {#example-testing}

* "Test the new cards block"
* "Run the tests before I open a PR"

#### What to Know {#wtk-testing}

* Testing follows a "value vs. cost" philosophy where you create and maintain tests when their value exceeds cost.
  * **Keeper tests** (unit tests) are for logic-heavy utilities, data processing, API integrations. These are fast, easy to maintain, and catch regressions in reused code.
  * **Browser checks** validate DOM transformations, interaction, and visual behavior. Keep useful regression tests and review evidence according to project practice.
* Use the project's declared test commands and content locations. Do not assume a folder is ignored or discard useful regression coverage.
* Before opening a PR, ensure that:
  * Existing tests pass
  * Unit tests are written for new logic
  * Browser validation is complete
  * All variants are tested
  * Responsive behavior is verified
  * Linting passes

### Debugging {#debugging}

Use this prompt to troubleshoot problems with blocks, images, CSS, or preview. For deeper EDS diagnostics, EMA can turn on the EDS troubleshooting [optional capability](console.md#optional-capabilities) for your project.

#### Example Prompts {#example-debugging}

* "Debug why images show as about:error"
* "Fix the hero block not rendering"
* "Why aren't my changes showing in preview?"

#### What to Know {#wtk-debugging}

* Common issues have known patterns:
  * **Images showing "about:error"**: Usually missing `createOptimizedPicture` call in block JS, or called before DOM restructuring
  * **Blocks not rendering**: Check block name format in markdown and verify that the block has both `.js` and `.css` files in `blocks/`.
  * **CSS not loading**: Check file paths, verify CSS file exists, and check the Network tab in browser.
  * **Changes not appearing**: Check each step separately: the change exists in the console workspace, the content was uploaded, the code was pushed, the preview URL names the right branch, and the content was previewed to `*.aem.page`. Refresh after verifying the intended versions are available.
* The agent checks each layer systematically:
  1. Source files
  1. Rendered output
  1. Block code
  1. Browser console
* The agent can inspect the console's preview of the workspace; you do not need to configure a local server for console onboarding.
* Preserve the failing URL/path and error details. Retry the smallest affected scope after correcting the cause. See [recovery and handover](production-migration.md#handoff) before overwriting or resetting work.
