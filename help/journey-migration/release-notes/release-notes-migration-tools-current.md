---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.4.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.4.0
feature: Release Information
exl-id: 4941736b-82cd-4050-b3e9-aef250d5c4c7
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.4.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2022.4.0.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.28 is April 22, 2022.

### What's New {#what-is-new-bpa}

* Ability to detect and report on usage of unsupported Asset Manager APIs. There are four APIs that are no longer supported in AEM as a Cloud Service. Customers should ensure that they are no longer using these APIs and should be using the new method of asset upload.

* Ability to detect usage of Content Fragment templates. Content Fragment templates are no longer supported for new content fragment creation on AEM as a Cloud Service. Customers will need to create content fragment models to replace content fragment templates.

* Ability to detect assets with more than 100 descendants under the metadate node of the asset in the repository. It is recommended to remove metadata nodes that are not needed to improve the performance when loading folders consisting of such assets.

* Ability to detect and report on type of Data Store used.

* Pattern updated for AEM Form Portal.

### Bug Fixes {#bug-fixes-bpa}

* BPA was reporting findings for core components instead of reporting only on customer components. This has been fixed.
