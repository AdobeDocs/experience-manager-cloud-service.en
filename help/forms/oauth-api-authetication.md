---
title: How to set up OAuth Server-to-Server Authentication?
description: Learn how to configure OAuth Server-to-Server authentication for Adobe Experience Manager Forms as a Cloud Service
role: Admin, Developer, User
feature: Adaptive Forms, APIs & Integrations
hide: yes
hidefromtoc: yes
index: no
---

# OAuth Server-to-Server Authentication 

OAuth Server-to-Server Authentication allows secure, token-based access to AEM Forms Communications APIs without requiring user interaction. OAuth server-to-server authentication is supported by Adobe Developer Console.

## Prerequisites

Before you begin, make sure the following prerequisites are met:

* Ensure that you have [access to the Adobe Developer Console](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/requirements/access-rights) specific to the environment you use.
* [Assign the System Administrator or Developer role in the Adobe Admin Console](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/requirements/role-based-permissions) to enable access to the Adobe Developer Console. 

## How to Generate an Access Token Using OAuth Server-to-Server Authentication?

Follow the steps below to generate an access token from the Adobe Developer console, and make your first API call through OAuth Server-to-Server Authentication.

### 1. Adobe Developer Console Project Setup

1. Navigate to [Adobe Developer Console](https://developer.adobe.com/console)
2. Log in with your Adobe ID

3. Create New Project or navigate to your existing project

>[!BEGINTABS]

>[!TAB To create a new project]

1. From the **Quick Start** section, click **Create new project**
2. A new project is created with a default name

    ![Create ADC Project](/help/forms/assets/adc-home.png)

3. Click **Edit project** in the top right corner

    ![Edit Project](/help/forms/assets/adc-edit-project.png)

4. Provide a meaningful name (e.g., "formsproject")
5. Click **Save**

    ![Edit Project Name](/help/forms/assets/adc-edit-projectname.png)

>[!TAB To navigate to your existing project]

1. Click **All Projects** from the Adobe Developer Console  

    ![Search Projects](/help/forms/assets/search-adc-project.png)

2. Locate your project and click to open it.

    ![Locate Projects](/help/forms/assets/locate-adc-project.png)

>[!ENDTABS]

### 2. Add Forms APIs

Add Forms APIs based on what you want to do:
   
* **AEM Forms Communications APIs**: use when you need to generate, convert, assemble, or secure documents (PDF and related formats).
* **Adaptive Forms Runtime APIs** – use when you need to render, submit, or process Adaptive Forms at runtime.

>[!BEGINTABS]

>[!TAB For AEM Forms Communications APIs]

1. Click **Add API** 

    ![Add api](/help/forms/assets/adc-add-api.png)

2. Select **Forms Communication APIs**
    1. In the _Add API_ dialog, filter by **Experience Cloud**
    2. Select **"Forms Communication APIs"**

        ![Add Forms Communication API](/help/forms/assets/adc-add-forms-api.png)

    3. Click **Next**
    4. Select **OAuth Server-to-Server** authentication method

        ![Select Authentication method](/help/forms/assets/adc-add-authentication-method.png)

>[!TAB For Adaptive Forms Runtime APIs]

1. **Click Add API**
   
    ![Add api](/help/forms/assets/adc-add-api.png)

2. **Select AEM Forms Delivery and Runtime API**
    1. In the _Add API_ dialog, filter by **Experience Cloud**
    2. Select **"AEM Forms Delivery and Runtime API"**
    ![Add Forms Communication API](/help/forms/assets/adc-add-runtime-api.png)

    3. Click **Next**
    4. Select **OAuth Server-to-Server** authentication method.
    ![Select Authentication method](/help/forms/assets/adc-add-authentication-method.png)

>[!ENDTABS]

You canalso  add the API and authentication method to your existing project by clicking **Add to Project** > **API**  
![Add API to existing Project](/help/forms/assets/add-api-existing-project.png)

### 3. Add Product Profile

Product profile provides permissions (or authorization) for credentials to access the AEM resources.

1. Select the **Product Profile** that matches your AEM instance URL (`https://Service Type -Environment Type-Program XXX-Environment XXX.adobeaemcloud.com`).  

    * **Service Type** –  specifies services or permissions associated with the AEM instance 

    * **Environment Type** – specifies whether the envrionment is for Author or Publish service

    * **Program XXX** – identifies the Cloud Manager program ID

    * **Environment XXX** – identifies the specific environment ID within that program

    >[!NOTE]
    >
    > Product profiles are tied to a specific AEM instance (program + environment). Always choose the profile that matches your instance URL.

2. Click **Save configured API**. The API and Product Profile are added to your project

    ![Select Project Configuration](/help/forms/assets/adc-add-product-profile.png)

### 4. Generate and Save Credentials

1. Navigate to your project in Adobe Developer Console
2. Click **OAuth Server-to-Server** credential
3. View the **Credential details** section

    ![View Credentials](/help/forms/assets/adc-view-credential.png)

**Record API Credentials**

```text
    API Credentials:
    ================
    Client ID: <your_client_id>
    Client Secret: <your_client_secret>
    Technical Account ID: <tech_account_id>
    Organization ID: <org_id>
    Scopes: AdobeID,openid,read_organizations
```

### 5. Access Token Generation

Generate the Access token either manually or programmatically:

>[!BEGINTABS]

>[!TAB For Testing]

Generate access tokens manually in Adobe Developer Console:

1. **Navigate to your Project**
    1. In Adobe Developer Console, open your project
    2. Click **OAuth Server-to-Server**

2. **Generate Access Token**
    1. Click the **"Generate access token"** button in your project's API section
    2. Copy the generated access token

    ![Generate Access Token](/help/forms/assets/adc-access-token.png)
    
    >[!NOTE]
    >
    > Access token is valid for only for **24 hours**

>[!TAB For Production]

Generate tokens programmatically using [Adobe IMS](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/setting-up-ims-integrations-for-aem-as-a-cloud-service) API:

**Required Credentials:**

* Client ID
* Client Secret
* Scopes (typically: `openid, AdobeID, read_organizations, additional_info.projectedProductContext, read_pc.dma_aem_cloud, aem.document`)

**Token Endpoint:**
    
```
https://ims-na1.adobelogin.com/ims/token/v3
```

**Sample Request (curl):**

```bash
curl -X POST 'https://ims-na1.adobelogin.com/ims/token/v3' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=client_credentials' \
-d 'client_id=<YOUR_CLIENT_ID>' \
-d 'client_secret=<YOUR_CLIENT_SECRET>' \
-d 'scope=AdobeID,openid,read_organizations'
```

**Response:**

```json
    {
    "access_token": "eyJhbGciOiJSUz...",
    "token_type": "bearer",
    "expires_in": 86399
    }
```

>[!ENDTABS]

You can now use the generated access token to make API call for development, stage, or production environments.

>![NOTE]
>
> To know more about OAuth Server-to-Server implementation to generate access token and make API calls, [click here](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/implementation).

## Best practices: Managing credentials for Development, Staging, and Production

* Always use separate credentials for Development, Staging, and Production.

* Map each credential to the correct AEM environment URL.

* Store secrets securely and never commit them to source control.

* Track access token validity, as tokens are valid for 24 hours only.

## Next Steps

To learn how to set up environment for Synchronous Forms Communication APIs, see [AEM Forms as a Cloud Service Communications Synchronous Processing](/help/forms/aem-forms-cloud-service-communications-on-demand-processing.md).


## Related Articles

Learn how to set environment for Synchronous (On-Demand) and Asynchronous (Batch) Forms Communications APIs:

<!-- START CARDS HTML - DO NOT MODIFY BY HAND -->
<div class="columns">
    <!-- Synchronous APIs Card -->
    <div class="column is-half-tablet is-half-desktop is-one-third-widescreen" aria-label="AEM Forms Communications APIs - Synchronous">
        <div class="card" style="height: 100%; display: flex; flex-direction: column;">
            <div class="card-image">
                <figure class="image x-is-16by9">
                    <a href="/help/forms/aem-forms-cloud-service-communications-on-demand-processing.md" title="Synchronous APIs" target="_self" rel="referrer">
                        <img class="is-bordered-r-small" src="/help/forms/assets/sync-api.png" alt="Synchronous APIs"
                             style="width: 100%; aspect-ratio: 16 / 9; object-fit: cover; overflow: hidden; display: block; margin: auto;">
                    </a>
                </figure>
            </div>
            <div class="card-content is-padded-small" style="display: flex; flex-direction: column; flex-grow: 1; justify-content: space-between;">
                <div class="top-card-content">
                    <p class="headline is-size-6 has-text-weight-bold">
                        <a href="/help/forms/aem-forms-cloud-service-communications-on-demand-processing.md" target="_self" rel="referrer" title="AEM Forms Communications APIs - Synchronous">AEM Forms Communications APIs - Synchronous</a>
                    </p>
                    <p class="is-size-6">Learn how to set up environment for Synchronous (on-demand) Forms Communications APIs that generate or process documents instantly. </p>
                </div>
                <a href="/help/forms/aem-forms-cloud-service-communications-on-demand-processing.md" target="_self" rel="referrer" class="spectrum-Button spectrum-Button--outline spectrum-Button--primary spectrum-Button--sizeM" style="align-self: flex-start; margin-top: 1rem;">
                    <span class="spectrum-Button-label has-no-wrap has-text-weight-bold">Learn more</span>
                </a>
            </div>
        </div>
    </div>
    <!-- Asynchronous APIs Card -->
    <div class="column is-half-tablet is-half-desktop is-one-third-widescreen" aria-label="AEM Forms Communications APIs - Asynchronous">
        <div class="card" style="height: 100%; display: flex; flex-direction: column;">
            <div class="card-image">
                <figure class="image x-is-16by9">
                    <a href="/help/forms/aem-forms-cloud-service-communications-batch-processing.md" title="AEM Forms Communications APIs - Asynchronous" target="_self" rel="referrer">
                        <img class="is-bordered-r-small" src="/help/forms/assets/async-api.png" alt="Asynchronous APIs"
                             style="width: 100%; aspect-ratio: 16 / 9; object-fit: cover; overflow: hidden; display: block; margin: auto;">
                    </a>
                </figure>
            </div>
            <div class="card-content is-padded-small" style="display: flex; flex-direction: column; flex-grow: 1; justify-content: space-between;">
                <div class="top-card-content">
                    <p class="headline is-size-6 has-text-weight-bold">
                        <a href="/help/forms/aem-forms-cloud-service-communications-batch-processing.md" target="_self" rel="referrer" title="Asynchronous APIs">AEM Forms Communications APIs - Asynchronous (Batch)</a>
                    </p>
                    <p class="is-size-6">Learn how to set up environment for Asynchronous (Batch) Forms Communications APIs that generate or process multiple documents in a scheduled manner.</p>
                </div>
                <a href="/help/forms/aem-forms-cloud-service-communications-batch-processing.md" target="_self" rel="referrer" class="spectrum-Button spectrum-Button--outline spectrum-Button--primary spectrum-Button--sizeM" style="align-self: flex-start; margin-top: 1rem;">
                    <span class="spectrum-Button-label has-no-wrap has-text-weight-bold">Learn more</span>
                </a>
            </div>
        </div>
    </div>
</div>
<!-- END CARDS HTML - DO NOT MODIFY BY HAND -->


