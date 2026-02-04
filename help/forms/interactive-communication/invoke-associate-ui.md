---
title: Invoke an Associate UI on Publish instance
description: Learn how to integrate and invoke the AEM Forms Associate UI on Publish instances to enable customer-facing professionals to generate personalized Interactive Communications in real-time.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
hide: yes
hidefromtoc: yes
---

# Generate Personalized Communications with Associate UI

<span> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.</span>

The Associate UI can be directly invoked on Publish instances, enabling customer-facing professionals such as field associates and service agents to generate personalized communications in real-time during customer interactions. 

The below table depicts the various real-world scenarios where Associate UI can be used to send personalized messages to customers:

| Industry | Use Case |
|----------|----------|
| **Financial Services** | Generate real-time loan confirmation letters, account statements, and risk-profile summaries during customer meetings |
| **Insurance** | Produce instant proof-of-insurance cards and claim disposition summaries at service counters |
| **Healthcare** | Create patient treatment plan summaries with calculated copay amounts and schedules |
| **Government** | Generate police verification reports, citizen service receipts, and case update summaries on-the-spot |

## Prerequisites

Before integrating the Associate UI with your application, ensure you have:

- Interactive Communication created and published
- Browser with popup support enabled
- Associate [users must be part of the forms-associates group](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/forms/administrator-help/setup-organize-users/creating-configuring-roles#assign-a-role-to-users-and-groups)
- Authentication configured using any [authentication mechanism supported by AEM](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/authentication/authentication) (for example, SAML 2.0, OAuth, or custom authentication handlers)

>[!NOTE]
>
>- This article demonstrates authentication configuration using SAML 2.0 with [Microsoft Entra ID (Azure AD) as the Identity Provider](https://learn.microsoft.com/en-us/power-pages/security/authentication/openid-settings). 
>- For Associate UI, additional SAML configurations are required beyond the standard setup explained in the [SAML 2.0 authentication](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/authentication/saml-2-0) article. See the [Additional SAML configurations for Associate UI](#additional-saml-configurations-for-associate-ui) section for details.

### Additional SAML configurations for Associate UI

When configuring SAML 2.0 authentication for the Associate UI, you must apply the following specific settings in your OSGi configuration files.

#### SAML Authentication Handler

Create the file `com.adobe.granite.auth.saml.SamlAuthenticationHandler~saml.cfg.json` in `ui.config/src/main/content/jcr_root/apps/<project-name>/osgiconfig/config.publish`:

```json
  {
    "path": ["/libs/fd/associate"],
    "serviceProviderEntityId": "https://publish-p{program-id}-e{env-id}.adobeaemcloud.com",
    "assertionConsumerServiceURL": "https://publish-p{program-id}-e{env-id}.adobeaemcloud.com/libs/fd/associate/saml_login"
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
      "addGroupMemberships": true,
      "defaultGroups": ["forms-associates"],
      "defaultRedirectUrl": "/libs/fd/associate/ui.html",
      "idpHttpRedirect": false,
      "service.ranking": 5002
  }
```

| Property | Description |
|----------|-------------|
| `path` | Must be set to `/libs/fd/associate` for Associate UI |
| `defaultGroups` | Set to `forms-associates` to automatically assign users to the required group |
| `defaultRedirectUrl` | Redirects authenticated users to the Associate UI |
| `idpHttpRedirect` | Must be `false` for SP-initiated flow |
| `idpCertAlias` | Must match the certificate alias in Trust Store exactly (case-sensitive) |

#### Sling Authenticator

Update the file `org.apache.sling.engine.impl.auth.SlingAuthenticator~saml.cfg.json` in `ui.config/src/main/content/jcr_root/apps/<project-name>/osgiconfig/config.publish`:

```json
{
  "sling.auth.requirements": ["+/libs/fd/associate/ui.html"],
  "sling.auth.anonymous": false
}
```

#### Dispatcher Filter

If not already present, add the following rules to your `dispatcher/src/conf.dispatcher.d/filters/filters.any` file:

```json
  # Allow Interactive Communications APIs and Associate UI
  /XXXX { /type "allow" /method '(GET|OPTIONS)' /url "/adobe/communications" }
  /XXXX { /type "allow" /method '(GET|POST|OPTIONS)' /url "/adobe/communications/*" }
  /XXXX { /type "allow" /method "GET" /url "/content/dam/fd:fonts/*" }
  /XXXX { /type "allow" /method '(GET|OPTIONS)' /url "/libs/fd/associate/*" }
```

>[!NOTE]
>
> Replace `XXXX` with the appropriate numerical sequence used in your existing `filters.any` file.

## Invoking Associate UI on Publish instance

To invoke the Associate UI from your application, configure the Publish instance URL, prepare the data payload, and use the integration function to launch the Associate UI in a new browser window.

### Step 1: Configure the Publish Instance URL

The Associate UI is accessed via a specific endpoint on your AEM Forms Cloud Service Publish instance:

```javascript
const AEM_URL = 'https://publish-p{program-id}-e{env-id}.adobeaemcloud.com/libs/fd/associate/ui.html';
```

Replace `{program-id}` and `{env-id}` with your actual environment values.

For security reasons, parameters such as Interactive Communication ID, prefill service, and service parameters are not passed through the URL. Instead, these parameters are securely passed using a JavaScript function that communicates with the Associate UI via the browser's postMessage API.

### Step 2: Prepare the Data Payload

Structure your data payload with the following format:

```javascript
const data = {
  id: "your-ic-id",              // Required: Interactive Communication ID
  prefill: {                      // Optional: Data to prefill the IC
    serviceName: "YourService",
    serviceParams: { key: "value" }
  },
  options: {}                     // Optional: Additional configuration options
};
```

**Payload Components:**

| Component | Required | Description |
|-----------|----------|-------------|
| `id` | Yes | The identifier of the Interactive Communication (IC) to load |
| `prefill` | Optional | Contains service configuration for data prefilling.|
| `prefill.serviceName` | Optional | Name of the Form Data Model service to invoke for prefilling data |
| `prefill.serviceParams` | Optional | Key-value pairs passed to the prefill service |
| `options` | Optional | Additional properties supported for PDF rendering - locale, includeAttachments, embedFonts, makeAccessible|

### Step 3: Implement the Integration Function

Create a JavaScript function to launch the Associate UI and handle the message communication:

```javascript
function launchAssociateUI(icId, prefillService, prefillParams, options) {
  if (!icId) {
    console.error('IC ID required');
    return;
  }
   
  const data = {
    id: icId,
    prefill: {
      serviceName: prefillService || '',
      serviceParams: prefillParams || {}
    },
    options: options || {}
  };
   
  const AEM_URL = 'https://your-aem.adobeaemcloud.com/libs/fd/associate/ui.html';
  const win = window.open(AEM_URL, '_blank');
   
  if (!win) {
    alert('Please enable pop-ups for this site');
    return;
  }
   
  const readyHandler = (event) => {
    if (event.data && event.data.type === 'READY' && event.data.source === 'APP') {
      win.postMessage({ type: 'INIT', source: 'PORTAL', data: data }, '*');
      window.removeEventListener('message', readyHandler);
    }
  };
   
  window.addEventListener('message', readyHandler);
   
  // Fallback timeout in case READY message is missed
  setTimeout(() => {
    if (win && !win.closed) {
      win.postMessage({ type: 'INIT', source: 'PORTAL', data: data }, '*');
      window.removeEventListener('message', readyHandler);
    }
  }, 1000);
}
```

### Step 4: Invoke the Function

Call the function with appropriate parameters:

```javascript
// Basic invocation with IC ID only
launchAssociateUI('12345', '', {}, {});

// With prefill service
launchAssociateUI('12345', 'IC_FDM', 
  { customerId: '101'}, {});

// With all parameters
launchAssociateUI('12345', 'IC_FDM', 
  { customerId: "101" }, 
  { locale: 'en', includeAttachments: "true" });
```

## Test Your Integration with a Sample HTML Page

To observe how the Associate UI appears on the frontend and test your integration, here is a simple HTML example. This sample page allows you to enter the IC ID, configure prefill service parameters, set PDF options, and launch the Associate UI on your Publish instance.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Associate UI Integration</title>
  <style>
    body { 
      font-family: sans-serif; 
      max-width: 600px; 
      margin: 50px auto; 
      padding: 20px; 
    }
    .form-group { 
      margin: 20px 0; 
    }
    label { 
      display: block; 
      margin-bottom: 5px; 
      font-weight: bold; 
    }
    input, textarea { 
      width: 100%; 
      padding: 8px; 
      border: 1px solid #ccc; 
      border-radius: 4px; 
      box-sizing: border-box;
    }
    textarea { 
      height: 80px; 
      font-family: monospace; 
    }
    button { 
      padding: 10px 20px; 
      margin: 5px; 
      cursor: pointer; 
      border-radius: 4px;
    }
    .btn-primary { 
      background: #007bff; 
      color: white; 
      border: none; 
    }
    .btn-primary:hover {
      background: #0056b3;
    }
    .error { 
      color: red; 
      font-size: 12px; 
      display: none; 
    }
  </style>
</head>
<body>
  <h1>Launch Associate UI</h1>
  
  <form id="form">
    <div class="form-group">
      <label>IC ID *</label>
      <input type="text" id="icId" placeholder="Enter Interactive Communication ID" required>
    </div>
    
    <div class="form-group">
      <label>Prefill Service</label>
      <input type="text" id="serviceName" placeholder="e.g., CustomerDataService">
    </div>
    
    <div class="form-group">
      <label>Service Parameters (JSON)</label>
      <textarea id="serviceParams" placeholder='{"customerId": "12345"}'>{}</textarea>
      <span id="paramsError" class="error">Invalid JSON format</span>
    </div>
    
    <div class="form-group">
      <label>Options (JSON)</label>
      <textarea id="options" placeholder='{"mode": "edit", "locale": "en_US"}'>{}</textarea>
      <span id="optionsError" class="error">Invalid JSON format</span>
    </div>
    
    <button type="button" onclick="reset()">Reset</button>
    <button type="button" class="btn-primary" onclick="launch()">Launch Associate UI</button>
  </form>

  <script>
    // Replace with your AEM Publish instance URL
    const AEM_URL = 'https://publish-p{program-id}-e{env-id}.adobeaemcloud.com/libs/fd/associate/ui.html';
    
    function validateJSON(str, errorId) {
      const err = document.getElementById(errorId);
      try {
        const obj = JSON.parse(str || '{}');
        err.style.display = 'none';
        return obj;
      } catch (e) {
        err.style.display = 'block';
        return null;
      }
    }
    
    function launch() {
      const icId = document.getElementById('icId').value.trim();
      if (!icId) { 
        alert('IC ID is required'); 
        return; 
      }
      
      const params = validateJSON(document.getElementById('serviceParams').value, 'paramsError');
      const opts = validateJSON(document.getElementById('options').value, 'optionsError');
      
      if (!params || !opts) { 
        alert('Please fix JSON errors before launching'); 
        return; 
      }
      
      const data = {
        id: icId,
        prefill: {
          serviceName: document.getElementById('serviceName').value.trim(),
          serviceParams: params
        },
        options: opts
      };
      
      const win = window.open(AEM_URL, '_blank');
      if (!win) { 
        alert('Pop-up blocked. Please enable pop-ups for this site.'); 
        return; 
      }
      
      const handler = (e) => {
        if (e.data && e.data.type === 'READY' && e.data.source === 'APP') {
          win.postMessage({ type: 'INIT', source: 'PORTAL', data }, '*');
          window.removeEventListener('message', handler);
        }
      };
      
      window.addEventListener('message', handler);
      
      // Fallback timeout in case READY message is missed
      setTimeout(() => {
        if (win && !win.closed) {
          win.postMessage({ type: 'INIT', source: 'PORTAL', data }, '*');
          window.removeEventListener('message', handler);
        }
      }, 1000);
    }
    
    function reset() {
      document.getElementById('form').reset();
      document.getElementById('serviceParams').value = '{}';
      document.getElementById('options').value = '{}';
      document.getElementById('paramsError').style.display = 'none';
      document.getElementById('optionsError').style.display = 'none';
    }
  </script>
</body>
</html>
```

### How the Sample Works

1. **IC ID Field**: Enter the Interactive Communication identifier (required)
2. **Prefill Service**: Specify the Form Data Model service name for prefilling data
3. **Service Parameters**: Enter JSON object with parameters to pass to the prefill service
4. **Options**: Enter configuration options for PDF, for example, locale, includeAttachments, embedFonts, makeAccessible
5. **Launch Button**: Opens the Associate UI in a new window and sends the initialization data

## Data Payload Examples

### Minimal Payload (IC Only)

Use this when no prefill data is required:

```json
{
  "id": "12345",
  "prefill": { 
    "serviceName": "", 
    "serviceParams": {} 
  },
  "options": {}
}
```

### With Prefill Data

Use this to dynamically populate the IC with customer data:

```json
{
  "id": "12345",
  "prefill": {
    "serviceName": "IC_FDM",
    "serviceParams": {
      "customerId": "101",
      "accountNumber": "ACC-98765"
    }
  },
  "options": {}
}
```

### With Options Configuration

Use this to specify additional rendering options:

```json
{
  "id": "12345",
  "prefill": {
    "serviceName": "IC_FDM",
    "serviceParams": {
      "customerId": "101",
      "accountNumber": "ACC-98765"
    }
  },
  "options": { 
      locale: "en_US",
      includeAttachments: "true",
      webOptimized: "false",
      embedFonts: "false",
      makeAccessible: "false"
  }
}
```

## Troubleshooting

### Pop-up Blocked

**Problem**: The Associate UI window doesn't open.

**Solution**: 
- Enable pop-ups for your domain in browser settings
- Ensure `window.open()` is called from a user action (e.g., button click)
- Test with different browsers to identify blocking behavior

### Data Not Loading

**Problem**: The Interactive Communication opens but data doesn't populate.

**Solution**:
- Verify the IC ID is correct and the IC is published
- Check browser console for JavaScript errors
- Ensure the `postMessage` structure matches the specification exactly
- Verify the Form Data Model service is configured correctly

### Authentication Error

**Problem**: User receives an authentication error when the Associate UI opens.

**Solution**: 
- Configure SAML 2.0 authentication on the Publish instance
- Verify the user is part of the **forms-associates** group
- Check session timeout settings

### CORS Errors

**Problem**: Cross-Origin Resource Sharing errors in console.

**Solution**: 
- For development: Use `'*'` as target origin in `postMessage`
- For production: Specify the exact origin URL of your application
- Ensure the Publish instance CORS settings allow your application domain

<!--## Best Practices

When implementing the Associate UI integration, follow these best practices:

1. **Validation**: Always validate the IC ID and JSON payload before sending
2. **Error Handling**: Implement proper error handling for `window.open()` failures
3. **User Experience**: Display a loading indicator while the Associate UI initializes
4. **Memory Management**: Remove event listeners after initialization to prevent memory leaks
5. **Testing**: Test the integration with popup blockers enabled to ensure graceful handling
6. **User Permissions**: Verify users have appropriate access to the forms-associates group-->

## See Also

- [Associate UI in Interactive Communication Editor](/help/forms/interactive-communication/associate-ui-in-interactive-communication-editor.md)
- [Interactive Communications on Cloud](/help/forms/early-access-ea-features.md#interactive-communications-on-cloud)
- [Early Access Features](/help/forms/early-access-ea-features.md)