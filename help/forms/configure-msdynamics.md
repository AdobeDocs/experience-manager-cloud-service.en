---
title: How to configure Microsoft Dynamics 365 out of the box form data models for Adaptive Forms?
description: Learn how to integrate Microsoft Dynamics 365 with Adaptive Forms.
feature: Adaptive Forms, Form Data Model
role: User, Developer
exl-id: 29ee324c-cd4c-403b-bb3d-b1eda8e8ad88
---

# Configure Microsoft&reg; Dynamics 365 for AEM Forms 

Adobe Experience Manager Forms Data Integration provides a cloud service configuration to integrate forms with Microsoft Dynamics server. It enables you to create Form Data Model (FDM) based on the entities, attributes, and services defined in Microsoft Dynamics service. The Form Data Model (FDM) can be used to create Adaptive Forms that interact with Microsoft Dynamics server to enable business workflows. For example:
* Query Microsoft Dynamics server for data and prepopulate Adaptive Forms.
* Write data into Microsoft Dynamics on Adaptive Form submission.
* Write data in Microsoft Dynamics through custom entities defined in Form Data Model (FDM).

AEM as a Cloud Service offers various out of the box submit actions for handling form submissions. You can learn more about these options in the [Adaptive Form Submit Action](/help/forms/configure-submit-actions-core-components.md)  article.

<!-- 
[[!DNL Experience Manager Forms] Data Integration](data-integration.md) provides [!DNL Microsoft&reg; Dynamics 365] Cloud Services to integrate Adaptive Forms with out of the box Form Data Model (FDM). The Adaptive Forms can then interact with [!DNL Microsoft&reg; Dynamics 365] servers to enable business workflows. For example:

* Write data into [!DNL Microsoft&reg; Dynamics 365] on Adaptive Form submission.
* Write data in [!DNL Microsoft&reg; Dynamics 365] through custom entities defined in Form Data Model (FDM) and conversely.
* Query [!DNL Microsoft&reg; Dynamics 365]server for data and prepopulate Adaptive Forms.
* Read data from [!DNL Microsoft&reg; Dynamics 365] server.

