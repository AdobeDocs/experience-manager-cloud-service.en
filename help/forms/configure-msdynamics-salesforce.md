---
title: How to configure Microsoft Dynamics 365 and Salesforce out of the box form data models for adaptive forms?
description: Learn how to integrate Microsoft Dynamics 365 and Salesforce with adaptive forms.
exl-id: 2a43b2db-2dfb-4c79-88be-ea770b44dac1
---
# Configure [!DNL Microsoft Dynamics 365] and [!DNL Salesforce] cloud services {#configure-azure-storage}

[[!DNL Experience Manager Forms] Data Integration](data-integration.md) provides [!DNL Microsoft Dynamics 365] and [!DNL Salesforce] cloud services to integrate adaptive forms with out of the box Form Data Models. The Adaptive Forms can then interact with [!DNL Microsoft Dynamics 365] and [!DNL Salesforce] servers to enable business workflows. For example:

* Write data into [!DNL Microsoft Dynamics 365] and [!DNL Salesforce] on Adaptive Form submission.
* Write data in [!DNL Microsoft Dynamics 365] and [!DNL Salesforce] through custom entities defined in Form Data Model and vice versa.
* Query [!DNL Microsoft Dynamics 365] and [!DNL Salesforce] server for data and prepopulate Adaptive Forms.
* Read data from [!DNL Microsoft Dynamics 365] and [!DNL Salesforce] server.

