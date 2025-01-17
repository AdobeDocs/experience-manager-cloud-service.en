---
title: Repoless Multi Site Management
description: Learn best practice recommendations on how to set up a project in a repoless manner with localized sites that leverage a single code base, each served up by Edge Delivery Services.
feature: Edge Delivery Services
role: Admin, Architect, Developer
exl-id: f6b861ed-18e4-4c81-92d2-49fadfe4669a
---
# Repoless Multi Site Management {#repoless-msm}

Learn best practice recommendations on how to set up a project in a repoless manner with localized sites that leverage a single code base, each served up by Edge Delivery Services. 

## Overview {#overview}

[Multi Site Manager (MSM)](/help/sites-cloud/administering/msm/overview.md) and its Live Copy features enable you to use the same site content in multiple locations, while allowing for variations. You can author content once and create Live Copies. MSM maintains live relationships between your source content and its Live Copies so that when you change the source content, the source and Live Copies can be synchronized.

You can use MSM to create an entire content structure for your brand across locales and languages, authoring the content centrally. Your localized sites can then each be delivered by Edge Delivery Services, leveraging a central code base.

## Requirements {#requirements}

To configure MSM in a repoless use case, you must first complete a number of tasks.

* This document assumes that you have already created a site for your project based on the [Developer Getting Started Guide for WYSIWYG Authoring with Edge Delivery Services](/help/edge/wysiwyg-authoring/edge-dev-getting-started.md) guide.
* You must have already [enabled the repoless feature for your project.](/help/edge/wysiwyg-authoring/repoless.md)

## Use Case {#use-case}

This document assumes that you have already created a basic localized site structure for your project. It uses the following structure for the wknd brand with a presence in Switzerland and Germany as an example.

```text
/content/wknd
/content/wknd/language-masters
/content/wknd/language-masters/en
/content/wknd/language-masters/de
/content/wknd/language-masters/fr
/content/wknd/language-masters/it
/content/wknd/ch
/content/wknd/ch/de
/content/wknd/ch/fr
/content/wknd/ch/it
/content/wknd/ch/en
/content/wknd/de
/content/wknd/de/de
/content/wknd/de/en
```

Content in `language-masters` is the source of Live Copies for the localized sites: Germany (`de`) and Switzerland (`ch`). The goal of this document is to create Edge Delivery Services sites that all use the same code base for each localized site.

## Configuration {#configuration}

There are several steps to configuring the MSM repoless use case.

