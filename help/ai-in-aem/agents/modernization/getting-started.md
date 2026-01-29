---
title: Getting Started with the Experience Modernization Agent
description: Learn what first steps you need to take to quickly become productive with the Experience Modernization Agent.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
---

# Getting Started with the Experience Modernization Agent {#getting-started}

Learn what first steps you need to take to quickly become productive with the Experience Modernization Agent.

>[!NOTE]
>
>If you are interested in using the Experience Modernization Console, you can request access to ensure a smooth onboarding experience.

## Prepare an Edge Delivery GitHub Repository {#prepare-repo}

1. Select an [Edge Delivery Services](/help/edge/overview.md) repository for use with the Experience Modernization Console.
   * This can be an existing Edge Delivery Services project or you can create a new one following the [developer tutorial](https://www.aem.live/developer/tutorial) using the [boilerplate repository.](https://github.com/adobe/aem-boilerplate)
1. Ensure that the [AEMY GitHub app](https://github.com/apps/aem-aemy) is installed in the repository.
   * This allows the console to inspect your code.
1. Ensure that the [AEM Code Sync GitHub app](https://github.com/apps/aem-code-sync) is installed in the repository.
   * This allows Edge Delivery Services to sync your code.
   * If your repo was based the on the developer tutorial, this step is already complete.

## Open the Experience Modernization Console {#open-console}

1. Navigate to [`aemcoder.adobe.io`.](https://aemcoder.adobe.io)
1. Login with your Adobe ID.

## Connect Your GitHub Repository {#connect-repo}

The console starts empty and requires a connected repository before any work can begin. First-time users see an overlay prompting for a GitHub connection.

1. Switch to the **Code view** (`</>` icon in the left sidebar).
1. Select **Connect** from the GitHub icon menu (top right).
1. Follow the instructions to connect.

## Start Prompting {#start-prompting}

Now that your console can access your code, you are ready to start prompting. For example:

* "Migrate the page `https://wknd-trendsetters.site`."
* "Import the general styles from `https://wknd-trendsetters.site`."

## Upload Content {#upload-content}

To upload your content to [Document Authoring](https://da.live):

1. Switch to the content view (file icon in the left sidebar).
1. Click the **Upload content** button (top right).
1. Enter your GitHub organization name and repository name.
   * For `https://github.com/my-corp/my-eds-project` the organization name is `my-corp` and the repository name is `my-eds-project`.
1. Select the files you want to upload and click upload.

To access the uploaded content in AEM, optionally click **View in AEM** in the notification when the upload completes, or navigate to `https://da.live/#/{organization}/{repository}`.

>[!TIP]
>
>If a [`fstab.yaml`](https://www.aem.live/docs/faq#what-is-fstabyaml) file is present in the repository with the organization and repository configured, the upload dialog will auto-populate these fields.

## Push Code Changes {#push-code-changes}

Once you are satisfied with the changes you have made to your code, you can push them to your GitHub repository.

1. Switch to code view (`</>` icon in the left sidebar).
1. In the list of files changed, if some files show up as untracked, click their `+` button to stage them.
1. Select **Push** from the GitHub icon menu (top right).
1. Choose to push changes to a new PR or the current branch and confirm.
   * When in doubt, you can push to the current branch to keep things simple.

If you wish to directly access the pushed changes in GitHub, click **View PR** in the notification when the push completes.

## Preview Site {#preview-site}

To view the changes in the preview environment:

1. Go back to Document Authoring.
   * It may still be open in a browser tab
   * Or navigate to `https://da.live/#/{organization}/{repository}`
1. Open one of the pages that you previously uploaded to AEM.
1. Click the paper plane icon (top right) and select **Preview**.

Congratulations! Your migrated content and styles are now live on the AEM preview environment.

