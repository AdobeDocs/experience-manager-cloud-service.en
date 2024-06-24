---
title: Adobe Analytics Integration with AEM Screens Cloud
description: Follow this page to learn about out of the box integration of AEM Screens with Adobe Analytics and provides you with a proof of play.
contentOwner: trushton
content-type: reference
products: SG_EXPERIENCEMANAGER/Cloud/SCREENS
topic-tags: administering
docset: aem65
role: Admin, Developer
level: Intermediate
exl-id: e22242ce-e5ce-4486-bba4-e6a89ac4fb5e
feature: Screens Deployments
---
# Adobe Analytics Integration with AEM Screens Cloud {#adobe-analytics-integration-with-aem-screens}

This section covers the following topics:

* **Overview**
* **Architectural Details**

## Overview {#overview}

***AEM Screens*** leverages Adobe Analytics, and with that you can achieve something unique in the market - cross-channel analytics that help correlate content shown in location with other data sources.

AEM Screens provides an out of the box integration with Adobe Analytics and provides you with a proof of play.

This section describes the following functionality involved with connecting an AEM Screens project with Adobe Analytics:

* Allows for proof of play reporting by device
* Allows for proof of play reporting by asset
* Ensures that all player events are captured and timestamped
* Ensures that all player events are stored locally if the play is not connected to a network
* Allows for feedback loops to be created which track play events over time
* Allows the system to modify content and layouts based on success criteria defined by the content author

Adobe Analytics Integration with AEM Screens thus enforces the following *goals*:

* Enable ROI from digital signage implementations
* Integrate Analytics as a foundation for future enablement of gathering and analyzing usage information

## Architectural Details {#architectural-details}

An AEM Screens customers wants to understand what content was shown at what time, and for how long (aggregated). This is common capability of signage solution. Instead of building our own analytics, AEM Screens uses Adobe Analytics, and with that, you can achieve something unique in the market - cross-channel analytics that help correlate content shown in location with other data sources.

The following architectural diagram explains the Adobe Analytics Integration with AEM Screens:

![Integration with Adobe Analytics](/help/screens-cloud/assets/analytics-architecture.png)

## Enabling Adobe Analytics in AEM Screens Cloud {#enabling-adobe-analytics-in-aem-screens-cloud}

Contact your Adobe Relationship Manager to enable Adobe analytics in Screens Cloud.

## Using Adobe Analytics Service in AEM Screens Cloud {#using-adobe-analytics-service-in-aem-screens}

This scenario invokes Analytics API through REST calls from an analytics service in the firmware and instrument screens-core components to explicitly create and send events specific to a particular use case while allowing extensibility where any custom message can be sent to Analytics from a custom developed channel.

Analytics events are stored offline in indexedDB and later chunked and sent to the cloud.

>[!NOTE]
>To learn more about the Sequencing and Standard Data Model for Events, see [Configuring Adobe Analytics for AEM Screens](https://experienceleague.adobe.com/docs/experience-manager-screens/user-guide/administering/analytics-integration/configuring-adobe-analytics-aem-screens.html) for details.
