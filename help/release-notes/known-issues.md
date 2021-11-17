---
title: Known Issues
description: Release notes specific to the Known Issues with Adobe Experience Manager as a Cloud Service
exl-id: 897b944a-d320-4d21-91f4-2cd3da6179b1
---
# Known issues {#known-issues}

This article lists the known issues of Adobe Experience Manager as a Cloud Service offering. The list is revised and updated with each continuous release of Experience Manager.

[Contact support](https://helpx.adobe.com/support/experience-manager.html) for more information about the known issues.

<!-- 
## Platform {#platform}

## Sites {#sites}
-->

## Assets {#assets}

<!-- Jira label: assets-cloud-known-issues -->

Some known issues are:

* **Metadata Schema**: Asset rating widget used to cause JSP compilation error. It was removed from the metadata schema. <!-- CQ-4282865, CQ-4284633 -->

### Upcoming Assets capabilities {#upcoming-assets-capabilities}

A few capabilities of Adobe Experience Manager Assets that depend on foundation capabilities, which are not yet available in the Experience Manager as a Cloud Service deployment architecture, are expected to be enabled at a later stage:

* Capabilities not enabled at this stage due to dependency on Commerce Integration Framework APIs:
  * Photoshoot workflow models.
  * Product information tab in the asset properties user interface is not populated.
* Capabilities not enabled at this stage due to dependency on InDesign Server integration:
  * Asset Templates and Asset Catalogs.
  * Multi-page preview of Adobe InDesign files.

>[!MORELIKETHIS]
>
>* [Major changes in AEM](aem-cloud-changes.md)
>* [Deprecated and removed features](deprecated-removed-features.md)
>* [Release notes](home.md)
