---
title: Publish Adaptive Forms with Edge Delivery Services
description: Learn how to publish, configure, and access Adaptive Forms using Edge Delivery Services for production use.
feature: Edge Delivery Services
role: Admin, Architect, Developer
level: Intermediate
keywords: [publish forms, Edge Delivery Services, form configuration, CORS, referrer filter]
exl-id: ba1c608d-36e9-4ca1-b87b-0d1094d978db
---
# Publish Adaptive Forms with Edge Delivery Services

## Overview

Publishing an Adaptive Form makes it available on Edge Delivery Services for end users to access and submit. This process involves three main phases: publishing the form, configuring security settings, and accessing the live form.

**What you'll accomplish:**

- Publish your form to Edge Delivery Services
- Configure security settings for form submission
- Access and verify your published form
- Set up proper URL routing and CORS policies

## Prerequisites

- **Form Requirements:**
  - Adaptive Form created using Edge Delivery Services template
  - Form tested and ready for production use

- **Access Requirements:**
  - AEM Forms author permissions
  - Cloud Manager access (for production configuration)
  - Developer access to form block code (for submission setup)

- **Related Documentation:**
  - [Create forms with Edge Delivery Services](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md)
  - [Configure submit actions](/help/edge/docs/forms/configure-submission-action-for-eds-forms.md)

## Phase 1: Publish Your Form

### Step 1: Initiate Publishing

1. **Access your form**: Open your Adaptive Form in the Universal Editor
2. **Start publishing**: Click the **Publish** icon in the toolbar

   ![Click Publish](/help/forms/assets/publish-icon-eds-form.png)

### Step 2: Review and Confirm

1. **Review publishing assets**: The system shows all assets being published, including your form

   ![On Click Publish](/help/forms/assets/on-click-publish.png)

2. **Confirm publishing**: Click **Publish** to proceed
3. **Verify success**: Look for the confirmation message

   ![Publish Success](/help/forms/assets/publish-success.png)

### Step 3: Verify Publication Status

**Check status**: Click the **Publish** icon again to view current status

![Publish Status](/help/forms/assets/publish-status.png)

**Validation Checkpoint:**

- Form shows "Published" status in the editor
- No error messages during publishing process
- Form appears in published assets list

### Managing Published Forms

**To unpublish a form:**

1. Open your form in the editor
2. Click the three-dot menu (⋯) in the upper-right corner
3. Select **Unpublish**

![Unpublish form](/help/forms/assets/unpublish--form.png)

## Phase 2: Configure Security Settings

### Why Security Configuration is Required

To enable secure form submissions, you must configure security settings that:

- Allow Edge Delivery Services to submit data to AEM
- Prevent unauthorized access to your AEM instance
- Enable CORS (Cross-Origin Resource Sharing) for form submissions
- Filter requests to only allow legitimate Edge Delivery domains

>[!IMPORTANT]
>
>**Required for Production**: These configurations are mandatory for form submissions to work in production environments.

### Step 1: Configure Form Submission URL

**Purpose**: Direct form submissions to your AEM instance

**File Location**: `blocks/form/constant.js` in your Edge Delivery Services project

**Configuration Examples:**

```javascript
// Production Environment
export const submitBaseUrl = 'https://publish-p120-e12.adobeaemcloud.com';

// Local Development Environment  
export const submitBaseUrl = 'http://localhost:4503';

// Staging Environment
export const submitBaseUrl = 'https://publish-staging-p120-e12.adobeaemcloud.com';
```

**Validation Checkpoint:**

- `constant.js` file updated with correct AEM publish URL
- URL matches your environment (production, staging, or local)
- No trailing slash in the URL

### Step 2: Configure CORS Settings

**Purpose**: Allow form submission requests from Edge Delivery Services domains

**Implementation**: Add CORS configuration to your AEM dispatcher or Apache configuration

```apache
# Local Development Environment
SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(http://localhost(:\d+)?$)#" CORSTrusted=true

# Edge Delivery Services - Preview/Stage Environment  
SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(https://.*\.hlx\.page$)#" CORSTrusted=true

# Edge Delivery Services - Production Environment
SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(https://.*\.hlx\.live$)#" CORSTrusted=true
```

**Validation Checkpoint:**

- CORS rules applied to dispatcher configuration
- All required domains (localhost, hlx.page, hlx.live) are included
- Configuration deployed to target environment

**Reference Documentation:**

- [CORS Configuration Guide](https://experienceleague.adobe.com/en/docs/experience-manager-learn/getting-started-with-aem-headless/deployments/configurations/cors)
- [Referrer Filter Documentation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/deployment/referrer-filter)

### Step 3: Configure Referrer Filter

**Purpose**: Restrict write operations to authorized Edge Delivery Services domains

**Implementation Method**: Configure via Cloud Manager in AEM as a Cloud Service

**Configuration File**: Add to your project's OSGi configuration

```json
{
  "allow.empty": false,
  "allow.hosts": [],
  "allow.hosts.regexp": [
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

**Configuration Breakdown:**

- **`allow.empty`**: Rejects requests without referrer headers
- **`allow.hosts.regexp`**: Permits requests from Edge Delivery Services domains
- **`filter.methods`**: Applies filtering to these HTTP methods
- **`exclude.agents.regexp`**: User agents excluded from filtering

**Validation Checkpoint:**

- Referrer filter configuration deployed via Cloud Manager
- Configuration active on AEM publish instance
- Test form submission works from Edge Delivery Services domain
- Unauthorized domains are blocked from submitting forms

**Reference Documentation:**

- [Configure Referrer Filter via Cloud Manager](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/security/understand-cross-origin-resource-sharing)

## Phase 3: Access Your Published Form

### URL Structure for Edge Delivery Services

**Standard URL Format:**

```
https://<branch>--<repo>--<owner>.aem.live/content/forms/af/<form_name>
```

**URL Components:**

- **`<branch>`**: Git branch name (typically `main`)
- **`<repo>`**: Repository name
- **`<owner>`**: GitHub organization or username  
- **`<form_name>`**: Your form's name (lowercase, hyphenated)

**Environment-Specific URLs:**

```
# Production Environment (.aem.live)
https://main--universaleditor--wkndforms.aem.live/content/forms/af/wknd-form

# Preview Environment (.aem.page) 
https://main--universaleditor--wkndforms.aem.page/content/forms/af/wknd-form
```

### Final Validation Steps

**Verify Form Accessibility:**

1. **Test form loading**: Visit your form URL and confirm it loads properly
2. **Test form submission**: Fill out and submit the form to verify data processing
3. **Check responsive design**: Test form on different devices and screen sizes
4. **Validate security**: Ensure CORS and referrer filter are working correctly

**Expected Results:**

- Form loads without errors
- All form fields render correctly
- Form submission processes successfully
- Data appears in configured destination (spreadsheet, email, etc.)
- No console errors related to CORS or security policies


## Next Steps

**Immediate Actions:**

- Test your published form thoroughly
- Monitor form submission data
- Set up analytics tracking if needed

**Advanced Topics:**

- [Configure form submission actions](/help/edge/docs/forms/universal-editor/submit-action.md)
- [Style and theme your forms](/help/edge/docs/forms/universal-editor/style-theme-forms.md)
- [Add reCAPTCHA protection](/help/edge/docs/forms/universal-editor/recaptcha-forms.md)
- [Create responsive form layouts](/help/edge/docs/forms/universal-editor/responsive-layout.md)

## Summary

You have successfully:

- Published your Adaptive Form to Edge Delivery Services
- Configured security settings for form submission
- Set up proper URL access for end users
- Verified form functionality and accessibility

Your form is now live and ready for production use.
