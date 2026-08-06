---
title: Release Notes for Cloud Manager 2026.8.0
description: Learn about the release of Cloud Manager 2026.8.0 in Adobe Experience Manager as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
---
# Release notes for Cloud Manager 2026.8.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

Learn about the release of Cloud Manager 2026.8.0 in AEM (Adobe Experience Manager) as a Cloud Service.

See also the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2026.8.0 in AEM as a Cloud Service is Thursday, August 6, 2026. 

The next planned release is Thursday, September 3, 2026.


### Git submodule authentication for external repositories

If your external Git repository (Bring Your Own Git) uses Git submodules, Cloud Manager now automatically authenticates submodule fetches from other repositories in the same organization during pipeline builds. Previously, submodule repositories not individually registered in Cloud Manager failed authentication, so those fetches failed. Credentials are handled server-side and are never exposed to the build environment. No configuration is required, and existing pipelines continue to run without changes.

For more information, see [Git submodule support for external repositories](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/managing-code/git-submodules#external-repositories).


## New features - Cloud Manager {#cloud-manager-whats-new}

* **GitHub Apps for EDS sites**  
    Cloud Manager now exposes an option for managing GitHub App connections on provisioned Edge Delivery Services (EDS) sites. This option allows teams and automation tools to configure GitHub App integrations programmatically, rather than through manual setup for each site. (CMGR-78197) <!-- new doc needed -->

* **Git submodule authentication for external repositories** 
    If your external Git repository (Bring Your Own Git) uses Git submodules, Cloud Manager now automatically authenticates submodule fetches from other repositories in the same organization during pipeline builds. Previously, submodule repositories not individually registered in Cloud Manager failed authentication, so those fetches failed. Credentials are handled server-side and are never exposed to the build environment. No configuration is required, and existing pipelines continue to run without changes. (CMGR-76737) <!-- new doc already added for this release -->

    For more information, see [Git Submodule Support for Adobe Repositories](/help/implementing/cloud-manager/managing-code/git-submodules.md#external-repositories).

* **Content sync API returns an Execution-Id for tracking**  
    Content sync actions triggered through the Cloud Manager API now return an Execution-Id header in the response. Customers can use this identifier to track and correlate the status of a specific content sync operation, making it easier to monitor sync activity from external tooling. (CMGR-78234) <!-- no new doc needed -->

* **GitLab External Git (BYOG) required a manual Sync Code step for new branches**
    Customers using GitLab with External Git (BYOG) manually triggered a Sync Code action in Cloud Manager before the Edge Delivery Services webhook picked up a new branch. New branches are now synced automatically, removing the need for this manual step. (CMGR-77786) <!-- no new doc needed -->
    






## Beta programs {#private-beta-program}

To get exclusive access to upcoming features before their general release, you can participate in Cloud Manager's beta programs.

>[!IMPORTANT]
>
>Beta releases contain defects and are provided "AS IS" without warranty of any kind. Adobe has no obligation to maintain, correct, update, change, modify or otherwise support the beta releases. Customers use beta releases at their own risk; do not rely on the correct functioning or performance of beta releases, or on any accompanying documentation or materials. Features and APIs in beta are subject to change without notice. Any use of the beta releases is entirely at the customer's own risk.

See also [AEM Beta programs](/help/release-notes/release-notes-cloud/release-notes-current.md#aem-beta-programs)

The following beta program opportunities are currently available:

### Edge Delivery Services with AEM Authoring and flexible publish tier configuration {#eds-with-aem-authoring}

Cloud Manager introduces two capabilities designed to support modern delivery architectures.

* **Edge Delivery Services with AEM Authoring**
You can now deliver sites using Edge Delivery Services while continuing to author content in AEM Author mode. Depending on your workflow preferences, you can choose from the following authoring approaches:

    * Document-based authoring
    * AEM-based authoring

For more information, see [Create Edge Delivery site in Cloud Manager](/help/implementing/cloud-manager/edge-delivery/create-edge-delivery-site.md#one-click-edge-delivery-site).

* **Flexible publish tier configuration**

Cloud Manager now lets you configure whether a publish tier is required for your program. This flexibility lets you set up environments that better match your chosen delivery architecture.

For more information, see [Flexible Publish Tier (Beta)](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#flexible-publish-tier).

To join the beta, email [grp-beta_xwalk-publish_config@adobe.com](mailto:grp-beta_xwalk-publish_config@adobe.com) with your Adobe Organization ID and Program ID.




## Bug fixes {#bug-fixes}

* Forms add-on incorrectly blocked on programs with Enhanced Security enabled. Customers with Enhanced Security enabled on their program were unable to add the Forms add-on to a Sites environment, even though the two are fully compatible. This restriction has been removed, and Forms can now be added normally regardless of Enhanced Security configuration. (CMGR-78266)

* Content Hub credit not released after restoring an environment from soft delete. When an environment was restored from a soft-deleted state, its associated Content Hub credit remained marked as consumed even though the environment was active again. Cloud Manager now correctly re-consumes the credit on restore, ensuring credit usage accurately reflects the environment's real state. (CMGR-78204)

* Custom domain mappings stuck in Pending for EDS sites with many domains. EDS sites configured with a large number of domains experienced domain mappings that remained stuck in a Pending state indefinitely, due to a memory issue in the underlying status update process. This issue has been resolved, and domain mapping status now updates reliably regardless of domain count. (CMGR-78179)

* Production-only pipelines incorrectly showed an editable Build variable service. Pipelines configured to run production deployments only, with no build phase — were still displaying "Build" as an editable environment variable service in the UI, even though no build step executed. This configuration has been corrected so the variable service list now accurately reflects the pipeline's actual configuration. (CMGR-78120)

* Pipeline execution status not updating in the UI. In certain cases, the Cloud Manager UI did not reflect the current status of a running pipeline execution, showing outdated information to the user. Pipeline execution status now updates correctly and consistently in the UI. (CMGR-77642)

* EDS Sites showed a generic error when adding a collaborator failed. When adding a collaborator to an EDS site failed, the Cloud Manager UI displayed a generic error message instead of the specific failure reason. The UI now surfaces the actual error detail, helping users self-diagnose collaborator issues. (CMGR-75810)

<!-- There are no significant bug fixes in the July 2026 Cloud Manager release. -->

<!-- ## Known issues {#known-issues} -->

