---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.9.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.9.0
feature: Release Information
exl-id: 2f787321-f156-480d-bbe8-1a6d04f110c5
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
