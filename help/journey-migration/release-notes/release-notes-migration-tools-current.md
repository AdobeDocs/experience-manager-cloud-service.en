---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.7.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.7.0
feature: Release Information
exl-id: 2f787321-f156-480d-bbe8-1a6d04f110c5
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.7.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2022.7.0.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.30 is July 27, 2022.

### What's New {#what-is-new-bpa}

* BPA can now detect and report on the total migratable Lucene Index size which is Total Lucene Index excluding `/oak:index/lucene` and `/oak:index/damAssetLucene`.
* New pattern added in BPA to detect and report on the use of custom i18n dictionary. Translator.html is not available in AEM as a Cloud Service and custom i18n dictionary needs to be deployed from Git via the Cloud Manager CI/CD pipeline.

### Bug Fixes {#bug-fixes-bpa}

* BPA was reporting on missing original renditions for Content Fragments. Since, Content Fragments do not have renditions, this check is now skipped for Content Fragments.
* The option to filter ACS Commons findings was missing from the BPA UI. This has been fixed.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v2.0.12 is July 19, 2022.

### What's New {#what-is-new-ctt}

* Users logged in via LDAP are now able to run Check Size and User Mapping features in CTT.
* To help debug SSL/TLS connection problems during extractions, users are now able to enable SSL Logging.
* To help debug source connectivity issues, sub domain names are now printed in the logs when connection to Azure fails.
* To help debug issues during pre-copy, AzCopy logs are now appended to the extraction logs when pre-copy fails.
* To avoid stale Check Size results, users will be able to re-run Check Size only after a previous Check Size is completed.

### Bug Fixes {#bug-fixes-ctt}

* Previous extraction logs were appearing after deleting and re-creating a migration set. This has been fixed.
* View Progress action button was not available for migration sets with STOPPED status. This has been fixed.
* Delete action button was not available for migration sets with an expired extraction key. This has been fixed.
* Multiple UI bugs fixed.

## Cloud Acceleration Manager {#cam-release}

### Release Date {#release-date-cam}

The Release Date for Cloud Acceleration Manager is July 15, 2022.

### What's New {#what-is-new-cam}

* Cloud Acceleration Manager now provides users to manually retrieve the migration token to be able to start an ingestion when automatic retrieval fails. Automatic retrieval can fail if customers have set up an IP allow-list that blocks CAM or if a non-admin user attempts to start an ingestion. Refer to [Troubleshooting](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#troubleshooting) for more information.
* Long tables on the Migration Complexity page are now collapsible for ease of use.
