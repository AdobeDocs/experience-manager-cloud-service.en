---
description: Configure Submit Actions for an Adaptive Form.
title: Submit Actions
feature: Edge Delivery Services
role: Admin, Architect, Developer
---
# Adaptive Form Submit Action (Universal **Editor)

A Submit Action specifies the destination for the data collected through an Adaptive Form. The submission process begins when the user clicks the **[!UICONTROL Submit]** button on the form. AEM Forms offers two types of submit actions described below, and lets you create and use custom submit actions to meet your specific needs.

{width=50%,height=50%}![Adaptive Form Properties](/help/forms/assets/properties-un-ed.png)

To define a Submit Action for an Adaptive Form, you use the Properties dialog of the **Adaptive Form block** in the **Editor**. The out-of-the-box submit actions are:

* [Submit to REST endpoint](#rest-endpoint-submission-ue)
* [Send Email](#email-submission-ue)

### Submit to REST endpoint {#rest-endpoint-submission-ue}

Submit to REST Endpoint action is used to send the submitted form data to a specified REST URL. This URL can belong to either an internal server where the form is hosted or to an external server. Configuring the Submit Action to REST Endpoint for Adaptive Forms offers several benefits such as:  

* Facilitates seamless integration of form data with external systems and services via RESTful APIs.  
* Offers flexibility in managing data submissions from Adaptive Forms, accommodating dynamic and complex data structures.  
* Allows dynamic mapping of form fields to parameters within the REST endpoint URL, enabling adaptable and customizable data submissions.

{width=50%,height=50%}![Adaptive Form properties in Universal **Editor](/help/forms/assets/submit-actions-ue.png)

To configure a REST endpoint:

1. Open your Adaptive Form in *Editor.
1. Select **[!UICONTROL Adaptive Form Block]**. 
1. Click the properties ![properties](/help/forms/assets/Smock_Properties_18_N.svg) icon.
1. From the **[!UICONTROL Submit Action]** drop-down list, Select the **[!UICONTROL Submit to a REST endpoint]**.
1. Specify the REST endpoint URL.

    {width=50%,height=50%}![Enable post request for adaptive forms](/help/forms/assets/enable-post-request-ue.png)

To post data to an internal server, provide the path of the resource. The data is posted to the path of the resource. For example, `/content/restEndPoint`. For such post requests, the authentication information of the submit request is used.

To post data to an external server, provide a URL. The format of the URL is `https://host:port/path_to_rest_end_point`. Ensure that you configure the path to handle the POST request anonymously.

You can also **Enable POST request** and provide a URL to post the request. To submit data to the AEM server hosting the form, use a relative path corresponding to the root path of the AEM server. For example, `/content/forms/af/SampleForm.html`. To submit data to any other server, use the absolute path.

### Send Email {#email-submission-ue}

Send Email Submit Action allows you to send an email to one or more recipients upon successful submission of the form. Send Email configuration helps you to create an email that can include form data in a predefined format. For instance, consider the following template where customer name, shipping address, state name, and ZIP code are retrieved from the submitted form data. Some advantages of configuring an Adaptive Form with Send Email submit action are:

1. Enables quick communication as form data is directly sent to designated email recipients.
1. Helps in streamlining the workflow by directly integrating form submissions into email notifications.
1. Helps organizations customize the email content, thus making it suitable for specific communication needs.

To configure submit action as an Email for your form submission:

1. Open your Adaptive Form in **Editor.
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
        * **Use External Template**: Enables the use of an external email template for formatting the email content. Provide the URL or path to the External template path to integrate a pre-designed email template hosted in your AEM Assets folder.
        * **Include Attachment**: Specifies whether the submitted form data should include an attachment submitted through the form in the email. Supported attachment formats are PDF, XML and JSON.

    {width=50%,height=50%}![Enable post request for adaptive forms](/help/forms/assets/email-config-ue.png)

## Show a custom thank you message on Adaptive Form submission {#submit-action-message-ue}

On Submit option helps you to configure a Submit Action message on Adaptive Form submission, To configure a Submit Action message for your form:

1. Open your Adaptive Form in **Editor.
1. Select your **[!UICONTROL Adaptive Form Block]**. 
1. Click the properties ![properties](/help/forms/assets/Smock_Properties_18_N.svg) icon. 
1. On click, you see the following option:
    * **[!UICONTROL On Submit]**: On Submit helps you to customize a message to be shown when a form is submitted. By default, a custom message "Thank you for submitting the form" is displayed to the user when a form is successfully submitted. 
    You can also customize the Thank You message on form submission, by selecting the option to **[!UICONTROL Show message]**, and add/edit your message in the Rich Text **Editor.