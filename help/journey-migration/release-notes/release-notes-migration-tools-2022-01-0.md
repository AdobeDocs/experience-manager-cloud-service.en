---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.1.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.1.0
exl-id: cbd0c316-bda3-48fb-89d6-a8f97bad1970
feature: Release Information
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
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.1.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2022.1.0.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.7.18 is January 18, 2022.

### What's New {#what-is-new-ctt}

* Toggle added to the extraction phase in the Content Transfer Tool to allow users to disable [pre-copy](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/handling-large-content-repositories.html) during extraction. For optimal extraction speeds, pre-copy during extraction should be disabled for small migration sets or if only a few blobs were added since the last extraction. 

### Bug Fixes {#bug-fixes-ctt}

* Default configurations updated to reduce execution timeouts during extraction.
