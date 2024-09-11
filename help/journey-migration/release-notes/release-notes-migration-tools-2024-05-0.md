---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2024.05.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2024.05.0
feature: Release Information
role: Admin
exl-id: f50a74fa-ad7d-4837-b0a1-9945c32af02f
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2024.05.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2024.05.0.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.50 is May, 2024.

### What's New {#what-is-new-bpa}

* The Best Practices Analyzer (BPA) now supports automatic uploading of BPA generated reports directly to Cloud Acceleration Manager (CAM). Users will no longer need to manually download the report and upload it to CAM. For more details, see [Using Best Practices Analyzer](/help/journey-migration/best-practices-analyzer/using-best-practices-analyzer.md)

### Bug fixes {#bug-fixes-bpa}

* The Best Practices Analyzer now detects all nodes larger than 16MB
* Race condition causing sproradic occurrences of NCC findings fixed.

## Cloud Acceleration Manager {#cam-release}

### What's New {#what-is-new-cam}

* Cloud Acceleration Manager (CAM) now supports automatic upload of BPA generated reports directly to CAM. To learn more see [Readiness Phase in Cloud Acceleration Manager - Using Best Practices Analysis Card](/help/journey-migration/cloud-acceleration-manager/using-cam/cam-readiness-phase.md#best-practices-analysis)

* Cloud Acceleration Manager now provides an estimate of how long an ingestion may take, given factors such as node count, data store size, etc. Learn more with [Ingesting Content into Cloud Service](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md)
