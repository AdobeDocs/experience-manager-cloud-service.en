---
title: Path to your first storefront
description: Learn how to get your first storefront.
index: no
hide: yes
hidefromtoc: yes
---
# Path to your first storefront {#first-storefront}

Learn how to get your first storefront.

## The Story So Far {#story-so-far}

In the previous document of the AEM Content and Commerce developer journey, [Getting Started with AEM Storefront](getting-started.md), you learned about the AEM Storefront and you should:

* Understand how to connect AEM with a commerce solution.
* Know more about AEM storefront.

This article builds on those fundamentals.

## Objective {#objective}

This document shows you how to get your first storefront. After reading you should:

* Have a functioning storefront.

## Connecting AEM with a Commerce Solution {#magento}

To connect the CIF add-on & the [AEM CIF Core Components](https://github.com/adobe/aem-core-cif-components) with a commerce solution, you need to provide the  GraphQL endpoint URL via a Cloud Manager environment variable. The variable name is `COMMERCE_ENDPOINT`. A secure connection via HTTPS must be configured.

This environment variable is used in two places:

* GraphQL calls from AEM to commerce backend, via some common shareable GraphQl client, used by the AEM CIF Core Components and customer project components.
* Setup a GraphQL proxy URL on each AEM environment the variable is set available at `/api/graphql`. This is used by the AEM commerce authoring tools (CIF add-on) and CIF client-side components.

A different  GraphQL endpoint URL can be used for each AEM as a Cloud Service environment. That way projects can connect AEM staging environments with commerce staging systems and AEM production environment to a commerce production system. That GraphQL endpoint must be publicly available, private VPN or local connections are not supported. Optionally, an authentication header can be provided in order to use additional CIF features that require authentication.

Optional and only for Adobe Commerce Enterprise / Cloud the CIF add-on supports the use of staged catalog data for AEM authors. This requieres to configure an authorization token. The configured authorization token is only available and used on AEM author instances for security reasons. AEM publish instances cannot show staged data.

There are two options to configure the endpoint:

### Via Cloud Manager UI (Default) {#cm-ui}

This can be done using a dialog on the Environment Details page. When viewing this page for a Commerce-enabled program, a button will be displayed if the endpoint is not currently configured:

![CM Enviornment Information](/help/commerce-cloud/assets/commerce-cmui.png)

Clicking this button opens a dialog:

![CM Commerce Endpoint](/help/commerce-cloud/assets/commerce-cm-endpoint.png)

After the endpoint (optionally an authentication token for staged catalog support) is set, the endpoint will be displayed on the detail page. Clicking the Edit icon will open the same dialog where the endpoint can be modified if necessary.

![CM Enviornment Information](/help/commerce-cloud/assets/commerce-cmui-done.png)

### Via Adobe I/O CLI  {#adobe-cli}

>[!VIDEO](https://video.tv.adobe.com/v/37843?quality=12&learn=on)

To connect AEM with a commerce solution via Adobe I/O CLI, follow these steps:

1. Get the Adobe I/O CLI with the Cloud Manager plugin

    Check the [Adobe Cloud Manager documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/introduction-to-cloud-manager.html) on how to download, setup and use the [Adobe I/O CLI](https://github.com/adobe/aio-cli) with the [Cloud Manager CLI plugin](https://github.com/adobe/aio-cli-plugin-cloudmanager).

2. Authenticate the Adobe I/O CLI with the AEM as a Cloud Service program

3. Set the `COMMERCE_ENDPOINT` variable in Cloud Manager

    ```bash
    aio cloudmanager:set-environment-variables ENVIRONMENT_ID --variable COMMERCE_ENDPOINT "<Magento GraphQL endpoint URL>"
    ```

    See [CLI docs](https://github.com/adobe/aio-cli-plugin-cloudmanager#aio-cloudmanagerset-environment-variables-environmentid) for details.

    The commerce GraphQL endpoint URL must point to commerce's GraphQl service and use a secure HTTPS connection. For example: `https://<yourmagentosystem>/graphql`.

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

With this, you are ready to use AEM Commerce as a Cloud Service and can deploy your project via Cloud Manager.


## What's Next {#what-is-next}

Now that you have completed this part of journey you should:

* have a functioning storefront.

Build on this knowledge and continue your journey by next reviewing the document [Integration of product catalog](catalog-integration.md).

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the journey by reviewing the document [Integration of product catalog](catalog-integration.md), the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the journey.

* [Getting started with AEM Commerce as a Cloud Service](/help/commerce-cloud/getting-started.md) - Learn how to deploy a commerce-enabled AEM project to a running AEM as a Cloud service environment.
