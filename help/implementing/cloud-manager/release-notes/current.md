---
title: Release Notes for Cloud Manager 2025.6.0
description: Learn about the release of Cloud Manager 2025.6.0 in Adobe Experience Manager as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
---
# Release notes for Cloud Manager 2025.6.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

<!-- https://wiki.corp.adobe.com/display/DMSArchitecture/Cloud+Manager+2025.03.0+Release -->

Learn about the release of Cloud Manager 2025.6.0 in AEM (Adobe Experience Manager) as a Cloud Service.

See also the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2025.6.0 in AEM as a Cloud Service is Thursday, June 5, 2025. 

The next planned release is Thursday, July 10, 2025.
 
## What's new {#what-is-new}

* **(UI) License dashboard now includes Edge Delivery Services license**

    Edge Delivery Services license usage is now displayed in the License dashboard, providing you with clearer visibility into your entitlements. <!-- CMGR-67686 -->

    ![License Dashboard](/help/implementing/cloud-manager/assets/license-dashboard.png)

    See [Licence dashboard](/help/implementing/cloud-manager/license-dashboard.md).

* **(UI) Edge Delivery site configuration updated**

    Simplified the flow for adding an Edge Delivery site by requesting the **Edge Delivery Origin** instead of the **Repository URL**, making onboarding and setup faster and more intuitive <!-- CMGR-67686 -->

    ![Add Edge Delivery site dialog box]()

    See [Add an Edge Delivery Site](/help/implementing/cloud-manager/edge-delivery/add-edge-delivery-site.md).

* **


## Early adopter program {#early-adoption}

Participate in Cloud Manager's Early Adopter Program to get exclusive access to upcoming features before their general release.

The following early adopter opportunities are currently available:

### Manage Access Tokens{#manage-access-tokens}

Use the **Manage Access Tokens** feature in Cloud Manager to view, rename, and delete access tokens associated with external Bring Your Own Git repositories, such as GitHub Enterprise, GitLab, Bitbucket, and Azure DevOps.

See [Manage Access Tokens](/help/implementing/cloud-manager/managing-code/manage-access-tokens.md)

If you are interested in testing this new feature and sharing your feedback, send an email to from your email address associated with your Adobe ID.

### Specialized Testing Environment {#specialized-test-environment}

Cloud Manager now supports the addition of a new environment type called **Specialized Testing Environment**. The environment is designed to help teams validate features under near-production conditions before going live. This environment type is distinct from *Production + Stage*, *Development*, or *Rapid Development* environments and offers a focused space for running advanced validation scenarios. 

See [Adding a Specialized Testing Environment](/help/implementing/cloud-manager/specialized-test-environment.md).

![Add environment dialog box with Specialized Testing Environment radio button selected](/help/implementing/cloud-manager/release-notes/assets/specialized-test-environment.png)

If you are interested in testing this new feature and sharing your feedback, send an email to [grp-earlyadopter_cs_advtestenvironment@adobe.com](mailto:grp-earlyadopter_cs_advtestenvironment@adobe.com) from your email address associated with your Adobe ID.


### Bring Your Own Git - now with support for Azure DevOps {#gitlab-bitbucket-azure-vsts}

<!-- BOTH CS & AMS -->

Customers can now onboard their Azure DevOps Git repositories into Cloud Manager, with support for both modern Azure DevOps and legacy VSTS (Visual Studio Team Services) repositories.

* For Edge Delivery Services users, the onboarded repository can be used to sync and deploy site code.
* For AEM as a Cloud Service and Adobe Managed Services (AMS) users, the repository can be linked to both full-stack and frontend pipelines.

Support for additional pipeline types and pull request validation through code quality pipelines is coming soon.

See [Add external repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/external-repositories.md).

![Add Repository dialog box](/help/implementing/cloud-manager/release-notes/assets/azure-repo.png)

If you are interested in testing this new feature and sharing your feedback, send an email to [Grp-CloudManager_BYOG@adobe.com](mailto:grp-cloudmanager_byog@adobe.com) from your email address associated with your Adobe ID. Be sure to include which Git platform you want to use and whether you are on a private/public or enterprise repository structure. 

#### Frequently asked questions about Bring Your Own Git

| Question | Answer |
|---|---|
| *How can a project switch back to the Adobe-managed Git repository if needed?* | Switching back is straightforward. [Update the pipelines](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md) to point to the Adobe repository and remove the external repository if it is no longer required. |
| *Is it possible to configure different repositories for different environments (for example, non-production versus production) to allow testing in non-production first?* | Yes, different repositories can be configured for separate environments. For example, the dev or code quality pipeline can point to an external repository while the production pipeline remains connected to the Adobe repository. Make sure that the sync job between the two repositories remains active during this configuration. |
| *Do existing settings like IP allow lists continue to work?* | Yes, existing IP allow lists continue to work as usual. However, if the external Git repository is protected by a firewall, the necessary [Adobe IP addresses must be added to the allow list](/help/implementing/cloud-manager/ip-allow-lists/introduction.md). |
| *Do all GitLab repository URLs work? The repository URL in use follows the format `https://gitlab_dedicated_url.com/path/repo-name.git`, which differs from the example in the documentation.* | Yes, any GitLab repository that supports API V3 or V4 is supported, including self-hosted GitLab URLs like the one described in [Add external repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/external-repositories.md) (`https://git-vendor-name.com/org-name/repo-name.git`). |

### Add Edge Delivery Config Pipeline {#add-eds-pipeline}

Config Pipelines are now supported for sites built with Edge Delivery Services, expanding this capability beyond just Cloud Service environments. You can use **Config Pipelines** to manage settings such as traffic filtering rules and Web Application Firewall (WAF) configurations, where applicable. See [Supported Configurations](/help/operations/config-pipeline.md#configurations).

![Add Edge Delivery pipeline in Add Pipeline drop-down list](/help/implementing/cloud-manager/release-notes/assets/add-edge-delivery-pipeline.png)

If you are interested in testing this new feature and sharing your feedback, send an email to [grp-aemeds-config-pipeline-adopter@adobe.com](mailto:grp-aemeds-config-pipeline-adopter@adobe.com) from your email address associated with your Adobe ID.




<!--
## Bug fixes

* Issue

* Issue

* Issue
-->

<!-- ## Known issues {#known-issues} -->

