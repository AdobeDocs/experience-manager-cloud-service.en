---
title: Previewing Content
description: Learn how to use the AEM Preview Service to preview content before going live.
---

# Previewing Content {#previewing-content}

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
https://preview-p1234-e5678.adobeaemcloud.com/pathtopage.html
```

See [Manage your Environments](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/how-to-use/manage-your-environment.html?lang=en) for more information on how to get the URLs for your environments. 