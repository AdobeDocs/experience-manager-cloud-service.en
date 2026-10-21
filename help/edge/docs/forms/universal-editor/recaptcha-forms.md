---
title: Add Google reCAPTCHA to Forms in Universal Editor
description: Configure score-based Google reCAPTCHA Enterprise protection in Edge Delivery Services forms to prevent spam and automated attacks.
feature: Edge Delivery Services
keywords: reCAPTCHA in forms, Using reCAPTCHA in Universal Editor, Add reCAPTCHA in forms, form security, spam protection
role: Developer, Admin
level: Intermediate
exl-id: 1f28bd13-133f-487e-8b01-334be7c08a3f
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: f2d27a5f-0d67-4d85-8a24-86a8d8a3574b
    internal-label: Developer tools
subfeature_v2:
  - id: f88183b7-5ea5-436c-ac46-96b53f0281ea
    internal-label: Edge Delivery Services
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
---

# Add Google reCAPTCHA to Forms in Universal Editor

Google reCAPTCHA helps protect forms by distinguishing between human users and automated bots. Edge Delivery Services Forms supports only reCAPTCHA Enterprise with score-based site keys. This guide explains how to configure this protection for forms in Universal Editor.

**Objectives:**

- Configure reCAPTCHA Enterprise with a score-based site key
- Add reCAPTCHA to your forms
- Validate and test the implementation
- Monitor and optimize performance

## Prerequisites

Before starting, ensure you have the following:

### Access Requirements

- AEM as a Cloud Service authoring access
- Universal Editor access with form editing permissions

### Technical Requirements

- Active Google account
- Google Cloud Platform project with billing enabled
- Verified domain ownership for your forms

### Knowledge Requirements

- Basic understanding of AEM Forms and Universal Editor
- Familiarity with cloud service configurations
- Understanding of form security concepts

## Why Use reCAPTCHA in Your Forms?

reCAPTCHA Enterprise evaluates user interactions to help protect forms from spam and automated abuse. Google documents the following capabilities:

