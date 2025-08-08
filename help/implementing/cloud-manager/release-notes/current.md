---
title: Release Notes for Cloud Manager 2025.8.0
description: Learn about the release of Cloud Manager 2025.8.0 in Adobe Experience Manager as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
---
# Release notes for Cloud Manager 2025.8.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

<!-- https://wiki.corp.adobe.com/display/DMSArchitecture/%5BKT%5D+Cloud+Manager+2025.08.0+Release -->

Learn about the release of Cloud Manager 2025.8.0 in AEM (Adobe Experience Manager) as a Cloud Service.

See also the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2025.8.0 in AEM as a Cloud Service is Thursday, August 7, 2025. 

The next planned release is Thursday, September 4, 2025.

## What's new {#what-is-new}

* **Edge Delivery Services license can be included in a HIPAA program in a self-service manner** 

    Organizations with healthcare or sensitive data requirements can now use Edge Delivery Services in a self-service manner, enabling HIPAA compliance to meet strict regulatory standards. <!-- CMGR-70016 -->

* **BYOG is now available for Edge Delivery Services**

    Cloud Manager now lets you configure external Git repositories, enabling flexible code-management workflows. <!--(CMGR‑69010, CMGR‑70988) --> It also lets you pull code from a chosen branch directly in the Cloud Manager UI, reducing manual repository tasks. See [Configure Edge Delivery site to use an external Git repository](/help/implementing/cloud-manager/edge-delivery/config-edge-delivery-site-with-byog.md) <!-- (CMGR‑68085)(CMGR-69015) --> <!-- KT: https://wiki.corp.adobe.com/display/DMSArchitecture/%5B2025%5D+Cloud+Manager+-+Bring+Your+Own+Git+with+EDS -->

* **Automated provisioning for the new Forms Add‑on**

    Sites-only customers often need a lightweight, low-cost way to build marketing forms. The new AEM Forms Sites Add-On meets that need by adding limited Forms features to a Sites program. It also creates a clear upgrade path to the full AEM Forms offering. <!-- (CMGR-64301) --> <!-- KT: CMGR Provisioning Support for AEM Forms Sites Add-On SKU https://wiki.corp.adobe.com/pages/viewpage.action?pageId=3578379797 -->

    The add-on:
    * Attaches to a Sites program and deploys alongside it&mdash;no separate Forms program or entitlement.
    * Targets simple marketing-form use cases.
    * Appears in the **Solutions & Add-ons** list during Production Program creation or Production Program edit, only when the IMS org holds available Forms add-on licenses.

        ![Forms add-ons](/help/implementing/cloud-manager/release-notes/assets/forms-add-on.png) *The Forms add-on can be added in the Program only if Forms add-on licenses are available in your IMS org.*

        ![Forms add-on in Solutions & Add-Ons when creating a production program](/help/implementing/cloud-manager/release-notes/assets/forms-add-on-creating-production-program.png) *During Program Creation, you can select the Forms add-on within the Sites solution.* 

        ![Forms add-on when editing a production program](/help/implementing/cloud-manager/release-notes/assets/forms-add-on-editing-production-program.png) *In **Edit Program**, select the Forms add-on for the Sites program, then run the pipeline to activate it in the environments.*

        For more information, see [Create a production program](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md).

## Beta programs {#private-beta-program}

Participate in Cloud Manager's beta programs to get exclusive access to upcoming features before their general release.

The following opportunities are currently available:

### One-click rollback for pipeline deployments {#one-click-rollback} 

Quickly revert to a previous deployment if the latest customer source code is not working as expected—no need to rerun the full pipeline or manually revert commits.<!--https://jira.corp.adobe.com/browse/CMGR-69556 -->

![Restore customer source code from the Environments card](/help/implementing/cloud-manager/release-notes/assets/restore-previous-code-deployed.png) *Environments card above showing the **Restore** > **Previous code deployed** option for a selected environment.* 

