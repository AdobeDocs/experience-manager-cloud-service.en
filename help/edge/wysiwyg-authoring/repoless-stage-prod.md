---
title: Repoless Stage and Prod Environments
description: Learn how to set up a separate sites for your staging and production environments leveraging a single code base in a repoless manner.
feature: Edge Delivery Services
role: Admin, Architect, Developer
exl-id: 701bd9bc-30e8-4654-8248-a06d441d1504
---
# Repoless Stage and Prod Environments {#repoless-stage-prod}

Learn how to set up a separate sites for your staging and production environments leveraging a single code base in a repoless manner.

## Overview {#overview}

You may wish to set up a site for your production environment separate from your staging environment. Setting up a second site for a separate staging and production setup is similar to the [setup required for multi site management.](/help/edge/wysiwyg-authoring/repoless-msm.md) In fact, it can be combined with MSM site structures if required.

This document uses the typical example of separate staging and production environments. You can create separate environments for any environments you wish.

## Configuration {#configuration}

This document describes how to set up a separate production site for your project using the same code base. The following assumptions are made.

* The staging site is already set up and you now want to create a configuration for the production site.
* The content structure in AEM authoring are similar.
* The same path mappings will be used for staging and production.

In this example, we are assuming that a production site has already been created for the project called wknd whose GitHub repo is also called wknd.

There are two steps to configuring a separate production site.

1. [Create new Edge Delivery Services sites for your production environment.](#create-edge-site)
1. [Update cloud configuration in AEM for your production site.](#update-cloud-configuration)

### Create New Edge Delivery Services Sites for Your Production Environment {#create-edge-site}

1. Retrieve your auth token and the technical account for your program.
   * Please see the document **Reusing Code Across Sites** for details on how to [obtain your access token](/help/edge/wysiwyg-authoring/repoless.md#access-token) and the [technical account](/help/edge/wysiwyg-authoring/repoless.md#access-control) for your program.
1. Create a new site by making the following call to the configuration service. Please consider:
   * The project name in the POST URL must be the new site name you are creating. In this example, it is `wknd-prod`.
   * The `code` configuration should be the same as you used for the initial project creation.
   * The `content` > `source` > `url` must be adapted to the name of the new site you are creating. In this example, it is `wknd-prod`.
   * I.e., the site name in POST URL and the `content` > `source` > `url` must be the same.

   ```text
   curl --request POST \
     --url https://admin.hlx.page/config/<your-github-org>/sites/wknd-prod.json \
     --header 'x-auth-token: <your-token>' \
     --header 'Content-Type: application/json' \
     --data '{
       "code": {
           "owner": "<your-github-org>",
           "repo": "wknd",
           "source": {
               "type": "github",
               "url": "https://github.com/<your-github-org>/wknd"
           }
       },
       "content": {
           "source": {
               "url": "https://author-p<programID>-e<environmentID>.adobeaemcloud.com/bin/franklin.delivery/<your-github-org>/wknd-prod/main",
               "type": "markup",
               "suffix": ".html"
           }
       },
       "access": {
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
       }
   }'
   ```

1. Add the path mapping for your new site by making the following call to the configuration service.

   ```text
   curl --request POST \
     --url https://admin.hlx.page/config/<your-github-org>/sites/wknd-prod/public.json \
     --header 'x-auth-token: <your-token>' \
     --header 'Content-Type: application/json' \
     --data '{
       "paths": {
           "mappings": [
               "/content/wknd/:/"
           ],
           "includes": [
               "/content/wknd/"
           ]
       }
   }'
   ```

Verify that the public configuration of your new site is working by calling `https://main--wknd-prod--<your-github-org>.aem.page/config.json` and verifying the content of the returned JSON.

### Update Cloud Configurations in AEM for Your Production Site {#update-cloud-configuration}

Your production AEM must be configured to use the new Edge Delivery Sites you created in the previous section for a dedicated production site. In this example, content under `/content/wknd` on your production environment needs to know to use the `wknd-prod` site you created.

1. Sign into the AEM production instance and go to **Tools** -&gt; **Cloud Services** -&gt; **Edge Delivery Services Configuration**.
1. Select the configuration that was automatically created for your project.
1. Tap or click **Properties** in the tool bar.
1. In the **Edge Delivery Services Configuration** window:
   * Provide your GitHub organization in the **Organization** field.
   * Change the site name to the name of the site you created in the previous section. In this case, that would be `wknd-prod`.
   * Change project type to **aem.live with repoless config setup**.
1. Tap or click **Save &amp; Close**.

## Verify Your Setup {#verify}

Now that you have made all of the necessary configuration changes, verify that everything is working as expected.

1. Sign into your AEM production authoring instance.
1. Navigate to the **Sites Console** by going to **Navigation** -&gt; **Sites**.
1. Select a page in your site.
1. Tap or click **Edit** in the toolbar.
1. Ensure that the page properly renders in the Universal Editor and uses the same code as your site root.
1. Make a change to the page and re-publish.
1. Visit your new Edge Delivery Services site for that page at `https://main--wknd-prod--<your-github-org>.aem.page`.

If you see the changes that you made, your separate production site setup is working properly.
