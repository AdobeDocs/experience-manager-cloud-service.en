---
title: Configuring Site Authentication for Content Authoring
description: Learn how AEM Live supports token-based authentication and how you can configure AEM to use authentication with WYSIWYG authoring.
feature: Edge Delivery Services
role: Admin, Architect, Developer
exl-id: a6bc0f35-9e76-4b5a-8747-b64e144c08c4
---

# Configuring Site Authentication for Content Authoring {#site-authentication}

Learn how AEM Live supports token-based authentication and how you can configure AEM to use authentication with WYSIWYG authoring.

## Overview {#overview}

AEM Live supports token-based authentication. Site authentication is usually applied to both the preview and publish sites, but can also be configured to only protect either site individually.

>[!NOTE]
>
>If you choose to activate site authentication, you must configure it in your AEM authoring environments as well

## Prerequisites {#prerequisites}

To take advantage of this feature, make sure you have done the following.

* Your site is already fully set up by following the document [Developer Getting Started Guide for WYSIWYG Authoring with Edge Delivery Services](/help/edge/wysiwyg-authoring/edge-dev-getting-started.md).
* Ask Adobe to activate the [aem.live configuration service](https://www.aem.live/docs/config-service-setup#prerequisites) for your environment and that you are configured as an administrator.
  * Reach out via your Slack channel or raise a support issue.
  * If you have already had the aem.live configuration service activated for another feature such as [repoless usage,](/help/edge/wysiwyg-authoring/repoless.md) you do not need to to this.

## Configure Site Authentication {#configure-authentication}

Please see the document [Configuring Site Authentication](https://www.aem.live/docs/authentication-setup-site) for details on how to configure site authentication.

Take note of the following information as you configure authentication:

* The ID of the technical account
* Your site authentication token

These items are required to complete the configuration of site authentication for your AEM authoring environment.

## Configure Authoring Environment {#authoring-environment}

Once site authentication is configured, you can enable it in your AEM authoring environment.

1. Sign into the AEM author instance and go to **Tools** -&gt; **Cloud Services** -&gt; **Edge Delivery Services Configuration** and select the configuration that was automatically created for your site and tap or click **Properties** in the tool bar.
1. In the **Edge Delivery Services Configuration** window, select the **Authentication** tab and provide the following values, which you noted when you configured site authentication.

   * **The technical account ID**
   * **Site Authentication Token**

   ![Edge Delivery Services Configuration](/help/edge/wysiwyg-authoring/assets/site-authentication/configure-aem-author.png)

1. Tap or click **Save &amp; Close**.
