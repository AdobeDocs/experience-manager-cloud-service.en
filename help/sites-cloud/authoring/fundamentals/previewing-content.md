---
title: Previewing Content
description: Learn how to use the AEM preview service to preview content before going live.
exl-id: 6b4b57f6-2e66-4c83-94d9-bc1e0daab0f3
---

# Previewing Content {#previewing-content}

AEM offers a Sites preview service lets developers and content authors preview a website's final experience before it reaches the publish environment and is available publicly.

It facilitates previewing page experiences that would not be otherwise visible from the author environment, like page transitions and other publish side only content.

For more details about the preview environments, please see the document [Manage Environments.](/help/implementing/cloud-manager/manage-environments.md#access-preview-service).

>[!NOTE]
>
>Publishing an Experience Fragment to Preview basically follows the same procedure as for a page, though from the Experience Fragments console or editor.

## Publishing Content to Preview {#publishing-content-to-preview}

You can publish content to the preview service by using the **Managed Publication** UI.

1. In the Sites console, select the page or pages you wish to send to preview and click on the **Manage Publication** button
1. In the following wizard, select **Preview** as the destination
   
   ![managed publication](/help/sites-cloud/authoring/assets/previewmanagedpublication.png)

1. Click **Next**, and then **Publish** to confirm.

1. A dialog will display the URLs for accessing the content in the preview environment.


Alternatively to using the URLs displayed in the wizard to see the preview content, you can also prepend `preview-` to the publish URL of your production instance. 

```
https://preview-p<programID>-e>environmentID>.adobeaemcloud.com/<pathtopage>.html
```

See the document [Managing Environments](/help/implementing/cloud-manager/manage-environments.md) for more information on how retrieve the URLs for your environments.

Content may also be published to preview by using a [publish content tree workflow](/help/operations/replication.md#publish-content-tree-workflow) with the `agentId` parameter set to `preview` or by using the [replication API](/help/operations/replication.md#replication-api) with an `AgentFilter` configured for preview.

## Unpublishing Content from Preview {#unpublishing-content-from-preview}

Unpublishing content from your **Preview** environment is basically the same process as [unpublishing pages](/help/sites-cloud/authoring/fundamentals/publishing-pages.md#unpublishing-pages) from the **Publish** environment. 

The only difference is that you can select the **Destination** to be **Preview**.

## Configuring OSGi Settings for the Preview Tier {#configuring-osgi-settings-for-the-preview-tier}

The preview tier's OSGi property values are inherited from the publish tier. However the preview tier's values can be distinct from the publish tier by setting the `service` parameter to the value `preview`. The following example of an OSGi property determines the URL of an integration endpoint.

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
See [Managing Environments](/help/implementing/cloud-manager/manage-environments.md) for more information on how to get the URLs for your environments.
