---
title: Release Notes for Cloud Manager 2023.9.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2023.9.0 in AEM as a Cloud Service.
feature: Release Information
---

# Release Notes for Cloud Manager 2023.9.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager release 2023.9.0 in AEM as a Cloud Service.

>[!NOTE]
>
>See [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2023.9.0 in AEM as a Cloud Service is 7 September 2023. The next release is planned for 5 October 2023.

## What's New {#what-is-new}

This release is focused on bug fixes.

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

* When a program is deleted, any associated, running pipeline is also deleted, ensuring that the pipeline is not incorrectly designated as failed status.
* Occasionally, when all steps of a pipeline execution are 'completed',  status of the pipeline is seen as "running", making it seem to be in a stuck state. It is now seen as 'Complete'.
* For repository branches generated using code generator archetype, CI/CD pipeline fails.
