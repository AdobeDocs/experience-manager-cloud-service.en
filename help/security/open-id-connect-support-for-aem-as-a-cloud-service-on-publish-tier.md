---
title: Open ID Connect Support for AEM as a Cloud Service on Publish Tier
description: Learn how to set up Open ID Connect (OIDC) for AEM as a Cloud Service on Publish Tier
feature: Security
role: Admin
---

# Open ID Connect Support for AEM as a Cloud Service on Publish Tier

## Introduction {#introduction}

As organizations modernize their digital experiences, secure and scalable identity management becomes a foundational requirement. Adobe Experience Manager (AEM) Cloud Service now supports OpenID Connect (OIDC) on the Publish tier, allowing seamless and standards-based integration with leading Identity Providers (IdPs) such as Entra ID (Azure AD), Google, Okta, Auth0, Ping Identity, ForgeRock and OIDC supported IDPs.

OIDC is an identity layer on top of the OAuth 2.0 protocol that enables robust user authentication while maintaining simplicity for developers. It is widely adopted for business-to-consumer (B2C), intranet, and partner portal scenarios, where secure user login and identity federations are required.

Until now, AEM customers were responsible for implementing their own custom login logic on the Publish tier, which increased development time and introduced long-term maintenance and security challenges. With native support for OIDC, AEM Cloud Service removes this burden by providing a secure, extensible, and Adobe-supported authentication mechanism for end users accessing Publish environments.

Whether you're delivering a personalized consumer website or an authenticated internal portal, OIDC on Publish simplifies identity federation and reduces risk through centralized identity governance. It also helps organizations meet modern compliance and security standards without sacrificing agility.

## Configure an Azure Active Directory OIDC Application {#configure-an-azure-ad-oidc-application}

### Configure a new Application in Azure Active Directory {#configure-a-new-application-in-azure-ad}

First, follow the steps below in order to create a new application in Azure Active Directory:

1. Go to the IAM Portal to set your password and Multi Factor Authentication for the stage version of Active Directory
1. Login to `https://adobe-stage.okta.com/`
1. Go to `portal.azure.com` and select the domain `Adobessostest.com`
1. Click on **More Services** and then on **Identity**
1. Click on **App registration**
1. Add a name, supported account types and redict uri of type "web", as shown in the screenshot below

   ![App Registration](/help/security/assets/odic-register-app.png)

1. See below how the screen detailing the application overview should look:

   ![Application Overview](/help/security/assets/odic-application-overview.png)

1. Create a secret and copy the value.

## Configure the AEM Authentication Handler {#configure-the-aem-authentication-handler}

### Configure the OIDC Connection {#configure-the-oidc-connection}

Next, we need to configure the OIDC connection. Multiple OIDC connections can be configured, and each has to have a different name.

1. Create a new `.cfg.json` file that will house the configuration. For example, you can use `org.apache.sling.auth.oauth_client.impl.OidcConnectionImpl~azure.cfg.json` - the **azure** suffix must be a unique identifier for the connection
1. Follow the configuration format in the example below:

   ```
   {
    "name":"azure",
    "scopes":[
      "openid"
    ],
    "baseUrl":"<https://login.microsoftonline.com/53279d7a-438f-41cd-a6a0-fdb09efc8891/v2.0>",
    "clientId":"5199fc45-8000-473e-ac63-989f1a78759f",
    "clientSecret":"xxxxxx"
   }
   ```

1. Configure the its properties as follows:
   * The **"name"** can be defined by the user
   * `baseUrl`, `clientid` and `clientSecret` are configuration values that come from Azure
   * The scopes must contain at least the value `openid`. 

### Configure OIDC Authentication Handler {#configure-oidc-authentication-handler}

Now, configure the OIDC authentication handler. Multiple OIDC connections can be configured. Each has to have a different name. If they share the same [OAK External Identity Provider](https://jackrabbit.apache.org/oak/docs/security/authentication/externalloginmodule.html), they can share users.

1. Create the configuration file. For this example, we'll use `org.apache.sling.auth.oauth_client.impl.OidcConnectionImpl~azure.cfg.json`. The `azure` suffix must be a unique identifier. See an example of the configuration file below:

   ```
   {
     "path":"/content/tests/us/en/test-7",
     "callbackUri":"http://localhost:14503/content/tests/us/en/test-7/j_security_check",
     "pkceEnabled":false,
     "defaultConnectionName":"azure"
     "idp": "azure-idp"
   }
   ```

1. Then, configure its properties as follows:
   * `path`: the path to be protected
   * `callbackUri`: to the path to be protected, adding the suffix: `/j_security_check`
   * `defaultConnectionName`: configure with the same name defined for the OIDC connection on the previous step+
   * `pkceEnabled`: `false` if this feature is not enabled in Azure AD
   * `idp`: the name of the [OAK External Identity Provider](https://jackrabbit.apache.org/oak/docs/security/authentication/externalloginmodule.html). Note that different OAK IDP cannot share users or groups

### Configure the Synchronization Handler {#configure-the-synchronization-handler}

At least one Synchronization Handler must me configured to synchronize the users authenticated in oak. For more details, see [this](https://jackrabbit.apache.org/oak/docs/security/authentication/external/defaultusersync.html) page.

Create a file named `org.apache.jackrabbit.oak.spi.security.authentication.external.impl.DefaultSyncHandler~azure.cfg.json`. The  **azure** suffix must be a unique identifier. For more information on how to configure its properties, consult the [Oak User and Group Synchronization documentation](https://jackrabbit.apache.org/oak/docs/security/authentication/external/defaultusersync.html). Please find an example configuration below:

```
{
  "user.expirationTime":"1s",
  "user.membershipExpTime":"1s",
  "user.propertyMapping":[
    "profile/familyName=profile/familyName",
    "profile/givenName=profile/givenName",
    "rep:fullname=cn",
    "profile/email=profile/email",
    "oauth-tokens"
  ],
  "user.pathPrefix":"azure",
  "handler.name":"azure"
}
```

### Configure the External Login Module {#configure-the-external-login-module}

Finally, you need to configure the External Login Module.

1. Create a file named `org.apache.jackrabbit.oak.spi.security.authentication.external.impl.ExternalLoginModuleFactory~azure.cfg.json`. See an example configuration below:

   ```
   {
    "sync.handlerName":"azure",
    "idp.name":"azure-idp"
   }
   ```

1. Configure its properties as follows:

   * `sync.handlerName`: name of the Synchronization Handler defined previously
   * `idp.name`: OAK Identity Provider defined in OIDC Authentication Handler

### Optional: Implement a Custom UserInfoProcessor {#implement-a-custom-userinfoprocessor}

The user is authenticated by an ID Token, and additional attributes are fetched in the `userInfo` endpoint defined for the IdP. If additional non-standard operations must be performed, a custom implementation of the [UserInfoProcessor](https://github.com/apache/sling-org-apache-sling-auth-oauth-client/blob/c546845be914a42aaf6c8171f2e486e28728f798/src/main/java/org/apache/sling/auth/oauth_client/spi/UserInfoProcessor.java) can be provided. [Here](https://github.com/apache/sling-org-apache-sling-auth-oauth-client/blob/c546845be914a42aaf6c8171f2e486e28728f798/src/main/java/org/apache/sling/auth/oauth_client/impl/SlingUserInfoProcessorImpl.java) is the default implementation from Sling. 













