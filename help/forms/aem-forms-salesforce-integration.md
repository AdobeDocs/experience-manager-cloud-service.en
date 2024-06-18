---
title: How to integrate Salesforce using OAuth 2.0 client credential flow with AEM Forms?
description: Learn to integrate Salesforce with AEM Forms using OAuth 2.0 client credential flow. It displays steps for AEM Forms Salesforce integration.
Keywords: Integration of Salesforce using OAuth 2.0 client credential flow, salesforce integration with oauth2 using client credential flow, salesforce and client credential integration, AEM Forms Salesforce integration
feature: Adaptive Forms, Form Data Model
role: User, Developer
exl-id: 2c2029ab-6fb4-41a6-846c-175c3a79d921
---
# Integrate Adaptive Form with Salesforce {#configure-salesforce-with-ouath-2.0-client-credential}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/form-data-model/oauth2-client-credentials-flow-for-server-to-server-integration.html)                  |
| AEM as a Cloud Service     | This article         |

Adobe Experience Manager (AEM) Forms integration with Salesforce allows organizations to streamline processes by connecting their form creation and management capabilities with the Salesforce platform. Connecting an Adaptive Form with Salesforce enables seamless data exchange between the two platforms. When users submit forms, the data is synchronized with Salesforce automatically. It ensures that all customer information is up-to-date and centralized within the system.

You can use OAuth 2.0 client credentials to integrate AEM Forms with the Salesforce application. OAuth 2.0 client credentials are a standard and secure method for direct communication without user involvement.  

![Workflow while setting communication between AEM Forms and Salesforce application](/help/forms/assets/salesforce-workflow.png)

AEM Forms exchanges the client credentials (consumer key and consumer secret), defined in the Salesforce connected application, to obtain an access token.

AEM as a Cloud Service offers various out of the box submit actions for handling form submissions. You can learn more about these options in the [Adaptive Form Submit Action](/help/forms/configure-submit-actions-core-components.md) article.
 
There are multiple benefits of using OAuth 2.0 client credentials for authentication over Authorization Code Flow authentication:

* OAuth 2.0 client credentials authentication allows more than five connections per user.
* AEM data source configuration continues working on deactivation, access changes, password update for an AEM user.

## Prerequisites {#prerequisites}

Before setting communication between a Salesforce application and an AEM environment:

* Create a [Salesforce connected app with OAuth 2.0 client credential flow](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5) and an API-only user for your organization and obtain the consumer key and consumer secret for the app.

* Ensure that your Swagger file is appropriately configured to match your organization's APIs. Alternatively, you can opt to [create a Swagger file](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/forms/integrate-with-salesforce/describe-rest-api.html) from the scratch, tailored for utilization in your AEM environment.


## Configure Salesforce application using OAuth 2.0 Client Credential flow {#steps-to-create-aem-datasource-configuration}

To connect Adaptive Form to  Salesforce application using OAuth 2.0 client credential authentication settings, perform following steps:

1. Log in to your Author instance.
1. Go to **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** > **[!UICONTROL Data Sources]**.
1. Select the configuration folder.
1. Click **[!UICONTROL Create]** and the **[!UICONTROL Create Data Source Configuration]** appears.
1. Specify the **[!UICONTROL Title]** and select the **[!UICONTROL Service Type]** as **[!UICONTROL RESTful Service]**.
1. Click **[!UICONTROL Next]**.
1. Select the **[!UICONTROL Swagger Source]** as **[!UICONTROL File].** 

    >[!NOTE]
    >
    > When the swagger file is selected, the Scheme, the Host name and the Base path are populated automatically.

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


After configuring the Salesforce application, you can use the configuration while creating form data model (FDM). For more information, see [Create form data model (FDM)](create-form-data-models.md). [Configure the Form Data Model Submit Action](/help/forms/using-form-data-model.md) for an Adaptive Form to send data to Salesforce applications.

For more information about creating and using Form Data Model (FDM) in business workflows, see [Data Integration](data-integration.md).

## Related Articles

{{af-submit-action}}


