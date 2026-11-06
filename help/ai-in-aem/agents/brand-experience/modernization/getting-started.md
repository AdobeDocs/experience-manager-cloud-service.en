---
title: Getting Started with the Experience Modernization Agent
description: Start with Auto mode or from an Edge Delivery Services repository, connect your site to the Experience Modernization Console, and make, save, and publish your first changes.
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

The Experience Modernization Agent builds and changes Edge Delivery Services sites with you. You describe what you want in the Experience Modernization Console, and the agent imports pages, styles them, and writes the code. This guide takes you from access to a first page that you can edit, preview, and publish.

In Edge Delivery Services, a site's code (blocks, styles, and scripts) lives in a Git repository, and its content lives in a separate content source that authors edit. The platform combines the two into fast pages. To learn more, see the [platform overview](/help/edge/overview.md).

In this guide, content is stored in the document-based content repository, where authors edit it in Experience Workspace, the visual authoring UI for Edge Delivery Services. If your content must stay in the JCR of an Adobe Experience Manager author instance, follow the [guide for Experience Manager authoring](getting-started-aem-authoring.md) for the steps that differ. To choose between the two, see [Where Content Is Stored and How Authors Edit It](overview.md#content-storage).

You need access to the Experience Modernization Console, and migrating pages can consume AI credits. See [Access and AI Credit Usage](#access).

## Choose How to Start {#first-outcome}

| Start with | Choose it when | What you do |
|---|---|---|
| [Auto mode, then Make it yours](#brand-trial) | You want to see a few of your own pages on Edge Delivery Services with little effort. | Give Auto mode your site's URL and wait for its email. Review the result, then transfer it to your own site with **Make it yours**. |
| [A new site from the boilerplate](#prepare-repo) | You are starting a new site, or you want to guide the import step by step. | Create a repository from the AEM boilerplate, or from the commerce boilerplate for a storefront, and install two GitHub apps. Connect the site in the console and ask the agent to import pages or build what you need. |
| [Your existing site](#existing-site) | Your site already runs on Edge Delivery Services. | Install the AEM Code Connector app and connect the site. Ask the agent to explain, change, or extend it. |

All three paths end in the same place: your site connected in the console. From there, you [prompt the agent](#start-prompting), then [save, preview, and publish](#save-work) the result. The console is hosted, so none of these paths needs a local development environment.

Before you import, choose a few pages of a site that you are authorized to migrate, including one of each common layout, and decide whether to keep the source design or apply a new one.

## Start with Auto Mode {#brand-trial}

Auto mode migrates a website, or a list of its pages, without step-by-step prompting. In the [guided workflow](#guided-import), the agent stops after each step for your review. In Auto mode, it imports the content, migrates the design, critiques the result against the source, and keeps refining it until its critique finds the pages close to the source.

Because it checks and refines its own work, Auto mode takes much longer than a guided import of the same pages, so it suits a first result that you collect later. Once a run starts, it doesn't ask for your input: you steer it only through the scope and options that you choose before you start. Auto mode starts from a website's URL, not from a repository; if your site is already on Edge Delivery Services, [connect it](#existing-site) instead. It produces document-based content; for content stored in the JCR, use the [guide for Experience Manager authoring](getting-started-aem-authoring.md).

1. Open [Auto mode](https://aemcoder.adobe.io/auto). If your account doesn't have it yet, select **Sign up**; you receive an email when your access is available.
1. Provide your site URL, or choose selected pages and list their URLs. Review the scope, settings, and [limits](#auto-mode-limits) shown before you start.
   * For a protected source site, enter credentials in the authentication fields that Auto mode offers, not in chat.
   * If Auto mode offers **Include integrations**, select it to carry over supported integration settings from the source site, such as analytics, tag manager, and consent settings. They stay switched off on the new site until you turn them on.
1. Start the run. A run can take up to 24 hours. You can leave the page; you receive an email when the run finishes. If the email doesn't arrive, check your spam folder.
1. Review which pages were migrated, and check their content, links, images, and styles. The run also shows its preview, repository, report, and errors. Links to pages that the run didn't migrate can still point to the source site.
1. Open the resulting site with **Open site**. To keep working on it, transfer it to your own site with [**Make it yours**](#make-it-yours), then import further pages and refine the result in the console.

### Auto Mode Limits {#auto-mode-limits}

Auto mode limits each account by the number of pages per migration, the number of migrations, and how many migrations can run at the same time. The Auto mode page shows the limits that apply to you before you start:

* By default, each migration can include up to 10 pages. A full-site run migrates a preview of up to that many pages, not the whole site; migrate the rest later in the console.
* If you have used all the migrations your account allows, or have as many running as allowed, Auto mode tells you so. Wait for a run to finish, or request more.
* To ask for more pages or migrations, use **Ask for a higher limit**, or **Get help** in the header. The team that builds the agent replies by email.

To stop a run, use **Cancel migration**. A cancelled run can't be resumed; start a new migration instead.

### Make It Yours {#make-it-yours}

An Auto mode run creates its site in an Adobe-managed location. To keep working on it in your own site, select **Make it yours** on the finished run. This transfers the run's code and content to a site that you own. It doesn't migrate anything again.

Prepare the destination first:

* A site whose code is in a GitHub repository created from an Edge Delivery Services template, with the AEM Code Sync and AEM Code Connector apps installed. The quickest way is to [create a new site from the boilerplate](#prepare-repo). A repository on [another Git host](#other-git) that is connected through Cloud Manager can also be used.
* A `main` branch in the repository, and the site's content stored in the document-based content repository. Nothing is transferred to a destination whose content is stored elsewhere, such as on an author instance.
* Write access to the repository and to the site's content, for the Adobe account that you use in the console.
* A site other than the run's own site.

To transfer the run:

1. Choose the destination site. If you are not yet connected to GitHub, the console asks you to connect first.
1. Review the destination repository, preview URL, and the new branch that will receive the code. Choose whether to overwrite existing pages and whether to preview the transferred pages.
1. Select **Start transfer** and follow its progress. The code is placed on a new branch, and the content is copied to the destination content location. For a document-based destination, the transfer also turns on Experience Workspace for the destination site. If that step fails, the console shows a warning; ask the site's administrator to turn Experience Workspace on.
1. Select **Open in EMA** to continue on the destination site in the console, or **Edit Site** to edit the content. If the console doesn't open on the destination site, [connect it](#connect-repo).

The transfer copies the following:

| What | How it is transferred |
|---|---|
| Code | Pushed to a new branch, created from the destination's `main` branch. On that branch, the run's project replaces the destination's code files. Nothing is merged into `main`. |
| Pages | Copied as documents to the destination's content in Experience Workspace, with the images and other media that they reference. |
| Existing pages | Skipped unless you choose to overwrite them. Before it overwrites a page, the transfer saves the page's current state as a version named **Before Transfer**, which you can restore from the page's version history in Experience Workspace. |
| Preview | If you choose, the transferred pages are previewed on the destination's `*.aem.page` site. They are not published. |

The transfer doesn't copy spreadsheets, such as redirects, bulk metadata, or placeholders; access permissions; site and organization configuration; or the run's Git history and GitHub workflow files.

If the transfer stops with an error, nothing is merged into `main`, but code and content are transferred separately, so check both the branch and the pages. If the new branch already exists, choose another branch name.

A transferred site isn't live yet. Agree who owns each remaining step:

* Review the transfer branch and merge it into `main` according to your repository policy. The merge changes the live site's code; see [How Changes Go Live](overview.md#code-content-lifecycle).
* Set up who can edit, preview, and publish the content. See [Permissions and security](https://www.aem.live/docs/ew/administering/permissions).
* Recreate the spreadsheets that you need, and check the site's Experience Workspace configuration, such as its block library. See [Configs](https://www.aem.live/docs/ew/administering/configs).
* [Publish](#publish) the pages that you accept. The transfer doesn't publish anything.
* Switch your domain to the site. See [Release, Recover, and Hand Over](production-migration.md#handoff).

In the console, continue with [prompts to start with](#first-prompts), then [save, preview, and publish](#save-work) your changes.

## Start from a Repository {#repo-start}

To work in the console, a GitHub repository needs two GitHub apps with similar names and different jobs:

* [AEM Code Sync](https://github.com/apps/aem-code-sync) lets Edge Delivery Services read your code so that it can serve your site. Every site whose code is on GitHub has it.
* [AEM Code Connector](https://github.com/apps/aem-code-connector) lets the console push changes and open pull requests in your repository. Until it is installed, the console can't push code or open pull requests.

>[!NOTE]
>
>For content stored in the JCR of an author instance, set up the repository with the [guide for Experience Manager authoring](getting-started-aem-authoring.md) instead.

### Create a New Site from the Boilerplate {#prepare-repo}

Use this path for a new site, including one that you fill with pages imported from an existing website.

1. Create the site from the [AEM boilerplate](https://github.com/adobe/aem-boilerplate) by following the first section of the [developer tutorial](https://www.aem.live/developer/tutorial), **Get started with the boilerplate repository template**:
   * Select **Use this template** to create your repository on GitHub.
   * Install the AEM Code Sync app for this repository only.
   * Optionally change the site's administrators and content source, then select **Finish setup**.

   Your site now runs at `https://main--{repository}--{owner}.aem.page/`, with example content that you can edit in Experience Workspace. You don't need the tutorial's local development steps, because the console provides the development environment.

   For a commerce storefront, create the site from the [commerce boilerplate](https://experienceleague.adobe.com/en/tools/commerce-storefront/boilerplate/) and follow its setup instead. It contains the commerce blocks and drop-in components, which are hard to add later to a site that started from the AEM boilerplate. See [Commerce Pages](block-development.md#commerce-pages).
1. Install the [AEM Code Connector](https://github.com/apps/aem-code-connector) app in the repository.
   * If the app is installed for selected repositories only, include this one. If your organization requires approval for GitHub apps, an organization owner must approve it.
1. [Open the console](#open-console) and [connect the site](#connect-repo).

### Bring Your Existing Site {#existing-site}

If your site already runs on Edge Delivery Services, you don't need to recreate it or migrate it again. Connect it, and the agent works on its code and content as they are.

1. On GitHub, check that the AEM Code Sync app is installed in the repository. If the site is already served from this repository, it is.
1. Install the [AEM Code Connector](https://github.com/apps/aem-code-connector) app in the repository, as for a new site.
1. [Open the console](#open-console) and [connect the site](#connect-repo).
1. Before you change anything, ask the agent to explain the project. Then make a first visual change with [Inspect mode](#inspect-mode). See [Prompts to Start With](#first-prompts).

Projects created from the current boilerplate include `AGENTS.md`, where you keep the project's instructions for the agent, and a one-line `CLAUDE.md` that makes the agent load `AGENTS.md` in every conversation. Older projects may not have them; ask the agent to add them from the current boilerplate. See [Project Instructions](project-instructions.md#agents-md).

To restyle your site or build blocks, see [Restyle an Existing Site](restyling.md#existing-site) and [Block Development](block-development.md). A migration is not required.

### Use Another Git Host {#other-git}

Edge Delivery Services also supports GitHub Enterprise (self-hosted), Adobe-hosted repositories, GitLab, Bitbucket, and Azure DevOps. Onboard the repository in Adobe Cloud Manager, the Experience Manager as a Cloud Service tool for managing programs, environments, and code repositories. Then configure your site to use it. See [Bring Your Own Git](https://www.aem.live/developer/byo-git).

>[!IMPORTANT]
>
>The console pushes changes to your repository. For repositories connected through Cloud Manager, it pushes a branch but doesn't open a pull request; open one in your Git host if you need a review. The access token you create in Cloud Manager must grant write access to repository code, alongside the permissions listed at [step 8 of Add external repositories](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/managing-code/external-repositories).
>
>If you already onboarded a token without write access, edit it in Cloud Manager under **Repositories > Manage Access Tokens** and paste a value that includes write access; you don't need to onboard the repository again. See [Manage access tokens](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/managing-code/manage-access-tokens#edit-access-tokens).

## Open the Experience Modernization Console {#open-console}

1. Navigate to [`aemcoder.adobe.io`.](https://aemcoder.adobe.io)
1. Log in with your Adobe ID.
   * Use an account that belongs to your company's Adobe organization. A personal Adobe ID that isn't part of an organization can't be used; the console explains this and lets you **Use a different account**. If you don't have a company account, ask your Adobe account team to add you to the organization.

The console keeps a hosted working copy of your project, called the console workspace in these docs; it is unrelated to Experience Workspace, the authoring UI. The agent imports content and changes code there until you upload or push. The console sets up your workspace the first time you sign in, which can take up to 10 minutes. Each Adobe organization that you sign in with has its own workspace, with its own projects and chats; to switch, sign out and sign in with the other organization's profile. After a period of inactivity, the workspace pauses. When you return, the console shows **Your workspace is paused**; select **Wake up** and wait a few minutes while it is restored.

### Demo Mode {#demo-mode}

If the console opens in demo mode, a **Demo site** button shows in the header. You can explore the sample project and try importing pages, but work in the demo site isn't saved, and the demo site can't push code to GitHub or upload content to Experience Workspace.

![Demo mode](assets/demo-mode.png)

## Connect Your Site {#connect-repo}

Connect the site that you created from the boilerplate, transferred with **Make it yours**, or already had.

1. Select **Demo site** in the header and then **Switch site**, or use **Switch site** in [Settings](console.md#settings-page).
1. This prompts you to authorize the AEM Code Connector app using your GitHub credentials. Select **Authorize AEM Code Connector**.
   * For GitHub Enterprise, or when OAuth sign-in isn't available, open **More ways to connect** and select **Sign in with a token** instead. Enter the **GitHub Host** and a **Personal Access Token**. A fine-grained token limited to the repositories you need is recommended. The token must be able to read your user account and push to the repository; with a token, the console lists only repositories that you can push to.
1. Back in the console, specify the preview URL of the site. Preview URLs follow the pattern `https://{branch}--{site}--{organization}.aem.page`, where `{site}` is the GitHub repository name and `{organization}` is the GitHub organization or user that owns it. You can copy one by previewing any page of the site, or construct it from those names. The console finds the associated GitHub repository automatically. Alternatively, you can search through your authorized GitHub projects to find a site.
   ![Connecting to GitHub project](assets/connect-site-and-github.png)
1. Select **Checkout to workspace** once the site has been verified. This copies the project into your console workspace.
1. When prompted to **Replace existing workspace**, verify that the current work is saved elsewhere, then select **Replace workspace**.
   ![Replace existing workspace](assets/replace-existing-workspace.png)

Your site and its GitHub repository are now connected to the console.

Confirm the connected repository, branch, and content destination before requesting changes. Connecting needs write access to the repository. If your organization or repository isn't listed, or the console can't verify the preview URL, see [Git Connection Problems](troubleshooting.md#git-connection).

![Site connection](assets/first-sign-on.png)

## Console Home {#console-home}

Until you start a conversation, the console opens on its **Home** page. Type a request, or select one of the suggested prompts, which are grouped by task. A request that you type runs at once. Most suggested prompts run in [Plan mode](console.md#prompt-input): the agent proposes its steps without changing any files, and you select **Execute plan** to carry them out.

![Console home](assets/console-home.png)

## Start Prompting {#start-prompting}

Once your site is connected, describe what you want in plain language. Say what result you expect and on which page, rather than how to write the code. The agent knows Edge Delivery Services, so you can also ask it how a part of your site works or what a platform term means. To learn how a page is built from sections, blocks, and default content, see [Markup, Sections, Blocks, and Auto Blocking](https://www.aem.live/developer/markup-sections-blocks).

>[!CAUTION]
>
>Never type, paste, or attach passwords, API keys, tokens, or other secrets in the chat. Everything in the chat reaches the AI model, and the agent can copy it into your project's files. Enter credentials in the console's **Settings**. See [Keep Secrets Out of the Chat](prompting-guide.md#secrets).

On a new site, start by [importing a page step by step](#guided-import). On a site that already has pages, such as your existing site or one transferred with **Make it yours**, ask the agent to explain the project, then [make a visual change with Inspect mode](#inspect-mode) or import further pages. See [Prompts to Start With](#first-prompts).

### Import a Page Step by Step {#guided-import}

Importing pages from an existing website is the most common way to start. In the guided workflow, the agent stops after each step so that you can check it: first the page's content, then its design. Save each result as soon as you have checked it: upload the content after the content step, and push the code after the design step.

1. Optionally, scope the source site first. Ask "scope site `https://www.example.com`". The agent finds the site's pages and groups those that share a layout into templates, which you review in the **Planning** view. Choose your first page from a template that covers many pages, because the blocks that it creates can be reused on all of them. See [Site Catalog](site-catalog.md).
1. Start with one authorized source page. Replace the example URL and destination in this prompt:
   * "Migrate only `https://www.example.com/about` to `/about` in this project. Target document-based content. Preserve its text, images, and links. Reuse existing blocks and default content. Do not upload, push, or publish."
   * For Experience Manager authoring, say that the content is stored in the JCR, and follow the [checks for that setup](getting-started-aem-authoring.md#validate-content).
1. Review the imported page, its destination path, and any reported gaps.
   ![Content import](assets/content-import.png)
1. Once the page is imported, the **Workspace** panel shows it. Select the page to render it in the console's preview panel on the right. This preview shows the working copy in the console workspace, not the preview site on `aem.page`.
   ![Content imported](assets/content-imported.png)
1. Check the page's structure as well as its text. The **Document view** of the preview panel shows how the content is split into sections, blocks, and default content; see [Content Views](console.md#content-view). Most of a page should be default content: headings, text, images, and links. A block belongs only where authors must mark which content forms a component, such as a set of cards; CSS and JavaScript can lay out default content however the design needs. Authors will edit this structure, so ask the agent to simplify it now, before more pages reuse it. See [Shape the Content Structure](production-migration.md#content-structure).
1. Upload the content, so that it is saved and authors can edit it. Until you upload it, the imported page exists only in the console workspace, and pushing code doesn't save it.
   * For document-based content, see [Upload Content](#upload-content). You can then open the page and edit it.
   * For Experience Manager authoring, see [Upload Content](getting-started-aem-authoring.md#upload-content) in the guide for that setup.
1. Now that you have content, request faithful source styling, or explicitly choose a [new target design](restyling.md). Styling changes only the project's CSS and JavaScript; the content that you uploaded stays as it is.
   * "Import the general styles from `https://www.example.com/about`, then style the blocks used on `/about`. Preserve the imported content."
1. When the agent has finished, select **Refresh preview** in the preview panel to see the styled page.
   ![Styles imported](assets/styles-imported.png)
1. Review the styled page at desktop and mobile widths. Compare its text, links, images, and structure with the source page, and ask the agent to fix what differs. Describe the visual differences that remain too; complex designs can take several rounds. See [How Close the Design Gets](prompting-guide.md#design-fidelity).
1. Push the code, so that the new blocks and styles are saved in your repository and show on the site's preview. See [Push Code Changes](#push-code-changes).

The page import doesn't build the shared navigation and footer; ask for them separately. Next, [preview and publish](#save-work) the page. For more pages, repeat these steps and ask the agent to reuse the blocks that it has created. Once your first pages look right, ask it to document its blocks and styles for later conversations; see [Let the Agent Maintain the Files](project-instructions.md#maintain).

### Make a Visual Change with Inspect Mode {#inspect-mode}

On a site that already has pages, such as your existing site or a site that you transferred with **Make it yours**, a visual change is the quickest way to see a result. Point at what you want to change rather than describe where it is: turn on **Inspect mode** in the preview panel, select the element, and describe the change, for example "Make this button use the primary button style". [Make Your First Change](visual-changes.md#first-change) gives the steps, including how to check each screen width and undo a change. Then [push the code](#push-code-changes) to keep it.

### Prompts to Start With {#first-prompts}

Replace the example URLs and paths with your own.

**A new site from the boilerplate:**

* "Explain the sections and blocks on the home page, and which files style each one."
* "Create a new page `/offers` from this Figma frame: `{Figma link}`." See [Create a New Page from Figma](prompting-guide.md#figma-new-page-from-figma).

**After Make it yours:**

* "Compare `/about` with `https://www.example.com/about` and fix the differences in layout and images."
* "Migrate `https://www.example.com/contact` to `/contact`. Reuse the existing blocks."

**Your existing site:**

* "Give me a tour of this project: list its blocks, what each one does, and which pages use them."
* "Add a variant of the cards block with a dark background, and show it on `/products`."
* "Check whether this project has the `AGENTS.md` and `CLAUDE.md` files of the current AEM boilerplate, and add them if they're missing."

### Prompting Tips {#prompting-tips}

* Ask for one change at a time, and check it before you ask for the next one. If a long task stops before it finishes, ask the agent to continue.
* Say what the agent must not do. The example prompts in these guides end with "Do not upload, push, or publish." This keeps the agent's work in your console workspace, so that you check it and then upload or push it yourself. Leave it out when you want the agent to do these steps for you and have turned on the [agent permissions](console.md#settings-page) that they need.
* For a change that spans several pages or shared styles, switch to [Plan mode](console.md#prompt-input) to review the steps before anything changes.

The agent knows only what is in the current conversation and in your project's files. Give it the context that it can't know, such as requirements, brand rules, screenshots, and links to the documentation of other systems; see [Give the Agent Context](prompting-guide.md#context). To make it follow your project's conventions in every conversation, ask it to write them in `AGENTS.md` and the files that `AGENTS.md` lists; see [Project Instructions and Memory](project-instructions.md). For prompts for each task, see the [Prompting Guide](prompting-guide.md).

## Save, Preview, and Publish {#save-work}

The agent's work stays in the console workspace until you save it elsewhere. Each of the next steps moves work to a different place:

* **Upload** copies content from the console workspace to its authoring destination: Experience Workspace for document-based projects, or the author instance for Experience Manager authoring. In the **Sync** menu, this is **Push** > **Content**.
* **Push** commits code to your Git repository, on the current branch or as a pull request.
* **Preview** and **Publish** put saved content on the preview site, `*.aem.page`, and then on the live site, `*.aem.live`.

Upload and push separately. Edge Delivery Services stores content apart from code, so pushing code doesn't save your pages, and uploading doesn't save your code. Your first result is complete when you can reopen the page in Experience Workspace, edit it, and see the requested change on the preview site, not merely when a preview link exists.

### Upload Content {#upload-content}

Upload the pages to the document-based content repository, where authors edit them in Experience Workspace. Some console labels and screens still say Document Authoring. Before you upload, confirm the destination and that you may replace any existing pages there. The upload uses your own content permissions; see [Content Push Permissions](evaluate.md#content-push-permissions). For Experience Manager authoring, follow [Upload Content](getting-started-aem-authoring.md#upload-content) in the guide for that setup instead.

1. In a **Content** view, the default view of the workspace, select **Upload content** at the top right. Alternatively, use **Sync** > **Push** > **Content** in the workspace header to upload all pending pages.
1. The **Upload content** dialog opens with the destination **Organization** and **Site** filled in from your site's configuration. If the fields are empty, enter the organization and site of your content in Experience Workspace.
1. Choose the files you want to upload and select **Upload**.
   ![Upload content dialog](assets/upload-content.png)
1. Once complete, the dialog shows how many files were uploaded. You can then preview, or preview and publish, the uploaded pages. The upload continues if you close the dialog; retry any pages that fail.
   ![View in AEM](assets/view-in-aem.png)

To find the uploaded content, select **View in AEM** in the notification when the upload completes, which opens the site's content in Experience Workspace, or go to `https://da.live/#/{organization}/{repository}`.

![Content in Document Authoring](assets/content-in-document-authoring.png)

Open an uploaded page, make an edit, save, and reopen it to check that authors can edit it and that the change persists. Where Experience Workspace is turned on for the site, **Edit in Experience Workspace** in the console opens the selected page in its visual editor.

### Push Code Changes {#push-code-changes}

Review the code diff and run the project's checks before pushing. Use a pull request for work that needs review; for what enforces review, see [Control over Changes](evaluate.md#security-control).

1. Optionally, switch to **Changes** view (branch icon in the view picker) to review the diff.
   ![Code view](assets/code-view-git-changes.png)
1. Open **Sync** in the workspace header and select **Push** > **Code**.
1. In the **Stage changes** dialog, stage the files you want to push and select **Continue**.
1. In the **Push changes** dialog, enter a commit message. Choose to create a new PR (default) or push to the current branch and select **Confirm** to push.
   * **Create new PR** pushes a new branch, named `aem-` followed by the date and time, and opens a pull request into the current branch. The pull request lists preview URLs of your pages on the new branch, so that reviewers can check the result. Your console workspace stays on the new branch; to continue on the original branch, switch back to it with **Switch branch** in the [Changes view](console.md#changes-actions).
   * **Push to current branch** adds the commit to the current branch, and updates its pull request if it has one. Use it only when your project's policy permits it and you intend to change that branch. On `main`, the change goes live at once.
1. Once complete, a notification appears at the bottom of the console.
   ![View PR](assets/view-pr.png)

If a pull request was created, select **View PR** in the completion notification. Otherwise, such as for a [repository connected through Cloud Manager](#other-git), verify the commit on the destination branch. If the branch is protected against direct pushes, push with **Create new PR**.

![Code in GitHub](assets/code-in-github.png)

Your code is now in GitHub. It shows on that branch's preview and live URLs straight away.

#### Commit Identity {#commit-identity}

The console commits with the Git identity, `user.name` and `user.email`, configured in your console workspace, and uses a default value for either one that is missing. Neither connecting your Git account nor the Git settings on your own computer set this identity.

#### If Someone Else Changed the Branch {#push-conflicts}

A branch is a sequence of saved changes, called commits. Your console workspace holds the branch as it was when you last pulled it, so if someone else has pushed to it since, the repository has commits that your workspace doesn't. **Push to current branch** then adds your commit after theirs and pushes again. If you changed different files or lines, this succeeds without anything more from you.

If you both changed the same lines, Git can't decide which version to keep. This is a conflict. The console shows **Push failed: Remote has conflicting changes that cannot be merged automatically**, keeps your changes, and switches the dialog to **Create new PR**.

1. Select **Confirm**. The console pushes your changes to a new branch and opens a pull request into the branch that you were working on.
1. Select **View PR** in the notification.
1. Resolve the conflicts. If only a few lines conflict, select **Resolve conflicts** in GitHub and keep the right version of each part; see [Resolving a merge conflict on GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github). If the conflicts span many files, ask a developer to resolve them in a local copy of the repository.
1. Once the pull request is reviewed, merge it.

The console doesn't merge branches or resolve conflicts itself. **Sync** > **Pull** > **Code** works the same way: if your commits conflict with the remote changes, it cancels the pull, leaves your work as it was, and suggests pushing to a new branch or asking the agent to help. To avoid conflicts, pull before you start a task, push small changes often, and agree with your team who changes which files. See [Work as a Team](production-migration.md#collaboration).

### Preview Site {#preview-site}

The console's preview panel shows only the working copy in the console workspace. To check the uploaded pages on the preview site with your code:

1. Go back to Experience Workspace, or go to `https://da.live/#/{organization}/{repository}`.
1. Open one of the pages that you previously uploaded.
1. Select the paper plane icon (top right), then **Preview**.
   ![Publish to preview](assets/publish-to-preview.png)

Verify that the preview contains both the saved content and the intended code version.

![Published preview content](assets/published-preview.png)

If your code is on a branch other than the one in the preview URL, change the preview URL to that branch. For Experience Manager authoring, follow [Validate Authoring and Preview](getting-started-aem-authoring.md#preview-site) instead.

### Publish {#publish}

When the preview looks right, publish the page to make it live on `*.aem.live`:

* In Experience Workspace, open the page, select the paper plane icon, then **Publish**.
* Or, after an upload in the console, choose to preview and publish the uploaded pages.

Publishing makes the page public. Who can publish is set by the site's publish role; follow your team's review process. Code doesn't need this step: it goes live as soon as it reaches `main`. See [Control over Changes](evaluate.md#security-control).

## Create a Customer Demo {#customer-demo}

A demo shows a few complete, branded pages of a site that you are authorized to use, along a path that you walk your audience through. It needs no production cutover, and shouldn't be presented as production-ready.

1. Choose the pages and the demo's goal. Include a typical page, not only the easiest one.
1. Use [Auto mode](#brand-trial), or [import the pages step by step](#guided-import), naming the exact page list.
1. Keep the source design, or [apply a new one during migration](restyling.md#during-migration). Complete the navigation, footer, and assets that the demo path needs.
1. Check text, images, links, layout, and mobile behavior, and walk the demo path. Note mocked interactions, integrations that aren't connected, and pages outside the scope.
1. Hand over the preview links, the source page behind each one, and the known gaps. See [Retain Context for People and Agents](project-documentation.md#portable-handoff).

## Access and AI Credit Usage {#access}

Request access to the Experience Modernization Console through your Adobe account manager, and sign in with an Adobe ID that belongs to your company's Adobe organization. Auto mode needs no request through your account manager; sign up on its page, as in [Start with Auto Mode](#brand-trial).

Signing in doesn't establish your organization's entitlement. Depending on your organization's agreement, migrating pages consumes AI credits:

* Credits are counted for each page that is uploaded to your content destination, Experience Workspace or the author instance, not for prompts or for iterations in the console.
* Each upload counts, including an upload of a page that you uploaded before. Check a page in the console's preview, and upload it once it's ready.
* A restyle changes code, not content, so it needs no new upload.
* Auto mode runs don't consume AI credits. **Make it yours** counts the pages that it copies to Experience Workspace.
* Pages that the agent uploads for you count the same as pages that you upload.

For how Adobe measures AI credit consumption for agentic capabilities, see [AI credit consumption](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/overview/ai-credit-consumption). For your organization's entitlement, usage, and commercial terms, contact your Adobe account team.

## Troubleshooting {#troubleshooting}

For problems with imports, source access, uploads, previews, Git connections, or the console workspace, see [Troubleshoot the Experience Modernization Agent](troubleshooting.md). If that doesn't solve the problem, [request support](console.md#request-support) from the team that builds the agent.

## Additional Resources {#additional-resources}

* [Migrate a Production Site](production-migration.md) - Migrate a whole site and take it live
* [Project Instructions and Memory](project-instructions.md) - Keep your project's conventions in every conversation
* [Experience Modernization Console](console.md) - Details on the console, its views, options, and capabilities
* [Prompting Guide for Experience Modernization Agent](prompting-guide.md) - Prompts for each task, and what the agent's skills can do
* [Troubleshoot the Experience Modernization Agent](troubleshooting.md) - Fixes for common problems
* [Edge Delivery Services developer tutorial](https://www.aem.live/developer/tutorial) - Useful if you are new to building these sites
* [Experience Workspace](https://www.aem.live/docs/ew/about) - Edit, preview, and publish document-based content
