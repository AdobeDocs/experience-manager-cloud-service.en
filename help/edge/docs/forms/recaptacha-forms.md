---
title: Use reCAPTCHA with Edge Delivery Services for AEM Forms as a Cloud Service
description: Use Google reCAPTCHA in an form for Edge Delivery Services for AEM Forms 
feature: Edge Delivery Services
exl-id: ac104e23-f175-435f-8414-19847efa5825
role: Admin, Architect, Developer
---

# Use reCAPTCHA with Edge Delivery Services for AEM Forms as a Cloud Service

<span>The **reCAPTCHA** feature is under the pre-release program. To request access to the **reCAPTCHA** feature for Edge Delivery Services for AEM Forms, send an email from your work address to mailto:aem-forms-ea@adobe.com.</span>

reCAPTCHA is a popular tool used to protect websites from fraudulent activities, spam, and misuse. In Edge Delivery Services, the Adaptive Forms Block provides the capability to add Google reCAPTCHA to distinguish between humans and bots. This feature allows users to protect their website from spam and misuse. 
For example, consider an enquiry form that collects data such as start and end trip dates, room budget, estimated trip cost, and traveler information. In such cases, there is a risk of malicious users exploiting the form for purposes like sending phishing emails or flooding it with irrelevant or harmful content using spambots. Integrating reCAPTCHA offers added security by verifying that submissions are from genuine users, effectively minimizing spam entries.

<!-- ![Recaptcha Image](/help/edge/docs/forms/assets/recaptcha-image.png){width="300" align="center"} -->

Edge Delivery Services only supports the **Score based(v3)-reCAPTCHA** for the Adaptive Form Block.

![Recaptcha V2](/help/forms/assets/recaptcha-v2-invisible.png){width="300" align="center"}


By the end of this article, you learn to:
  * [Enable Google reCAPTCHA for a single form](#enable-google-recaptchas-for-a-single-form)
  * [Enable reCAPTCHA for all the forms on your Site](#enable-recaptcha-for-all-the-forms)

## Pre-requisites

* Begin the development of Edge Delivery Services Forms by following the steps explained in [Create a form using Adaptive Forms Block](/help/edge/docs/forms/create-forms.md). 
* Register your domain with [Google reCAPTCHA and obtain credentials](https://www.google.com/recaptcha/admin/create).

## Enable Google reCAPTCHA for a single form {#enable-google-recaptchas-for-a-single-form}

Enabling Google reCAPTCHA for a single form involves integrating Google's reCAPTCHA service into a specific web form to prevent automated abuse or spam submissions.

To enable Google reCAPTCHA for a single form:
1. [Configure the reCAPTCHA secret key in the project configuration file](#configure-secret-key)
1. [Add the reCAPTCHA site key to your form](#add-site-key)

To start configuring reCaptcha in Edge Delivery Services Forms, refer to the following [spreadsheet](/help/edge/docs/forms/assets/recaptcha.xlsx) that includes the form definition for a form.

### Configure the reCAPTCHA secret key in the project configuration file {#configure-secret-key}

The Site Secret for domain registered with Google reCAPTCHA is added to project the configuration file (`.helix/config`) in your AEM Project folder at Microsoft SharePoint or Google Drive. To add the Site Secret to the config file:

1. Go to your AEM Project folder on Microsoft&reg; SharePoint or Google Drive. 
1. Create the `.helix/config.xlsx` file in your AEM Project folder in Microsoft SharePoint Site or the `.helix/config` file in AEM Project folder within your Google Drive. 

    >[!NOTE]
    >
    > The [project configuration file](https://www.aem.live/docs/configuration) is a spreadsheet located at `/.helix/config`. If the file does not exist, create it.

1. Open the `config` file and add the following key and value pairs:

    * **captcha.secret**: Google reCAPTCHA secret key value
    * **captcha.type**: reCAPTCHA v2

    >[!NOTE]
    >
    >  * You can retrieve the reCAPTCHA keys from the [Google reCAPTCHA Admin Console](https://www.google.com/recaptcha/admin).
    >  *  You must specify the value of **captcha.type** in the `config` file as **reCAPTCHA v2**.

   Refer to the screenshot of a project configuration file below:

    ![Project configuration file](/help/forms/assets/recaptcha-config-file.png)

1. Save the `config` file.

1. Preview and publish the `config` file using [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content). 

### Add reCAPTCHA site key to your form {#add-site-key}

The Site Key for a domain registered with Google reCAPTCHA is added to the spreadsheet of the form that is to be protected. To add the Site key to a form:

1. Go to your AEM Project folder on Microsoft&reg; SharePoint or Google Drive and open your spreadsheet. You can also create new spreadsheet for a form.
1. Insert a row into the spreadsheet to add new field as CAPTCHA, including the following details:
    * **type**: captcha
    * **value**: Google reCAPTCHA site key value
  
    Refer to the screenshot below, depicting the spreadsheet with the new row type as CAPTCHA:
  
   ![Recaptcha spreadsheet](/help/edge/docs/forms/assets/recaptcha-spreadsheet.png)
   
    >[!NOTE]
    >
    >  You can retrieve the reCAPTCHA keys from the [Google reCAPTCHA Admin Console](https://www.google.com/recaptcha/admin).

1. Save the spreadsheet.
1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview and publish the sheet. 

After adding new row in the form definition, a reCAPTCHA badge appears at the bottom-right corner of the form. This ensures that the form is now protected from fraudulent activities, spam, and misuse.

![recaptcha-form](/help/edge/docs/forms/assets/recaptcha-form.png)

## Enable reCAPTCHA for all the forms on your Site{#enable-recaptcha-for-all-the-forms}

To apply Google reCAPTCHA to all the forms on your Site that use Adaptive Forms Block, skip the previous steps and directly embed the `sitekey` value into the `recaptcha.js` file. To include site key value in the `recaptcha.js` file:

1. [Update the Google reCAPTCHA Site Key in the recaptcha.js file](#1-update-google-recaptcha-site-key-in-recaptchajs-file)
1. [Deploy the file and build the project](#2-deploy-the-file-and-build-the-project)
1. [Preview the Site using the AEM sidekick](#3-preview-the-site-using-the-aem-sidekick)

### Update Google reCAPTCHA Site Key in recaptcha.js File

1. Open the corresponding GitHub repository on your local machine. 
1. Navigate to `[../Form Block/integrations]` folder and open the `recaptcha.js` file.
1. Replace the `siteKey` with Google reCAPTCHA Site key value.

    ![Recaptcha apply to all forms](/help/forms/assets/recaptcha-apply-to-all-forms.png)

    >[!NOTE]
    >
    >  You can retrieve the reCAPTCHA keys from the [Google reCAPTCHA Admin Console](https://www.google.com/recaptcha/admin).

1. Save the `recaptcha.js` file.

### Deploy the file and build the project

Deploy the updated `recaptcha.js` file to your GitHub project and verify a successful build.

### Preview the Site using the AEM sidekick

Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview and publish the site. 

The reCAPTCHA badge starts appearing for all the forms on your Site. 

## See also

{{see-more-forms-eds}}

