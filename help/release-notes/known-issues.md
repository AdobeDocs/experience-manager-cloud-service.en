---
title: Known Issues
seo-title: Known Issues
description: Release notes specific to the Known Issues with Adobe Experience Manager as a Cloud Service
seo-description: Release notes specific to the Known Issues with Adobe Experience Manager as a Cloud Service
topic-tags: release-notes

---

# Known issues {#known-issues}

This article lists the known issues of Adobe Experience Manager as a Cloud Service offering. The list is revised and updated with each continuous release of Experience Manager.

[Contact support](https://helpx.adobe.com/support/experience-manager.html) for more information about the known issues.

## Platform {#platform}

## Sites {#sites}

## Assets {#assets}

<!-- Jira label: assets-cloud-known-issues -->

* **Versioning UI:** Version comparison slider is not visible and preview version button does not display the preview interface. <!-- CQ-4284536 -->
* **Metadata Schema**: Asset rating widget can cause JSP compilation error. A workaround is to remove the asset rating component from the metadata schema. <!-- CQ-4282865 -->

### Upcoming Assets capabilities {#upcoming-assets-capabilities}

A few capabilities of Adobe Experience Manager Assets that depend on foundation capabilities, which are not yet available in the Experience Manager as a Cloud Service deployment architecture, are expected to be enabled at a later stage:

* Publishing to Brand Portal is not enabled at this stage. You can extend and deploy [Asset Share Commons](https://adobe-marketing-cloud.github.io/asset-share-commons/) implementation for asset distribution use-cases.
* Capabilities not enabled at this stage due to dependency on Commerce Integration Framework APIs:
  * Photoshoot workflow models.
  * Product information tab in the asset properties user interface is not populated.
* Capabilities not enabled at this stage due to dependency on InDesign Server integration:
  * Asset Templates and Asset Catalogs.
  * Multi-page preview of InDesign files.

>[!MORELIKETHIS]
>
>* [Major changes in AEM](aem-cloud-changes.md)
>* [Deprecated and removed features](deprecated-removed-features.md)
>* [Release notes](release-notes.md)
