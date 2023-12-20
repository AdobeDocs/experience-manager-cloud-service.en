---
title: Universal Editor Developer Overview
description: If you are developer interested in how the Universal Editor works and how to use it in your project, this document give you an end-to-end introduction.
---

# Universal Editor Developer Overview {#developer-overview}

If you are developer interested in how the Universal Editor works and how to use it in your project, this document give you an end-to-end introduction.

## Purpose {#purpose}

This document serves as a developer's introduction to both how the Universal Editor functions and how to instrument your application to work with it.

It does this by taking a standard example that most AEM developer's a familiar with, the Core Components and the WKND site, and instruments a few example components to be editable using the Universal editor.

>[!TIP]
>
>This document takes extra steps to illustrate how the Universal Editor works and is intended to deepen the developer's understanding of the editor.
>
>If you want to get up-and-running as quickly as possible, please see the [Getting Started with the Universal Editor in AEM](/help/implementing/universal-editor/getting-started.md) document.

## Prerequisites {#prerequisites}

You will need the following available to you.

* [Local development instance of AEM as a Cloud Service](https://experienceleague.adobe.com/docs/experience-cloud/software-distribution/home.html)
* [WKND demo site installed](https://github.com/adobe/aem-guides-wknd)
* [Access to the Universal Editor](/help/implementing/universal-editor/getting-started.md#onboarding)
* Your local development instance must be [configured with HTTPS for development purpose on `localhost`.](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/security/use-the-ssl-wizard.html)

Beyond general familiarity with web development, this document assumes basic familiarity with AEM development. If you are not experienced with AEM development, consider reviewing the WKND tutorial before continuing.

## Start AEM and Sign In to the Universal Editor {#sign-in}

If you haven't already, you must have your local AEM development instance running with WKND installed and HTTPS enabled as [detailed in the prerequisites.](#prerequisites)

This document assumes your instance is running at `https://localhost:8443`.

1. Open the main English language master page in the AEM editor.

   ```text
   https://localhost:8443/editor.html/content/wknd/language-masters/en.html
   ```

1. In the **Page Information** menu of the editor, select **View as Published**. This opens the same page in a new tab with the AEM editor disabled.

   ```text
   https://localhost:8443/content/wknd/language-masters/en.html?wcmmode=disabled
   ```

1. Copy this link.

1. Now sign in to the Universal Editor.

   ```text
   https://experience.adobe.com/#/aem/editor
   ```

1. Paste the link you copied previously of the WKND content into the **Site URL** field of the Universal Editor and click **Open**.

   ![Open the WKND page in the Universal Editor](assets/dev-ue-open.png)

## Universal Editor Attempts to Load the Content {#sameorigin}

The Universal Editor loads content to be edited in a frame. AEM's default settings for X-Frame options prevent this, which can clearly be seen in the browser as an error and detailed in the console output.

![Browser error due to SAMEORIGIN option](assets/dev-sameorigin.png)

The X-Frame option `sameorigin` prevents rendering AEM pages within a frame. You must remove tis header to allow the pages to be loaded in the Universal Editor.

1. Open the Configuration Manager.

   ```text
   http://localhost:4502/system/console/configMgr
   ```

1. Edit the OSGi configuration `org.apache.sling.engine.impl.SlingMainServlet`

   ![OSGi property for SAMEORIGIN](assets/dev-sameorigin-osgi.png)

1. Delete the property `X-Frame-Options=SAMEORIGIN` of the property **Additional response headers**.

1. Save the changes.

Now if you reload the Universal Editor, you will see that your AEM page loads.

>[!TIP]
>
>* See the document [Getting Started with the Universal Editor in AEM](/help/implementing/universal-editor/getting-started.md#sameorigin) for more details on this OSGi configuration.
>* See the document [Configuring OSGi for Adobe Experience Manager as a Cloud Service](/help/implementing/deploying/configuring-osgi.md) for details on OSGi in AEM.

### com.day.crx.security.token.impl.impl.TokenAuthenticationHandler {#samesite-cookies}

When the Universal Editor loads your page, it loads to the AEM sign-in page to ensure that you are authenticated to make changes.

However, you will not be able to successfully sign in. Showing the browser console, you can see that the browser has blocked input on the frame

![Input blocked](assets/dev-cross-origin.png)

The login token cookie is sent to AEM as a third-party domain. Therefore the same-site cookie must be set explicitly to `None`.

1. Open the Configuration Manager.

   ```text
   http://localhost:4502/system/console/configMgr
   ```

1. Edit the OSGi configuration `com.day.crx.security.token.impl.impl.TokenAuthenticationHandler`

   ![OSGi property for same-site cookies](assets/dev-cross-origin-osgi.png)

1. Change the property **SameSite attribute for the login-token cookie** to `None`.

1. Save the changes.

Now if you reload the Universal Editor, you can successfully sign in to AEM and your target page loads.

>[!TIP]
>
>* See the document [Getting Started with the Universal Editor in AEM](/help/implementing/universal-editor/getting-started.md#samesite-cookies) for more details on this OSGi configuration.
>* See the document [Configuring OSGi for Adobe Experience Manager as a Cloud Service](/help/implementing/deploying/configuring-osgi.md) for details on OSGi in AEM.

## Universal Editor Connects to the Remote Frame {#ue-connect-remote-frame}

With the page loaded in the Universal Editor and you signed into AEM, the Universal Editor will try to connect to the remote frame. This is done via a JavaScript library that must be loaded in the remote frame. If the JavaScript library is not present, the page will create a timeout error in the console.

![Timeout error](assets/dev-timeout.png)

You must add the necessary JavaScript library to the page component of the WKND app.

1. Open CRXDE Lite.

   ```text
   http://localhost:4502/crx/de
   ```

1. Under `/apps/wknd/components/page` edit the file `customheaderlibs.html`.

   ![Editing the customheaderlibs.html file](assets/dev-customheaderlibs.png)

1. Add the JavaScript library to the end of the file.

   ```html
   <script src="https://cdn.jsdelivr.net/gh/adobe/universal-editor-cors/dist/universal-editor-embedded.js"></script>
   ```

1. Click **Save All** and then reload the Universal Editor.

The page now loads with the proper JavaScript library to allow the Universal Editor to connect to your page and the timeout error no longer appears in the console.




lax cookie
uBlock origin
experience.adobe.com/#/@sitesinternal/aem/editor/

