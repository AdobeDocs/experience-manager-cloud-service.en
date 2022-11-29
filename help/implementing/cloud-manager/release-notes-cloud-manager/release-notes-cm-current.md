---
title: Release Notes for Cloud Manager 2022.12.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2022.12.0 in AEM as a Cloud Service.
feature: Release Information
exl-id: 9c73d7ab-c2c2-4803-a07b-e9054220c6b2
---

# Release Notes for Cloud Manager 2022.12.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager 2022.12.0 in AEM as a Cloud Service.

>[!NOTE]
>
>Refer to [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2022.12.0 in AEM as a Cloud Service is 29 November 2022. The next release is planned for 19 January 2023.

## What's New {#what-is-new}

* AEM Maintenance Update notification via UI will be rolled out in a phased manner over the next weeks.
* When an ingestion via Content Transfer Tool (CTT) is in progress, environment status in both Developer Console and in Cloud Manager will display as 'Ingestion in Progress'
* Improvements to availability and reliability of Cloud Manager pipelines.

## Bug Fixes {#bug-fixes}

* Front-End pipelines were prevented from running while a pipeline execution was in progress on the same environment. (CMGR-40575)
* PATCH /program//environment//variables request was incorrectly allowed for environments in status failed.
