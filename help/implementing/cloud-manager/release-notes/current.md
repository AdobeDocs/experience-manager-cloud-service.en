---
title: Release Notes for Cloud Manager 2023.8.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2023.8.0 in AEM as a Cloud Service.
feature: Release Information
exl-id: 9c73d7ab-c2c2-4803-a07b-e9054220c6b2
---

# Release Notes for Cloud Manager 2023.8.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager release 2023.8.0 in AEM as a Cloud Service.

>[!NOTE]
>
>See [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2023.8.0 in AEM as a Cloud Service is 10 August 2023. The next release is planned for 7 September 2023.

## What's New {#what-is-new}

* For [content copy](/help/implementing/developing/tools/content-copy.md) purposes, [content aware configurations](/help/implementing/developing/introduction/configurations.md) are now permitted in content sets when using the UI.
* Enhancements were made to improve comprehensibility and surfacing of error messages in Cloud Manager UI.

## Bug Fixes {#bug-fixes}

* The **Environments** menu now closes after triggering the **[Copy Content](/help/implementing/developing/tools/content-copy.md)** modal.
* [A pipeline re-execution](/help/implementing/cloud-manager/deploy-code.md#reexecute-deployment) is no longer allowed if the previous execution does not have a `commitId` set on the build phase state.
* A more understandable message is now displayed for rare errors when a user clicks on a pipeline in the **Activity** or **Pipeline** screens.
* The `contentSetName` value is no longer missing in logs and is now provided in the inputs when starting a [content copy](/help/implementing/developing/tools/content-copy.md) operation.
* It is no longer possible under certain rare circumstances to start two executions from the same pipeline leading to a "stuck" state.
* When a certificate expires, domain names and IP allow-lists associated with the certificate will no longer be removed from the CDN.
  * In such cases, the site will continue to be reachable.
  * [The Cloud Manager UI](/help/implementing/cloud-manager/managing-ssl-certifications/introduction.md) will provide more visible advance warnings that the SSL certificate is about to expire.
