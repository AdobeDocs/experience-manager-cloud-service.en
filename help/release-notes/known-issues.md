---
title: Known Issues
seo-title: Known Issues
description: Release notes specific to the Known Issues with Adobe Experience Manager as a Cloud Service
seo-description: Release notes specific to the Known Issues with Adobe Experience Manager as a Cloud Service
topic-tags: release-notes

---

# Known Issues {#known-issues}

This page keeps a list of known issues from Adobe Experience Manager as a Cloud Service that was released in December 2019. The list will be revised and updated with each continuous release of Experience Manager.

[Contact support](https://helpx.adobe.com/support/experience-manager.html) if you need more information about the known issues.

## Platform {#platform}

## Sites {#sites}

## Assets {#assets}

<!-- JIRA label: assets-cloud-known-issues -->

* **Versioning UI:** Version comparison slider is not visible and preview version button does not show the preview UI <!-- CQ-4284536 -->
* **Metadata Schema**: Asset Rating widget can cause JSP compilation error (workaround: remove the Asset Rating component from the metadata schema) <!-- CQ-4282865 -->

### Assets capabilities to be enabled at a later data

A few capabilities of Adobe Experience Manager Assets that depend on foundation capabilites, which are not yet available in the Experiecne Manager as a Cloud Service deployment architecture, are expected to be enabled at a later stage:

* Publishing to Brand Portal is not enabled at this stage
  * Customers can extend and deploy [Asset Share Commons](https://adobe-marketing-cloud.github.io/asset-share-commons/) implementation for asset distribution usecases
* Capabilties not enabled at this stage due to dependency on Commerce Integration Framework APIs:
  * Photoshoot workflow models
  * Product information tab in the asset properties user interface will be empty
* Capabiltiies not enabled at this stage due to dependency on InDesign Server integration:
  * Asset Templates & Asset Catalogs
  * Multi-page preview of InDesign Files
