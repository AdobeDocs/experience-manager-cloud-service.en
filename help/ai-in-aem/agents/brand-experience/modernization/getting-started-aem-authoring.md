---
title: Getting Started with the Experience Modernization Agent for Experience Manager Authoring Projects
description: Learn the specific setup steps required for Experience Manager authoring projects when getting started with the Experience Modernization Agent using the Experience Modernization Console.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: 94a5e40b-af4a-42ed-922b-b1ec9bb82e24
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

# Getting Started with the Experience Modernization Agent for Experience Manager Authoring Projects {#getting-started-aem-authoring}

>[!NOTE]
>
>In this setup, content is stored in the Java Content Repository (JCR) of your Adobe Experience Manager as a Cloud Service author instance, authors edit it with the Universal Editor, and Edge Delivery Services delivers the pages. This setup was previously called Crosswalk. For the storage that Adobe recommends for new implementations, see [Where Content Is Stored and How Authors Edit It](overview.md#content-storage).

Use this workflow when a requirement depends on content staying in the JCR. The [Universal Editor](/help/implementing/universal-editor/introduction.md) is Adobe's visual editor for content in Experience Manager. This is not a migration to HTL-based delivery, and the source website's technology doesn't determine where your content is stored.

You need console access, repository permissions, and permission to create or update content and assets on the target author instance. Record the author instance's host, site identifier, page root, DAM destination (the Experience Manager Assets folder for images and files), code repository, and working branch before importing. Auto mode produces document-based content, so it doesn't apply to this setup.

## Create Your Edge Delivery Services Project Repo {#create-repo}

For a new project:

1. Use the [`aem-block-collection-xwalk`](https://github.com/adobe-rnd/aem-block-collection-xwalk) repository as your template rather than the document-based boilerplate. Templates for Experience Manager authoring have `xwalk`, short for Crosswalk, in their names.
1. Verify that `fstab.yaml`, the file that points Edge Delivery Services to the site's content source, refers to your author instance's host, Git owner, and Git repository. Review and commit the configuration to the branch used for setup.
   * See [Configure content source](/help/implementing/cloud-manager/edge-delivery/configure-content-source.md) for instructions.
1. Follow the [Universal Editor tutorial](https://www.aem.live/developer/ue-tutorial) to set up your repo.
   * Stop when you are asked to create a site in Experience Manager.
1. For this new-project setup, remove the template's `paths.json` and commit the change. Do not remove an existing site's path mappings without reviewing their purpose and replacement.
1. Add the [AEM Code Connector](https://github.com/apps/aem-code-connector/installations/select_target) app to your repo, so that the console can push changes. For how it differs from AEM Code Sync, see [Start from a Repository](getting-started.md#repo-start).

For an existing project that stores its content in the JCR, reuse its configuration and content models. Do not recreate the site or replace its repository with the template. Confirm [code synchronization and repository access](getting-started.md#repo-start) without repeating the document-based setup.

## Create a New Site in Experience Manager {#create-site}

1. In the Sites console, select **Create** > **Site from template**.
1. Select the **AEM Site with Edge Delivery Services Template**.
   * Don't see it listed? [Install the template](https://github.com/adobe-rnd/aem-boilerplate-xwalk/releases).
1. For this template setup, keep the **name** of the site (not the title) as provided.
   * The site name is used as the unique identifier.
   * The title can be changed for display.
1. Select **Create**.
   * You are redirected to the Sites page.
   * Refresh the page if the new site does not appear immediately.

Skip site creation if the target site already exists. Confirm its identifier and destinations instead; do not rename a live site to fit an example.

## Connect the Site and Import a Page {#continue}

The console steps are the same as in the [main guide](getting-started.md). Only the import request and the checks differ.

1. [Open the console](getting-started.md#open-console) and [connect your site](getting-started.md#connect-repo).
1. Ask the agent to import one page, and say that the content is stored in the JCR. Replace the example URL:
   * "Migrate only `https://www.example.com/about` to the agreed page root in this Experience Manager authoring project. Preserve content and links. Reuse the project's block models and validate JCR conversion. Do not upload, push, or publish."

   ![Content imported](assets/content-imported-aem-authoring.png)

1. [Validate the content](#validate-content), [upload it](#upload-content) as a content package, and [check that authors can edit and preview it](#preview-site).
1. Request styling, as in the styling steps of [Import a Page Step by Step](getting-started.md#guided-import), and [push the code](getting-started.md#push-code-changes).

## Validate Content {#validate-content}

Validate the selected page in the content panel. Use **Markdown view**, **JCR XML view**, and **Errors** to check content and conversion. Use **Add to chat** to aim a fix at a page or at one of the [import scripts](production-migration.md#migration-at-scale) that the agent generates.

In Experience Manager authoring projects, each block also has a model: configuration that defines the fields authors edit for that block in the Universal Editor. The Universal Editor edits only the fields that a block's model defines, so a page can render correctly in the HTML preview while blocks that don't match their models can't be edited. Ask the agent to check that the source block models, component definitions, and generated aggregate configuration agree. Update the source configuration through the project's generation workflow rather than fixing only a generated file. Check field mappings and authoring hints, page paths, image references, and the intended site/DAM destinations.

Resolve conversion errors on one sample page before creating a larger package.

![Contextual chat](assets/contextual-chat.png)

## Upload Content {#upload-content}

Package upload writes content to the author instance. Confirm the selected pages, host, site, page root, and asset destination with the target owner. Preserve existing content before replacing it; local validation does not make an overwrite safe.

The upload uses your Adobe sign-in, so the author instance applies your own permissions to the pages and assets. See [Content Push Permissions](evaluate.md#content-push-permissions).

1. Make sure you are in a **Content** view and select the **Upload content** button on the top-right.
1. In the **Create content package** dialog, choose the pages to include in the package.
   * Optionally enter a **Package name** (defaults to the site name if left empty).
   * Use **Select all**, **Clear selection**, **Expand all**, or **Collapse all** to manage the list.
1. Select **Create package**.

   ![Create content package – choose pages and create](assets/content-package.png)

1. After the package is created, the **Upload content package** dialog shows that the package is ready.
   1. You can **Download package** to save it locally, or proceed to upload.
   1. Under **Upload to AEM**, confirm the **AEM site** and **AEM host** (pre-filled from your project settings).
      * Optionally leave **Upload images** checked to include images.
   1. Select **Upload to AEM**.

   ![Package ready to upload or download](assets/upload-package-start.png)

1. The dialog shows upload progress as pages and assets are sent to the author instance. Review the upload log, including individual failures, before closing the dialog.

   ![Upload progress and completion](assets/upload-package-complete.png)

For a failed package or image upload, retain the log and selected paths. Correct conversion, credentials, permissions, or destinations as indicated, then retry the affected scope. A package download alone does not import content into the author instance. Confirm which pages and assets arrived before retrying to avoid unintended replacements.

If **Create package** reports **Missing site configuration**, the console doesn't know the project's site path, `/content/{site-name}`, and DAM folder, `/content/dam/{folder-name}`. It finds them by looking up the site on the author instance that the project's content source points to, as set in `fstab.yaml` or in the site's configuration. Check that the site exists on that author instance and that the Adobe account you signed in with can access it, then reload the console. If the message persists, [request support](console.md#request-support). If it reports **Missing site base URL**, enter the origin URL of the source site, such as `https://www.example.com`, as **Site base url** in [Settings](console.md#settings-page).

If the Experience Manager as a Cloud Service environment is hibernated, the upload dialog and Settings say so and link to the Developer Console. De-hibernate the environment there, then retry the upload. See [De-hibernate a sandbox program from the Developer Console](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/hibernating-environments.md#de-hibernation-introduction).

Review and [push the matching code and configuration](getting-started.md#push-code-changes) through your project's repository policy. This is separate from the package upload; see [How Changes Go Live](overview.md#code-content-lifecycle).

## Validate Authoring and Preview {#preview-site}

1. In the Sites console, locate the imported page under the agreed site root.
1. Open it in the Universal Editor. Verify that expected fields and blocks can be selected and edited, not merely rendered.
1. Change some text and an image, save, and reopen the page. Confirm that the content and asset references persist.
1. Use the project's configured preview workflow (preview pages are served on `*.aem.page`). Verify the page against the intended code branch and check responsive layout, links, and images.
1. For production, complete the [checks before release](production-migration.md#acceptance), then publish the pages from the Universal Editor or the Sites console. See [Publishing Content with the Universal Editor](/help/sites-cloud/authoring/universal-editor/publishing.md).

Successful package upload, successful authoring, preview, and publication are distinct checkpoints. If editing fails, revisit model mappings and generated configuration; do not accept a static preview as completion.

Record the uploaded package, paths, code revision, author/preview URLs, remaining errors, and recovery owner in the [handover](project-documentation.md#portable-handoff). Code rollback does not restore JCR pages or DAM assets; recover those separately using the target environment's approved process.

## Additional Resources {#additional-resources}

* [Getting Started with the Experience Modernization Agent](getting-started.md) - Full workflow including console, prompting, upload, and preview
* [Experience Modernization Console](console.md) - Console reference
* [Universal Editor tutorial](https://www.aem.live/developer/ue-tutorial) - Set up a project with Experience Manager authoring and the Universal Editor
* [`aem-block-collection-xwalk`](https://github.com/adobe-rnd/aem-block-collection-xwalk) - Template repository for these projects
