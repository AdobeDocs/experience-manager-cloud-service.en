---
title: Previewing Content
description: Learn how to use the AEM preview service to preview content before going live.
exl-id: 6b4b57f6-2e66-4c83-94d9-bc1e0daab0f3
---

# Previewing Content {#previewing-content}

AEM offers a Sites preview service lets developers and content authors preview a website's final experience before it reaches the publish environment and is available publicly.

It facilitates previewing page experiences that would not be otherwise visible from the author environment, like page transitions and other publish side only content. 

>[!NOTE]
>
>As the content is *published* to the preview environment it is accessible by URL (so does not need access to AEM).

For more details about the preview environments, see [Manage Environments](/help/implementing/cloud-manager/manage-environments.md#access-preview-service).

## Publishing Content to Preview {#publishing-content-to-preview}

You can publish content to the preview service by using the **Managed Publication** UI.

1. In the Sites console, select the page or pages you want to send to preview and click the **Manage Publication** button.
1. In the following wizard, select **Preview** as the destination.

   ![managed publication](/help/sites-cloud/authoring/assets/previewmanagedpublication.png)

1. Click **Next**, and then **Publish** to confirm.

1. A dialog will display the URLs for accessing the content in the preview environment.

   >[!NOTE]
   >
   >As the content is *published* to the preview environment it is accessible by URL (so does not need access to AEM).

Alternatively to using the URLs displayed in the wizard to see the preview content, you can also prepend `preview-` to the publish URL of your production instance. 

```
https://preview-p<programID>-e>environmentID>.adobeaemcloud.com/<pathtopage>.html
```

See the document [Managing Environments](/help/implementing/cloud-manager/manage-environments.md) for more information on how retrieve the URLs for your environments.

Content may also be published to preview by using a [publish content tree workflow](/help/operations/replication.md#publish-content-tree-workflow) with the `agentId` parameter set to `preview` or by using the [replication API](/help/operations/replication.md#replication-api) with an `AgentFilter` configured for preview.

## Unpublishing Content from Preview {#unpublishing-content-from-preview}

Unpublishing content from your **Preview** environment is basically the same process as [unpublishing pages](/help/sites-cloud/authoring/fundamentals/publishing-pages.md#unpublishing-pages) from the **Publish** environment. 

The only difference is that you can select the **Destination** to be **Preview**.

## Further Information {#further-information}

See also:

* [Configuring OSGi Settings for the Preview Tier](/help/implementing/preview-tier/preview-tier-configuring-osgi.md#configuring-osgi-settings-for-the-preview-tier)

* [Debugging Preview Using the Developer Console](/help/implementing/preview-tier/preview-tier-configuring-osgi.md#debugging-preview-using-the-developer-console)