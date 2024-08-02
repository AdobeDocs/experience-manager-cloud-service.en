---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2024.07
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2024.07.0
feature: Release Information
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2024.07.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2024.07.0.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v3.0.16 is July, 2024.

### What's New {#what-is-new-ctt}

* Automatic upload of CTT extraction logs in case of failures.
* Users can now successfully perform ingestion upon renewal of the extraction key.
* Added support for performing CTT extractions using an Azure access key and secret key with AzureDataStore.
* Users will now receive the correct error message when an invalid key is used to create a migration set.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.50 is May, 2024.

### Bug fixes {#bug-fixes-bpa}

* The Best Practices Analyzer now detects all nodes larger than 16MB
* Race condition causing sproradic occurrences of NCC findings fixed.
