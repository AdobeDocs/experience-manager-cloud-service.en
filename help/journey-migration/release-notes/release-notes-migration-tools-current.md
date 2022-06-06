---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.5.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.5.0
feature: Release Information
exl-id: 2f787321-f156-480d-bbe8-1a6d04f110c5
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.5.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2022.5.0.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.30 is June 1, 2022.

### What's New {#what-is-new-bpa}

* Ability to detect and report on usage of custom dialog widgets using CoralUI and Classic dialog widgets. It is recommended to convert custom Classic Dialog widgets from ExtJS to CoralUI. Custom Coral Dialog Widgets should be updated to CoralUI3.
* Ability to detect and report on the usage and version of Assets Share Commons. Asset Share Commons 1.x is not supported on AEM as a Cloud Service and must be upgraded to 2.x.
* Ability to detect and report on the number of nodes from versions.
* Ability to detect and report on custom replication agents or out of the box replication agents that have been modified.

### Bug Fixes {#bug-fixes-bpa}

* BPA was reporting NCC (Non-compatible changes), UMI (Upgrade Misconfiguration Issue), and PCX (Page Complexity) findings that are false positives. These have been fixed.
* BPA was reporting failures when any node name length exceeded 150 bytes. This has been fixed to detect such failures only when the node parent path is equal or larger than 350 bytes.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v2.0.10 is June 2, 2022.

### What's New {#what-is-new-ctt}

* The Content Transfer Tool (CTT) has been evolved to work with Cloud Acceleration Manager to streamline the entire content transfer process. CTT now focuses on performing content extractions. The CTT ingestion service is now integrated into Cloud Acceleration Manager. Benefits provided via this evolution are:
   * Self-service way to extract a migration set once and ingest it into multiple environments in parallel.
   * Improved user experience via better loading states, guardrails, and error handling.
   * Ingestion logs are persisted and are always available for troubleshooting.

## Cloud Acceleration Manager {#cam-release}

### Release Date {#release-date-cam}

The Release Date for Cloud Acceleration Manager is June 2, 2022.

### What's New {#what-is-new-cam}

* Cloud Acceleration Manager now provides users to start and manage content transfers to move content from a customer’s AEM instance (On-premise or Adobe Managed Services) to AEM as a Cloud Service as part of a migration project. Refer to [Using Content Transfer Card](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-acceleration-manager/using-cam/cam-implementation-phase.html#content-transfer) for more details.
