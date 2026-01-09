---
title: How to set up JWT (JSON Web Token) Authentication?
description: Learn how to configure JWT (JSON Web Token) authentication for Adobe Experience Manager Forms as a Cloud Service
role: Admin, Developer, User
feature: Adaptive Forms, APIs & Integrations
hide: yes
hidefromtoc: yes
index: no
---

# JWT (JSON Web Token) Authentication 

JWT authentication in AEM Forms, particularly for server-side integrations with AEM as a Cloud Service, involves a specific process to securely interact with AEM services.

## Prerequisites

Before you begin, make sure the following prerequisites are met:

* Ensure that you have access to the [Adobe Cloud Manager](https://experience.adobe.com/#/@formsinternal01/cloud-manager/landing.html) specific to the environment you use.
* Assign the System Administrator or Developer role to access Adobe Cloud Manager.

## How to Generate an Access Token Using JWT Credentials?

Follow the steps below which shows you how to generate an access token from the JWT credentials.

1. **Adobe Cloud Manager**

   1. Log in to your [Cloud Manager account](https://experience.adobe.com/#/@formsinternal01/cloud-manager/landing.html).
   2. On your selected program, click **[!UICONTROL Program Overview]**.

        ![Cloud Manager Account](/help/forms/assets/jwt-cloud-manager-landing.png)

   3. On your program, click three-dots menu and select **[!UICONTROL Developer Console]**.

        ![Developer Console](/help/forms/assets/jwt-developer-console.png)

2. **AEM Developer Console**
   1. Login in AEM Developer Console
   2. Click **[!UICONTROL Integrations]** located on the upper menu bar.

        ![Integrations](/help/forms/assets/jwt-integrations.png)

   3. Click the option to **[!UICONTROL Create new technical account]**.

        ![Create new technical account](/help/forms/assets/jwt-creae-new-tech-account.png)

    Once you click on create a new technical account, required information to generate access token such as client id and client secret along with other technical account information including private key, public key, expiration date generates.

    ![JWT  Credentials](/help/forms/assets/jwt-credentials.png)


3. Generate and Save Credentials

   1. Record API Credentials

        ```text
        API Credentials:
        ================
        Client ID: <your_client_id>
        Client Secret: <your_client_secret>
        Technical Account ID: <tech_account_id>
        Organization ID: <org_id>
        Scopes: AdobeID,openid,read_organizations
        ```

4. Access Token Generation

    Generate tokens programmatically using cURL command:

    **Required Credentials:**

      * Client ID
      * Client Secret
      * Scopes (typically: `openid, AdobeID, read_organizations, additional_info.projectedProductContext, read_pc.dma_aem_cloud, aem.document`)

    **Token Endpoint:**
    
    ```
    https://ims-na1.adobelogin.com/ims/token/v3
    ```

    **Sample Request (cURL):**

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


>[!NOTE]
>
> To learn more about service credentials and how to generate an access token using the Adobe IMS API, [click here](https://experienceleague.adobe.com/en/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials).

You can now use the generated access token to make API call for development, stage, or production environments.

## Related Article Steps

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


