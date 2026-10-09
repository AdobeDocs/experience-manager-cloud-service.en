---
title: Integrate Content Fragment Selector using Vanilla JS
description: Integrate Content Fragment selector with various Adobe, non-Adobe, and third party applications.
role: Admin, User, Developer
exl-id: 84734f1d-2eb8-4768-9c0b-6cea9baddb0f
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Integrate Content Fragment Selector using Vanilla JS {#integrate-content-fragment-selector-using-vanilla-js}

You can integrate any Adobe or non-Adobe application with Adobe Experience Manager (AEM) as a Cloud repository and select Content Fragments from within that application. 

The integration is done by importing the Content Fragment Selector package and connecting to the AEM as a Cloud Service using the Vanilla JavaScript library. Edit an `index.html` or any appropriate file within your application to:

* Define the authentication details
* Access the AEM as a Cloud Service repository
* Configure the Content Fragment Selector display properties

You can perform authentication without defining some of the IMS properties, if you:

* are integrating an Adobe application on [Unified Shell](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/aem-cloud-service-on-unified-shell)
* already have an IMS token generated for authentication