| Capability | What Google provides |
|------------|----------------------|
| Risk-based assessments | A score from 0.0 to 1.0 for each assessed interaction. Higher scores indicate lower risk; lower scores indicate higher risk. See [Interpret assessments for websites](https://docs.cloud.google.com/recaptcha/docs/interpret-assessment-website). |
| Challenge-free protection | Score-based keys assess interactions without displaying a checkbox or CAPTCHA challenge. See [reCAPTCHA keys](https://docs.cloud.google.com/recaptcha/docs/keys). |
| Analytics and reporting | Dashboards, global fraud reports, and platform logging. Google's Enterprise tier also offers advanced analytics, customer-specific fraud reports, and attack investigation. See [Google's feature comparison](https://docs.cloud.google.com/recaptcha/docs/compare-tiers). |
| Domain restrictions | Website keys can be restricted to specified domains and their subdomains. A key can cover multiple domains. See [Create reCAPTCHA keys for websites](https://docs.cloud.google.com/recaptcha/docs/create-key-website). |
| Additional fraud protections | Google's broader service offers custom policies, advanced risk reason codes, and account and transaction protection features. Availability depends on the tier and feature-specific configuration. See [Google's feature comparison](https://docs.cloud.google.com/recaptcha/docs/compare-tiers). |

**Pricing, quotas, and support:** Costs depend on the Google service tier and assessment volume. Usage is subject to [Google's quotas](https://docs.cloud.google.com/recaptcha/quotas), not unlimited. For current pricing, subscription requirements, and support options, see [Google's tier details](https://docs.cloud.google.com/recaptcha/docs/compare-tiers). Google lists customer support across its tiers and dedicated account management for its Enterprise tier.

## Set Up reCAPTCHA Enterprise


+++ Step 1: Prepare Google Cloud Environment

**Requirements:**

1. Google Cloud Project with billing enabled
2. Project ID (from GCP dashboard)
3. Domain verification for your forms
4. Admin access to GCP and AEM

**Setup:**

1. Create or select a Google Cloud Project
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Note your Project ID

2. Enable reCAPTCHA Enterprise API
   - Go to APIs & Services > Library
   - Search for "reCAPTCHA Enterprise API"
   - Click Enable

3. Create API Credentials
   - Go to APIs & Services > Credentials
   - Click Create Credentials > API Key
   - Copy and store your API key

4. Create Site Key
   - Go to Security > Fraud Defense > Keys
   - Click Create key and select Web as the application type
   - Add your domain(s)
   - Click Next step (optional) to open the additional settings
   - Keep Will you use challenges? turned off to create a score-based site key
   - Click Create key and copy the site key

**Validation Checkpoint:** Ensure you have:

- Project ID
- API Key
- Site Key
- Verified domain in Google Cloud

+++

+++ Step 2: Configure AEM Cloud Configuration Container

![Step-by-step cloud configuration setup](/help/edge/docs/forms/universal-editor/assets/recaptcha-general-configuration.png)
*Figure: Enabling cloud configurations for your form container*

**Setup:**

1. Access Configuration Browser
   - Log in to your AEM author instance
   - Go to Tools > General > Configuration Browser

2. Enable Cloud Configurations
   - Locate your form's configuration container
   - Select Properties
   - Check Cloud Configurations
   - Click Save & Close

3. Verify Configuration
   - Confirm "Cloud Configurations" appears in the container properties

**Validation Checkpoint:** 

- Cloud Configurations enabled for your container
- Container appears in Configuration Browser
- Properties show "Cloud Configurations" as enabled

+++

+++ Step 3: Configure reCAPTCHA Enterprise Service in AEM

![reCAPTCHA Enterprise configuration screen](/help/edge/docs/forms/universal-editor/assets/recaptcha-enterprise.png)
*Figure: reCAPTCHA Enterprise configuration interface in AEM*

**Configuration:**

1. Access reCAPTCHA Configuration
   - Go to Tools > Cloud Services > reCAPTCHA
   - Select your form's configuration container
   - Click Create

2. Configure Enterprise Settings
   - Title: Descriptive name (e.g., "Production reCAPTCHA")
   - Name: System name (auto-generated or custom)
   - Version: Select ReCAPTCHA Enterprise
   - Project ID: Enter your Google Cloud Project ID
   - Site Key: Enter the site key from Google Cloud
   - API Key: Enter your Google Cloud API key
   - Key Type: Select Score-based site key

3. Set Security Threshold
   - Threshold Score: Set between 0.0 and 1.0
   - Recommended values:
     - 0.7-0.9: High security (may block some legitimate users)
     - 0.5-0.7: Balanced security (recommended)
     - 0.1-0.5: Lower security (allows more users)

4. Save and Publish
   - Click Create to save configuration
   - Click Publish to make it available

**Validation Checkpoint:**

- Configuration saved successfully
- All required fields completed
- Configuration published and visible
- No error messages

+++

## Add reCAPTCHA to Your Form

After configuring the reCAPTCHA service, add protection to your form as follows:

![Adding the reCAPTCHA component to a form](/help/edge/docs/forms/universal-editor/assets/add-recaptcha-component.png)
*Figure: Adding the Invisible Captcha component to your form*

+++1. Open Form in Universal Editor
Go to your form in AEM Sites and click Edit to open it in Universal Editor. Wait for the editor to load.

- Go to your form in AEM Sites
- Click Edit to open in Universal Editor
- Wait for the editor to load
+++

+++2. Locate the Form Structure
In the Content Tree (left panel), find your Adaptive Form section and expand the form structure to see insertion points.

- In the Content Tree (left panel), find your Adaptive Form section
- Expand the form structure to see insertion points
+++

+++3. Add reCAPTCHA Component
Add the Captcha (Invisible) component to your form.

- Click the Add (+) icon in your form section
- From the component list, select Captcha (Invisible)
- Alternatively, drag and drop the component from the components panel
+++

+++4. Configure Component (Optional)
Select the newly added captcha component and verify it uses your reCAPTCHA configuration.

- Select the newly added captcha component
- In the Properties panel, verify it uses your reCAPTCHA configuration
- No additional configuration is needed for basic setup
+++

+++5. Publish Your Changes
Publish your changes and verify there are no errors.

- Click Publish in Universal Editor
- Wait for confirmation
- Verify no errors appear
+++

### Verify Implementation

Your protected form is now available at:

```
https://<branch>--<repo>--<owner>.aem.live/content/forms/af/
<form-name>
```

**Example URL:**

```
https://main--my-forms--company.aem.live/content/forms/af/
contact-us-form
```
