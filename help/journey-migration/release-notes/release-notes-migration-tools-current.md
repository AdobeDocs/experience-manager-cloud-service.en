---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2024.09
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2024.09.0
feature: Release Information
exl-id: 52709511-eab2-47a7-8bea-1b707cd568a1
role: Admin
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2024.09.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2024.09.0.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v3.0.20 is August 28, 2024.

### What's New {#what-is-new-ctt}

* Users will no longer be ingested with this release and for that reason the User Mapping optional capability has been removed.
* An OSGI config option has been added to disable or enable the migration of principals during extraction and ingestion (the default setting is to enable it)

### Bug fixes {#bug-fixes-ctt}

* CTT was improved to prevent an error while unprotecting a secret key in azcopy config
* CTT now gracefully handles any error while copying AzCopy logs in validation phase
* Change azcopy log directory created during extraction process

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.52 is September 4, 2024

### What's New {#what-is-new-bpa}

* A new pattern was introduced to detect JCR based eventing in AEM

### Bug fixes {#bug-fixes-bpa}

* Fixed false positives
* Improved robustness to handle redirected response from dispatcher
* Fixed non-reporting of NCC finding for all languages under /apps/wcm/core/resources/languages/
* added a check to detect if a multi-property of a node has no values

