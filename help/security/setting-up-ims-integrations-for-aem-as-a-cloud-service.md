---
title: Setting Up IMS Integrations for AEM as a Cloud Service
description: Learn how to set up IMS integrations for AEM as a Cloud Service
exl-id: 72fb1ea1-355c-4faa-a733-77bc7de75ed5
feature: Security
role: Admin
---
# Setting Up IMS Integrations for AEM as a Cloud Service {#setting-up-ims-integrations-for-aemaacs}

Adobe Experience Manager (AEM) as a Cloud Service can be integrated with many other Adobe solutions. For example, Adobe Target, Adobe Analytics, and others. 

The integrations use an IMS integration, configured with S2S OAuth.

* Once you have created:

  * [Credentials in the Developer Console](#credentials-in-the-developer-console) 

* Then you can:

  * Create a (new) [OAuth configuration](#creating-oauth-configuration)

## Credentials in the Developer Console {#credentials-in-the-developer-console}

As the first step you need to configure the OAuth credentials in the Adobe Developer Console. 

For details on how to do this, see the Developer Console documentation, depending on your requirements:

* Overview:

  * [Server to Server authentication](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/)

* Creating a new OAuth credential:

  * [OAuth Server-to-Server credential implementation guide](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/implementation)

* Migrating an existing JWT credential to an OAuth credential:

  * [Migrating from Service Account (JWT) credential to OAuth Server-to-Server credential](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/migration/)

For example:

![OAuth Credential in the Developer Console](assets/ims-configuration-developer-console.png)

## Creating an OAuth configuration {#creating-oauth-configuration}

To create a new Adobe IMS Integration using OAuth:

1. In AEM, navigate to **Tools**, **Security**, **Adobe IMS Integration**.

1. Select **Create**.

1. Complete the configuration based on details from the [Developer Console](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/implementation). For example:

   ![Create OAuth Configuration](assets/ims-create-oauth-configuration.png)

1. **Save** your changes.
