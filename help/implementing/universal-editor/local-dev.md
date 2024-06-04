---
title: Local AEM Development with the Universal Editor
description: Learn how the Universal Editor supports editing on local AEM instances for development purposes.
exl-id: ba1bf015-7768-4129-8372-adfb86e5a120
feature: Developing
role: Admin, Architect, Developer
---

# Local AEM Development with the Universal Editor {#local-dev-ue}

Learn how the Universal Editor supports editing on local AEM instances for development purposes.

## Overview {#overview}

The Universal Editor Service is what binds the Universal Editor and the backend system. To be able to develop locally for the Universal Editor, you must run a local copy of the Universal Editor Service. This is because:

* Adobe's official Universal Editor Service is hosted globally, and your local AEM instance would need to be exposed to the internet.
* While developing with a local AEM SDK, Adobe's Universal Editor Service can not be accessed from the internet.
* If your AEM instance has IP restrictions and Adobe's Universal Editor Service isn't in a defined IP range, you can host it yourself.

This document explains how to run AEM in HTTPS alongside a local copy of the Universal Editor Service so you can develop locally on AEM for use with the Universal Editor.

## Set Up AEM to Run on HTTPS {#aem-https}

Within an outer frame secured with HTTPS an unsecure HTTP frame cannot be loaded. The Universal Editor Service runs on HTTPS and therefore AEM or any other remote page must run also on HTTPS.

To do this, you need to set up AEM to run on HTTPS. For development purposes you can use self-signed certificate.

[See this document](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/security/use-the-ssl-wizard.html) on how to set up AEM running on HTTPS including a self-signed certificate you can use.

## Install the Universal Editor Service {#install-ue-service}

The Universal Editor Service is not an entire copy of the Universal Editor, but only a subset of its features to ensure that calls from your local AEM environment are not routed over the internet, but from a defined endpoint you control.

[NodeJS version 16](https://nodejs.org/en/download/releases) is required to run a local copy of the Universal Editor Service.

The Universal Editor Service is available via Software Distribution. Please see the [Software Distribution documentation](https://experienceleague.adobe.com/docs/experience-cloud/software-distribution/home.html) for details on how to access it.

Save the `universal-editor-service.cjs` file from Software Distribution to your local development environment.

## Create a Certificate to Run the Universal Editor Service with HTTPS {#ue-https}

The Universal Editor Service also requires a certificate to run on HTTPS in your development environment.

Run the following command.

```text
$ openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
```

The command generates a `key.pem` and a `certificate.pem` file. Save these files to the same path as your `universal-editor-service.cjs` file.

## Setting up the Universal Editor Service configuration {#setting-up-service}

A number of environment variables must be set in NodeJS to run the Universal Editor Service locally.

On the same path as your `universal-editor-service.cjs`, `key.pem` and `certificate.pem` files, create an `.env` file with the following content.

```text
EXPRESS_PORT=8000
EXPRESS_PRIVATE_KEY=./key.pem
EXPRESS_CERT=./certificate.pem
NODE_TLS_REJECT_UNAUTHORIZED=0
```

The variable have the following meanings:

* `EXPRESS_PORT`: Defines on which port the Universal Editor Service listens
* `EXPRESS_PRIVATE`: Points to your [previously-created private key,](#ue-https) `key.pem`
* `EXPRESS_CERT`: Points to your [previously-created certificate,](#ue-https) `certificate.pem`
* `NODE_TLS_REJECT_UNAUTHORIZED=0`: Accepts self-signed certificates

## Running the Universal Editor Service {#running-ue}

To start the Universal Editor Service, execute the following command:

```text
$ node ./universal-editor-service.cjs
```

It should output the following to your terminal:

```text
Universal Editor Service listening on port 8000 as HTTPS Server
```

Ensure the service starts HTTPS Server not HTTP Server.

## Using the Local Universal Editor Service Instead of the Global Service {#using-local-ue}

The Universal Editor knows which Universal Editor Service to use to edit a page based on how the page is instrumented. This is done via meta tags in the page loaded in the Universal Editor.

For a page to be edited using your local Universal Editor Service, the following meta tag must be set:

```html
<meta name="urn:adobe:aue:config:service" content="https://localhost:8000">
```

Once set, you should see every content update call go to `https://localhost:8000` instead of the default Universal Editor Service.

>[!NOTE]
>
>Attempting to directly access `https://localhost:8000` results in a `404` error. This is expected behavior.
>
>To test accessing your local Universal Editor Service, use `https://localhost:8000/corslib/LATEST`. See the [next section](#editing) for details.

>[!TIP]
>
>For more details on how pages are instrumented to use the Global Universal Editor Service, see the document [Getting Started with the Universal Editor in AEM](/help/implementing/universal-editor/getting-started.md#instrument-page)

## Editing a Page with the Local Universal Editor Service {#editing}

With the [Universal Editor Service running locally](#running-ue) and your [content page instrumented to use the local service,](#using-loca-ue) you can now start the editor.

1. Open your browser to `https://localhost:8000/corslib/LATEST`.
1. Direct your browser to accept [your self-signed certificate.](#ue-https)
1. Once the self-signed certificate is trusted, you can edit the page using your local Universal Editor Service.

