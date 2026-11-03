---
title: Site Catalog Skill
description: Analyze your website's pages, templates, and blocks to support Edge Delivery Services migration planning.
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

# Site Catalog Skill {#site-catalog-skill}

Analyze an authorized source website to prepare a migration to Edge Delivery Services (EDS). Use the catalog to select representative pages and review coverage, not as proof that the site has already migrated.

## Overview {#overview}

The site catalog skill discovers URLs, analyzes reachable pages, groups page templates and block variants, and captures screenshots. A template is a group of pages that share the same layout of blocks. A block variant is a version of a block with its own content structure or look. Review and refine the results in the [site planning UI](#planning-ui). Discovery can miss pages and analysis can fail; reconcile the result with your agreed inventory.

The skill supports migration planning in the following ways:

* **Starting a migration project** — Establish a baseline page/template/block inventory and inspect missing or failed pages before committing to the full migration scope.
* **Effort estimation and planning** — Get quantified metrics to support proposals, sprint planning, and resourcing.
* **Catalog review and correction** — Validate the templates and blocks the agent identified in the [site planning UI](#planning-ui) and correct them before migration begins.
* **Bulk import preparation** — See which pages share the same layout and plan [template-by-template bulk imports](#bulk-import).
* **Stakeholder reporting** — Share the results with project managers, architects, and business stakeholders.

## Invoking {#invoking}

Confirm source authorization, reachability, and the intended project first. Cataloging analyzes the source; it does not upload content or publish a target site.

[In the Experience Modernization Console,](/help/ai-in-aem/agents/brand-experience/modernization/console.md) start planning in either of the following ways.

* Open the [site planning UI](#accessing-planning-ui). If the project has no plan yet, it shows **Plan your migration**. Enter the site's address and select **Plan my migration**. Start with the home page; the agent finds the other pages.
* Ask the agent in the chat:

  `scope site https://www.example.com`

While planning runs, the site planning UI shows **Planning your migration** with the current step, the number of pages found and read, and the elapsed time. You can begin reviewing results before the run completes.

To stop a run, use the stop control in the chat. The site planning UI then shows **Planning stopped before it finished**, and you can pick up where it left off or start over. The chat thread shows what happened before it stopped.

The skill's workflow has four phases that run in sequence:

1. **Analyzing** — Each page is loaded, screenshotted, and divided into blocks based on its author-editable content.
1. **Block cataloging** — Similar blocks across pages are grouped into block variants, and each variant is mapped to a block from the block library and named.
1. **Templating** — Pages that share the same layout of blocks are grouped into template candidates.
1. **Naming** — Template candidates are reviewed, merged where they are structurally the same, and given meaningful names.

When the run completes, [review the results in the site planning UI](#planning-ui).

### Additional Prompts {#additional-prompts}

Most projects only need the prompt above. If you need to rerun a phase, for example after the site has changed, ask the agent to repeat it by name.

`repeat block cataloging`

Rerunning a phase also reruns every phase after it, while earlier phases are kept. Changes you make in the [site planning UI](#planning-ui), such as splitting or moving block instances, are kept when the catalog is regenerated.

## Output {#output}

When the run completes, the agent posts a summary in the chat with the number of pages, templates, and block variants it found, a breakdown by locale, and the overall status of the run. The full results are available to review and refine in the [site planning UI](#planning-ui).

The status of the run is shown in the chat summary and in the site planning UI.

|Status|Meaning|
|---|---|
|**complete**|All pages were analyzed successfully (or there was a 10% or lower failure rate).|
|**incomplete**|Over 10% of pages failed, or block detection failed on over 50% of pages. The results are still usable but partial.|
|**failed**|No pages were successfully analyzed.|

**Complete does not mean full coverage.** Review failed URLs even for a complete run. Keep discovered, successfully analyzed, imported, and accepted page counts separate. Compare the discovered URLs with the site's agreed migration scope; unlinked or undiscovered pages need an explicit decision.

## Site Planning UI {#planning-ui}

The site planning UI is a view in the [workspace panel](/help/ai-in-aem/agents/brand-experience/modernization/console.md#workspace-panel) of the Experience Modernization Console where you can review the results of the site catalog skill and correct them before you begin migrating. It shows the templates, pages, and blocks the agent identified, along with screenshots, so you can confirm that they were identified correctly.

Because the accuracy of the catalog directly affects project sizing and every downstream migration step, it is recommended that you review the catalog in the site planning UI before importing pages.

### Accessing the Site Planning UI {#accessing-planning-ui}

You can open the site planning UI in any of the following ways.

* In the workspace panel header, open the view picker and select **Planning** under **Project**.
* Navigate directly to [`https://aemcoder.adobe.io/chat/project/plan`](https://aemcoder.adobe.io/chat/project/plan).
* When a run completes, select **View plan** in the **Your migration plan is ready** notification.

![Selecting the Planning view from the view picker](assets/site-planning-view-picker.png)

>[!NOTE]
>
>If you have not yet cataloged a site in the current project, the site planning UI asks for the site's address so that you can [start planning](#invoking).

The site planning UI updates as pages are analyzed and imported, so you can begin reviewing results before the run completes.

### Overview Dashboard {#dashboard}

The overview dashboard summarizes the cataloged site. The header shows the site title, the [report status](#output), and the analysis date. Select **Open site** in the workspace header to open the source site in a new tab.

![Site planning overview dashboard](assets/site-planning-dashboard.png)

The dashboard includes the following cards.

* **Content** — The number of URLs discovered, templates identified, pages analyzed, and documents found
* **Pages** — The progress of page analysis, showing the number of pages successfully analyzed and the number that failed, plus the URL discovery method (for example sitemap or crawl)
  * Select the failed count to open the [failed URLs list](#failed-urls).
* **Blocks** — The number of blocks and block variants identified
* **Locales** — The number of pages per locale (only shown if the site has more than one locale)

Below the cards is a table which you can switch between two views using the toggle in the table toolbar.

* **Templates** — Lists every template with its description and the number of pages that use it. Select a template name to open its [template details](#template-details).
* **Blocks** — Lists every block with its variants nested underneath. Select a variant to view its [variant instances](#variant-instances).

Both tables can be searched and sorted. Select the **Expand table** icon to hide the dashboard cards and give the table more room.

### Blocks Table {#blocks-table}

The blocks table shows one expandable row per block, with the block's variants nested underneath. For each block it shows the number of variants, pages, and templates it is found on, along with its code status.

![Blocks table in the site planning UI](assets/site-planning-blocks.png)

Each block is shown with its name and the type of block from the block library that it is based on, for example a `cards-story` block of type `cards`. Its variants are listed underneath by their variant class, such as `.with-button`. A variant without a class is the block's default. Page header, footer, and default content (such as plain headings and text) are not listed as blocks.

The **Code** column shows whether code has been generated for the block.

|Status|Meaning|
|---|---|
|**Ready**|Block code has been generated.|
|**Needs update**|Block code exists but does not yet cover all of the block's variants.|
|**Not ready**|Block code has not been generated yet.|
|**Invalid name**|The block or variant name can't be used as a block folder or CSS class name. [Rename the block or variant](#planning-actions) to fix it.|
|**Unclassified**|The block type has not been identified, so no code will be generated for it. Use **Classify block type** to fix it.|

The **Confidence** column shows how sure the agent is that a block variant was grouped and classified correctly.

* **High** or **Low** is set by cataloging. Select the information icon next to the level to read the reason. Review **Low** variants first.
* **User** means that a person confirmed or changed the variant, for example through a [guided review](#review-catalog) or a [refining action](#planning-actions).

After code has been generated with sample content, use **View sample** in a block's actions menu to open the block's sample page in the preview.

The same blocks table is also shown in template and page details, scoped to that template or page.

### Template Details {#template-details}

Selecting a template opens its details, which list every page that uses the template with the page path, title, and number of blocks. Select a page path to open its [page details](#page-details). Use the **Pages** / **Blocks** toggle to switch to the blocks used by that template.

![Template details in the site planning UI](assets/site-planning-template-details.png)

Once pages of a template are being migrated, the template shows how many pages were imported and how many failed, and each page shows its import status. The status updates while the import runs.

|Status|Meaning|
|---|---|
|**Imported**|The page was imported. Select the label to open the imported page in the preview.|
|**Import failed**|The import failed. The reason is shown under the status.|
|**Not imported**|The page is part of the migration but has not been imported yet.|

A dash means the page's template is not part of the current migration.

### Page Details {#page-details}

Page details list the blocks found on the page, along with analysis details such as the number of sections and blocks. Select **View screenshot** in the header to view the full-page screenshot. Use the **Locate on page** action of a block variant to view the full-page screenshot with that block highlighted.

![Page details in the site planning UI](assets/site-planning-page-details.png)

### Variant Instances {#variant-instances}

Selecting a block variant shows every instance of that variant found across the site side by side, along with the number of instances, pages, and templates it appears on. This makes it easy to spot an instance that has been grouped incorrectly.

![Variant instances in the site planning UI](assets/site-planning-variant-instances.png)

The actions menu of each instance lets you view its screenshot, locate it on its page, open its page details, or open the source page.

To correct the grouping, select one or more instances and choose one of the following actions.

* **Split into a new variant** — Moves the selected instances into a new variant.
* **Move to another variant** — Moves the selected instances into an existing variant.

At least one instance must remain in the original variant. To move every instance of a variant, use **Give this variant its own block** or **Make this a variant of another block** on the variant instead. Your split and move changes are preserved when the catalog is regenerated.

### Failed URLs {#failed-urls}

The failed URLs list shows each page that could not be analyzed, along with the reason it failed and when. Non-page files such as images and documents that were skipped are counted separately and are not listed.

### Review the Catalog {#review-catalog}

When planning finishes, the agent offers to **Review scoping results**. Use it as your starting point for checking the catalog, especially for large sites.

1. Choose **Review each step** to answer the agent's questions, or **Autopilot** to let it decide.
1. The agent first fixes issues that have only one sensible answer and tells you what it changed. For example, it moves outliers to the variant where they fit, turns lone links and buttons into page text, combines look-alike variants, and fixes invalid names.
1. It then asks you about the remaining items one at a time, starting with clear mistakes. Each question shows the screenshots and the agent's suggestion, and you answer with one click. Ask why if you want its reasoning.
1. Select **Finish for me** on any step to let the agent complete the rest of the review without more questions.
1. The review ends with a short report of what changed and what to check in the plan. Items the agent is still unsure about are left unchanged and flagged. Select **Review remaining items** to continue with them, or **Start site migration** when the catalog is ready.

The review changes the catalog only. It does not import pages or generate code.

### Refining the Catalog {#planning-actions}

You can refine the catalog directly from the site planning UI using AI actions. Open the actions menu (**...**) of any template, page, block, or variant and select **AI actions** to see the actions available for it. You can also select multiple items (up to 20) to act on them together.

When you choose an action, the selected items are added to the chat as context along with a request. Review its scope and any proposed changes before confirming execution. You can also choose **Add to chat** and write your own prompt, including preservation constraints and whether remote writes are allowed.

The following actions are available.

|Item|Actions|
|---|---|
|Template|**Migrate template to AEM**, **Rename template**, **Add pages to template**, **Create a new template from a subset**, **Suggest structural refactors**|
|Page|**Migrate page to AEM**, **Move to another template**, **Review page structure**|
|Block|**Generate block code**, **Classify block type**, **Rename block**, **Make this a variant of another block**|
|Block variant|**Rename variant**, **Give this variant its own block**, **Make this a variant of another block**|
|Block on a page|**Classify block type**|
|Variant instances|**Split into a new variant**, **Move to another variant**|

Some actions are only offered when they apply. For example, **Generate block code** and **Rename block** are only available for blocks whose type has been classified, and **Give this variant its own block** is only available for variants that have a variant class.

In action labels such as **Migrate page to AEM** and **Migrate template to AEM**, *AEM* refers to the EDS project connected to the console. The imported content stays in the console workspace until it is uploaded to the project's authoring destination: Experience Workspace for document-based projects, or the AEM author instance for AEM authoring.

Grouping and naming corrections update catalog metadata and block-library organization; they do not retroactively repair already imported pages. **Generate block code** changes code, while migration actions start content-generation workflows. Review their output separately. Catalog structural refactoring is not the same as [refactoring block code](block-development.md#refactor).

## Bulk Import Workflow {#bulk-import}

The site catalog skill is part of the recommended approach for migrating a full site.

1. Run the site catalog skill to get the full template catalog and block catalog.
1. Open the [site planning UI](#planning-ui) to review the templates and blocks the agent identified and correct any that were identified incorrectly. The [guided review](#review-catalog) is the quickest way to start.
1. Generate code for the blocks you need. You can select several blocks and generate code for only those.
1. For each template, open its [template details](#template-details) and use **Migrate page to AEM** on one or two representative pages. Refine the import until the output is correct.
1. Use **Migrate template to AEM** to import the remaining pages that use that template. Follow each page's [import status](#template-details) and retry failed pages after correcting the cause.
1. Repeat for each template until the full site is migrated.

Before reimporting, preserve or reconcile author edits in affected pages. If analysis fails, inspect the [failed URLs](#failed-urls), correct source access or extraction issues, and retry the affected scope. If mappings are wrong, refine a representative first rather than repeat a large import unchanged.

For production, continue with [inventory reconciliation and acceptance](production-migration.md#acceptance). Generated block code marked **Ready** does not establish that it has passed authoring, functional, or production checks.

## Catalog Files {#catalog-files}

Most users only need the [site planning UI](#planning-ui). If you want to work with the raw output, for example to share an offline report or to use the data in other tools, the skill saves its files to the `catalog/` folder of your project.

|File|Description|
|---|---|
|`template-catalog-report-bundle.zip`|An interactive HTML report with screenshots that you can download, open locally, and share with stakeholders who don't use the console|
|`summary.json`|Totals and the status of the run|
|`template-catalog.json`|Every template with the URLs that use it|
|`block-catalog.json`|Every block variant with its name, type, and screenshots|
|`urls-all.json`|Every URL discovered|
|`catalog.log`|Execution log|

The folder also contains intermediate files, including per-page analysis and screenshots in `.pages/` and per-variant metadata in `.blocks/`.

## Limitations {#limitations}

The site catalog skill has the following limitations.

* **Source access** — The catalog workflow must be able to reach and read the authorized source. Do not assume that authentication configured for auto mode also applies to cataloging, or that a browser login provides backend access. Verify a representative protected URL before planning a catalog run. If bot protection blocks discovery or analysis, see [source sites with bot protection](getting-started.md#bot-protection).
* **Interaction-dependent content** — Client-rendered or CSS-hidden content is not inherently excluded, but content requiring additional user interaction to appear may not be captured. Inspect the screenshots and source content.
* **Coverage** — Discovery and analysis do not guarantee a complete inventory. Record failures, missing URLs, and approved exclusions.

Hand over the analysis date, source scope, report, corrections, unresolved URLs, and validated representatives using the [project handover](project-documentation.md#portable-handoff).
