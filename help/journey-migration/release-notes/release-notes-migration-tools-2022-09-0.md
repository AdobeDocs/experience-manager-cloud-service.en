---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.9.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.9.0
feature: Release Information
exl-id: 581370ba-e3e8-487e-af83-a1eacbda2763
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
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.9.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2022.9.0.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.34 is September 12, 2022. 

### What's New {#what-is-new-bpa}

* BPA can now detect and report on whether the customer has added a custom logger configuration. AEM as a Cloud Service does not support custom log files. All log files need to be piped to `error.log`
* BPA can now report on the different binary MIME types present in the customer's repository and counts associated with them.

### Bug Fixes {#bug-fixes-bpa}

* The BPA UI had rendering issues when displaying a large number of findings under a single pattern. This has been fixed.
* BPA was incorrectly reporting some findings as non-compatible changes with critical severity. This has been fixed.
