---
title: Use reCAPTCHA with AEM Forms Edge Delivery Services
description: Use Google reCAPTCHA in an EDS Form
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
exl-id: ac104e23-f175-435f-8414-19847efa5825
---
# Use reCAPTCHA with AEM Forms Edge Delivery Services

reCAPTCHA is a popular tool used to protect websites from fraudulent activities, spam, and misuse. In Edge Delivery Services, the Adaptive Forms Block provides the capability to add Google reCAPTCHA to distinguish between humans and bots. This feature allows users to protect their website from spam and misuse. 
For example, consider an enquiry form that collects data such as start and end trip dates, room budget, estimated trip cost, and traveler information. In such cases, there is a risk of malicious users exploiting the form for purposes like sending phishing emails or flooding it with irrelevant or harmful content using spambots. Integrating reCAPTCHA offers added security by verifying that submissions are from genuine users, effectively minimizing spam entries.

By the end of this article, you learn to:

* [Configure the secret key in project configuration file](#configure-secret-key)
* [Add site key in the form definition](#add-site-key)


## Pre-requisite

Configure [Google reCAPTCHA secret and site keys](https://www.google.com/recaptcha/admin/create).

>[!NOTE]
>
> Edge Delivery Services only support the **Challenge (v2): Invisible reCAPTCHA badge** for the Form Block.

## Configure the reCAPTCHA secret key in project configuration file {#configure-secret-key}

After configuring the Google reCAPTCHA secret and site keys, proceed to modify the project configuration file to enable the use of reCAPTCHA in a form: 

1. Go to your Edge Deliver project folder on Microsoft® SharePoint or Google Workspace. 
1. Create the `.helix/config.xlsx` file in your SharePoint site or the `.helix/config` file within your Google Workspace. 

    >[!NOTE]
    >
    > The project configuration file is a spreadsheet located at `/.helix/config`. In case the file does not exist, create it with the same name.

2. Open the `config` file and add the following key and value pairs:

    * **captcha.secret**: Google reCAPTCHA secret key value
    * **captcha.type**: reCAPTCHA v2
  
   Refer to the image for an illustration of a project configuration file:

    ![Project configuration file](/help/forms/assets/recaptcha-config-file.png)

    >[!NOTE]
    >
    >  You can retrieve the reCAPTCHA keys from the [Google reCAPTCHA Admin Console](https://www.google.com/recaptcha/admin).

3.  Make sure to preview and publish the `config` file using [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content). 

 ## Add reCAPTCHA site key in the form definition{#add-site-key}

In the form definition, users are required to insert a row in a spreadsheet to incorporate new field as CAPTCHA, along with its corresponding value. To add new field as CAPTCHA in a spreadsheet:

1. Go to your Edge Deliver project folder on Microsoft® SharePoint or Google Workspace and open your spreadsheet. You can also [create new spreadsheet for a form](/help/forms/create-forms.md).
1. Insert a row into the spreadsheet to add new field as CAPTCHA, including the following details:
    * **type**: captcha
    * **value**: Google reCAPTCHA site key value
  
    Refer to the illustration below, depicting the spreadsheet with the new row type as CAPTCHA:
  
   ![Recaptcha spreadsheet](/help/forms/assets/recaptcha-spreadsheet.png)

   
    >[!NOTE]
    >
    >  You can retrieve the reCAPTCHA keys from the [Google reCAPTCHA Admin Console](https://www.google.com/recaptcha/admin).

2. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview and publish the sheet. 
You can refer to the [spreadsheet](/help/forms/assets/recaptcha-enquiry.xlsx) that includes the form definition for an enquiry form.

After adding new row in the form definition, a reCAPTCHA badge appears at the bottom-right corner of the form. This ensures that the form is now protected from fraudulent activities, spam, and misuse.

Refer to the image below, which showcases the form with the reCAPTCHA badge:

![recaptcha-form](/help/forms/assets/recaptcha-form.png)

## Extra Byte {#extra-byte}

To apply Google reCAPTCHA to all forms, skip the previous steps and directly embed the `sitekey` value into the `recaptcha.js` file. To include site key value in the `recaptcha.js` file:

1. Open the corresponding GitHub repository on your local machine. 
1. Navigate to `../blocks/form/integrations/recaptcha.js` file.
1. Replace the `siteKey` with Google reCAPTCHA site key value.

![Recaptcha apply to all forms](/help/forms/assets/recaptcha-apply-to-all-forms.png)

>[!NOTE]
>
>  You can retrieve the reCAPTCHA keys from the [Google reCAPTCHA Admin Console](https://www.google.com/recaptcha/admin).

The reCAPTCHA badge starts appearing for all the Edge Delivery Services forms. 

