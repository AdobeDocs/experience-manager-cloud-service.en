---
title: Getting started with AEM Commerce as a Cloud Service
description: Learn how to deploy a commerce-enabled AEM project to a running AEM as a Cloud service environment. Use features of Adobe Cloud Manager and a CI/CD pipeline to build the Venia reference storefront to a running environment.
topics: Commerce
feature: Commerce Integration Framework, Cloud Manager
version: cloud-service
doc-type: tutorial
kt: 4947
thumbnail: 37843.jpg
exl-id: 73ba707e-5e2d-459a-8cc8-846d1a5f2fd7
---
# Getting started with AEM Commerce as a Cloud Service {#start}

To get started with AEM Commerce as a Cloud Service, your Experience Manager Cloud Service needs to be provisioned with the Commerce Integration Framework (CIF) add-on. The CIF add-on is an additional module on top of [AEM Sites as a Cloud Service](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/sites/home.html).

## Onboarding {#onboarding}

The onboarding for AEM Commerce as a Cloud Service is a two-step process:

1. Get AEM Commerce as a Cloud Service enabled and the CIF add-on provisioned
2. Connect AEM Commerce as a Cloud Service with your commerce solution

The first onboarding step is done by Adobe. For more details on pricing and provisioning, you need to reach out to your sales representative.

Once you have been provisioned with the CIF add-on, it will be applied to any existing Cloud Manager programs. In case, you don't have a Cloud Manager Program, you will need to create a new one. For more details, refer to [Setup your Program](https://docs.adobe.com/content/help/en/experience-manager-cloud-manager/using/getting-started/setting-up-program.html).

The second step is self-service for each AEM as a Cloud Service environment. There are some additional configurations you will need to do after the initial provisioning of the CIF add-on.

## Connecting AEM with a commerce solution {#magento}

To connect the CIF add-on & the [AEM CIF Core Components](https://github.com/adobe/aem-core-cif-components) with a commerce solution, you need to provide the  GraphQL endpoint URL via a Cloud Manager environment variable. The variable name is `COMMERCE_ENDPOINT`. A secure connection via HTTPS must be configured.
A different  GraphQL endpoint URL can be used for each AEM as a Cloud Service environment. That way projects can connect AEM staging environments with commerce staging systems and AEM production environment to a commerce production system. That GraphQL endpoint must be publicly available, private VPN or local connections are not supported. Optionally, an authentication header can be provided in order to use additional CIF features that require authentication. 

There are two options to configure the endpoint:

### 1) Via Cloud Manager UI (Default)

This can be done using a dialog on the Environment Details page. When viewing this page for a Commerce-enabled program, a button will be displayed if the endpoint is not currently configured:

![Eco Friendly Badge Final Implementation](/help/commerce-cloud/assets/commerce-cmui.png)

Clicking this button opens a dialog:

![Eco Friendly Badge Final Implementation](/help/commerce-cloud/assets/commerce-cm-endpoint.png)
   
After the endpoint (and, optionally, the token) is set, the endpoint will be displayed on the detail page. Clicking the Edit icon will open the same dialog where the endpoint can be modified if necessary.

![Eco Friendly Badge Final Implementation](/help/commerce-cloud/assets/commerce-cmui-done.png)

### 2) Via Adobe I/O CLI

>[!VIDEO](https://video.tv.adobe.com/v/37843?quality=12&learn=on)

To connect AEM with a commerce solution via Adobe I/O CLI, follow these steps:

1. Get the Adobe I/O CLI with the Cloud Manager plugin

    Check the [Adobe Cloud Manager documenation](https://docs.adobe.com/content/help/en/experience-manager-cloud-manager/using/introduction-to-cloud-manager.html) on how to download, setup and use the [Adobe I/O CLI](https://github.com/adobe/aio-cli) with the [Cloud Manager CLI plugin](https://github.com/adobe/aio-cli-plugin-cloudmanager).

2. Authenticate the Adobe I/O CLI with the AEM as a Cloud Service program

3. Set the `COMMERCE_ENDPOINT` variable in Cloud Manager

    ```bash
    aio cloudmanager:set-environment-variables ENVIRONMENT_ID --variable COMMERCE_ENDPOINT "<Magento GraphQL endpoint URL>"
    ```

    See [CLI docs](https://github.com/adobe/aio-cli-plugin-cloudmanager#aio-cloudmanagerset-environment-variables-environmentid) for details.

    The commerce GraphQL endpoint URL must point to commerce's GraphQl service and use a secure HTTPS connection. For example: `https://demo.magentosite.cloud/graphql`.

>[!TIP]
>
>You can list all Cloud Manager variables using the following command to double-check: `aio cloudmanager:list-environment-variables ENVIRONMENT_ID`

With this, you are ready to use AEM Commerce as a Cloud Service and can deploy your project via Cloud Manager.

## Enable features that require authentication (Optional) {#staging}

>[!NOTE]
>
>This feature is only available with Magento Enterprise Edition or Magento Cloud.

1. Login to Magento and create an integration token. See [Token-based authentication](https://devdocs.magento.com/guides/v2.4/get-started/authentication/gs-authentication-token.html#integration-tokens) for details. Make sure the integration token has *only* access to `Content -> Staging` resources. Copy the `Access Token` value.

1. Set the `COMMERCE_AUTH_HEADER` secret variable in Cloud Manager:

    ```bash
    aio cloudmanager:set-environment-variables ENVIRONMENT_ID --secret COMMERCE_AUTH_HEADER "Authorization: Bearer <Access Token>"
    ```

    Please see [Connecting AEM Commerce with Magento](#magento) on how to configure the Adobe I/O CLI for Cloud Manager.

## 3rd party commerce integrations {#integrations}

For 3rd party commerce integrations, an [API mapping layer](architecture/third-party.md) is needed to connect AEM Commerce as a Cloud Service and CIF Core Components with your commerce system. This API mapping layer is typically deployed on Adobe I/O Runtime. Contact your sales representative for available integrations and access to Adobe I/O Runtime.
