---
title: Release Notes for Cloud Manager 2025.7.0
description: Learn about the release of Cloud Manager 2025.7.0 in Adobe Experience Manager as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
---
# Release notes for Cloud Manager 2025.7.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

<!-- https://wiki.corp.adobe.com/display/DMSArchitecture/Cloud+Manager+2025.03.0+Release -->

Learn about the release of Cloud Manager 2025.7.0 in AEM (Adobe Experience Manager) as a Cloud Service.

See also the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2025.7.0 in AEM as a Cloud Service is Thursday, July 10, 2025. 

The next planned release is Thursday, August 7, 2025.
 
## What's new {#what-is-new}

* **Cloud Manager adds ECDSA (Elliptic Curve Digital Signature Algorithm) SSL certificate support**

    Cloud Manager now supports ECDSA certificates. The feature delivers strong security with smaller key sizes, enabling customers to apply lightweight modern cryptography in their CDN configurations. <!-- https://jira.corp.adobe.com/browse/CMGR-62399 -->

* **Download Site license-usage report**

    On the **Sites usage details** page (In Cloud Manager, click **License**. In the Solutions table, in the **Sites** row, click **View usage details**), customers can now click **Download report** to export its data as a CSV file. This download simplifies analyzing and sharing usage trends. <!-- https://jira.corp.adobe.com/browse/CMGR-42274 -->

    ![Sites usage details page](/help/implementing/cloud-manager/release-notes/assets/sites-license-usage-page.png)

## Early adopter programs {#private-beta-program}

Participate in Cloud Manager's alpha and beta programs to get exclusive early access to upcoming features before their general release.

The following opportunities are currently available:


### One-click rollback for pipeline deployments {#one-click-rollback} 

Quickly revert to a previous deployment if the latest code is not working as expected—no need to rerun the full pipeline or manually revert commits.<!--https://jira.corp.adobe.com/browse/CMGR-69556 -->

<!-- Add link to topic within the affected article ==>


### Specialized Testing Environment {#specialized-test-environment}

Cloud Manager now supports the addition of a new environment type called **Specialized Testing Environment**. The environment is designed to help teams validate features under near-production conditions before going live. This environment type is distinct from *Production + Stage*, *Development*, or *Rapid Development* environments and offers a focused space for running advanced validation scenarios.

Recent enhancement: You can now configure specialized testing environments on a non-production pipeline through a simpler, more intuitive workflow. The streamlined setup speeds completion and reduces configuration errors.

See [Add a Specialized Testing Environment](/help/implementing/cloud-manager/specialized-test-environment.md).

![Add environment dialog box with Specialized Testing Environment radio button selected](/help/implementing/cloud-manager/release-notes/assets/specialized-test-environment.png)

If you are interested in testing this new feature and sharing your feedback, send an email to [grp-earlyadopter_cs_advtestenvironment@adobe.com](mailto:grp-earlyadopter_cs_advtestenvironment@adobe.com) from your email address associated with your Adobe ID.


### Bring Your Own Git (BYOG) - now with support for Azure DevOps {#gitlab-bitbucket-azure-vsts}

<!-- BOTH CS & AMS -->

Customers can now onboard their Azure DevOps Git repositories into Cloud Manager, with support for both modern Azure DevOps and legacy VSTS (Visual Studio Team Services) repositories.

* For Edge Delivery Services users, the onboarded repository can be used to sync and deploy site code.
* For AEM as a Cloud Service and Adobe Managed Services (AMS) users, the repository can be linked to both full-stack and frontend pipelines.

Support for additional pipeline types and pull request validation through code quality pipelines is coming soon.

See [Add external repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/external-repositories.md).

![Add Repository dialog box](/help/implementing/cloud-manager/release-notes/assets/azure-repo.png)

If you are interested in testing this new feature and sharing your feedback, send an email to [Grp-CloudManager_BYOG@adobe.com](mailto:grp-cloudmanager_byog@adobe.com) from your email address associated with your Adobe ID. Be sure to include which Git platform you want to use and whether you are on a private/public or enterprise repository structure. 


**Frequently asked questions about BYOG**

