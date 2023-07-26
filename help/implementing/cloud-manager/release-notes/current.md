---
title: Release Notes for Cloud Manager 2023.7.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2023.7.0 in AEM as a Cloud Service.
feature: Release Information
exl-id: 9c73d7ab-c2c2-4803-a07b-e9054220c6b2
---

# Release Notes for Cloud Manager 2023.7.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager release 2023.7.0 in AEM as a Cloud Service.

>[!NOTE]
>
>See [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2023.7.0 in AEM as a Cloud Service is 29 June 2023. The next release is planned for 10 August 2023.

## What's New {#what-is-new}

* Cards on the Cloud Manager landing page now indicate if [enhanced security](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md) is enabled for their programs.
* If a development [pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) contains no testing steps, users now have the option to include testing steps when they [start the pipeline.](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#running-pipelines)
  * This will be rolled out in a phased manner.
* When [cancelling execution,](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#view-details) the pipeline execution approval step now asks the user to provide a reason for cancelling.
  * This will be rolled out in a phased manner.
* Users can now access [logs from the copy content process.](/help/implementing/developing/tools/content-copy.md#accessing-logs)
  * This option is available only if both the source and destination environments are on AEM version `2023.7.12549` or higher.

## Bug Fixes {#bug-fixes}

* Navigating to the authoring UI from Cloud Manager no longer fails to redirect into Unified Shell after login.
* Editing the go-live date via the go-live widget now navigates to the **Go Live** tab instead of the **Enhanced Security** tab.
* When starting a copy operation, a user will no longer be able to select an environment where a copy operation is already invoked.
