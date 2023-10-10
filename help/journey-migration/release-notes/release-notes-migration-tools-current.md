---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.10.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.10.0
feature: Release Information
exl-id: 52709511-eab2-47a7-8bea-1b707cd568a1
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2023.10.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2022.10.0.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v3.0.4 is October 06, 2023.

### What's New {#what-is-new-ctt}

* Changes have been made to the content ingestion process - It is no longer required to submit a Customer Care/Support ticket to disable the AEM Version Updates on the destination environment. This process is now automated. For more details, refer to [AEM Version Updates and Ingestions](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/ingesting-content.html#aem-version-updates-and-ingestions)
* Dynamic concurrency will be used during the [pre-copy](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/handling-large-content-repositories.html?lang=en) step in both extraction and ingestion phases, significantly reducing the content migration time.  
