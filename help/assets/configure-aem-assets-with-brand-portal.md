---
title: Configure AEM Assets cloud service with Brand Portal
description: Configure AEM Assets cloud service with Brand Portal.
contentOwner: Vishabh Gupta
---

# Configure AEM Assets with Brand Portal {#configure-aem-assets-with-brand-portal}

Adobe Experience Manager (AEM) Assets is configured with Brand Portal via Adobe Developer Console, which procures an IMS token for authorization of your Brand Portal tenant.

**How configuration works?**

Configuring the AEM Assets cloud instance with a Brand Portal tenant (organization) requires configurations in both, AEM Assets cloud instance as well as in Adobe Developer Console.

1. In AEM Assets cloud instance, create an IMS account and generate a public certificate (public key).
1. In Adobe Developer Console, create a project for your Brand Portal tenant (organization).
1. Under the project, configure an API using the public key to create a service account (JWT) connection.
1. Get the service account credentials and JWT payload information.
1. In AEM Assets cloud instance, configure the IMS account using the service account credentials and JWT payload.
1. In AEM Assets cloud instance, configure the Brand Portal cloud service using the IMS account and Brand Portal endpoint (organization URL).
1. Test the configuration by publishing an asset from AEM Assets cloud instance to Brand Portal.

>[!NOTE]
 >
 >A Brand Portal tenant shall only be configured with one AEM Assets cloud instance.
 >
 >Do not configure a Brand Portal tenant with multiple AEM Assets cloud instances.
 >

## Prerequisites {#prerequisites}

You require the following to configure AEM Assets with Brand Portal:

* An up and running AEM Assets cloud instance.
* Brand Portal tenant URL.
* A user with system administrator privileges on the IMS organization of the Brand Portal tenant. 

**Contact Customer Care** for further queries.

## Create configuration {#create-new-configuration}

Perform the following steps in the specified sequence to configure AEM Assets cloud instance with Brand Portal.
 
