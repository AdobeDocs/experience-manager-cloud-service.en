---
title: Reusing Code Across Sites
description: If you have many similar sites that mostly look and behave the same, but have different content, learn how you can share code across multiple sites in a repoless model.
feature: Edge Delivery Services
role: Admin, Architect, Developer
---

# Reusing Code Across Sites {#repoless}

If you have many similar sites that mostly look and behave the same, but have different content, learn how you can share code across multiple sites in a repoless model.

## One Codebase for Multiple Sites {#one-codebase}

By default, AEM is tightly bound to your code repository, which meets the majority of use cases. However you may have multiple sites that differ mostly in their content, but could leverage the same code base.

Rather than creating multiple GitHub repositories and running each site off a dedicated GitHub repository while keeping them in sync, AEM supports running multiple sites from the same codebase.

This simplified setup, which eliminates the need for code replication is also known as "repoless", because all but your first site don't need a GitHub repository of their own.

If your project requires the repoless flexibility of code reuse across sites, you can activate the feature.

Regardless of how many sites you want to ultimately create in a repoless fashion, you must create your first site, which serves as your base site. This document explains how to create you first site for repoless use.

## Prerequisites {#prerequisites}

To take advantage of this feature, make sure you have done the following.

* Your site is already fully set up by following the document [Developer Getting Started Guide for WYSIWYG Authoring with Edge Delivery Services.](/help/edge/wysiwyg-authoring/edge-dev-getting-started.md)
* You are running AEM as a Cloud Service 2024.08 at a minimum.

You will also need to ask Adobe to configure two items for you. Reach out to Adobe via your Slack channel or raise a support issue to make these requests.

