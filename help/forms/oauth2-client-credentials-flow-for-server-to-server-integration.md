---
title: How to integrate salesforce integration with AEM Forms using OAuth 2.0 client credential flow?
seo-title: Salesforce integration with AEM Forms using OAuth 2.0 client credential flow
description: Steps to integrate Salesforce integration with AEM Forms using OAuth 2.0 client credential flow
seo-description: Steps to integrate Salesforce integration with AEM Forms using OAuth 2.0 client credential flow
Keywords: Integration of Salesforce using OAuth 2.0 client credential flow, salesforce integration with oauth2 using client credential flow, salesforce and client credential integration
---

# Integration of Salesforce application using OAuth 2.0 client credential flow {#configure-salesforce-with-ouath-2.0-client-credential}

You can use OAuth 2.0 client credentials to integrate AEM Forms with the Salesforce application. OAuth 2.0 client credentials is a standard and secure method for direct communication without user involvement.  


AEM Forms exchanges the client credentials (consumer key and consumer secret), defined in the Salesforce connected application, to obtain an access token.
 
There are multiple benefits of using OAuth 2.0 client credentials for authentication over Authorization Code Flow authentication:

* OAuth 2.0 client credentials authentication allows more five connections per user.
* AEM data source configuration continues working on deactivation, access changes, password update for an AEM user.

## Prerequisites {#prerequisites}

To retrieve and fetch data between Salesforce application and AEM environments requires certain prerequisites:

+++ **Set up a Saleforce connected application with client credential flow and an API-only user**

It is mandatory to create a Salesforce connected app with OAuth 2.0 client credential flow and an API-only user for your organization. For detailed steps, refer to the article [OAuth 2.0 Client Credentials Flow for Server-to-Server Integration](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5). These steps help you obtain the consumer key and consumer secret.

>[!NOTE]
>
> Make sure to note down consumer key and consumer secret as they are required while creating an AEM data source configuration.

+++

+++ **Create a Swagger file**

Swagger is an open-source set of rules, specifications, and tools to develop and describe RESTful APIs. [Create a swagger file](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/forms/integrate-with-salesforce/describe-rest-api.html) before integrating Salesforce with AEM Forms.   

+++

## Configure Salesforce application using OAuth 2.0 Client Credential flow {#steps-to-create-aem-datasource-configuration}

To integrate Salesforce application with an Adaptive Form using OAuth 2.0 client credential authentication settings, perform following steps:

1. Log in to your Author instance.
1. Go to **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** > **[!UICONTROL Data Sources]**.
1. Select the configuration folder.
1. Click **[!UICONTROL Create]** and the **[!UICONTROL Create Data Source Configuration]** appears.
1. Specify the **[!UICONTROL Title]** and select the **[!UICONTROL Service Type]** as **[!UICONTROL RESTful Service]**.
1. Click **[!UICONTROL Next]**.
1. Select the **[!UICONTROL Swagger Source]** as **[!UICONTROL File].** 
    >[!NOTE]
    >
    > As soon as the swagger file is selected, the Scheme, the Host name and the Base path are populated automatically.

1. Upload the created swagger file from your local machine by clicking **[!UICONTROL Browse]**.
1. Select the **[!UICONTROL Authentication Type]** as **[!UICONTROL OAuth 2.0]** and the **[!UICONTROL Authentication Settings]** panel appears.
1. Select the **[!UICONTROL Grant Type]** as **[!UICONTROL Client Credential]**.
1. Specify the **[!UICONTROL Client Id]** and **[!UICONTROL Client Secret]** obtained from the Salesforce connected app.
1. Specify the **[!UICONTROL Access Token URL]** in format 
`https://[MyDomainName].my.salesforce.com/services/oauth2/token`.

    >[!NOTE]
    >
    > Each organization has its own specific domain name. 

1. Click **[!UICONTROL Test Connection]**.
1. If the connection succeeds, click the **[!UICONTROL Create]** button.

Now, you can [create the Form Data Model](/help/forms/create-form-data-models.md) to integrate the configured datasource with your Adaptive Form.
