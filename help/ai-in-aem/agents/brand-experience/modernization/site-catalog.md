---
title: Site Catalog Skill
description: Learn how the Experience Modernization Agent's site catalog skill performs automated analysis of an existing website to support Edge Delivery Services migration planning.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Site Catalog Skill {#site-catalog-skill}

Learn how the Experience Modernization Agent's site catalog skill performs automated analysis of an existing website to support Edge Delivery Services migration planning.

## Overview {#overview}

The site catalog skill discovers every page on the site, identifies the page templates and block variants in use, captures screenshots of each, and generates an interactive HTML report bundle you can browse in the Console preview tab or download and open locally.

The skill supports you and your migration of an existing project to Edge Delivery Services in the following ways:

* **Starting a migration project** — Run the skill before any work begins to understand the site's scale including page count, templates, block variants, and locales. It establishes the baseline inventory every downstream decision depends on.
* **Effort estimation and planning** — Get quantified metrics to support proposals, sprint planning, and resourcing.
* **Bulk import preparation** — Use `template-catalog.json` to identify which pages share the same layout and plan template-by-template bulk imports.
* **Stakeholder reporting** — Share the interactive HTML report bundle with project managers, architects, and business stakeholders.

## Invoking {#invoking}

[In the Experience Modernization Console,](/help/ai-in-aem/agents/brand-experience/modernization/console.md) use natural language to ask the agent to catalog a site. The following are example prompts.

* `scope site https://www.example.com`
* `site scope https://www.example.com`
* `analyze https://www.example.com`
* `find templates on https://www.example.com`
* `discover templates on https://www.example.com`
* `catalog site https://www.example.com`
* `how many page types are there on https://www.example.com`
* `what are the layouts on https://www.example.com`
* `analyze site structure of https://www.example.com`

You will notice that the skill's workflow has four phases that run in sequence:

1. Analyzing
1. Templating
1. Tuning
1. Block cataloging

You can replay any phase and the agent clears that phase's outputs and all downstream outputs and then resumes from that point forward. Here are some example prompts of replaying phases.

* `Repeat analyzing` / `Redo page analysis` / `Rerun analyze pages`
* `Repeat templating` / `Redo the template discovery step` / `Restart the templating step`
* `Repeat tuning` / `Rerun tune templates` / `Redo template tuning`
* `Repeat block cataloging` / `Restart catalog block variants`

When replaying a phase, prior phases are preserved.

## Output {#output}

When the skill completes its cataloging of the site, you receive three different types of output.

1. **A completion summary in chat** including totals (pages, templates, block variants with EDS-mapped vs. custom breakdown), locale breakdown, coverage percentage, and overall report status (complete / incomplete / failed)
1. **An interactive HTML report bundle** as your primary deliverable, saved to `catalog/template-catalog-report-bundle.zip`
   * The bundle contains `template-catalog-report.html` plus all referenced screenshots and assets.
   * You can download the bundle and view it locally or share it.
   * Or you can ask the agent to `Move template-catalog-report-bundle.zip to the /content folder to render it in the preview tab. Update all references as needed.` to view the report in the console.
1. **Structured JSON artifacts** in `catalog/` for downstream skills and programmatic use including `summary.json`, `template-catalog.json`, `block-catalog.json`, `urls-all.json`, `urls-grouped.json`, `urls-checklist.json`, `.pages/`, `.blocks/`

### Catalog Folder Contents {#contents}

Structured JSON artifacts are stored in `catalog/` by the skill.

|File|Description|
|---|---|
|`template-catalog-report-bundle.zip`|Interactive HTML report bundle (primary deliverable)|
|`summary.json`|Roll-up metrics and [report status](#status)|
|`template-catalog.json`|All unique templates with the URLs that use each (used for bulk imports)|
|`block-catalog.json`|All block variants with metadata and screenshot references|
|`urls-all.json`|Every URL discovered|
|`urls-grouped.json`|URLs grouped by pattern and locale|
|`urls-sample.json`|Representative URLs sampled for analysis|
|`urls-checklist.json`|Per-URL analysis status|
|`catalog.log`|Execution log|
|`.pages/<page-slug>/page-catalog.json`|Page-level analysis output|
|`.pages/<page-slug>/full-page.jpg`|Full-page screenshot|
|`.pages/<page-slug>/blocks/<block-name>.jpg`|Per-block screenshots|
|`.pages/_global/header.json + header.jpg`|Global header analysis and screenshot|
|`.pages/_global/footer.json + footer.jpg`|Global footer analysis and screenshot|
|`.blocks/<variantId>/metadata.json`|Block variant metadata|
|`.blocks/<variantId>/screenshots/<name>.jpg`|Block variant screenshots|

### Report Statuses {#status}

The `status` field in [`summary.json`](#contents) can be:

|Status|Meaning|
|---|---|
|`complete`|All pages were analyzed successfully (or there was a 10% or lower failure rate).|
|`incomplete`|Over 10% of pages failed, or block detection crashed on over 50% of pages. Outputs are still usable but partial.|
|`failed`|No pages were successfully analyzed.|

## Sampling for Large Sites {#sampling}

By default, the skill limits deep page analysis to 1000 URLs. For sites with up to and including 1000 URLs, every page is analyzed.

For sites with more than 1000 URLs, the agent pauses and asks how to proceed:

* Increase the sampling cap (up to a maximum 5000 URLs)
* Analyze a specific group only (e.g. only `/products/*` or `/blog/*`)
* Analyze all URLs and run the full site with no sampling

URL discovery always covers the full site regardless of the sample limit. Only the deep per-page analysis phase is limited.

To override and analyze every page, tell the agent:

* `analyze all URLs`
* `analyze everything`
* `analyze every page`
* `run the full site`

## Bulk Import Workflow {#bulk-import}

The site catalog skill is part of the recommended approach for migrating a full site.

1. Run the site catalog skill to get the full template catalog and block catalog.
1. Open [the HTML report bundle](#output) to visually review the templates the agent identified.
1. For each template, manually import the representative pages (listed in [`template-catalog.json`](#output)) and refine the import until output is correct.
1. Bulk-import the remaining pages for that template using the URL list from `template-catalog.json`.
1. Repeat for each template until the full site is migrated.

## Limitations {#limitations}

The site catalog skill has the following limitations.

* **Public sites only** — The target must be publicly accessible (no authentication, VPN, or firewall).
* **Dynamic content is not supported** — Content requiring user interaction to appear in the DOM may not be captured.
* **Default 1000 URL limit** - The deep analysis phase is by default limited to 1000 URLs, [which can be overridden](#sampling) to up to a maximum of 5000 URLs.
