---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.03.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.03.0
feature: Release Information
exl-id: 2f787321-f156-480d-bbe8-1a6d04f110c5
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.03.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2022.03.0.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.40 is March 03, 2023. 

### What's New {#what-is-new-bpa}

* BPA can now detect and report on conflicting nodes - nodes with the same `jcr:uuid`. Such findings are flagged as critical since it can lead to content ingestion failures when moving content to AEM as a Cloud Service.  
* BPA can now detect and report on the usage of Event Listeners. It is recommended to refactor this type of event handing mechanism to sling jobs when moving to AEM as a Cloud Service. 

### Bug Fixes {#bug-fixes-bpa}

* BPA was reporting false positives on `grouprendercondition`. This has been fixed.