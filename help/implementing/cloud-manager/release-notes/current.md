---
title: Release Notes for Cloud Manager 2023.6.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2023.6.0 in AEM as a Cloud Service.
feature: Release Information
exl-id: 9c73d7ab-c2c2-4803-a07b-e9054220c6b2
---

# Release Notes for Cloud Manager 2023.6.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager release 2023.6.0 in AEM as a Cloud Service.

>[!NOTE]
>
>Refer to [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2023.6.0 in AEM as a Cloud Service is 8 June 2023. The next release is planned for 6 July 2023.

## What's New {#what-is-new}

* When creating a new [program or environment,](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md) the user is now notified of unsupported characters in program or environment name.
* When resuming a [production pipeline,](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md) a confirmation dialog is now displayed at the approve step.
* For the **[Customer Functional Tests](/help/implementing/cloud-manager/functional-testing.md#custom-functional-testing)** and **[Custom UI Testing](/help/implementing/cloud-manager/ui-testing.md)** pipeline steps, a new `INCOMPLETE` status is now possible, which indicates that such tests were not present and hence not performed.
  * In such cases, the pipeline does not fail and proceeds to the next step.
* User input for program and environment name will be restricted to accept only alphanumeric characters and a list of limited special characters.

## Bug Fixes {#bug-fixes}

* The [web tier config pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#web-tier-config-pipelines) are no longer incorrectly enabled for Assets-only programs.
* More robust validation was added to prevent certain types of failures during environment provisioning.
