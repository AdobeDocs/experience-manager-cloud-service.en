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

## Configure an OIDC Application {#configure-an-azure-ad-oidc-application}

### Prerequisites {#prerequisits}

We assume that following information are available or defined:

1. The paths of the content to be protected in the AEM repository
1. An identifier for the IdP to be configured. This can be any string

Information from the IdP Configuration:

1. The Client Id configured in the IdP
1. The Client Secret configured in the Idp. If PKCE was configured on the Idp, the Client Secret is not available. Do not store the plain text value in the configuration file. Use a CM Secret and reference it
1. The scopes configured on the Idp. At least the scope `openid` must be provided
1. Whether PKCE is enabled on the IdP
1. The `callbackUrl` is defined using one of the configured path defined at point 1 and adding the suffix: `/j_security_check`
1. The `baseUrl` to access to the standard `.well-known` file. For example, if the well-known url is: `https://login.microsoftonline.com/53279d7a-438f-41cd-a6a0-fdb09efc8891/v2.0/.well-known/openid-configuration` the `baseUrl` is: `https://login.microsoftonline.com/53279d7a-438f-41cd-a6a0-fdb09efc8891`

### Overview of the Configuration Files {#overview-of-the-configuration-files}

Find below a list of files that need to be configured:

1. **OIDC Connection**: this will be used by the `OidcAuthenticationHandler` to authenticate the users, or by other components to [authorize access to resources protected by the IdP using OAuth](https://github.com/apache/sling-org-apache-sling-auth-oauth-client)
1. **OIDC Authentication Handler**: This is the authentication handler used to authenticate users that access to the configured paths
1. **UserInfoProcessor**: This component process the information received by the IdP. It can be extended by customers to implement custom logic
1. [**Default Synchronization Handler**](https://jackrabbit.apache.org/oak/docs/security/authentication/external/defaultusersync.html): This component creates the user in the repository
1. [**ExternalLoginModule**](https://jackrabbit.apache.org/oak/docs/security/authentication/externalloginmodule.html): This component authenticate the user in the local oak repository.

The following diagram shows how the mentioned configuration elements are linked. Note that since these are `ServiceFactory` components, the `~uniqueid` can be any random unique string:

![OIDC configuration diagram](/help/security/assets/oidc-diagram.png)

### Details on the Configuration of DefaultSyncHandler {#details-on-the-configuration-of-defaultsynchandler}

|  Property name | Notes  | Suggested value  |
|---|---|---|
| `user.expirationTime`  | Duration until a synced user gets expired. Users are synchronized only after the expiration time.  | 1h  |
| `user.membershipExpTime`     | Duration until a synced user membership gets expired. User memberships are synchronized only after the expiration time.  | 1h  |
| `user.dynamicMembership`  | We recommend enabling dynamic group membership  | true  |
| `user.enforceDynamicMembership`  | We recommend enabling the enforcement of dynamic group membership  | true  |
| `group.dynamicGroups`  | We recommend enabling dynamic groups  |  true |
| user.propertyMapping  | The provided implementation of `UserInfoProcessor` synchronizes only few properties. It can be modified and customized.  | <code>"profile/givenName=profile/given_name",</code><br><code>"profile/familyName=profile/family_name",</code><br><code>"rep:fullname=profile/name",</code><br><code>"profile/email=profile/email",</code><br><code>"access_token=access_token",</code><br><code>"refresh_token=refresh_token"</code> ||

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
  "user.expirationTime":"300s",
  "user.membershipExpTime":"300s",
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

### Additional Information about Azure AD Groups {#additional-information-about-azure-ad-groups}

To configure a group to for the enterprise application, you need to search the application on: **Enterprise Applications** and add the groups: <!-- Alexandru: this bit cound be clearer-->

![OIDC Group add](/help/security/assets/oidc-ad-additional-info.png)

To enable the group claim in Id Token, add the claim in **Token Configuration**: <!-- Alexandru: this bit cound be clearer as well-->

![OIDC Claim Token ID](/help/security/assets/oidc-claim-id-token.png)

The configuration of `SlingUserInfoProcessor` must be modified like in the example below.

The filaname that needs to be modified is `org.apache.sling.auth.oauth_client.impl.SlingUserInfoProcessorImpl.cfg.json`. The content should be configured as follows:

```
{
  "connection": "azure",
  "groupsInIdToken": "true",
  "storeAccessToken": "false",
  "storeRefreshToken": "false"
}
```

>[!NOTE]
>
> These changes will work after that following tickets are completed:
> * [SLING-12851](https://issues.apache.org/jira/browse/SLING-12851)
> * [SLING-12850](https://issues.apache.org/jira/browse/SLING-12850)

<!-- Alexandru: is it worth referencing the above SLING tickets in the public docs? -->











