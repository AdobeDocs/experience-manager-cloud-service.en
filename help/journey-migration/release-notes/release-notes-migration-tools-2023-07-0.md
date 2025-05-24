---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.07.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.07.0
feature: Release Information
exl-id: 2f787321-f156-480d-bbe8-1a6d04f110c5
role: Admin
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.07.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2023.07.0.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.42 is July 06, 2023.

### What's New {#what-is-new-bpa}

* Multiple best practices patterns were added to this release of the Best Practices Analyzer. These include:
  * Identifying minimum maintenance task configuration
  * Detecting long-running/heavy queries
  * Detecting high number of author workflows in running or stale state
  * Detecting OSGI Apache sling job configuration
  * Detecting custom Guava-caches

### Bug Fixes {#bug-fixes-bpa}

* BPA was improved to prevent out of memory report generation failures for reports with high number of findings.
* BPA was improved to detect escape characters in paths to prevent content ingestion failures when migration content to AEM as a Cloud Service.