1. [Update AEM site configurations.](#update-aem-configurations)
1. [Create new Edge Delivery Services sites for your localized pages.](#create-edge-sites)
1. [Update cloud configuration in AEM for your localized sites.](#update-cloud-configurations)

### Update AEM Site Configurations {#update-aem-configurations}

[Configurations](/help/implementing/developing/introduction/configurations.md) can be thought of as workspaces that can be used to gather groups of settings and their associated content for organizational purposes. When you create a site in AEM, a configuration is automatically created for it.

You generally want to share certain content between sites such as:

* Templates created from content in the blueprint
* Content Fragment models, persisted, queries etc.

You can create additional configurations to facilitate such sharing. For the wknd use case, we would need configurations for the following paths.

```text
/content/wknd
/content/wknd/ch
/content/wknd/de
```

That is, you will have a configuration for the root of the wknd brand's content (`/content/wknd`) used by the blueprints and a configuration used by each localized site (Switzerland and Germany).

1. Sign into your AEM authoring instance.
1. Navigate to the **Configuration Browser** by going to **Tools** -&gt; **General** -&gt; **Configuration Browser**.
1. Select the configuration that was automatically created for your project (in this case wknd) and then tap or click **Create** in the toolbar.
1. In the **Create Configuration** dialog, provide a descriptive **Name** for your localized site (such as `Switzerland`) and for the **Title** use the same title of the localized size (in this case `ch`).
1. Select the **Cloud Configuration** feature and any additional features you may need for your project such as **Editable Templates**.
1. Tap or click **Create**.

Create configurations for each localized site you need. In the case of wknd, you would need you create a configuration for `de` as well alongside the `ch` configuration.

Once the configurations are created, you need to ensure that the localized sites use them.

1. Sign into your AEM authoring instance.
1. Navigate to the **Sites Console** by going to **Navigation** -&gt; **Sites**.
1. Select the localized site such as `Switzerland`.
1. Tap or click **Properties** in the tool bar.
1. In the page properties window, select the **Advanced** tab and under the **Configuration** heading, unselect the option **Inherited from /content/wknd**, where `wknd` is the site root.
1. In **Cloud Configuration** field, use the path browser to select the configuration you created for your localized site such as `Switzerland` under `/conf/wknd/ch`.
1. Tap or click **Save &amp; Close**.

Assign the respective configurations to the additional localized sites. In the case of wknd, you would need to assign the `/conf/wknd/de` configuration to the Germany site as well.

### Create New Edge Delivery Services Sites for Your Localized Pages {#create-edge-sites}

To connect more sites to Edge Delivery Services for a multi-region, multi-language site setup, you must set up a new aem.live site for each of your AEM MSM sites. There is a 1:1 relationship between AEM MSM sites and aem.live sites with a shared Git repository and code base.

For this example, we will create the site `wknd-ch` for the Swiss presence of wknd, whose localized content is under the AEM path `/content/wknd/ch`. 

1. Retrieve your auth token and the technical account for your program.
   * Please see the document **Reusing Code Across Sites** for details on how to [obtain your access token](/help/edge/wysiwyg-authoring/repoless.md#access-token) and the [technical account](/help/edge/wysiwyg-authoring/repoless.md#access-control) for your program.
1. Create a new site by making the following call to the configuration service. Please consider:
   * The project name in the POST URL must be the new site name you are creating. In this example, it is `wknd-ch`.
   * The `code` configuration should be the same as you used for the initial project creation.
   * The `content` > `source` > `url` must be adapted to the name of the new site you are creating. In this example, it is `wknd-ch`.
   * I.e., the site name in POST URL and the `content` > `source` > `url` must be the same.
   * Adapt the `admin` block to define the users who should have full administrative access to the site.
     * It is an array of email addresses.
     * The wildcard `*` can be used.
     * See the document [Configuring Authentication for Authors](https://www.aem.live/docs/authentication-setup-authoring#default-roles) for more information.

   ```text
   curl --request POST \
     --url https://admin.hlx.page/config/<your-github-org>/sites/wknd-ch.json \
     --header 'Content-Type: application/json' \
     --header 'x-auth-token: <your-token>' \
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
               "url": "https://author-p<programID>-e<environmentID>.adobeaemcloud.com/bin/franklin.delivery/<your-github-org>/wknd-ch/main",
               "type": "markup",
               "suffix": ".html"
           }
       },
       "access": {
           "admin": {
               "role": {
                   "admin": [
                       "<email>@<domain>.<tld>"
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
     --url https://admin.hlx.page/config/<your-github-org>/sites/wknd-ch/public.json \
     --header 'Content-Type: application/json' \
     --header 'x-auth-token: <your-token>' \
     --data '{
       "paths": {
           "mappings": [
               "/content/wknd/ch/:/"
           ],
           "includes": [
               "/content/wknd/ch/"
           ]
       }
   }'
   ```

1. Verify that the public configuration of your new site is working by calling `https://main--wknd-ch--<your-github-org>.aem.page/config.json` and verifying the content of the returned JSON.

Repeat the steps to create additional localized sites. In the case of wknd, you would need to create a `wknd-de` site for the German presence as well.

### Update Cloud Configurations in AEM for Your Localized Pages {#update-cloud-configurations}

Your pages in AEM must be configured to use the new Edge Delivery Sites you created in the previous section for your localized presence. In this example, content under `/content/wknd/ch` needs to know to use the `wknd-ch` site you created. Similarly content under `/content/wknd/de` needs to use the `wknd-de` site.

1. Sign into the AEM author instance and go to **Tools** -&gt; **Cloud Services** -&gt; **Edge Delivery Services Configuration**.
1. Select the configuration that was automatically created for your project and then the folder that was created for the localized page. In this case, that would be Switzerland (`ch`).
1. Tap or click **Create** > **Configuration** in the tool bar.
1. In the **Edge Delivery Services Configuration** window:
   * Provide your GitHub organization in the **Organization** field.
   * Change the site name to the name of the site you created in the previous section. In this case, that would be `wknd-ch`.
   * Change project type to **aem.live with repoless config setup**.
1. Tap or click **Save &amp; Close**.

## Verify Your Setup {#verify}

Now that you have made all of the necessary configuration changes, verify that everything is working as expected.

1. Sign into your AEM authoring instance.
1. Navigate to the **Sites Console** by going to **Navigation** -&gt; **Sites**.
1. Select the localized site such as `Switzerland`.
1. Tap or click **Edit** in the toolbar.
1. Ensure that the page properly renders in the Universal Editor and uses the same code as your site root.
1. Make a change to the page and re-publish.
1. Visit your new Edge Delivery Services site for that localized page at `https://main--wknd-ch--<your-github-org>.aem.page`.

If you see the changes that you made, your MSM setup is working properly.
