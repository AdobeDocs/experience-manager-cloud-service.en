---
title: Add Google reCAPTCHA to Forms in Universal Editor
description: Guide to implementing Google reCAPTCHA protection in Edge Delivery Services forms to prevent spam and automated attacks
feature: Edge Delivery Services
keywords: reCAPTCHA in forms, Using reCAPTCHA in Universal Editor, Add reCAPTCHA in forms, form security, spam protection
role: Developer, Admin
level: Intermediate
exl-id: 1f28bd13-133f-487e-8b01-334be7c08a3f
---

# Add Google reCAPTCHA to Forms in Universal Editor

Google reCAPTCHA helps protect forms by distinguishing between human users and automated bots. This guide explains how to implement both reCAPTCHA Enterprise and Standard versions in Universal Editor.

**Objectives:**

- Select the appropriate reCAPTCHA solution
- Configure reCAPTCHA Enterprise or Standard
- Add reCAPTCHA to your forms
- Validate and test the implementation
- Monitor and optimize performance

## Prerequisites

Before starting, ensure you have the following:

### Access Requirements

- AEM as a Cloud Service authoring access
- Universal Editor access with form editing permissions
- Enrollment in the early access program for reCAPTCHA features

### Technical Requirements

- Active Google account
- For Enterprise: Google Cloud Platform project with billing enabled
- For Standard: Google reCAPTCHA account
- Verified domain ownership for your forms

### Knowledge Requirements

- Basic understanding of AEM Forms and Universal Editor
- Familiarity with cloud service configurations
- Understanding of form security concepts

## Why Use reCAPTCHA in Your Forms?

| ![Security](/help/edge/docs/forms/universal-editor/assets/security.svg) | ![Bot Protection](/help/edge/docs/forms/universal-editor/assets/bot-protection.svg) | ![User Experience](/help/edge/docs/forms/universal-editor/assets/user-experience.svg) |
|:-------------:|:-------------:|:-------------:|
| **Enhanced Security** | **Bot & Spam Prevention** | **Seamless User Experience** |
| Protect forms from fraudulent activities and attacks | Prevent automated bots from submitting forms | Invisible reCAPTCHA does not disrupt legitimate users |

**Key Concept:** reCAPTCHA uses machine learning to analyze user behavior and assigns a score (0.0 to 1.0) indicating the likelihood of human interaction. Higher scores indicate human users; lower scores suggest bots.

**Example:** A tax calculation form handling sensitive data requires protection from automated attacks. reCAPTCHA verifies that submissions are from real users, not bots.

## Choose Your reCAPTCHA Solution

Edge Delivery Services Forms supports two Google reCAPTCHA options. Use the following criteria to select the right solution:

### Quick Decision Guide

**Use reCAPTCHA Enterprise if you have:**

- High-traffic forms (>10,000 requests/month)
- Strict compliance requirements (GDPR, SOX, HIPAA)
- Need for advanced analytics and reporting
- Budget for premium security features
- Complex multi-domain deployments

**Use reCAPTCHA Standard if you have:**

- Low to moderate traffic (<10,000 requests/month)
- Basic security needs
- Limited budget (free tier)
- Simple single-domain setup
- Are new to reCAPTCHA

### Detailed Comparison

| **Feature** | **reCAPTCHA Enterprise** | **reCAPTCHA Standard** |
|-------------|--------------------------|------------------------|
| **Cost** | Paid (usage-based pricing) | Free |
| **Request Limit** | Unlimited | 1M requests/month |
| **Advanced Analytics** | Detailed reporting | Basic stats only |
| **Custom Rules** | Account-specific rules | Global rules only |
| **Multi-domain Support** | Advanced management | Basic support |
| **SLA** | 99.9% uptime guarantee | Best effort |
| **Support** | Enterprise support | Community support |
| **Compliance** | Enterprise-grade | Standard compliance |

**Both solutions provide:**

- Score-based detection (0.0 to 1.0 scale)
- Invisible operation (no user interaction required)
- Machine learning-powered bot detection
- Real-time risk assessment

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
   - Go to Security > reCAPTCHA Enterprise
   - Click Create Key
   - Choose Score-based key type
   - Add your domain(s)
   - Set threshold score (recommended: 0.5)

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

## Set Up reCAPTCHA Standard

+++Step 1: Obtain reCAPTCHA API Keys (See details)

>[!IMPORTANT]
>
> Edge Delivery Services Forms only supports reCAPTCHA v2 (Score-based). Do not use the checkbox version.

**Key Generation:**

1. Access Google reCAPTCHA Console

   - Go to [Google reCAPTCHA Admin Console](https://www.google.com/recaptcha/admin)
   - Sign in with your Google account

2. Create New Site

   - Click + to add a new site
   - Label: Enter a descriptive name
   - reCAPTCHA Type: Select reCAPTCHA v2 > "I'm not a robot" Invisible
   - Domains: Add your form domain(s)
   - Accept terms and click Submit

3. Collect Your Keys

   - Site Key: Copy the site key (public key)
   - Secret Key: Copy the secret key (private key)

**Validation Checkpoint:**

- Site created in reCAPTCHA console

- Site Key obtained

- Secret Key obtained

- Domain(s) added and verified

+++

+++Step 2: Configure AEM Cloud Configuration Container (See details)

Follow the same process as in the Enterprise setup:

1. Enable Cloud Configurations in Configuration Browser

2. Verify container configuration

3. Confirm settings are saved

+++

+++Step 3: Configure reCAPTCHA Standard Service in AEM (See details)

![reCAPTCHA Standard configuration screen](/help/edge/docs/forms/universal-editor/assets/recaptcha.png)
*Figure: reCAPTCHA Standard configuration interface in AEM*

**Configuration:**

1. Access reCAPTCHA Configuration

   - Go to Tools > Cloud Services > reCAPTCHA
   - Select your form's configuration container
   - Click Create

2. Configure Standard Settings

   - Title: Descriptive name (e.g., "Standard reCAPTCHA")
   - Name: System name (auto-generated or custom)
   - Version: Select ReCAPTCHA v2
   - Site Key: Enter your Google reCAPTCHA site key
   - Secret Key: Enter your Google reCAPTCHA secret key

3. Save and Publish

   - Click Create to save configuration
   - Click Publish to make it available

**Validation Checkpoint:**

- Configuration created without errors

- Both keys entered correctly

- Configuration published successfully

- Configuration appears in the list

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
