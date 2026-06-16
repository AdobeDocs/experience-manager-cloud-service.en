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

This article describes how to keep a single, portable Adaptive Form and have its [Submit to REST endpoint](/help/forms/configure-submit-action-restpoint.md) action resolve to the correct endpoint in each environment. The form references a REST configuration *by name* instead of by URL, and each environment supplies its own value for that configuration.

## Prerequisites {#prerequisites}

* An Adaptive Form based on Core Components.
* A [Configuration Container](/help/implementing/developing/introduction/configurations.md) created through the Configuration Browser (**Tools** > **General** > **Configuration Browser**) with **Cloud Configurations** enabled.
* Permission to access **Tools** > **Cloud Services** and, for promotion, [Package Manager](/help/implementing/developing/tools/package-manager.md) on each environment (or a [Cloud Manager deployment pipeline](/help/implementing/deploying/overview.md#deploying-content-packages-via-cloud-manager-and-package-manager)).

## Create the RESTful service configuration on staging {#create-rest-configuration}

>[!VIDEO](https://video.tv.adobe.com/v/3492383)

On the staging author instance, create the named configuration that your form refers to. Set the **Service Endpoint URL** to the REST or webhook endpoint for staging.

1. Go to **Tools** > **Cloud Services** > **Data Sources**.

1. Select your Configuration Container, then select **Create**.

1. On the **General** tab, provide a **Name** for the configuration (for example, `restTest`). Use the *same* name on every environment so the form resolves consistently after promotion.

1. On the **Authentication Settings** tab, configure:

   * **Select RESTful Service**: **Service Endpoint**.
   * **Method Type**: **POST**.
   * **Service Endpoint URL**: the staging endpoint URL (for example, a webhook URL you use to test submissions from staging).
   * **Content Type**: for example, **Multi-Part Form Data**.
   * **Authentication Type**: as required by your endpoint (for example, **None** or **Basic Authentication**).

1. Select **Save & Close**.

## Point the Adaptive Form at the Configuration Container {#set-configuration-container}

>[!VIDEO](https://video.tv.adobe.com/v/3492384)

On staging, associate the form with the Configuration Container that holds your REST configuration.

1. In **Forms & Documents**, select your Adaptive Form and open **Properties**.

1. On the **Basic** tab, set **Configuration Container** to the container that holds your RESTful service configuration (for example, `/conf/restConfigTest`).

1. Select **Save & Close**.

## Configure the Submit to REST endpoint action {#configure-submit-action}

>[!VIDEO](https://video.tv.adobe.com/v/3492385)

On staging, configure the form to submit through the named REST configuration instead of a hardcoded URL. For the full submit action reference, see [Configure an Adaptive Form for REST Endpoint submit action](/help/forms/configure-submit-action-restpoint.md).

1. Open the Adaptive Form for editing, select the **Guide Container** component, and open its **Adaptive Form Container** properties.

1. Open the **Submission** tab and, from the **Submit Action** drop-down list, select **Submit to REST endpoint**.

1. Under **Action Configuration**, select **Enable POST request**.

1. For **Select an option**, choose **Configuration** (not **URL**).

1. Select your named configuration (for example, `restTest`) from the list.

1. Select **Done**.

The form now resolves its submission endpoint through the named configuration rather than a fixed URL.

## Promote the form from staging to production {#promote-across-environments}

After you configure and test on staging, move the same form and Configuration Container to production. You can use either of the following approaches.

### Option 1: Author and package approach {#option-package}

>[!VIDEO](https://video.tv.adobe.com/v/3492386)

Use this when authors maintain the form and configuration directly in each environment.

1. On the **staging** author instance, build a content package in [Package Manager](/help/implementing/developing/tools/package-manager.md) that includes the form and its Configuration Container, for example:

   * `/content/dam/formsanddocuments/<your-form-path>`
   * `/content/forms/af/<your-form-path>`
   * `/conf/<your-config-container>` (which contains `.../settings/cloudconfigs/fdm/<your-config>`)

1. Download the package and install it on the **production** author instance.

>[!IMPORTANT]
>
>The package installs the same configuration on production, including the **Service Endpoint URL** from staging. Do not leave that staging URL in place on production. Update the endpoint on production after installation, as described in the next section.

### Option 2: Context-aware override approach (recommended for automation) {#option-context-aware}

Use this when you want one packaged configuration whose endpoint, user name, and password resolve automatically per environment, with no manual editing after deployment. This approach overrides configuration properties using Cloud Manager environment variables.

For REST configurations, you typically create environment variables for the `serviceEndPoint`, `userName`, and `password` properties, then reference them from an `OsgiConfigurationOverrideProvider` configuration file in your project.

For the full procedure, see [Context Aware Cloud Configurations](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/forms/developing-for-cloud-service/context-aware-fdm).

## Update the endpoint URL on production {#configure-endpoint-on-production}

>[!VIDEO](https://video.tv.adobe.com/v/3492387)

After you install the package on production, the Adaptive Form and the REST configuration **name** (for example, `restTest`) match staging. The **Service Endpoint URL** in that configuration still points to the staging endpoint from the package. Open the configuration on production and replace it with the production endpoint URL.

1. On the **production** author instance, go to **Tools** > **Cloud Services** > **Data Sources**.

1. Select the Configuration Container you deployed (for example, `restConfigTest`), then open the named configuration (for example, `restTest`).

1. On the **Authentication Settings** tab, set **Service Endpoint URL** to the production REST or webhook endpoint.

1. Select **Save & Close**.

During testing, a request inspector such as a webhook capture service gives you a unique URL per environment so you can confirm which endpoint receives each submission.

## Verify the routing {#verify}

>[!VIDEO](https://video.tv.adobe.com/v/3492388)

Submit the same form from staging and production and confirm each environment posts to its own endpoint—not the other environment's URL.

1. On the **staging** author instance, open the Adaptive Form and submit it with test data (for example, enter `stagetest` in a text field). Confirm the POST request arrives at the **staging** **Service Endpoint URL** you configured on staging.

1. On the **production** author instance, open the same Adaptive Form and submit it with test data (for example, enter `prodtest` in a text field). Confirm the POST request arrives at the **production** **Service Endpoint URL** you configured on production—not the staging URL.

1. Confirm each request uses the expected content type (for example, **Multi-Part Form Data**) and includes the submitted form data. Use a real, secured endpoint (HTTPS) for production.

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