![Restore previous code deployed dialog box](/help/implementing/cloud-manager/release-notes/assets/restore-previous-code-deployed-dialogbox.png) 
*In the **Restore previous code deployed** dialog box, review the currently deployed version and the version you want to restore, then click **Confirm***.

![Restoring activation](/help/implementing/cloud-manager/release-notes/assets/restoring-previous-code-deployed-restoring.png) 
*Cloud Manager rolls the environment back to the earlier build, keeps content and configuration intact, and marks the environment **Restoring** until deployment completes.*

![Source code version in use](/help/implementing/cloud-manager/release-notes/assets/environments-view-details-sourcecodeversion.png) *The Environment details view, as seen above, now also shows the active source-code version in use.*

If you are interested in testing this new feature and sharing your feedback, send an email to [restorecode@adobe.com](mailto:restorecode@adobe.com) from your email address associated with your Adobe ID.

See [Restore the Previous Code Deployed in AEM as a Cloud Service](/help/operations/restore-previous-code-deployed.md).

See also [Content Restore in AEM as a Cloud Service](/help/operations/restore.md).

### Specialized Testing Environment {#specialized-test-environment}

Cloud Manager now supports the addition of a new environment type called **Specialized Testing Environment**. The environment is designed to help teams validate features under near-production conditions before going live. This environment type is distinct from *Production + Stage*, *Development*, or *Rapid Development* environments and offers a focused space for running advanced validation scenarios.

**Recent enhancements**

* You can now configure a Specialized Testing Environment on a non-production pipeline through a simpler, more intuitive workflow. The streamlined setup speeds completion and reduces configuration errors.
* **Copy Content** is now supported in Specialized Testing Environments. You can now run **Copy Content** safely in isolated testing environments that mirror Production. <!-- (CMGR‑68900) -->

See [Add a Specialized Testing Environment](/help/implementing/cloud-manager/specialized-test-environment.md).

![Add environment dialog box with Specialized Testing Environment radio button selected](/help/implementing/cloud-manager/release-notes/assets/specialized-test-environment.png)

If you are interested in testing this new feature and sharing your feedback, send an email to [grp-earlyadopter_cs_advtestenvironment@adobe.com](mailto:grp-earlyadopter_cs_advtestenvironment@adobe.com) from your email address associated with your Adobe ID.


### Bring Your Own Git (BYOG) {#gitlab-bitbucket-azure-vsts}

<!-- BOTH CS & AMS -->

Customers can now onboard their Azure DevOps Git repositories into Cloud Manager, with support for both modern Azure DevOps and legacy VSTS (Visual Studio Team Services) repositories.

* For Edge Delivery Services users, the onboarded repository can be used to sync and deploy site code.
* For AEM as a Cloud Service and Adobe Managed Services (AMS) users, the repository can be linked to both full-stack and frontend pipelines.

Support for additional pipeline types and pull request validation through code quality pipelines is coming soon.

See [Add external repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/external-repositories.md).

![Add Repository dialog box](/help/implementing/cloud-manager/release-notes/assets/azure-repo.png)

<!-- If you are interested in testing this new feature and sharing your feedback, send an email to [Grp-CloudManager_BYOG@adobe.com](mailto:grp-cloudmanager_byog@adobe.com) from your email address associated with your Adobe ID. Be sure to include which Git platform you want to use and whether you are on a private/public or enterprise repository structure. -->

**Frequently asked questions about BYOG**

| Question | Answer |
|---|---|
| *How can a project switch back to the Adobe-managed Git repository if needed?* | Switching back is straightforward. [Update the pipelines](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md) to point to the Adobe repository and remove the external repository if it is no longer required. |
| *Is it possible to configure different repositories for different environments (for example, non-production versus production) to allow testing in non-production first?* | Yes, different repositories can be configured for separate environments. For example, the dev or code quality pipeline can point to an external repository while the production pipeline remains connected to the Adobe repository. Make sure that the sync job between the two repositories remains active during this configuration. |
| *Do existing settings like `IP Allow` lists continue to work?* | Yes, existing `IP Allow` lists continue to work as usual. However, if the external Git repository is protected by a firewall, the necessary [Adobe IP addresses must be added to the allow list](/help/implementing/cloud-manager/ip-allow-lists/introduction.md). |
| *Do all GitLab repository URLs work? The repository URL in use follows the format `https://gitlab_dedicated_url.com/path/repo-name.git`, which differs from the example in the documentation.* | Yes, any GitLab repository that supports API V3 or V4 is supported, including self-hosted GitLab URLs like the one described in [Add external repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/external-repositories.md) (`https://git-vendor-name.com/org-name/repo-name.git`). |


