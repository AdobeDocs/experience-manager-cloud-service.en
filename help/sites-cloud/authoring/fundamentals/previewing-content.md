---
title: Previewing Content
description: Learn how to use the AEM Preview Service to preview content before going live.
exl-id: 6b4b57f6-2e66-4c83-94d9-bc1e0daab0f3
---
# Previewing Content {#previewing-content}

>[!NOTE]
>
>The Preview feature is part of the 2021.5.0 release and will be rolled out gradually over the next few weeks.

AEM offers a Sites Preview Service that is designed to let developers and content authors preview a website's final experience before it reaches the publish environment and is available publicly.

It facilitates previewing of page experiences that would not be otherwise visible from the author environment, like page transitions and other publish side only content.

## Publishing Content to Preview {#publishing-content-to-preview}

You can publish content to the Preview Service by using the Managed Publicaton UI as follows:

1. Select the page or pages you wish to send to preview in the sites console and click on the **Manage Publication** button
1. In the following wizard, select **Preview** as the destination
   
   ![managed publication](/help/sites-cloud/authoring/assets/previewmanagedpublication.png)

1. Click **Next**, and then **Publish** to confirm.

The see the preview content, append **preview** to the publish URL of your production instance. The URL should be constructed like this:

```
https://preview-p[programID]-e[environmentID].adobeaemcloud.com/pathtopage.html
```

See [Manage your Environments](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/how-to-use/manage-your-environment.html?lang=en) for more information on how to get the URLs for your environments.

Content may also be published to preview by using a [Publish Content Tree Workflow](/help/operations/replication.md#publish-content-tree-workflow) with the agentId parameter set to preview or by using the [replication API](/help/operations/replication.md#replication-api) with an AgentFilter configured for preview.

## Configuring OSGi Settings for the Preview Tier {#configuring-osgi-settings-for-the-preview-tier}

Thr preview tier's OSGI property values are inherited from the publish tier, but the preview tier values can be distinguished from the publish tier using environment-specific values setting the service parameter with the value "preview". Take the example below of an OSGI property that determines the URL of an integration endpoint:

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

Follow these steps in order to debug the preview tier using the Developer Console:

* In the [Developer Console](/help/implementing/developing/introduction/development-guidelines.md#aem-as-a-cloud-service-development-tools), select either **-- All Preview --** or a production environment that includes **prev** in its name
* Generate the relevant information for the preview instance
See [Manage your Environments](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/how-to-use/manage-your-environment.html?lang=en) for more information on how to get the URLs for your environments.
