---
title: Previewing Content
description: Learn how to use the AEM Preview Service to preview content before going live.
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

1. A dialog will display the URLs for accessing the content on the Preview environment.

   Or to see the preview content, you can also append **preview** to the publish URL of your production instance. 

   The URL should be constructed like this:

   ```
   https://preview-p[programID]-e[environmentID].adobeaemcloud.com/pathtopage.html
   ```

See [Manage your Environments](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/how-to-use/manage-your-environment.html?lang=en) for more information on how to get the URLs for your environments. 

