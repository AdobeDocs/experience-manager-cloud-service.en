---
title: Introduction to Adobe Experience Manager as a Cloud Service - Terminology
description: Introduction to Adobe Experience Manager as a Cloud Service - Terminology.
exl-id: a76f68f1-4f84-4844-a099-0952707cd96d
---
# Adobe Experience Manager as a Cloud Service - Terminology {#adobe-experience-manager-as-a-cloud-service-terminology}

The following terms are used in relation to Adobe Experience Manager (AEM) as a Cloud Service:

## Products {#products}

|Product|Description|
|---|---|
|AEM as a Cloud Service|The cloud-native way of leveraging the AEM applications|
|AEM Assets as a Cloud Service| Digital Asset Management (DAM) capabilities as cloud-native, scalable solution, to ingest, process, and manage your digital assets, while integrating with the wider Adobe Experience Cloud and Adobe Creative Cloud ecosystem. |
|AEM Sites as a Cloud Service|An instance of the AEM as a Cloud Service with the AEM Sites application.|

## Instances and Pipelines {#instances-and-pipelines}

|Instance|Desription|
|---|---|
|Adobe Pipeline|The mechanism for publishing content from author to publish.|
|AEM Author Tier|Describes the authoring environment for Sites and Assets.|
|AEM Preview Tier|Describes the preview environment for Sites.|
|AEM Publish Tier|Describes the publishing environment for Sites.|


<!-- This section of the table must be alphabetic -->

## Terminology {#terminology}

|Term|Description|
|---|---|
|AEM Image|A deployable artifact that contains the AEM product code together with the customer code.|
| Asset microservices | Cloud-based digital asset processing services that cater to various asset processing use cases, such as rendition generation, PDF processions, subasset handling, text extraction, and so on. See [asset microservices overview](/help/assets/asset-microservices-overview.md), for more information. |
|Cloud Manager Git Repository|Where customers store their code and configuration settings.|
|Cloud Provider|AEM as a Cloud Service currently supports Azure. AWS support is a roadmap item.|
|Content Delivery Network (CDN)|AEM as Cloud Service is shipped with a default CDN. Its main purpose is to reduce latency by delivering cacheable content from the CDN nodes at the edge, near the browser. It is fully managed and configured for optimal performance of AEM applications.|
|Content Repository|Where the content is persisted.|
|Enterprise Isolation|Each instance of the AEM as a Cloud service is isolated from the other instances.|
|Golden Master|The AEM publish tier.|
|Orchestration Engine|AEM as a Cloud Service uses an orchestration engine to ensure that all author and publish services are scaling as and when needed.|
