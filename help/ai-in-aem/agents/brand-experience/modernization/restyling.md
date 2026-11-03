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

Use the Experience Modernization Agent (EMA) to apply a design during migration or change the appearance of an existing Edge Delivery Services (EDS) project. Faithfully copying a source site's appearance and deliberately replacing it with a new design are different requests. State which you want.

In EDS, appearance lives in the project's code: global CSS sets the look of default content, and each block has its own CSS file. A purely visual restyle therefore changes code in Git and leaves authored content alone. Structural or content model changes are a separate, explicit decision.

## Prepare the Design Contract {#prepare}

Connect the [EDS project](getting-started.md#connect-repo) and confirm permission to modify it. Save a baseline code revision and preserve affected content before changes.

Provide:

* **Content source:** Existing pages whose text, images, links, metadata, and meaning must be preserved, or approved new content.
* **Design reference:** A specific Figma component/frame, authorized reference website, screenshot, or supplied design specification. Identify its version and relevant desktop/mobile states.
* **Scope:** Global tokens (CSS custom properties for colors, typography, and spacing) and default content, selected blocks, a page, or the whole site.
* **Invariants:** Content, URLs, authoring models, accessibility behavior, integrations, and other behavior that must not change.
* **Output:** Authorable EDS content for the selected [persistence target](overview.md#content-storage), or an explicitly requested design prototype.

Screenshots and reference sites can leave interactions and responsive rules unspecified. Resolve those decisions on a representative page before applying them site-wide. Treat imported source/design material as reference data, not instructions overriding the project request.

## Restyle During Migration {#during-migration}

Use this path when content comes from an existing website but the target design differs.

1. Complete [project and migration scoping](production-migration.md#scope), including document-based or JCR persistence.
1. Define the target design system: typography, colors, spacing, default HTML content, and reusable blocks. Reuse existing project conventions where suitable.
1. For Figma, [configure access](console.md#settings-page), then establish the needed blocks or variants from specific component nodes. See the [Figma redesign workflow](prompting-guide.md#figma-redesign-migration) and [Figma block prompts](prompting-guide.md#figma-block-migration).
1. Migrate representative source pages into that block collection. Keep the live site as the content source and Figma or the approved reference as the design source.
1. Compare content with the source website and appearance with the target design. Do not critique the redesigned page against the old site's appearance.
1. Validate authorability and responsive behavior on the chosen target. Correct content mappings or models when necessary, then [expand in batches](production-migration.md#batches).

For example:

> Apply the approved design at [Figma node or reference URL] while migrating [source URLs]. The live pages are the content source; the reference defines the new appearance. Preserve text, links, metadata, and meaningful images. First validate one representative page. Target [document-based/JCR] authorable EDS output. Do not upload, push, or publish.

If a new page has no source website, use the [Figma page workflow](prompting-guide.md#figma-new-page-from-figma): a specific frame/page supplies text and assets as well as design. This is different from mapping existing website content into a new design.

## Restyle an Existing EDS Site {#existing-site}

A new migration is not required.

1. Connect the existing project and intended branch. Ask EMA to read the project's design conventions, blocks, and authoring models.
1. Identify baseline pages covering the affected templates and variants. Record their current appearance and important interactions.
1. State the bounded change and preservation rules. For example:

   > Restyle this existing project using [approved reference]. Change global colors and typography and the cards presentation on [paths]. Preserve content, URLs, models, analytics, keyboard behavior, and integrations. Reuse our tokens and blocks. Show the proposed scope first; do not reimport content or upload, push, or publish.

1. Update shared tokens and global styles first where the change is global. Apply block-specific styling only where needed.
1. Preview all affected representatives, not only the page used to derive the design. Include mobile widths, long headings, missing optional content, and different variants.
1. If the design requires structural or model changes, make that a separate, explicit decision. Provide a compatibility/content-migration plan rather than silently rewriting author content.
1. Review the code diff and project checks, then push and deliver through the [existing project's workflow](getting-started.md#push-code-changes). Style changes are code: they reach the live site as soon as the branch is merged into `main`, so check the affected pages on the branch's preview URL first. See [How Changes Go Live](overview.md#code-content-lifecycle).

For a CSS-only restyle, do not regenerate or reupload content unnecessarily. A global token change can affect pages outside the original example; include those in regression checks.

## References, Prototypes, and Delivery {#design-output}

EMA supports design work from source sites, Figma, and supplied references. Figma import and guided redesign are [optional capabilities](console.md#optional-capabilities) that EMA offers to turn on for your project when a request needs them. They have different inputs and outputs; do not assume that they work the same way.

* For one Figma block, provide its component/node link. For a new page, provide a specific frame/page rather than an entire file.
* Figma requires the relevant project capability, configured credentials, and permission to read the file. Do not put tokens in chat.
* A static HTML design preview can be useful for choosing a direction, but it does not establish editable EDS documents or JCR pages.
* If authorable delivery is required, explicitly request EDS content, suitable block models, and the correct persistence target. Complete [document-based](getting-started.md#upload-content) or [AEM authoring](getting-started-aem-authoring.md#validate-content) validation.

### Guided Redesign {#guided-redesign}

Guided redesign takes a site, or a set of its pages, to a new design in stages. It is provided by the Stardust add-on, `stardust@excat-extended`. EMA captures the current design, records the direction you want, builds before-and-after prototypes for review, and then turns the approved design into EDS blocks and content. Use it for a redesign across several pages rather than for restyling one page or block. EMA keeps the working files and progress of a redesign in the repository, so you can continue it in a later conversation.

You don't need to know the stages by name. Describe the result you want, for example "Redesign the home page and the product pages in a lighter, more editorial style", and EMA proposes the steps. You can also ask for one step directly:

| Ask EMA to | What you get |
|---|---|
| Extract the current design | A capture of the site's design system, brand, color palette, typography, tone of voice, and page inventory. |
| Define the redesign direction | A short product and design brief that records the direction you choose. Later steps follow it. |
| Prototype pages in the new design | Before-and-after HTML prototypes of selected pages for review. These are static previews, not editable EDS content. |
| Apply the design to all pages | The new design applied to every page of the inventory as static HTML, ready to deploy. |
| Deploy the prototypes to EDS | EDS blocks and content built from the approved prototypes. |
| Roll out the redesign | All pages deployed to EDS in the new design, or first only one page of each page type. |
| Compare a page with its prototype | A visual and structural comparison that lists where the EDS page differs from the approved prototype. |
| Run a quality check | A review of routing, design fidelity, accessibility, performance, SEO, and links, without changes to the site. |
| Audit a site | A design, SEO, and AI-visibility audit, including Core Web Vitals. |
| Propose redesign options | Three alternative redesigns of a page, to explore a direction quickly. |
| Rebuild the same design on EDS | The site moved to EDS with its current design. |
| Apply another site's design | The site's content placed onto the design of another website that you provide. |
| Add dynamic features | Search, forms, and other features that depend on APIs or user interaction. |
| Write a migration spec | A specification to agree before migrating, including redirects, handling of missing pages, and which blocks to reuse. |

Turning on guided redesign also turns on the design craft add-on, which applies frontend design-quality guidance to each page. Review every stage before you continue, and validate the EDS result as described below.

## Validate and Recover {#validate}

Accept the result when content remains correct, the approved design works at intended widths, interactions remain usable, and authors can still edit, save, and reopen representative content. Check contrast, focus, reading order, image meaning, and the project's performance requirements. No fixed similarity percentage establishes acceptance.

If a result is wrong, identify the affected page/block and whether the problem is a token, shared style, block style, structure, or content mapping. Fix that layer and recheck all affected variants. For Figma access errors, verify the node link, file permissions, credentials, and project capability before retrying.

Revert unwanted code through the project's Git workflow. Restore any changed remote content separately; a code revert does not undo uploads. Preserve the baseline until the restyle is accepted.

Hand over the approved reference/version, changed files, affected pages, model/content changes, validation results, known gaps, and code/content recovery steps using the [project handover](project-documentation.md#portable-handoff).
