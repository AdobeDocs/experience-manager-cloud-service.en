---
title: OAuth2 Support for the Mail Service
description: Oauth2 Support for the Mail Service in Adobe Experience Manager as a Cloud Service
exl-id: 93e7db8b-a8bf-4cc7-b7f0-cda481916ae9
---
# OAuth2 Support for the Mail Service {#oauth2-support-for-the-mail-service}

AEM as a Cloud Service offers OAuth2 support for its integrated Mail Service, in order to allow organizations to adhere to secure email requirements.

You can configure OAuth for multiple email providers. Below are step-by-step instructions for configuring the AEM Mail Service to authenticate via OAuth2 with Microsoft Office 365 Outlook. Other vendors can be configured in a similar manner.

For more information on the AEM as a Cloud Service Mail Service, see [Sending Email](/help/implementing/developing/introduction/development-guidelines.md#sending-email).

## Microsoft Outlook {#microsoft-outlook}

1. Go to [https://portal.azure.com/](https://portal.azure.com/) and log in.
1. Search for **Azure Active Directory** in the search bar and click on the result. Alternatively, you can browse directly to [https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview)
1. Click on **App Registration** - **New Registration**

   ![](assets/oauth-outlook1.png)

1. Fill in the information according to your requirements, then click on **Register**
1. Go to the newly created app, and select **API Permissions** 
1. Go to **Add Permission** - **Graph Permission** - **Delegated Permissions**
1. Select the below permissions for your app, then click **Add Permission**:
   * `SMTP.Send`
   * `Mail.Read`
   * `Mail.Send`
   * `openid`
   * `offline_access`
1. Go to **Authentication** - **Add a platform** - **Web**, and in the **Redirect Urls** section, add the below URLs - one with and one without a forward slash:
   * `http://localhost/`
   * `http://localhost`
1. Press **Configure** after adding each URL and configure your settings according to your requirements
1. Next, go to **Certificates and Secrets**, click on **New client secret** and follow the on screen steps to create a secret. Make sure to take note of this secret for later use
1. Press **Overview** in the left hand pane and copy the values for **Application (client) ID** and **Directory (tenant) ID** for later use

To recap, you will need to the following information to configure OAuth2 for the Mail service on the AEM side:

* The Auth URL, which will be constructed with the tenant ID. It will have this form: `https://login.microsoftonline.com/<tenantID>/oauth2/v2.0/authorize`
* The Token URL, which will be constructed with the tenant ID. It will have this form: `https://login.microsoftonline.com/<tenantID>/oauth2/v2.0/token`
* The Refresh URL, which will be constructed with the tenant ID. It will have this form: `https://login.microsoftonline.com/<tenantID>/oauth2/v2.0/token`
* The Client ID
* The Client Secret

### Generating the Refresh Token {#generating-the-refresh-token}

Next, you need to generate the refresh token, which will be a part of the OSGi configuration in a subsequent step.

You can do this by following these steps:

1. Open the following URL in the browser after replacing `clientID` and `tenantID` with the values specific to your account: `https://login.microsoftonline.com/<tenantID>/oauth2/v2.0/authorize?client_id=<clientId>&response_type=code&redirect_uri=http://localhost&response_mode=query&scope=https%3A%2F%2Foutlook.office365.com%2FSMTP.Send%20EWS.AccessAsUser.All%20https%3A%2F%2Foutlook.office365.com%2FSMTP.Send%20https%3A%2F%2Foutlook.office365.com%2FMail.Read%20https%3A%2F%2Foutlook.office365.com%2FMail.Send%20openid%20offline_access&state=12345`
1. Allow permission when asked
1. The URL will redirect to a new location, constructed in this format: `http://localhost/?code=<code>&state=12345&session_state=4f984c6b-cc1f-47b9-81b2-66522ea83f81#`
1. Copy the value of `<code>` in the example above
1. Use the following cURL command to get the refreshToken. You need to replace the tenantID, clientID and clientSecret with the values for your account, as well as the value for `<code>`:
   
   ```
   curl --location --request POST 'https://login.microsoftonline.com/<tenantId>/oauth2/v2.0/token' \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --header 'Cookie: buid=0.ARgAep0nU49DzUGmoP2wnvyIkcQjsx26HEpOnvHS0akqXQgYAAA.AQABAAEAAAD--DLA3VO7QrddgJg7Wevry9XPJSKbGVlPt5NWYxLtTl3K1W0LwHXelrffApUo_K02kFrkvmGm94rfBT94t25Zq4bCd5IM3yFOjWb3V22yDM7-rl112sLzbBQBRCL3QAAgAA; esctx=AQABAAAAAAD--DLA3VO7QrddgJg7Wevr4a8wBjYcNbBXRievdTOd15caaeAsQdXeBAQA3tjVQaxmrOXFGkKaE7HBzsJrzA-ci4RRpor-opoo5gpGLh3pj_iMZuqegQPEb1V5sUVQV8_DUEbBv5YFV2eczS5EAhLBAwAd1mHx6jYOL8LwZNDFvd2-MhVXwPd6iKPigSuBxMogAA; x-ms-gateway-slice=estsfd; stsservicecookie=estsfd; fpc=Auv6lTuyAP1FuOOCfj9w0U_5vR5dAQAAALDXP9gOAAAAwIpkkQEAAACT2T_YDgAAAA' \
   --data-urlencode 'client_id=<clientID>' \
   --data-urlencode 'scope=https://outlook.office365.com/SMTP.Send https://outlook.office365.com/Mail.Read https://outlook.office365.com/Mail.Send openid' \
   --data-urlencode 'redirect_uri=http://localhost' \
   --data-urlencode 'grant_type=authorization_code' \
   --data-urlencode 'client_secret=<clientSecret>' \
   --data-urlencode 'code=<code>'
   ```

1. Make note of the refreshToken and accessToken.

### Validating the Tokens {#validating-the-tokens}

Before proceeding to configure OAuth on the AEM side, make sure to validate both the accessToken and refreshToken with the below procedure:

1. Generate the accessToken by using the refreshToken produced in the previous procedure. You can achieve this with following curl, replacing the values for `<client_id>`,`<client_secret>` and `<refreshToken>`:

   ```
   curl --location --request POST 'https://login.microsoftonline.com/<tenetId>/oauth2/v2.0/token' \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --header 'Cookie: buid=0.ARgAep0nU49DzUGmoP2wnvyIkcQjsx26HEpOnvHS0akqXQgYAAA.AQABAAEAAAD--DLA3VO7QrddgJg7Wevry9XPJSKbGVlPt5NWYxLtTl3K1W0LwHXelrffApUo_K02kFrkvmGm94rfBT94t25Zq4bCd5IM3yFOjWb3V22yDM7-rl112sLzbBQBRCL3QAAgAA; esctx=AQABAAAAAAD--DLA3VO7QrddgJg7Wevr4a8wBjYcNbBXRievdTOd15caaeAsQdXeBAQA3tjVQaxmrOXFGkKaE7HBzsJrzA-ci4RRpor-opoo5gpGLh3pj_iMZuqegQPEb1V5sUVQV8_DUEbBv5YFV2eczS5EAhLBAwAd1mHx6jYOL8LwZNDFvd2-MhVXwPd6iKPigSuBxMogAA; x-ms-gateway-slice=estsfd; stsservicecookie=estsfd; fpc=Auv6lTuyAP1FuOOCfj9w0U_IezHLAQAAAPeNSdgOAAAA' \
   --data-urlencode 'client_id=<client_id>' \
   --data-urlencode 'scope=https://outlook.office365.com/SMTP.Send https://outlook.office365.com/Mail.Read https://outlook.office365.com/Mail.Send openid' \
   --data-urlencode 'redirect_uri=http://localhost' \
   --data-urlencode 'grant_type=refresh_token' \
   --data-urlencode 'client_secret=<client_secret>' \
   --data-urlencode 'refresh_token=<refreshToken>'
   ```

1. Send a mail using the accessToken, to see if is working properly.

>[!NOTE]
>
> You can get the Postman API collection from [this location](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow).

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
       refreshUrl: "<Refresh token Url>",
       refreshToken: "$[secret:SECRET_SMTP_OAUTH_REFRESH_TOKEN]"
   }
   ```
   
1. Fill in the `authUrl`, `tokenUrl` and `refreshURL` by constructing them as described in the previous section.
1. Add the following Scopes to the configuration:
   * `openid`
   * `offline_access`
   * `https://outlook.office365.com/Mail.Send`
   * `https://outlook.office365.com/Mail.Read`
   * `https://outlook.office365.com/SMTP.Send`
1. Create an OSGI property file `called com.day.cq.mailer.impl.DefaultMailService.cfg.json`
under `/apps/<my-project>/osgiconfig/config`  with the following syntax:
   
   ```
   {
    "smtp.host": "<smtp hostname>"
    "smtp.user": "<user account that logged into get the oauth tokens>",
    "smtp.password": "value not used",
    "smtp.port": 587,
    "from.address": "<from address used for sending>"
    "smtp.ssl": false,
    "smtp.starttls": true,
    "smtp.requiretls": true,
    "debug.email": false,
    "oauth.flow": true
   }
   ```

1. For outlook, the `smtp.host` configuration value is `smtp.office365.com`
1. At runtime, pass in the `refreshToken values` and `clientSecret` secrets using the Cloud Manager variables API as described [here](/help/implementing/deploying/configuring-osgi.md#setting-values-via-api). The values for the variables `SECRET_SMTP_OAUTH_REFRESH_TOKEN`  and `SECRET_SMTP_OAUTH_CLIENT_SECRET` should be defined.
   
### Troubleshooting {#troubleshooting}

If the mail service is not working properly, you will, in most cases, need to regenerate the `refreshToken` as described above, passing in the new value via Cloud Manager API. It will take a few minutes for the new value to be deployed.
