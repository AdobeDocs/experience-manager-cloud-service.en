---
title: Use reCAPTCHA with Edge Delivery Services for AEM Forms as a Cloud Service
description: Use Google reCAPTCHA in an form for Edge Delivery Services for AEM Forms
feature: Edge Delivery Services
exl-id: ac104e23-f175-435f-8414-19847efa5825
role: Admin, Developer
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
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---

# Use reCAPTCHA with Edge Delivery Services for AEM Forms as a Cloud Service

<!--
<span>The **reCAPTCHA** feature is under the pre-release program. To request access to the **reCAPTCHA** feature for Edge Delivery Services for AEM Forms, send an email from your work address to mailto:aem-forms-ea@adobe.com.</span>
-->

reCAPTCHA is a popular tool used to protect websites from fraudulent activities, spam, and misuse. In Edge Delivery Services, the Adaptive Forms Block provides the capability to add Google reCAPTCHA to distinguish between humans and bots. This feature allows users to protect their website from spam and misuse. 
For example, consider an enquiry form that collects data such as start and end trip dates, room budget, estimated trip cost, and traveler information. In such cases, there is a risk of malicious users exploiting the form for purposes like sending phishing emails or flooding it with irrelevant or harmful content using spambots. Integrating reCAPTCHA offers added security by verifying that submissions are from genuine users, effectively minimizing spam entries.

<!-- ![Recaptcha Image](/help/edge/docs/forms/assets/recaptcha-image.png){width="300" align="center"} -->

Edge Delivery Services Forms supports only **reCAPTCHA Enterprise with score-based site keys** for the Adaptive Forms Block.

By the end of this article, you learn to:

- [Enable Google reCAPTCHA for a single form](#enable-google-recaptchas-for-a-single-form)
- [Enable reCAPTCHA for all the forms on your Site](#enable-recaptcha-for-all-the-forms)

## Pre-requisites

- Begin the development of Edge Delivery Services Forms by following the steps explained in [Create a form using Adaptive Forms Block](/help/edge/docs/forms/create-forms.md). 
- Create a reCAPTCHA Enterprise score-based site key for your form's domain. Follow the [Google Cloud project and key-creation instructions](/help/forms/captcha-adaptive-forms-core-components.md#steps-to-implement-reCAPTCHA-enterprise-in-forms-core-components), and keep **Will you use challenges?** turned off.

## Enable Google reCAPTCHA for a single form {#enable-google-recaptchas-for-a-single-form}

Enabling Google reCAPTCHA for a single form involves integrating Google's reCAPTCHA service into a specific web form to prevent automated abuse or spam submissions.

To enable reCAPTCHA Enterprise for a single form, [add the score-based site key to your form](#add-site-key).

The following [spreadsheet](/help/edge/docs/forms/assets/recaptcha.xlsx) includes an example form definition. Replace its sample site key with your own reCAPTCHA Enterprise score-based site key.

### Add reCAPTCHA site key to your form {#add-site-key}

Add the reCAPTCHA Enterprise score-based site key to the spreadsheet of the form that is to be protected:

1. Go to your AEM Project folder on Microsoft&reg; SharePoint or Google Drive and open your spreadsheet. You can also create new spreadsheet for a form.
1. Insert a row into the spreadsheet to add new field as CAPTCHA, including the following details:
    - **type**: captcha
    - **value**: Your reCAPTCHA Enterprise score-based site key
  
    Refer to the screenshot below, depicting the spreadsheet with the new row type as CAPTCHA:
  
   ![Recaptcha spreadsheet](/help/edge/docs/forms/assets/recaptcha-spreadsheet.png)
   
    >[!NOTE]
    >
    >  Copy the site key from **Security > Fraud Defense > Keys** in the [Google Cloud Console](https://console.cloud.google.com/).

1. Save the spreadsheet.
1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview and publish the sheet. 

After adding new row in the form definition, a reCAPTCHA badge appears at the bottom-right corner of the form. This ensures that the form is now protected from fraudulent activities, spam, and misuse.

![recaptcha-form](/help/edge/docs/forms/assets/recaptcha-form.png)

## Enable reCAPTCHA for all the forms on your Site{#enable-recaptcha-for-all-the-forms}

To apply reCAPTCHA Enterprise to all the forms on your Site that use Adaptive Forms Block, use your Enterprise score-based site key in the `recaptcha.js` file. To include the site key value in the `recaptcha.js` file:

1. [Update the Google reCAPTCHA Site Key in the recaptcha.js file](#1-update-google-recaptcha-site-key-in-recaptchajs-file)
1. [Deploy the file and build the project](#2-deploy-the-file-and-build-the-project)
1. [Preview the Site using the AEM sidekick](#3-preview-the-site-using-the-aem-sidekick)

### Update Google reCAPTCHA Site Key in recaptcha.js File

1. Open the corresponding GitHub repository on your local machine. 
1. Navigate to `[../Form Block/integrations]` folder and open the `recaptcha.js` file.
1. Replace the `siteKey` with your reCAPTCHA Enterprise score-based site key.

    ![Recaptcha apply to all forms](/help/forms/assets/recaptcha-apply-to-all-forms.png)

    >[!NOTE]
    >
    >  Copy the site key from **Security > Fraud Defense > Keys** in the [Google Cloud Console](https://console.cloud.google.com/).

1. Save the `recaptcha.js` file.

### Deploy the file and build the project

Deploy the updated `recaptcha.js` file to your GitHub project and verify a successful build.

### Preview the Site using the AEM sidekick

Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview and publish the site. 

The reCAPTCHA badge starts appearing for all the forms on your Site. 
