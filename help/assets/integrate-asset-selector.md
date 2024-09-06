---
title: Asset Selector for [!DNL Adobe Experience Manager] as a [!DNL Cloud Service]
description: Integrate Asset selector with various Adobe, non-Adobe, and third party applications.
role: Admin, User
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

## Integrate Asset Selector with various applications {#asset-selector-integration-with-apps}

You can integrate Asset Selector with various applications such as:

* [Integrate Asset Selector with an [!DNL Adobe] application](#integrate-asset-selector.md)
* [Integrate Asset Selector with a non-Adobe application](#integrate-asset-selector-non-adobe.md)
* [Integration for Dynamic Media with OpenAPI capabilities](#integrate-asset-selector-dynamic-media-open-api.md)


>[!MORELIKETHIS]
>
>* [Asset Selector customization](/help/assets/asset-selector-customization.md)
>* [Asset Selector properties](/help/assets/asset-selector-properties.md)
>* [Integrate Asset Selector dynamic media open APIs](/help/assets/integrate-asset-selector-dynamic-media-open-api.md)
