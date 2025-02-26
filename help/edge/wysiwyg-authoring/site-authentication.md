---
title: Configuring Site Authentication for Content Authoring
description: Learn how AEM Live supports token-based authentication and how you can configure AEM to use authentication with WYSIWYG authoring.
feature: Edge Delivery Services
role: Admin, Architect, Developer
---

# Configuring Site Authentication for Content Authoring {#site-authentication}

Learn how AEM Live supports token-based authentication and how you can configure AEM to use authentication with WYSIWYG authoring.

## Overview {#overview}

AEM Live supports token-based authentication. Site authentication is usually applied to both the preview and publish sites, but can also be configured to only protect either site individually.

>[!NOTE]
>
>If you choose to activate site authentication, you must configure it in your AEM authoring environments as well

## Requirements {#requirements}

To configure site authentication for use with content authoring, you must first complete the following tasks:

* This document assumes that you have already created a site for your project based on the [Developer Getting Started Guide for WYSIWYG Authoring with Edge Delivery Services guide.](/help/edge/wysiwyg-authoring/edge-dev-getting-started.md)
* You must have already [enabled the repoless feature for your project.](/help/edge/wysiwyg-authoring/repoless.md)

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
