---
title: Release Notes for Cloud Manager 2022.11.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2022.11.0 in AEM as a Cloud Service.
feature: Release Information
exl-id: 9c73d7ab-c2c2-4803-a07b-e9054220c6b2
---

# Release Notes for Cloud Manager 2022.11.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager 2022.11.0 in AEM as a Cloud Service.

>[!NOTE]
>
>Refer to [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2022.11.0 in AEM as a Cloud Service is 3 November 2022. The next release is planned for 29 November 2022.

## What's New {#what-is-new}

* [AEM Guides](https://experienceleague.adobe.com/docs/experience-manager-guides-learn/tutorials/overview.html) can now be configured in a self-service manner in [sandbox programs.](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md)
* For users who only have the **Cloud Manager User** role, a new card on the welcome page has been customized to guide them through navigating to AEM environments and restricted program access.
* Users without any Cloud Manager roles will no longer be able to access program details. Such users can, however, navigate to author end points from the Cloud Manager landing page.
* Users can set up [incident and proactive notification groups](/help/journey-onboarding/user-groups.md) to receive communications from Adobe about incidents or recommendations related to their AEMaaCS applications.
* The **Add Program** button on the landing page will consistently be shown and provide tool tips, even when it is disabled due to permission or entitlement-related reasons.

## Bug Fixes {#bug-fixes}

* The workflow to add an environment now includes additional validation to ensure a successful outcome.
* The feedback provided to the user has been improved during AEM app build when Maven faces connectivity issues to private repos.
