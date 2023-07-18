---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.06.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.06.0
feature: Release Information
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.06.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2022.06.0.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v2.0.20 is June 08, 2023.

### What's New {#what-is-new-ctt}

* A new migration tool - Content Transformer (CT) has been integrated with the Content Transfer Tool (CTT) with this release. The Content Transformer can automatically detect and fix content related issues reported by the [Best Practices Analyzer (BPA)](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/best-practices-analyzer/overview-best-practices-analyzer.html?lang=en) before migrating content from your current AEM implementation (On-premise or Managed Services) to AEM as a Cloud Service. 
Benefits provided by the Content Transformer are:
   * Fail-safe: a package is created by the Content Transformer every time it makes any modification to the repository to fix issues. If needed, you can revert back to the previous state by installing the package.
   * Easy-to-use: the Content Transformer has been integrated with the Content Transfer Tool and comes with a simple user interface that is intuitive.
   * Saves time: when you have a high number of content issues that fall under one pattern category, you can resolve all of them with just a couple of clicks using the Content Transformer, significantly reducing time and migration complexity.
