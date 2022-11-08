---
title: AEM Forms as a Cloud Service - Communications
description: Automatically merge data with XDP and PDF templates or generate output in PCL, ZPL, and PostScript formats
exl-id: 9fa9959e-b4f2-43ac-9015-07f57485699f
---

# Use synchronous processing {#sync-processing-introduction}

Communications allows you to create, assemble, and deliver brand-oriented and personalized communications such as business correspondences, documents, statements, claim processing letters, benefit notices, claim processing letters, monthly bills, and welcome kits. You can use Communications APIs to combine a template (XFA or PDF) with customer data to generate documents in PDF, PS, PCL, DPL, IPL, and ZPL formats.

Consider a scenario where you have one or more templates and multiple records of XML data for each template. You can use Communications APIs to generate a print document for each record. <!-- You can also combine the records into a single document. --> The result is a non-interactive PDF document. A non-interactive PDF document does not let users enter data into its fields.


Communications provide APIs for on-demand and scheduled document generation. You can use synchronous APIs for on-demand and batch APIs (asynchronous APIs) for scheduled document generation:

* Synchronous APIs are suitable for on-demand, low latency, and single record document generation use cases. These APIs are more suitable for user-action based use cases. For example, generating a document after a user fill a form.

* Batch APIs (Asynchronous APIs) are suitable for scheduled high throughput multiple document generation use cases. These APIs generate documents in batches. For example, phone bills, credit card statements, and benefits statements generated every month.

## Use Synchronous operations {#batch-operations}

A synchronous operation is a process of generating documents in a linear manner. Separate APIs are available to:

* Generates a PDF Document from a template and merge data to it.
* Generate a PostScript (PS), Printer Command Language (PCL), Zebra Printing Language (ZPL) document from an XDP file or PDF document.
* Assemble PDF documents
* Disassemble PDF documents
* Convert a document to PDF/A-compliant document
* Validate a PDF/A-compliant document


### Authenticate an API call

Synchronous operations support two type of authentication:

* **Basic authentication**: Basic authentication is a simple authentication scheme built into the HTTP protocol. The client sends HTTP requests with the Authorization header that contains the word Basic followed by a space and a base64-encoded string username:password. For example, to authorize as admin / admin the client sends Basic [base64-encoded string username]: [base64-encoded string password].

* **Token-based authentication:** Token-based authentication uses an access token (Bearer authentication token) to make requests to Experience Manager as a Cloud Service. AEM Forms as a Cloud Service provides APIs to securely retrieve the access token. To retrieve and use the token to authenticate a request:

    1. [Retrieve Experience Manager as a Cloud Service credentials from the Developer Console](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html).
    1. [Install Experience Manager as a Cloud Service credentials on your environment](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html). (Application Server, Web Server, or other non-AEM servers) configured to send requests to (make calls) the cloud service.
    1. [Generate a JWT token and exchanged it with Adobe IMS APIs for an access token](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html).
    1. Run the Experience Manager API with the access token as a Bearer Authentication token.
    1. [Set appropriate permissions for the technical account user in the Experience Manager environment](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html?lang=en#configure-access-in-aem). 

    >[!NOTE]
    >
    >Adobe recommends using token-based authentication on a production environment. 


### (Only for Document Generation APIs) Configure assets and permissions 

To use Synchronous APIs, the following is required: 

* PDF or XDP templates 
* [Data to be merged with templates](#form-data)
* Users with Experience Manager administrator privileges
* Upload templates and other assets to your Experience Manager Forms Cloud Service instance

### (Only for Document Generation APIs) Upload templates and other assets to your Experience Manager instance

An organization typically has multiple templates. For example, one template each for credit card statements, benefits statements, and claim applications. Upload all such XDP and PDF templates to your Experience Manager instance. To upload a template:

1. Open you Experience Manager instance.
1. Go to Forms > Forms and Documents
1. Click Create > Folder and create a folder. Open the folder.
1. Click Create > File Upload and upload the templates.


### Invoke an API

The [API reference documentation](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/) provides detailed information about all the parameters, authentication methods, and various services provided by APIs. The API reference documentation is also provides API defination file in the .yaml format. You can download the .yaml file and upload it to postman to check functionality of the APIs.

>[!VIDEO](https://video.tv.adobe.com/v/335771)

>[!NOTE]
>
>Only members of forms-users group can access Communications APIs.
