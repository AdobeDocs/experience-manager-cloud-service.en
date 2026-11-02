---
title: Create, Update, and Refactor Blocks with the Experience Modernization Agent
description: Develop lightweight Edge Delivery Services blocks from author needs and real content, and preserve compatibility when updating or refactoring them.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Create, Update, and Refactor Blocks {#block-development}

Use EMA for ongoing EDS development as well as migration. Begin with the author need and real content, then choose the smallest implementation that supports them.

Connect the intended repository and branch, confirm modification permissions, and identify whether authors use document-based or JCR-backed content. Preserve a baseline before changing shared code or content models.

## Compose Before Creating a Block {#composition}

HTML elements are the basic building units, or atoms: headings, paragraphs, links, lists, and images. Authors should use default content for these where possible. Global styles and CSS custom properties, or design tokens, define shared typography, colors, spacing, and link/button presentation.

A block adds a reusable content structure or behavior where default content is insufficient. Keep it lightweight and focused; a visual difference alone does not always need a new block.

Check the project's conventions before generating code:

| Need | Decision to check |
|---|---|
| Call to action (CTA) | How an authored link becomes a button, which variants exist, and how the label and destination remain editable. |
| Button group | Whether adjacent links/default content already support the grouping, or a reusable model is needed for order, wrapping, and variants. |
| Footnote | How markers, target IDs, return links, and reading order are authored and preserved. |
| Repeated content | Whether an existing cards/list block or variant represents it without extra author fields. |

These are project conventions, not universal EMA authoring controls. Do not invent a button-group or footnote UI. Check the actual content model and rendered result.

## Create a Block {#create}

Provide the author task, example content, desired behavior/design, target persistence, and destination test page.

1. Ask EMA to inspect existing blocks and suitable [reference implementations](prompting-guide.md#reference-blocks). Prefer reuse or a variant over a duplicate.
1. Define a content model that authors can understand. Use headings, links, images, and grouped content naturally rather than exposing CSS or implementation details as fields.
1. Create representative content first. Include long text, missing optional values, multiple items, and meaningful images/links.
1. Implement only the needed HTML decoration, CSS, and JavaScript. Reuse project tokens and shared utilities.
1. For JCR-backed projects, update the source models/component configuration and regenerate aggregates through the project workflow. Check conversion and authoring hints. A document table alone does not establish a working Universal Editor model.
1. [Validate](#validation), then document an authorable example and allowed variants.

For example:

> Create a testimonials block for [authoring target]. Start from these real content examples: [paths]. Check existing blocks first. Authors need to edit quote, attribution, and optional image without layout configuration. Use our tokens. Include long text and no-image examples. Do not upload, push, or publish.

The output is reusable code, a working target-specific model where needed, and editable examples—not just a screenshot or generated files.

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

Review the diff, stage only intended files, and [push through the repository policy](getting-started.md#push-code-changes). Upload test or production content only when authorized; a code push does not save it.

For recovery, revert code through Git and restore changed remote content separately. Keep compatible old examples until any required content migration is accepted.

Use the [project handover](project-documentation.md#portable-handoff) to retain changed files, models, examples, validation results, remaining risks, and the recovery approach for the next person or agent.
