---
title: Migrate a Production Site with the Experience Modernization Agent
description: Migrate and validate an Edge Delivery Services site with document-based or Experience Manager authoring persistence.
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

# Migrate a Production Site {#production-migration}

Use this workflow to move an agreed site inventory to Edge Delivery Services, the Adobe Experience Manager service that delivers websites. Start with representative pages, establish reusable content and design mappings, and expand only after those pages work in the chosen authoring environment. If terms such as blocks, default content, or preview are new to you, see [How Edge Delivery Services Works](overview.md#eds-basics).

For a few demonstration pages or an initial evaluation, use the smaller [demo and trial workflows](getting-started.md#first-outcome). Their completion criteria are different from production acceptance.

## Agree Scope and Destinations {#scope}

You need authorization to read the source, modify the target repository, and write content and assets to the destination. Agree who accepts the result and who authorizes release. If some pages require sign-in, set up [protected site authentication](console.md#protected-site-authentication) with a dedicated read-only account. If the source uses bot protection, arrange access with its administrator before cataloging. See [source sites with bot protection](getting-started.md#bot-protection).

Record:

| Input | Decisions to retain |
|---|---|
| Source inventory | Domains, page URLs, locales, documents, assets, and excluded or retired content. |
| Code | Repository, working branch, review policy, and release owner. |
| Content destination | Document-based persistence, edited visually in Experience Workspace, or Experience Manager authoring with JCR persistence and the Universal Editor. See [Where Content Is Stored and How Authors Edit It](overview.md#content-storage). |
| Design | Preserve the source appearance or [apply a new design](restyling.md#during-migration). Name the approved reference and version. |
| Behavior | Navigation, forms, search, commerce, consent, analytics, personalization, and other integrations that must work. Identify their owners. |
| URL policy | Destination paths, redirects, canonical URLs, language relationships, and links to retain. |
| Recovery | Code baseline, content backup/recovery process, and authority to overwrite or publish. |

The source CMS does not dictate destination persistence. Both targets deliver through Edge Delivery Services.

For a new implementation, Adobe strongly recommends document-based persistence with Experience Workspace, including for large sites with thousands of pages. Experience Manager authoring with JCR persistence remains fully supported when a specific requirement depends on content staying in Experience Manager.

Page import copies each page's content and design. Integrations and CMS features run on the source's servers, such as search, form processing, personalization rules, and content inheritance, so import copies only their output on each page. List them under **Behavior** and decide how each works on the new site. See [Limitations](overview.md#limitations).

## Prepare and Catalog {#prepare}

1. Follow [shared console setup](getting-started.md#repo-start), or [Experience Manager authoring setup](getting-started-aem-authoring.md#create-repo) for a JCR-backed project. Reuse an existing project's configuration rather than recreate it.
1. Ask the agent to catalog the authorized site: `Scope site https://www.example.com`. The [site catalog skill](site-catalog.md) discovers pages and groups them into templates (pages that share a layout) and block variants.
1. Review the [site planning UI](site-catalog.md#planning-ui). Correct template and block groupings and investigate failed URLs.
1. Reconcile discovered URLs against your agreed inventory. Include pages missing from discovery and make explicit decisions about failed, skipped, duplicate, or excluded URLs.
1. Select representatives for each template and important variant, including long content, unusual images, locales, and interaction-heavy pages.

Cataloging analyzes the source; it does not migrate or accept every page. A **complete** catalog run can still contain failures.

## Validate Representatives {#representatives}

Start with one template and a small set of pages. For example:

> Migrate only these authorized product pages: [URLs]. Target [document-based or JCR persistence] at [destination paths]. Preserve approved text, links, metadata, and image meaning. Reuse the project's blocks and content conventions. Report missing content and unsupported interactions. Do not upload, push, or publish.

1. Review content mapping. Headings, paragraphs, lists, and images stay default content, outside any block. Use a block only where authors need to mark which content forms a component, such as a set of cards, because the code can't infer it. A different look alone doesn't need a block: CSS and JavaScript can style default content and sections however the design requires. Authors will edit every migrated page in this structure, so settle it on the representatives. See [David's Model](https://www.aem.live/docs/davidsmodel).
1. Compare imported text, links, images, metadata, and section order against the source. Fix the reusable parser, transformer, or mapping when a pattern is wrong. These are the import scripts that the agent generates: a parser converts one block's source HTML, and a transformer cleans up the whole page.
1. Apply source styling or follow the [redesign workflow](restyling.md#during-migration). Check global styles before refining individual blocks.
1. Complete the shared header, navigation, and footer separately from page import. The agent migrates them, including footer images, with dedicated skills, so that every page shares one header and one footer.
1. Upload a representative to the chosen authoring destination and verify edit, save, reopen, and preview:
   * [Document-based upload and preview](getting-started.md#upload-content).
   * [JCR conversion, package upload, and Universal Editor validation](getting-started-aem-authoring.md#validate-content).
1. Record the accepted source-to-output mapping, models, design decisions, and known exceptions before expanding the batch.

A matching screenshot is insufficient if authors cannot maintain the result. For JCR-backed projects, check models, generated component configuration, conversion errors, and asset destinations before scaling.

## Import in Batches {#batches}

Use the [catalog bulk-import workflow](site-catalog.md#bulk-import) and [bulk-import prompts](prompting-guide.md#bulk-import) after validating representatives.

1. Import a small batch using the established template mapping.
1. Check both ordinary pages and edge cases. If a mapping is wrong, correct it and rerun the affected pages before expanding.
1. Keep a reconciliation record for each source URL: destination, imported state, errors, acceptance, and any approved exclusion.
1. Continue template by template. Track discovered, analyzed, imported, failed, skipped, and accepted pages separately.
1. Recheck earlier representatives when changing shared styles, parsers, transformers, models, or block code.

Before reimporting, compare the affected output with author edits already made in the target. Preserve or merge those edits; a corrected importer does not automatically reconcile them.

## Complete the Site {#complete-site}

Automated import is one part of delivery. Implement and verify the agreed requirements, including:

* Header, footer, navigation, internal links, and error pages.
* Images, downloads, fonts, asset permissions, and any retained Dynamic Media references.
* Titles, descriptions, canonical URLs, structured data, redirects, sitemaps, and locale relationships where required.
* Forms, search, commerce, account features, analytics, consent, and other integrations.
* Author guidance, operational ownership, access, and deployment configuration.

The agent implements the code side of these, for example blocks that call your search or commerce API, forms, and the code that loads analytics and consent. It can't configure systems outside your repository and content, such as the search service, the CDN, or the analytics account, and it doesn't decide your requirements. Give it the API documentation and the agreed behavior, and name an owner for each external system who accepts the result.

## Accept the Result {#acceptance}

Agree acceptance criteria with the site owner. Test against the actual target, not only the console preview.

| Area | Observable acceptance |
|---|---|
| Coverage | Every in-scope URL has an accepted destination or an approved exception. Failed and skipped pages are resolved or recorded. |
| Content | Text, links, assets, metadata, and locale content are complete and correct. |
| Authoring | Authors can edit representative fields and blocks, save, reopen, and preview the result in the chosen authoring environment. |
| Design | Approved desktop and mobile layouts work on real content, including long text and block variants. |
| Function | Navigation, keyboard interaction, forms, integrations, and agreed user journeys work. |
| Quality | Accessibility, performance, and relevant SEO and security checks meet the project's agreed requirements. Automated accessibility tools find only the issues that a rule can detect, so also test representative pages with a keyboard and a screen reader. Test performance with [PageSpeed Insights](https://pagespeed.web.dev/); on GitHub, Edge Delivery Services runs the same check on each pull request for the test URLs in its description. |
| Operations | Repository review, content publication, recovery, monitoring, and support ownership are documented and tested as needed. |

Each automated signal checks one thing: an importer status that the script ran, a generated package that content was converted, a visual similarity score that a page looks like its source, and a Lighthouse score how one page loads in a lab test. Production readiness needs every area in the table.

## Release, Recover, and Hand Over {#handoff}

1. Review and push the accepted code through the repository's policy. Merging into `main` updates the live site's code immediately; there is no separate code publish step. Plan the merge with the content release. See [How Changes Go Live](overview.md#code-content-lifecycle).
1. Upload only the accepted content and assets to the confirmed destination. Review per-page and per-asset errors.
1. Verify the saved content with the intended code revision on the preview site, `*.aem.page`.
1. Obtain the site's release approval and follow the configured publication and domain cutover process. Publishing makes pages available on `*.aem.live`; the cutover is what serves them on your own domain.
1. Check the live URLs, redirects, key journeys, and monitoring after release.
1. Provide the [project handover](project-documentation.md#portable-handoff), inventory, author examples, acceptance results, exceptions, and recovery contacts.

For failures, retain the exact URL/path, operation, and error log. Retry the smallest affected scope after correcting the cause. Do not restart a successful full batch solely because one page failed.

Code push, document copy, JCR package import, and publication are separate operations on separate systems. A partial failure can leave only some changes applied, and no single rollback undoes all of them. Recover code through Git, and content and assets through the authoring system's version history or approved process.