[!DNL Microsoft&reg; Dynamics 365] cloud services and Form Data Model (FDM) are available out of the box on the [!DNL AEM Forms] Server after you [set up a development project for Forms based on Experience Manager archetype](setup-local-development-environment.md#forms-cloud-service-local-development-environment).

>[!NOTE]
>
>Microsoft&reg; Dynamics 365 cloud services and Form Data Model (FDM) are available out of the box only if you set up an [!DNL Experience Manager Forms] as a [!DNL Cloud Service] project based on [AEM Archetype 30](https://github.com/adobe/aem-project-archetype/releases/tag/aem-project-archetype-30) or later.-->

## Prerequisites

Before integrating [!DNL Microsoft® Dynamics 365] with AEM Forms as a Cloud Service, ensure that you have performed the following steps:


1. **Set up the account in Microsoft Dynamics 365** 
   
     Follow the steps explained in the video to set up a Microsoft Dynamics 365 account. In this video, a trial account is created for demonstration purposes.

    >[!VIDEO](https://video.tv.adobe.com/v/3444389/)

1. **Create an account in the Power Platform Admin Center**
    Create an account in the **Power Platform Admin Center** to: 
    * Add Dataverse
    * Enable Microsoft Dynamics 365 aaplications
    
    Follow the steps in the video to create an account in the Power Platform Admin Center. In this video, a trial account has been created for demonstration purposes.
    
    >[!VIDEO](https://video.tv.adobe.com/v/3444388)

1. **Register an application for [!DNL Microsoft&reg; Dynamics 365] in Azure Active Directory**

    Follow the steps in the video to register an application for [!DNL Microsoft&reg; Dynamics 365] in Azure Active Directory.

    >[!VIDEO](https://video.tv.adobe.com/v/3444369/dynamics365integration-microsoftdynamics-apiaccess-azuread-appregistration)

    >[!NOTE]
    >
    > * To create the connected [!DNL Microsoft® Dynamics 365] application, select **Web** as the platform and specify the **Redirect URI** in the following format: `https://'[server]:[port]'/libs/fd/fdm/gui/components/admin/fdmcloudservice/fdm.html`.
    > * Make sure to save the Client ID (also known as the Application ID) and Client secret for future reference.
    
## Connect Forms to Microsoft&reg; Dynamics 365

Once you have configured the prerequisites above, you can proceed with integrating Adaptive Forms with Microsoft® Dynamics 365. To send data to Microsoft® Dynamics 365 on form submission, follow the below steps:

[1. Configure cloud service configuration for Microsoft Dynamics](#1-configure-cloud-service-configuration-for-microsoft-dynamics)

[2. Create Form Data Model (FDM)](#2-create-form-data-model-fdm)

### 1. Configure cloud service configuration for Microsoft Dynamics

 >[!VIDEO](https://video.tv.adobe.com/v/3444370/cloudconfiguration-dataintegration-adobeexperiencemanager-aemforms-microsoftdynamics)

Perform the following steps to configure the [!DNL Microsoft&reg; Dynamics 365] cloud service configuration:

1. Navigate to **[!UICONTROL Tools]** ![hammer](assets/hammer.png) &gt; **[!UICONTROL Cloud Services]** &gt; **[!UICONTROL Data Sources]** on [!DNL AEM Forms] author instance,.

    ![Select Cloud Data Source](/help/forms/assets/dynamics-data-source.png)
1. Select a Configuration Container. The configuration is stored in the selected Configuration Container.
1. Click **[!UICONTROL Create]**.

    ![Create Cloud Configuration](/help/forms/assets/dynamics-select-configuration.png)

    The **Create Data Source Configuration** configuration wizard appears.

    ![Create Data Source Configuration wizard](/help/forms/assets/dynamics-create-data-configuration.png)

1. Specify the **[!UICONTROL Title]**, **[!UICONTROL Name]** and select **[!UICONTROL Service Type]** as **OData Service**.
1. Click **[!UICONTROL Next]**. The **Authentication** tab appears.

    ![Authentication Tab](/help/forms/assets/dynamics-authentication-tab.png)

1. Specify the value for the **[!UICONTROL Service Root]** field. 

    Go to your Dynamics instance in the **Power Platform Admin Center** and navigate to [Developer Resources](https://docs.microsoft.com/en-us/powerapps/developer/data-platform/view-download-developer-resources) to view the value of the **Service Root**. The **Web API endpoint** represents the **Service Root** value for the Dynamics instance you want to integrate with Adaptive Forms. The **Service Root** URL  is in the following format: `https://<tenant-name>.dynamics.com/api/data/v9.1/`

    ![Service Root field](/help/forms/assets/dynamics-service-root.png)

1. Select the **[!UICONTROL Authentication Type]** as **OAuth2.0**.
1. Specify the **Client ID** (referred to as Application ID) and **Client Secret** for the connected application. 
   You can retrieve the **Client ID** and **Client Secret** from the Azure Active Directory Application.

    ![Client ID and Client Secret](/help/forms/assets/dynamics-azure-app-resgistration.png)

1. Specify the following in the **[!UICONTROL OAuth URL]**, **[!UICONTROL Refresh Token URL]**, and **[!UICONTROL Access Token URL]** fields.
   You can retrieve the **[!UICONTROL OAuth URL]**, **[!UICONTROL Refresh Token URL]**, and **[!UICONTROL Access Token URL]** from the **Endpoints** section of your Azure Active Directory Application.

    ![Azure App Endpoints](/help/forms/assets/dynamics-azure-app-endpoints.png)

1. Specify `openid` in the **[!UICONTROL Authorization Scope]** field for authorization process on [!DNL Microsoft&reg; Dynamics 365].
1. Specify the dynamics instance URL in the **[!UICONTROL Resource]** field to configure [!DNL Microsoft&reg; Dynamics 365] with a Form Data Model (FDM). 
    You can copy the **Environment URL** from the **Power Platform Admin Center** or derive the Dynamics instance URL using the **Service Root** URL. The resource URL is in the following format: `https://<tenant-name>.dynamics.com`.

    ![Power App Resource Field](/help/forms/assets/dynamics-resource-field.png)

1. Log in with your [!DNL Microsoft&reg; Dynamics 365] credentials and accept to allow the cloud service configuration to connect to [!DNL Microsoft&reg; Dynamics 365] service. If the connection is successful, you are redirected to the [!DNL Microsoft&reg; Dynamics 365] cloud service configuration page, which displays a success message.
1. Select **[!UICONTROL Create]** to save the configuration.

### 2. Create Form Data Model (FDM)

>[!VIDEO](https://video.tv.adobe.com/v/3444367/aemforms-adobeexperiencemanager-formdatamodel--dataintegration-digitalforms)

You can use the create the Form Data Model (FDM) using the created [!DNL Microsoft&reg; Dynamics 365] cloud configuration. Perform the following steps to create Form Data Model:

1. Navigate to **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Data Integrations]**. 
   ![Create Form Data Model](/help/forms/assets/dynamics-create-fdm.png)

1. Click **[!UICONTROL Create]** and select **[!UICONTROL Form data Model]**. 
   ![Select Form Data Model](/help/forms/assets/dynamics-select-fdm.png)
   
   The **Create Form Data Model** wizard appears.
1. Click **[!UICONTROL Next]**.
1. Select the created cloud configuration from the **Select Datasource** tab. 
    ![Select Cloud Configuration](/help/forms/assets/dynamics-select-cloud-config.png)

1. Click the Edit ![Edit](assets/edit.png) icon to view and configure the Form Data Model (FDM).

Next, you can [configure the Form Data Model (FDM)](/help/forms/work-with-form-data-model.md#configure-services) and use it in various Adaptive Form use cases, such as:

* Prefill Adaptive Form by querying information from [!DNL Microsoft Dynamics] entities and services
* Invoke [!DNL Microsoft Dynamics] server operations defined in a Form Data Model (FDM) using Adaptive Form rules
* Write submitted form data to [!DNL Microsoft Dynamics] entities
* You can configure the Form Data Model Submit Action for an Adaptive Form to send data to [!DNL Microsoft Dynamics].

You can then use the [Submit using Form Data Model (FDM)](/help/forms/using-form-data-model.md) option in an **Adaptive Form** to transfer data from your form to the configured [!DNL Microsoft® Dynamics 365].


>[!MORELIKETHIS]
>
>* [Configure data sources for AEM Forms](/help/forms/configure-data-sources.md)
>* [Configure Azure storage for AEM Forms](/help/forms/configure-azure-storage.md)
>  [Add Forms Portal to an AEM Sites page](/help/forms/configure-forms-portal.md)
