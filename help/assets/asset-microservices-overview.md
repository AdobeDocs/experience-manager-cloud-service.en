---
title: Know how asset microservices can process your digital assets in the cloud
description: Process your digital assets using cloud-native and scalable asset processing microservices.
cloud: experience-cloud
solution-title: Experience Cloud
product: Adobe Experience Manager Cloud Service
sub-product: Adobe Experience Manager Cloud Service

---

# Overview of asset ingestion and processing with asset microservices {#asset-microservices-overview}

<!--
First half of content at https://git.corp.adobe.com/aklimets/project-nui/blob/master/docs/Project-Nui-Asset-Compute-Service.md is useful for this article.
-->

Adobe Experience Manager as a Cloud Service provides a cloud-native way of levering AEM applications and capabilities. One of the key elements of this new architecture is asset ingestion and processing, powered by Asset Microservices.

Asset microservices provide a scalable and resilient processing of assets using cloud services, which are managed by Adobe for optimal handling of different asset types. Key benefits include:

* Scalable architecture that allows for resource-intensive asset processing
* Efficient indexing and text extractions that does not impact the performance of your AEM environments.
* Minimize the need for workflows to handle asset processing in the AEM environment, freeing up resources and minimizing load on AEM
* Improved resilience of asset processing, as potential issues handling problematic files (e.g., corrupted files, extremely large ones) won't impact the AEM environment
* Simplified configuration of asset processing for the administrator in AEM Tools UI
* Assets processing setup managed and maintained by Adobe to provide best known configuration for handling renditions, metadata, and text extraction for various file types
* Native Adobe file processing services are used where applicable, providing high-fidelity output
* Ability to configure post-processing workflow to add customer-specific actions and integrations

Asset microservices help to avoid the need for third-party rendering tools (like ImageMagick), and greatly simplify configuration of the system, while providing good results for common file types out of the box.

## High-level architecture

A high-level architecture diagram depicts the key elements of asset ingestion and processing.

<!-- Proposed DRAFT diagram for asset microservices overview - see section "Asset processing - high-level diagram" in the PPTX deck

https://adobe-my.sharepoint.com/personal/gklebus_adobe_com/_layouts/15/guestaccess.aspx?guestaccesstoken=jexDC5ZnepXSt6dTPciH66TzckS1BPEfdaZuSgHugL8%3D&docid=2_1ec37f0bd4cc74354b4f481cd420e07fc&rev=1&e=CdgElS
-->
![Asset ingestion and processing with asset microservices](assets/asset-microservices-overview.png)

Key steps of the ingestion and processing using asset microservices include:

* Clients (e.g, web browser, desktop clients like Adobe Asset Link) send an upload request to AEM and start uploading the binary directly to the binary cloud storage. 
* When the direct binary upload completes, the client notifies AEM
* AEM sends a request for procesing the assets to asset microservices. The request content depends on Processing Profiles configuration in AEM that specify, which renditions should be generated
* Assets microservices backend receives the request, dispatches it to one or more  microservices based on the request. Each microservice can access the original binary directly from the binary cloud store
* Results of the processing (like renditions) are stored in the Binary Cloud Storage
* AEM is notified that the processing is complete along with direct pointers to the generated binaries (renditions), which are then available in AEM for the uploaded asset

This is the basic flow of asset ingestion and processing. If configured, AEM can also start customer's workflow model to do post-processing of the asset - e.g., to execute some customized steps that are specific to customer envrionment, like fetching information from customer's enterprise systems to add to asset properties.

The ingestion and processing flow shows a few key concepts leveraged by the asset microservices architecture for AEM:

* **Direct binary access** - assets are transported (and uploaded) to the Cloud Binary Store once configured for AEM environments, and then AEM, asset microservices, and finally clients get direct access to them to carry out their work. This minimizes the load on networks and duplication of binaries stored
* **Externalized processing** - processing of assets is done outside of AEM environment, and saves its resources (CPU, memory) for providing key Digital Asset Management functionalities and supporting interactive work with the system for end users

## Asset upload with direct binary access

Experience manager clients, which are a part of product offerinng, all support upload with direct binary access by default. These include upload using web UI, Adobe Asset Link, AEM desktop app.

Customers can also use custom upload tools, which work directly with AEM HTTP APIs. They can use these APIs directly, or use and extend the following open source projects implementing the upload protocol:

* [Open source upload library](https://github.com/adobe/aem-upload)
* [Open source command-line tool](https://github.com/adobe/aio-cli-plugin-aem)

For more information, see [uploading assets](add-assets.md).

## Adding custom asset post-processing

While most customers should get all their asset processing needs from the configurable asset microservices, some might need additional asset processing. This is especially true if assets need to be processed based on information coming from other systems via integrations. In cases like that, custom post-processing workflows can be used.

Post-processing workflows are regular AEM workflow models, created and managed in AEM Workflow editor. Customers can configure the workflows to carry out additional processing steps on an asset, including using avaialble out of the box workflow steps, as well as custom-built ones.

Experience manager can then be configured to start these post-processing workflows. They are executed automatically after the main asset processing finishes.

For more details, see [Get started using asset microservices](asset-microservices-configure-and-use.md).

<!-- GK: The diagram below is way too technical and uses internal project names. -->
<!--
![Data flow diagram for asset microservices](assets/asset-microservices-data-flow-diagram.png)
*Figure: Data flow diagram for asset microservices*
-->

>[!MORELIKETHIS]
>
>[Supported file formats](file-format-support.md)
