---
title: Protect Your Forms with reCAPTCHA - A Visual Guide
description: Learn how to easily add Google reCAPTCHA to your Edge Delivery Services forms to prevent spam and bot submissions
feature: Edge Delivery Services
keywords: reCAPTCHA in forms, Using reCAPTCHA in Universal Editor, Add reCAPTCHA in forms, form security, spam protection
role: Developer
exl-id: 1f28bd13-133f-487e-8b01-334be7c08a3f
---

# Protect Your Forms from Spam with Google reCAPTCHA

<span class="preview"> This feature is available through the early access program. To request access, send an email from your official address to <a href="mailto:aem-forms-ea@adobe.com">aem-forms-ea@adobe.com</a> with your GitHub organization name and repository name.</span>



## Why use reCAPTCHA in your forms?

| ![Security](/help/edge/docs/forms/universal-editor/assets/security.svg) | ![Bot Protection](/help/edge/docs/forms/universal-editor/assets/bot-protection.svg) | ![User Experience](/help/edge/docs/forms/universal-editor/assets/user-experience.svg) |
|:-------------:|:-------------:|:-------------:|
| **Enhanced Security** | **Bot & Spam Prevention** | **Seamless User Experience** |
| Protect your forms from fraudulent activities and malicious attacks | Stop automated bots from flooding your forms with irrelevant or harmful content | The invisible reCAPTCHA works behind the scenes without disrupting legitimate users |

For example, a tax calculation form with sensitive financial information needs protection from misuse. reCAPTCHA verifies that submissions come from genuine users, not automated systems.

## Choose Your reCAPTCHA Solution

Edge Delivery Services Forms supports two Google reCAPTCHA options:

