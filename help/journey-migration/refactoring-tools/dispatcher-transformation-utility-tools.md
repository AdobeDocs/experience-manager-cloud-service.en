---
title: AEM Dispatcher Converter Tool
description: AEM Dispatcher Converter Tool
exl-id: 97eb4f3f-dc03-461a-8d7e-164065bd1e4c
---
# AEM Dispatcher Converter {#introduction}

>[!CONTEXTUALHELP]
>id="aemcloud_nonbpa_dispconverter"
>title="AEM Dispatcher Converter"
>abstract="Adobe Experience Manager Dispatcher Converter converts existing AEM Dispatcher configurations to AEM as a Cloud Service Dispatcher configurations."

Adobe Experience Manager Dispatcher Converter converts existing AEM Dispatcher configurations to AEM as a Cloud Service Dispatcher configurations.

## Introduction to Dispatcher {#introduction-dispatcher}

Dispatcher is Adobe Experience Manager's caching and/or load balancing tool. Using AEM's Dispatcher also helps to protect your AEM server from attack. Therefore, you can increase the security of your AEM instance by using the Dispatcher in conjunction with an enterprise-class web server.

>[!NOTE]
>The most common use of Dispatcher is to cache responses from an **AEM publish instance**, to increase the responsiveness and security of your externally facing published website.

Refer to [Dispatcher Overview](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/dispatcher.html) to learn how dispatcher performs caching, returns documents and performs Load Balancing.

### Apache and Dispatcher Configuration and Testing {#dispatcher-configurations-cloud}

You must learn how to structure the AEM as a Cloud Service Apache and Dispatcher configurations, as well as how to validate and run it locally before deploying to Cloud environments.

Refer to [Dispatcher in the Cloud](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/content-delivery/disp-overview.html) for more information.

## AEM Dispatcher Converter {#aem-dispatcher-converter}

AEM Dispatcher Converter provides the capability of refactoring existing on-premise or Adobe Managed Services Dispatcher configurations to AEM as a Cloud Service compatible Dispatcher configuration.

## Using AEM Dispatcher Converter {#using-dispatcher-converter}

* Via Adobe I/O CLI : It is recommended to use the AEM Dispatcher Converter via `aio-cli-plugin-aem-cloud-service-migration` (AEM as a Cloud Service code refactoring plugin for the Adobe I/O CLI).

   Refer to **[Git Resource: aio-cli-plugin-aem-cloud-service-migration](https://github.com/adobe/aio-cli-plugin-aem-cloud-service-migration#introduction)** to learn how to install and use the plugin.

* As a standalone utility : The AEM Dispatcher Converter tool can also be executed as a standalone utility.

   Refer to **[Git Resource: AEM Cloud Service Dispatcher Converter](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/dispatcher-converter)** to learn about the usage and troubleshooting for this tool.

>[!IMPORTANT]
>AEM Dispatcher Converter is developed using NodeJS. It is recommended to have NodeJS 10.0+ installed.
