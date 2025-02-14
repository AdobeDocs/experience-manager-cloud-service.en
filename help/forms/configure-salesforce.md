---
title: How to configure Salesforce out of the box form data models for Adaptive Forms?
description: Learn how to integrate Salesforce with Adaptive Forms.
feature: Adaptive Forms, Form Data Model
role: User, Developer
exl-id: 184db05b-7237-4dce-8059-03c39b93d7d7
---
# Configure Salesforce for AEM Forms {#configure-azure-storage}

[[!DNL Experience Manager Forms] Data Integration](data-integration.md) provides [!DNL Salesforce] Cloud Services to integrate Adaptive Forms with OOTB Form Data Model (FDM). The Adaptive Forms can then interact with [!DNL Salesforce] servers to enable business workflows. For example:

* Write data into [!DNL Salesforce] on Adaptive Form submission.
* Write data in [!DNL Salesforce] through custom entities defined in Form Data Model (FDM) and conversely.
* Query [!DNL Salesforce] server for data and prepopulate Adaptive Forms.
* Read data from [!DNL Salesforce] server.

[!DNL Salesforce] cloud services and Form Data Model (FDM) are available out of the box on the [!DNL AEM Forms] Server after you [set up a development project for Forms based on Experience Manager archetype](setup-local-development-environment.md#forms-cloud-service-local-development-environment).

>[!NOTE]
>
>[!DNL Salesforce] cloud services and Form Data Model (FDM) are available out of the box only if you set up an [!DNL Experience Manager Forms] as a [!DNL Cloud Service] project based on [AEM Archetype 30](https://github.com/adobe/aem-project-archetype/releases/tag/aem-project-archetype-30) or later.

## Configure [!DNL Salesforce] cloud service {#configure-salesforce-cloud-service}

Before configuring the [!DNL Salesforce] cloud services, ensure that you perform the following tasks:

* [Create a connected OAuth-enabled [!DNL Salesforce] application](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_api_integration.htm&type=5). When you are creating the connected [!DNL Salesforce] application, specify the callback URL in the following format:

   ```
   https://'[server]:[port]'/libs/fd/fdm/gui/components/admin/fdmcloudservice/createcloudconfigwizard/cloudservices.html
   ```

   Where server and port refer to the hostname and port number for the [!DNL AEM Forms] Server. 

* While creating the connected [!DNL Salesforce] application, specify `full` and `offline_access` as the values for the OAuth scope.

* Take a note of the values for the client ID (referred to as Consumer Key) and client secret (referred to as Consumer Secret) for the connected application.

Perform the following steps to configure the [!DNL Salesforce] cloud service:

1. On [!DNL AEM Forms] author instance, navigate to **[!UICONTROL Tools]** ![hammer](assets/hammer.png) &gt; **[!UICONTROL Cloud Services]** &gt; **[!UICONTROL Data Sources]**. 
2. Select the folder name, select **[!UICONTROL Salesforce Cloud Config]**, and select **[!UICONTROL Properties]**.
3. In the **[!UICONTROL Authentication Settings]** tab:
   1. Specify the [!DNL Salesforce] Domain URL in the **[!UICONTROL Host]** field. For example, [Domain-name].my.salesforce.com.
   2. Specify the client ID (referred to as Consumer Key) and client secret (referred to as Consumer Secret) for the connected application.
   3. Specify **full offline_access** (`full` and `offine_access` values separated by a space) in the **[!UICONTROL Authorization Scope]** field.
   4. Select **[!UICONTROL Connect to OAuth]**. You are redirected to [!DNL Salesforce] login page.
   5. Log in with your [!DNL Salesforce] credentials and accept to allow the cloud service configuration to connect to [!DNL Salesforce] service. If the connection is successful, you are redirected to the [!DNL Salesforce] cloud service configuration page, which displays a success message.
4. Select **[!UICONTROL Save & Close]** to complete the configuration setup.

### Access out of the box [!DNL Salesforce] Form Data Model (FDM)

A [!DNL Salesforce] Form Data Model (FDM) is available out of the box on the [!DNL AEM Forms] Server after you [set up a development project for Forms based on Experience Manager archetype](setup-local-development-environment.md#forms-cloud-service-local-development-environment).

To access the Form Data Model (FDM):
1. Navigate to **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Data Integrations]**.  
1. Select the folder name, select the **[!UICONTROL Salesforce Data Model]**, and select the Edit ![Edit](assets/edit.png) icon to view the form data model (FDM).

After configuring the [[!DNL Salesforce] Cloud Config service](#configure-salesforce-cloud-service), you can integrate adaptive forms with out of the box [!DNL Salesforce] Data Model.

>[!MORELIKETHIS]
>
>* [Configure data sources for AEM Forms](/help/forms/configure-data-sources.md)
>* [Configure Azure storage for AEM Forms](/help/forms/configure-azure-storage.md)
>  [Add Forms Portal to an AEM Sites page](/help/forms/configure-forms-portal.md)
