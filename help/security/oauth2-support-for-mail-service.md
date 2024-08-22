---
title: OAuth2 Support for the Mail Service
description: OAuth2 Support for the Mail Service in Adobe Experience Manager as a Cloud.Service.
exl-id: 93e7db8b-a8bf-4cc7-b7f0-cda481916ae9
feature: Security
role: Admin
---

# OAuth2 Support for the Mail Service {#oauth2-support-for-the-mail-service}

AEM as a Cloud Service offers OAuth2 support for its integrated Mail Service to allow organizations to adhere to secure email requirements.

You can configure OAuth for multiple email providers. Below are step-by-step instructions for configuring the AEM Mail Service to authenticate via OAuth2 with Microsoft&reg; Office 365 Outlook. Other vendors can be configured in a similar manner.

For more information on the AEM as a Cloud Service Mail Service, see [Sending Email](/help/implementing/developing/introduction/development-guidelines.md#sending-email).

## Microsoft&reg; Outlook {#microsoft-outlook}

1. Go to [https://portal.azure.com/](https://portal.azure.com/) and log in.
1. Search for **Azure Active Directory** in the search bar and click the result. Alternatively, you can browse directly to [https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview)
1. Click **App Registration** > **New Registration**.

   ![Start app registration process](assets/oauth-outlook1.png)

1. Fill in the information according to your requirements, then click **Register**.
1. Go to the created app, and select **API Permissions**.
1. Click **Add Permission** > **Graph Permission** > **Delegated Permissions**.
1. Select the below permissions for your app, then click **Add Permission**:

   >[!NOTE]
   >
   >Permissions configuration may evolve over time. Work with Microsoft&reg; if these do not work as expected.

   * `https://outlook.office.com/SMTP.Send`
   * `openid`
   * `offline_access`
   * `email`
   * `profile`
1. Go to **Authentication** > **Add a platform** > **Web**, and in the **Redirect Urls** section, add the below URLs - one with and one without a forward slash:
   * `http://localhost/`
   * `http://localhost`
1. Press **Configure** after adding each URL and configure your settings according to your requirements.
1. Next, go to **Certificates and Secrets**, click **New client secret** and follow the on-screen steps to create a secret. Make sure to take note of this secret for later use.
1. Press **Overview** in the left-hand pane and copy the values for **Application (client) ID** and **Directory (tenant) ID** for later use.

To recap, use following information to configure OAuth2 for the Mail service on the AEM side:

* The Auth URL, which is constructed with the tenant ID. It has this form: `https://login.microsoftonline.com/<tenantID>/oauth2/v2.0/authorize`
* The Token URL, which is constructed with the tenant ID. It has this form: `https://login.microsoftonline.com/<tenantID>/oauth2/v2.0/token`
* The Refresh URL, which is constructed with the tenant ID. It has this form: `https://login.microsoftonline.com/<tenantID>/oauth2/v2.0/token`
* The Client ID
* The Client Secret

### Generating the Refresh Token {#generating-the-refresh-token}

Next, generate the refresh token, which is a part of the OSGi configuration in a subsequent step by doing the following:

1. Open the following URL in the browser after replacing `clientID` and `tenantID` with the values specific to your account: 

   ```
   https://login.microsoftonline.com/%3ctenantID%3e/oauth2/v2.0/authorize?client_id=%3cclientId%3e&response_type=code&redirect_uri=http://localhost&response_mode=query&scope=https://outlook.office.com/SMTP.Send%20email%20openid%20profile%20offline_access&state=12345`
   ```

1. When asked, allow permission.
1. The URL redirects to a new location, constructed in this format: 

   ```
   http://localhost/?code=<code>&state=12345&session_state=4f984c6b-cc1f-47b9-81b2-66522ea83f81#`
   ```

1. Copy the value of `<code>` in the example above.
1. Use the following cURL command to get the refreshToken. Replace the tenantID, clientID, and clientSecret with the values for your account, and the value for `<code>`:
   
   ```
   curl --location --request POST 'https://login.microsoftonline.com/<tenantId>/oauth2/v2.0/token' \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --header 'Cookie: buid=0.ARgAep0nU49DzUGmoP2wnvyIkcQjsx26HEpOnvHS0akqXQgYAAA.AQABAAEAAAD--DLA3VO7QrddgJg7Wevry9XPJSKbGVlPt5NWYxLtTl3K1W0LwHXelrffApUo_K02kFrkvmGm94rfBT94t25Zq4bCd5IM3yFOjWb3V22yDM7-rl112sLzbBQBRCL3QAAgAA; esctx=AQABAAAAAAD--DLA3VO7QrddgJg7Wevr4a8wBjYcNbBXRievdTOd15caaeAsQdXeBAQA3tjVQaxmrOXFGkKaE7HBzsJrzA-ci4RRpor-opoo5gpGLh3pj_iMZuqegQPEb1V5sUVQV8_DUEbBv5YFV2eczS5EAhLBAwAd1mHx6jYOL8LwZNDFvd2-MhVXwPd6iKPigSuBxMogAA; x-ms-gateway-slice=estsfd; stsservicecookie=estsfd; fpc=Auv6lTuyAP1FuOOCfj9w0U_5vR5dAQAAALDXP9gOAAAAwIpkkQEAAACT2T_YDgAAAA' \
   --data-urlencode 'client_id=<clientID>' \
   --data-urlencode 'scope=https://outlook.office.com/SMTP.Send https://graph.microsoft.com/Mail.Read https://graph.microsoft.com/Mail.Send https://graph.microsoft.com/User.Read email openid profile offline_access' \
   --data-urlencode 'redirect_uri=http://localhost' \
   --data-urlencode 'grant_type=authorization_code' \
   --data-urlencode 'client_secret=<clientSecret>' \
   --data-urlencode 'code=<code>'
   ```

1. Make note of the refreshToken and accessToken.

### Validating the Tokens {#validating-the-tokens}

Before proceeding to configure OAuth on the AEM side, make sure to validate both the accessToken and refreshToken with the below procedure:

1. Generate the accessToken by using the refreshToken produced in the previous procedure by using the following curl, replacing the values for `<client_id>`,`<client_secret>`, and `<refreshToken>`:

   ```
   curl --location --request POST 'https://login.microsoftonline.com/<tenetId>/oauth2/v2.0/token' \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --header 'Cookie: buid=0.ARgAep0nU49DzUGmoP2wnvyIkcQjsx26HEpOnvHS0akqXQgYAAA.AQABAAEAAAD--DLA3VO7QrddgJg7Wevry9XPJSKbGVlPt5NWYxLtTl3K1W0LwHXelrffApUo_K02kFrkvmGm94rfBT94t25Zq4bCd5IM3yFOjWb3V22yDM7-rl112sLzbBQBRCL3QAAgAA; esctx=AQABAAAAAAD--DLA3VO7QrddgJg7Wevr4a8wBjYcNbBXRievdTOd15caaeAsQdXeBAQA3tjVQaxmrOXFGkKaE7HBzsJrzA-ci4RRpor-opoo5gpGLh3pj_iMZuqegQPEb1V5sUVQV8_DUEbBv5YFV2eczS5EAhLBAwAd1mHx6jYOL8LwZNDFvd2-MhVXwPd6iKPigSuBxMogAA; x-ms-gateway-slice=estsfd; stsservicecookie=estsfd; fpc=Auv6lTuyAP1FuOOCfj9w0U_IezHLAQAAAPeNSdgOAAAA' \
   --data-urlencode 'client_id=<client_id>' \
   --data-urlencode 'scope=https://outlook.office.com/SMTP.Send https://graph.microsoft.com/Mail.Read https://graph.microsoft.com/Mail.Send https://graph.microsoft.com/User.Read email openid profile offline_access' \
   --data-urlencode 'redirect_uri=http://localhost' \
   --data-urlencode 'grant_type=refresh_token' \
   --data-urlencode 'client_secret=<client_secret>' \
   --data-urlencode 'refresh_token=<refreshToken>'
   ```

1. Send a mail using the accessToken, so you can see if it is working properly.

>[!NOTE]
>
> You can get the Postman API collection from [this location](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow).
>
> See the [MSFT OAuth documentation](https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth) for more details.

### Integration with AEM as a Cloud Service {#integration-with-aem-as-a-cloud-service}

1. Create an OSGI property file called `com.day.cq.mailer.oauth.impl.OAuthConfigurationProviderImpl.cfg.json` under `/apps/<my-project>/osgiconfig/config` with the following syntax:
   
   ```
   {
       authUrl: "<Authorization Url>",
       tokenUrl: "<Token Url>",
       clientId: "<clientID>",
       clientSecret: "$[secret:SECRET_SMTP_OAUTH_CLIENT_SECRET]",
       scopes: [
          "scope1",
          "scope2"
       ],
       authCodeRedirectUrl: "http://localhost",
       refreshUrl: "<Refresh token Url>",
       refreshToken: "$[secret:SECRET_SMTP_OAUTH_REFRESH_TOKEN]"
   }
   ```
   
1. Fill in the `authUrl`, `tokenUrl`, and `refreshURL` by constructing them as described in the previous section.
1. Add the following Scopes to the configuration:

   >[!NOTE]
   >
   >Scopes may evolve over time. Work with Microsoft&reg; if these do not work as expected.

   * `https://outlook.office.com/SMTP.Send`
   * `openid`
   * `offline_access`
   * `email`
   * `profile`
1. Create an OSGI property file `called com.day.cq.mailer.DefaultMailService.cfg.json`
under `/apps/<my-project>/osgiconfig/config` with the syntax below. The `smtp.host` and `smtp.port` values reflects advanced networking configuration, as described in the [Email Service tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/networking/examples/email-service).
   
   ```
   {
    "smtp.host": "$[env:AEM_PROXY_HOST;default=proxy.tunnel]",
    "smtp.user": "<user account that logged into get the oauth tokens>",
    "smtp.password": "value not used",
    "smtp.port": 30465,
    "from.address": "<from address used for sending>",
    "smtp.ssl": false,
    "smtp.starttls": true,
    "smtp.requiretls": true,
    "debug.email": false,
    "oauth.flow": true
   }
   ```

1. For outlook, the `smtp.host` configuration value is `smtp.office365.com`
1. At runtime, pass in the `refreshToken values` and `clientSecret` secrets using the [Cloud Manager variables API](/help/implementing/deploying/configuring-osgi.md#setting-values-via-api) or by using [Cloud Manager to add variables](/help/implementing/cloud-manager/environment-variables.md). The values for the variables `SECRET_SMTP_OAUTH_REFRESH_TOKEN`  and `SECRET_SMTP_OAUTH_CLIENT_SECRET` should be defined.
   
### Troubleshooting {#troubleshooting}

If the mail service is not working properly, you, must regenerate the `refreshToken` as described above, passing in the new value via Cloud Manager API. It takes a few minutes for the new value to be deployed.
