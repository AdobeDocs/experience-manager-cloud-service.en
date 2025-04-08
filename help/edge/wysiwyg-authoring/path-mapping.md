---
title: Path Mapping for Edge Delivery Services
description: Learn how to map page paths used on the AEM authoring instance to public page paths used on the website and control which content is published to Edge Delivery Services.
feature: Edge Delivery Services
role: User
exl-id: 3d68135d-e84c-4bf4-93d1-38a0be70ce4a
---
# Path Mapping for Edge Delivery Services {#path-mapping}

Learn how to map page paths used on the AEM authoring instance to public page paths used on the website and control which content is published to Edge Delivery Services.

## Overview {#overview}

To be able to author WYSIWYG content using AEM and publish it to Edge Delivery Services, you must set up your project's path mapping. This mapping has two purposes.

* It maps and creates a relationship between page paths used on your AEM authoring instance and the public page paths used on your website.
* It controls which content (pages, sheets, assets, etc.) are published to Edge Delivery Services.

The path mapping must be configured for each project individually and according to the project's content and URL structure. It is used by AEM during content publishing and while editing content in the [Universal Editor](/help/sites-cloud/authoring/universal-editor/navigation.md).

## Configuration Format {#configuration-format}

The format of the path mapping configuration contains two sections (`mappings` and `includes`) similar to the following example.

```json
{
  "mappings": [
    "/content/aem-boilerplate/:/",
    "/content/aem-boilerplate/configuration:/.helix/config.json"
  ],
  "includes:" [
    "/content/aem-boilerplate/"
  ]
}
```

### mappings {#mappings}

The `mappings` configuration holds an array of internal paths (on the AEM authoring instance) and external URL paths (on the public website).

The format is `<internal paths>:<external path>`. It typically consists of a minimum of two entries.

1. The first entry from the example is the path mapping of the website pages. 
1. The second entry controls the mapping of the `.helix/config.json` to the corresponding spreadsheet page in the AEM authoring repository. 

In this example, all pages stored under `/content/aem-boilerplate/...` will be publicly accessible on the Edge Delivery Services site directly under `https://main--my-site--org.aem.live/....`.

>[!TIP]
>
>All tabular data managed as spreadsheets (e.g. metadata, redirects, and taxonomy) are typically published as `.json` API URLs on Edge Delivery Services. To do so, they must be individually listed in the mapping configuration.
>
>Please see the document [Using Spreadsheets to Manage Tabular Data](/help/edge/wysiwyg-authoring/tabular-data.md) for more information.

### includes {#includes}

The `includes` configuration controls which content paths are actually replicated to Edge Delivery Services. It can hold any array of paths as well and typically contains the sites top level root page.

Assets used on Edge Delivery Services pages are typically published alongside the webpage. They will be exported from the AEM authoring instance to Edge Delivery Services automatically.

>[!TIP]
>
>If you have a use case where you want assets published directly to Edge Delivery Services (for example you would like images or PDFs to be directly accessible by their URLs outside of a page context), you must add the DAM paths to the `includes` section of the configuration as well.
>
>For example, if an asset root folder such as `/content/dam/my-site/documents` containing a set of PDF should be publicly accessible via `/assets/...`, an entry must be added to the `includes` section of the configuration.

## How to Configure {#how-to-configure}

Your path mappings can be configured in one of two ways depending on the setup of your project.

1. If the project is configured for `aem.live` and uses the [configuration service](https://www.aem.live/docs/config-service-setup) for centralized configurations, the paths mapping for each site is configured via this configuration service.

   * Here is an example cURL request to configure path mappings.

   ```text
   curl --request POST \
     --url https://admin.aem.page/config/{org}/sites/{site}/public.json \
     --header 'Content-Type: application/json' \
     --header 'x-auth-token: ......' \
     --data '{
       "paths": {
       "mappings": [
         "/content/aem-boilerplate/:/",
         "/content/aem-boilerplate/configuration:/.helix/config.json"
       ],
       "includes": [
         "/content/aem-boilerplate/"
       ]
   }
   }'
   ```

1. If the project does not use the configuration service, the paths mapping is configured via a `paths.json` file in you projects GitHub repository.

   * See [`https://github.com/adobe-rnd/aem-boilerplate-xwalk/blob/main/paths.json`](https://github.com/adobe-rnd/aem-boilerplate-xwalk/blob/main/paths.json) for an example.

In both cases, once you configure your path mappings, you can check the configuration via the publicly-accessible configuration URL `https://<branch>--<site>--<org>.aem.page/config.json`.
