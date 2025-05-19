---
title: Release Notes for Cloud Manager 2025.5.0
description: Learn about the release of Cloud Manager 2025.5.0 in Adobe Experience Manager as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
---
# Release notes for Cloud Manager 2025.5.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

<!-- https://wiki.corp.adobe.com/display/DMSArchitecture/Cloud+Manager+2025.03.0+Release -->

Learn about the release of Cloud Manager 2025.5.0 in AEM (Adobe Experience Manager) as a Cloud Service.

See also the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2025.5.0 in AEM as a Cloud Service is Thursday, May 8, 2025. 

The next planned release is Thursday, June 5, 2025.
 
## What's new {#what-is-new}

### Configure the content source in one click for Edge Delivery Services

Adobe Experience Manager (AEM) Edge Delivery Services allows content delivery from multiple sources such as Google Drive, SharePoint, or AEM itself, using a fast, globally distributed edge network.

The content source configuration differs between Helix 4 and Helix 5 in the following way:

| Version | Content source configuration method |
| --- | --- |
| Helix 4 | YAML file (`fstab.yaml`) |
| Helix 5 | Configuration Service API (*no `fstab.yaml`*) |

This article provides comprehensive configuration steps, examples, and validation instructions for both versions.

**Before you start**

If you use [one click Edge Delivery in Cloud Manager](/help/implementing/cloud-manager/edge-delivery/create-edge-delivery-site.md##one-click-edge-delivery-site), your site is Helix 5 with a single repository. Follow the Helix 5 instructions and use the provided Helix 4 YAML version of the instructions as a fallback.

**Determine your Helix version**

* Helix 4 - Your project includes an `fstab.yaml` file.
* Helix 5 - Your project *does not* use `fstab.yaml` and was set up through the Edge Delivery Services UI or API.

Confirm through repository metadata or consult your administrator if you are still uncertain.

#### Configure the content source for Helix 4

In Helix 4, the fstab.yaml file defines the content source for your site. Located at the root of your GitHub repository, this file maps URL path prefixes (called mountpoints) to external content sources. A typical example looks like the following:

```yaml
mountpoints:
  /: https://drive.google.com/drive/folders/your-folder-id
```

This example is for illustration only. The actual URL should point to your content source, such as a Google Drive folder, SharePoint directory, or AEM path.

**To configure the content source for Helix 4:**

Steps vary by the source system that you use.

* **Google Drive**

    1. Create a Google Drive folder.
    1. Share the folder with `helix@adobe.com`.
    1. Get the shareable folder link.
    1. Update your `fstab.yaml` as shown in the following:

        ```yaml
        mountpoints: 
            /: https://drive.google.com/drive/folders/<folder-id>
        ```

    1. Commit and push changes to GitHub.

* **SharePoint**

    1. Create a SharePoint folder or document library.
    1. Share access with `helix@adobe.com`.
    1. Obtain the folder URL.
    1. Update your `fstab.yaml` as shown in the following:

        ```yaml
        mountpoints:
          /: https://<tenant>.sharepoint.com/sites/<site>/Shared%20Documents/<folder>
        ```

    1. Commit and push changes to GitHub.

* **AEM**

    1. Identify your AEM content path.
    1. Use the AEM content export URL as shown in the following:

        ```yaml
        mountpoints:
          /: https://author.<your-aem-instance>.com/bin/franklin.delivery/<org>/<repo>/main
        ```

    1. Commit and push changes to GitHub.

##### Validation

* Using the AEM Sidekick Chrome Extension, click **Preview** > **Publish** > **Test the live site**.
* Validate URL: `https://main--<repo>--<org>.hlx.page/`

#### Configure the content source for Helix 5

Helix 5 is repoless, does not use `fstab.yaml`, and supports multiple sites sharing the same directory. Configuration is managed through the Configuration Service API or the Edge Delivery Services UI. Configuration is site-level (not repository-level).

Conceptual differences are the following:

| Aspect | Helix 4 | Helix 5 |
| --- | --- | --- |
| Configuration | Done through `fstab.yaml` | Done through the API or UI instead of YAML. |
| Mountpoints | Defined in `fstab.yaml`. | Not required. The root is implicitly understood. |

**To configure the content source for Helix 5:**

1. Using the Configuration Service API, authenticate through an API key or access token.
1. Make the following `PUT` API call:

    ```bash {.line-numbering}
    PUT /api/{program}/{programId}/site/{siteId}
    Content-Type: application/json

    {
      "sitename": "my-site",
      "branchName": "main",
      "version": "v5",
      "repo": "my-content-repo-link"
    }
    ```

1. Validate response (expected: HTTP 200 OK).

##### Validation

* Using the AEM Sidekick Chrome Extension, click **Preview** > **Publish** > **Test the live site**.
* Validate URL: `https://main--<repo>--<org>.aem.page/`
* (Optional) Inspect current configuration through the following `GET` API call:

    ```bash
    GET /api/{program}/{programId}/site/{siteId}
    ```

<!--
* **AI-powered build summaries now available for internal use**

    Internal users can now use AI-powered build summaries to simplify build log analysis. The feature provides actionable recommendations and helps identify the root causes of build failures.

    ![Build Summary dialog box](/help/implementing/cloud-manager/release-notes/assets/build-summary.png)
-->


## Early adopter program {#early-adoption}

Participate in Cloud Manager's Early Adopter Program to get exclusive access to upcoming features before their general release.

The following early adopter opportunities are currently available:

### Add Edge Delivery Config Pipeline {#add-eds-pipeline}

Config Pipelines are now supported for sites built with Edge Delivery Services, expanding this capability beyond just Cloud Service environments. You can use **Config Pipelines** to manage settings such as traffic filtering rules and Web Application Firewall (WAF) configurations, where applicable. See [Supported Configurations](/help/operations/config-pipeline.md#configurations).

![Add Edge Delivery pipeline in Add Pipeline drop-down list](/help/implementing/cloud-manager/release-notes/assets/add-edge-delivery-pipeline.png)

If you are interested in testing this new feature and sharing your feedback, send an email to [grp-aemeds-config-pipeline-adopter@adobe.com](mailto:grp-aemeds-config-pipeline-adopter@adobe.com) from your email address associated with your Adobe ID.

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


<!--
## Bug fixes

* Issue

* Issue

* Issue
-->

<!-- ## Known issues {#known-issues} -->

