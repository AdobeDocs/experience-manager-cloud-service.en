---
title: Troubleshooting 403 Forbidden Errors in Edge Delivery Services Form Submission
description: Learn how to diagnose and resolve 403 Forbidden errors when submitting forms from Edge Delivery Services to AEM Publish. This guide covers common causes including CORS, Dispatcher rules, and Referrer Filter issues.
feature: Edge Delivery Services, Forms
role: Admin, Developer
---

# Troubleshooting 403 Forbidden Errors in Edge Delivery Services Form Submission {#troubleshooting-403-forbidden-edge-delivery}

When submitting forms from Edge Delivery Services to AEM Publish, you may encounter a **403 Forbidden** error. This error indicates that the server is refusing to process the request, typically due to security configurations. This article helps you identify and resolve the most common causes of this issue.

## Problem Description

Users experience a **403 Forbidden** error when submitting forms from Edge Delivery Services to AEM Publish. The error appears as:

- HTTP Status Code: 403
- Error Message: "Forbidden" or "Access Denied"
- The form submission fails without reaching the AEM submission servlet

This issue commonly occurs in Edge Delivery Services integrations where forms hosted on Edge domains (`.aem.live`, `.aem.page`, `.hlx.page`, `.hlx.live`) attempt to submit data to AEM Publish instances.

>[!IMPORTANT]
>
>With repoless setups, multiple sites can be hosted using the same repository. Each site domain must be individually added to allowlists for form submissions to work properly.
>
>**Example:**
>
>- Repository: `https://github.com/adobe/abc`
>- Site 1: `main--abc--adobe.aem.live`
>- Site 2: `main--abc1--adobe.aem.live`
>
>Both domains need separate allowlist entries for form submission to function from both sites.

## Common Causes and Solutions

A 403 Forbidden error in Edge Delivery Services form submission can have multiple causes. Follow these troubleshooting steps in order:

### 1. CORS (Cross-Origin Resource Sharing) Issues

**Symptoms:**

- Browser console shows CORS-related error messages
- Network tab shows the request being blocked before reaching the server
- Error messages mentioning "Cross-Origin Request Blocked"

**Diagnosis:**

1. Open browser Developer Tools (F12)
2. Check the Console tab for CORS error messages
3. Look for messages like: `Access to fetch at 'https://publish-xxx.adobeaemcloud.com' from origin 'https://main--repo--owner.aem.live' has been blocked by CORS policy`

**Solution:**
Configure CORS settings in AEM to allow requests from your specific Edge Delivery site domains:

```apache
# Developer Localhost
SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(http://localhost(:\d+)?$)#" CORSTrusted=true

# Edge Delivery Sites - Add each site domain individually
SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(https://main--abc--adobe\.aem\.live$)#" CORSTrusted=true
SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(https://main--abc1--adobe\.aem\.live$)#" CORSTrusted=true

# Legacy Franklin domains (if still in use)
SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(https://.*\.hlx\.page$)#" CORSTrusted=true  
SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(https://.*\.hlx\.live$)#" CORSTrusted=true
```

>[!NOTE]
>
>Replace `main--abc--adobe.aem.live` and `main--abc1--adobe.aem.live` with your actual site domains. Each site hosted from the same repository requires a separate CORS configuration entry.

