---
title: How to use Forms as a Cloud Service to merge data with XDP and PDF templates or generate output in PCL, ZPL, and PostScript formats?
description: Automatically merge data with XDP and PDF templates or generate output in PCL, ZPL, and PostScript formats
exl-id: 9fa9959e-b4f2-43ac-9015-07f57485699f
feature: "Adaptive Forms,APIs & Integrations"
role: Admin, Developer, User
---

# Use synchronous processing {#sync-processing-introduction}

Forms as a Cloud Service - Communications APIs lets you create, assemble, and deliver brand-oriented and personalized communications such as business correspondences, documents, statements, claim processing letters, benefit notices, claim processing letters, monthly bills, and welcome kits. You can use Communications APIs to combine a template (XFA or PDF) with customer data to generate documents in PDF, PS, PCL, DPL, IPL, and ZPL formats.

Consider a scenario where you have one or more templates and multiple records of XML data for each template. You can use Communications APIs to generate a print document for each record. <!-- You can also combine the records into a single document. --> The result is a non-interactive PDF document. A non-interactive PDF document does not let users enter data into its fields.

Forms as a Cloud Service - Communications provides on-demand and batch APIs (asynchronous APIs) for scheduled document generation:

* Synchronous APIs are suitable for on-demand, low latency, and single record document generation use cases. These APIs are more suitable for user-action based use cases. For example, generating a document after a user fill a form.

* Batch APIs (Asynchronous APIs) are suitable for scheduled high throughput multiple document generation use cases. These APIs generate documents in batches. For example, phone bills, credit card statements, and benefits statements generated every month.

## Use Synchronous operations {#batch-operations}

A synchronous operation is a process of generating documents in a linear manner. These APIs are classified as single-tenant APIs and multi-tenant APIs:

### Single-tenant APIs

* Document generation APIs
* Document manipulation APIs

<!-- 
### Multi-tenant APIs

* Document utility APIs -->


### Authenticate a single-tenant API

Single-tenant API operations support two type of authentication:

* **Basic authentication**: Basic authentication is a simple authentication scheme built into the HTTP protocol. The client sends HTTP requests with the Authorization header that contains the word Basic followed by a space and a base64-encoded string username:password. For example, to authorize as admin / admin the client sends Basic [base64-encoded string username]: [base64-encoded string password].

