---
title: Effortless Bulk PDF Creation - Master the Art with Batch Processing – Your Self-Help Guide to Generating Millions of PDF Documents!
description: How to create brand-oriented and personalized communications?
feature: Adaptive Forms, APIs & Integrations
role: Admin, Developer, User
exl-id: 542c8480-c1a7-492e-9265-11cb0288ce98
---
# AEM Forms as a Cloud Service Communications Batch Processing

Communications lets you create, assemble, and deliver brand-oriented and personalized communications such as business correspondences, documents, statements, claim processing letters, benefit notices, monthly bills, and welcome kits. You can use Communications APIs to combine a template (XFA or PDF) with customer data to generate documents in PDF, PS, PCL, DPL, IPL, and ZPL formats.

Communications provide APIs for on-demand and scheduled document generation. You can use synchronous APIs for on-demand and batch APIs (asynchronous APIs) for scheduled document generation:

* Synchronous APIs are suitable for on-demand, low latency, and single record document generation use cases. These APIs are more suitable for user-action based use cases. For example, generating a document after a user fill a form. 

* Batch APIs (Asynchronous APIs) are suitable for scheduled high throughput multiple document generation use cases. These APIs generate documents in batches. For example, phone bills, credit card statements, and benefits statements generated every month.

<!-- The following skills are required to create templates and use HTTP APIs: 

* Understanding of Adobe Forms Designer or Acrobat Forms to create templates

* Understanding of HTTP APIs and experience of using HTTP APIs

* Basic understanding of Adobe Experience Manager -->


## Batch operations {#batch-operations}

A batch operation is a process of generating multiple documents of similar type for a set of records at scheduled intervals. A batch operation has two parts: Configuration (definition) and execution. 

* **Configuration (definition)**: A batch configuration stores information about various assets and properties to set for generated documents. For example, it provides details about the XDP or PDF template and location of customer data to use along with specifying various properties for output documents.

* **Execution**: To start a batch operation, pass the batch configuration name to batch execution API.

### Components of a batch operation {#components-of-a-batch-operations}

**Cloud configuration**: Experience Manger Cloud configuration helps you connect an Experience Manager instance to customer owned Microsoft Azure Storage. It lets you specify the credentials for customer owned Microsoft Azure account to connect to it.

**Batch Data Store configuration (USC)**: Batch data configuration helps you configure a specific instance of Blob storage for Batch APIs. It lets you specify the input and output locations in customer owned Microsoft Azure Blob storage.

**Batch APIs**: Lets you create a batch configurations and execute the batch runs based on these configurations to merge a PDF or XDP template with data and generate output in PDF, PS, PCL, DPL, IPL and ZPL formats. Communications provide batch APIs for configuration management and batch execution.  

![data-merge-table](assets/communications-batch-structure.png)

**Storage**: Communication APIs use customer owned Microsoft Azure Cloud storage to fetch customer records and store generated documents. You configure Microsoft Azure Storage in Experience Manager Cloud Service Configuration.

**App**: Your custom application to use the Batch APIs to generate and consume documents.

## Generate multiple documents using batch operations {#generate-multiple-documents-using-batch-operations}

You can use batch operations to generate multiple documents at scheduled intervals.

