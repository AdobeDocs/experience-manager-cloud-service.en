---
title: Integrate Asset Selector using Vanilla JS
description: Integrate Asset selector with various Adobe, non-Adobe, and third party applications.
role: Admin, User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 1c0051a3-549c-4783-9fc1-594f424a70c3
---
# Integrate Asset Selector using Vanilla JS {#integration-using-vanilla-js}

You can integrate any [!DNL Adobe] or non-Adobe application with [!DNL Experience Manager Assets] repository and select assets from within the application. See [Asset Selector Integration with various applications](#asset-selector-integration-with-apps).

The integration is done by importing the Asset Selector package and connecting to the Assets as a Cloud Service using the Vanilla JavaScript library. Edit an `index.html` or any appropriate file within your application to:

* Define the authentication details
* Access the Assets as a Cloud Service repository
* Configure the Asset Selector display properties

You can perform authentication without defining some of the IMS properties, if:

* You are integrating an [!DNL Adobe] application on [Unified Shell](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/overview/aem-cloud-service-on-unified-shell.html?lang=en).
* You already have an IMS token generated for authentication.

