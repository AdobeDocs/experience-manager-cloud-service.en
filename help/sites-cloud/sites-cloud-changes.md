---
title: Notable Changes to AEM Sites in AEM Cloud Service
seo-title: Notable Changes to AEM Sites in AEM Cloud Service
description: Notable Changes to AEM Sites in AEM Cloud Service 
seo-description: Notable Changes to AEM Sites in AEM Cloud Service
---

# Notable Changes to AEM Sites in AEM Cloud Service {#notable-changes}

AEM Cloud Service brings many new features and possibilities for managing your AEM projects. However there are a number of differences between AEM Sites on premise or in Adobe Managed Service as compared to AEM Cloud Service. This document highlights the important differences.

>[!NOTE]
>This document highlights the notable changes to AEM Sites. For changes general to AEM in the Cloud see:
>
>* [Notable Changes to Adobe Experience Manager (AEM) as a Cloud Service](/help/release-notes/aem-cloud-changes.md)

The main differences are found in the following areas:

- [Page Bulk Operations](#page-bulk-operations)
- [Removal of Classic UI](#classic-ui)

## Page Bulk Operations {#page-bulk-operations}

In AEM Cloud service, operations that traditionally have blocked the UI have been broken down into smaller tasks which run in the background.

- Move pages
- Roll-out pages

The initiator of such actions can check their status in a new UI at `/mnt/overlay/dam/gui/content/asyncjobs.html`.

>[!NOTE]
>
>There is no change required by the user of the system to make use of this new feature. It is noted here simply as a change in behavior from previous on-premise versions of AEM.

## Removal of Classic UI {#classic-ui}

The Classic UI is no longer available in AEM Cloud Service.
