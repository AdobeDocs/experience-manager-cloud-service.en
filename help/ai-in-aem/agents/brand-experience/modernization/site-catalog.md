---
title: Plan a Migration with the Site Catalog
description: List a site's pages, group them into templates and block variants, and correct the grouping before you migrate to Edge Delivery Services.
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

# Plan a Migration with the Site Catalog {#site-catalog-skill}

The site catalog of the Experience Modernization Agent lists the pages of a site that you're authorized to migrate, and groups them before anything is imported. Pages that share a layout of blocks form a template. Similar blocks across pages form a block variant: a version of a block that differs in content structure or look. On import, a variant whose fields differ becomes a [block of its own](production-migration.md#content-structure). With this grouping, you migrate and check one sample page per template, then import the rest of the template in bulk. The templates, blocks, and locales that the catalog finds also give you an [estimate of the project](production-migration.md#estimate), and its report can be shared with stakeholders who don't use the console.

The catalog reads the source site and imports nothing. For the whole migration workflow, see [Migrate a Production Site](production-migration.md).

## Start Planning {#invoking}

Check that you're authorized to read the source site and that the console can reach it. Then start planning in the [Experience Modernization Console](console.md) in either of these ways:

* Open the [Planning view](#accessing-planning-ui). If the project has no plan yet, it shows **Plan your migration**. Enter the site's address and select **Plan my migration**. Start with the home page; the agent finds the other pages.
* Ask the agent in the chat:

  `scope site https://www.example.com`

While planning runs, the **Planning** view shows **Planning your migration** with the current step, the number of pages found and read, and the elapsed time. You can review results before the run completes.

The agent analyzes every page that it discovers. When it finds more than 1,000 pages, it tells you roughly how long the analysis will take, and continues. For a very large site, ask the agent to propose how to divide the migration, then catalog the sections that you choose.

To stop a run, use the stop control in the chat. The **Planning** view then shows **Planning stopped before it finished**, and you can pick up where it left off or start over. The chat thread shows what happened before it stopped.

Planning runs in four phases:

1. **Analyzing:** The agent loads each page, takes a screenshot, and divides the page into blocks based on its author-editable content. Screenshots leave out cookie banners and other large dialogs that cover the page. The analysis leaves out the site's header and footer, because an Edge Delivery Services site builds them once from separate navigation and footer content.
1. **Block cataloging:** The agent groups similar blocks across pages into block variants, maps each variant to a block from the block library, and names it.
1. **Templating:** The agent groups pages that share the same layout of blocks into template candidates.
1. **Naming:** The agent merges template candidates that are structurally the same and gives each template a meaningful name.

## Results and Status {#output}

When the run completes, the agent posts a summary in the chat: the number of pages, templates, and block variants, a breakdown by locale, and the status of the run. The **Planning** view shows the same status.

|Status|Meaning|
|---|---|
|**complete**|All pages were analyzed, or 10% or fewer failed.|
|**incomplete**|More than 10% of pages failed, or block detection failed on more than half of them. The results are usable but partial.|
|**failed**|No page was analyzed.|

A **complete** run can still have failed pages, so review the [failed URLs](#failed-urls) anyway. Compare the discovered URLs with your agreed scope: pages that nothing links to need a decision of their own. Keep the counts of discovered, analyzed, imported, and signed-off pages apart.

## The Planning View {#planning-ui}

The **Planning** view in the [workspace panel](console.md#workspace-panel) shows the templates, pages, and blocks that the agent identified, with screenshots, so that you can correct them before you migrate. Every later step builds on this grouping, so review it before you import pages. The view is unrelated to the chat's **Plan** mode, in which the agent proposes its approach to one request before it changes any files.

### Open the Planning View {#accessing-planning-ui}

* In the workspace panel header, open the view picker and select **Planning** under **Project**. It is always there; you don't need to turn it on.
* Go to [`https://aemcoder.adobe.io/chat/project/plan`](https://aemcoder.adobe.io/chat/project/plan).
* When a run completes, select **View plan** in the **Your migration plan is ready** notification.

![Selecting the Planning view from the view picker](assets/site-planning-view-picker.png)

If you haven't cataloged a site in the current project, the view asks for the site's address so that you can [start planning](#invoking).

The view shows one migration plan per console workspace, from the files in the [`catalog/` folder](#catalog-files). You can't keep several plans side by side, for example one per country site. Plan and migrate the sites one after the other, and download each plan's report bundle if you want to keep a record of it.

### Dashboard {#dashboard}

The dashboard summarizes the cataloged site. Its header shows the site title, the [run status](#output), and the analysis date. Select **Open site** in the workspace header to open the source site in a new tab.

![Site planning dashboard](assets/site-planning-dashboard.png)

The dashboard cards show:

* **Content:** The URLs discovered, templates identified, pages analyzed, and documents found.
* **Pages:** The pages analyzed and failed, and how the URLs were discovered, such as from the sitemap or by following links. Select the failed count to open the [failed URLs](#failed-urls).
* **Blocks:** The blocks and block variants identified.
* **Locales:** The pages per locale. This card shows only for a site with more than one locale.

Below the cards, a toggle switches the table between **Templates**, with each template's description and number of pages, and **Blocks**, with each block and its variants. Select a template name to open its [template details](#template-details), or a variant to see its [instances](#variant-instances). Both tables can be searched and sorted. Select **Expand table** to hide the cards and give the table more room.

### Blocks Table {#blocks-table}

The blocks table shows one expandable row per block, with the block's variants nested underneath. For each block, it shows the number of variants, pages, and templates that it is found on, and its code status.

![Blocks table in the Planning view](assets/site-planning-blocks.png)

Each block shows its name and the type of block from the block library that it is based on, for example a `cards-story` block of type `cards`. Its variants are listed underneath by their variant class, such as `.with-button`. A variant without a class is the block's default. The page header, the footer, and default content, such as plain headings and text, aren't listed as blocks.

The **Code** column shows whether code has been generated for the block.

|Status|Meaning|
|---|---|
|**Ready**|Block code has been generated.|
|**Needs update**|Block code exists but doesn't cover all of the block's variants yet.|
|**Not ready**|Block code hasn't been generated yet.|
|**Invalid name**|The block or variant name can't be used as a block folder or CSS class name. [Rename the block or variant](#planning-actions) to fix it.|
|**Unclassified**|The block type hasn't been identified, so no code will be generated for it. Use **Classify block type** to fix it.|

**Ready** means only that the code exists. Whether authors can edit the block and whether it works are part of the [checks before release](production-migration.md#acceptance).

The **Confidence** column shows how sure the agent is that a block variant was grouped and classified correctly:

* **High** or **Low** is set by cataloging. Select the information icon next to the level to read the reason. Review **Low** variants first.
* **User** means that a person confirmed or changed the variant, for example through a [guided review](#review-catalog) or a [refining action](#planning-actions).

After code has been generated with sample content, select **View sample** in a block's actions menu to open the block's sample page in the preview.

Template and page details show the same blocks table, limited to that template or page.

### Template Details {#template-details}

Select a template to see every page that uses it, with the page path, title, and number of blocks. Select a page path to open its [page details](#page-details). Use the **Pages** / **Blocks** toggle to switch to the blocks that the template uses.

![Template details in the Planning view](assets/site-planning-template-details.png)

Once pages of a template are being migrated, the template shows how many pages were imported and how many failed, and each page shows its import status. The status updates while the import runs.

|Status|Meaning|
|---|---|
|**Imported**|The page was imported. Select the label to open the imported page in the preview.|
|**Import failed**|The import failed. The reason is shown under the status.|
|**Not imported**|The page is part of the migration but hasn't been imported yet.|

A dash means that the page's template isn't part of the current migration.

### Page Details {#page-details}

Page details list the blocks found on the page, with details from the analysis such as the number of sections and blocks. Select **View screenshot** in the header to see the full-page screenshot. Select **Locate on page** on a block variant to see the screenshot with that block highlighted.

![Page details in the Planning view](assets/site-planning-page-details.png)

### Variant Instances {#variant-instances}

Select a block variant to see every instance of it across the site side by side, with the number of instances, pages, and templates that it appears on. An instance in the wrong group stands out.

![Variant instances in the Planning view](assets/site-planning-variant-instances.png)

The actions menu of each instance lets you view its screenshot, locate it on its page, open its page details, or open the source page.

To correct the grouping, select one or more instances and choose one of these actions:

* **Split into a new variant:** Moves the selected instances into a new variant.
* **Move to another variant:** Moves the selected instances into an existing variant.

At least one instance must remain in the original variant. To move every instance of a variant, use **Give this variant its own block** or **Make this a variant of another block** on the variant instead. Your split and move changes are kept when the catalog is regenerated.

### Failed URLs {#failed-urls}

The failed URLs list shows each page that couldn't be analyzed, with the reason and the time. Files that aren't pages, such as images and documents, are skipped, counted separately, and not listed.

### Review the Catalog {#review-catalog}

When planning finishes, the agent offers to **Review scoping results**. Use it as your starting point for checking the catalog, especially for large sites.

1. Choose **Review each step** to answer the agent's questions, or **Autopilot** to let it decide.
1. The agent first fixes issues that have only one sensible answer and tells you what it changed. For example, it moves outliers to the variant where they fit, turns lone links and buttons into page text, combines look-alike variants, and fixes invalid names.
1. It then asks you about the remaining items one at a time, starting with clear mistakes. Each question shows the screenshots and the agent's suggestion, and you answer in one step. Ask why if you want its reasoning.
1. Select **Finish for me** on any step to let the agent complete the rest of the review without more questions.
1. The review ends with a short report of what changed and what to check in the plan. Items that the agent is still unsure about are left unchanged and flagged. Select **Review remaining items** to continue with them, or **Start site migration** when the catalog is ready.

The review changes the catalog only. It doesn't import pages or generate code.

**Start site migration** migrates one template at a time. The agent asks which template to start with, then uses the catalog's pages and blocks for it. Check that template's pages before you continue with the next one, and expect to correct some of them.

### Refining the Catalog {#planning-actions}

Open the actions menu (**...**) of any template, page, block, or variant and select **AI actions** to see the actions available for it. You can also select up to 20 items to act on them together.

When you choose an action, the console adds the selected items to the chat with a request. Review its scope and any proposed changes before you confirm. You can also choose **Add to chat** and write your own prompt, including what must not change and whether the agent may upload content.

|Item|Actions|
|---|---|
|Template|**Migrate template to AEM**, **Rename template**, **Add pages to template**, **Create a new template from a subset**, **Suggest structural refactors**|
|Page|**Migrate page to AEM**, **Move to another template**, **Review page structure**|
|Block|**Generate block code**, **Classify block type**, **Rename block**, **Make this a variant of another block**|
|Block variant|**Rename variant**, **Give this variant its own block**, **Make this a variant of another block**|
|Block on a page|**Classify block type**|
|Variant instances|**Split into a new variant**, **Move to another variant**|

Some actions show only where they apply. For example, **Generate block code** and **Rename block** are available only for blocks whose type has been classified, and **Give this variant its own block** only for variants that have a variant class.

In **Migrate page to AEM** and **Migrate template to AEM**, *AEM* refers to the project connected to the console. The imported content stays in the console workspace until you upload it: to Experience Workspace for document-based projects, or to the author instance for Experience Manager authoring.

Grouping and naming corrections change the catalog, not the pages that you already imported. **Generate block code** changes code, and the migration actions import content, so review their output separately. A structural refactor in the catalog isn't a refactor of block code; for that, see [Refactor Without Changing the Outcome](block-development.md#refactor).

### Rerun a Phase {#additional-prompts}

To rerun a phase, for example after the source site has changed, ask the agent to repeat it by name:

`repeat block cataloging`

The agent also reruns every later phase and keeps the earlier ones. Changes that you made in the **Planning** view, such as splitting or moving block instances, are kept.

If the **Planning** view shows **Block catalog is out of date**, the catalog was created in an earlier format that the current version can't read. Run planning again from the chat with `scope site` and the site's address. If planning stopped before it finished, **Start over** in the **Planning** view also starts a new run for the same site.

## Bulk Import Workflow {#bulk-import}

To migrate a full site template by template:

1. Run the site catalog to get the templates and block variants.
1. Review them in the [Planning view](#planning-ui) and correct any that were identified incorrectly. The [guided review](#review-catalog) is the quickest way to start.
1. Generate code for the blocks that you need. You can select several blocks and generate code for only those.
1. For each template, open its [template details](#template-details) and use **Migrate page to AEM** on one or two sample pages. Refine the import until the output is correct.
1. Use **Migrate template to AEM** to import the remaining pages of that template. Follow each page's [import status](#template-details), and retry failed pages after you correct the cause.
1. Repeat for each template.

If the output of a template is wrong, correct it on a sample page before you import more pages. If analysis fails, check the [failed URLs](#failed-urls), correct the source access, and retry those pages. Importing a page again overwrites edits that authors made to it since; see [Import in Batches](production-migration.md#batches).

## Catalog Files {#catalog-files}

Most users need only the [Planning view](#planning-ui). To share an offline report or use the data in other tools, find the raw output in the `catalog/` folder of your project.

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

* **Source access:** The agent reads the source from its hosted environment, so being signed in to the source in your own browser doesn't give it access. For pages that require sign-in or a secret header, configure [protected site authentication](console.md#protected-site-authentication), and check one protected page before you start a full run. Don't assume that authentication set up for Auto mode also applies to cataloging. If the source blocks automated visitors, see [Source Sites with Bot Protection](troubleshooting.md#bot-protection).
* **Content behind interactions:** The catalog loads each page in a browser, as the import does, so content that appears only after a visitor clicks or types isn't captured. Check the screenshots against the source. See [Limitations](overview.md#limitations).
* **Coverage:** Discovery uses the sitemap or follows links from the start page, so it doesn't find pages that neither lists nor links to, such as campaign landing pages. Compare the result with your own URL list, and record failures, missing URLs, and approved exclusions.

To hand the analysis over, record its date, the source scope, the report, your corrections, the unresolved URLs, and the sample pages that you checked in the [project handover](project-documentation.md#portable-handoff).
