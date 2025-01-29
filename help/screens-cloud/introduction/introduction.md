---
title: Introduction to AEM Screens as a Cloud Service
description: Understand AEM Screens as a Cloud Service.
exl-id: b1cc0a63-ecd3-4d89-ac49-f384cc610cdc
feature: Screens Deployments
role: Admin, Developer, User
---

# Introduction to AEM Screens as a Cloud Service {#introduction-screens-cloud}

With Adobe Experience Manager (AEM) Screens as a Cloud Service, you can create engaging and dynamic digital signage experiences intended to be consumed in public spaces. It is the next evolution of the AEM Screens product and represents a major leap forward in usability and scalability. 

AEM Screens as a Cloud Service is a digital signage solution that allows marketers to create and manage dynamic digital experiences at scale. Also, it involves different types of physical screens as part of a comprehensive digital marketing strategy. It extends Adobe's omni-channel offering beyond the usual web and mobile channels to also include digital signage channels that are all around us. AEM Screens as a Cloud Service enables more relevant, contextual, productive, and anticipatory user experiences through a deep understanding of content creation, content assembly, triggered event management, and media play back for all consumers and visitors in any public space.

## Understanding Components in Screens as a Cloud Service {#understanding-components}

Screens as a Cloud Service has two main components, namely:

* **[Content Provider](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/screens-as-cloud-service/configure-screens-cloud/using-screens-content-provider.html)**, which is the Screens add-on running on AEM Cloud Service or on Adobe Managed Services (AMS). Screens Content Provider allows the content author to create and manage channels. The content authors can add new content, edit the content without worrying about the details of creating displays or player registration. The Content Provider provides an abstraction from the underlying details of developing content, displays, or player registration. 

* **[Services Provider](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/screens-as-cloud-service/configure-screens-cloud/navigating-to-screens-services-provider.html)**, which is the digital signage management service running on Adobe I/O Runtime. Screens Services Provider allows content authors, developers, and administrators to manage displays and players for content playback once the content is added to the channels. Also, the Screens Services Provider informs the orchestrator where and when content is going to play at a high-level.


## Architectural Overview {#architectural-overview}

As an AEM Screens as a Cloud Service user, you can add and manage content in channels. You can register, and manage displays and players from the interfaces designed specifically for Screens as a Cloud Service, namely, **Screens Services Provider** and **Screens Content Provider**.

![Architectural Overview](/help/screens-cloud/assets/architecture-screenscloud.png)
