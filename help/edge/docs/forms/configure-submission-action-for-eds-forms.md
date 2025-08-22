---
title: Configure Submit Actions for AEM Forms with Edge Delivery Services
description: Learn how to configure submit actions in AEM Forms using Edge Delivery Services. Choose between Forms Submission Service and AEM Publish Submit Action to handle form data securely and efficiently.
feature: Edge Delivery Services
role: Admin, Architect, Developer
exl-id: 8f490054-f7b6-40e6-baa3-3de59d0ad290
---
# Configure Submit Actions for AEM Forms

Configure form submission handling to route data to spreadsheets, email, or backend systems using AEM Forms with Edge Delivery Services.

## Quick Decision Guide

Choose your submission method:

| Method | Best For | Setup Complexity | Use Cases |
|--------|----------|------------------|-----------|
| **Forms Submission Service** | Simple data capture | Low | Contact forms, surveys, basic data collection |
| **AEM Publish Submission** | Complex workflows | High | Enterprise integrations, custom processing, workflows |

## Prerequisites

Before configuring submit actions, ensure you have:

- AEM Forms as a Cloud Service instance
- Edge Delivery Services project configured  
- Form created using Document Authoring or Universal Editor
- Required permissions for target destinations (spreadsheets, email systems, or AEM)

+++ Method 1: Forms Submission Service

The Forms Submission Service is an Adobe-hosted endpoint ideal for simple data capture scenarios.

### Supported Destinations

- **Spreadsheets**: Google Sheets, Microsoft Excel (OneDrive/SharePoint)
- **Email**: Send form data to specified email addresses

### Configuration Steps

1. **Set Up Destination Access**
   - For spreadsheets: Grant edit permission to `forms@adobe.com` on target spreadsheet
   - For email: Verify recipient email addresses are accessible

2. **Configure Form Submission**
   - Open your form in the authoring environment
   - Set submit action to "Forms Submission Service"
   - Specify target spreadsheet URL or email addresses
   - Save and publish the form

3. **Test Submission**
   - Submit test data through the form
   - Verify data appears in target destination
   - Check error logs if submission fails

### Important Notes

- Service account `forms@adobe.com` requires edit access to target spreadsheets
- Email notifications are sent immediately upon form submission
- Data validation occurs at the service level

![Forms Submission Service Flow](/help/forms/assets/eds-fss.png)

+++

+++ Method 2: AEM Publish Submission

Submit form data directly to your AEM as a Cloud Service Publish instance for complex processing.

### When to Use AEM Publish

- Custom AEM Workflows required after submission
- Form Data Model (FDM) integration with databases
- Third-party service integrations (Marketo, Power Automate, Workfront Fusion)
- Azure Blob Storage or SharePoint document libraries
- Complex server-side validation or processing logic

### Available Submit Actions

- [Submit to REST endpoint](/help/forms/configure-submit-action-restpoint.md)
- [Send email via AEM mail services](/help/forms/configure-submit-action-send-email.md)
- [Submit using Form Data Model](/help/forms/configure-data-sources.md)
- [Invoke AEM Workflow](/help/forms/aem-forms-workflow-step-reference.md)
- [Submit to SharePoint](/help/forms/configure-submit-action-sharepoint.md)
- [Submit to OneDrive](/help/forms/configure-submit-action-onedrive.md)
- [Submit to Azure Blob Storage](/help/forms/configure-submit-action-azure-blob-storage.md)
- [Submit to Microsoft Power Automate](/help/forms/forms-microsoft-power-automate-integration.md)
- [Submit to Adobe Workfront Fusion](/help/forms/submit-adaptive-form-to-workfront-fusion.md)
- [Submit to Adobe Marketo Engage](/help/forms/submit-adaptive-form-to-marketo-engage.md)

![AEM Publish Submission Flow](/help/forms/assets/eds-aem-publish.png)

### Configuration Requirements

#### 1. Update AEM Instance URL in Edge Delivery

Update the AEM Cloud Service instance URL in the `constant.js` file in the `../form` block under `submitBaseUrl`. You can configure the URL based on your environment:

**For Cloud Service instance**

   ```js

   export const submitBaseUrl = '<aem-author-instance-URL>';
   ```

**For local development**

   ```js
   export const submitBaseUrl = 'http://localhost:<port-number>';

   ```
<!--
#### 2. AEM Dispatcher Configuration

Configure Dispatcher on your AEM Publish instance:

- **No Redirects**: Ensure Dispatcher rules do not redirect form submission paths

Update Dispatcher configuration to allow form submission requests:

1. Ensure POST requests to form submission endpoints are allowed
2. Add appropriate filter rules for Edge Delivery domains
3. Verify that the submission servlet path is not blocked

Example Dispatcher filter configuration:

```apache
/filter {
  # Allow POST requests to form submission servlet
  /0100 { /type "allow" /method "POST" /url "/content/forms/af/*" }
  /0101 { /type "allow" /method "POST" /url "/adobe/forms/af/submit/*" }
  /0102 { /type "allow" /method "POST" /url "/content/forms/portal/submit/adaptiveform" }
}
```
-->

#### 2. OSGi Referrer Filter

Configure the Referrer Filter to allow your specific Edge Delivery site domains:

1. Create or update the OSGi configuration file: `org.apache.sling.security.impl.ReferrerFilter.cfg.json`

