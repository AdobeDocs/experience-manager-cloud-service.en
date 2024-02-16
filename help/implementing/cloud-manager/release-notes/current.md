---
title: Release Notes for Cloud Manager 2024.2.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2024.2.0 in AEM as a Cloud Service.
feature: Release Information
exl-id: 9c73d7ab-c2c2-4803-a07b-e9054220c6b2
---

# Release Notes for Cloud Manager 2024.2.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager release 2024.2.0 in AEM as a Cloud Service.

>[!NOTE]
>
>See [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2024.2.0 in AEM as a Cloud Service is 16 February 2024. The next release is planned for 16 March 2024.

## What's New {#what-is-new}

* Cloud Manager now supports self-service management of [pipeline variables](/help/implementing/cloud-manager/configuring-pipelines/pipeline-variables.md) via the Cloud Manager UI.
* [The preview service](/help/implementing/cloud-manager/manage-environments.md#access-preview-sevice) will now be enabled for environments created before the preview service feature was rolled out.
* [Cloud Manager custom permissions](/help/implementing/cloud-manager/custom-permissions.md) let you create custom permission profiles with configurable permissions to restrict access to programs, pipelines, and environments for Cloud Manager users.
  * This feature began rolling out in a phased manner with the [December 2023 release](/help/implementing/cloud-manager/release-notes/2023/2023-12-0.md) and will be complete on 20 February 2024.
* For all new environments, the [environment product profile](/help/onboarding/aem-cs-team-product-profiles.md) names will be a more user-friendly format based on a combination of profile description, environment type, number, and program number.
* [The build environment](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md) has been updated to Maven version 3.9.4 and JDK versions jdk-11.0.22 and jdk1.8.0_401.

## Early Adoption Program {#early-adoption}

For a chance to test some upcoming features, be a part of Adobe's early adoption program.

### Client-Side Collection via Real User Monitoring (RUM) {#rum}

You can leverage the [Real User Monitoring (RUM) Data Service](/help/implementing/cloud-manager/content-requests.md#cliendside-collection) to enable client-side collection for AEM as a Cloud Service.

Real User Monitoring (RUM) Data Service offers a more precise reflection of user interactions, ensuring a reliable measure of website engagement. It is a great opportunity to gain advanced insights into your page performance. This is beneficial for customers who use either Adobe-managed CDN or non-Adobe managed CDN. For customers using a non-Adobe managed CDN, automated traffic reporting can now be enabled for them, thus removing the need to share any traffic report with Adobe.

If you are interested in testing this new feature and sharing your feedback, please send an email to `aemcs-rum-adopter@adobe.com` from the email address associated with your Adobe ID. Please include the domain name for production, stage, and dev environments in your email.  Availability of the early adopter program of this feature is limited.

### Bring your own GitHub {#byo-github}

If you use GitHub to manage your repositories, [you can now validate code directly within your GitHub repositories through Cloud Manager.](/help/implementing/cloud-manager/managing-code/byo-github.md) This integration eliminates the need to consistently sync code with the Adobe repository and allows you to verify pull requests before merging them into the main branches. This feature is exclusive to public GitHub. Support for self-hosted GitHub is not available.

If you are interested in testing this new feature and sharing your feedback, send an email to `Grp-CloudManager_BYOG@adobe.com` from your email address associated with your Adobe ID.

### Self-Service Content Restore {#content-restore}

[A new self-service content restore feature](/help/operations/restore.md) now provides backup restoration for up to seven days and is available to early adopters for evaluation purposes featuring:

* Point-in-time backup restoration for the previous 24 hours
* Fixed time restorations for up to seven days

If you are interested in testing this new feature and sharing your feedback, send an email to `aemcs-restorefrombackup-adopter@adobe.com` from your email associated with your Adobe ID.

* The early adopter program is limited to development environments only.
* Availability of the early adopter program of this feature is limited.
* This feature is for recovering accidentally deleted content and is not intended for disaster recovery.

### Experience Audit Dashboard {#experience-audit-dashboard}

[The Cloud Manager Experience Audit dashboard](/help/implementing/cloud-manager/experience-audit-dashboard.md) includes a trended view of your page performance scores along with insights and recommendations to help you improve them. Experience Audit is included as a step in the Cloud Manager production pipeline.

The dashboard uses Google Lighthouse, an open-source, automated tool for improving the quality of your web apps. You can run it against any web page, public, or requiring authentication. It has audits for performance, accessibility, progressive web apps, SEO, and more.

Interested in test-driving the new dashboard? To get started, send an email to `aem-lighthouse-pilot@adobe.com` from your email associated with your Adobe ID.

## Bug Fixes {#bug-fixes}

* The JDK of the build containers has been updated to a version that solves [JDK-8313765.](https://bugs.openjdk.org/browse/JDK-8313765)