1. [Obtain public certificate](#public-certificate)
1. [Create service account (JWT) connection](#createnewintegration) 
1. [Configure IMS account](#create-ims-account-configuration)
1. [Configure cloud service](#configure-the-cloud-service)
1. [Test configuration](#test-configuration)

### Create IMS configuration {#create-ims-configuration}

IMS configuration authenticates your Brand Portal tenant with AEM Assets cloud instance. 

IMS configuration includes two steps:

* [Obtain public certificate](#public-certificate) 
* [Configure IMS account](#create-ims-account-configuration)

### Obtain public certificate {#public-certificate}

Public certificate allows you to authenticate your profile on Adobe Developer Console.

1. Log in to your AEM Assets cloud instance.

1. From the **Tools** ![Tools](assets/tools.png) panel, navigate to **[!UICONTROL Security]** > **[!UICONTROL Adobe IMS Configurations]**.

   ![Adobe IMS Account Configuration UI](assets/ims-configuration1.png)

1. In Adobe IMS Configurations page, click **[!UICONTROL Create]**. 
   
1. You are redirected to the **[!UICONTROL Adobe IMS Technical Account Configuration]** page. By default, the **Certificate** tab opens.

   Select the cloud solution **[!UICONTROL Adobe Brand Portal]**.  

1. Mark the check box **[!UICONTROL Create new certificate]** and specify an **alias** for the certificate. The alias serves as name of the dialog. 

1. Click **[!UICONTROL Create certificate]**. Then, click **[!UICONTROL OK]** in the dialog box to generate the public certificate.

   ![Create Certificate](assets/ims-config2.png)

1. Click **[!UICONTROL Download Public Key]** and save the certificate (.crt) file on your machine. 

   The certificate file will be used in further steps to configure API for your Brand Portal tenant and generate service account credentials in Adobe Developer Console.  

   ![Download Certificate](assets/ims-config3.png)

1.  Click **[!UICONTROL Next]**. 

    In the **Account** tab, you create the Adobe IMS account but for that you will need the service account credentials that are generated in Adobe Developer Console. Keep this page open for now.

    Open a new tab and [create a service account (JWT) connection in Adobe Developer Console](#createnewintegration) to get the credentials and JWT payload for configuring the IMS account. 

### Create service account (JWT) connection {#createnewintegration}

In Adobe Developer Console, projects and APIs are configured at organization (Brand Portal tenant) level. Configuring an API creates a service account (JWT) connection in Adobe Developer Console. There are two methods to configure API, by generating a key pair (private and public keys) or by uploading a public key. To configure AEM Assets cloud instance with Brand Portal, you must generate a public certificate (public key) in AEM Assets cloud instance and create credentials in Adobe Developer Console by uploading the public key. This public key is used to configure API for the selected Brand Portal organization and generates the credentials and JWT payload for the service account. These credentials are further used to configure the IMS account in AEM Assets cloud instance. Once the IMS account is configured, you can configure the Brand Portal cloud service in AEM Assets cloud instance.

Perform the following steps to generate the service account credentials and JWT payload:

1. Log in to Adobe Developer Console with system administrator privileges on the IMS organization (Brand Portal tenant). The default URL is 

   [https://www.adobe.com/go/devs_console_ui](https://www.adobe.com/go/devs_console_ui)


   >[!NOTE]
    >
    >Ensure that you have selected the correct IMS organization (Brand Portal tenant) from the dropdown (organization list) located at the upper-right corner.
    >

1. Click **[!UICONTROL Create new project]**. A blank project is created for your organization. 

   Click **[!UICONTROL Edit project]** to update the **[!UICONTROL Project Title]** and **[!UICONTROL Description]**, and click **[!UICONTROL Save]**.

   ![Create Project](assets/service-account1.png)
   
1. In the Project overview tab, click **[!UICONTROL Add API]**.

   ![Add API](assets/service-account2.png)

1. In the Add an API window, select **[!UICONTROL AEM Brand Portal]** and click **[!UICONTROL Next]**. 

   Ensure that you have access to the AEM Brand Portal service.

1. In the Configure API window, click **[!UICONTROL Upload your public key]**. Then, click **[!UICONTROL Select a File]** and upload the public certificate (.crt file) that you have downloaded in the [obtain public certificate](#public-certificate) section. 

   Click **[!UICONTROL Next]**.

   ![Upload Public Key](assets/service-account3.png)

1. Verify the public certificate and click **[!UICONTROL Next]**.

1. Select the default product profile **[!UICONTROL Assets Brand Portal]** and click **[!UICONTROL Save configuration]**. 

   <!-- 
   In Brand Portal, a default profile is created for each organization. The Product Profiles are created in admin console for assigning users to groups (based on the roles and permissions). For configuration with Brand Portal, the OAuth token is created at organization level. Therefore, you must configure the default Product Profile for your organization. 
   -->

   ![Select Product Profile](assets/service-account4.png)

1. With the API configured, you are redirected to the API overview. From the left navigation under **[!UICONTROL Credentials]**, click **[!UICONTROL Service Account (JWT)]**.

   >[!NOTE]
    >
    >You can view the credentials and perform other actions (generate JWT tokens, copy credential details, retrieve client secret, and so on) as needed.
    >

1. From the **[!UICONTROL Client Credentials]** tab, copy the **[!UICONTROL client ID]**. 

   Click **[!UICONTROL Retrieve Client Secret]** and copy the **[!UICONTROL client secret]**.

   ![Service Account Credentials](assets/service-account5.png)

1. Navigate to the **[!UICONTROL Generate JWT]** tab and copy the **[!UICONTROL JWT Payload]**. 

You can now use the client ID (API key), client secret, and JWT payload to [configure the IMS account](#create-ims-account-configuration) in AEM Assets cloud instance.

<!--
1. Click **[!UICONTROL Create Integration]**.

1. Select **[!UICONTROL Access an API]**, and click **[!UICONTROL Continue]**.

   ![Create New Integration](assets/create-new-integration1.png)

1. Create a new integration page opens. 
   
   Select your organization from the drop-down list.

   In **[!UICONTROL Experience Cloud]**, Select **[!UICONTROL AEM Brand Portal]** and click **[!UICONTROL Continue]**. 

   If the Brand Portal option is disabled for you, ensure that you have selected correct organization from the drop-down box above the **[!UICONTROL Adobe Services]** option. If you do not know your organization, contact your administrator.

   ![Create Integration](assets/create-new-integration2.png)

1. Specify a name and description for the integration. Click **[!UICONTROL Select a File from your computer]** and upload the `AEM-Adobe-IMS.crt` file downloaded in the [obtain public certificates](#public-certificate) section.

1. Select the profile of your organization. 

   Or, select the default profile **[!UICONTROL Assets Brand Portal]** and click **[!UICONTROL Create Integration]**. The integration is created.

1. Click **[!UICONTROL Continue to integration details]** to view the integration information. 

   Copy the **[!UICONTROL API Key]** 
   
   Click **[!UICONTROL Retrieve Client Secret]** and copy the Client Secret key.

   ![API Key, Client Secret, and payload information of an integration](assets/create-new-integration3.png)

1. Navigate to **[!UICONTROL JWT]** tab, and copy the **[!UICONTROL JWT payload]**.

   The API Key, Client Secret key, and JWT payload information will be used to create IMS account configuration.

-->

### Configure IMS account {#create-ims-account-configuration}

Ensure that you have performed the following steps:

* [Obtain public certificate](#public-certificate)
* [Create service account (JWT) connection](#createnewintegration)

Perform the following steps to configure the IMS account that you have created in [obtain public certificate](#public-certificate).

1. Open the IMS Configuration and navigate to the **[!UICONTROL Accounts]** tab. You kept the page open while [obtaintaing the public certificate](#public-certificate).

1. Specify a **[!UICONTROL Title]** for the IMS account.

   In **[!UICONTROL Authorization Server]**, enter the URL: [https://ims-na1.adobelogin.com/](https://ims-na1.adobelogin.com/)  

   Paste the client ID in API key, client secret, and JWT payload that you have copied while [creating the service account (JWT) connection](#createnewintegration).

   Click **[!UICONTROL Create]**.

   The IMS account is configured. 

   ![IMS Account configuration](assets/create-new-integration6.png)

   
1. Select the IMS account configuration and click **[!UICONTROL Check Health]**.

   Click **[!UICONTROL Check]** in the dialog box. On successful configuration, a message appears that the *Token is retrieved successfully*.

   ![](assets/create-new-integration5.png)

>[!CAUTION]
 >
 >You must have only one IMS configuration. Do not create multiple IMS configurations.
 >
 >Ensure that the IMS configuration passes the health check. If the configuration does not pass the health check, it is invalid. You must delete it and create a new, valid configuration.
 >


### Configure cloud service {#configure-the-cloud-service}

Perform the following steps to configure the Brand Portal cloud service:

1. Log in to your AEM Assets cloud instance.

1. From the **Tools** ![Tools](assets/tools.png) panel, navigate to **[!UICONTROL Cloud Services]** > **[!UICONTROL AEM Brand Portal]**.

1. In the Brand Portal Configurations page, click **[!UICONTROL Create]**.

1. Specify a **[!UICONTROL Title]** for the configuration. 

   Select the IMS configuration that you have created while [configuring the IMS account](#create-ims-account-configuration).
   
   In the **[!UICONTROL Service URL]**, enter your Brand Portal tenant (organization URL).   
   
    ![](assets/create-cloud-service.png)

1. Click **[!UICONTROL Save and Close]**. The cloud configuration is created. Your AEM Assets cloud instance is now configured with the Brand Portal tenant. 

### Test configuration {#test-configuration}

Perform the following steps to validate the configuration:

1. Log in to your AEM Assets cloud instance.

1. From the **Tools** ![Tools](assets/tools.png) panel, navigate to **[!UICONTROL Deployment]** > **[!UICONTROL Distribution]**.

    ![](assets/test-bpconfig1.png)

1. In the Distribution page, you can see that a Brand Portal distribution agent `bpdistributionagent0` is created for **[!UICONTROL Publish to Brand Portal]**.

   Click **[!UICONTROL Publish to Brand Portal]**.

   ![](assets/test-bpconfig2.png)

   >[!NOTE]
    >
    >By default, one distribution agent is created for a Brand Portal tenant.
    >

1. In the distribution agent page, you can see the distribution queues under the **[!UICONTROL Status]** tab. 
   
   A distribution agent contains two queues: 
   * **processing-queue**: for the distribution of assets to Brand Portal. 

   * **error-queue**: for the assets where distribution has failed. 
   
   >[!NOTE]
    >
    >It is recommended to review the failures and  clear the **error-queue** periodically.  
    > 

   ![](assets/test-bpconfig3.png)

1. To verify the connection between AEM Assets and Brand Portal, click **[!UICONTROL Test Connection]**.

   ![](assets/test-bpconfig4.png)

   A message appears at the bottom of page that your test package is successfully delivered.

   >[!NOTE]
    >
    >Avoid disabling the distribution agent, as it can cause the distribution of the assets (running-in-queue) to fail.
    > 


Your AEM Assets cloud instance is successfully configured with Brand Portal, you can now:

* [Publish assets from AEM Assets to Brand Portal](publish-to-brand-portal.md)
* [Publish folders from AEM Assets to Brand Portal](publish-to-brand-portal.md#publish-folders-to-brand-portal)
* [Publish collections from AEM Assets to Brand Portal](publish-to-brand-portal.md#publish-collections-to-brand-portal)

In addition to the above, you can also publish metadata schemas, image presets, search facets, and tags from AEM Assets to Brand Portal. 

* [Publish presets, schemas, and facets to Brand Portal](https://docs.adobe.com/content/help/en/experience-manager-brand-portal/using/publish/publish-schema-search-facets-presets.html)
* [Publish tags to Brand Portal](https://docs.adobe.com/content/help/en/experience-manager-brand-portal/using/publish/brand-portal-publish-tags.html)


See, [Brand Portal documentation](https://docs.adobe.com/content/help/en/experience-manager-brand-portal/using/home.html) for more information.


## Distribution logs {#distribution-logs}

You can check the logs for detailed information on the actions performed by the distribution agent. 

For example, we have published an asset from AEM Assets to Brand Portal to validate the configuration. 

1. Follow the steps (from 1 to 4) as shown in the [Test Configuration](#test-configuration) section and navigate to the distribution agent page.

1. Click **[!UICONTROL Logs]** to view the distribution logs. You can see the processing and error logs here.

   ![](assets/test-bpconfig5.png)

The distribution agent generates the following logs:

* INFO: This is a system generated log that triggers on successful configuration that enables the distribution agent. 
* DSTRQ1 (Request 1): Triggers on test connection.
   
On publishing the asset, the following request and response logs are generated:

**Distribution agent request**:
* DSTRQ2 (Request 2): The asset publishing request is triggered.
* DSTRQ3 (Request 3): The system triggers another request to publish the folder in which the asset exists and replicates the folder in Brand Portal.

**Distribution agent response**:
* queue-bpdistributionagent0 (DSTRQ2): The asset is published to Brand Portal.
* queue-bpdistributionagent0 (DSTRQ3): The system replicates the folder containing the asset in Brand Portal.

In the above example, an additional request and response are triggered. The system could not find the parent folder (a.k.a Add Path) in Brand Portal because the asset was published for the first time, therefore, triggers an additional request to create a parent folder with the same name in Brand Portal where the asset is published.  

>[!NOTE]
 >
 >Additional request is generated in case the parent folder does not exist in Brand Portal (in the above example), or the parent folder has been modified in AEM Assets. 
 >


<!--

## Additional information {#additional-information}

Go to `/system/console/slingmetrics` for statistics related to the distributed content:

1. **Counter metrics**
   * sling: `mac_sync_request_failure`
   * sling: `mac_sync_request_received`
   * sling: `mac_sync_request_success`

1. **Time metrics**
   * sling: `mac_sync_distribution_duration`
   * sling: `mac_sync_enqueue_package_duration`
   * sling: `mac_sync_setup_request_duration`

-->

<!--
   Comment Type: draft

   <li> </li>
   -->

   <!--
   Comment Type: draft

   <li>Step text</li>
   -->
