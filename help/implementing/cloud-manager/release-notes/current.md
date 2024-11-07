---
title: Release Notes for Cloud Manager 2024.10.0 in Adobe Experience Manager as a Cloud Service
description: Learn about the release notes for Cloud Manager 2024.10.0 in AEM as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
---
# Release notes for Cloud Manager 2024.10.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager release 2024.10.0 in AEM as a Cloud Service.

>[!NOTE]
>
>See the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release date {#release-date}

The release date for Cloud Manager release 2024.10.0 in AEM as a Cloud Service is October 3, 2024. 

The next release is planned for November 14, 2024.

## What's new {#what-is-new}

* <!-- BOTH CS & AMS --> The AEM Archetype version used in Cloud Manager is now updated to version 26. See [https://github.com/adobe/aem-project-archetype/releases](https://github.com/adobe/aem-project-archetype/releases) 

<!-- (CMGR-59817) -->

* <!-- CS ONLY --> When adding a new custom domain, the previous verification method involved a lengthy DNS validation process. Adobe has simplified this process for customers. Now, you only need to provide a valid SSL certificate (EV or OV), which serves as proof of ownership. There is no longer a need to update TXT records in the DNS.

    >[!NOTE]
    >
    >This feature is only applicable to EV and OV certificates managed by the customer. DV certificates managed by Adobe still require the presence of a CNAME record.

    See [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md).

    ![Verify domain for a customer managed EV/OV certificate](/help/implementing/cloud-manager/assets/verify-domain-customer-managed-step.png)

* <!-- CS ONLY --> When you add or edit network infrastructure, the values in the IP address and network mask fields are validated according to the following rules:

    * The address space must not overlap with the addresses defined in the connection address space.
    * DNS addresses must either belong to the network mask defined in the connection address space or be public.

    ![Add network infrastructure dialog box](/help/implementing/cloud-manager/release-notes/assets/network-infrastructure-add.png)

* <!-- CS ONLY --> Changes are being made to the format of environment deployment logs for indexing, install mutable content, and transform jobs.

    >[!NOTE]
    >
    >This change is planned for rollout in a phased manner with an expected completion date in December 2024.

    ![Deploy to production card](/help/implementing/cloud-manager/release-notes/assets/deploy-to-production-card.png)

    The format of the log is going to change from a simple entry seen in the following:

    ![Log file showing simple entries](/help/implementing/cloud-manager/release-notes/assets/log-file-simple-entry.png)

    To a JSON entry seen in the following:

    ![Log file showing json entries](/help/implementing/cloud-manager/release-notes/assets/log-file-json-entry.png)


## Early adoption program {#early-adoption}

Be a part of Cloud Manager's early adoption program and have a chance to test upcoming features.

### Bring Your Own Git - now with support for GitLab and Bitbucket {#gitlab-bitbucket}

<!-- BOTH CS & AMS -->

The **Bring Your Own Git** feature has been expanded to include support for external repositories such as GitLab and Bitbucket. This new support is in addition to the already existing support for private and enterprise GitHub repositories. When you add these new repos, you can also link them directly to your pipelines. You can host these repositories on public cloud platforms or within your private cloud or infrastructure. This integration also removes the need for constant code synchronization with the Adobe repository and provides the ability to validate pull requests before merging them into a main branch.

See [Add external repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/external-repositories.md).

![Add Repository dialog box](/help/implementing/cloud-manager/release-notes/assets/repositories-add-release-notes.png)

>[!NOTE]
>
>Currently, the out-of-the-box pull request code quality checks are exclusive to GitHub-hosted repositories, but an update to extend this functionality to other Git vendors is in the works.

If you are interested in testing this new feature and sharing your feedback, send an email to [Grp-CloudManager_BYOG@adobe.com](mailto:Grp-CloudManager_BYOG@adobe.com) from your email address associated with your Adobe ID. Be sure to include which Git platform you want to use and whether you are on a private/public or enterprise repository structure.


<!-- ## Bug fixes




## Known issues {#known-issues} -->
