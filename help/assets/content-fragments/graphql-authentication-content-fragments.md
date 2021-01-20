---
title: Authentication for Remote AEM GraphQL Queries on Content Fragments
description: Learn about the authentication required for Remote AEM GraphQL queries.
---

# Authentication for Remote AEM GraphQL Queries on Content Fragments {#authentication-for-remote-aem-graphql-queries-on-content-fragments}

The [Adobe Experience Manager as a Cloud Service (AEM) GraphQL API used with Content Fragments](/help/assets/content-fragments/graphql-api-content-fragments.md) is primarily designed for remote queries from third party applications or services.  These are not (usually) part of the Adobe infrastructure, but interrogate AEM resources for content.

>[NOTE]
>
>For testing and development you can also access the AEM GraphQL API directly using the [GraphiQL interface](/help/assets/content-fragments/graphql-api-content-fragments.md#graphiql-interface) interface.

For authentication the third party service needs to use an [Access Token](#access-token); this can be obtained for either [development](#retrieving-access-token-development) or for use by a [third party service](#retrieving-access-token-third-party-service).

## Access Token {#access-token}

For a third party service to connect with an AEM instance it needs to have an *Access Token*. The service must then add this token to the *Authorization* header on the POST request. For example, a GraphQL Authorization Header:

```xml
Authorization: Bearer <access_token>
```

## Retrieving an Access Token for use by a Third Party Service {#retrieving-access-token-third-party-service}

To retrieve an Access Token for use by a third party service, it helps to first understand how the access token is generated:

* [Service Credentials are generated, based on a JSON Web Token (JWT)](#creating-service-credentials-json-web-token).
* This is used to [generate the Access Token](#creating-access-token)

>[!NOTE]
>
>* The Service Credentials have a lifespan of 1 year; this is due to the certificates used.
>
>* The Access Token generated through the JWT token is only available for 24 hours after it was generated, This is why it must be fetched again and again using the Service Credentials.
>
>* Calls made using these Access Tokens are processed on the AEM instance with a single [Tech Service Account](#tech-service-account-service-credentials).

### Creating Service Credentials using a JSON Web Token {#creating-service-credentials-json-web-token}

Adobe uses a system based on [JSON Web Token](https://jwt.io/) in order to generate access tokens for service-to-service communications. 

>[!CAUTION]
>
>The first time the service token is generated, it must be from a user with the **IMS Organization Administrator** role. A normal AEM administrator can not perform this action for the first time, but can perform it any time after that.

1. Open the [Developer Console](/help/implementing/cloud-manager/manage-environments.md#accessing-developer-console).

1. Open the **Integrations** tab.

1. Select **Get Service Credentials**.
   
   ![Developer Console - Get Service Credentials](assets/cfm-graphql-auth-dev-console.png)

This will retrieve a JWT (also known as Service Credentials) that looks similar to the following:

```xml
{
  "ok": true,
  "integration": {
    "imsEndpoint": "ims-na1.adobelogin.com",
    "metascopes": "ent_aem_cloud_api",
    "technicalAccount": {
      "clientId": "cm-**REDACTED**-integration",
      "clientSecret": "***REDACTED***"
    },
    "email": "***REDACTED***@techacct.adobe.com",
    "id": "***REDACTED***",
    "org": "***REDACTED***",
    "privateKey": "-----BEGIN RSA PRIVATE KEY----- ***REDACTED**** ----END RSA PRIVATE KEY-----\r\n",
    "publicKey": "-----BEGIN CERTIFICATE----- ***REDACTED*** ----END CERTIFICATE-----\r\n"
  },
  "statusCode": 200
}
```

### Creating an Access Token {#creating-access-token}

The JWT can now be used by a third party service to create Access Tokens.

You can generate an Access Token by calling the Adobe IMS services through requests. The utility tool found at [https://github.com/adobe/aemcs-api-client-lib](https://github.com/adobe/aemcs-api-client-lib) provides an example of how a service can do this.

Using this utility tool as an example, you can receive a response in the form of a Service Access Token:

```xml
{
"token_type": "bearer",
"access_token": "eyJ4-REDACTED-F4MAA",
"expires_in": 86399999
}
```

Your service can now use the `access_token` in its Authorization header of requests to the AEM instance. For example, a GraphQL Authorization Header:

```xml
Authorization: Bearer <access_token>
```

### The Tech Service Account created by the Service Credentials process {#tech-service-account-service-credentials}

Any calls coming through the Service Credentials are managed by only one service tech account on the AEM instance. 

This user account is:

* Created automatically when the IMS Org Administrator generates the Service Credentials for the first time.
* Is automatically added to the contributors group. 
 
You can identify the account, as the user ID is the same as the email for the account used to generate the [JWT Service Credentials JSON](#creating-service-credentials-json-web-token).

![Tech Service Account](assets/cfm-tech-service-account.png)

>[!CAUTION]
>
>All requests for a particular instance go through only one Tech Service Account. 
>
>This means that even if the users have different projects on the instance, the Tech Service Account is the same for all requests. 
>
>The account is unique per environment.

>[!CAUTION]
>
>The Tech Service Account might not automatically have all the proper permissions to perform GraphQL queries. 
>
>Administrators will need to manually add permissions to this account to ensure that GraphQL functions properly.

## Retrieving an Access Token for Development {#retrieving-access-token-development}

If you are developing a third party application, you can get a temporary Access Token directly from the Developer Console: 

>[!CAUTION]
>
>Anyone with [access to the Developer Console](/help/implementing/cloud-manager/manage-environments.md#accessing-developer-console) can generate this Local Development Token.
>
>However, it expires after 24 hours, so it will need to be refreshed every day.

1. Open the [Developer Console](/help/implementing/cloud-manager/manage-environments.md#accessing-developer-console).

1. Open the **Integrations** tab.

1. Select **Get Local Development Token**.
   
   ![Developer Console - Get Local Development Token](assets/cfm-graphql-auth-dev-console.png)

This will generate a **Service Access Token**. For example:

```xml
{
  "ok": true,
  "statusCode": 200,
  "accessToken": "***REDACTED***"
}
```

You can then use the value of the `accessToken` field to create (local) requests to the GraphQL endpoint. To do this, add the token to the Authorization token of the GraphQL Authorization Header:

```xml
Authorization: Bearer <access_token>
```

>[!NOTE]
>
>All requests made using this access token will actually be made *by the user account that generated the token*. 
>
>This means that you need to check that the account has the permissions required to run GraphQL queries. 
>
>You can check this by using GraphiQL on the local instance.
