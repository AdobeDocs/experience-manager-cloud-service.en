---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2021.11.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2021.11.0
feature: Release Information
exl-id: 668c0c66-88f5-4d74-9a2a-3bdc63b0bba7
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
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2021.11.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2021.11.0.

>[!NOTE]
>
>See [Current Release Notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md) for the latest release notes.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.7.2 is November 01, 2021.

### What's New {#what-is-new-ctt}

* Support for an optional [pre-copy](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/handling-large-content-repositories.html) step added to use with Content Transfer Tool when source AEM instance is configured to use File Data Store to significantly speed up the extraction phase.

* Additional descriptive messages added to the ingestion phase in the Content Transfer Tool UI to indicate when indexing and mongo recovery steps are in-progress.
