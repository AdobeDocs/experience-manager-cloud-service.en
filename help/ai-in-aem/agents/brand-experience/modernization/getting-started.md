---
title: Getting Started with the Experience Modernization Agent
description: Learn the first steps to quickly become productive with the Experience Modernization Agent using the Experience Modernization Console.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: 612c211e-43bf-47dc-89a8-9995a960e4d7
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

# Getting Started with the Experience Modernization Agent {#getting-started}

Use your brand's content to try EDS and EMA, or prepare a few customer demo pages. For a full-site release, use the [production migration guide](production-migration.md) after validating representative pages.

>[!NOTE]
>
>If you are interested in using the Experience Modernization Console, you can request access through your account manager to ensure a smooth onboarding experience.

## Choose Your First Outcome {#first-outcome}

The console is hosted. You do not need a local development environment to begin.

Before importing, identify the authorized source URLs, the pages to include, and whether to preserve the source design or apply a new design. For a connected project, also confirm the code repository and branch, content destination, and permission to write there.

### Trial Your Brand's Content {#brand-trial}

Use a small, representative set of your own pages so that your first edit is useful beyond a sample tour.

1. If your account has access to **auto mode**, open that entry and provide your site URL, or choose selected pages and list their URLs. Review the scope, settings, and [limits](#auto-mode-limits) displayed before starting. Use the authentication fields offered by auto mode, not chat, to provide credentials for a protected source site.
1. Start the run. A run can take several hours; you receive an email when it finishes, and you can leave the page in the meantime. Review its status and result, including the preview, repository, report, and errors where available. A failed or partial run is not proof that all requested pages migrated.
1. Open the resulting site with **Open site**. To continue in your own repository, use [**Make it yours**](#make-it-yours), or [connect an EDS site](#connect-repo) you already own. If auto mode is unavailable, use the guided [single-page import](#start-prompting) below. Auto mode is not a prerequisite for trying your content.
1. Ask for one useful change, such as correcting a heading or updating a call to action. Check it on the intended page and at mobile width.
1. [Save content and code separately](#upload-content), then reopen the remote document and the matching branch preview. Record the project, repository, branch, content location, and preview URL so that you can return.

The trial is complete when the content is editable and the useful change is retained, not merely when a preview link exists. A static design preview does not demonstrate remote authorable content.

Auto-mode access does not imply a universal free entitlement, page allowance, or retention period. Check your account's displayed limits and save work you want to keep. Use the [guided AEM authoring path](getting-started-aem-authoring.md) for JCR-backed delivery; do not assume auto-mode results use that target.

#### Auto-Mode Limits {#auto-mode-limits}

Auto mode limits each account by the number of pages per migration, the number of migrations, and how many migrations can run at the same time. The auto-mode page shows the limits that apply to you before you start:

* A full-site migration uses the page allowance for your account. Where your account permits it, you can set how many pages the migration includes.
* When you select pages, a counter shows how many of the allowed pages you have selected. A run with more pages than your account allows cannot start.
* If you have used all the migrations your account allows, or already have as many migrations running as allowed, auto mode tells you so. Wait for a run to finish, or request more.
* Use **Ask for a higher limit**, or the help button in the header, to ask the support team for more pages or migrations.

To stop a run, use **Cancel migration**. A cancelled run can't be resumed; you would start a new migration.

#### Make It Yours {#make-it-yours}

An auto-mode run creates its site in an Adobe-managed location. To keep working on it in your own EDS site, select **Make it yours** on the finished run.

1. Choose the destination site. If you are not yet connected to GitHub, the console asks you to connect first.
1. Review the destination repository, preview URL, and the new branch that will receive the code. Choose whether to overwrite existing pages and whether to preview the transferred pages.
1. Select **Start transfer** and follow its progress. The code is placed on a new branch, and the content is copied to the destination content location.
1. Select **Open in EMA** to continue in the console, or **Edit Site** to edit the content.

Review and merge the new branch according to your repository policy. Transferring does not publish the site.

### Create a Customer Demo {#customer-demo}

1. Select authorized customer-owned or brand-owned pages and the audience's demo goal. Include representative content rather than only the easiest page.
1. Use auto mode where available, or [import the selected pages](#start-prompting). Name the exact page list; a request for one page is not a full-site migration.
1. Apply the source design, or follow [restyling during migration](restyling.md#during-migration). Complete the navigation, footer, and assets needed for the demo path.
1. Check text, imagery, links, layout, and mobile behavior. Walk the actual demo sequence. Identify mocked interactions, unavailable integrations, and pages outside scope.
1. Retain the work as described for a trial. Hand over exact preview links, their source-page mapping, and the known gaps.

A good demo presents complete, branded pages and working demo paths. It does not require full production cutover, but it must not be described as production-ready.

## Prepare an Edge Delivery GitHub Repository {#prepare-repo}

>[!NOTE]
>
>Using an AEM Sites and Universal Editor project? Follow [Getting Started for AEM Sites/Universal Editor](/help/ai-in-aem/agents/brand-experience/modernization/getting-started-aem-authoring.md) setup steps.

1. Select an [Edge Delivery Services](/help/edge/overview.md) repository for use with the Experience Modernization Console.
   * This can be an existing Edge Delivery Services project or you can create a new one following the [developer tutorial](https://www.aem.live/developer/tutorial) using the [boilerplate repository.](https://github.com/adobe/aem-boilerplate)
1. Ensure that the [AEM Code Connector](https://github.com/apps/aem-code-connector) is installed in the repository.
   * This allows the console to inspect your code.
1. Ensure that the [AEM Code Sync GitHub app](https://github.com/apps/aem-code-sync) is installed in the repository.
   * This allows Edge Delivery Services to sync your code.
   * If your repo is based the on the tutorial, this step is already complete.

>[!NOTE]
>
>**Using a different Git host?** Edge Delivery Services also supports GitHub Enterprise (self-hosted), Adobe-hosted repositories, GitLab, Bitbucket, and Azure DevOps. Onboard the repository in Adobe Cloud Manager, then configure your Edge Delivery site to use it. See [Bring Your Own Git.](https://www.aem.live/developer/byo-git)

>[!IMPORTANT]
>
>The Experience Modernization agent pushes changes and opens pull requests in your repository. The access token you create in Cloud Manager must grant write access to repository code, alongside the permissions listed at [step 8 of Add external repositories.](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/managing-code/external-repositories)
>
>**Already onboarded a token without write access?** You do not need to re-onboard the repository. In Cloud Manager, go to **Repositories > Manage Access Tokens**, edit the token, and paste a value that includes write access. Cloud Manager revalidates the associated repositories automatically. See [Manage access tokens.](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/managing-code/manage-access-tokens#edit-access-tokens)

## Open the Experience Modernization Console {#open-console}

1. Navigate to [`aemcoder.adobe.io`.](https://aemcoder.adobe.io)
1. Log in with your Adobe ID.
   * Use an account that belongs to your company's Adobe organization. A personal Adobe ID that isn't part of an organization can't be used; the console explains this and lets you **Use a different account**. If you don't have a company account, ask your Adobe account team to add you to the organization.

Your workspace pauses after a period of inactivity to save resources. When you return, the console shows **Your workspace is paused**; click **Wake up** and wait a few minutes while the workspace is restored.

## Demo Mode {#demo-mode}

If the console opens in demo mode, you can optionally explore its sample project and try importing additional pages. A **Demo site** button in the header indicates that you are in demo mode. Work in the demo site isn't saved, and the demo site can't push code to GitHub or content to Document Authoring. Sample exploration is not required before trying your own content.

![Demo mode](assets/demo-mode.png)

## Connect Your Site {#connect-repo}

Connect a new or existing EDS project. If you have local workspace changes to keep, save content and push code before replacing the workspace.

1. Click **Demo site** in the header and then **Switch site**, or use **Switch site** in [Settings](console.md#settings-page).
1. This will prompt you to authorize the AEM Code Connector app using your GitHub credentials. Click **Authorize AEM Code Connector**.
   * For GitHub Enterprise, or when OAuth sign-in isn't available, click **Sign in with a token** instead. Enter the **GitHub Host** and a **Personal Access Token**. A fine-grained token limited to the repositories you need is recommended.
1. Back in the console, specify the Preview URL of the site. The preview URL can be obtained by previewing any document in the site, or by constructing it from branch, site-name and org. The system will retrieve the associated Github Project automatically. Alternatively, you can search through your authorized GitHub projects to find a site.
   ![Connecting to GitHub project](assets/connect-site-and-github.png)
1. Click **Checkout to workspace** once the site has been verified.
1. When prompted to **Replace existing workspace**, verify that the current work is saved elsewhere, then click **Replace workspace**.
   ![Replace existing workspace](assets/replace-existing-workspace.png)

Your GitHub project and site is now connected to the console.

Confirm the connected repository, branch, and content destination before requesting changes.

![Site connection](assets/first-sign-on.png)

## Console Home {#console-home}

When you visit [aemcoder](https://aemcoder.adobe.io) the Home Page will appear until a chat conversation has been started. The home page allows you to get started chatting by either typing your first prompt or by selecting one of the suggested prompts.

![Console home](assets/console-home.png)

## Start Prompting {#start-prompting}

Now that your console can access your code, you are ready to start prompting.

1. Start with one authorized source page. Replace the example URL and destination in this prompt:
   * "Migrate only `https://www.example.com/about` to `/about` in this project. Target document-based content. Preserve its text, images, and links. Reuse existing blocks and default content. Do not upload, push, or publish."
   * For AEM authoring, specify JCR persistence and follow the [target-specific checks](getting-started-aem-authoring.md#validate-content).
1. Review the imported page, its destination path, and any reported gaps.
   * The console observes separation of concerns and handles content and presentation separately.
   * Import duration depends on the source and requested scope.
   * The console presents you with ongoing feedback as it begins its work, including an overview of its planned steps.
   ![Content import](assets/content-import.png)
1. Once the site is imported, the **Workspace** panel shows the pages. Select a page to preview it in the right panel.
  ![Content imported](assets/content-imported.png)
1. Now that you have content, request faithful source styling, or explicitly choose a [new target design](restyling.md).
   * "Import the general styles from `https://www.example.com/about`, then style the blocks used on `/about`. Preserve the imported content."
1. As with the initial content import, the import may take several minutes and the console provides feedback as it processes your request and imports the styles. Once the task is complete, click **Refresh preview** in the right panel to view the styled content.
   ![Styles imported](assets/styles-imported.png)

Review the page at desktop and mobile widths. Compare text, links, images, and document structure with the source. Page import does not finish shared navigation and footer automatically; request those separately when needed.

The result is working content and code in the console. It is not yet evidence that remote content was saved, the code was pushed, or the site was published.

>[!TIP]
>
>[Check out the prompting guide](/help/ai-in-aem/agents/brand-experience/modernization/prompting-guide.md) for more ideas on how to prompt the agent and what its skills can do.

## Upload Content {#upload-content}

For document-based persistence, upload to [Document Authoring](https://da.live). Code push does not save these documents. Confirm the organization, repository, destination paths, and permission to replace any existing content before uploading.

1. Make sure you are in a **Content** view and then click the **Upload content** button on the top-right. Alternatively, use **Sync** > **Push** > **Content** in the workspace header to upload all pending pages.
   * By default you are in **Content** view when entering the console.
   * Your view is indicated by the selected View Picker item in the workspace area of the console.
1. The **Upload content** dialog opens with the destination org and repo pre-filled from your project settings.
   * If an `fstab.yaml` is not present in your connected repository, you will need to manually enter your **Organization** and **Repository**.
   * If you used the boilerplate, an `fstab.yaml` is provided.
1. Select the files you want to upload and click **Upload**.
   ![Upload content dialog](assets/upload-content.png)
1. The console indicates upload process by disabling the **Upload** button.
1. Once complete, the dialog shows how many files were uploaded. You can then preview, or preview and publish, the uploaded pages. This runs as a tracked job that continues if you close the dialog; retry any pages that fail.
   ![View in AEM](assets/view-in-aem.png)

To access the uploaded content in Document Authoring, optionally click **View in AEM** in the notification when the upload completes, or navigate to `https://da.live/#/{organization}/{repository}`.

![Content in Document Authoring](assets/content-in-document-authoring.png)

Open an uploaded document, make an edit, save, and reopen it to check authorability and persistence. Use the project's available authoring experience, including Experience Workspace where configured. Review upload errors before assuming all selected pages were copied.

>[!TIP]
>
>If you are working on an AEM Sites and Universal Editor project, uploading content to AEM works slightly differently. Refer to [Getting Started with the Experience Modernization Agent for AEM Sites/Universal Editor Projects](/help/ai-in-aem/agents/brand-experience/modernization/getting-started-aem-authoring.md#upload-content) for specific upload instructions.

## Push Code Changes {#push-code-changes}

Review the code diff and run the project's checks before pushing. Use a pull request for work requiring review. Repository protections, not an optional planning conversation, enforce branch rules.

1. Optionally, switch to **Changes** view (branch icon in the view picker) to review the diff.
   ![Code view](assets/code-view-git-changes.png)
1. Open **Sync** in the workspace header and select **Push** > **Code**.
1. In the **Stage changes** dialog, stage the files you want to push and click **Continue**.
1. In the **Push changes** dialog, enter a commit message. Choose to create a new PR (default) or push to the current branch and click **Confirm** to push.
   * Push directly to the current branch only when your project's policy permits it and you intend to change that branch.
1. Once complete, a notification appears at the bottom of the console.
   ![View PR](assets/view-pr.png)

If a pull request was created, click **View PR** in the completion notification. Otherwise, verify the commit on the destination branch.

![Code in GitHub](assets/code-in-github.png)

Your code is now in GitHub.

## Preview Site {#preview-site}

To view the changes in the preview environment:

1. Go back to Document Authoring.
   * It may still be open in a browser tab you opened after clicking **View in AEM** after uploading the content.
   * Or navigate to `https://da.live/#/{organization}/{repository}`
1. Open one of the pages that you previously uploaded to AEM.
1. Click the paper plane icon (top right) and select **Preview**.
   ![Publish to preview](assets/publish-to-preview.png)

Verify that the preview contains both the saved content and the intended code version. Preview is separate from publication to the live site.

![Published preview content](assets/published-preview.png)

If your code is on a branch other than the one in the preview URL, change the preview URL to that branch. For JCR-backed content, complete [AEM authoring validation and preview](getting-started-aem-authoring.md#preview-site) instead of the Document Authoring steps above.

## Retain or Hand Over Your Work {#retain-work}

Record source and output URLs, code repository and branch, remote content location, accepted pages, unresolved issues, and the next useful task. See [project handover](project-documentation.md#portable-handoff).

If your workflow offers transfer to another document-based project, confirm the destination and overwrite choice. Transfer pushes code and copies content separately: either operation can fail independently. Verify both before leaving the source project. Do not assume this route transfers document content into JCR or provides atomic rollback.

## Troubleshooting {#troubleshooting}

If import fails, retain the error and exact source URL. Check source reachability and permissions, correct the extraction or mapping, and retry one affected page before repeating a batch. Do not bypass source access controls.

If a change is missing, check each location separately: the console workspace, uploaded remote content, pushed code branch, and previewed page. Reimport can overwrite local content changes; save or reconcile author edits first.

Before reset, discard, replacement, or overwrite, preserve the affected work. Recover code through your repository workflow and restore content separately through the authoring system's available recovery process. A code revert alone does not undo remote document writes.

### Allowlist IP Addresses {#allowlist-ip-addresses}

Where approved by your source-site administrator, the following backend addresses can be allowlisted for source extraction. Network access alone does not grant authorization or satisfy login requirements, and does not provide VPN/private-network connectivity:

* `34.228.136.112`
* `54.90.51.39`
* `3.224.194.242`

## Additional Resources {#additional-resources}

The following documents may be useful as you continue to explore the Experience Modernization agent and its console.

* [Experience Modernization Console](/help/ai-in-aem/agents/brand-experience/modernization/console.md) - Details on the console, it's views, options, and capabilities
* [Prompting Guide for Experience Modernization Agent](/help/ai-in-aem/agents/brand-experience/modernization/prompting-guide.md) - Ideas on how to prompt the agent and what its skills can do
* [Edge Delivery Services developer tutorial](https://www.aem.live/developer/tutorial) - Useful if you are new to AEM and Edge Delivery Services projects
* [Document Authoring](https://da.live) - Useful if you are new to Document Authoring for content management