#### Manage Access Tokens{#manage-access-tokens}

Use **Manage Access Tokens** in Cloud Manager to view, rename, and delete access tokens associated with external BYOG repositories, such as GitHub Enterprise, GitLab, Bitbucket, and Azure DevOps.

See [Manage Access Tokens](/help/implementing/cloud-manager/managing-code/manage-access-tokens.md).

<!-- If you are interested in testing this new feature and sharing your feedback, send an email to [Grp-CloudManager_BYOG@adobe.com](mailto:grp-cloudmanager_byog@adobe.com) from your email address associated with your Adobe ID. -->


### Add Edge Delivery Config Pipeline {#add-eds-pipeline}

Config Pipelines are now supported for sites built with Edge Delivery Services, expanding this capability beyond just Cloud Service environments. You can use **Config Pipelines** to manage settings such as traffic filtering rules and Web Application Firewall (WAF) configurations, where applicable. See [Supported Configurations](/help/operations/config-pipeline.md#configurations).

**Recent enhancement**

* Edge Delivery Services pipelines now display **Configuration** in the **Deployed Code** column, enabling instant identification of configuration-only deployments. <!-- CMGR‑69681 -->
* Cloud Manager shows **Add Edge Delivery Pipeline** once a program contains at least one Edge Delivery Services site and one mapped domain. Otherwise, the option appears disabled, and a tooltip explains missing requirements. <!-- CMGR‑69680 -->
* The **Edge Delivery** tab shows a new **Edge Delivery pipelines** widget that lists each pipeline's Name, Status, Repository, and Branch. <!-- (CMGR-69052) -->

    ![Edge Delivery pipeline widget showing pipeline name, status, repository, and branch](/help/implementing/cloud-manager/release-notes/assets/edge-delivery-pipeline-widget.png)

* The **Filters** panel adds a **Delivery Type** section; includes **Edge delivery** and **Publish delivery** checkboxes. <!-- (CMGR-69682) -->

    ![Filter panel showing new Delivery type of Edge delivery and Publish delivery](/help/implementing/cloud-manager/release-notes/assets/filter-delivery-type.png)

![Add Edge Delivery pipeline in Add Pipeline drop-down list](/help/implementing/cloud-manager/release-notes/assets/edge-delivery-pipeline-add.png) *Adding an Edge Delivery pipeline from the **Program Overview** page, **Pipelines** card.*

![Add Edge Delivery pipeline dialog box](/help/implementing/cloud-manager/release-notes/assets/edge-delivery-pipeline-add-dialogbox.png) *Add Edge Delivery pipeline dialog box.*

See [Add Edge Delivery Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-edge-delivery-pipeline.md)

<!-- If you are interested in testing this new feature and sharing your feedback, send an email to [grp-aemeds-config-pipeline-adopter@adobe.com](mailto:grp-aemeds-config-pipeline-adopter@adobe.com) from your email address associated with your Adobe ID. -->


## Bug fixes

* Pipelines now deliver variables only to the active Edge Delivery Services domain configuration, skipping any configuration removed during pipeline recreation. <!-- (CMGR‑70039) -->
* Pipeline execution now starts reliably; fixed an issue where some pipelines failed to start due to internal resource handling errors. <!-- (CMGR‑58167) -->
* Content Copy validates Cloud Manager permissions and blocks starts by users lacking Deployment Manager or Administrator rights. <!-- (CMGR‑62097) -->


<!-- ## Known issues {#known-issues} -->

