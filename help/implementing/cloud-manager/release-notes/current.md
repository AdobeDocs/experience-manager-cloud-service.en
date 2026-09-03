---
title: Release Notes for Cloud Manager 2026.9.0
description: Learn about the release of Cloud Manager 2026.8.0 in Adobe Experience Manager as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
---
# Release notes for Cloud Manager 2026.9.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

Learn about the release of Cloud Manager 2026.9.0 in AEM (Adobe Experience Manager) as a Cloud Service.

See also the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2026.9.0 in AEM as a Cloud Service is Thursday, September 3, 2026. 

The next planned release is Thursday, October 1, 2026.


## New features - Cloud Manager {#cloud-manager-whats-new}

<!--
* **GitHub Apps for EDS sites**  
    Cloud Manager now exposes an option for managing GitHub App connections on provisioned Edge Delivery Services (EDS) sites. This option allows teams and automation tools to configure GitHub App integrations programmatically, rather than through manual setup for each site. (CMGR-78197) new doc needed
-->

* **Git submodule authentication for external repositories** 
    If your external Git repository (Bring Your Own Git) uses Git submodules, Cloud Manager now automatically authenticates submodule fetches from other repositories in the same organization during pipeline builds. Previously, submodule repositories not individually registered in Cloud Manager failed authentication, so those fetches failed. Credentials are handled server-side and are never exposed to the build environment. No configuration is required, and existing pipelines continue to run without changes. (CMGR-76737) <!-- new doc already added for this release -->

    For more information, see [Git Submodule Support for Adobe Repositories](/help/implementing/cloud-manager/managing-code/git-submodules.md#external-repositories).

* **Content sync API returns an Execution-Id for tracking**  
    Content sync actions triggered through the Cloud Manager API now return an Execution-Id header in the response. Customers can use this identifier to track and correlate the status of a specific content sync operation, making it easier to monitor sync activity from external tooling. (CMGR-78234) <!-- no new doc needed -->

* **GitLab External Git (BYOG) now syncs new branches automatically**
    Customers using GitLab with External Git (BYOG) no longer need to trigger a manual Sync Code action for new branches. New branches are now synced automatically, removing the need for this manual step. (CMGR-77786) <!-- no new doc needed -->
    


## Beta programs {#private-beta-program}

To obtain access to upcoming features before their general release, you can participate in Cloud Manager's beta programs.

>[!IMPORTANT]
>
>Beta releases contain defects and are provided without warranty of any kind. Adobe has no obligation to maintain, correct, update, change, modify or otherwise support the beta releases. Customers use beta releases at their own risk; do not rely on the correct functioning or performance of beta releases, or on any accompanying documentation or materials. Features and APIs in beta are subject to change without notice. Any use of the beta releases is entirely at the customer's own risk.

See also [AEM Beta programs](/help/release-notes/release-notes-cloud/release-notes-current.md#aem-beta-programs)

The following beta program opportunities are currently available:

### Edge Delivery Services with AEM Authoring and flexible publish tier configuration {#eds-with-aem-authoring}

Cloud Manager introduces two capabilities designed to support current delivery architectures.

* **Edge Delivery Services with AEM Authoring**
You can now deliver sites using Edge Delivery Services while continuing to author content in AEM Author mode. Depending on your workflow preferences, you can choose from the following authoring approaches:

    * Document-based authoring
    * AEM-based authoring

For more information, see [Create Edge Delivery site in Cloud Manager](/help/implementing/cloud-manager/edge-delivery/create-edge-delivery-site.md#one-click-edge-delivery-site).

* **Flexible publish tier configuration**

Cloud Manager now lets you configure whether a publish tier is required for your program. This flexibility lets you configure environments that better match your chosen delivery architecture.

For more information, see [Flexible Publish Tier (Beta)](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#flexible-publish-tier).

To join the beta, email [grp-beta_xwalk-publish_config@adobe.com](mailto:grp-beta_xwalk-publish_config@adobe.com) with your Adobe Organization ID and Program ID.



## Bug fixes {#bug-fixes}

* Regenerating a repository access password now invalidates the old password. Previously, regenerating the Git repository access password did not immediately invalidate the previous password, leaving the old credential usable. Regenerating the password now invalidates the old one immediately, ensuring the previous credential can no longer be used. (CMGR-41820)


* EDS site management endpoints returning errors after platform upgrade. Following a platform upgrade, several Edge Delivery Services site management endpoints, such as listing site administrators and connected GitHub Apps, began returning errors. These endpoints have been fixed and now return their results correctly. (CMGR-79247)


* EDS sites fail to serve traffic due to an incorrect stored origin. In some cases a Cloud Manager-connected EDS site returned an unknown-domain error at the CDN because the stored origin incorrectly included a validation challenge path. The stored origin is now recorded correctly, allowing the site to serve traffic as expected. (CMGR-78479)


* Large Git updates cause errors on EDS sites. For Edge Delivery Services sites using External Git (also known as Bring Your Own Git), a push with many changed files is synced only in part. This causes the live site to fail. This occurred because the incoming push notification truncated its list of changed files. Cloud Manager now falls back to a full branch sync when a push reports a large number of changed files, ensuring every changed file is applied and the site stays consistent. (CMGR-79250)


* Environment deletion fails permanently in rare cases. Environment deletion fails permanently when a regional deployment has no associated Kubernetes namespace, leaving the environment in a state that cannot be cleaned up. Deletion now handles this case correctly and completes successfully. (CMGR-79263)


* BYOG repositories using certain certificate authorities incorrectly reported as failing. Bring Your Own Git validation incorrectly reports a connection failure for repositories hosted behind certificates issued by the HARICA certificate authority, misreporting a trust issue as a server error. The certificate authority is now trusted, and these repositories validate successfully. (CMGR-78711)


* Permission checks hardened to enforce resource ownership. Resolved an issue in how permission checks were evaluated so that access to a program is always validated against the organization that owns it. This strengthens isolation between organizations for permission-gated operations. (CMGR-79156)

<!-- There are no significant bug fixes in the July 2026 Cloud Manager release. -->

<!-- ## Known issues {#known-issues} -->

