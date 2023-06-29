---
title: Configuring OSGi Settings for the Preview Tier
description: Learn how to configure the AEM preview service to preview content before going live.
exl-id: 1200bb17-8a3c-4e41-85f4-ed2334b61f69
---
# Configuring OSGi Settings for the Preview Tier {#configure-osgi-preview-tier}

AEM offers a Sites preview service that lets developers and content authors preview a website's final experience before it reaches the publish environment and is available publicly.

It facilitates previewing a range of experiences that would not be otherwise visible from the author environment. For example, page transitions, experience fragments, and other publish side only content.

The preview tier's OSGi property values are inherited from the publish tier. However the preview tier's values can be distinct from the publish tier by setting the `service` parameter to the value `preview`. 

>[!NOTE]
>
>For more details about the preview environments, see [Manage Environments](/help/implementing/cloud-manager/manage-environments.md#access-preview-service).

## Configuring the OSGi Settings for the Preview Tier {#configuring-osgi-settings-for-the-preview-tier}

The following example of an OSGi property determines the URL of an integration endpoint.

```
[
{
"name":"INTEGRATION_URL",
"type":"string",
"value":"http://s2.integrationvendor.com",
"service": "preview"
}
]
```

For more information, see [this section](/help/implementing/deploying/configuring-osgi.md#author-vs-publish-configuration) of the OSGi configuration documentation.

## Debugging Preview Using the Developer Console {#debugging-preview-using-the-developer-console}

Follow these steps so you can debug the preview tier using the Developer Console:

* In the [Developer Console](/help/implementing/developing/introduction/development-guidelines.md#aem-as-a-cloud-service-development-tools), select either **-- All Preview --** or a production environment that includes **prev** in its name
* Generate the relevant information for the preview instance
See [Managing Environments](/help/implementing/cloud-manager/manage-environments.md) for more information on how to get the URLs for your environments.
