---
title: Troubleshoot the Experience Modernization Agent
description: Find and fix common problems with the Experience Modernization Agent, including imports and source access, missing changes, previews, content writes, Git connections, the console workspace, sending messages, and removing pages.
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

# Troubleshoot the Experience Modernization Agent {#troubleshooting}

Find the symptom, then follow its section. Most problems come from access to the source site, from the accounts that write code and content to your Adobe Experience Manager Edge Delivery Services site, or from a difference between your console workspace and what is saved in Git and in your content source.

|Symptom|Section|
|---|---|
|An import fails, or a captured page shows an error or a sign-in page.|[Import Fails](#import-fails)|
|URLs are missing after discovery, or the source site returns HTTP 403, 429, or 503.|[Source Sites with Bot Protection](#bot-protection)|
|A change that you made doesn't show up.|[A Change Is Missing](#missing-change)|
|The console preview doesn't match the preview site.|[Console Preview Differs from the Site](#preview-differs)|
|An upload, pull, or transfer fails.|[Content Writes Fail](#write-errors)|
|The console doesn't list your repository, or can't push to it.|[Git Connection Problems](#git-connection)|
|The console keeps preparing your workspace.|[Workspace Setup Takes Time or Fails](#workspace-setup)|
|Your project is gone after you sign in.|[Project Seems Missing](#missing-workspace)|
|**Failed to send message. Please try again.**|[Failed to Send Message](#send-failed)|
|You need to remove imported pages.|[Remove Pages](#remove-pages)|

Before you reset, discard, replace, or overwrite anything, preserve the affected work. Code and content are recovered separately; see [Release, Recover, and Hand Over](production-migration.md#handoff).

If this page doesn't solve the problem, [request support](console.md#request-support) in the console, or select **Get help** on the Auto mode pages.

## Import Fails {#import-fails}

Keep the error and the exact source URL, and check that the URL opens in a browser. If pages require sign-in, or a capture shows a sign-in page instead of the content, set up [protected site authentication](console.md#protected-site-authentication). If the source site blocks automated access, see [Source Sites with Bot Protection](#bot-protection). If the source is reachable, give the agent the error and ask it to fix the import of that page. Retry one affected page before you repeat a batch.

## Source Sites with Bot Protection {#bot-protection}

Bot protection in a content delivery network (CDN) or web application firewall (WAF) can block or challenge the agent's requests to a source site in every workflow: URL discovery, the site catalog, page capture, and import. Typical signs are access-denied errors such as HTTP 403, 429, or 503, URLs missing after discovery, failed pages, or a challenge or verification page captured instead of the page content.

Migrate only sites that you own or are authorized to migrate. Arrange access with the site's administrator rather than working around the protection:

1. Ask the administrator to allow access for the migration period, for example by allowlisting the [backend addresses](#allowlist-ip-addresses) in the CDN or WAF.
1. If the protection accepts a credential instead, such as a secret request header, enter it in the authentication controls offered by your workflow, such as [Protected site authentication](console.md#protected-site-authentication) in the console settings. Use a scoped credential and remove it when the migration is complete.
1. If the administrator provides an accessible staging or origin host with the same content, use it as the source and record which host the content came from.
1. If only discovery is blocked, provide the list of page URLs to migrate instead.

Check one page, including its images and other assets, before you start a catalog or batch run. After access changes, retry the failed pages, and check captures for challenge or access-denied pages before you accept the content.

### Allowlist IP Addresses {#allowlist-ip-addresses}

With your source-site administrator's approval, allowlist these backend addresses for source extraction:

* `34.228.136.112`
* `54.90.51.39`
* `3.224.194.242`

Allowlisting gives network access only: the source must still be reachable over the internet, and protected pages still need [Protected Site Authentication](console.md#protected-site-authentication).

## A Change Is Missing {#missing-change}

Code and content are saved in different places, so check each one: the console workspace, the uploaded content, the pushed branch, and the previewed page. A reimport overwrites local content changes, so upload or reconcile edits before you import a page again. To compare the console preview with the preview site, see [Console Preview Differs from the Site](#preview-differs).

## Console Preview Differs from the Site {#preview-differs}

The console preview and the preview site render different copies of the content and code, as [Know Which Result You Are Viewing](console.md#preview-states) explains. Look for one of these causes:

* **Content not uploaded:** Pages changed in the console are not yet in Experience Workspace. Upload them with **Sync** > **Push** > **Content**.
* **Content edited elsewhere:** Pages changed in Experience Workspace are not yet in the console workspace. Pull them with **Sync** > **Pull** > **Content**, which overwrites local edits to those pages; **Refresh** only reloads the rendering.
* **Different code:** The code is not pushed, or the preview URL uses another branch. Push the code, and open the preview URL of the branch that has it.
* **Different width:** The console preview fills the panel by default. Compare at the same width, using the [**Viewport** menu](console.md#content-view).
* **Markup that the preview site removes:** Edge Delivery Services keeps only sections, blocks, and default content, so styling inside the page markup is lost. Ask the agent to move it into the project's CSS. See [How the Preview Works](console.md#how-preview-works).

## Content Writes Fail {#write-errors}

Code and content use different accounts. Code is pushed with your GitHub connection, or your Cloud Manager connection for other Git hosts. Content is written to Experience Workspace with the Adobe account that you signed in with. A code push can therefore succeed while a content upload fails, or the other way round.

If an upload, pull, or transfer says that your Document Authoring session may have expired, sign in again and retry. The console shows the same message when the session is valid but your Adobe account doesn't have write access to the site's content. If it persists, ask the site's administrator to confirm that your account, with the email address and organization that you use in the console, can write to the site in Experience Workspace. Access to Experience Manager in Adobe Admin Console doesn't by itself grant write access to a site's content. If the console says that you are rate limited, wait a minute and retry.

## Git Connection Problems {#git-connection}

For what each GitHub app does, see [Start from a Repository](getting-started.md#repo-start).

|Problem|What to do|
|---|---|
|Your organization or repository isn't listed.|The AEM Code Connector app is missing from the organization or account, covers other selected repositories only, or waits for an organization owner's approval. Add it as described in [Start from a Repository](getting-started.md#repo-start). With a personal access token, the console lists only repositories that you can push to.|
|**You don't have write access to** the repository.|Connecting needs push access. Ask a repository administrator for write access, or connect another repository.|
|The console can't verify the preview URL.|Without AEM Code Sync in the repository, the site has no preview URL. Check that the app is there, and that the URL follows the pattern `https://{branch}--{site}--{organization}.aem.page`.|
|**Pushing is disabled until the AEM Code Connector app is installed**, or **AEM Code Connector required**.|The console can read the repository but not write to it: AEM Code Sync lets Edge Delivery Services read your code, and only AEM Code Connector lets the console change it. Add AEM Code Connector to the repository.|
|**Invalid or expired token**, or the token lacks user read access.|Create a new token. Use a classic token, or a fine-grained token that can read your user account and write to the repository's contents.|
|**Allow LLM to use my git credentials** isn't in Settings.|The setting isn't available to you yet. The agent can still change code in the console workspace; push it yourself with **Sync** > **Push** > **Code**.|
|**Push denied: you need the Deployment Manager role in Cloud Manager**.|For a repository connected through Cloud Manager, ask your administrator for the Deployment Manager role in Cloud Manager.|

For conflicting changes and protected branches, see [Push Code Changes](getting-started.md#push-code-changes).

## Workspace Setup Takes Time or Fails {#workspace-setup}

Preparing a workspace takes up to 10 minutes, the first time you sign in and after a reset. If all workspaces are in use, the console tells you so and starts setting yours up as soon as one is available; you don't need to retry. If you need it sooner, select **Request support**. If setup fails, the console offers to retry. If it keeps failing, use the **Request support** link on the setup screen. If the console says that your account can't use it, contact your Adobe account team. For a workspace that shows **Your workspace is paused**, see [Open the Experience Modernization Console](getting-started.md#open-console).

## Project Seems Missing {#missing-workspace}

If you belong to several Adobe organizations, the project may be in another organization's [console workspace](getting-started.md#open-console). Sign out, then sign in with the same account and choose the profile of the organization that you used before. Don't [reset the workspace](console.md#settings-page) while you investigate: a reset deletes work that you haven't pushed. If the project is still missing, [request support](console.md#request-support) with the project name and preview URL. Pushed code and uploaded content are safe in your Git repository and content source either way.

## Failed to Send Message {#send-failed}

**Failed to send message. Please try again.** means that the console couldn't deliver your prompt to the agent. The message doesn't give the cause, which can be your network connection, an expired sign-in, or a temporary service problem.

1. Check your network connection and send the prompt again. The console doesn't retry automatically.
1. If it fails again, copy your prompt, reload the page, and sign in if asked. Your chat history is kept.
1. If it still fails after a few minutes, use **Request support** in [Settings](console.md#request-support), with the time of the failure and your project name.

If the console instead says that it's at capacity, see [Workspace Setup Takes Time or Fails](#workspace-setup).

## Remove Pages {#remove-pages}

A safeguard in the console stops the agent from deleting files in the project's content folder, so that migrated content isn't removed by mistake. Asking the agent to delete pages therefore doesn't work. Remove them yourself, in each place where they exist:

* **Console workspace:** In a [content view](console.md#content-view), select the page and use **Delete**, one page at a time. This removes only the console workspace copy.
* **Content source:** Delete uploaded pages in Experience Workspace or on the author instance. Until you do, a page that you deleted in the console reappears in the content view with a cloud icon.
* **Preview and live sites:** Unpublish or delete previewed and published pages with the [AEM Sidekick](https://www.aem.live/docs/sidekick#unpublishing-and-deleting-content).

If pages were imported to the wrong path, import them again to the correct path, check them, and then delete the copies at the wrong path.
