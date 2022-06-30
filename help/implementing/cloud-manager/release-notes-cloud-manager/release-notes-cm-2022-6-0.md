---
title: Release Notes for Cloud Manager 2022.6.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2022.6.0 in AEM as a Cloud Service.
feature: Release Information
---

# Release Notes for Cloud Manager 2022.6.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager 2022.6.0 in AEM as a Cloud Service.

>[!NOTE]
>
>Refer to [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2022.6.0 in AEM as a Cloud Service is June 9, 2022. The next release is planned for June 30, 2022.

## What's New {#what-is-new}

* The Cloud Manager UI now allows [self-service content restoration](/help/operations/backup.md) to a known good state of the AEM cloud environment.
  * This feature will be rolled out in a phased approach over the weeks following the 2022.06.0 release.
* A new welcome card on the Cloud Manager landing page gives users quick access to onboarding tutorials and progress metrics related to the tenant.
  * This feature will be rolled out in a phased approach over the week following the 2022.06.0 release.
* Users with requisite permissions can access a new [License Dashboard](/help/implementing/cloud-manager/license-dashboard.md) on the Cloud Manager landing page to view details of entitlements available to the tenant.
  * AEM Sites is the first solution for which availability and usage consumption is delivered via the Cloud Manage dashboard.
  * This feature will be rolled out in a phased approach over the weeks following the 2022.06.0 release.
* [New Relic sub-account and self-service user management](/help/implementing/cloud-manager/user-access-new-relic.md) is now available via the Cloud Manager UI.
  * This feature will be rolled out in a phased approach over the weeks following the 2022.06.0 release.
* A new Go Live widget on the home page of Cloud Service production programs now provides guidance to prepare for a successful go live experience.
* [Build artifacts can now be reused](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/setting-up-project.md#build-artifact-reuse) when using git mirroring.

## API Changes {#api-changes}

* The [`List Programs`](https://developer.adobe.com/experience-cloud/cloud-manager/reference/api/#operation/getPrograms) API has been deprecated and [`List Programs for Tenant`](https://developer.adobe.com/experience-cloud/cloud-manager/reference/api/#operation/getProgramsForTenant) should be used instead.
  * `List Programs` continues to work, but its usage will generate warning messages in logs.
  * It will no longer be supported after three months.
  