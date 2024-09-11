---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.1.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.1.0
exl-id: cbd0c316-bda3-48fb-89d6-a8f97bad1970
feature: Release Information
role: Admin
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
