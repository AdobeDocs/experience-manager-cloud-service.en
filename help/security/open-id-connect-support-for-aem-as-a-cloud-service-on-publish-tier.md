---
title: Open ID Connect Support for AEM as a Cloud Service on Publish Tier
description: Learn how to set up Open ID Connect (OIDC) for AEM as a Cloud Service on Publish Tier
feature: Security
role: Admin
exl-id: d2f30406-546c-4a2f-ba88-8046dee3e09b
---
# Open ID Connect Support for AEM as a Cloud Service on Publish Tier {#open-id-connect-support-for-aem-as-a-cloud-service-on-publish-tier}

## Introduction {#introduction}

As organizations modernize their digital experiences, secure and scalable identity management becomes a foundational requirement. Adobe Experience Manager (AEM) Cloud Service now supports OpenID Connect (OIDC) on the Publish tier, allowing seamless and standards-based integration with leading Identity Providers (IdPs) such as Entra ID (Azure AD), Google, Okta, Auth0, Ping Identity, ForgeRock and OIDC supported IDPs.

OIDC is an identity layer on top of the OAuth 2.0 protocol that enables robust user authentication while maintaining simplicity for developers. It is widely adopted for business-to-consumer (B2C), intranet, and partner portal scenarios, where secure user login and identity federations are required.

Until now, AEM customers were responsible for implementing their own custom login logic on the Publish tier, which increased development time and introduced long-term maintenance and security challenges. With native support for OIDC, AEM Cloud Service removes this burden by providing a secure, extensible, and Adobe-supported authentication mechanism for end users accessing Publish environments.

Whether you're delivering a personalized consumer website or an authenticated internal portal, OIDC on Publish simplifies identity federation and reduces risk through centralized identity governance. It also helps organizations meet modern compliance and security standards without sacrificing agility.

## Configure AEM for OIDC Authentication {#configure-aem-oidc-authentication}

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

### Configure the OIDC Connection {#configure-the-oidc-connection}

First, we need to configure the OIDC connection. Multiple OIDC connections can be configured, and each has to have a different name.

1. Create a new `.cfg.json` file that will house the configuration. For example, you can use `org.apache.sling.auth.oauth_client.impl.OidcConnectionImpl~azure.cfg.json` - the **azure** suffix must be a unique identifier for the connection
1. Follow the configuration format in the example below:

   ```
   {
    "name":"azure",
    "scopes":[
      "openid"
    ],
    "baseUrl":"<https://login.microsoftonline.com/tenant-id/v2.0>",
    "clientId":"client-id-from-idp",
    "clientSecret":"xxxxxx"
   }
   ```

In some environments, the identity provider (IdP) may not expose a valid `.well-known` endpoint.
When this occurs, the required endpoints can be defined manually by specifying the following properties in the configuration file.
In this configuration mode, the `baseUrl` property must not be set.
 
   ```
   "authorizationEndpoint": "https://idp-url/oauth2/v1/authorize",
   "tokenEndpoint": "https://idp-url/oauth2/v1/token",
   "jwkSetURL":"https://idp-url/oauth2/v1/keys",
   "issuer": "https://idp-url"
   ```

1. Configure the its properties as follows:
   * The **"name"** can be defined by the user
   * `baseUrl`, `clientid` and `clientSecret` are configuration values that come from the IdP.
   * The scopes must contain at least the value `openid`. 

### Configure OIDC Authentication Handler {#configure-oidc-authentication-handler}

