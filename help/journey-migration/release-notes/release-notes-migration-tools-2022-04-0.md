---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.4.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.4.0
feature: Release Information
exl-id: 4941736b-82cd-4050-b3e9-aef250d5c4c7
role: Admin
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: ed762d86-a04b-452b-a08f-86359bb8ff27
    internal-label: Configuration and operations
subfeature_v2:
  - id: c21ccc2b-e0c8-4853-bf41-f12259ed93f8
    internal-label: Release information
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.4.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2022.4.0.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.28 is April 22, 2022.

### What's New {#what-is-new-bpa}

* Ability to detect and report on usage of unsupported Asset Manager APIs. There are four APIs that are no longer supported in AEM as a Cloud Service. Customers should ensure that they are no longer using these APIs and should be using the new method of asset upload.

* Ability to detect usage of Content Fragment templates. Content Fragment templates are no longer supported for new content fragment creation on AEM as a Cloud Service. Customers need to create content fragment models to replace content fragment templates.

* Ability to detect assets with more than 100 descendants under the metadate node of the asset in the repository. It is recommended to remove metadata nodes that are not needed to improve the performance when loading folders consisting of such assets.

* Ability to detect and report on type of Data Store used.

* Pattern updated for AEM Form Portal.

### Bug Fixes {#bug-fixes-bpa}

* BPA was reporting findings for core components instead of reporting only on customer components. This has been fixed.
