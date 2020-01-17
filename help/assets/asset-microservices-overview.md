---
title: Know how asset microservices can process your digital assets in the cloud
description: Process your digital assets using cloud-native and scalable asset processing microservices.
contentOwner: AG
---

# Overview of asset ingestion and processing with asset microservices {#asset-microservices-overview}

<!--
First half of content at https://git.corp.adobe.com/aklimets/project-nui/blob/master/docs/Project-Nui-Asset-Compute-Service.md is useful for this article.
TBD: Post-GA we will provide detailed information at \help\assets\asset-microservices-configure-and-use.md. However, for GA, all information is added, in short, in this article.

-->

Adobe Experience Manager as a Cloud Service provides a cloud-native way of leveraging Experience Manager applications and capabilities. One of the key elements of this new architecture is asset ingestion and processing, powered by asset microservices.

Asset microservices provide a scalable and resilient processing of assets using cloud services, which are managed by Adobe for optimal handling of different asset types and processing options. Key benefits are:

* Scalable architecture that allows for seamless processing for resource-intensive operations.
* Efficient indexing and text extractions that does not impact the performance of your Experience Manager environments.
* Minimize the need for workflows to handle asset processing in the Experience Manager environment. This frees up resources, minimizes load on Experience Manager, and provides scalability.
* Improved resilience of asset processing. Potential issues when handling atypical files, such as corrupted files or extremely large files, do not impact the deployment's performance anymore.
* Simplified configuration of asset processing for the administrators.
* Assets processing setup is managed and maintained by Adobe to provide best known configuration for handling renditions, metadata, and text extraction for various file types
* Native Adobe file processing services are used where applicable, providing high-fidelity output and efficient handling of Adobe proprietary formats.
* Ability to configure post-processing workflow to add user-specific actions and integrations.

Asset microservices help to avoid the need for third-party rendering tools (like ImageMagick) and simplify configuration of the system, while providing out-of-the-box functionality for common file types.

## High-level architecture {#asset-microservices-architecture}

A high-level architecture diagram depicts the key elements of asset ingestion and processing and flow of assets across the system.

<!-- Proposed DRAFT diagram for asset microservices overview - see section "Asset processing - high-level diagram" in the PPTX deck

https://adobe-my.sharepoint.com/personal/gklebus_adobe_com/_layouts/15/guestaccess.aspx?guestaccesstoken=jexDC5ZnepXSt6dTPciH66TzckS1BPEfdaZuSgHugL8%3D&docid=2_1ec37f0bd4cc74354b4f481cd420e07fc&rev=1&e=CdgElS
-->

![Asset ingestion and processing with asset microservices](assets/asset-microservices-overview.png "Asset ingestion and processing with asset microservices")

The key steps of the ingestion and processing using asset microservices are:

* Clients, such as web browsers or Adobe Asset Link, send an upload request to Experience Manager and start uploading the binary directly to the binary cloud storage.
* When the direct binary upload completes, the client notifies Experience Manager.
* Experience Manager sends a processing request to asset microservices. The request contents depends on the processing profiles configuration in Experience Manager that specify, which renditions should be generated
* Assets microservices back-end receives the request, dispatches it to one or more microservices based on the request. Each microservice accesses the original binary directly from the binary cloud store.
* Results of the processing, such as renditions, are stored in the binary cloud storage.
* Experience Manager is notified that the processing is complete along with direct pointers to the generated binaries (renditions), which are then available in Experience Manager for the uploaded asset

This is the basic flow of asset ingestion and processing. If configured, Experience Manager can also start customer's workflow model to do post-processing of the asset - e.g., to execute some customized steps that are specific to customer environment, like fetching information from customer's enterprise systems to add to asset properties.

The ingestion and processing flow shows a few key concepts leveraged by the asset microservices architecture for Experience Manager:

* **Direct binary access** - assets are transported (and uploaded) to the Cloud Binary Store once configured for Experience Manager environments, and then AEM, asset microservices, and finally clients get direct access to them to carry out their work. This minimizes the load on networks and duplication of binaries stored
* **Externalized processing** - processing of assets is done outside of AEM environment, and saves its resources (CPU, memory) for providing key Digital Asset Management functionalities and supporting interactive work with the system for end users

## Asset upload with direct binary access {#asset-upload-with-direct-binary-access}

Experience manager clients, which are a part of product offering, all support upload with direct binary access by default. These include upload using web interface, Adobe Asset Link, and AEM desktop app.

You can use custom upload tools, which work directly with AEM HTTP APIs. You can use these APIs directly, or use and extend the following open source projects that implement the upload protocol:

* [Open source upload library](https://github.com/adobe/aem-upload)
* [Open source command-line tool](https://github.com/adobe/aio-cli-plugin-aem)

For more information, see [uploading assets](add-assets.md).

## Add custom asset post-processing {#add-custom-asset-post-processing}

While most customers should get all their asset processing needs from the configurable asset microservices, some might need additional asset processing. This is especially true if assets need to be processed based on information coming from other systems via integrations. In cases like that, custom post-processing workflows can be used.

Post-processing workflows are regular AEM workflow models, created and managed in AEM Workflow editor. Customers can configure the workflows to carry out additional processing steps on an asset, including using available out-of-the-box workflow steps and custom workflows.

Adobe Experience Manager can be configured to automatically trigger the post-processing workflows after asset processing completes.

<!-- TBD asgupta, Engg: Create some asset-microservices-data-flow-diagram.
-->

>[!MORELIKETHIS]
>
>* [Get started using asset microservices](asset-microservices-configure-and-use.md)
>* [Supported file formats](file-format-support.md)
>* [Adobe Asset Link](https://helpx.adobe.com/enterprise/using/adobe-asset-link.html)
>* [AEM desktop app](https://docs.adobe.com/content/help/en/experience-manager-desktop-app/using/introduction.html)
>* [Apache Oak documentation on direct binary access](https://jackrabbit.apache.org/oak/docs/features/direct-binary-access.html)