| ![reCAPTCHA Enterprise](/help/edge/docs/forms/universal-editor/assets/enterprise.svg) | ![reCAPTCHA Standard](/help/edge/docs/forms/universal-editor/assets/standard.svg) |
|:-------------:|:-------------:|
| [**reCAPTCHA Enterprise**](#set-up-recaptcha-enterprise) | [**reCAPTCHA Standard**](#set-up-recaptcha-standard) |
| Premium, enterprise-grade fraud detection with additional features and customization | Free service with score-based detection that operates invisibly in the background |
| Best for: Large organizations with complex security needs | Best for: Small to medium projects with basic protection needs |

Both options use score-based detection (0.0 to 1.0) to identify human vs. bot interactions without disrupting the user experience.

## Set Up reCAPTCHA Enterprise

### Step 1: Get Your Google Cloud Credentials

Before configuring reCAPTCHA Enterprise, you'll need:

- A [Google Cloud project](https://cloud.google.com/recaptcha/docs/prepare-environment#before-you-begin) with your [Project ID](https://support.google.com/googleapi/answer/7014113)
- [reCAPTCHA Enterprise API enabled](https://cloud.google.com/recaptcha/docs/prepare-environment#enable-api) for your project
- An [API key](https://console.cloud.google.com/apis/credentials) for authentication
- A [site key](https://console.cloud.google.com/security/recaptcha) for your domain

### Step 2: Create a Cloud Configuration Container

![Step-by-step cloud configuration setup](/help/edge/docs/forms/universal-editor/assets/recaptcha-general-configuration.png)

1. Log in to your AEM author instance
2. Navigate to **Tools** > **General** > **Configuration Browser**
3. Find your form and select **Properties**
4. Enable **Cloud Configurations** in the dialog
5. Save and publish your configuration

### Step 3: Configure reCAPTCHA Enterprise Service

![reCAPTCHA Enterprise configuration screen](/help/edge/docs/forms/universal-editor/assets/recaptcha-enterprise.png)

1. Go to **Tools** > **Cloud Services** > **reCAPTCHA**
2. Navigate to your form and click **Create**
3. In the dialog:
   - Select **ReCAPTCHA Enterprise** version
   - Enter a Title and Name
   - Add your Project ID, Site Key, and API key
   - Select **Score-based site key** as Key type
   - Set a threshold score (0-1) to distinguish humans from bots
4. Click **Create** and publish your configuration

## Set Up reCAPTCHA Standard

### Step 1: Get Your API Keys

Before starting, [obtain a reCAPTCHA API key pair](https://www.google.com/recaptcha/admin) (Site key and Secret key) from the Google reCAPTCHA Console.

>[!IMPORTANT]
>
>Edge Delivery Services Forms only supports **reCAPTCHA Score based** version.

### Step 2: Create a Cloud Configuration Container

Follow the same steps as in the Enterprise version to create and publish a cloud configuration container.

### Step 3: Configure reCAPTCHA Standard Service

![reCAPTCHA Standard configuration screen](/help/edge/docs/forms/universal-editor/assets/recaptcha.png)

1. Go to **Tools** > **Cloud Services** > **reCAPTCHA**
2. Navigate to your form and click **Create**
3. In the dialog:
   - Select **ReCAPTCHA v2** version
   - Enter a Title and Name
   - Add your Site Key and Secret Key
4. Click **Create** and publish your configuration

## Add reCAPTCHA to your Form

Now that you've configured reCAPTCHA, it's time to add it to your form:

![Adding the reCAPTCHA component to a form](/help/edge/docs/forms/universal-editor/assets/add-recaptcha-component.png)

1. Open your form in Universal Editor
2. Navigate to the Adaptive Form section in the Content tree
3. Click the **Add** icon and select **Captcha (Invisible)** from the Adaptive Form Components list
   - *Alternatively, drag and drop the component into your form*
4. Click **Publish** to update your form with reCAPTCHA protection

Your form is now protected! View it at:
`https://<branch>--<repo>--<owner>.aem.live/content/forms/af/<form-name>`

![Form with reCAPTCHA protection enabled](/help/edge/docs/forms/universal-editor/assets/form-with-recaptcha.png)

## Validating your reCAPTCHA integration

After adding reCAPTCHA to your form, it's essential to verify that it's working correctly. Here's how to validate your implementation:

### Visual verification

While reCAPTCHA v2 (Score-based) operates invisibly, you can confirm its presence by:

1. **Inspect the page source**: Right-click on your form page and select "View Page Source"
   - Look for the reCAPTCHA script inclusion with your site key
   - Example: `<script src="https://www.google.com/recaptcha/api.js?render=YOUR_SITE_KEY"></script>`

2. **Check Network Requests**: Using browser developer tools (F12)
   - Submit your form and look for network requests to `google.com/recaptcha`
   - These requests indicate reCAPTCHA is active on your form

### Functional testing

To verify reCAPTCHA is actually protecting your form:

1. **Normal Submission Test**:
   - Fill out your form with valid data
   - Submit the form at a normal human pace
   - Verify the form submits successfully

2. **Bot-like Behavior Test**:
   - Open your form in an incognito/private browsing window
   - Fill out the form extremely quickly (automated-like behavior)
   - Submit multiple times in rapid succession
   - If reCAPTCHA is working, these submissions might be blocked or flagged

3. **Check Form Submission Records**:
   - Review your form submission data
   - Each submission should include a reCAPTCHA score
   - Scores closer to 1.0 indicate likely human users
   - Scores closer to 0.0 indicate potential bot activity

### Using Google reCAPTCHA admin console

For Enterprise users, the Google Cloud Console provides detailed analytics:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to **Security** > **reCAPTCHA**
3. Select your site key
4. Review the assessment charts and statistics
5. Look for:
   - Traffic patterns
   - Score distributions
   - Potentially fraudulent activities

For Standard reCAPTCHA users, basic statistics are available in the [reCAPTCHA Admin Console](https://www.google.com/recaptcha/admin/).

### Adjusting your implementation

Based on your validation results:

- If legitimate users are being blocked, consider lowering your threshold score
- If you're still receiving spam, consider increasing your threshold score
- For persistent issues, review your reCAPTCHA configuration and ensure all keys are correctly entered

Remember that reCAPTCHA uses machine learning to improve over time, so its effectiveness may increase as it learns your site's traffic patterns.

## Troubleshooting & FAQs

| ![Question](/help/edge/docs/forms/universal-editor/assets/question.svg) | ![Answer](/help/edge/docs/forms/universal-editor/assets/answer.svg) |
|:-------------:|:-------------:|
| **What if I don't create a reCAPTCHA configuration?** | The system will look for a configuration in the Global Container. If none exists, you'll get an error. |
| **What if I create multiple configurations?** | The system automatically uses the first created configuration. |
| **Why aren't my changes visible on the published URL?** | Make sure you republish your form after making changes. |
| **Which reCAPTCHA services are supported?** | Edge Delivery Services Forms only supports score-based reCAPTCHA services. |

## Next steps

Now that you've protected your form with reCAPTCHA:

- **Validate your implementation**: Follow the [validation steps](#-validating-your-recaptcha-integration) to ensure reCAPTCHA is working correctly
- **Monitor performance**: Regularly check your Google reCAPTCHA dashboard for suspicious activities and score distributions
- **Fine-tune settings**: Adjust your threshold score based on your security needs and user experience feedback
- **Stay updated**: Keep your reCAPTCHA implementation current with Google's latest security recommendations
- **Educate your team**: Share knowledge about how reCAPTCHA works and how to interpret the analytics
- **Collect feedback**: Monitor user experience to ensure legitimate users aren't being blocked

Remember that effective form protection is an ongoing process that requires regular monitoring and adjustments.


