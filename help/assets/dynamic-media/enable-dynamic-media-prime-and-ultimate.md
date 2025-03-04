---
title: Enable [!DNL Dynamic Media] Prime and Ultimate
description: Learn how to enable [!DNL Dynamic Media] Prime and Ultimate offerings.
feature: Asset Management
role: User, Admin
---
# Enable [!DNL Dynamic Media] Prime and Ultimate {#enable-dynamic-media-prime-and-ultimate}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

[!DNL Adobe Experience Manager] as a Cloud Service enables you to access [!DNL Dynamic Media] Prime and Ultimate offerings to streamline your digital workflows and optimize content management. See [Dynamic Media Prime and Ultimate](/help/assets/dynamic-media/dm-prime-ultimate.md) to understand their benefits and the key differences between them.

This article describes the end-to-end workflow to enable the [!DNL Dynamic Media] Prime and Ultimate offerings.

## Enable [!DNL Dynamic Media] Ultimate {#enable-dynamic-media-ultimate}

Execute the following steps in your cloud service environment to enable [!DNL Dynamic Media] Ultimate:

1. [Activate [!DNL Dynamic Media with OpenAPI]](#activate-dynamic-media-with-openapi) 
1. [Configure [!DNL Dynamic Media] solutions](#configure-dynamic-media-solutions) 
1. [Create and list [!DNL Dynamic Media] companies](#create-and-list-dynamic-media-companies)
1. [Configure custom domain in delivery tier](#configure-custom-domain-in-delivery-tier) 
<!--
1. [Onboard API keys using the [!DNL AEM] [!DNL Dynamic Media] API card](#onboarding-api-keys)
-->
If you need to enable [!DNL Dynamic Media Prime], see quick links provided in [Enable [!DNL Dynamic Media Prime]](#enable-dynamic-media-prime).

### Activate [!DNL Dynamic Media with OpenAPI] {#activate-dynamic-media-with-openapi}

[!DNL Dynamic Media] with OpenAPI capabilities puts DAM at the core of an agile and efficient content supply chain ecosystem to ensure asset governance and delivery.

The first step in the process of enabling [!DNL Dynamic Media] Ultimate is to activate [[!DNL Dynamic Media] with OpenAPI](/help/assets/dynamic-media-open-apis-overview.md) for your Cloud Service environment.

#### Prepare yourself to get started {#prerequisites}

Ensure that you fulfil the following requirements before starting the activation process:

1. [Access to Cloud Manager](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/cloud-manager).
1. [Your program includes [!DNL Dynamic Media] solutions](#configure-dynamic-media-solutions).
1. Your organization has [!DNL Dynamic Media] with OpenAPI credits. 

#### Enable [!DNL Dynamic Media with OpenAPI] capabilities in your Cloud Service environment {#enable-dynamic-media-with-openapi-capabilites-in-your-CS-environment}

Execute these steps to enable [!DNL Dynamic Media with OpenAPI] for your cloud service environment:

1. [Navigate to the Cloud Manager UI](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/cloud-manager). 
1. [Create an environment](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/create-environments) if you do not have access to an existing one.
1. Select **[!UICONTROL Click to activate]** in the **[!UICONTROL Dynamic Media]** row of the **[!UICONTROL Environment Information]** section on the Environment details page.
![activate dynamic media with OpenAPI capabilities](/help/assets/assets/activate-adv-capabiliites-of-dm-openAPI.png){width="700" align="center"}
1. Click **[!UICONTROL Activate]** on the confirmation dialog to start the [!DNL Dynamic Media with OpenAPI] activation process. After successful activation, the Cloud Manager displays the following status updates:
    1. **[!UICONTROL Environment stage]**: **[!UICONTROL Running]**
    1. ![DM activated](/help/assets/assets/Images_icon.svg)**[!UICONTROL Dynamic Media]**: **[!UICONTROL OpenAPI capabilities are activated]**
    
   ![activation successful](/help/assets/assets/activation-successful.png){width="700" align="center"}

#### Retry activation {#retry-activation}

If activation fails, the Cloud Manager displays the following status updates:

* **[!UICONTROL Environment stage]**: **[!UICONTROL DM with OpenAPI Failed]**
* ![DM activated](/help/assets/assets/Images_icon.svg)**[!UICONTROL Dynamic Media]**: **[!UICONTROL OpenAPI capabilities failed to activate]**
![retry activation](/help/assets/assets/retry-dm-openapi-failed-activation.png){width="700" align="center"}

Select **[!UICONTROL Click to retry]** to restart activation.

Alternatively, execute these steps to restart the activation process:

1. Navigate to the page which lists all environments.
1. Click more options (![more options](/help/assets/assets/three-dots.svg)) at the end of your environment row.
1. Select **[!UICONTROL Retry DM with OpenAPI Activation]** to restart activation.
![retry activation from environment details page](/help/assets/assets/restart-activation-process-from-list-environment-page.png)

### Configure [!DNL Dynamic Media] solutions {#configure-dynamic-media-solutions}

Configure [!UICONTROL Dynamic Media] solutions to use the basic and advanced capabilities of [Dynamic Media with OpenAPI](/help/assets/dynamic-media-open-apis-overview.md) on existing or new environments available in Cloud Manager.

#### Prepare yourself to get started {#prerequisites-to-configure-dynamic-media-solutions}

Ensure you have the following to configure [!UICONTROL Dynamic Media] solutions:

1. [Access to Cloud Manager](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/cloud-manager).
1. Your organization has [!DNL Dynamic Media with OpenAPI] credits.

#### Configure [!DNL Dynamic Media] solutions for asset delivery {#configure-dynamic-media-solutions-for-asset-delivery}

Execute the following steps:

1. [Create a new program](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/create-program) or navigate to an existing program and click **[!UICONTROL Edit]**. The **[!UICONTROL Set up for production]** page displays the **[!UICONTROL Solutions & Add-ons]** tab. 
1. Select **[!UICONTROL Assets]**, **[!UICONTROL Assets Prime]**, **[!UICONTROL Assets Ultimate]** or **[!UICONTROL Sites]** to add the **[!UICONTROL Dynamic Media]** solution to your program.
1. Select **[!UICONTROL Dynamic Media]** solution and click **[!UICONTROL Continue]** to add **[!UICONTROL Dynamic Media]** solution to your program. This action restarts all existing environments in your program and adds the [!DNL Dynamic Media] solution to them. Also, any new environment that you create under your program automatically gets [!DNL Dynamic Media].

![set up for production](/help/assets/assets/set-up-for-prod.png){width="500" align="center"}
See [Activate [!DNL Dynamic Media with OpenAPI]](#activate-dynamic-media-with-openapi) to start using the capabilities of [!DNL Dynamic Media] with OpenAPI capabilities in your environment.

### Create and list [!DNL Dynamic Media] companies {#create-and-list-dynamic-media-companies}

Create and list [!DNL Dynamic Media] companies in your AEM cloud service environment to manage configurations within your AEM environment. 

#### Prepare yourself to get started {#prerequisites-to-create-and-list-dynamic-media-companies}

To see the existing companies (accounts) or add a new [!DNL Dynamic Media] company (account) in your IMS org, you must have: 

1. [Access to Cloud Manager](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/cloud-manager).
1. [!DNL Dynamic Media with OpenAPI] credits in your organization.

#### Create and list [!DNL Dynamic Media] companies in your IMS organization {#create-and-list-dynamic-media-companies-in-your-ims-organisation}

Execute these steps to create and list a new [!DNL Dynamic Media] company (account) that can be configured within your [!DNL AEM] environment:

1. Navigate to the [Cloud Manager license page](https://experience-stage.adobe.com/#/@ssahnichstage/cloud-manager/license).
1. Click **[!UICONTROL Add Company]**, the **[!UICONTROL Create Dynamic Media Company]** dialog box displays. 
1. Specify a unique [!DNL Dynamic Media] company name, select a company region and add a list of company admin email IDs separated by commas.
 ![Create Dynamic Media company](/help/assets/assets/create-dynamic-media-company.png){width="500" align="center"}
1. Click **[!UICONTROL Create]** to start creating your company. This action adds a new row to **[!UICONTROL [!DNL Dynamic Media] companies]** section and displays **[!UICONTROL Setting up]** as the company's **[!UICONTROL STATUS]**.
![initiated Dynamic Media company creation](/help/assets/assets/dm-company-creation-initiated.png)
1. **Optional:** Click ![info icon](/help/assets/assets/info-icon-solid-black.svg) to see the company's details. The **[!UICONTROL STATUS]** updates to **[!UICONTROL Ready]**, when the company is created. 

   ![Dynamic Media company information](/help/assets/assets/dm-company-information.png)
1. As a Dynamic Media Administrator, check your mailbox for a welcome email that includes a list of steps to [configure [!DNL Dynamic Media]](/help/assets/dynamic-media/config-dm.md#architecture-diagram-of-dynamic-media) company in your [!DNL AEM] Cloud Service environment to get started.
![welcome email](/help/assets/assets/welcome-email.png)

#### Retry company creation {#retry-company-creation}

If [!DNL Dynamic Media] company creation fails, execute the following steps based on the failure status:

1. If **[!UICONTROL Status]** is Pending, then raise the issue to the customer support team for resolution.
![pending status](/help/assets/assets/company-creation-pending-status.png){width="350" align="center"}
1. If **[!UICONTROL Status]** is failed, then retry based on the reason of failure.
![failed status](/help/assets/assets/company-creation-failure-status.png){width="380" align="center"}

### Optional: Configure custom domain in delivery tier {#configure-custom-domain-in-delivery-tier}

While AEM as a Cloud Service comes with a default domain, you can customize it as per your needs. Attach a custom domain to the delivery tier using Cloud Manager.

#### Prepare yourself to get started {#prerequisites-to-configure-custom-domain-in-delivery-tier}

Ensure that you fulfil the following requirements before starting the configuration process:

1. [Access to Cloud Manager](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/cloud-manager).
1. [Already activated [!DNL Dynamic Media with OpenAPI] in your environment](#activate-dynamic-media-with-openapi).
1. Enabled [!DNL Dynamic Media with OpenAPI] in ready state.
1. EV or OV type certificate for the domain to be used for delivery tier. See [Introduction to SSL certificates](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-ssl-certificates/introduction-to-ssl-certificates) for more details.

#### Configure custom domain in delivery tier using Cloud Manager {#configure-custom-domain-in-delivery-tier-using-cloud-manager}

Execute the following steps in Cloud Manager to configure a custom domain in the delivery tier: 

1. [Add a customer managed SSL certificate](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-ssl-certificates/add-ssl-certificate#add-customer-managed-ssl-cert).
1. [Add a custom domain name](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/custom-domain-names/add-custom-domain-name#adding-cdn-settings).
1. Navigate to the environment details page and [add a CDN configuration](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/cdn-configurations/add-cdn-config). While adding the configuration, select **[!UICONTROL Delivery]** in the **[!UICONTROL Tier]** field in the **[!UICONTROL Configure CDN]** dialog box.
![Configure CDN](/help/assets/assets/select-delivery-tier-in-configure-cdn-form.png)

   After adding the configurations, the **[!UICONTROL STATUS]** of **[!UICONTROL CDN Configurations]** updates to **[!UICONTROL Applied]**. 
![Configure CDN deployment status](/help/assets/assets/cdn-configuration-deployment-status.png)
1. Click more options (![more options](/help/assets/assets/three-dots.svg)) and select **[!UICONTROL Go live readiness]** to display the **[!UICONTROL Go live readiness]** dialog box.
![go live readiness option](/help/assets/assets/go-live-readiness-option.png)
1. Execute the **[!UICONTROL Configure CNAME]** steps to map [cdn.adobeaemcloud.com](http://cdn.adobeaemcloud.com/) (CNAME record) in the DNS record of the DNS service provider. This mapping ensures that requests received at the custom domain are redirected to Adobe's CDN. 
![go live readiness dialogbox](/help/assets/assets/go-live-readiness-dialogbox.png){width="500" align="center"}
1. Click **[!UICONTROL Ok]**, the **[!UICONTROL STATUS]** updates to **[!UICONTROL Verified]**. The custom domain is ready to use in the delivery URL. 

![Configure CDN](/help/assets/assets/cdn-configurations-varified.png)
<!--
### Onboard API keys {#onboarding-api-keys}

Create an API key to access [!DNL Dynamic Media] with OpenAPIs and the delivery tier backed Asset Selector.

#### Prepare yourself for API keys onboarding process {#prerequisites-for-onboarding-api-keys} 

To start the API keys onboarding process, ensure you have:

1. [Access to Cloud Manager](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/cloud-manager).
1. [Activated [!DNL Dynamic Media with OpenAPI] in your environment](#activate-dynamic-media-with-openapi).
1. [Access to the Adobe Developer Console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/invoke-openapi-based-aem-apis#create-adobe-developer-console-adc-project).

#### Onboard the API keys using [!DNL AEM Dynamic Media] API card {#onboarding-api-keys-using-aem-dynamic-media-api-card}

Use the [Adobe Developer Console](https://developer.adobe.com/developer-console/) to onboard the API keys to:

1. [Access Dynamic Media APIs](#access-dynamic-media-apis)
1. [Access Delivery tier backed Asset Selector](#access-delivery-tier-backed-asset-selector)

#### Create an API key to access [!DNL Dynamic Media] with OpenAPIs {#access-dynamic-media-apis}

Execute the following steps to create an API key to access [!DNL Dynamic Media] with OpenAPIs:

1. Navigate to the **[!UICONTROL Admin Console]**. The Admin Console displays the **[!UICONTROL author]**, **[!UICONTROL delivery]** and **[!UICONTROL publish]** instances.
![instances on admin console](/help/assets/assets/delivery-instance-admin-console.png)
1. Select the **[!UICONTROL delivery]** instance to display the product profile with **[!UICONTROL AEM Dynamic Media enable API Services]** enabled by default. The product profile looks like this: **[!UICONTROL AEM Assets DM OpenAPI Users - delivery  - Program [ID Number] - Environment [ID Number]]**. 

   ![product profile on admin console](/help/assets/assets/admin-console-product-profile.png)

   >[!NOTE]
   >
   >This delivery instance is common for [!DNL Content Hub] and [!DNL Dynamic Media] with OpenAPI capabilities.

1. Navigate to the [Adobe Developer console](https://developer.adobe.com/console) and [create a new project](https://developer.adobe.com/dep/guides/dev-console/create-project/). See [Invoke OpenAPI-based AEM APIs for server to server authentication](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/invoke-openapi-based-aem-apis) to learn about creating a new project.
1. Select **[!UICONTROL AEM Dynamic Media API]** to access to the [!DNL Dynamic Media with OpenAPI capabilities] and click **[!UICONTROL Next]**.
![adobe developer console](/help/assets/assets/adobe-developer-console.png)
1. Select **[!UICONTROL Server-to-Server Authentication]** and click **[!UICONTROL Next]**. See [Server to Server authentication](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/) to learn more about this authentication type.
![server-to-server-authentication](/help/assets/assets/server-to-server-authentication.png)
1. Select **[!UICONTROL OAuth Server-to-Server]**, specify a unique **[!UICONTROL Credential name]** and click **[!UICONTROL Next]**.
![oauth server to server credential](/help/assets/assets/oauth-server-server-and-credential-name.png)
1. Select your product profile (mentioned in step 2) to access the APIs using the environment's delivery endpoint and click **[!UICONTROL Save configured API]**.
![select product profile](/help/assets/assets/select-product-profile.png)
1. Select **[!UICONTROL AEM Dynamic Media API]**. Use the **[!UICONTROL OAuth Server-to-Server]** to fetch the **X-API-key** and access the token for the **authorization** header. 
![oauth server to server](/help/assets/assets/oauth-server-to-server-credentials.png)
Execute the below steps to use [Dynamic Media with OpenAPIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/) using the **[!UICONTROL OAuth Server-to-Server]** credentials. 
    1. Copy the **[!UICONTROL API KEY (Client ID)]** and replace the `X-Api-Key` in the cURL.
    1. Click **[!UICONTROL Generate access token]** to generate an access token and replace `YOUR_JWT_HERE` with the token in the cURL.

The cURL looks like this:
```
headers: {
    'Content-Type': 'application/json',
      'X-Adobe-Accept-Experimental': '1',
      Authorization: 'Bearer <YOUR_JWT_HERE>',
      'X-Api-Key': 'YOUR_API_KEY_HERE'
    `},
```
See [Search Assets API](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dynamic-media-open-apis/search-assets-api#search-assets-api-header) for more information.

### Access Delivery tier backed Asset Selector {#access-delivery-tier-backed-asset-selector}

TBD: Wiki in progress.
-->

## Enable [!DNL Dynamic Media] Prime {#enable-dynamic-media-prime}

Execute the following steps in your cloud service environment to enable [!DNL Dynamic Media] Prime:

1. [Activate Dynamic Media with OpenAPI](#activate-dynamic-media-with-openapi) 
1. [Optional: Configure custom domain in delivery tier](#configure-custom-domain-in-delivery-tier) 
<!--
1. [Onboard API keys using the AEM Dynamic Media API card](#onboarding-api-keys)
-->