---
title: AEM Dispatcher Converter Tool
description: AEM Dispatcher Converter Tool
---

# AEM Dispatcher Converter {#introduction}

Adobe Experience Manager Dispatcher Converter converts existing AMS Dispatcher configurations to AEM as a Cloud Service Dispatcher configurations.

## Introduction to Dispatcher {#introduction-dispatcher}

Dispatcher is Adobe Experience Manager's caching and/or load balancing tool. Using AEM's Dispatcher also helps to protect your AEM server from attack. Therefore, you can increase the security of your AEM instance by using the Dispatcher in conjunction with an enterprise-class web server.

>[!NOTE]
>The most common use of Dispatcher is to cache responses from an **AEM publish instance**, to increase the responsiveness and security of your externally facing published website.

Refer to [Dispatcher Overview](https://docs.adobe.com/content/help/en/experience-manager-dispatcher/using/dispatcher.html) to learn how dispatcher performs caching, returns documents and performs Load Balancing.

### Apache and Dispatcher Configuration and Testing {#dispatcher-configurations-cloud}

You must learn how to structure the AEM as a Cloud Service Apache and Dispatcher configurations, as well as how to validate and run it locally before deploying to Cloud environments.

Refer to [Dispatcher in the Cloud](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/dispatcher/overview.html) for more information.

## AEM Dispatcher Converter {#aem-dispatcher-converter}

AEM Dispatcher Converter is a utility for converting existing AMS Dispatcher configurations to AEM as a Cloud Service Dispatcher configurations. This utility is for AMS instances.

The implemented converter is **AEMDispatcherConfigConverter** that follows the transformation guidelines.

Refer to [Converting an AMS to an Adobe Experience Manager as a Cloud Service Dispatcher Configuration](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/content-delivery/disp-overview.html#how-to-convert-an-ams-to-an-aem-as-a-cloud-service-dispatcher-configuration) for converting an AMS to an Adobe Experience Manager as a Cloud Service Dispatcher configuration.

## Using AEM Dispatcher Converter {#using-dispatcher-converter}

The following section describes the resources and information required for using the AEM Dispatcher Converter tool.

Refer to **[Git Resource: AEM Cloud Service Dispatcher Converter](https://github.com/adobe/aem-cloud-service-dispatcher-converter)** to learn about the usage, limitations, and troubleshooting for this tool.

>[!IMPORTANT]
>AEM Dispatcher Converter is developed using Python 3.7.3. It is recommended to have Python 3.5 or above installed.

## Limitations {#limitations}

AEM Dispatcher Converter works on the assumption that the provided dispatcher configuration folder's structure is similar to the one described in Cloud Manager dispatcher configuration.