>[!VIDEO](https://video.tv.adobe.com/v/338349)

You can watch the video or perform the instructions below to learn how to generate documents using batch operations. The API reference documentation used in video is available in the .yaml format. You can download the [Batch APIs](assets/batch-api.yaml) file and upload it to Postman to check functionality of APIs and follow along the video.

### Pre-requisites {#pre-requisites}

To use Batch API, the following is required: 

* [Microsoft Azure Storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create)
* PDF or XDP templates 
* [Data to be merged with templates](#form-data)
* Users with Experience Manager administrator privileges

### Set up your environment {#setup-your-environment}

Before using a batch operation:

* Upload customer data (XML files) to Microsoft Azure Blob Storage
* Create a Cloud configuration
* Create Batch Data Store configuration
* Upload templates and other assets to your Experience Manager Forms Cloud Service instance

### Upload customer data (XML files) to Azure Storage {#upload-customer-data-to-Azure-Storage}

On your Microsoft Azure Storage, create [containers](https://docs.microsoft.com/en-us/azure/vs-azure-tools-storage-explorer-blobs) and [upload customer data (XML)](https://docs.microsoft.com/en-us/azure/vs-azure-tools-storage-explorer-blobs#managing-blobs-in-a-blob-container) to the [folders](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal) inside the containers.  

>[!NOTE]
>
>You can configure Microsoft Azure storage to automatically clean input folder or move content of output folder to a different location at scheduled intervals. However, ensure that folders are not cleaned when a batch operation referencing the folders is still running.

### Create a Cloud configuration {#create-a-cloud-configuration}

The Cloud configuration connects your Experience Manager instance to Microsoft Azure Storage. To create a Cloud configuration:

1. Go to Tools > Cloud Services > Azure Storage
1. Open a folder to host the configuration and click Create. You use the Global folder or create a folder.
1. Specify name of the configuration and credentials to connect to the service. You can [retrieve these credentials from your Microsoft Azure Storage portal](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal#view-account-access-keys).  
1. Click Create.

Your Experience Manager instance is now ready to connect to Microsoft Azure Storage and use it to store and read content, when required.

### Create Batch Data Store configuration {#create-batch-data-store-configuration}

Batch data configuration helps you configure containers and folders for input and output. You keep your customer records in Source Folder and generated documents are placed in the Destination Folder.

To create the configuration:

1. Go to Tools > Forms > Unified Storage Connector.
1. Open a folder to host the configuration and click Create. You use the Global folder or create a folder.
1. Specify Title and Name of the configuration. In Storage select Microsoft Azure Storage.
1. In Storage Configuration Path, browse and select the Cloud Configuration which contains credentials of customer-owned Azure storage account.  
1. In the Source Folder, specify name of Azure Storage container and folder containing records.
1. In the Destination Folder, specify path of Azure Storage container and folder to store the generated documents.
1. Click Create.

Your Experience Manager instance is now connected to Microsoft Azure Storage and configured to retrieve and send data to specific locations on Microsoft Azure Storage.

### Upload templates and other assets to your Experience Manager instance {#upload-templates-and-other-assets-to-your-AEM-instance}

An organization typically has multiple templates. For example, one template each for credit card statements, benefits statements, and claim applications. Upload all such XDP and PDF templates to your Experience Manager instance. To upload a template:

1. Open you Experience Manager instance. 
1. Go to Forms > Forms and Documents 
1. Click Create > Folder and create a folder. Open the folder.
1. Click Create > File Upload and upload the templates.

## Use batch API to generate documents {#use-batch-API-to-generate-documents}

To use a batch API, create a batch configuration and execute a run based on that configuration. The API documentation provides information about APIs to create and run a batch, corresponding parameters, and possible errors. You can download the [API definition file](assets/batch-api.yaml) file and upload it to [Postman](https://go.postman.co/home) or similar software to test the APIs to create and run a batch operation.

### Create a batch {#create-a-batch}

To create a batch, use the `POST /config` API. Include the following mandatory properties in the body of the HTTP request:

* **configName**: Specify Unique name of the batch. For example, `wknd-job`
* **dataSourceConfigUri**: Specify location of the Batch Data Store configuration. It can be relative or absolute path of the configuration. For example: `/conf/global/settings/forms/usc/batch/wknd-batch`
* **outputTypes**: Specify output formats: PDF and PRINT. If you use the PRINT output type, in `printedOutputOptionsList` property, specify at least one print options. The print options are identified by their render type, so at present multiple print options with the same render type are not allowed. The supported formats are PS, PCL, DPL, IPL and ZPL. 

* **template**: Specify absolute or relative path of the template. For example, `crx:///content/dam/formsanddocuments/wknd/statements.xdp`

If you specify relative path, also provide a content root. See, API documentation for details of content root. 

<!-- For example, you include the following JSON in the body of HTTP APIs to create a batch named wknd-job: -->

You can use `GET /config /[configName]` to see details of the batch configuration.

### Run a batch {#run-a-batch}

To run (execute) a batch, use the `POST /config /[configName]/execution`. For example, to run a batch named wknd-demo, use /config/wknd-demo/execution. The server returns HTTP response code 202 on accepting the request. The API does not return any payload except a unique code (execution-identifier) in header of HTTP response for the batch job running on the server. You can use the execution-identifier to retrieve the status of the batch.

>[!NOTE]
>
>While the batch is running, do not make any changes to corresponding source and destination folders, data source configuration, and Microsoft Azure Cloud configuration.

### Check status of a batch {#status-of-a-batch}

To retrieve status of a batch, use the `GET /config /[configName]/execution/[execution-identifier]`. The execution-identifier is included in the header of HTTP response for the batch execution request. 

The response of the status request contains the status section. It provides details about status of the batch job, number of records already in pipeline (already read and being processed), and status of each outputType/renderType(number of in-progress, succeeded, and failed items). Status also includes start and end time of batch job along with information about errors, if any. The end time is -1 until batch run actually completes.

>[!NOTE]
>
>* When you request multiple PRINT formats, the status contains multiple entries. For example, PRINT/ZPL, PRINT/IPL. 
>* A batch job does not read all the records simultaneously, rather the job keeps reading and incrementing the number of records. So, the status returns -1 until all the records have been read.

### View generated documents {#view-generated-documents}

On completion of job, the generated documents are stored to the `success` folder at the destination location specified in the Batch Data Store configuration. If there are any errors, the service creates a `failure` folder. It provides information about the type and reason of errors. 

Let's understand with the help of an example: Assume there is an input data file `record1.xml` and two output types: `PDF` and `PCL`. Then the destination location contains two sub-folders `pdf` and `pcl`, one for each of the output types. Lets assume PDF generation succeeded, then the `pdf` sub-folder contains the `success` sub-folder which in turn contains the actual generated PDF document `record1.pdf`. Lets assume PCL generation failed, then the `pcl` sub-folder contains a `failure` sub-folder which in turn contains an error file `record1.error.txt` which contains details of the error. Also, the destination location  contains a temporary folder called `__tmp__` which holds certain files required during batch execution. This folder can be deleted when there are no active batch runs referencing the destination folder.

>[!NOTE]
>
>Processing a batch can take some time depending on the number of input records and complexity of the template, wait for a few minutes before checking destination folders for output files.

## API reference documentation

The API reference documentation provides detailed information about all the parameters, authentication methods, and various services provided by APIs. The API reference documentation is available in the .yaml format. You can download the [Batch APIs](assets/batch-api.yaml) file and upload it to Postman to check functionality of APIs.

>[!MORELIKETHIS]
>
>* [Introduction to AEM Forms as a Cloud Service Communications](/help/forms/aem-forms-cloud-service-communications-introduction.md)
>* [AEM Forms as a Cloud Service Architecture for Adaptive Forms and Communication APIs](/help/forms/aem-forms-cloud-service-architecture.md)
>* [Communication Processing - Synchronous APIs](/help/forms/aem-forms-cloud-service-communications.md)
>* [Communication Processing - Batch APIs](/help/forms/aem-forms-cloud-service-communications-batch-processing.md)