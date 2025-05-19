---
title: Configure Your Content Source
description: Learn how to configure the content source for your Edge Delivery site using either fstab.yaml in Helix 4 or the Edge Delivery Services UI (or Configuration Service API) in Helix 5.
feature: Cloud Manager, Developing
role: Admin, Architect, Developer

---
# Configure your content source in one click for Edge Delivery Services {#config-content-source}

Adobe Experience Manager (AEM) Edge Delivery Services allows content delivery from multiple sources such as Google Drive, SharePoint, or AEM itself, using a fast, globally distributed edge network.

The content source configuration differs between Helix 4 and Helix 5 in the following way:

| Version | Content source configuration method |
| --- | --- |
| Helix 4 | YAML file (`fstab.yaml`) |
| Helix 5 | Configuration Service API (*no `fstab.yaml`*) |

This article provides comprehensive configuration steps, examples, and validation instructions for both versions.

**Before you start**

If you use [one click Edge Delivery in Cloud Manager](/help/implementing/cloud-manager/edge-delivery/create-edge-delivery-site.md##one-click-edge-delivery-site), your site is Helix 5 with a single repository. [Follow the Helix 5 instructions](#config-helix5) and use the provided Helix 4 YAML version of the instructions as a fallback.

**Determine your Helix version**

* Helix 4 - Your project includes an `fstab.yaml` file.
* Helix 5 - Your project *does not* use `fstab.yaml` and was set up through the [Edge Delivery Services UI](#config-helix5) or API.

Confirm through repository metadata or consult your administrator if you are still uncertain.

## Configure the content source for Helix 4

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

### Validation

* Using the AEM Sidekick Chrome Extension, click **Preview** > **Publish** > **Test the live site**.
* Validate URL: `https://main--<repo>--<org>.hlx.page/`

## Configure the content source for Helix 5 {#config-helix5}

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

### Validation

* Using the AEM Sidekick Chrome Extension, click **Preview** > **Publish** > **Test the live site**.
* Validate URL: `https://main--<repo>--<org>.aem.page/`
* (Optional) Inspect current configuration through the following `GET` API call:

    ```bash
    GET /api/{program}/{programId}/site/{siteId}
    ```
