---
title: Configure SAML 2.0 Authentication for Associate UI
description: Learn how to implement SAML 2.0 authentication on AEM Publish instance to protect Forms Associate UI using Microsoft Entra ID.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: Admin, Developer
---

# Configure SAML 2.0 Authentication for Associate UI

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

This article provides a complete guide for implementing SAML 2.0 authentication on AEM Publish instance to protect the Forms Associate UI (`/libs/fd/associate/ui.html`) using Microsoft Entra ID.

## What You Achieve

After completing this configuration:

- End users authenticate via Microsoft Entra ID to access Forms Associate UI
- Users are automatically created in AEM with synced attributes (name, email)
- Users are automatically assigned to the `forms-associates` group
- Session persistence is maintained across requests

## Prerequisites

Before you begin, ensure you have:

- Cloud Manager Deployment Manager access
- AEM Administrator access (Author and Publish)
- Microsoft Entra ID Administrator access
- Git repository access
- AEM user group `forms-associates` exists

For more information about SSO options, see [What is single sign-on in Microsoft Entra ID?](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/what-is-single-sign-on)

## Implementation Steps

### Step 1: Configure Microsoft Entra ID (Azure AD)

#### Create Enterprise Application

1. Navigate to **Azure Portal** > **Azure Active Directory** > **Enterprise Applications** > **New application**
2. Click **Create your own application**
3. Enter the name: `AEM Forms Associate UI - SAML`
4. Select **Integrate any other application (Non-gallery)**
5. Click **Create**

#### Configure SAML Settings

1. Go to **Single sign-on** > Select **SAML**
2. Edit **Basic SAML Configuration** with the following values:

| Field | Value Pattern |
|-------|---------------|
| Identifier (Entity ID) | `https://publish-p{program-id}-e{env-id}.adobeaemcloud.com` |
| Reply URL | `https://publish-p{program-id}-e{env-id}.adobeaemcloud.com/libs/fd/associate/saml_login` |
| Sign on URL | `https://publish-p{program-id}-e{env-id}.adobeaemcloud.com/libs/fd/associate/ui.html` |

3. Save the configuration
4. Download **Certificate (Base64)** from the **SAML Signing Certificate** section
5. Go to **Users and groups** > **Add user/group** > Assign test users

### Step 2: Install Certificate in AEM

1. Navigate to **AEM Author** > **Tools** > **Security** > **Trust Store**
2. Create Trust Store if needed (set password and record it securely)
3. Click **Add Certificate from CER file** > Upload the Azure AD certificate
4. Note the certificate alias (for example, `certAlias___1234567890123`)
5. Create a package: **Tools** > **Deployment** > **Packages**
6. Add filter: `/etc/truststore`
7. Build the package and replicate to Publish

### Step 3: Configure SAML Authentication Handler

Create the file `com.adobe.granite.auth.saml.SamlAuthenticationHandler~saml.cfg.json` in the following location:

`ui.config/src/main/content/jcr_root/apps/<project-name>/osgiconfig/config.publish`

```json
{
  "path": ["/libs/fd/associate"],
  "serviceProviderEntityId": "https://publish-p{program-id}-e{env-id}.adobeaemcloud.com",
  "assertionConsumerServiceURL": "https://publish-p{program-id}-e{env-id}.adobeaemcloud.com/libs/fd/associate/saml_login",
  "idpUrl": "https://login.microsoftonline.com/{azure-tenant-id}/saml2",
  "idpCertAlias": "{your-certificate-alias}",
  "idpIdentifier": "https://sts.windows.net/{azure-tenant-id}/",
  "userIDAttribute": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name",
  "createUser": true,
  "userIntermediatePath": "saml",
  "synchronizeAttributes": [
    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname=profile/givenName",
    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname=profile/familyName",
    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress=profile/email"
  ],
  "identitySyncType": "idp",
  "addGroupMemberships": true,
  "defaultGroups": ["forms-associates"],
  "groupMembershipAttribute": "http://schemas.microsoft.com/ws/2008/06/identity/claims/groups",
  "defaultRedirectUrl": "/libs/fd/associate/ui.html",
  "idpHttpRedirect": false,
  "service.ranking": 5002
}
```

**Key Configuration Properties:**

| Property | Description |
|----------|-------------|
| `path` | Must be set to `/libs/fd/associate` for Associate UI |
| `serviceProviderEntityId` | Must match the Identifier configured in Azure AD |
| `assertionConsumerServiceURL` | Must match the Reply URL configured in Azure AD |
| `idpCertAlias` | Must match the certificate alias in Trust Store exactly (case-sensitive) |
| `createUser` | Set to `true` to automatically create users in AEM |
| `defaultGroups` | Set to `forms-associates` for automatic group assignment |
| `defaultRedirectUrl` | Redirects authenticated users to the Associate UI |
| `idpHttpRedirect` | Must be `false` for SP-initiated flow |

### Step 4: Configure Sling Authenticator

Create the file `org.apache.sling.engine.impl.auth.SlingAuthenticator~saml.cfg.json` in the following location:

