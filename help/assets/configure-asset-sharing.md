---
title: Share assets, folders, and collections as a link
description: This article describes how to share assets, folders, and collections within Experience Manager Assets as a hyperlink.
contentOwner: AG
---

# Configure asset link sharing {#asset-link-sharing}

To generate the URL for assets you want to share with users, use the Link Sharing dialog. Users with administrator privileges or with read permissions at `/var/dam/share` location are able to view the links shared with them. Sharing assets through a link is a convenient way of making resources available to external parties without them having to first log in to AEM Assets.

   >[!NOTE]
   >
   >If you want to share links from your AEM Author instance to external entities, ensure that you expose only the following URLs for `GET` requests. Block other URLs to ensure that your AEM Author instance is secure.
   >* `[aem_server]:[port]/linkshare.html`
   >* `[aem_server]:[port]/linksharepreview.html`
   >* `[aem_server]:[port]/linkexpired.html`

## Configure Day CQ mail service {#configmailservice}

Before you can share assets as links, configure the email service.

1. Click or tap the AEM logo, and then navigate to **[!UICONTROL Tools]** &gt; **[!UICONTROL Operations]** &gt; **[!UICONTROL Web Console]**.
1. From the list of services, locate **[!UICONTROL Day CQ Mail Service]**.
1. Click the **[!UICONTROL Edit]** icon beside the service, and configure the following parameters for **Day CQ Mail Service]** with the details mentioned against their names:

    * SMTP server host name: email server host name
    * SMTP server port: email server port
    * SMTP user: email server user name
    * SMTP password: email server password

1. Click/tap **Save**.

## Configure maximum data size {#maxdatasize}

When you download assets from the link shared using the Link Sharing feature, AEM compresses the asset hierarchy from the repository and then returns the asset in a ZIP file. However, in the absence of limits to the amount of data that can be compressed in a ZIP file, huge amounts of data is subjected to compression, which causes out of memory errors in JVM. To secure the system from a potential denial of service attack due to this situation, configure the maximum size using the **Max Content Size (uncompressed)** parameter for Day CQ DAM Adhoc Asset Share Proxy Servlet in Configuration Manager. If uncompressed size of the asset exceeds the configured value, asset download requests are rejected. The default value is 100 MB.

1. Click/Tap the AEM logo and then go to **Tools** &gt; **Operations** &gt; **Web Console**.
1. From the web console, locate the **Day CQ DAM Adhoc Asset Share Proxy Servlet** configuration.
1. Open the **Day CQ DAM Adhoc Asset Share Proxy Servlet** configuration in edit mode, and modify the value of the **Max Content Size (uncompressed)** parameter.
1. Save the changes.

<!--
Add content or link about how to configure sharing via BP, DA, AAL, etc.
-->
