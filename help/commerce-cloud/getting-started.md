---
title: Getting started with AEM Commerce as a Cloud Service
description: Learn how to deploy an Adobe Experience Manager (AEM) commerce project, using Adobe Cloud Manager, a CI/CD pipeline, and the Venia reference storefront.
topics: Commerce
feature: Commerce Integration Framework, Cloud Manager
version: Experience Manager as a Cloud Service
doc-type: tutorial
kt: 4947
thumbnail: 37843.jpg
exl-id: 73ba707e-5e2d-459a-8cc8-846d1a5f2fd7
role: Admin
---
# Getting started with AEM Commerce as a Cloud Service {#start}

To get started with Adobe Experience Manager (AEM) Commerce as a Cloud Service, your Experience Manager Cloud Service must be provisioned with the Commerce Integration Framework (CIF) add-on. The CIF add-on is an extra module on top of [AEM Sites as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/home.html).

## Onboarding {#onboarding}

The onboarding for AEM Commerce as a Cloud Service is a two-step process:

1. Get AEM Commerce as a Cloud Service enabled and the CIF add-on provisioned
2. Connect AEM Commerce as a Cloud Service with your commerce solution

The first onboarding step is done by Adobe. For more details on pricing and provisioning, you must reach out to your sales representative.

After you are provisioned with the CIF add-on, it is applied to any existing Cloud Manager programs. In case you do not have a Cloud Manager Program, you must create one. For more details, see [Set up your Program](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/content/getting-started/program-setup.html).

The second step is self-service for each AEM as a Cloud Service environment. There are some additional configurations that you must do after the initial provisioning of the CIF add-on.

## Connecting AEM with a Commerce Solution {#solution}

