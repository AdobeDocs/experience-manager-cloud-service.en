---
title: HTML Email Templates in Adaptive Forms on Forms as a Cloud Service
description: Learn to use email templates with Adaptive forms.
feature: Adaptive Forms, Core Components
role: User, Developer
hide: yes
hidefromtoc: yes
---
# Email Templates in Adaptive Forms 

Adaptive Forms allows you use HTML and plain-text email templates. HTML email templates enable you to send rich, personalized, and visually appealing emails when a form is submitted. These emails can be customized with form data and enhanced using various email tags, such as images and links. With Adaptive Forms, you can either upload a file containing an HTML template or use a plain-text editor to create these templates.

![HTML email templates](/help/forms/assets/html-email.png)

This article helps you configure and use email templates in Adaptive Forms. By the end, you will be able to:

* [Configure an HTML template for an adaptive form](#configure-an-html-template-for-an-adaptive-form)
* [Configure a plain text email template for an adaptive form](#configure-a-plain-text-template-for-an-adaptive-form)
* [Use forms data in your email templates](#use-form-data-in-your-email-templates)


Here is a quick overview of the steps involved:

1. Open the Adaptive Form for editing.
1. Configure the [Send Email](/help/forms/configure-submit-action-send-email.md) submit action.
1. Select or upload an HTML template, or manually enter the email template.
1. Test your email configuration.

## Configure an HTML template for an adaptive form

You can set up an Adaptive Form to send an email upon submission using the [**Send Email** submit action](/help/forms/configure-submit-action-send-email.md). The action provides two methods for configuring an HTML template:

### Option 1: Select a File Containing the HTML Template

Before proceeding, ensure that you have uploaded the HTML template to your AEM Forms environment.

1. Open the Adaptive Form for editing.
1. Go to the **Content Browser**, select the **Guide Container**, and tap the properties icon. A dialog box with title `Adaptive Form Container`  appears.
1. Go to the **Submission** tab and select the **Send Email** submit action.
1. Enable the **Use external template** option. 
1. Enable the **Use HTML template** option. 
1. Click the folder icon for the External Template Path option and browse to select your HTML template.
1. Click Done to save the configuration.

Your HTML template is now configured for the Adaptive Form.

### Option 2: Manually Enter or Paste an HTML Template

1. Open the Adaptive Form for editing.
1. Go to the **Content Browser**, select the **Guide Container**, and tap the properties icon. A dialog box with title `Adaptive Form Container`  appears.
1. Go to the **Submission** tab and select the **Send Email** submit action.
1. Enable the **Use external template** option. 
1. Enable the **Use HTML template** option. 
1. Type or paste your HTML code directly into the provided **Email Template** box.


## Configure a plain-text template for an adaptive form

You can set up an Adaptive Form to send an email upon submission using the [**Send Email** submit action](/help/forms/configure-submit-action-send-email.md). The action provides two methods for configuring a plain-text template:

### Option 1: Select a File Containing the Template

Before proceeding, ensure that you have uploaded the HTML template to your AEM Forms environment.

1. Open the Adaptive Form for editing.
1. Go to the **Content Browser**, select the **Guide Container**, and tap the properties icon. A dialog box with title `Adaptive Form Container`  appears.
1. Go to the **Submission** tab and select the **Send Email** submit action.
1. Enable the **Use external template** option. 
1. Click the folder icon for the **External Template Path** option and browse to select your plain-text template.
1. Click Done to save the configuration.

Your template is now configured for the Adaptive Form.

### Option 2: Manually Enter or Paste an HTML Template

1. Open the Adaptive Form for editing.
1. Go to the **Content Browser**, select the **Guide Container**, and tap the properties icon. A dialog box with title `Adaptive Form Container`  appears.
1. Go to the **Submission** tab and select the **Send Email** submit action.
1. Type or paste your plain-text template code directly into the provided **Email Template** box.

## Use Form Data in Your Email Templates

You can include form data in your email templates by using placeholders. These placeholders are dynamically replaced with actual form field values when the email is sent. For example:

* ${name}: The value of the field named "name."
* ${email}: The value of the field named "email."
* ${message}: The value of the field named "message."

### Sample HTML Email Template

Here's an example of an HTML email template that uses form data placeholders:

```HTML

    <!DOCTYPE html>
    <html>
    <head>
        <title>Form Submission</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
            }
            h2 {
                color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h2>Thank You for Your Submission</h2>
        <p>Dear ${name},</p>
        <p>We have received your submission with the following details:</p>
        <ul>
            <li><strong>Email:</strong> ${email}</li>
            <li><strong>Phone Number:</strong> ${phone_number}</li>
            <li><strong>Message:</strong> ${message}</li>
        </ul>
        <p>We will get back to you soon!</p>
        <p>Best regards,</p>
        <p>Your Team</p>
    </body>
    </html>

```

### Sample Plain-Text Email Template

Here's an example of a plain-text email template:

```TXT
    
    Subject: Thank You for Your Submission
    
    Dear ${name},
    
    We have received your submission with the following details:
    
    - Email: ${email}
    - Phone Number: ${phone_number}
    - Message: ${message}
    
    We will get back to you soon!
    
    Best regards,
    Your Team

```

Replace the placeholders (${name}, ${email}, etc.) with the corresponding form field names in your Adaptive Form.

## Best Practices for HTML Email Templates

* Ensure your styles are inline for better compatibility with email clients.
* Make your template responsive for a better experience on mobile devices.
* Use tools like Litmus or Email on Acid to preview your email across various email clients.
* Ensure the placeholder names match the form field names exactly.
* Check for missing or incorrect tags in your HTML template.
* Verify that the [Send Email](/help/forms/configure-submit-action-send-email.md) submit action is correctly configured.
