---
title: Release Notes for Cloud Manager 2023.9.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2023.9.0 in AEM as a Cloud Service.
feature: Release Information
exl-id: 9c73d7ab-c2c2-4803-a07b-e9054220c6b2
---

# Release Notes for Cloud Manager 2023.9.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager release 2023.9.0 in AEM as a Cloud Service.

>[!NOTE]
>
>See [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2023.9.0 in AEM as a Cloud Service is 14 September 2023. The next release is planned for 5 October 2023.

## What's New {#what-is-new}

* CDN logs, when available, can be downloaded via Cloud Manager UI.
* Users can now opt-in to include Experience Audit testing powered by Google LightHouse in non-production, full stack pipelines.

## Early Adoption Program {#early-adoption}

Be a part of our early adoption program and have a chance to test some upcoming features.

### Self-Service Content Restore {#content-restore}

[A new self-service content restore feature](/help/operations/restore.md) now provides backup restoration for up to seven days and is available to early adopters for evaluation purposes featuring:

* Point-in-time backup restoration for the previous 24 hours
* Fixed time restorations for up to seven days

If you are interested in testing this new feature and sharing your feedback, please send an email to `aemcs-restorefrombackup-adopter@adobe.com` from your email associated with your Adobe ID. Please note:

* The early adopter program is limited to development environments only.
* Availability of the early adopter program of this feature is limited.
* This feature is for recovering accidentally deleted content and is not intended for disaster recovery.

### Experience Audit Dashboard {#experience-audit-dashboard}

[The Cloud Manager Experience Audit dashboard](/help/implementing/cloud-manager/experience-audit-dashboard.md) includes a trended view of your page performance scores along with insights and recommendations to help you improve them. Experience Audit is included as a step in the Cloud Manager production pipeline.

The dashboard leverages Google Lighthouse, an open-source, automated tool for improving the quality of your web apps. You can run it against any web page, public or requiring authentication. It has audits for performance, accessibility, progressive web apps, SEO, and more.

Interested in test-driving the new dashboard? Please send an email to `aem-lighthouse-pilot@adobe.com` from your email associated with your Adobe ID and we can get you started.

## Bug Fixes {#bug-fixes}

* When a program is deleted, any associated, running pipeline is now also deleted.
* If a pipeline is in progress, the **Send** button of the **Go-live complete** dialog is now disabled and informs the user that the go-live date can't be set because of the the running pipeline.
* An occasional error has been fixed where all steps of a pipeline execution were marked as completed, but the status of the pipeline was still running, giving the appearance of a stuck state.