`ui.config/src/main/content/jcr_root/apps/<project-name>/osgiconfig/config.publish`

```json
{
  "sling.auth.requirements": ["+/libs/fd/associate/ui.html"],
  "sling.auth.anonymous": false
}
```

>[!IMPORTANT]
>
> The PID must be `org.apache.sling.engine.impl.auth.SlingAuthenticator`. System paths like `/libs/` require explicit Sling Authenticator configuration.

### Step 5: Configure Referrer Filter

Update or create the file `org.apache.sling.security.impl.ReferrerFilter.cfg.json` in the following location:

`ui.config/src/main/content/jcr_root/apps/<project-name>/osgiconfig/config.publish`

```json
{
  "allow.hosts": ["login.microsoftonline.com"],
  "filter.methods": ["POST"]
}
```

### Step 6: Configure CORS Policy

Create the file `com.adobe.granite.cors.impl.CORSPolicyImpl~saml.cfg.json` in the following location:

`ui.config/src/main/content/jcr_root/apps/<project-name>/osgiconfig/config.publish`

```json
{
  "alloworigin": ["https://login.microsoftonline.com"],
  "allowedpaths": [".*/saml_login"],
  "supportedmethods": ["POST"]
}
```

### Step 7: Configure Dispatcher

New IC customers must add the rules below to the `filters.any` configuration file in their Git repository to ensure that IC APIs and Associate UI function correctly on the Publish instance.

```
# Allow POST for Forms IC Document Services APIs and Associate UI
/XXXX { /type "allow" /method '(GET|OPTIONS)' /url "/adobe/communications" }
/XXXX { /type "allow" /method '(GET|POST|OPTIONS)' /url "/adobe/communications/*" }
/XXXX { /type "allow" /method '(GET|OPTIONS)' /url "/libs/fd/associate/*" }
```

>[!NOTE]
>
> - Typical path to the `filters.any` file: `<git_repo_root>/dispatcher/src/conf.dispatcher.d/filters/filters.any`
> - Replace `XXXX` with the next appropriate numerical sequence used in your existing `filters.any` file.

### Step 8: Deploy and Test

1. Build the project:

   ```bash
   mvn clean install
   ```

2. Commit and push the changes:

   ```bash
   git add .
   git commit -m "SAML 2.0 configuration for Forms Associate UI"
   git push origin main
   ```

3. Deploy via Cloud Manager pipeline

4. Test the authentication:
   - Open an incognito browser window
   - Navigate to the protected URL: `https://publish-p{program-id}-e{env-id}.adobeaemcloud.com/libs/fd/associate/ui.html`
   - You should be redirected to Microsoft login
   - After login, you should be redirected back to AEM Associate UI

## Troubleshooting

### Authentication Not Triggering

**Symptom**: 404 error or no redirect to Azure AD

**Solution**:
- Verify the path is listed in `/system/console/slingauth`
- Ensure the PID is correct: `org.apache.sling.engine.impl.auth.SlingAuthenticator`
- System paths (`/libs/`) need explicit Sling Authenticator configuration
- Check the handler is active in `/system/console/components`

### AADSTS750054: SAMLRequest Missing

**Symptom**: Azure error "SAMLRequest must be present"

**Solution**:
- Set `idpHttpRedirect` to `false` (SP-initiated flow)
- Verify `?SAMLRequest=` appears in the URL via browser DevTools Network tab

### Status 422: Invalid Payload

**Symptom**: POST from Azure returns 422

**Solution**: Ensure all three filters are configured:
- ReferrerFilter: `login.microsoftonline.com` in `allow.hosts`
- CORS: Allow `https://login.microsoftonline.com` origin
- Dispatcher: Allow POST to `*/saml_login`

### Certificate Not Found

**Symptom**: Certificate error in logs

**Solution**:
- Install the certificate in Author Trust Store
- Package `/etc/truststore` and replicate to Publish
- Verify the alias matches exactly (case-sensitive)

### Certificate Validation Failed

**Symptom**: Certificate exists but validation fails

**Solution**:
- Check `idpCertAlias` matches Trust Store alias exactly
- Common issue: typo in alias (even one character difference causes failure)

### User Not Created

**Symptom**: Authentication works but no user appears in AEM

**Solution**:
- Set `createUser` to `true`
- Check `userIDAttribute` matches the Azure claim
- Use full URI format for Azure AD attributes

### No IDP Found Error

**Symptom**: Log error but authentication works

**Solution**: This can be ignored if authentication is functioning correctly

### Configuration Not Reflecting

**Symptom**: Configuration deployed but not active

**Solution**:
- Verify correct PID in filename
- Check the configuration is in `config.publish` folder (not `config.author`)
- Review `/system/console/configMgr` for configuration status

## See Also

- [SAML 2.0 Authentication on AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/authentication/saml-2-0)
- [What is single sign-on in Microsoft Entra ID?](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/what-is-single-sign-on)
- [Invoke an Associate UI on Publish instance](/help/forms/invoke-associate-ui.md)
- [Associate UI in Interactive Communication Editor](/help/forms/interactive-communication/associate-ui-in-interactive-communication-editor.md)
