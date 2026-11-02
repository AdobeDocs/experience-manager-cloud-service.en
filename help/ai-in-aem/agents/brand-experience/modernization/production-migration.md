---
title: Migrate a Production Site with the Experience Modernization Agent
description: Migrate and validate an Edge Delivery Services site with document-based or AEM authoring persistence.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Migrate a Production Site {#production-migration}

Use this workflow to move an agreed site inventory to Edge Delivery Services (EDS). Start with representative pages, establish reusable content and design mappings, and expand only after those pages work in the chosen authoring environment.

For a few demonstration pages or an initial evaluation, use the smaller [demo and trial workflows](getting-started.md#first-outcome). Their completion criteria are different from production acceptance.

## Agree Scope and Destinations {#scope}

You need authorization to read the source, modify the target repository, and write content and assets to the destination. Agree who accepts the result and who authorizes release.

Record:

| Input | Decisions to retain |
|---|---|
| Source inventory | Domains, page URLs, locales, documents, assets, and excluded or retired content. |
| Code | Repository, working branch, review policy, and release owner. |
| Content destination | Document-based persistence for Experience Workspace/Document Authoring, or AEM authoring with JCR persistence and the Universal Editor. |
| Design | Preserve the source appearance or [apply a new design](restyling.md#during-migration). Name the approved reference and version. |
| Behavior | Navigation, forms, search, commerce, consent, analytics, personalization, and other integrations that must work. Identify their owners. |
| URL policy | Destination paths, redirects, canonical URLs, language relationships, and links to retain. |
| Recovery | Code baseline, content backup/recovery process, and authority to overwrite or publish. |

The source CMS does not dictate destination persistence. Both targets deliver through EDS. Complex enterprise requirements can be implemented on EDS, but page import does not automatically reproduce every source integration or CMS feature.

## Prepare and Catalog {#prepare}

1. Follow [shared console setup](getting-started.md#prepare-repo), or [AEM authoring setup](getting-started-aem-authoring.md#create-repo) for a JCR-backed project. Reuse an existing project's configuration rather than recreate it.
1. Ask EMA to catalog the authorized site: `Scope site https://www.example.com`.
1. Review the [site planning UI](site-catalog.md#planning-ui). Correct template and block groupings and investigate failed URLs.
1. Reconcile discovered URLs against your agreed inventory. Include pages missing from discovery and make explicit decisions about failed, skipped, duplicate, or excluded URLs.
1. Select representatives for each template and important variant, including long content, unusual images, locales, and interaction-heavy pages.

Cataloging analyzes the source; it does not migrate or accept every page. A **complete** catalog run can still contain failures.

## Validate Representatives {#representatives}

Start with one template and a small set of pages. For example:

> Migrate only these authorized product pages: [URLs]. Target [document-based or JCR persistence] at [destination paths]. Preserve approved text, links, metadata, and image meaning. Reuse the project's blocks and content conventions. Report missing content and unsupported interactions. Do not upload, push, or publish.

1. Review content mapping. Prefer headings, paragraphs, lists, and images as default content; use blocks for content that needs a reusable model or behavior.
1. Compare imported text, links, images, metadata, and section order against the source. Fix the reusable parser, transformer, or mapping when a pattern is wrong.
1. Apply source styling or follow the [redesign workflow](restyling.md#during-migration). Check global styles before refining individual blocks.
1. Complete shared navigation and footer separately from page import.
1. Save a representative to the chosen authoring destination and verify edit, save, reopen, and preview:
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

Use EMA for bounded development tasks where appropriate. Keep explicit ownership and acceptance for work that requires external systems, credentials, or specialist validation.

## Accept the Result {#acceptance}

Agree acceptance criteria with the site owner. Test against the actual target, not only the console preview.

| Area | Observable acceptance |
|---|---|
| Coverage | Every in-scope URL has an accepted destination or an approved exception. Failed and skipped pages are resolved or recorded. |
| Content | Text, links, assets, metadata, and locale content are complete and correct. |
| Authoring | Authors can edit representative fields and blocks, save, reopen, and preview the result in the chosen authoring environment. |
| Design | Approved desktop and mobile layouts work on real content, including long text and block variants. |
| Function | Navigation, keyboard interaction, forms, integrations, and agreed user journeys work. |
| Quality | Accessibility, performance, and relevant SEO/security checks meet the project's agreed requirements. Automated scores do not establish compliance. |
| Operations | Repository review, content publication, recovery, monitoring, and support ownership are documented and tested as needed. |

An importer status, generated package, visual similarity score, or Lighthouse score alone does not establish production readiness.

## Release, Recover, and Hand Over {#handoff}

1. Review and push the accepted code through the repository's policy.
1. Upload only the accepted content and assets to the confirmed destination. Review per-page and per-asset errors.
1. Verify the saved content with the intended code revision in EDS preview.
1. Obtain the site's release approval and follow the configured publication and domain cutover process.
1. Check the live URLs, redirects, key journeys, and monitoring after release.
1. Provide the [project handover](project-documentation.md#portable-handoff), inventory, author examples, acceptance results, exceptions, and recovery contacts.

For failures, retain the exact URL/path, operation, and error log. Retry the smallest affected scope after correcting the cause. Do not restart a successful full batch solely because one page failed.

Code push, document copy, JCR package import, and publication are separate operations. A partial failure can leave only some changes applied. Recover code through Git and content/assets through the authoring system's approved process; do not promise an atomic rollback across them.
