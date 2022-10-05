---
title: Release Notes for Cloud Manager 2022.10.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2022.10.0 in AEM as a Cloud Service.
feature: Release Information
exl-id: 9c73d7ab-c2c2-4803-a07b-e9054220c6b2
---

# Release Notes for Cloud Manager 2022.10.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager 2022.10.0 in AEM as a Cloud Service.

>[!NOTE]
>
>Refer to [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2022.9.0 in AEM as a Cloud Service is 6 October 2022. The next release is planned for 3 November 2022.

## What's New {#what-is-new}

* The version of the [AEM project archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html) used by Cloud Manager has been updated to version 36.
* The license dashboard UI will now inform users if a Sites programs is configured with a CDN on top of AEM as a Cloud Service.

## Bug Fixes {#bug-fixes}

* A situation was fixed where users with uppercase letters in their email address could not be added to a New Relic sub-account in Cloud Manager.
* The Screens solution is now displayed if there are multiple solutions in the program.
* A situation was fixed where the front-end pipeline execution would not start when the environment had the status UPDATING.
