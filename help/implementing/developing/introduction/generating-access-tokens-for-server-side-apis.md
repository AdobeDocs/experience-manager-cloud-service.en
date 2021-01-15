---
title: Generating Access Tokens for Server Side APIs
description: Learn how to facilitate communication between a third party server and AEM as a Cloud Service by generating a secure JWT Token
---

# Introduction {#introduction}

>[!IMPORTANT]
>
>This feature is not yet available. Please see the [Release Notes](/help/release-notes/release-notes-cloud/release-notes-current.md) for an up to date list of features.

Some architectures rely on making calls to AEM as a Cloud Service from an application hosted on a server outside of AEM infrastructure. For example, a mobile application that calls a server, which then makes API requests to AEM as a Cloud Service.

The server-to-server flow is described below, along with a simplified flow for development. The AEM as a Cloud Service [Developer Console](development-guidelines.md#crxde-lite-and-developer-console) is used to generate tokens needed for the authentication process.

## The Server-to-server Flow {#the-server-to-server-flow}

A user with the admin role can generate a AEM as a Cloud Service credential, which should be installed on the server and should be treated carefully as a secret key. This JSON format file contains all the data required to integrate with an AEM as a Cloud Service API. The data is used to create a signed JWT token, which is exchanged with IMS for an IMS access token. This access token can then be used as a Bearer authentication token to make requests to AEM as a Cloud Service.

The server-to-server flow involves the following steps:

* Fetch the AEM as a Cloud Service credentials from the Developer Console
* Install the AEM as a Cloud Service credentials on a non AEM server making calls to AEM
* Generate a JWT token and exchange that token for an access token using Adobe's IMS APIs
* Calling the AEM API with the access token as a Bearer Authentication token

### Fetch the AEM as a Cloud Service Credentials {#fetch-the-aem-as-a-cloud-service-credentials}

Users who have the admin role for an IMS organization will see the integrations tab in the Developer Console for a given environment, as well as two buttons. Clicking the **Get Service Credentials** button will generate the service credentials json, which will contain all the information required for the non AEM server, including client id, client secret, private key, certificate, and configuration for author and publish tiers of the environment, regardless of the pod selection.

![JWT Generation](assets/JWTtoken3.png)

The output will be similar to the following:

```
{
  "ok": true,
  "integration": {
    "imsEndpoint": "ims-na1.adobelogin.com",
    "metascopes": "ent_aem_cloud_sdk,ent_cloudmgr_sdk",
    "technicalAccount": {
      "clientId": "cm-p123-e1234",
      "clientSecret": "4AREDACTED17"
    },
    "email": "abcd@techacct.adobe.com",
    "id": "ABCDAE10A495E8C@techacct.adobe.com",
    "org": "1234@AdobeOrg",
    "privateKey": "-----BEGIN RSA PRIVATE KEY-----\r\REDACTED\r\n==\r\n-----END RSA PRIVATE KEY-----\r\n",
    "publicKey": "-----BEGIN CERTIFICATE-----\r\nREDACTED\r\n-----END CERTIFICATE-----\r\n"
  },
  "statusCode": 200
}
```

### Install the AEM Service Credentials on a Non AEM Server {#install-the-aem-service-credentials-on-a-non-aem-server}

The non-AEM application making calls to AEM should be able to access the AEM as a Cloud Service credentials, treating it as a secret.

### Generate a JWT Token and Exchange It for an Access Token{#generate-a-jwt-token-and-exchange-it-for-an-access-token}

Use the credentials to create a JWT token in a call to Adobe's IMS service in order to retrieve an access token, which is valid for 24 hours.

The AEM-CS Service Credentials may be exchanged for an access token using client libraries designed for this purpose. The client libraries are available from [Adobe's public GitHub repository](https://github.com/adobe/aemcs-api-client-lib), which contains more detailed guidance and latest information.

```
/*jshint node:true */
"use strict";

const fs = require('fs');
const exchange = require("@adobe/aemcs-api-client-lib");

const jsonfile = "aemcs-service-credentials.json";

var config = JSON.parse(fs.readFileSync(jsonfile, 'utf8'));
exchange(config).then(accessToken => {
    // output the access token in json form including when it will expire.
    console.log(JSON.stringify(accessToken,null,2));
}).catch(e => {
    console.log("Failed to exchange for access token ",e);
});
```

The same exchange can be performed in any language capable of generating a signed JWT Token with the correct format and calling the IMS Token Exchange APIs.

The access token will define when it expires, which is typically 12h. There is sample code in the git repository to manage an access token and refresh it before it expires.

### Calling the AEM API {#calling-the-aem-api}

Make the appropriate server-to-server API calls to an AEM as a Cloud Service environment, including the access token in the header. So for the "Authorization" header, use the value `"Bearer <access_token>"`. For example, using `curl`:

```curlc
curl -H "Authorization: Bearer <your_ims_access_token>" https://author-p123123-e23423423.adobeaemcloud.com/content/dam.json
```

## Developer Flow {#developer-flow}

Developers will likely want to test using a development instance of their non-AEM application (either running on their laptop or hosted) that makes requests to a development AEM as a Cloud Service dev environment. However, since developers do not necessarily have admin role access to the AEM as a Cloud Service dev environment, we cannot assume they can generate the JWT bearer described in the regular server-to-server flow. Thus, we provide a mechanism for a developer to generate an access token directly that can be used in requests to AEM as a Cloud Service environments which they have access to. 

See the [Developer Guidelines documentation](/help/implementing/developing/introduction/development-guidelines.md#crxde-lite-and-developer-console) for information about the required permissions to use the AEM as a Cloud Service developer console.

>[!NOTE]
>
>The token is valid for 24 hours after which time it must be regenerated using the same method.

Developers may use this token to make calls from their non-AEM test application to an AEM as a Cloud Service environment. Typically, the developer will use this token with the non-AEM application on their own laptop. Also, the AEM as a Cloud is typically a non-production environment.

The developer flow involves the following steps:

* Generate an access token from the Developer Console
* Call the AEM application with the access token.

Developers can also make API calls to an AEM project running on their local machine, in which case an access token is not needed.

### Generating the Access Token {#generating-the-access-token}

Click the **Get Local Development Token** button in the Developer Console to generate an access token.

### Call then AEM Application with an Access Token {#call-the-aem-application-with-an-access-token}

Make the appropriate server-to-server API calls from the non-AEM application to an AEM as a Cloud Service environment, including the access token in the header. So for the "Authorization" header, use the value `"Bearer <access_token>"`.

## Service Credentials Revocation {#service-credentials-revocation}

Please submit a request to customer support if the JWT bearer token needs to be revoked.