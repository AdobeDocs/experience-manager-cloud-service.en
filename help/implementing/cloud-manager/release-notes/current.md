---
title: Release Notes for Cloud Manager 2024.10.0 in Adobe Experience Manager as a Cloud Service
description: Learn about the release notes for Cloud Manager 2024.10.0 in AEM as a Cloud Service.
feature: Release Information
role: Admin

---
# Release notes for Cloud Manager 2024.10.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager release 2024.10.0 in AEM as a Cloud Service.

>[!NOTE]
>
>See the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release date {#release-date}

The release date for Cloud Manager release 2024.10.0 in AEM as a Cloud Service is October 3, 2024. The next release is planned for November 14, 2024.

## What's new {#what-is-new}

* j

## Early adoption program {#early-adoption}

Be a part of Cloud Manager's early adoption program and have a chance to test upcoming features.

### Bring Your Own Git - now with extensions for Bitbucket, GitLab, and GitHub Enterprise Server

Following the introduction of direct support for GitHub-hosted repositories in Cloud Manager, you can now also add repositories from Bitbucket, GitLab, or self-hosted GitHub and link them to your pipelines. See [Add external repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/onboard-external-repositories.md). These repositories can be hosted on public clouds or within your private cloud or infrastructure. This integration also removes the need for constant code synchronization with the Adobe repository. 

>[!NOTE]
>
>Currently, the out-of-the-box pull request code quality checks are exclusive to GitHub-hosted repositories, but an update to extend this functionality to other Git vendors is in the works.

If you are interested in testing this new feature and sharing your feedback, send an email to [Grp-CloudManager_BYOG@adobe.com](mailto:Grp-CloudManager_BYOG@adobe.com) from your email address associated with your Adobe ID. Be sure to include which Git platform you want to use and whether you are on a private/public or enterprise repository structure.

### Staging-only and production-only pipelines {#staging-production-only-pipelines}

Adobe announces the introduction of support for [staging-only and production-only pipelines](/help/implementing/cloud-manager/configuring-pipelines/stage-prod-only.md). This new feature lets you divide full-stack production deployment pipelines into smaller, more specialized deployments.

If you would like to test this feature and provide feedback, email [Grp-cloudmanager_splitpipelines@adobe.com](mailto:Grp-cloudmanager_splitpipelines@adobe.com) from your email address associated with your Adobe ID.



## Bug fixes

* Pagination for SSL certificates table view now works as expected. <!-- (CMGR-60804 - [UI] Pagination doesn't work for ssl certificates) -->
* The wrong artifact version got promoted when using the **Promote Build** button from an execution. <!-- ( KEEP IN? SP: YES CMGR-59519 and Slack https://cq-dev.slack.com/archives/C07LFPN2R08/p1725408253474129 ) -->

<!-- * Slack message says next release? SP: REMOVE (Leave in for now) SSL Certificates table in Cloud Manager now enables pagination in the user experience. ( https://jira.corp.adobe.com/browse/CMGR-61041 and Slack https://cq-dev.slack.com/archives/C07LFRE9QJU/p1725408553760009 ) -->



## Known Issues {#known-issues}
