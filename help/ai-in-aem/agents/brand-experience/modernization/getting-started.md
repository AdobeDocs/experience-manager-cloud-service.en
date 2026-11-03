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

Use your brand's content to try Edge Delivery Services (EDS) and the Experience Modernization Agent (EMA), or prepare a few customer demo pages. For a full-site release, use the [production migration guide](production-migration.md) after validating representative pages.

This guide covers document-based persistence. Content is stored in the EDS document-based repository, and authors edit it visually in Experience Workspace, the visual authoring UI for EDS. Adobe strongly recommends this setup for new implementations.

If your content must be stored in AEM's JCR repository and edited with the Universal Editor, follow the [AEM authoring guide](getting-started-aem-authoring.md) for the steps that differ. If AEM or EDS terms are new to you, read [How EDS Pages Work](overview.md#eds-basics) and [Where Content Is Stored and How Authors Edit It](overview.md#content-storage) first. Older articles may call EDS Helix or Franklin, the project names under which its architecture was developed.

## Access and AI Credit Usage {#access}

To use the Experience Modernization Console, request access through your Adobe account manager. Sign in with an Adobe ID that belongs to your company's Adobe organization; see [Open the Experience Modernization Console](#open-console). Auto mode is in early access and has its own access request; see [Trial Your Brand's Content](#brand-trial).

Being able to sign in to the console does not by itself establish your organization's entitlement. Depending on your organization's agreement, work in EMA can consume AI credits. Consumption varies with the work, such as the number of pages, the steps the agent runs, and how often it iterates on a result. For how Adobe measures AI credit consumption for agentic capabilities, see [AI credit consumption](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/overview/ai-credit-consumption). For your organization's entitlement, usage, and commercial terms, contact your Adobe account team.

## Choose Your First Outcome {#first-outcome}

The console is hosted. You do not need a local development environment to begin.

Before importing, identify the authorized source URLs, the pages to include, and whether to preserve the source design or apply a new design. For a connected project, also confirm the code repository and branch, [content destination](overview.md#content-storage), and permission to write there.

### Trial Your Brand's Content {#brand-trial}

Use a small, representative set of your own pages so that your first edit is useful beyond a sample tour.

The steps below start with Auto mode, which migrates a site, or a list of pages you select, without step-by-step prompting. Auto mode is in early access. If you don't have access yet, the Auto mode page at [`aemcoder.adobe.io/auto`](https://aemcoder.adobe.io/auto) shows a form to request it. Auto mode is not a prerequisite for trying your content: without it, import a few pages with the guided [single-page import](#start-prompting) and continue from step 5.

Auto mode and the guided workflow differ in how much the agent does before it hands back to you:

* **Guided workflow:** EMA stops after it imports a page's content so that you can review it. You then ask it to migrate the design, to critique the result against the source page, and to make further improvements, checking each step.
* **Auto mode:** EMA works through all these steps on its own. It imports the content, migrates the design, critiques the result, and keeps refining it until its critique finds the pages close to the source, without stopping for your review.

Auto mode takes much longer than a guided import of the same pages because it checks and refines its own work, so it suits a first result that you collect later. By default, a full-site run migrates a preview of up to 10 pages. After the run, continue in the console to import further pages and refine the result with the guided workflow.

Auto mode migrates a website, starting from its URL or from a list of its page URLs. It doesn't move an existing EDS repository; to work on a site that is already on EDS, [connect it](#connect-repo) instead. Once a run starts, it doesn't ask for your input: you steer it only through the scope and options that you choose before you start. To guide how blocks are identified or styled as you go, use the guided workflow, or refine the result in the console after the run.

1. Open Auto mode and provide your site URL, or choose selected pages and list their URLs. Review the scope, settings, and [limits](#auto-mode-limits) shown before you start.
   * For a protected source site, enter credentials in the authentication fields that Auto mode offers, not in chat.
   * If Auto mode offers **Include integrations**, select it to carry over supported integration settings from the source site, such as analytics, tag manager, and consent settings. They stay switched off on the new site until you turn them on.
1. Start the run. A run can take up to 24 hours. You can leave the page; you receive an email when the run finishes. If the email doesn't arrive, check your spam folder.
1. Review the run's status and result, including the preview, repository, report, and errors where available. Check which pages were migrated, and their content, links, images, and styles. Links to pages that the run didn't migrate can still point to the source site. A failed or partial run is not proof that all requested pages migrated.
1. Open the resulting site with **Open site**. To continue in your own repository, use [**Make it yours**](#make-it-yours), or [connect an EDS site](#connect-repo) you already own.
1. Ask for one useful change, such as correcting a heading or updating a call to action. Check it on the intended page and at mobile width.
1. [Upload the content and push the code separately](#upload-content). Then reopen the document in Experience Workspace and the matching branch on the preview site.
1. Record the project, repository, branch, content location, and preview URL so that you can return.

The trial is complete when the content is editable and the useful change is retained, not merely when a preview link exists. A static design preview does not demonstrate remote authorable content.

Access to Auto mode does not establish a general entitlement or page allowance. Check the limits shown for your account, and use **Make it yours** to keep the work in your own site. Auto mode produces document-based content. For JCR-backed delivery, use the [guided AEM authoring path](getting-started-aem-authoring.md).

#### Auto Mode Limits {#auto-mode-limits}

Auto mode limits each account by the number of pages per migration, the number of migrations, and how many migrations can run at the same time. The Auto mode page shows the limits that apply to you before you start:

* When you are granted Auto mode access, each migration can include up to 10 pages by default. A full-site run migrates a preview of up to that many pages, not the whole site. You can migrate the rest of the site later in the console.
* When you select pages, a counter shows how many of the allowed pages you have selected. A run with more pages than your account allows cannot start.
* If you have used all the migrations your account allows, or already have as many migrations running as allowed, Auto mode tells you so. Wait for a run to finish, or request more.
* Use **Ask for a higher limit**, or the help button in the header, to ask the support team for more pages or migrations.

To stop a run, use **Cancel migration**. A cancelled run can't be resumed; you would start a new migration.

#### Make It Yours {#make-it-yours}

An Auto mode run creates its site in an Adobe-managed location. To keep working on it in your own EDS site, select **Make it yours** on the finished run. This transfers the run's code and content to a site that you own. It doesn't migrate anything again.

Prepare the destination first:

* An EDS site whose code is in a GitHub repository created from an EDS template, such as the [AEM boilerplate](https://github.com/adobe/aem-boilerplate), with the AEM Code Sync and AEM Code Connector apps installed. See [Prepare an Edge Delivery GitHub Repository](#prepare-repo). A repository on another Git host that is connected through Cloud Manager can also be used.
* A `main` branch in the repository, and the site's content stored in Experience Workspace. A destination whose content is stored elsewhere, such as in AEM, can't receive the transfer.
* Write access to the repository, and to the site's content in Experience Workspace for the Adobe account that you use in the console.
* A site other than the run's own site.

To transfer the run:

1. Choose the destination site. If you are not yet connected to GitHub, the console asks you to connect first.
1. Review the destination repository, preview URL, and the new branch that will receive the code. Choose whether to overwrite existing pages and whether to preview the transferred pages.
1. Select **Start transfer** and follow its progress. The code is placed on a new branch, and the content is copied to the destination content location. For a document-based destination, the transfer also turns on Experience Workspace for the destination site. If that step fails, the console shows a warning; ask the site's administrator to turn Experience Workspace on.
1. Select **Open in EMA** to continue in the console, or **Edit Site** to edit the content.

The transfer copies the following:

| What | How it is transferred |
|---|---|
| Code | Pushed to a new branch, created from the destination's `main` branch. On that branch, the run's project replaces the destination's code files. Nothing is merged into `main`. |
| Pages | Copied as documents to the destination's content in Experience Workspace, with the images and other media that they reference. |
| Existing pages | Skipped unless you choose to overwrite them. Before it overwrites a page, the transfer saves the page's current state as a version named **Before Transfer**, which you can restore from the page's version history in Experience Workspace. |
| Preview | If you choose, the transferred pages are previewed on the destination's `*.aem.page` site. They are not published. |

The transfer doesn't copy:

* Spreadsheets, such as redirects, bulk metadata, or placeholders. Recreate the ones that you need in the destination.
* Access permissions, or site and organization configuration. Set them up in the destination.
* The run's Git history and GitHub workflow files.

If the transfer stops with an error, nothing is merged into `main`, but code and content are transferred separately, so check both the branch and the pages. If the new branch already exists, choose another branch name. If the destination doesn't store its content in Experience Workspace, nothing is transferred. Choose a document-based site, or [connect your site](#connect-repo) and import the pages there.

Review the new branch's changes, then merge it according to your repository policy. Transferring does not publish content, but merging the branch into `main` changes the live site's code immediately. See [How Changes Go Live](overview.md#code-content-lifecycle).

### Create a Customer Demo {#customer-demo}

1. Select authorized customer-owned or brand-owned pages and the audience's demo goal. Include representative content rather than only the easiest page.
1. Use Auto mode if your account has access, or [import the selected pages](#start-prompting). Name the exact page list; a request for one page is not a full-site migration.
1. Apply the source design, or follow [restyling during migration](restyling.md#during-migration). Complete the navigation, footer, and assets needed for the demo path.
1. Check text, imagery, links, layout, and mobile behavior. Walk the actual demo sequence. Identify mocked interactions, unavailable integrations, and pages outside scope.
1. Retain the work as described for a trial. Hand over exact preview links, their source-page mapping, and the known gaps.

A good demo presents complete, branded pages and working demo paths. It does not require full production cutover, but it must not be described as production-ready.

## Prepare an Edge Delivery GitHub Repository {#prepare-repo}

An EDS project keeps its code (blocks, styles, and scripts) in a Git repository and its content in a separate content source. This section prepares the code repository.

>[!NOTE]
>
>Using AEM authoring with JCR persistence and the Universal Editor? Follow the [AEM authoring setup steps](getting-started-aem-authoring.md) instead.

1. Select an [Edge Delivery Services](/help/edge/overview.md) repository for use with the Experience Modernization Console.
   * This can be an existing EDS project, or you can create a new one from the [boilerplate repository](https://github.com/adobe/aem-boilerplate) by following the first section of the [developer tutorial](https://www.aem.live/developer/tutorial), **Get started with the boilerplate repository template**. It creates the repository, installs the AEM Code Sync app, and sets up the site with example content that you can edit in Experience Workspace. You don't need the tutorial's local development steps, because EMA provides the development environment.
1. Ensure that the [AEM Code Connector](https://github.com/apps/aem-code-connector) GitHub app is installed in the repository.
   * This lets the console push changes and open pull requests in your repository. Until it is installed, the console can't push code or open pull requests.
   * If the app is installed for selected repositories only, include this one. If your organization requires approval for GitHub apps, an organization owner must approve it.
1. Ensure that the [AEM Code Sync GitHub app](https://github.com/apps/aem-code-sync) is installed in the repository.
   * This lets EDS fetch your code so that it can serve your site.
   * If your repository is based on the tutorial, this step is already complete.

The two apps have similar names but different jobs: one lets EDS serve your site's code, the other lets the console change it.

>[!NOTE]
>
>**Using a different Git host?** EDS also supports GitHub Enterprise (self-hosted), Adobe-hosted repositories, GitLab, Bitbucket, and Azure DevOps. Onboard the repository in Adobe Cloud Manager, the AEM as a Cloud Service tool for managing programs, environments, and code repositories. Then configure your EDS site to use it. See [Bring Your Own Git.](https://www.aem.live/developer/byo-git)

>[!IMPORTANT]
>
>EMA pushes changes to your repository. For repositories connected through Cloud Manager, it pushes a branch but doesn't open a pull request; open one in your Git host if you need a review. The access token you create in Cloud Manager must grant write access to repository code, alongside the permissions listed at [step 8 of Add external repositories.](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/managing-code/external-repositories)
>
>**Already onboarded a token without write access?** You do not need to re-onboard the repository. In Cloud Manager, go to **Repositories > Manage Access Tokens**, edit the token, and paste a value that includes write access. Cloud Manager revalidates the associated repositories automatically. See [Manage access tokens.](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/managing-code/manage-access-tokens#edit-access-tokens)

## Open the Experience Modernization Console {#open-console}

1. Navigate to [`aemcoder.adobe.io`.](https://aemcoder.adobe.io)
1. Log in with your Adobe ID.
   * Use an account that belongs to your company's Adobe organization. A personal Adobe ID that isn't part of an organization can't be used; the console explains this and lets you **Use a different account**. If you don't have a company account, ask your Adobe account team to add you to the organization.

The console keeps a hosted working copy of your project, called the console workspace in these docs. The agent imports content and changes code there until you upload or push. It is unrelated to Experience Workspace, the authoring UI. The console workspace pauses after a period of inactivity to save resources. When you return, the console shows **Your workspace is paused**; click **Wake up** and wait a few minutes while it is restored.

## Demo Mode {#demo-mode}

If the console opens in demo mode, you can optionally explore its sample project and try importing additional pages. A **Demo site** button in the header indicates that you are in demo mode. Work in the demo site isn't saved, and the demo site can't push code to GitHub or upload content to Experience Workspace (Document Authoring). Sample exploration is not required before trying your own content.

![Demo mode](assets/demo-mode.png)

## Connect Your Site {#connect-repo}

Connect a new or existing EDS project. If your console workspace has changes you want to keep, upload the content and push the code before you replace it.

1. Click **Demo site** in the header and then **Switch site**, or use **Switch site** in [Settings](console.md#settings-page).
1. This prompts you to authorize the AEM Code Connector app using your GitHub credentials. Click **Authorize AEM Code Connector**.
   * For GitHub Enterprise, or when OAuth sign-in isn't available, open **More ways to connect** and click **Sign in with a token** instead. Enter the **GitHub Host** and a **Personal Access Token**. A fine-grained token limited to the repositories you need is recommended. The token must be able to read your user account and push to the repository; with a token, the console lists only repositories that you can push to.
1. Back in the console, specify the preview URL of the site. Preview URLs follow the pattern `https://{branch}--{site}--{organization}.aem.page`, where `{site}` is the GitHub repository name and `{organization}` is the GitHub organization or user that owns it. You can copy one by previewing any page of the site, or construct it from those names. Older projects and documentation may show the earlier `hlx.page` domain. The console finds the associated GitHub repository automatically. Alternatively, you can search through your authorized GitHub projects to find a site.
   ![Connecting to GitHub project](assets/connect-site-and-github.png)
1. Click **Checkout to workspace** once the site has been verified. This copies the project into your console workspace.
1. When prompted to **Replace existing workspace**, verify that the current work is saved elsewhere, then click **Replace workspace**.
   ![Replace existing workspace](assets/replace-existing-workspace.png)

Your site and its GitHub repository are now connected to the console.

Confirm the connected repository, branch, and content destination before requesting changes. You need write access to the repository to connect it. If your organization or repository isn't listed, or the console can't verify the preview URL, see [Git Connection Problems](#git-connection).

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
   * In this guided flow, the agent imports content first; you request styling in a later step.
   * Import duration depends on the source and requested scope.
   * The console presents you with ongoing feedback as it begins its work, including an overview of its planned steps.
   ![Content import](assets/content-import.png)
1. Once the site is imported, the **Workspace** panel shows the pages. Select a page to render it in the console's preview panel on the right. This preview shows the working copy in the console workspace, not the EDS preview site.
  ![Content imported](assets/content-imported.png)
1. Now that you have content, request faithful source styling, or explicitly choose a [new target design](restyling.md).
   * "Import the general styles from `https://www.example.com/about`, then style the blocks used on `/about`. Preserve the imported content."
1. As with the initial content import, the import may take several minutes and the console provides feedback as it processes your request and imports the styles. Once the task is complete, click **Refresh preview** in the right panel to view the styled content.
   ![Styles imported](assets/styles-imported.png)

Review the page at desktop and mobile widths. Compare text, links, images, and document structure with the source. Page import does not finish shared navigation and footer automatically; request those separately when needed.

The result is working content and code in the console. It is not yet evidence that remote content was saved, the code was pushed, or the site was published. Each of the next steps moves work to a different place:

* **Upload** copies content from the console workspace to its authoring destination: Experience Workspace for document-based projects, or the AEM author instance for AEM authoring. In the **Sync** menu, this is **Push** > **Content**.
* **Push** commits code to your Git repository, on the current branch or as a pull request.
* **Preview** copies saved content to the EDS preview site, `*.aem.page`.
* **Publish** makes previewed content live on `*.aem.live`.

>[!TIP]
>
>[Check out the prompting guide](prompting-guide.md) for more ideas on how to prompt the agent and what its skills can do.

## Upload Content {#upload-content}

For document-based persistence, upload the pages to the document-based repository at [`da.live`](https://da.live), where authors edit them in Experience Workspace. Console labels and some screens still call it Document Authoring. Code push does not save these documents, because EDS stores content separately from code. Confirm the organization, repository, destination paths, and permission to replace any existing content before uploading.

1. Make sure you are in a **Content** view and then click the **Upload content** button on the top-right. Alternatively, use **Sync** > **Push** > **Content** in the workspace header to upload all pending pages.
   * By default you are in **Content** view when entering the console.
   * Your view is indicated by the selected View Picker item in the workspace area of the console.
1. The **Upload content** dialog opens with the destination **Organization** and **Site** pre-filled from your site's configuration: the repository's `fstab.yaml` file, which points EDS to the site's content source, or, if the repository has none, the site's configuration in EDS.
   * Sites created from the current boilerplate have no `fstab.yaml`; their content source is set when the site is set up.
   * If the console can't determine the destination, the fields are empty. Enter the **Organization** and **Site** of your content in Experience Workspace yourself.
1. Select the files you want to upload and click **Upload**.
   ![Upload content dialog](assets/upload-content.png)
1. The console indicates upload process by disabling the **Upload** button.
1. Once complete, the dialog shows how many files were uploaded. You can then preview, or preview and publish, the uploaded pages. This runs as a tracked job that continues if you close the dialog; retry any pages that fail.
   ![View in AEM](assets/view-in-aem.png)

To find the uploaded content, optionally click **View in AEM** in the notification when the upload completes, which opens it at `da.live`, or navigate to `https://da.live/#/{organization}/{repository}`.

![Content in Document Authoring](assets/content-in-document-authoring.png)

Open an uploaded document, make an edit, save, and reopen it to check authorability and persistence. Where Experience Workspace is turned on for the site, edit the page visually there; in the console, **Edit in Experience Workspace** opens the selected page in its editor. Experience Workspace is off by default and is turned on per site or organization. Review upload errors before assuming all selected pages were copied.

>[!TIP]
>
>If you are working on an AEM authoring project, with JCR persistence and the Universal Editor, uploading content to the AEM author instance works differently. Refer to [Getting Started with the Experience Modernization Agent for AEM Authoring Projects](getting-started-aem-authoring.md#upload-content) for specific upload instructions.

## Push Code Changes {#push-code-changes}

Review the code diff and run the project's checks before pushing. Use a pull request for work requiring review. Branch rules are enforced by your repository's protections; the console and the optional plan mode do not enforce them. See [Control over Changes](overview.md#security-control).

1. Optionally, switch to **Changes** view (branch icon in the view picker) to review the diff.
   ![Code view](assets/code-view-git-changes.png)
1. Open **Sync** in the workspace header and select **Push** > **Code**.
1. In the **Stage changes** dialog, stage the files you want to push and click **Continue**.
1. In the **Push changes** dialog, enter a commit message. Choose to create a new PR (default) or push to the current branch and click **Confirm** to push.
   * **Create new PR** pushes a new branch, named `aem-` followed by the date and time, and opens a pull request into the current branch.
   * **Push to current branch** adds the commit to the current branch, and updates its pull request if it has one. Use it only when your project's policy permits it and you intend to change that branch. A push to `main` changes the live site's code immediately.
1. Once complete, a notification appears at the bottom of the console.
   ![View PR](assets/view-pr.png)

If a pull request was created, click **View PR** in the completion notification. Otherwise, verify the commit on the destination branch. For repositories connected through Cloud Manager, the console pushes the branch without opening a pull request.

If the branch has changed in the repository since your last pull, the console tries to apply your commit on top of the remote changes and push again. If that fails, it shows **Push failed: Remote has conflicting changes** and switches the dialog to **Create new PR**, so that you can push to a new branch and resolve the conflict in the pull request. If the branch is protected against direct pushes, push with **Create new PR**.

![Code in GitHub](assets/code-in-github.png)

Your code is now in GitHub. It shows on that branch's preview and live URLs straight away.

## Preview Site {#preview-site}

EDS preview copies your saved content to the preview site, `*.aem.page`, where it renders with the code of the branch in the URL. This is different from the console's preview panel, which shows only the working copy in the console workspace. Publishing, a separate step, makes the content live on `*.aem.live`. To preview the uploaded pages:

1. Go back to Experience Workspace at `da.live`.
   * It may still be open in a browser tab you opened after clicking **View in AEM** after uploading the content.
   * Or navigate to `https://da.live/#/{organization}/{repository}`
1. Open one of the pages that you previously uploaded.
1. Click the paper plane icon (top right) and select **Preview**.
   ![Publish to preview](assets/publish-to-preview.png)

Verify that the preview contains both the saved content and the intended code version.

![Published preview content](assets/published-preview.png)

If your code is on a branch other than the one in the preview URL, change the preview URL to that branch. For JCR-backed content, complete [AEM authoring validation and preview](getting-started-aem-authoring.md#preview-site) instead of the Experience Workspace steps above.

## Retain or Hand Over Your Work {#retain-work}

Record source and output URLs, code repository and branch, remote content location, accepted pages, unresolved issues, and the next useful task. See [project handover](project-documentation.md#portable-handoff).

If you transfer an Auto mode run with [**Make it yours**](#make-it-yours), confirm the destination and overwrite choice. Transfer pushes code and copies content separately: either operation can fail independently. Verify both before leaving the source project. Transfer doesn't copy document content into JCR or provide atomic rollback.

## Troubleshooting {#troubleshooting}

If import fails, retain the error and exact source URL. Check source reachability and permissions, correct the extraction or mapping, and retry one affected page before repeating a batch. Do not bypass source access controls. If pages require sign-in, or a capture shows a sign-in page instead of the content, set up [protected site authentication](console.md#protected-site-authentication). If the source site blocks automated access, see [Source Sites with Bot Protection](#bot-protection).

If a change is missing, check each location separately: the console workspace, uploaded remote content, pushed code branch, and previewed page. Reimport can overwrite local content changes; save or reconcile author edits first.

Before reset, discard, replacement, or overwrite, preserve the affected work. Recover code through your repository workflow and restore content separately through the authoring system's available recovery process. A code revert alone does not undo remote document writes.

### Console Preview Differs from the Site {#preview-differs}

The console's preview panel renders the working copy in the console workspace with the workspace's current code. The EDS preview and live sites render the saved content with the code of the branch in their URL. Differences usually have one of these causes:

* **Content not uploaded:** Pages changed in the console are not yet in Experience Workspace. Upload them with **Sync** > **Push** > **Content**.
* **Content edited elsewhere:** Pages changed in Experience Workspace are not yet in the console workspace. **Refresh** in the preview panel only reloads the rendering; to replace the console's copies with the saved documents, use **Sync** > **Pull** > **Content**. This overwrites local edits to those pages.
* **Different code:** The code is not pushed, or the preview URL uses another branch. Push the code, and open the preview URL of the branch that has it.
* **Different width:** The console preview fills the panel by default. Compare at the same width, using the [**Viewport** menu](console.md#content-view).

### Content Writes Fail {#write-errors}

Code and content use different accounts. Code is pushed with your GitHub connection, or your Cloud Manager connection for other Git hosts. Content is written to Experience Workspace with the Adobe account that you signed in with. A code push can therefore succeed while a content upload fails, or the other way round.

If an upload, pull, or transfer says that your Document Authoring session may have expired, sign in again and retry. The console shows the same message when the session is valid but your Adobe account doesn't have write access to the site's content. If it persists, ask the site's administrator to confirm that your account, with the email address and organization that you use in the console, can write to the site in Experience Workspace. Access to AEM in Adobe Admin Console doesn't by itself grant write access to a site's content. If the console says that you are rate limited, wait a minute and retry.

### Git Connection Problems {#git-connection}

The console connects to GitHub through the AEM Code Connector app, or with a personal access token. EDS reads your code through a different app, AEM Code Sync.

|Problem|What to do|
|---|---|
|Your organization or repository isn't listed.|Install the [AEM Code Connector](https://github.com/apps/aem-code-connector) app on the organization or account. If the app is installed for selected repositories only, add this one. If your organization requires approval for GitHub apps, ask an organization owner to approve it. With a token, the console lists only repositories that you can push to.|
|**You don't have write access to** the repository.|Connecting needs push access. Ask a repository administrator for write access, or connect another repository.|
|The console can't verify the preview URL.|Check that the URL follows the pattern `https://{branch}--{site}--{organization}.aem.page` and that the [AEM Code Sync](https://github.com/apps/aem-code-sync) app is installed in the repository.|
|**Pushing is disabled until the AEM Code Connector app is installed**, or **AEM Code Connector required**.|The console can read the repository but can't write to it. Install the AEM Code Connector app on the repository. AEM Code Sync alone isn't enough: it lets EDS read your code, not the console change it.|
|**Invalid or expired token**, or the token lacks user read access.|Create a new token. Use a classic token, or a fine-grained token that can read your user account and write to the repository's contents.|
|**Allow LLM to use my git credentials** isn't in Settings.|The setting isn't available to you yet. The agent can still change code in the console workspace; push it yourself with **Sync** > **Push** > **Code**.|
|**Push denied: you need the Deployment Manager role in Cloud Manager**.|For a repository connected through Cloud Manager, ask your administrator for the Deployment Manager role in Cloud Manager.|

For conflicting changes and protected branches, see [Push Code Changes](#push-code-changes).

### Workspace Setup Takes Time or Fails {#workspace-setup}

When you first open the console, or after a reset, it prepares your console workspace. This can take up to 10 minutes. If all workspaces are in use, the console tells you so and starts setting yours up as soon as one is available; you don't need to retry. If setup fails, the console offers to retry. If it keeps failing, use the **Request support** link on the setup screen. If the console says that your account can't use it, contact your Adobe account team.

### Project Seems Missing {#missing-workspace}

Your console workspace belongs to the Adobe account and organization that you sign in with. If the console opens without your project, sign out, then sign in with the same account and organization that you used before. Don't reset the workspace while you investigate, because a reset permanently deletes its chat history and files. If the project is still missing, [request support](console.md#request-support) with the project name and preview URL. Code that you pushed and content that you uploaded stay in your Git repository and in Experience Workspace.

### Failed to Send Message {#send-failed}

**Failed to send message. Please try again.** means that the console couldn't deliver your prompt to the agent. The message doesn't give the cause, which can be your network connection, an expired sign-in, or a temporary service problem.

1. Check your network connection and send the prompt again. The console doesn't retry automatically.
1. If it fails again, copy your prompt, reload the page, and sign in if asked. Your chat history is kept.
1. If it still fails after a few minutes, use **Request support** in [Settings](console.md#request-support), with the time of the failure and your project name.

If the console instead says that it's at capacity, see [Workspace Setup Takes Time or Fails](#workspace-setup).

### Remove Pages {#remove-pages}

EMA blocks the agent's delete commands in the project's content folder, so that migrated content isn't removed by mistake. Asking the agent to delete pages therefore doesn't work; remove them yourself.

To remove pages from the console workspace, select a page in a [content view](console.md#content-view) and use **Delete**. This deletes one page at a time; you can't delete a folder, and you can't undo it. If pages were imported to the wrong path, import them again to the correct path, check them, and then delete the copies at the wrong path.

**Delete** removes only the console workspace copy. If you already uploaded, previewed, or published a page, also delete it in Experience Workspace or on the AEM author instance, and unpublish or delete it from the preview and live sites with the [AEM Sidekick](https://www.aem.live/docs/sidekick#unpublishing-and-deleting-content).

### Source Sites with Bot Protection {#bot-protection}

Bot protection in a content delivery network (CDN) or web application firewall (WAF) can block or challenge automated access to a source site. This can affect URL discovery, the site catalog, page capture, and import in any workflow, not only Auto mode. Typical signs are access-denied errors such as HTTP 403, 429, or 503, URLs missing after discovery, failed pages, or a challenge or verification page captured instead of the page content.

Migrate only sites that you own or are authorized to migrate. Arrange access with the site's administrator rather than working around the protection:

1. Ask the administrator to allow access for the migration period, for example by allowlisting the [backend addresses](#allowlist-ip-addresses) in the CDN or WAF.
1. If the protection accepts a credential instead, such as a secret request header, enter it in the authentication controls offered by your workflow, such as [Protected site authentication](console.md#protected-site-authentication) in the console settings. Use a scoped credential and remove it when the migration is complete.
1. If the administrator provides an accessible staging or origin host with the same content, use it as the source and record which host the content came from.
1. If only discovery is blocked, provide the list of page URLs to migrate instead.

Verify one representative page before you start a catalog or batch run. After access changes, retry the failed pages, and check captures for challenge or access-denied pages before you accept the content.

### Allowlist IP Addresses {#allowlist-ip-addresses}

Where approved by your source-site administrator, the following backend addresses can be allowlisted for source extraction. Network access alone does not grant authorization or satisfy login requirements, and does not provide VPN/private-network connectivity:

* `34.228.136.112`
* `54.90.51.39`
* `3.224.194.242`

## Additional Resources {#additional-resources}

The following documents may be useful as you continue to explore the Experience Modernization Agent and its console.

* [Experience Modernization Console](console.md) - Details on the console, its views, options, and capabilities
* [Prompting Guide for Experience Modernization Agent](prompting-guide.md) - Ideas on how to prompt the agent and what its skills can do
* [Edge Delivery Services developer tutorial](https://www.aem.live/developer/tutorial) - Useful if you are new to AEM and Edge Delivery Services projects
* [Experience Workspace](https://www.aem.live/docs/ew/about) - The visual authoring UI for document-based EDS content, formerly called Document Authoring
