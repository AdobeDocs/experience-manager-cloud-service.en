---
title: Restyle Sites with the Experience Modernization Agent
description: Apply a new design during migration or restyle an existing Edge Delivery Services project while preserving content and authorability.
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

# Restyle Sites {#restyling}

Use the Experience Modernization Agent to apply a design during migration or change the appearance of an existing Edge Delivery Services project. Faithfully copying a source site's appearance and deliberately replacing it with a new design are different requests. State which you want.

Appearance lives in the project's code: global CSS sets the look of default content, and each block has its own CSS and JavaScript. Together they can give the same semantic content any design without restructuring it, because the JavaScript can rebuild the markup in the browser; see [Understand Your Project](overview.md#project-foundations). A purely visual restyle therefore changes code in Git and leaves authored content alone.

This guide is for the person who leads a restyle. If you are a designer making individual visual changes that a developer reviews, start with [Make Visual Changes](visual-changes.md).

## Agree What Changes and What Stays {#prepare}

Connect the [project](getting-started.md#connect-repo) and confirm permission to modify it. Save a baseline code revision and preserve affected content before changes.

Provide:

* **Content source:** Existing pages whose text, images, links, metadata, and meaning must be preserved, or approved new content.
* **Design reference:** A specific Figma component or frame, an authorized reference website, a screenshot, or a design specification. Name its version and the desktop and mobile states that matter.
* **Scope:** Global tokens (CSS custom properties for colors, typography, and spacing) and default content, selected blocks, a page, or the whole site.
* **What must not change:** Content, URLs, authoring models, accessibility behavior, and integrations.
* **Output:** Content that authors can edit, in the [storage option](overview.md#content-storage) that your project uses, or a static design prototype if that is all you need.

Screenshots and reference sites can leave interactions and responsive rules unspecified. Settle those on one sample page before you apply them to the whole site.

## Restyle During Migration {#during-migration}

Use this path when content comes from an existing website but the target design differs.

1. Complete [project and migration scoping](production-migration.md#scope), including where content is stored.
1. Define the target design system: typography, colors, spacing, default content, and reusable blocks. Reuse existing project conventions where they fit.
1. For Figma, [set up access](visual-changes.md#figma), then create the blocks or variants that you need from specific component nodes. See [Redesign with Blocks from Figma](prompting-guide.md#figma-redesign-migration) and [Create a Block from Figma](prompting-guide.md#figma-block-migration).
1. Migrate a sample page for each template into that block collection. Keep the live site as the content source and Figma or the approved reference as the design source.
1. Compare content with the source website and appearance with the target design. Don't judge the redesigned page against the old site's appearance.
1. Check that authors can edit the result and that it works at each screen width. Correct content mappings or models where needed, then [continue in batches](production-migration.md#batches).

For example:

> Apply the approved design at [Figma node or reference URL] while migrating [source URLs]. The live pages are the content source; the reference defines the new appearance. Preserve text, links, metadata, and meaningful images. Check one sample page first. Create content that authors can edit in [Experience Workspace or Experience Manager authoring]. Do not upload, push, or publish.

If a new page has no source website, see [Create a New Page from Figma](prompting-guide.md#figma-new-page-from-figma): a specific frame supplies the text and assets as well as the design. This is different from mapping existing website content into a new design.

## Restyle an Existing Site {#existing-site}

A new migration is not required.

1. Connect the existing project and intended branch. Ask the agent to read the project's design conventions, blocks, and authoring models.
1. Identify baseline pages covering the affected templates and variants. Record their current appearance and important interactions.
1. State the scope of the change and what must stay. For example:

   > Restyle this existing project using [approved reference]. Change global colors and typography and the cards presentation on [paths]. Preserve content, URLs, models, analytics, keyboard behavior, and integrations. Reuse our tokens and blocks. Show the proposed scope first; do not reimport content or upload, push, or publish.

1. Update shared tokens and global styles first where the change is global. Apply block-specific styling only where needed.
1. Preview all affected sample pages, not only the page used to derive the design. Include mobile widths, long headings, missing optional content, and different variants. A global token change can affect pages outside the original example, so include those too.
1. If the design requires structural or model changes, make that a separate, explicit decision. Plan how existing content moves to the new structure rather than silently rewriting author content.
1. Review the code diff and project checks, then push and deliver through the [existing project's workflow](getting-started.md#push-code-changes). Style changes are code: they reach the live site as soon as the branch is merged into `main`, so check the affected pages on the branch's preview URL first. See [How Changes Go Live](overview.md#code-content-lifecycle).

## References, Prototypes, and Delivery {#design-output}

The agent supports design work from source sites, Figma, and supplied references. Figma import and guided redesign are [optional capabilities](console.md#optional-capabilities) that it offers to turn on for your project when a request needs them. They have different inputs and outputs; do not assume that they work the same way.

* For one Figma block, provide its component or node link. For a new page, provide a specific frame rather than an entire file.
* Figma import needs a Figma access token and permission to read the file. See [Work from a Figma Design](visual-changes.md#figma).
* A static HTML design preview shows the new design on copies of your pages, which helps you choose a direction. Authors can't edit those copies; they aren't the site's documents or Experience Manager pages.
* If authors must edit the result, ask for site content and block models in the storage option that your project uses, then check them as described for [document-based content](getting-started.md#upload-content) or [Experience Manager authoring](getting-started-aem-authoring.md#validate-content).

### Guided Redesign {#guided-redesign}

Guided redesign takes a site, or a set of its pages, to a new design in stages. It is provided by the Stardust add-on, `stardust@excat-extended`. The agent captures the current design, records the direction you want, builds before-and-after prototypes for review, and then turns the approved design into blocks and content. Use it for a redesign across several pages rather than for restyling one page or block. The agent keeps the working files and progress of a redesign in the repository, so you can continue it in a later conversation.

You don't need to know the stages by name. Describe the result you want, for example "Redesign the home page and the product pages in a lighter, more editorial style", and the agent proposes the steps. You can also ask for one step directly:

| Ask the agent to | What you get |
|---|---|
| Extract the current design | A capture of the site's design system, brand, color palette, typography, tone of voice, and page inventory. |
| Define the redesign direction | A short product and design brief that records the direction you choose. Later steps follow it. |
| Prototype pages in the new design | Before-and-after HTML prototypes of selected pages for review. These are static previews, not editable pages. |
| Apply the design to all pages | The new design applied to every page of the inventory as static HTML, ready to deploy. |
| Deploy the prototypes to Edge Delivery Services | Blocks and content built from the approved prototypes. |
| Roll out the redesign | All pages deployed in the new design, or first only one page of each page type. |
| Compare a page with its prototype | A visual and structural comparison that lists where the deployed page differs from the approved prototype. |
| Run a quality check | A review of routing, design fidelity, accessibility, performance, SEO, and links, without changes to the site. |
| Audit a site | A design, SEO, and AI-visibility audit, including Core Web Vitals. |
| Propose redesign options | Three alternative redesigns of a page, to explore a direction quickly. |
| Rebuild the same design on Edge Delivery Services | The site migrated with its current design. |
| Apply another site's design | The site's content placed onto the design of another website that you provide. |
| Add dynamic features | Search, forms, and other features that depend on APIs or user interaction. |
| Write a migration spec | A specification to agree before migrating, including redirects, handling of missing pages, and which blocks to reuse. |

Turning on guided redesign also turns on the design craft add-on, which applies frontend design-quality guidance to each page. Review every stage before you continue, and validate the deployed result as described below.

## Validate and Recover {#validate}

The restyle is done when content remains correct, the approved design works at each screen width, interactions remain usable, and authors can still edit, save, and reopen the sample pages. Check contrast, focus, reading order, image meaning, and the project's performance requirements. A similarity score doesn't decide this for you.

If a result is wrong, identify the affected page or block and whether the problem is a token, shared style, block style, structure, or content mapping. Fix that layer and recheck all affected variants. For Figma access errors, check the node link, file permissions, token, and that Figma import is on for the project before you try again.

Revert unwanted code through the project's Git workflow. Restore any changed remote content separately; a code revert does not undo uploads. Keep the baseline until the restyle is signed off.

Hand over the approved reference and its version, changed files, affected pages, model and content changes, check results, known gaps, and how to recover code and content, using the [project handover](project-documentation.md#portable-handoff).
