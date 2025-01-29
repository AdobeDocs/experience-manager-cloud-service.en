---
title: Asset Selector for [!DNL Adobe Experience Manager] as a [!DNL Cloud Service]
description: Integrate Asset selector with various Adobe, non-Adobe, and third party applications.
role: Admin, User
exl-id: 1c0051a3-549c-4783-9fc1-594f424a70c3
---
# Integrate Asset Selector using Vanilla JS {#integration-using-vanilla-js}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

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

* [Integrate Asset Selector with an [!DNL Adobe] application](/help/assets/integrate-asset-selector-adobe-app.md)
* [Integrate Asset Selector with a non-Adobe application](/help/assets/integrate-asset-selector-non-adobe-app.md)
* [Integration for Dynamic Media with OpenAPI capabilities](/help/assets/integrate-asset-selector-dynamic-media-open-api.md)


>[!MORELIKETHIS]
>
>* [Asset Selector customizations](/help/assets/asset-selector-customization.md)
>* [Asset Selector properties](/help/assets/asset-selector-properties.md)
>* [Integrate Asset Selector with Dynamic Media with OpenAPI capabilities](/help/assets/integrate-asset-selector-dynamic-media-open-api.md)
