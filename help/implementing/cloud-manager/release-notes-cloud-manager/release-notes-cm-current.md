---
title: Release Notes for Cloud Manager 2022.3.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2022.3.0 in AEM as a Cloud Service.
feature: Release Information
exl-id: 9c73d7ab-c2c2-4803-a07b-e9054220c6b2
---

# Release Notes for Cloud Manager 2022.3.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager 2022.3.0 in AEM as a Cloud Service.

>[!NOTE]
>
>Refer to [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2022.3.0 in AEM as a Cloud Service 10 March 2022. The next release is planned for 7 April 2022.

## What's New {#what-is-new}

* A user with the **Developer** role can now access the AEM environment log.
* The `reliability_rating` critical metric has been disabled.
* A user can now sort on the columns in the **Pipelines** page in Cloud Manager.

## Bug Fixes {#bug-fixes}

* A subset of manually-created git repositories had incorrect name values which affected [the build artifact reuse feature.](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/setting-up-project.md#build-artifact-reuse) The names of those repositories have been changed and users will see the corrected name in the Cloud Manager API/UI.
* When adding or editing a code quality pipeline, the options to handle metric failures is no longer displayed.
* Unexpected pipeline variable configurations no longer cause errors in the build step.