* **Token-based authentication:** Token-based authentication uses an access token (Bearer authentication token) to make requests to Experience Manager as a Cloud Service. AEM Forms as a Cloud Service provides APIs to securely retrieve the access token. To retrieve and use the token to authenticate a request:

    1. [Retrieve Experience Manager as a Cloud Service credential from the Developer Console](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html).
    1. [Install Experience Manager as a Cloud Service credential on your environment](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html). (Application Server, Web Server, or other non-AEM servers) configured to send requests to (make calls) the cloud service.
    1. [Generate a JWT token and exchanged it with Adobe IMS APIs for an access token](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html).
    1. Run the Experience Manager API with the access token as a Bearer Authentication token.
    1. [Set appropriate permissions for the technical account user in the Experience Manager environment](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html?lang=en#configure-access-in-aem).

    >[!NOTE]
    >
    >Adobe recommends using token-based authentication on a production environment.

<!-- 

### Authenticate a multi-tenant API

#### Authentication Headers

Every inbound HTTP API call to the multi-tenant API must contain these three headers:


* `x-api-key`
* `x-gw-ims-org-id`
* `Authorization`

The values which should be sent in the `x-api-key` and `x-gw-ims-org-id` headers are provided in the Credentials details screen in the [Adobe Developer Console](https://developer.adobe.com/console). The value of the `x-api-key` header is the Client ID and the value for the `x-gw-ims-org-id` header is the Organization ID.

#### Configure Adobe Developer console to generate an access token

To set up authentication APIs, create a project in Adobe Developer Console and add Communication APIs to the project on Adobe Developer Console. The integration generates API Key, Client Secret, Payload (JWT):

1. Contact you Adobe Developer Console administrator. Ask the administrator to add as a developer.
1. Log in to `https://developer.adobe.com/console/`. Use your developer account that your administrator has provisioned to log in to Adobe Developer Console.
1. Select your organization from the top-right corner. If you do not know your organization, contact your administrator.
1. Select **[!UICONTROL Create new project]**. A screen to get started with your new project appears. Select **[!UICONTROL Add API]**. A screen with list of all the APIs enabled for your account appears.
1. Select **[!UICONTROL AEM Forms - Communications]** and select **[!UICONTROL Next]**. A screen to configure the API appears.
1. Select **[!UICONTROL OPTION 1 Generate a key pair]** and select **[!UICONTROL Generate keypair]**. It creates and downloads the configuration file. The downloaded configuration file contains all your app settings, along with the only copy of your private key. Adobe does not record your private key, make sure to securely store the downloaded file. Select **[!UICONTROL Next]**.
1. Select **[!UICONTROL Integrations - Cloud Service]** and select **[!UICONTROL Save configured API]**. Select **[!UICONTROL Service Account (JWT)]** to view the API Key, Client Secret, and other information required to access the APIs. You set to use the token to access the APIs.

#### Programmatically generate and use an access token

To programmatically generate an access token, generate a JSON Web Token (JWT) and exchange it with the Adobe Identity Management Service (IMS) for an access token.

Use the following keys, referred to as claims, to construct JWT JSON object:


* `exp`- the requested expiration of the access token, expressed as several seconds since January 1, 1970 GMT. For most use cases, this is a relatively small value. For example, 5 minutes, for five minutes from now, this value should be 1670923791.
* `iss` - the Organization ID from the Adobe Developer Console project, in the format org_ident@AdobeOrg.
* `sub` - the Technical Account ID from the Adobe Developer Console integration, in the format: id@techacct.adobe.com.
* `aud` - the Client ID from the Adobe Developer Console integration prepended with `https://ims-na1.adobelogin.com/c/`.
* `https://ims-na1-stg1.adobelogin.com/s/ent_aemforms_docprocessing` - set to the literal value `true`

This JSON object must be then base64 encoded and signed using the private key for the project. Finally, the encoded value is sent in the body of a POST request to `https://ims-na1.adobelogin.com/ims/exchange/jwt` along with the Client ID and Client Secret for the project.

##### Example

```JSON

    ========================= REQUEST ==========================
    POST https://ims-na1.adobelogin.com/ims/exchange/jwt
    -------------------------- body ----------------------------
    client_id={myClientId}&client_secret={myClientSecret}&jwt_token={myJSONWebToken}
    ------------------------- headers --------------------------
    Content-Type: application/x-www-form-urlencoded
    Cache-Control: no-cache

```

#### Language Support for JWT

While it is possible to do the entire JWT generation and exchange process in custom code, it is more common to use a higher-level library to do so. A number of such libraries are listed on the [Adobe I/O JWT Documentation](https://developer.adobe.com/developer-console/docs/guides/authentication/JWT/).

-->

### (Only for Document Generation APIs) Configure assets and permissions

To use Synchronous APIs, the following is required:

* Users with Experience Manager administrator privileges
* Upload templates and other assets to your Experience Manager Forms Cloud Service instance

### (Only for Document Generation APIs) Upload templates and other assets to your Experience Manager instance

An organization typically has multiple templates. For example, one template each for credit card statements, benefits statements, and claim applications. Upload all such XDP and PDF templates to your Experience Manager instance. To upload a template:

1. Open you Experience Manager instance.
1. Go to Forms > Forms and Documents
1. Click Create > Folder and create a folder. Open the folder.
1. Click Create > File Upload and upload the templates.

### Invoke an API

The [API reference documentation](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/) provides detailed information about all the parameters, authentication methods, and various services provided by APIs. The API reference documentation also provides API definition file in the .yaml format. You can download the .yaml file and upload it to [Postman](https://www.postman.com/) to check functionality of the APIs.

>[!VIDEO](https://video.tv.adobe.com/v/335771)

>[!NOTE]
>
>Only members of forms-users group can access Communications APIs.

>[!MORELIKETHIS]
>
>* [Introduction to AEM Forms as a Cloud Service Communications](/help/forms/aem-forms-cloud-service-communications-introduction.md)
>* [AEM Forms as a Cloud Service Architecture for Adaptive Forms and Communication APIs](/help/forms/aem-forms-cloud-service-architecture.md)
>* [Communication Processing - Synchronous APIs](/help/forms/aem-forms-cloud-service-communications.md)
>* [Communication Processing - Batch APIs](/help/forms/aem-forms-cloud-service-communications-batch-processing.md)