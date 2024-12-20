---
title: Reusing Code Across Sites
description: If you have many similar sites that mostly look and behave the same, but have different content, learn how you can share code across multiple sites in a repoless model.
feature: Edge Delivery Services
role: Admin, Architect, Developer
exl-id: a6bc0f35-9e76-4b5a-8747-b64e144c08c4
---
# Reusing Code Across Sites {#repoless}

If you have many similar sites that mostly look and behave the same, but have different content, learn how you can share code across multiple sites in a repoless model.

## One Codebase for Multiple Sites {#one-codebase}

By default, AEM is tightly bound to your code repository, which meets the majority of use cases. However you may have multiple sites that differ mostly in their content, but could leverage the same code base.

Rather than creating multiple GitHub repositories and running each site off a dedicated GitHub repository while keeping them in sync, AEM supports running multiple sites from the same codebase.

This simplified setup, which eliminates the need for code replication is also known as ["repoless",](https://www.aem.live/docs/repoless) because all but your first site don't need a GitHub repository of their own.

If your project requires the repoless flexibility of code reuse across sites, you can activate the feature.

Regardless of how many sites you want to ultimately create in a repoless fashion, you must create your first site, which serves as your base site. This document explains how to create you first site for repoless use.

## Prerequisites {#prerequisites}

To take advantage of this feature, make sure you have done the following.

* Your site is already fully set up by following the document [Developer Getting Started Guide for WYSIWYG Authoring with Edge Delivery Services.](/help/edge/wysiwyg-authoring/edge-dev-getting-started.md)
* You are running AEM as a Cloud Service 2024.08 at a minimum.

You will also need to ask Adobe to configure two items for you. Reach out to Adobe via your Slack channel or raise a support issue to make these requests.

* The [aem.live configuration service](https://www.aem.live/docs/config-service-setup#prerequisites) is active for your environment and you are configured as an administrator.
* The repoless feature must be enabled for your program by Adobe.

## Activate Repoless Feature {#activate}

There are several steps to activate repoless functionality for your project.

1. [Retrieve access token](#access-token)
1. [Set up configuration service](#config-service)
1. [Add site configuration and technical account](#access-control)
1. [Update AEM configuration](#update-aem)
1. [Authenticate site](#authenticate-site)

These steps use the site `https://wknd.site` as an example. Substitute your own appropriately.

### Retrieve Access Token {#access-token}

You will first need an access token to use the configuration service and configure it for the repoless use case.

1. Go to `https://admin.hlx.page/login` and use the `login_adobe` address to login with the Adobe identity provider.
1. You will be forwarded to `https://admin.hlx.page/profile`.
1. By using your browser's developer tools, copy the value of the `x-auth-token` either from the JSON web token cookie that the `admin.hlx.page` page sets.

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

If the configuration service is set up properly, JSON similar to the following will be returned.

```json
{
  "title": "<your-github-org>",
  "description": "Your GitHub Org",
  "lastModified": "2024-11-14T12:14:04.230Z",
  "created": "2024-11-14T12:13:37.032Z",
  "version": 1,
  "users": [
    {
      "email": "justthisguyyouknow@adobe.com",
      "roles": [
        "admin"
      ],
      "id": "<your-id>"
    }
  ]
}
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
     --header 'x-auth-token: <your-token>' \
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

### Add Path Mapping for Site Configuration and Set Technical Account {#access-control}

You need to create a site configuration and add it to your path mapping.

1. Create a new page at the root of your site and choose the [**Configuration** template.](/help/edge/wysiwyg-authoring/tabular-data.md#other)
   * You can leave the configuration empty with only the predefined `key` and `value` columns. You only need to create it.
1. Create a mapping in the public configuration to the site configuration using a cURL command similar to the following.
   ```text
   curl --request POST \
     --url https://admin.hlx.page/config/<your-github-org>/sites/<your-aem-project>/public.json \
     --header 'x-auth-token: <your-token>' \
     --header 'Content-Type: application/json' \
     --data '{
       "paths": {
           "mappings": [
               "/content/<your-site-content>/:/",
               "/content/<your-site-content>/configuration:/.helix/config.json"
      ],
           "includes": [
               "/content/<your-site-content>/"
           ]
       }
   }'
   ```
1. Validate that the public configuration has been set an is available with a cURL command similar to the following.
   ```text
   curl 'https://main--<your-aem-project>--<your-github-org>.aem.live/config.json'
   ```

Once the site configuration is mapped, you can configure access control by defining your technical account so it has privileges to publish.

1. In your browser, retrieve the technical account in the response of the following link.
   ```text
   https://author-p<programID>-e<envionmentID>.adobeaemcloud.com/bin/franklin.delivery/<your-github-org>/<your-aem-project>/main/.helix/config.json
   ```

1. The response will be similar to the following.

   ```json
   {
     "total": 1,
     "offset": 0,
     "limit": 1,
     "data": [
       {
         "key": "admin.role.publish",
         "value": "<tech-account-id>@techacct.adobe.com"
       }
     ],
     ":type": "sheet"
   }
   ```

1. Set the technical account in your configuration with a cURL command similar to the following.
   ```text
   curl --request POST \
     --url https://admin.hlx.page/config/<your-github-org>/sites/<your-aem-project>/access.json \
     --header 'Content-Type: application/json' \
     --header 'x-auth-token: <your-token>' \
     --data '{
       "admin": {
           "role": {
               "admin": [
                   "*@adobe.com"
               ],
               "config_admin": [
                   "<tech-account-id>@techacct.adobe.com"
               ]
           },
           "requireAuth": "auto"
       }
   }'
   ```

Since you now use the configuration service, you can remove `fstab.yaml` and `paths.json` from your Git repository.

>[!NOTE]
>
>By using the configuration service and exposing the path mapping via `config.json`, the `path.json` file is ignored.

Once AEM is configured for repoless use, you must use the configuration service and provide a valid `config.json` with the paths mapping.

### Update AEM Configuration {#update-aem}

Now you are ready to make the necessary changes to your Edge Delivery Services in AEM.

1. Sign into the AEM author instance and go to **Tools** -&gt; **Cloud Services** -&gt; **Edge Delivery Services Configuration** and select the configuration that was automatically created for your site and tap or click **Properties** in the tool bar.
1. In the **Edge Delivery Services Configuration** window, change project type to **aem.live with repoless config setup** and tap or click **Save &amp; Close**.
   ![Edge Delivery Services Configuration](/help/edge/wysiwyg-authoring/assets/repoless/edge-delivery-services-configuration.png)
1. Return to your site using the Universal Editor and ensure that it still renders properly.
1. Modify some of your content and re-publish.
1. Visit your published site at `https://main--<your-aem-project>--<your-github-org>.aem.page/` and verify that the changes are properly reflected.

Your project is now set up for repoless use.

## Next Steps {#next-steps}

Now that your base site is configured for repoless usage, you can create additional sites that leverage the same code base. Refer to the following documentation depending on your use case.

* [Repoless Multi Site Management](/help/edge/wysiwyg-authoring/repoless-msm.md)
* [Repoless Stage and Prod Environments](/help/edge/wysiwyg-authoring/repoless-stage-prod.md)

## Troubleshooting {#troubleshooting}

The most common issue encountered after configuring the repoless use case is that pages in the Universal Editor no longer render or you receive a white page or a generic AEM as a Cloud Service error message. In such cases:

* View the source of the rendered page.
  * Is there actually something rendered (correct HTML head with `scripts.js`, `aem.js`, and editor-related JSON files)?
* Check the AEM `error.log` of the author instance for exceptions.
  * The most common issue is the page component fails with 404 errors.
  * `config.json or paths.json` can not be loaded
  * `component-definition.json` etc. can not be loaded