To connect the CIF add-on & the [AEM CIF Core Components](https://github.com/adobe/aem-core-cif-components) with a commerce solution, you must provide the GraphQL endpoint URL by way of a Cloud Manager environment variable. The variable name is `COMMERCE_ENDPOINT`. A secure connection by way of HTTPS must be configured.

This environment variable is used in two places:

- GraphQL calls from AEM to commerce backend, by way of some common shareable GraphQl client, used by the AEM CIF Core Components and customer project components.
- Set up a GraphQL proxy URL on each AEM environment the variable is set available at `/api/graphql`. This URL is used by the AEM commerce authoring tools (CIF add-on) and CIF client-side components.

A different  GraphQL endpoint URL can be used for each AEM as a Cloud Service environment. That way projects can connect AEM staging environments with commerce staging systems and AEM production environment to a commerce production system. That GraphQL endpoint must be publicly available, private VPN or local connections are not supported. Optionally, an authentication header can be provided to use additional CIF features that require authentication.

Optionally, and only for Adobe Commerce Enterprise / Cloud, the CIF add-on supports the use of staged catalog data for AEM authors. This data requires that you configure an authorization header. This header is only available and used on AEM Author instances for security reasons. AEM Publish instances cannot show staged data.

There are two options to configure the endpoint:

### By way of Cloud Manager user interface (Default) {#cm-ui}

>[!VIDEO](https://video.tv.adobe.com/v/37843?quality=12&learn=on)

This configuration can be done using a dialog box on the Environment Details page. When viewing this page for a Commerce-enabled program, a button is displayed if the endpoint is not currently configured:

![CM Enviornment Information](/help/commerce-cloud/assets/commerce-cmui.png)

Clicking this button opens a dialog box:

![CM Commerce Endpoint](/help/commerce-cloud/assets/commerce-cm-endpoint.png)

After the endpoint and optionally an authorization header for staged catalog support is set, the endpoint is displayed on the detail page. Clicking the Edit icon to open the same dialog box where you can edit the endpoint, if necessary.

![CM Enviornment Information](/help/commerce-cloud/assets/commerce-cmui-done.png)

### By way of Adobe I/O CLI  {#adobe-cli}

To connect AEM with a commerce solution by way of Adobe I/O CLI, follow these steps:

1. Get the Adobe I/O CLI with the Cloud Manager plugin

    Check the [Adobe Cloud Manager documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/content/introduction.html) on how to download, setup, and use the [Adobe I/O CLI](https://github.com/adobe/aio-cli) with the [Cloud Manager CLI plugin](https://github.com/adobe/aio-cli-plugin-cloudmanager).

2. Authenticate the Adobe I/O CLI with the AEM as a Cloud Service program

3. Set the `COMMERCE_ENDPOINT` variable in Cloud Manager

    ```bash
    aio cloudmanager:set-environment-variables ENVIRONMENT_ID --variable COMMERCE_ENDPOINT "<Magento GraphQL endpoint URL>"
    ```

    See [CLI docs](https://github.com/adobe/aio-cli-plugin-cloudmanager#aio-cloudmanagerset-environment-variables-environmentid) for details.

    The commerce GraphQL endpoint URL must point to commerce's GraphQl service and use a secure HTTPS connection. For example: `https://<yourcommercesystem>/graphql`.

4. Enable Staged catalog features that require authentication (Optional)

    >[!NOTE]
    >
    >This feature is only available with Adobe Commerce Enterprise or Cloud Edition. See [Token-based authentication](https://devdocs.magento.com/guides/v2.4/get-started/authentication/gs-authentication-token.html#integration-tokens) for details.

    Set the `COMMERCE_AUTH_HEADER` secret variable in Cloud Manager:

    ```bash
    aio cloudmanager:set-environment-variables ENVIRONMENT_ID --secret COMMERCE_AUTH_HEADER "Authorization: Bearer <Access Token>"
    ```

>[!TIP]
>
>You can list all Cloud Manager variables using the following command to double-check: `aio cloudmanager:list-environment-variables ENVIRONMENT_ID`

You are ready to use AEM Commerce as a Cloud Service and can deploy your project by way of Cloud Manager.

## Configuring stores and catalogs {#catalog}

The CIF add-on and the [CIF Core Components](https://github.com/adobe/aem-core-cif-components) can be used on multiple AEM site structures connected to different commerce stores (or store views, and so on). By default, the CIF add-on is deployed with a default config connecting to Adobe Commerce's default store and catalog.

This configuration can be adjusted for the project by way of the CIF Cloud Service config following these steps:

1. In AEM go to Tools > Cloud Services > CIF Configuration.

2. Select the commerce configuration that you want to change.

3. Open the configuration properties by way of the action bar.

![CIF Cloud Services Configuration](/help/commerce-cloud/assets/cif-cloud-service-config.png)

The following properties can be configured:

- GraphQL Client - select the configured GraphQL client for commerce backend communication. This client should typically stay at default.
- Store View - the store view identifier. If empty, the default store view is used.
- GraphQL Proxy Path - the URL path GraphQL Proxy in AEM use to proxy requests to the commerce backend GraphQL endpoint.
    >[!NOTE]
    >
    > In most setups, the default value `/api/graphql` must not be changed. Only advanced setup not using the provided GraphQL proxy should change this setting.
- Enable Catalog UID Support - enable support for UID instead of ID in the commerce backend GraphQL calls.
    >[!NOTE]
    >
    > Support for UIDs got introduced in Adobe Commerce 2.4.2. Only enable UIDs if your commerce backend supports a GraphQL schema of version 2.4.2 or later.
- Catalog Root Category Identifier - the identifier (UID or ID) of the store catalog root
    >[!CAUTION]
    >
    > Starting with CIF Core Components version 2.0.0 the support for `id` was removed and replaced with `uid`. If your project uses CIF Core Components version 2.0.0 you must enable Catalog UID Support and use a valid category UID as "Catalog Root Category Identifier".

The configuration shown above is for reference. Projects should provide their own configurations.

For more complex setups, using multiple AEM site structures combined with different commerce catalogs see the [Commerce Multi-Store Setup](configuring/multi-store-setup.md) tutorial.

## Additional Resources {#additional-resources}

- [AEM Project Archetype](https://github.com/adobe/aem-project-archetype)
- [AEM Venia Reference Store](https://github.com/adobe/aem-cif-guides-venia)
- [Commerce Multi-Store Setup](configuring/multi-store-setup.md)
- [Multiple Commerce Systems Setups](configuring/multiple-commerce-systems-setup.md)

