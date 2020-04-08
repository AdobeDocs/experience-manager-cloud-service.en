---
title: Release Notes for Release 2020.4.0
description: Release Notes for Release 2020.4.0
---

# Release Notes for AEM as a Cloud Service 2020.4.0 {#release-notes}

The following section outlines the general Release Notes for Experience Manager as a Cloud Service 2020.4.0.

## Assets {#assets}

Follow this section to learn about what is new and the updates for Experience Manager Assets and Dynamic Media in AEM as a Cloud Service Release 2020.4.0.

### What's New {#assets-what-is-new}

* [Brand Portal](https://docs.adobe.com/content/help/en/experience-manager-brand-portal/using/home.html) is available for AEM as a Cloud Service Assets, supporting asset distribution use cases. Brand Portal aids organizations to meet their marketing needs by securely distributing approved brand and product assets to external agencies, partners, internal teams, and resellers for download.
   * Brand Portal configuration is done through Adobe I/O console
   * Asset sourcing in Brand Portal is not yet supported with AEM as a Cloud Service
* The new release of [Adobe Asset Link](https://helpx.adobe.com/enterprise/using/adobe-asset-link.html) 2.0 is supported with AEM as a Cloud Service. Adobe Asset Link streamlines collaboration between creatives and marketers in the content creation process by connecting AEM Assets with Creative Cloud desktop apps Photoshop, Illustrator, and InDesign via in-app Asset Link panel.
   * AEM as a Cloud Service is preconfigured for Adobe Asset Link, which results in [simplified configuration](https://helpx.adobe.com/enterprise/using/configure-aem-assets-for-asset-link.html).
   * Asset Link now supports an [AEM environment switcher](https://helpx.adobe.com/enterprise/using/manage-assets-using-adobe-asset-link.html#UseAdobeAssetLink), allowing creative users to connect to different AEM enviroments more easily (e.g., in case of agency designers working with multiple clients with AEM Assetes)
* Auto-start for [post-processing worfklows](../../assets/manage/asset-microservices-configure-and-use.md#post-processing-workflows) can be configured in Folder Properties UI for specific folder hierarchies.
   * Folder Properties UI has been simplified, with new Asset Processing tab containg Metadata Profile, Processing Profile, and the new Auto-Start Workflow configuration
* Asset reprocessing dialog allows for selecting a specific processing profile and decide to reprocess in sub-folders
* Dynamic Media: Added Selective Publish configuration, which means that assets are auto published for secure preview only and can be explicitly published to AEM without publishing to DMS7 for delivery in the public domain.

### Bug Fixes  {#assets-bug-fixes}

* Fixes in asset processing
* Fixes in Dynamic Media configuration and publishing assets to Dynamic Media delivery service
