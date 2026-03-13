---
title: Prompting Guide for Experience Modernization Agent
description: This guide provides tips for effective prompting of the Experience Modernization Agent and describes what its skills do.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
exl-id: 4771606b-a327-48b3-b142-44e03e4dc41d
---
# Prompting Guide for Experience Modernization Agent {#prompting-guide}

The Experience Modernization Agent automatically selects the appropriate skill based on natural-language requests. This guide provides tips for effective prompting and describes what the skills do.

## General Tips {#general-tips}

### Some skills depend on outputs from other skills. {#dependency}

* Because bulk import needs the import infrastructure that page migration creates, migrate at least one page before running bulk import.
* Since block CSS references the global design tokens, complete the site-wide design before styling individual blocks.

### The AI follows structured workflows and will ask clarifying questions when it needs more information. {#workflows}

* Trust the process and answer these qualifying questions as they come up.
* Do not try to front-load all requirements in the initial prompt.

### Create markdown files in the project to document project-specific rules, guidelines, design decisions, or constraints. {#markdown-files}

* These markdown files (e.g., INSTRUCTIONS.md, CONTEXT.md) can include file naming conventions, content mapping rules, or brand guidelines.
* When starting a new conversation, ask the agent to "warm up by reading the project documentation" so it loads this context before proceeding with tasks.

### The agent's context window is not infinite. {#limited-window}

* Over long conversations, earlier instructions may be compacted or forgotten.
* If the agent seems to have lost context, either remind it of the key points or clear the chat and start fresh with a warm-up prompt to read project documentation.

### Use iterative prompting to refine results. {#iterate}

* If something doesn't look right (e.g., wrong background color on a block), prompt the agent to fix the specific issue rather than starting over.

## Site Creation and Migration Skills {#site-migration}

The Site Modernization Agent offers many skills for creating new Edge Delivery Services sites and migrating existing websites. Any new Edge Delivery Site site or migration project should leverage these skills.

### Migrate a site or page to AEM {#migrate-a-site}

Use this prompt when migrating content from an existing website to Edge Delivery Services.

#### Example Prompts {#example-migrate}

* "Migrate this page: `https://example.com/about`
* "Migrate these pages: URL1, URL2, URL3"

#### What to Know {#wtk-migrate}

* Migration follows a seven-step workflow:
  1. The agent scrapes source page.
  1. It identifies section structure.
  1. It performs authoring analysis.
  1. It maps the content to block variants.
  1. It generates markdown.
  1. It creates import infrastructure.
  1. It previews the result.
* The agent analyzes pages using a two-level hierarchy:
  * First it identifies section boundaries (background changes, spacing shifts)
  * Then it identifies content sequences within each section.
