---
description: Send your Adaptive Form created in Universal Editor to multiple submit actions such as Email, REST endpoint and more.
title: Submit Actions
feature: Edge Delivery Services
role: Admin, Architect, Developer
---
# Adaptive Form Submit Action (Universal Editor)

A Submit Action enables you to specify where the data collected from an Adaptive Form should be sent. It is triggered when the user clicks the **[!UICONTROL Submit]** button on the form. The Universal Editor supports the creation of forms and provides pre-configured [submit actions](#configure-submit-action-ue). These ready-to-use Submit Actions allow you to:

* Conveniently submit the data to a REST endpoint.
* Effortlessly send form data via email.

 {width=50%,height=50%}![Adaptive Form properties in Universal Editor](/help/forms/assets/submit-actions-ue.png)


To define a Submit Action for an Adaptive Form, you use the Properties dialog of the **Adaptive Form block** in the Universal Editor. The Properties dialog of the **Adaptive Form Block** component includes:

* [On Submit](#submit-action-message-ue)
* [Submit Action](#configure-submit-action-ue)

## Configure Submit Action message on Adaptive Form submission {#submit-action-message-ue}

On Submit option helps you to configure Submit Action message on Adaptive Form submission, To configure a Submit Action message for your form:

1. Open your Universal Editor Content browser.
1. Select your **[!UICONTROL Adaptive Form Block]**. 
1. Click the properties ![properties](/help/forms/assets/Smock_Properties_18_N.svg) icon. 
1. On clicking, you see the following options:
    * **[!UICONTROL On Submit]**: On Submit helps you to customize a message to be shown when a form is submitted. By default, a custom message "Thank you for submitting the form" is displayed to the user when a form is successfully submitted. You can also customize your form submission message by selecting the option to **[!UICONTROL Show message]**, and add/edit your message in the Rich Text Editor.

## Configure Submit Actions for Adaptive Form submission {#configure-submit-action-ue}

To configure submit actions type, follow the steps given below:

1. Open your Universal Editor Content browser. 
1. Select your **[!UICONTROL Adaptive Form Block]**. 
1. Click the properties ![properties](/help/forms/assets/Smock_Properties_18_N.svg) icon. 
1. On clicking, you find the **[!UICONTROL Submit Action]** drop-down list, where you select the submit actions type to send the form via an Email or a REST endpoint, described in the next sections.

* [Submit to REST endpoint](#rest-endpoint-submission-ue)
* [Send Email](#email-submission-ue)

### Configure REST endpoint for Adaptive Form submission {#rest-endpoint-submission-ue}

Submit to REST Endpoint action is used to send the submitted form data to a specified REST URL. This URL can belong to either an internal server (where the form is hosted) or an external server. Configuring the Submit to REST Endpoint action for Adaptive Forms offers several benefits:  

* It facilitates seamless integration of form data with external systems and services via RESTful APIs.  
* It offers flexibility in managing data submissions from Adaptive Forms, accommodating dynamic and complex data structures.  
* It allows dynamic mapping of form fields to parameters within the REST endpoint URL, enabling adaptable and customizable data submissions.  

To configure a REST endpoint:

1. Open your Universal Editor Content browser.
1. Select your **[!UICONTROL Adaptive Form Block]**. 
1. Click the properties ![properties](/help/forms/assets/Smock_Properties_18_N.svg) icon.
1. From the **[!UICONTROL Submit Action]** drop-down list, Select the **[!UICONTROL Submit to a REST endpoint]**.
1. Specify the REST endpoint URL.

    {width=50%,height=50%}![Enable post request for adaptive forms](/help/forms/assets/enable-post-request-ue.png)

To post data to an internal server, provide the path of the resource. The data is posted to the path of the resource. For example, `/content/restEndPoint`. For such post requests, the authentication information of the submit request is used.

To post data to an external server, provide a URL. The format of the URL is `https://host:port/path_to_rest_end_point`. Ensure that you configure the path to handle the POST request anonymously.

You can also **Enable POST request** and provide a URL to post the request. To submit data to the AEM server hosting the form, use a relative path corresponding to the root path of the AEM server. For example, `/content/forms/af/SampleForm.html`. To submit data to any other server, use the absolute path.

### Configure Email configuration for Adaptive Form submission {#email-submission-ue}

Send Email Submit Action enables you to send an email to one or more recipients upon successful submission of the form. It helps you to create an email that can include form data in a predefined format. For instance, consider the following template where customer name, shipping address, state name, and ZIP code are retrieved from the submitted form data. Some advantages of configuring an Adaptive Form with Send Email submit action are:

1. It enables quick communication as form data is directly sent to designated email recipients.
1. It helps in streamlining the workflow by directly integrating form submissions into email notifications.
1. It helps organizations customize the email content, thus making it suitable for specific communication needs.

To configure submit action as an Email for your form submission:

1. Open your Universal Editor Content browser.
1. Select your **[!UICONTROL Adaptive Form Block]**. 
1. Click the properties ![properties](/help/forms/assets/Smock_Properties_18_N.svg) icon.
1. From the **[!UICONTROL Submit Action]** drop-down list, select **[!UICONTROL Send email]**.  
1. Once you select the send email option, you can configure the following properties:
    * **Email Configuration** The "Email Configuration" section defines how the email is sent, including sender details, recipients, and additional parameters. Below are the key fields:
        * **From**: The email address of the sender.
        * **To**: Specify the primary recipients of the email, multiple email addresses can be added, separated by commas.
        * **CC**: Specify the recipients who should receive a carbon copy (CC) of the email.
        * **BCC**: Specify the recipients who should receive a blind carbon copy (BCC) of the email.
        * **Subject**: Specify the subject line of the email.
        * **Use External Template**: Enables the use of an external email template for formatting the email content. Provide the URL or path to the External template path to integrate a pre-designed email template hosted in your AEM assets folder.
        * **Include Attachment**: Specifies whether the submitted form data should include an attachment submitted through the form in the email. Supported attachment formats are PDF, XML and JSON.

    {width=50%,height=50%}![Enable post request for adaptive forms](/help/forms/assets/email-config-ue.png)