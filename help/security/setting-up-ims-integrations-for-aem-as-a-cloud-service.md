---
title: Setting Up IMS Integrations for AEM as a Cloud Service
description: Learn how to set up IMS integrations for AEM as a Cloud Service
exl-id: 72fb1ea1-355c-4faa-a733-77bc7de75ed5
feature: Security
role: Admin
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: b1210526-416b-4ef6-bcc0-1692e99f30e9
    internal-label: Administration and security
subfeature_v2:
  - id: c35bc059-fd80-4a01-91a6-e48da3c76758
    internal-label: Security practices
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
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