* Authoring analysis follows [David's Model.](https://www.aem.live/docs/davidsmodel)
  * for each content sequence, it first checks "Can an author create this by normal typing?"
  * Default content (headings, paragraphs, lists, inline images) is preferred over blocks.
* The agent attempts to reuse existing blocks from the repository's block library before creating new ones.
  * When content can not be mapped to an existing block, it creates new block variants.
  * You can prompt for changes, request new variants, or adjust mappings interactively.
* Block variants are tracked with metadata.
  * When migrating multiple pages, the agent loads existing custom variants first and reuses them when styling matches (70% similarity threshold based on purpose, colors, typography, spacing, layout).
* Header, navigation, and footer are excluded from page migration. These are handled by dedicated skills.
* Each migration creates import infrastructure (page templates, block parsers, transformers) for future bulk imports.

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
  * Mixing templates in a single run is not supported.

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

Use this prompt to extracting content, metadata, and images from a source URL for analysis or migration.

#### Example Prompts {#example-scraping}

* "Scrape this page for analysis: `https://example.com`"
* "Extract content from `https://example.com/product`"

#### What to Know {#wtk-scraping}

* This prompt is usually invoked automatically as the first step of page migration.
* Content hidden via CSS is captured too if present in the DOM.
* Lazy-loaded images and client-side rendered content is handled by scrolling through the page in headless Chromium and letting scripts execute.
* WebP/AVIF/SVG images are converted to PNG for compatibility.
* Metadata is extracted including title, description, Open Graph tags, JSON-LD structured data, canonical URL.
* Images in DOM are fixed.
  * background-image is converted to img.
  * Picture elements are unwrapped
  * srcset is resolved to src
  * Relative URLs are converted to absolute
  * Inline SVG to are converted to img files.
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

#### What to Know {#wtk-design}

* Design migration has two phases:
  1. Phase 1 (site-wide) extracts the following to `styles/styles.css`:
     * Global color palette and accent colors
     * Typography system (fonts, sizes, weights)
     * Spacing system (padding, margins, gaps)
     * Section backgrounds (light, dark, colored)
     * Base component styles (buttons, links, images)
     * Outputs to 
  1. Phase 2 migrates individual block styles and creates block-specific CSS in `/blocks/{name}/{name}.css`.
* Block styling (phase 2) requires site-wide design (phase 1) to be complete first.
  * The global design system provides CSS custom properties that blocks reference.
* Estimated time:
  * Phase 1: 5-10 minutes
  * Phase 2: 10-15 minutes
* Ambiguous requests default to complete migration (both phases).

### Block Critique {#block-critique}

Use this prompt to validate and refine individual migrated blocks and ensure visual accuracy against the original website.

#### Example Prompts {#example-block-critique}

* "Critique hero block"
* "Validate block custom-cards"

#### What to Know {#wtk-block-critique}

* Block critique compares a migrated block against its original source and iteratively applies CSS fixes until an 85% visual similarity is achieved or three iterations are completed.
* The skill requires the block to have been created by page migration first.
* A block critique follows a six-step workflow:
  1. It captures the original block from source page using an XPath selector.
  1. It initializes the critique session.
  1. It inspects the original block (screenshots, styles, HTML).
  1. It inspects the migrated block.
  1.  It compares elements and generates a similarity score with CSS fixes.
  1. It applies fixes and re-inspects until the 85% target is reached.
* Each iteration displays a complete critique report with all differences, applies all CSS fixes (prioritized by visual impact), verifies in preview, re-inspects, and shows improvement metrics.
* Use the block critique after [design migration](#design-migration) is complete.

### Page Critique {#page-critique}

Use this prompt to validate entire migrated pages for full-page visual fidelity against the original website.

#### Example Prompts {#example-page-critique}

* "Critique the about page"
* "Validate the migrated page against `https://example.com/about`"

#### What to Know {#wtk-page-critique}

* Page critique performs a full-page visual comparison between the original and the migrated page, iterating until reaching an 85% similarity target or three iterations are completed.
* A page critique has a five-step workflow:
  1. It Initializes a critique session.
  1. It inspects all elements on the original page.
  1. It inspects all elements on the migrated page.
  1. It compares and generates a similarity score with prioritized CSS fixes.
  1. It applies fixes and re-inspects until the 85% target is  reached.
* A page critique needs the source page URL and the migrated path (e.g.,"/about") as input.
* Use page critique when validating overall page fidelity or validating multiple blocks simultaneously.
* [Use block critique](#block-critique) for focused validation on specific components.
* The following workflow is recommended:
  1. Migrate a page.
  1. Apply a design.
  1. Run a block critique on key blocks
  1. Run ap age critique for full validation.

### Figma Block Migration {#figma-block-migration}

Use this prompt to migrating a block from Figma design to Edge Delivery Services.

Note that you must set up your Figma details in [the Experience Modernization Console](/help/ai-in-aem/agents/brand-experience/modernization/console.md) to use this prompt.

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
  1. **Asset download** — The agent saves images and icons from Figma to the hosted environment's workspace.
  1. **Edge Delivery Services content generation** — The agent creates the markdown file following EDS block structure
  1. **Output validation** — The agent previews the result and performs visual comparison against the original Figma design.
* The skill first reads metadata (step 1) to understand structure, and then extracts detailed design context (steps 2-5).
  * This phased approach prevents issues with large or complex Figma files.
* This skill takes a styles-first approach.
  * All styles are extracted as CSS custom properties (design tokens) before any CSS is written.
  * This ensures the migrated block stays consistent with your design system.
* The prompt requires the Figma URL (with `fileKey` and optional `node-id`) or a Figma file key directly as input.

### Navigation Setup {#navigation-setup}

Use this prompt to set up or migrate site navigation.

#### Example Prompts {#example-navigation}

* "Set up navigation from `https://example.com`"
* "Fix the navigation menu"

#### What to Know {#wtk-navigation}

* Edge Delivery Services navigation enforces a three-section structure (enforced by `header.js`):
  1. **Brand** (section 1): Logo and primary branding link
  1. **Sections** (section 2): Main navigation menu with optional dropdowns
  1. **Tools** (section 3): Utility links (subscribe, login, cart)
* Navigation content lives in `nav.md` in the root directory.
* Sections are separated by (`---`) markers.
* Bold items (`**Text**`) with nested lists create dropdowns.
* Links in navigation may render as buttons due to Document Authoring's auto-wrapping behavior.
  * The header block includes code to strip button classes from nav links.

## Block Development Capabilities {#block-development-capabilities}

These prompts are used for creating and evolving blocks, providing continuous value beyond initial site creation or migration.

### Block Development {#block-development}

Use this prompt to create new blocks or modify existing ones.

#### Example Prompts {#example-block-development}

* "Create a testimonials block"
* "Add a video background variant to the hero block"

#### What to Know {#wtk-block-development}

* The agent follows Content-Driven Development (CDD), a mandatory process for all Edge Delivery Services development.
  * It will ask about content models and test content before writing code.
* The CDD philosophy is that author needs come before developer needs.
  * Content models must be intuitive for authors, even if that means more complex decoration code.
* Creating test content first provides:
  * Immediate testing capability
  * PR validation links for PSI checks
  * Living documentation for authors
  * Discovery of edge cases that code-first approaches miss
* The agent will search for similar blocks in the [Block Collection](https://www.aem.live/developer/block-collection) and [Block Party](https://www.aem.live/developer/block-party/) before implementing, to find patterns and reusable code.
* Skip CDD only for trivial CSS-only tweaks (but still identify test content for validation).

### Content Modeling {#content-modeling}

Use this prompt to design the table structure that authors work with when creating block content.

#### Example Prompts {#example-modeling}

* "Design a content model for a testimonials block"
* "What's the best content model for this carousel?"

#### What to Know {#wtk-modeling}

* Edge Delivery Services has four canonical model types:
  * **Standalone:** Distinct visual/narrative elements (hero, blockquote)
    * Single table with block content
  * **Collection:** Repeating semi-structured content (cards, carousel)
    * Table with repeating row pattern
  * **Configuration:** API-driven or dynamic content where config controls display (blog listing, search results)
    * Table with key-value config rows.
  * **Auto-Blocked:** Complex structures that authors create as sections/default content, then get transformed (tabs, YouTube embeds)
* There is a limit of four cells per row.
  * Group related elements into cells.
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
  * It also includes sidekick plugins, build tools (webpack, vite, sass), and integrations.
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
* The top ten most relevant results returned by default.

### Testing {#testing}

Use this prompt to validate code changes before opening a pull request.

#### Example Prompts {#example-testing}

* "Test the new cards block"
* "Run the tests before I open a PR"

#### What to Know {#wtk-testing}

* Testing follows a "value vs. cost" philosophy where you create and maintain tests when their value exceeds cost.
  * **Keeper tests** (unit tests) are for logic-heavy utilities, data processing, API integrations. These are fast, easy to maintain, and catch regressions in reused code.
  * **Throwaway tests** (browser tests) are for DOM transformations and visual validation. Use to validate implementation, capture screenshots for PR review, then discard.
* Throwaway tests go in `test/tmp/` and test content in `drafts/tmp/` (both gitignored).
* Before opening a PR, ensure that:
  * Existing tests pass
  * Unit tests are written for new logic
  * Browser validation is complete
  * All variants are tested
  * Responsive behavior is verified
  * Linting passes

### Debugging {#debugging}

Use this prompt to troubleshoot problems with blocks, images, CSS, or preview.

#### Example Prompts {#example-debugging}

* "Debug why images show as about:error"
* "Fix the hero block not rendering"
* "Why aren't my changes showing in preview?"

#### What to Know {#wtk-debugging}

* Common issues have known patterns:
  * **Images showing "about:error"**: Usually missing `createOptimizedPicture` call in block JS, or called before DOM restructuring
  * **Blocks not rendering**: Check block name format in markdown and verify that the block has both `.js` and `.css` files in `blocks/`.
  * **CSS not loading**: Check file paths, verify CSS file exists, and check the Network tab in browser.
  * **Changes not appearing**: Code sync takes 3-5 seconds. Try hard refresh (Ctrl+Shift+R).
* The agent checks each layer systematically:
  1. Source files
  1. Rendered output
  1. Block code
  1. Browser console
* The agent has the capability to check local previews at `http://localhost:3000`.

<!--
## Additional Sections {#additional-sections}

@gwalt, is the additional content in the prompting guide wiki ready to be added here?
-->