2. Add the following configuration with your specific site domains:

    ```json
    {
      "allow.empty": false,
      "allow.hosts": [
        "main--abc--adobe.aem.live",
        "main--abc1--adobe.aem.live"
      ],
      "allow.hosts.regexp": [
        "https://.*\\.aem\\.live:443",
        "https://.*\\.aem\\.page:443",
        "https://.*\\.hlx\\.page:443",
        "https://.*\\.hlx\\.live:443"
      ],
      "filter.methods": [
        "POST",
        "PUT",
        "DELETE",
        "COPY",
        "MOVE"
      ],
      "exclude.agents.regexp": [
        ""
      ]
    }
    ```

3. Deploy the configuration through Cloud Manager

#### 3. CORS (Cross-Origin Resource Sharing) Issues

Configure CORS settings in AEM to allow requests from your specific Edge Delivery site domains:

**Developer Localhost**

```apache

SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(http://localhost(:\d+)?$)#" CORSTrusted=true

```

**Edge Delivery Sites - Add each site domain individually**

```apache
SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(https://main--abc--adobe\.aem\.live$)#" CORSTrusted=true
SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(https://main--abc1--adobe\.aem\.live$)#" CORSTrusted=true

```

**Legacy Franklin domains (if still in use)**

```apache

SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(https://.*\.hlx\.page$)#" CORSTrusted=true  
SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(https://.*\.hlx\.live$)#" CORSTrusted=true

```

>[!NOTE]
>
>Replace `main--abc--adobe.aem.live` and `main--abc1--adobe.aem.live` with your actual site domains. Each site hosted from the same repository requires a separate CORS configuration entry.

For detailed CORS configuration, refer to the [CORS Configuration Guide](https://experienceleague.adobe.com/en/docs/experience-manager-learn/getting-started-with-aem-headless/deployments/configurations/cors).

<!--
#### 4. CDN Redirect Rules

Configure your Edge Delivery CDN to route submissions:

- Route requests from `/adobe/forms/af/submit/...` to your AEM Publish instance
- Implementation varies by CDN provider (Fastly, Akamai, Cloudflare)-->

#### 4. Form Configuration

1. Create form in Universal Editor
2. Configure submit action to target AEM Forms action
3. Specify submission endpoint path
4. Publish form to Edge Delivery site

+++
<!--
+++ Form Embedding

Embed forms created in one location into different web pages or sites.

### Use Cases

- Reuse standard forms across multiple landing pages
- Include specialized forms in Document-Authored content
- Maintain single form across multiple EDS projects

### CORS Configuration

Configure Cross-Origin Resource Sharing on the form source:

1. **Add CORS Headers** to form source responses:
   - `Access-Control-Allow-Origin: https://your-host-domain.com`
   - `Access-Control-Allow-Methods: GET, OPTIONS`  
   - `Access-Control-Allow-Headers: Content-Type`

2. **Example Configuration**:

        # Configuration for site hosting the form
        headers:
          - path: /forms/**
            custom:
              Access-Control-Allow-Origin: https://host-domain.com
              Access-Control-Allow-Methods: GET, OPTIONS

### Embedding Steps

1. **Create and Publish Form**
   - Build form using Document Authoring or Universal Editor
   - Configure submission method (FSS or AEM Publish)
   - Publish to standalone URL

2. **Configure CORS**
   - Set up CORS headers on form source site
   - Allow host page domain to fetch form

3. **Embed in Host Page**
   - Add form embedding block to host page
   - Point block to published form URL
   - Publish host page

![Embedded Form Architecture](/help/forms/assets/eds-embedded-form.png)

+++-->

+++ Common Issues

| Issue | Solution |
|-------|----------|
| **Form submission fails** | Check console errors, verify endpoint URL, confirm permissions |
| **Embedded form not appearing** | Configure CORS headers on form source, verify form URL |
| **403/401 errors with AEM** | Update Sling Referrer Filter, check authentication settings |
| **Data not reaching spreadsheet** | Verify `forms@adobe.com` has edit access, check spreadsheet URL |
| **CORS errors** | Add proper `Access-Control-Allow-Origin` headers to form source |

+++

## Configuration Examples

+++ Document-Based Form with Spreadsheet Submission

1. Create form structure in Google Docs/Sheets
2. Configure Forms Submission Service endpoint
3. Grant `forms@adobe.com` edit access to target spreadsheet
4. Publish document to Edge Delivery site
5. Test form submission and data flow

+++

+++ Universal Editor Form with AEM Workflow

1. Build form in Universal Editor
2. Configure submit action to "Invoke AEM Workflow"
3. Set up Dispatcher and referrer filter on AEM Publish
4. Configure CDN routing rules
5. Publish form and test workflow execution

+++

## Best Practices

- **Use Forms Submission Service** for simple data capture scenarios
- **Choose AEM Publish** when complex processing or integrations are required
- **Test thoroughly** in staging environment before production deployment
- **Monitor submissions** using AEM logs and console errors
- **Implement proper error handling** for failed submissions
- **Validate data** at both client and server levels
- **Use HTTPS** for all form submissions and data transmission

## Related Topics

- [Document-Based Authoring with EDS Forms](/help/edge/docs/forms/tutorial.md)
- [Universal Editor with EDS Forms](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md)
- [AEM Forms Submission Service](/help/forms/forms-submission-service.md)
- [Configure Data Sources](/help/forms/configure-data-sources.md)
- [AEM Forms Workflow Reference](/help/forms/aem-forms-workflow-step-reference.md)