For detailed CORS configuration, refer to the [CORS Configuration Guide](https://experienceleague.adobe.com/en/docs/experience-manager-learn/getting-started-with-aem-headless/deployments/configurations/cors).

### 2. Dispatcher Rules

**Symptoms:**

- 403 error occurs without CORS messages in browser console
- Request reaches the server but is blocked by Dispatcher
- Error occurs before reaching AEM application layer

**Diagnosis:**

1. Check if the request URL matches any Dispatcher filter rules
2. Review Dispatcher configuration for `/filter` rules that might block POST requests
3. Verify that the form submission endpoint is allowed in Dispatcher configuration

**Solution:**
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

### 3. Referrer Filter Issues

**Symptoms:**

- 403 error with no CORS issues in browser console
- Request reaches AEM but is rejected by Sling Referrer Filter
- Error occurs at the AEM application layer

**Diagnosis:**
Check AEM error logs for Referrer Filter rejection messages:

1. [Access AEM Cloud Service logs through Cloud Manager](/help/implementing/cloud-manager/manage-logs.md)
2. Look for entries in `aemerror.log` containing:
   - "Referrer filter rejected"
   - "org.apache.sling.security.impl.ReferrerFilter"
   - Messages indicating referrer validation failures

**Example log entry:**

```
[ERROR] org.apache.sling.security.impl.ReferrerFilter Referrer filter rejected request with referrer 'https://main--abc--adobe.aem.live' for POST /content/forms/af/submit
```

**Solution:**
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

>[!IMPORTANT]
>
>**Forrepoless setups:** You must add each site domain individually to the `allow.hosts` array. Using only regex patterns may not be sufficient for all scenarios. Include both specific domains and regex patterns for comprehensive coverage.

>[!WARNING]
>
>AEM's Referrer Filter is not an OSGi configuration factory, meaning only one configuration is active on an AEM service at a time. When possible, avoid adding custom Referrer Filter configurations, as this will overwrite AEM's native configurations, and may break product functionality.

## Diagnostic Steps

Follow these steps to identify the specific cause of your 403 error:

### Step 1: Check Browser Console

1. Open browser Developer Tools (F12)
2. Navigate to the Console tab
3. Attempt form submission
4. Look for CORS-related error messages

**If CORS errors are present:** Follow the CORS solution above.
**If no CORS errors:** Proceed to Step 2.

### Step 2: Check Network Tab

1. Open browser Developer Tools (F12)
2. Navigate to the Network tab
3. Attempt form submission
4. Check the failed request details
5. Look at response headers and status

**If request doesn't reach server:** Likely a Dispatcher issue.
**If request reaches server but fails:** Likely a Referrer Filter issue.

### Step 3: Check AEM Logs

1. Access Cloud Manager
2. Navigate to Environments → Your Environment → Logs
3. Download or view `aemerror.log`
4. Search for entries around the time of form submission
5. Look for Referrer Filter or security-related messages

## Prevention and Best Practices

### 1. Proper Configuration During Setup

- Configure CORS, Dispatcher, and Referrer Filter settings during initial Edge Delivery Services setup
- **For each new site:** Add the specific domain to all allowlists (CORS, Referrer Filter)
- Test form submissions in development environment before going live

### 2. Environment-Specific Configurations

- Use different configurations for development, staging, and production environments
- Include localhost domains for local development testing
- **Document all site domains** that need allowlist access for your repository

### 3. Monitoring and Logging

- Set up log monitoring for Referrer Filter rejections
- Implement proper error handling in form submission code
- Use browser developer tools during testing

### 4. Documentation and Team Knowledge

- **Maintain a registry** of all site domains using the same repository
- Train development team on troubleshooting steps
- Maintain a checklist for Edge Delivery Services form setup
- **Update allowlists** whenever new sites are created from existing repositories

## Site Domain Management for Repoless Setups

With Helix-5 and repoless architectures, follow these guidelines:

### When Creating New Sites

1. **Identify the site domain** (e.g., `main--newsite--adobe.aem.live`)
2. **Update CORS configuration** to include the new domain
3. **Update Referrer Filter** to include the new domain in `allow.hosts`
4. **Test form submission** from the new site
5. **Document the new domain** in your site registry

### Domain Naming Patterns

- Standard pattern: `{branch}--{site}--{owner}.aem.live`
- Each site gets a unique domain even when sharing the same repository
- Both `.aem.live` and `.aem.page` domains may be used

### Configuration Management

- Use specific domain entries in `allow.hosts` for better security
- Supplement with regex patterns for broader coverage
- Regularly audit and update allowlists as sites are added or removed

## Additional Resources

- [Referrer Filter Configuration with AEM Headless](/help/headless/deployment/referrer-filter.md)
- [CORS Configuration Guide](https://experienceleague.adobe.com/en/docs/experience-manager-learn/getting-started-with-aem-headless/deployments/configurations/cors)
- [Understanding Cross-Origin Resource Sharing](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/security/understand-cross-origin-resource-sharing)
- [Edge Delivery Services Forms Documentation](/help/edge/docs/forms/universal-editor/publish-forms.md)

## Related Topics

- [Configuring Submit Actions](/help/forms/configuring-submit-actions.md)
- [Forms Submission Service](/help/forms/forms-submission-service.md)
- [Edge Delivery Services Overview](/help/edge/overview.md)


**Need additional help?** If you continue to experience issues after following these troubleshooting steps, contact Adobe Customer Support with:

- Your specific error messages
- AEM Cloud Service environment details
- **All Edge Delivery Services site domains** that need form submission access
- Relevant log entries from the time of the error

**Need additional help?** If you continue to experience issues after following these troubleshooting steps, contact Adobe Customer Support with:

- Your specific error messages
- AEM Cloud Service environment details
- Edge Delivery Services domain information
- Relevant log entries from the time of the error 
