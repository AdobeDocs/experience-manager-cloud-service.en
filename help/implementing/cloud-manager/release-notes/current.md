---
title: Release Notes for Cloud Manager 2023.10.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2023.10.0 in AEM as a Cloud Service.
feature: Release Information
exl-id: 9c73d7ab-c2c2-4803-a07b-e9054220c6b2
---

# Release Notes for Cloud Manager 2023.10.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager release 2023.10.0 in AEM as a Cloud Service.

>[!NOTE]
>
>See [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2023.10.0 in AEM as a Cloud Service is 5 October 2023. The next release is planned for 2 November 2023.

## What's New {#what-is-new}

* [You can now safely cancel a pipeline](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#cancel) in the validate and build image steps.
* Improvements to [indexing](/help/operations/indexing.md) have reduced pipeline duration when deploying new indexes.
  * Improvements vary depending on content profile.
* Automatic [updates for development environments](/help/implementing/cloud-manager/manage-environments.md#updating-environments) are enabled by default for new programs, saving you the time having to execute updates manually.
  * This update will be rolled out in a phased manner.
* With the October 2023 release of Cloud Manager, Java and Maven versions are being updated via a phased roll-out.
    * Apache Maven is being updated to version 3.8.8.
    * The Java versions are being updated to Oracle JDK 8u371 and Oracle JDK 11.0.20.
    * By default, the `JAVA_HOME` environment variable is being updated to `/usr/lib/jvm/jdk1.8.0_371` which contains Oracle JDK 8u371.
    * See the document [Build Environment](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md) for more details.
    * [See the OpenJDK advisory](https://openjdk.org/groups/vulnerability/advisories/) for details on the security and bugfixes in these JDK updates.

## Early Adoption Program {#early-adoption}

Be a part of our early adoption program and have a chance to test some upcoming features.

### Custom Permissions {#custom-permissions}

[Cloud Manager custom permissions](/help/implementing/cloud-manager/custom-permissions.md) allows you to create new custom permission profiles with configurable permissions to restrict access to programs, pipelines, and environments for Cloud Manager users.

if you are interested in testing this new feature and sharing your feedback, please send and email `Grp-CloudManager-custom-permissions@adobe.com` from your email address associated with your Adobe ID.

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
