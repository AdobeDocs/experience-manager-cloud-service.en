---
title: Release Notes for Cloud Manager 2022.3.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2022.3.0 in AEM as a Cloud Service.
feature: Release Information
exl-id: d09d48c5-6e0a-4a6a-85e9-1a60fdd6e5bf
---
# Release Notes for Cloud Manager 2022.3.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager 2022.3.0 in AEM as a Cloud Service.

>[!NOTE]
>
>Refer to [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2022.3.0 in AEM as a Cloud Service is March 10, 2022. The next release is planned for April 7, 2022.

## What's New {#what-is-new}

* Accessing AEM Environment log can be done using the Developer role.

## Bug Fixes {#bug-fixes}

* A subset of git repositories created manually had an incorrect name value which prevented the build artifact reuse feature from being effective. The names of those repositories have been changed and users will see the corrected name in the Cloud Manager API/UI.
* Build artifacts from non-production pipelines were inappropriately reused on production full stack pipelines.
 * When adding or editing a code quality pipeline, the options to handle metric failures is no longer displayed.
* Some unexpected pipeline variable configurations could cause in the build step.
