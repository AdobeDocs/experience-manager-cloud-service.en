---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.10.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.10.0
feature: Release Information
exl-id: e5250b5b-a56c-4bf0-8510-2334a12e36b6
role: Admin
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.10.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2023.10.0.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v3.0.4 is October 06, 2023.

### What's New {#what-is-new-ctt}

* Changes have been made to the content ingestion process - It is no longer required to submit a Customer Care/Support ticket to disable the AEM Version Updates on the destination environment. This process is now automated. For more details, refer to [AEM Version Updates and Ingestions](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#aem-version-updates-and-ingestions)
* Dynamic concurrency will be used during the [pre-copy](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md) step in both extraction and ingestion phases, significantly reducing the content migration time.
