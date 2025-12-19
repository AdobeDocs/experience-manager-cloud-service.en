---
title: Integrate Content Fragment Selector using Vanilla JS
description: Integrate Content Fragment selector with various Adobe, non-Adobe, and third party applications.
role: Admin, User, Developer
---
# Integrate Content Fragment Selector using Vanilla JS {#integrate-content-fragment-selector-using-vanilla-js}

You can integrate any Adobe or non-Adobe application with Experience Manager Assets repository and select fragments from within the application. 

The integration is done by importing the Content Fragment Selector package and connecting to the AEM as a Cloud Service using the Vanilla JavaScript library. Edit an `index.html` or any appropriate file within your application to:

* Define the authentication details
* Access the Assets as a Cloud Service repository
* Configure the Content Fragment Selector display properties

You can perform authentication without defining some of the IMS properties, if:

* You are integrating an [!DNL Adobe] application on [Unified Shell](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/overview/aem-cloud-service-on-unified-shell.html?lang=en).
* You already have an IMS token generated for authentication.
