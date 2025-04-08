---
title: AEM Dispatcher Converter Tool
description: Learn how to convert existing configurations on AEM Dispatcher to configurations on AEM as a Cloud Service Dispatcher.
exl-id: 2e95ff7b-cc94-477d-99ab-816a58998287
feature: Migration
role: Admin
---
# AEM Dispatcher Converter {#introduction}

>[!CONTEXTUALHELP]
>id="aemcloud_nonbpa_dispconverter"
>title="AEM Dispatcher Converter"
>abstract="Adobe Experience Manager Dispatcher Converter converts existing configurations on AEM Dispatcher to configurations on AEM as a Cloud Service Dispatcher."

Adobe Experience Manager Dispatcher Converter converts existing configurations on AEM Dispatcher to configurations on AEM as a Cloud Service Dispatcher.

## Introduction to Dispatcher {#introduction-dispatcher}

Dispatcher is Adobe Experience Manager's caching, or load-balancing, or both, tool. Using AEM's Dispatcher also helps to protect your AEM server from attack. Therefore, you can increase the security of your AEM instance by using the Dispatcher with an enterprise-class web server.

>[!NOTE]
>The most common use of Dispatcher is to cache responses from an **AEM publish instance**, to increase the responsiveness and security of your externally facing published website.

See [Dispatcher Overview](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/dispatcher.html) to learn how Dispatcher performs caching, returns documents and performs Load Balancing.

### Apache and Dispatcher Configuration and Testing {#dispatcher-configurations-cloud}

Learn how to structure the AEM as a Cloud Service Apache and Dispatcher configurations, and how to validate and run it locally before deploying to Cloud environments.

See [Dispatcher in the Cloud](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/content-delivery/disp-overview.html) for more information.

## AEM Dispatcher Converter {#aem-dispatcher-converter}

AEM Dispatcher Converter provides the capability of refactoring existing on-premise or Adobe Managed Services Dispatcher configurations to AEM as a Cloud Service compatible Dispatcher configuration.

## Using AEM Dispatcher Converter {#using-dispatcher-converter}

* By way of Adobe Developer CLI : Adobe recommends that you use the AEM Dispatcher Converter by way of `aio-cli-plugin-aem-cloud-service-migration` (AEM as a Cloud Service code refactoring plugin for the Adobe Developer CLI).

   See **[Git Resource: aio-cli-plugin-aem-cloud-service-migration](https://github.com/adobe/aio-cli-plugin-aem-cloud-service-migration#introduction)** so you can learn how to install and use the plugin.

* As a standalone utility : The AEM Dispatcher Converter tool can also be run as a standalone utility.

   See **[Git Resource: AEM Cloud Service Dispatcher Converter](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/dispatcher-converter)** so you can learn about the usage and troubleshooting for this tool.

>[!IMPORTANT]
>AEM Dispatcher Converter is developed using NodeJS. Adobe recommends that you have NodeJS 10.0+ installed.