* The [aem.live configuration service](https://www.aem.live/docs/config-service-setup#prerequisites) is active for your environment and you are configured as an administrator.
* The repoless feature must be enabled for your org by Adobe.

## Activate Repoless Feature {#activate}

There are several steps to activate repoless functionality for your project.

1. [Retrieve access token](#access-token)
1. [Set up configuration service](#config-service)
1. [Set access control](#access-control)
1. [Update AEM configuration](#update-aem)
1. [Authenticate site](#authenticate-site)

These steps use the site `https://wknd.site` as an example. Substitute your own appropriately.

### Retrieve Access Token {#access-token}

You will first need an access token to use the configuration service and configure it for the repoless use case.

1. Go to `https://admin.hlx.page/login` and use the `login_adobe` address to login with the Adobe identity provider.
1. You will be forwarded to `https://admin.hlx.page/profile`.
1. Copy the value of the `x-auth-token` either from:
   * The JSON that the Adobe login service returns.
   * From the JSON web token cookie that the `admin.hlx.page` page sets by using your browser's developer tools.

Once you have your access token, it can be is passed in the header of cURL requests in the following format.

```text
--header 'x-auth-token: <your-token>'
```

### Configure Your Configuration Service {#config-service}

As mentioned in the [prerequisites,](#prerequisites) the configuration service must be enabled for your environment. You can check your configuration service setup with this cURL command.

```text
curl  --location 'https://admin.hlx.page/config/<your-github-org>.json' \
--header 'x-auth-token: <your-token>'
```

Reach out to Adobe via your project Slack channel or raise a support issue if your configuration service is not enabled. Once you have your token and verified that the configuration service is enabled, you can continue the configuration.

1. Check that your content source is set up properly.

   ```text
   curl --request GET \
   --url https://admin.hlx.page/config/<your-github-org>/sites/<your-aem-project>.json \
   --header 'x-auth-token: <your-token>'
   ```

1. Add a path mapping to the public configuration.

   ```text
   curl --request POST \
     --url https://admin.hlx.page/config/<your-github-org>/sites/<your-aem-project>/public.json \
     --header 'x-auth-token: id_token=<your-token>&idp_name=adobe' \
     --header 'Content-Type: application/json' \
     --data '{
       "paths": {
           "mappings": [
               "/content/<your-site-content>/:/"
      ],
           "includes": [
               "/content/<your-site-content>/"
           ]
       }
   }'
   ```

Once the public configuration is created, you can access it via a URL similar to `https://main--<your-aem-project>--<your-github-org>.aem.page/config.json` in order to verify it.

### Set Access Control {#access-control}

To set up access control, you need to provide the technical account.

1. Your site should already have a configuration assigned to it automatically as part of the site creation process. Confirm this by signing into the authoring instance and going to **Sites**, selecting your site and then **Properties** from the toolbar.
1. On the **Advanced** tab, you should see a configuration assigned in the **Cloud Configuration** field similar to `/conf/<conf-name>`. If not, [create a configuration and assign it to your site.](/help/implementing/developing/introduction/configurations.md)
1. Create a mapping in the public configuration to the site configuration using a cURL command similar to the following.
   ```text
   curl --request POST \
     --url https://admin.hlx.page/config/mhaack/sites/my-aem-project/public.json \
     --header 'x-auth-token: id_token=<your-token>&idp_name=adobe' \
     --header 'Content-Type: application/json' \
     --data '{
       "paths": {
           "mappings": [
               "/content/mh-aem-project/:/",
               "/content/mh-aem-project/configuration:/.helix/config.json"
      ],
           "includes": [
               "/content/mh-aem-project/"
           ]
       }
   }'
   ```
1. Validate that the public configuration has been set an is available with a cURL command similar to the following.
   ```text
   curl 'https://main--my-aem-project--mhaack.aem.live/config.json'
   ```
1. Now you can retrieve the technical account in the response of a cURL command similar to the following.
   ```text
   https://author-pXX-eYY.adobeaemcloud.com/bin/franklin.delivery/mhaack/my-aem-project/main/.helix/config.json
   ```
1. Set the technical account in your configuration with a cURL command similar to the following.
   ```text
   curl --request POST \
     --url https://admin.hlx.page/config/mhaack/sites/my-aem-project/access.json \
     --header 'Content-Type: application/json' \
     --header 'x-auth-token: id_token=<your-token>&idp_name=adobe' \
     --data '{
       "admin": {
           "role": {
               "admin": [
                   "*@adobe.com"
               ],
               "config_admin": [
                   "<--xyz-->@techacct.adobe.com"
               ]
           },
           "requireAuth": "auto"
       }
   }'
   ```
1. Since you now use the configuration service, you can remove `fstab.yaml` and `paths.json` from your Git repository.
   >[!NOTE]
   >
   >By using the configuration service and exposing the path mapping via `config.json`, the `path.json` file is ignored.
   >
   >Once AEM is configured for repoless use, you must use the configuration service and provide a valid `config.json` with the paths mapping.
1. Verify that the public configuration can be accessed by the project by accessing the `config.json` resource of your project such as `https://main--my-aem-project-mhaack.aem.page/config.json`

### Update AEM Configuration {#update-aem}

Now you are ready to make the necessary changes to your Edge Delivery Services in AEM.

1. Sign into the AEM author instance and go to **Tools** -&gt; **Cloud Configurations** -&gt; **Edge Delivery Services Configuration** and select the configuration that was automatically created for your site and tap or click **Properties** in the tool bar.
1. In the **Edge Delivery Services Configuration** window, change project type to **aem.live with repoless config setup** and tap or click **Save &amp; Close**.
   ![Edge Delivery Services Configuration](/help/edge/wysiwyg-authoring/assets/repoless/edge-delivery-services-configuration.png)
1. Return to your site using the Universal Editor and ensure that it still renders properly.
1. Modify some of your content and re-publish.
1. Visit your published site on `https://main--my-aem-project--mhaack.aem.page/` and verify that the changes are properly reflected.

### Authenticate Site {#authenticate-site}

To authenticate your preview and publish services, you will need to provide an authentication token to your **Edge Delivery Service Configuration** in AEM.

1. [Follow the process documented here](https://www.aem.live/docs/authentication-setup-site#create-a-token-to-access-your-protected-site) to generate an authentication token.
   * You will receive a site authentication token to access your protected site similar to `<site-auth-token>=hlx_ZGFzIGlzdCBkZWluIHRva2Vu`.
1. Sign into the AEM author instance and go to **Tools** -&gt; **Cloud Configurations** -&gt; **Edge Delivery Services Configuration** and select the configuration that was automatically created for your site and tap or click **Properties** in the tool bar.
1. In the **Edge Delivery Services Configuration** window, provide the `<site-auth-token>` value in the `Site Authentication Token` field and tap or click **Save &amp; Close**.
   ![Edge Delivery Services Configuration](/help/edge/wysiwyg-authoring/assets/repoless/site-authentication-token.png)

## Next Steps {#next-steps}

Now that your base site is configured for repoless usage, you can create additional sites that leverage the same code base. Refer to the following documentation depending on your use case.

* [Repoless Multi Site Management](help/edge/wysiwyg-authoring/repoless-msm.md)
* [Repoless Stage and Prod Environments](help/edge/wysiwyg-authoring/repoless-stage-prod.md)

## Troubleshooting {#troubleshooting}

The most common issue encountered after configuring the repoless use case is that pages in the Universal Editor no longer render or you receive a white page or a generic AEM as a Cloud Service error message. In such cases:

* View the source of the rendered page.
  * Is there actually something rendered (correct HTML head with `scripts.js`, `aem.js`, and editor-related JSON files)?
* Check the AEM `error.log` of the author instance for exceptions.
  * The most common issue is the page component fails with 404 errors.
  * `config.json or paths.json` can not be loaded
  * `component-definition.json` etc. can not be loaded
