---
title: Running Your Own Universal Editor Service
description: Learn how you can run your own Universal Editor Service either for local development or as part of your own infrastructure.
exl-id: ba1bf015-7768-4129-8372-adfb86e5a120
feature: Developing
role: Admin, Architect, Developer
---

# Running Your Own Universal Editor Service {#local-ue-service}

Learn how you can run your own Universal Editor Service either for local development or as part of your own infrastructure.

## Overview {#overview}

The Universal Editor Service is what binds the Universal Editor and the backend system. To be able to develop locally for the Universal Editor, you must run a local copy of the Universal Editor Service. This is because:

* Adobe's official Universal Editor Service is hosted globally, and your local AEM instance would need to be exposed to the internet.
* While developing with a local AEM SDK, Adobe's Universal Editor Service can not be accessed from the internet.
* If your AEM instance has IP restrictions and Adobe's Universal Editor Service isn't in a defined IP range, you can host it yourself.

## Use Cases {#use-cases}

Your own copy of the Universal Editor Service is useful if you wish to:

* Develop locally on AEM for use with the Universal Editor.
* Run your own Universal Editor Service as part of your own infrastructure, independent of Adobe's Universal Editor Service.

Both use cases are supported. This document explains how to run AEM in HTTPS alongside a local copy of the Universal Editor Service.

If you wish to run your own Universal Editor Service as part of your own infrastructure, you would follow the same steps as the local development example.

## Set Up AEM to Run on HTTPS {#aem-https}

Within an outer frame secured with HTTPS, an unsecure HTTP frame cannot be loaded. The Universal Editor Service runs on HTTPS and therefore AEM or any other remote page must run also on HTTPS.

To do this, you need to set up AEM to run on HTTPS. For development purposes you can use self-signed certificate.

[See this document](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/security/use-the-ssl-wizard.html) on how to set up AEM running on HTTPS including a self-signed certificate you can use.

## Install the Universal Editor Service {#install-ue-service}

The Universal Editor Service is not an entire copy of the Universal Editor, but only a subset of its features to ensure that calls from your local AEM environment are not routed over the internet, but from a defined endpoint you control.

[NodeJS version 20](https://nodejs.org/en/download/releases) is required to run a local copy of the Universal Editor Service.

The Universal Editor Service is available via Software Distribution. Please see the [Software Distribution documentation](https://experienceleague.adobe.com/docs/experience-cloud/software-distribution/home.html) for details on how to access it.

Save the `universal-editor-service.cjs` file from Software Distribution to your local development environment.

## Create a Certificate to Run the Universal Editor Service with HTTPS {#ue-https}

The Universal Editor Service also requires a certificate to run on HTTPS in your development environment.

Run the following command.

```text
$ openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
```

The command generates a `key.pem` and a `certificate.pem` file. Save these files to the same path as your `universal-editor-service.cjs` file.

## Setting up the Universal Editor Service Configuration {#setting-up-service}

A number of environment variables must be set in NodeJS to run the Universal Editor Service locally.

On the same path as your `universal-editor-service.cjs`, `key.pem` and `certificate.pem` files, create an `.env` file with the following content.

```text
UES_PORT=8000
UES_PRIVATE_KEY=./key.pem
UES_CERT=./certificate.pem
UES_TLS_REJECT_UNAUTHORIZED=false
UES_CORS_PRIVATE_NETWORK=true
```

These are the minimum values required for local development in our example.

>[!NOTE]
>
>If you are running Chrome version 130+, you must enable sending CORS headers for [private network access](https://wicg.github.io/private-network-access/#private-network-request) using the `UES_CORS_PRIVATE_NETWORK` option.


The following table details these and additional values available.

|Value|Optional|Default|Description|
|---|---|---|---|
|`UES_PORT`|Yes|`8080`|Port on which the server runs|
|`UES_PRIVATE_KEY`|Yes|None|Path to the private key for HTTPS server|
|`UES_CERT`|Yes|None|Path to the certification file for HTTPS server|
|`UES_TLS_REJECT_UNAUTHORIZED`|Yes|`true`|Reject unauthorized TLS connections|
|`UES_DISABLE_IMS_VALIDATION`|Yes|`false`|Disable IMS validation|
|`UES_ENDPOINT_MAPPING`|Yes|Empty|Mapping of the endpoints for internal rewrites<br>Example: `UES_ENDPOINT_MAPPING='[{"https://your-public-facing-author-domain.net": "http://10.0.0.1:4502"}]'`<br>Result: Universal Editor Service will connect to `http://10.0.0.1:4502` instead of the provided connection `https://your-public-facing-author-domain.net`|
|`UES_LOG_LEVEL`|Yes|`info`|Log level for the server, possible values are `silly`, `trace`, `debug`, `verbose`, `info`, `log`, `warn`, `error`, and `fatal`|
|`UES_SPLUNK_HEC_URL`|Yes|None|HEC URL to Splunk endpoint|
|`UES_SPLUNK_TOKEN`|Yes|None|Splunk token|
|`UES_SPLUNK_INDEX`|Yes|None|Index to write logs to|
|`UES_SPLUNK_SOURCE`|Yes|`universal-editor-service`|Name of the source in the splunk logs|
|`UES_CORS_PRIVATE_NETWORK`|Yes|`false`|Enable sending CORS headers to allow [Private network](https://wicg.github.io/private-network-access/#private-network-request). Required for users of Chrome version 130+|

>[!NOTE]
>
>Prior to the [2024.08.13 release](/help/release-notes/universal-editor/current.md) of the Universal Editor, the following variables were required in the `.env` file. These values will be supported until 1 October 2024 for backwards compatibility.
>
>`EXPRESS_PORT=8000`
>`EXPRESS_PRIVATE_KEY=./key.pem`
>`EXPRESS_CERT=./certificate.pem`
>`NODE_TLS_REJECT_UNAUTHORIZED=0`

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

With the [Universal Editor Service running locally](#running-ue) and your [content page instrumented to use the local service](#using-loca-ue), you can now start the editor.

1. Open your browser to `https://localhost:8000/ping`.
1. Direct your browser to accept [your self-signed certificate](#ue-https).
1. Once the self-signed certificate is trusted, you can edit the page using your local Universal Editor Service.