[!DNL Microsoft Dynamics 365] and [!DNL Salesforce] cloud services and Form Data Models are available out of the box on the [!DNL AEM Forms] server  after you [set up a development project for Forms based on Experience Manager archetype](setup-local-development-environment.md##forms-cloud-service-local-development-environment).

>[!NOTE]
>
>Microsoft Dynamics 365 and [!DNL Salesforce] cloud services and Form Data Models are available out of the box only if you set up an [!DNL Experience Manager Forms] as a [!DNL Cloud Service] project based on [AEM Archetype 30](https://github.com/adobe/aem-project-archetype/releases/tag/aem-project-archetype-30) or later.

## Configure [!DNL Salesforce] cloud service {#configure-salesforce-cloud-service}

Before configuring the [!DNL Salesforce] cloud services, ensure that you perform the following tasks:

* [Create a connected OAuth-enabled [!DNL Salesforce] application](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_api_integration.htm&type=5). When you are creating the connected [!DNL Salesforce] application, specify the callback URL in the following format:

   ```
   https://'[server]:[port]'/libs/fd/fdm/gui/components/admin/fdmcloudservice/createcloudconfigwizard/cloudservices.html
   ```

   Where server and port refers to the hostname and port number for the [!DNL AEM Forms] server. 

* While creating the connected [!DNL Salesforce] application, specify `full` and `offline_access` as the values for the OAuth scope.

* Take a note of the values for the client ID (referred to as Consumer Key) and client secret (referred to as Consumer Secret) for the connected application.

Perform the following steps to configure the [!DNL Salesforce] cloud service:

1. On [!DNL AEM Forms] author instance, navigate to **[!UICONTROL Tools]** ![hammer](assets/hammer.png) &gt; **[!UICONTROL Cloud Services]** &gt; **[!UICONTROL Data Sources]**. The list of available wrapper folders includes a folder with the title specified for `DappTitle`  while [generating the AEM archetype project](setup-local-development-environment.md##forms-cloud-service-local-development-environment).
1. Tap the folder name, select **[!UICONTROL Salesforce Cloud Config]**, and tap **[!UICONTROL Properties]**.
1. In the **[!UICONTROL Authentication Settings]** tab:
   1. Specify the [!DNL Salesforce] Domain URL in the **[!UICONTROL Host]** field. For example, [Domain-name].my.salesforce.com.
   1. Specify the client ID (referred to as Consumer Key) and client secret (referred to as Consumer Secret) for the connected application.
   1. Specify **full offline_access** (`full` and `offine_access` values separated by a space) in the **[!UICONTROL Authorization Scope]** field.
   1. Tap **[!UICONTROL Connect to OAuth]**. You are redirected to [!DNL Microsoft Dynamics] login page.
   1. Log in with your [!DNL Salesforce] credentials and accept to allow the cloud service configuration to connect to [!DNL Salesforce] service. If the connection is successful, you are redirected to the [!DNL Salesforce] cloud service configuration page, which displays a success message.
1. Tap **[!UICONTROL Save & Close]** to complete the configuration setup.

### Access out of the box [!DNL Salesforce] Form Data Model

A [!DNL Salesforce] Form Data Model is available out of the box on the [!DNL AEM Forms] server  after you [set up a development project for Forms based on Experience Manager archetype](setup-local-development-environment.md##forms-cloud-service-local-development-environment).

To access the Form Data Model, navigate to **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Data Integrations]**. The list of available folders include a folder with the title specified for `DappTitle`  while [generating the AEM archetype project](setup-local-development-environment.md##forms-cloud-service-local-development-environment). Tap the folder name, select the **[!UICONTROL Salesforce Data Model]**, and tap the Edit ![Edit](assets/edit.png) icon to view the form data model.

After configuring the [[!DNL Salesforce] Cloud Config service](#configure-salesforce-cloud-service), you can integrate adaptive forms with out of the box [!DNL Salesforce] Data Model.

## Configure [!DNL Microsoft Dynamics 365] cloud service {#configure-dynamics-cloud-service}

Before configuring the [!DNL Microsoft Dynamics 365] cloud service, ensure that you perform the following tasks:

* [Register an application for [!DNL Microsoft Dynamics 365] with Azure Active Directory](https://docs.microsoft.com/en-us/powerapps/developer/data-platform/walkthrough-register-app-azure-active-directory). When you are creating the connected [!DNL Microsoft Dynamics 365] application, specify the  Reply URLs in the following format:

   ```
   https://'[server]:[port]'/libs/fd/fdm/gui/components/admin/fdmcloudservice/createcloudconfigwizard/cloudservices.html
   ```

   Where server and port refers to the hostname and port number for the [!DNL AEM Forms] server. 

* Take a note of the values for the client ID (also referred to as Application ID) and client secret for the connected application.

Perform the following steps to configure the [!DNL Microsoft Dynamics 365] cloud service:

1. On [!DNL AEM Forms] author instance, navigate to **[!UICONTROL Tools]** ![hammer](assets/hammer.png) &gt; **[!UICONTROL Cloud Services]** &gt; **[!UICONTROL Data Sources]**. The list of available wrapper folders includes a folder with the title specified for `DappTitle`  while [generating the AEM archetype project](setup-local-development-environment.md##forms-cloud-service-local-development-environment).
1. Tap the folder name, select **[!UICONTROL Microsoft Dynamics 365 Cloud Config]**, and tap **[!UICONTROL Properties]**.
1. In the **[!UICONTROL Authentication Settings]** tab:
   1. Enter the value for the **[!UICONTROL Service Root]** field. Go to the Dynamics instance and navigate to [Developer Resources](https://docs.microsoft.com/en-us/powerapps/developer/data-platform/view-download-developer-resources) to view the value for the Service Root field. For example, `https://<tenant-name>.dynamics.com/api/data/v9.1/`
   1. Specify the client ID (referred to as Application ID) and client secret for the connected application.
   1. Replace `{tenant}` with a tenant ID in the **[!UICONTROL OAuth URL]**, **[!UICONTROL Refresh Token URL]**, and **[!UICONTROL Access Token URL]** fields.
   1. Specify the dynamics instance URL in the **[!UICONTROL Resource]** field to configure [!UICONTROL Microsoft Dynamics] with a Form Data Model. Use the Service Root URL to derive the Dynamics instance URL. For example, `https://<tenant-name>.dynamics.com`.

   1. Specify `openid` in the **[!UICONTROL Authorization Scope]** field for authorization process on [!DNL Microsoft Dynamics 365].
   1. Log in with your [!DNL Microsoft Dynamics 365] credentials and accept to allow the cloud service configuration to connect to [!DNL Microsoft Dynamics 365] service. If the connection is successful, you are redirected to the [!DNL Microsoft Dynamics 365] cloud service configuration page, which displays a success message.
1. Tap **[!UICONTROL Save & Close]** to complete the configuration setup.

### Access out of the box [!DNL Microsoft Dynamics 365] Form Data Model

A [!DNL Microsoft Dynamics 365] Form Data Model is available out of the box on the [!DNL AEM Forms] server  after you [set up a development project for Forms based on Experience Manager archetype](setup-local-development-environment.md##forms-cloud-service-local-development-environment).

To access the Form Data Model, navigate to **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Data Integrations]**. The list of available folders include a folder with the title specified for `DappTitle`  while [generating the AEM archetype project](setup-local-development-environment.md##forms-cloud-service-local-development-environment). Tap the folder name, select the **[!UICONTROL Microsoft Dynamics 365 Data Model]**, and tap the Edit ![Edit](assets/edit.png) icon to view the form data model.

After configuring the [[!DNL Microsoft Dynamics 365] Cloud Config service](#configure-dynamics-cloud-service), you can integrate adaptive forms with out of the box [!DNL Microsoft Dynamics 365] Data Model.