Now, configure the OIDC authentication handler. Multiple OIDC connections can be configured. Each has to have a different name. If they share the same [OAK External Identity Provider](https://jackrabbit.apache.org/oak/docs/security/authentication/identitymanagement.html), they can share users.

1. Create the configuration file. For this example, we'll use `org.apache.sling.auth.oauth_client.impl.OidcAuthenticationHandler~azure.cfg.json`. The `azure` suffix must be a unique identifier. See an example of the configuration file below:

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
   * `callbackUri`: the path to be protected, adding the suffix: `/j_security_check`. That same callbackUri must be also configured in the remote IdP as redirect url.
   * `defaultConnectionName`: configure with the same name defined for the OIDC connection on the previous step+
   * `pkceEnabled`: `true` Proof Key for Code Exchange (PKCE) on Authorization code flow 
   * `idp`: the name of the [OAK External Identity Provider](https://jackrabbit.apache.org/oak/docs/security/authentication/identitymanagement.html). Note that different OAK IDP cannot share users or groups

### Configure SlingUserInfoProcessor {#configure-slinguserinfoprocessor}

1. Create the configuration file. For this example, we'll use `org.apache.sling.auth.oauth_client.impl.SlingUserInfoProcessor~azure.cfg.json`. The `azure` suffix must be a unique identifier. See an example of the configuration file below:

   ```
   {
      "groupsInIdToken":true,
      "groupsClaimName": "groups",
      "connection":"azure",
      "storeAccessToken": false,
      "storeRefreshToken": false,
      "idpNameInPrincipals": true
   }
   ```

1. Then, configure its properties as follows:
   * `groupsInIdToken`: Set to true if the groups are sent in ID Token. If the value is false, or not specified, the groups are read from UserInfo endpoint.
   * `groupsClaimName`: Name of the claim contains the groups to be synchronized in AEM.
   * `connection`: configure with the same name defined for the OIDC connection on the previous step
   * `storeAccessToken`: true if the Access Token must be stored in the repostory. By default this is false. Set it to true only if AEM needs to access resources in behalf of the user stored in external servers protected by the same IdP.
   * `storeRefreshToken`: true if the Refresh Token must be stored in the repostory. By default this is false. Set it to true only if AEM needs to access resources in behalf of the user stored in external servers protected by the same IdP and need to refresh the token from the IdP.
   * `idpNameInPrincipals`: when set to true, the name of the IdP is added as suffix to the user and group principals separated by a ';'. For example, if the IdP name is `azure-idp` and the user name is `john.doe`, the principal stored in oak will be `john.doe;azure-idp`. This is useful when multiple IdPs are configured in oak to avoid conflicts between users or groups with the same name coming from different IdPs. This can also be set to avoid conflicts with users or groups created by other authentication handlers like Saml.
Remark that Access Token and Refresh Token are stored encrypted with AEM master key.


### Configure the Synchronization Handler {#configure-the-synchronization-handler}

At least one Synchronization Handler must me configured to synchronize the users authenticated in oak. For more details, see [this](https://jackrabbit.apache.org/oak/docs/security/authentication/external/defaultusersync.html) page.

Create a file named `org.apache.jackrabbit.oak.spi.security.authentication.external.impl.DefaultSyncHandler~azure.cfg.json`. The  **azure** suffix must be a unique identifier. For more information on how to configure its properties, consult the [Oak User and Group Synchronization documentation](https://jackrabbit.apache.org/oak/docs/security/authentication/external/defaultusersync.html). Please find an example configuration below:

```
{
  "user.expirationTime":"1h",
  "user.membershipExpTime":"1h",
  "group.expirationTime": "1d"
  "user.propertyMapping":[
    "profile/givenName=profile/given_name",
    "profile/familyName=profile/family_name",
    "rep:fullname=profile/name",
    "profile/email=profile/email",
    "access_token=access_token",
    "refresh_token=refresh_token"
  ],
  "user.pathPrefix":"azure",
  "handler.name":"azure"
}
```

During development, expiration times can be reduced to a lower value (for example: 1s) to speed up testing of user and group synchronization in oak.
Below some of the most relevant attributes to be configured in DefaultSyncHandler. Remark that Dynamic Group Memberhsip should always be enabled in Cloud Services.

|  Property name | Notes  | Suggested value  |
|---|---|---|
| `user.expirationTime`  | Duration until a synced user gets expired. Users are synchronized only after the expiration time.  | 1h  |
| `user.membershipExpTime`     | Duration until a synced user membership gets expired. User memberships are synchronized only after the expiration time.  | 1h  |
| `user.dynamicMembership`  | We recommend enabling dynamic group membership  | true  |
| `user.enforceDynamicMembership`  | We recommend enabling the enforcement of dynamic group membership  | true  |
| `group.dynamicGroups`  | We recommend enabling dynamic groups  |  true |
| user.propertyMapping  | The provided implementation of `UserInfoProcessor` synchronizes only few properties. It can be modified and customized.  | <code>"profile/givenName=profile/given_name",</code><br><code>"profile/familyName=profile/family_name",</code><br><code>"rep:fullname=profile/name",</code><br><code>"profile/email=profile/email",</code><br><code>"access_token=access_token",</code><br><code>"refresh_token=refresh_token"</code> |
| `user.membershipNestingDepth`| Returns the maximum depth of group nesting when membership relations are synced. A value of 0 effectively disables group membership lookup. A value of 1 only adds the direct groups of a user. This value has no effect when syncing individual groups only when syncing a users membership ancestry. | 1|

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

The user is authenticated by an ID Token, and additional attributes are fetched in the `userInfo` endpoint defined for the IdP. If additional non-standard operations must be performed, a custom implementation of the [UserInfoProcessor](https://github.com/apache/sling-org-apache-sling-auth-oauth-client/blob/master/src/main/java/org/apache/sling/auth/oauth_client/impl/SlingUserInfoProcessorImpl.java) is the default implementation from Sling. 

### Configure ACL for external groups {#configure-acl-for-external-groups}

When users are authenticated through OIDC, their group memberships are typically synchronized from the external identity provider.
These external groups are created dynamically in the AEM repository but are not automatically associated with any access control entries.
To ensure that users have the appropriate permissions, access control lists (ACLs) must be explicitly defined for these groups.

Two primary approaches are available.

### Option 1 — Local Groups

The external group can be added as a member of a local group that already has the required ACLs.
* The external group must exist in the repository, which occurs automatically when a user belonging to that group logs in for the first time.
* This option is generally preferred when Closed User Groups (CUGs) are in use, as the local group exists on both author and publish environments.

### Option 2 — Direct ACLs on External Groups via RepoInit 

ACLs can be applied directly to external groups using RepoInit scripts.
* This approach is more efficient and is preferred when CUGs are not used.
* The following example shows a RepoInit configuration that assigns read permissions to an external group. The option `ignoreMissingPrincipal` allows the creation of the ACL even if the group does not yet exist in the repository:
    
    ```
    {
      "scripts":[
        "set ACL for \"my-group;my-idp\"  (ACLOptions=ignoreMissingPrincipal)\r\n  allow jcr:read on /content/wknd/us/en/magazine\r\nend"
      ]
    }    
    ```

>[!NOTE]
>The AEM Permissions UI can be used to inspect the ACLs assigned to group principals

## Example: Configure OIDC authentication with Azure Active Directory

### Configure a new Application in Azure Active Directory {#configure-a-new-application-in-azure-ad}

1. Create a new application in Azure Active Directory by following the [Azure Active Directory documentation](https://learn.microsoft.com/en-us/power-pages/security/authentication/openid-settings#create-an-app-registration-in-azure).  See below how the screen detailing the application overview should look:

   ![Application Overview](/help/security/assets/odic-application-overview.png)

1. If Groups or application roles are required, follow the [documentation](https://learn.microsoft.com/en-us/entra/external-id/customers/how-to-use-app-roles-customers) to enable them for the application and send them in the ID Token. Below an example of configured groups:

![OIDC Claim Token ID](/help/security/assets/oidc-claim-id-token.png)

1. Follow the previously documented steps to create the required configuration files. Below an example specific for Azure AD where:
   * We define the name of oidc Connection, Authentication Handler and DefaultSyncHandler as: `azure`
   * The website url is: `www.mywebsite.com`
   * We protect the path `/content/wknd/us/en/adventures` that is accessible only to authenticated users member of the group `adventures`
   * Tennant is: `tennat-id`,
   * Client id is: `client-id`,
   * Secret is: `secret`,
   * The groups are sent in the ID Token in a claim called: `groups`

### org.apache.sling.auth.oauth_client.impl.OidcConnectionImpl~azure.cfg.json

```
{
  "name":"azure",
  "scopes":[
    openid", "User.Read", "profile", "email"
  ],
  "baseUrl":"https://login.microsoftonline.com/tenant-id/v2.0",
  "clientId":"client-id",
  "clientSecret":"secret"
}
```

### org.apache.sling.auth.oauth_client.impl.OidcAuthenticationHandler~azure.cfg.json 

```
{
  "callbackUri":"https://www.mywebsite.com/content/wknd/us/en/adventures/j_security_check",
  "path":[
    "/content/wknd/us/en/adventures"
  ],
  "idp":"azure",
  "defaultConnectionName":"azure"
}
```

### org.apache.jackrabbit.oak.spi.security.authentication.external.impl.ExternalLoginModuleFactory~azure.cfg.json

```
{
  "sync.handlerName":"azure",
  "idp.name":"azure"
}
```

### org.apache.jackrabbit.oak.spi.security.authentication.external.impl.DefaultSyncHandler~azure.cfg.json

```
{
  "user.expirationTime":"1h",
  "user.membershipExpTime":"1h",
  "group.expirationTime": "1d"
  "user.propertyMapping":[
    "profile/givenName=profile/given_name",
    "profile/familyName=profile/family_name",
    "rep:fullname=profile/name",
    "profile/email=profile/email",
    "access_token=access_token",
    "refresh_token=refresh_token"
  ],
  "user.pathPrefix":"azure",
  "group.pathPrefix": "oidc",
  "user.membershipNestingDepth": "1",
  "handler.name":"azure"
}
```

### org.apache.sling.jcr.repoinit.RepositoryInitializer~azure.cfg.json

```
{
  "scripts":[
    "set ACL for \"adventures;azure\"  (ACLOptions=ignoreMissingPrincipal)\r\n  allow jcr:read on /content/wknd/us/en/adventures\r\nend"
  ]
}
```

### org.apache.sling.auth.oauth_client.impl.SlingUserInfoProcessorImpl~azure.cfg.json

```
{
  "groupsInIdToken": "true",
  "storeAccessToken": "false",
  "storeRefreshToken": "false",
  "connection": "azure",
  "groupsClaimName": "groups"
}
```

### Additional Information about Azure AD Groups {#additional-information-about-azure-ad-groups}

To configure a group to for the enterprise application in the Microsoft Azure Portal, you need to search the application on: **Enterprise Applications** and add the groups: <!-- Alexandru: this bit cound be clearer-->

![OIDC Group add](/help/security/assets/oidc-ad-additional-info.png)

To enable the group claim in Id Token, add the claim in the **Token Configuration** section of the Microsoft Azure Portal: <!-- Alexandru: this bit cound be clearer as well-->

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

## How to migrate from Saml Authentication Handler to Oidc Authentication Handler

When AEM is already configured with a SAML Authentication Handler, and users are present in the repository with [data synchronization](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/personalization/user-and-group-sync-for-publish-tier#data-synchronization) enabled, conflicts can occur between the original SAML users and the new OIDC users.

1. Configure the [OidcAuthenticationHandler](#configure-oidc-authentication-handler) and enable `idpNameInPrincipals` in [SlingUserInfoProcessor](#configure-slinguserinfoprocessor) configuration
1. Setup [ACL for external groups](#configure-acl-for-external-groups). 
1. After login from users, the old users created by the saml authentication handler can be deleted.

>[!NOTE]
>Once the SAML Authentication Handler is disabled and the OIDC Authentication Handler is enabled, if [data synchronization](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/personalization/user-and-group-sync-for-publish-tier#data-synchronization) is not enabled, existing sessions become invalid. Users will be required to authenticate again, which results in the creation of new OIDC user nodes in the repository.

