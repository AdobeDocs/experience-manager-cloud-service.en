---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.09.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.09.0
feature: Release Information
exl-id: 484a60d4-a439-43d6-a23e-4a3b45ef4160
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.09.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2022.09.0.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v3.0.0 is September 07, 2023.

### What's New {#what-is-new-ctt}

The Content Transfer Tool has been significantly improved to provide the following benefits:
* Reduced transfer time when migrating a subset of a content repository by leveraging AzCopy to copy only the required blob ids instead of copying all blob ids
* Faster differential content top-ups using Oak-upgrade
* Improved robustness by separating the indexing process from the content ingestion process. In case of a failed indexing, content will not have to be ingested again. Only indexing will automatically re-start, saving significant time and effort
