---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2021.12.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2021.12.0
feature: Release Information
exl-id: 4155e1c0-cd40-4cbc-9d6c-b106d68a2db5
role: Admin
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2021.12.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2021.12.0.

>[!NOTE]
>
>See [Current Release Notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md) for the latest release notes.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.22 is December 01, 2021.

### What's New {#what-is-new-bpa}

* Ability to detect and report on the version of ACS commons used.
* Ability to detect and report on the number of users and sub-groups in a group.
* Ability to detect and report on node property values in MongoDB that exceed 16MB.

### Bug Fixes {#bug-fixes-bpa}

* Detection of Foundation components was refined to reduce false negatives.
* For AEM Forms customers, BPA messaging regarding `EMAIL_PDF_SUBMIT_ACTION` not being available on AEM as a Cloud Service has been fixed. 


## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.7.10 is December 08, 2021.

### What's New {#what-is-new-ctt}

* Toggle added to the ingestion phase in the Content Transfer Tool to allow users to disable [pre-copy](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/handling-large-content-repositories.html) during ingestion. For optimal ingestion speeds, pre-copy during ingestion should be disabled for small migration sets or if only a few blobs were added since the last ingestion. 
* User Mapping updated to use improved User Management API that allows it to get 2000 users at a time, significantly improving the performance.
