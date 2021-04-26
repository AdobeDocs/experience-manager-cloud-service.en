---
title: Notable Changes to AEM Sites in AEM Cloud Service
description: Notable Changes to AEM Sites in AEM Cloud Service
exl-id: 60b1aec4-75a0-459f-bf77-8d8c1af757ce
---
# Notable Changes to AEM Sites as a Cloud Service {#notable-changes}

AEM Sites as a Cloud Service provides experience management capabilities as part of the cloud-native AEM as a Cloud Service platform. In addition to core benefits of AEM as a Cloud Service, such as cloud-native scalability, uptime, and always being up-to-date, AEM Sites as a Cloud Service also provides a number of Sites-specific changes and additions. 

>[!NOTE]
>This document highlights the notable changes to AEM Sites. For changes general to AEM as a Cloud Service, and other modules, see:
>
>* [An Introduction to Adobe Experience Manager as a Cloud Service](/help/overview/introduction.md)
>* An [Overview of AEM as a Cloud Service - What is New and What is Different](/help/overview/what-is-new-and-different.md)
>* The [Architecture](/help/core-concepts/architecture.md) of Adobe Experience Manager as a Cloud Service
>* [Notable changes to AEM as a Cloud Service (Release Notes)](/help/release-notes/aem-cloud-changes.md)
>* [Notable changes to AEM Assets as a Cloud Service](/help/assets/assets-cloud-changes.md)
>* [Introducing AEM Assets as a Cloud Service](/help/assets/overview.md)
>* [Adobe Experience Manager as a Cloud Service Tutorials](https://docs.adobe.com/content/help/en/experience-manager-learn/cloud-service/overview.html)

Changes and additions in AEM Sites as a Cloud Service are as follows:

* [Asynchronous Page Operations](#asynchronous-page-operations)
* [New Reference Site and Tutorial](#new-reference-site-and-tutorial)

## Asynchronous Page Operations {#asynchronous-page-operations}

In AEM Cloud service, operations that traditionally have blocked the UI have been broken down into smaller tasks which run in the background.

* Move pages
* Roll-out pages

The initiator of such actions can check their status in a new UI at `/mnt/overlay/dam/gui/content/asyncjobs.html`.

>[!NOTE]
>
>There is no change required by the user of the system to make use of this new feature. It is noted here simply as a change in behavior from previous on-premise versions of AEM.

## New Reference Site and Tutorial {#new-reference-site-and-tutorial}

[WKND](https://wknd.site/), a new AEM reference site, has been updated and published to reflect best practices for to build a web site with AEM, and the comprehensive set of capabilities, components, and deployment models that are available in AEM. The new reference site and [accompanying tutorial](https://docs.adobe.com/content/help/en/experience-manager-learn/getting-started-wknd-tutorial-develop/overview.html) covers fundamental topics like project setup, Core Components, Editable Templates, client libraries, and component development with Adobe Experience Manager Sites.

Previously, We.Retail was installed by default with AEM (except when started in production mode).  Now, a reference site will not be installed by default going forward.  Instead the [git repo](https://github.com/adobe/aem-guides-wknd/) and [accompanying tutorial](https://docs.adobe.com/content/help/en/experience-manager-learn/getting-started-wknd-tutorial-develop/overview.html) with the updated WKND reference site code is provided.

## Capabilities not available at Runtime {#capabilities-not-available-at-runtime}

AEM as a Cloud Service is always on and always up to date. Achieving this requires the separation of the AEM repository in immutable and mutable content, and prohibiting access to immutable content at runtime. For more details on mutable vs immutable content see [Mutable vs. Immutable Areas of the Repository](/help/implementing/developing/introduction/aem-project-content-package-structure.md#mutable-vs-immutable). 

As a result of immutable content being inaccessible at runtime, the following AEM Sites operations are not available at runtime:

* i18n dictionary translation 
* Developer Mode in AEM Sites Page Editor 

These capabilities can be used via local, standalone developer instances of AEM as a Cloud Service, for updating content and code in the AEM as a Cloud Service GIT repository, but not in hosted runtime instances.
