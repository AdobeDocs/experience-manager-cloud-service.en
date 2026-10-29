---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.06.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.06.0
feature: Release Information
exl-id: 021b7472-d1e4-4ef6-a040-c612fed8d3c3
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
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.06.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2023.06.0.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v2.0.20 is June 08, 2023.

### What's New {#what-is-new-ctt}

* A new migration tool - Content Transformer (CT) has been integrated with the Content Transfer Tool (CTT) with this release. The Content Transformer can automatically detect and fix content related issues reported by the [Best Practices Analyzer (BPA)](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/best-practices-analyzer/overview-best-practices-analyzer.html) before migrating content from your current AEM implementation (On-premise or Managed Services) to AEM as a Cloud Service. 
Benefits provided by the Content Transformer are:
   * Fail-safe: a package is created by the Content Transformer every time it makes any modification to the repository to fix issues. If needed, you can revert back to the previous state by installing the package.
   * Easy-to-use: the Content Transformer has been integrated with the Content Transfer Tool and comes with a simple user interface that is intuitive.
   * Saves time: when you have a high number of content issues that fall under one pattern category, you can resolve them all with several clicks using the Content Transformer, significantly reducing time and migration complexity.
