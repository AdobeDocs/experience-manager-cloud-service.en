---
title: Configure environment-specific REST endpoints for the same Adaptive Form | Adobe Experience Manager as a Cloud Service
description: Learn how to route the same Adaptive Form to different REST submission endpoints across your development, staging, and production environments without changing the form.
feature: Adaptive Forms, Core Components
role: User, Developer
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: 40410875-96d0-4728-8cbd-b1e1dfa438c4
---

# Configure environment-specific REST endpoints for the same Adaptive Form

When you promote an Adaptive Form from development to staging to production, the form usually needs to submit to a *different* REST endpoint in each environment, while the form itself stays identical. Hardcoding the endpoint URL in the form's submit action breaks this, because the same URL then travels with the form to every environment.

This article describes how to keep a single, portable Adaptive Form and have its **Submit to REST endpoint** action resolve to the correct endpoint in each environment. The form references a REST configuration *by name* instead of by URL, and each environment supplies its own value for that configuration.

For the field-level reference of the **Submit to REST endpoint** action itself, see [Configure an Adaptive Form for REST Endpoint submit action](/help/forms/configure-submit-action-restpoint.md).

## How it works {#how-it-works}

Three pieces work together to make the form portable:

* **The Adaptive Form** references a **Configuration Container** (for example, `/conf/restConfigTest`) in its form properties, rather than pointing at a URL.
* **The Configuration Container** holds a **RESTful service data source configuration** (for example, a configuration named `restTest`). This configuration stores the actual endpoint URL, content type, and authentication settings.
* **The Submit to REST endpoint action** on the form selects the **Configuration** option and chooses that named configuration, instead of entering a URL directly.

Because the form refers to the configuration *by name*, you can deploy the identical form to every environment. Each environment holds a configuration of the same name, but with an endpoint value appropriate to that environment. At submission time, the form resolves the name to whatever endpoint that environment defines.

>[!NOTE]
>
>The capability to specify the REST endpoint using a configuration applies to Adaptive Forms based on Core Components and Edge Delivery Services Forms. Confirm the current availability and any program enrollment requirement for the **Service Endpoint** capability before you rely on it in production. See [Configure data sources](/help/forms/configure-data-sources.md#configure-restful-services-service-endpoint).

## Prerequisites {#prerequisites}

* An Adaptive Form based on Core Components.
* A [Configuration Container](/help/implementing/developing/introduction/configurations.md) created through the Configuration Browser (**Tools** > **General** > **Configuration Browser**) with **Cloud Configurations** enabled.
* Permission to access **Tools** > **Cloud Services** and, for promotion, **CRX Package Manager** on each environment (or a Cloud Manager deployment pipeline).

## Create the RESTful service configuration {#create-rest-configuration}

Create the named configuration that your form refers to. Repeat this on each environment, supplying that environment's endpoint value.

1. On the AEM Forms author instance, go to **Tools** > **Cloud Services** > **Data Sources**.

1. Select your Configuration Container, then select **Create**.

1. On the **General** tab, provide a **Name** for the configuration (for example, `restTest`). Use the *same* name on every environment so the form resolves consistently.

1. On the **Authentication Settings** tab, configure:

   * **Select RESTful Service**: **Service Endpoint**.
   * **Method Type**: **POST**.
   * **Service Endpoint URL**: the endpoint for *this* environment, for example a development endpoint on the development instance and a production endpoint on the production instance.
   * **Content Type**: for example, **Multi-Part Form Data**.
   * **Authentication Type**: as required by your endpoint (for example, **None** or **Basic Authentication**).

   >[!NOTE]
   >
   >Author capture: replace the placeholder above with a screenshot of the **Authentication Settings** tab for the `restTest` configuration.

1. Select **Save & Close**.

## Point the Adaptive Form at the Configuration Container {#set-configuration-container}

1. In **Forms & Documents**, select your Adaptive Form and open **Properties**.

1. On the **Basic** tab, set **Configuration Container** to the container that holds your RESTful service configuration (for example, `/conf/restConfigTest`).

1. Select **Save & Close**.

## Configure the Submit to REST endpoint action {#configure-submit-action}

1. Open the Adaptive Form for editing, select the **Guide Container** component, and open its **Adaptive Form Container** properties.

1. Open the **Submission** tab and, from the **Submit Action** drop-down list, select **Submit to REST endpoint**.

1. Under **Action Configuration**, select **Enable POST request**.

1. For **Select an option**, choose **Configuration** (not **URL**).

1. Select your named configuration (for example, `restTest`) from the list.

1. Select **Done**.

The form now resolves its submission endpoint through the named configuration rather than a fixed URL.

## Promote the form across environments {#promote-across-environments}

You can move the portable form between environments in two ways. Choose based on how much you want to automate.

### Author and package approach {#option-package}

Use this when authors maintain the form and configuration directly in each environment.

1. On the source environment, build a content package in **CRX Package Manager** that includes the form and its Configuration Container, for example:

   * `/content/dam/formsanddocuments/<your-form-path>`
   * `/content/forms/af/<your-form-path>`
   * `/conf/<your-config-container>` (which contains `.../settings/cloudconfigs/fdm/<your-config>`)

1. Download the package and install it on the target environment.

1. On the target environment, open the configuration (**Tools** > **Cloud Services** > **Data Sources**) and set its **Service Endpoint URL** to that environment's endpoint.

>[!IMPORTANT]
>
>In AEM as a Cloud Service, content packages deployed through a pipeline are installed on all environment types. Because the endpoint value differs per environment, maintain the per-environment value directly on each environment (or use the override approach in Option 2) rather than shipping a single hardcoded value to all of them.

## Verify the routing {#verify}

1. Open and submit the form on one environment (for example, staging). Confirm the submission reaches that environment's endpoint.

1. Repeat on another environment (for example, production). Confirm the submission reaches the *different* endpoint that the environment defines.

During testing, a request inspector such as a webhook capture service is a quick way to confirm that each environment posts to its own endpoint with the expected content type and payload. Use a real, secured endpoint for production.

## Best practices {#best-practices}

* Use an identical configuration **name** on every environment so the form resolves consistently after promotion.
* Keep the endpoint **value** environment-specific. Never hardcode a single environment's URL into the form's submit action.
* For production endpoints, ensure the URL is secure (HTTPS) and that the receiving path is configured to handle the POST request appropriately for your authentication model.
* Prefer the context-aware override approach when you want deployment to be repeatable and free of manual post-deployment edits.

## Related articles {#related-articles}

* [Configure an Adaptive Form for REST Endpoint submit action](/help/forms/configure-submit-action-restpoint.md)
* [Configure data sources](/help/forms/configure-data-sources.md)
* [Context Aware Cloud Configurations](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/forms/developing-for-cloud-service/context-aware-fdm)
* [Adaptive Form Submit Action](/help/forms/aem-forms-submit-action.md)