| Question | Answer |
|---|---|
| *How can a project switch back to the Adobe-managed Git repository if needed?* | Switching back is straightforward. [Update the pipelines](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md) to point to the Adobe repository and remove the external repository if it is no longer required. |
| *Is it possible to configure different repositories for different environments (for example, non-production versus production) to allow testing in non-production first?* | Yes, different repositories can be configured for separate environments. For example, the dev or code quality pipeline can point to an external repository while the production pipeline remains connected to the Adobe repository. Make sure that the sync job between the two repositories remains active during this configuration. |
| *Do existing settings like IP allow lists continue to work?* | Yes, existing IP allow lists continue to work as usual. However, if the external Git repository is protected by a firewall, the necessary [Adobe IP addresses must be added to the allow list](/help/implementing/cloud-manager/ip-allow-lists/introduction.md). |
| *Do all GitLab repository URLs work? The repository URL in use follows the format `https://gitlab_dedicated_url.com/path/repo-name.git`, which differs from the example in the documentation.* | Yes, any GitLab repository that supports API V3 or V4 is supported, including self-hosted GitLab URLs like the one described in [Add external repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/external-repositories.md) (`https://git-vendor-name.com/org-name/repo-name.git`). |


#### Manage Access Tokens{#manage-access-tokens}

Use **Manage Access Tokens** in Cloud Manager to view, rename, and delete access tokens associated with external BYOG repositories, such as GitHub Enterprise, GitLab, Bitbucket, and Azure DevOps.

See [Manage Access Tokens](/help/implementing/cloud-manager/managing-code/manage-access-tokens.md).

If you are interested in testing this new feature and sharing your feedback, send an email to [Grp-CloudManager_BYOG@adobe.com](mailto:grp-cloudmanager_byog@adobe.com) from your email address associated with your Adobe ID.


### Add Edge Delivery Config Pipeline {#add-eds-pipeline}

Config Pipelines are now supported for sites built with Edge Delivery Services, expanding this capability beyond just Cloud Service environments. You can use **Config Pipelines** to manage settings such as traffic filtering rules and Web Application Firewall (WAF) configurations, where applicable. See [Supported Configurations](/help/operations/config-pipeline.md#configurations).

![Add Edge Delivery pipeline in Add Pipeline drop-down list](/help/implementing/cloud-manager/release-notes/assets/edge-delivery-pipeline-add.png) *Adding an Edge Delivery pipeline from the **Program Overview** page, **Pipelines** card.*

![Add Edge Delivery pipeline dialog box](/help/implementing/cloud-manager/release-notes/assets/edge-delivery-pipeline-add-dialogbox.png) *Add Edge Delivery pipeline dialog box.*

If you are interested in testing this new feature and sharing your feedback, send an email to [grp-aemeds-config-pipeline-adopter@adobe.com](mailto:grp-aemeds-config-pipeline-adopter@adobe.com) from your email address associated with your Adobe ID.


## Bug fixes

* Cloud Manager now updates the release version for all pipelines during environment upgrades, ensuring consistent version tracking across all pipeline types. <!-- CMGR-69043 -->
* The UI now displays status and detailed error messages when a Domain Validation (DV) SSL certificate fails, helping to understand and resolve certificate issues. <!-- CMGR-68872 -->
* While editing a domain mapping, the UI now prevents selecting SSL certificates that do not match the chosen domain, reducing misconfigurations and improving reliability during setup. <!-- CMGR-64307 -->
* In some situations, the certificates were not properly deleted, maintaining the domain is still active. <!-- CMGR-69867 -->
* Fixed an issue that could block upgrades from *Adobe Assets* to *Adobe Assets Ultimate* in certain cases. Transitions are now smoother and more reliable. <!-- CMGR-69506 -->
* Resolved an issue where key region fields are automatically set when creating multi-region environments to support downstream services and deployments smoothly. <!-- CMGR-69471 -->
* Resolved an issue where some configuration pipelines did not stop properly after execution. Now, pipelines are completed successfully and close as expected, improving reliability. <!-- CMGR-69344 -->


<!-- ## Known issues {#known-issues} -->

