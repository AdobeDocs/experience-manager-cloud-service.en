---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.03.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.03.0
feature: Release Information
exl-id: cdc57cca-e10a-4b0d-b803-910ccc9350a6
role: Admin
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.03.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2023.03.0.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.40 is March 03, 2023. 

### What's New {#what-is-new-bpa}

* BPA can now detect and report on conflicting nodes - nodes with the same `jcr:uuid`. Such findings are flagged as critical since it can lead to content ingestion failures when moving content to AEM as a Cloud Service.  
* BPA can now detect and report on the usage of Event Listeners. It is recommended to refactor this type of event handing mechanism to sling jobs when moving to AEM as a Cloud Service. 

### Bug Fixes {#bug-fixes-bpa}

* BPA was reporting false positives on `grouprendercondition`. This has been fixed.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v2.0.16 is March 08, 2023.

### What's New {#what-is-new-ctt}

* User mapping has been streamlined and integrated into the content extraction step. No setup is needed and by default user mapping is done automatically when the user initiates content extraction. The user has the option to disable user mapping if needed. Learn more [here](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/user-mapping-and-migration.html#user-mapping-detail).
* The precopy step using [AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) has been integrated with the Content Transfer Tool to speed up content extractions significantly. Precopy is automatically configured and installed when this version of the CTT is installed. By default, when extraction is initiated, precopy will run automatically for migration sets larger than 200 GB. User has the option to disable it if needed. Learn more [here](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/handling-large-content-repositories.html).
* CTT can now be used on Windows servers.

### Bug Fixes {#bug-fixes-ctt}

* Multiple bug fixes to improve content extraction resiliency.
