---
title: Submit Actions
description: Configure Submit Actions for Adaptive Form.
feature: Edge Delivery Services
role: Admin, Architect, Developer
exl-id: beee9be7-8215-496b-9fb9-61fba000a055
hide: yes
hidefromToC: yes
---
# Adaptive Form Submit Action

## Overview

Form submission is the critical final step in the user journey—it's where collected data is processed and actions are taken. This document provides a comprehensive guide to configuring and managing submit actions for Adaptive Forms in Universal Editor.

### What You'll Learn

By the end of this document, you'll understand how to:

* Configure different types of submit actions for your forms
* Set up REST endpoint submissions for integration with external systems
* Configure email submissions for form responses
* Implement custom submit actions for specific business needs
* Handle form validation and error scenarios during submission

### Target Audience

This guide is designed for:

* **Form developers** implementing submission logic
* **System integrators** connecting forms to backend systems
* **Business analysts** defining form workflows
* **Technical architects** designing form submission processes

### Available Submit Actions

Universal Editor provides two primary submit action types:

1. **Submit to REST endpoint** * Send form data to API endpoints
2. **Send Email** * Deliver form responses via email

### Prerequisites

Before configuring submit actions, ensure you have:

* Access to Universal Editor
* Proper permissions for form configuration
* Understanding of your target submission endpoint or email configuration

A Submit Action specifies the destination for the data collected through an Adaptive Form. The submission process begins when the user clicks the **[!UICONTROL Submit]** button on the form. AEM Forms offers two types of submit actions described below, and lets you create and use custom submit actions to meet your specific needs. The out-of-the-box submit actions are:

<!--To define a Submit Action for an Adaptive Form, you use the Properties dialog of the **Adaptive Form block** in the **Editor**-->

* [Submit to REST endpoint](#rest-endpoint-submission-ue)
* [Send Email](#email-submission-ue)


### Submit to REST endpoint {#rest-endpoint-submission-ue}

Submit to REST Endpoint action is used to send the submitted form data to a specified REST endpoint. The endpoint can belong to either an internal server where the form is hosted or to an external server by using a relative path or an absolute path. To submit data to the AEM server hosting the form, use a relative path corresponding to the root path of the AEM server. For example, `/content/forms/af/SampleForm.html`. To submit data to any other server, use the absolute path.

<!--Configuring the Submit Action to REST Endpoint for Adaptive Forms offers several benefits such as:  
* It facilitates seamless integration of form data with external systems and services via RESTful APIs.  
* Offers flexibility in managing data submissions from Adaptive Forms, accommodating dynamic and complex data structures.  
* Allows dynamic mapping of form fields to parameters within the REST endpoint URL, enabling adaptable and customizable data submissions.
-->



To configure a REST endpoint:

1. Open your Adaptive Form in **[!UICONTROL Editor]**.
1. Select **[!UICONTROL Adaptive Form Block]**. 
1. Click the properties ![properties](/help/forms/assets/Smock_Properties_18_N.svg) icon.
1. Select the **[!UICONTROL Submit to a REST endpoint]** from the **[!UICONTROL Submit Action]** drop-down list.
1. Specify the REST endpoint URL.
1. You can also **Enable POST request** and provide a URL to post the request. 

![Screenshot of the Universal Editor properties panel showing the REST endpoint configuration fields including URL input and Enable POST request toggle for form submission](/help/forms/assets/enable-post-request-ue.png)

  >[!NOTE]
  >
  > * To post data to an internal server, provide the path of the resource. The data is posted to the path of the resource. For example, `/content/restEndPoint`. For such post requests, the authentication information of the submit request is used.
  > * To post data to an external server, provide a URL. The format of the URL is `https://host:port/path_to_rest_end_point`. Ensure that you configure the path to handle the POST request anonymously. 

### Send Email {#email-submission-ue}

Send Email Submit Action allows you to send an email to one or more recipients upon successful submission of the form. Send Email configuration helps you to create an email that can include form data in a predefined format. For example, consider the following template where customer name, shipping address, state name, and ZIP code are retrieved from the submitted form data. [Learn more about Email Templates in Adaptive Forms](/help/forms/html-email-templates-in-adaptive-forms.md). Some advantages of configuring an Adaptive Form with Send Email submit action are:

1. It enables quick communication as form data is directly sent to designated email recipients.
1. It helps in streamlining the workflow by directly integrating form submissions into email notifications.
1. It helps organizations customize the email content, thus making it suitable for specific communication needs.

![Adaptive Form properties in Universal Editor](/help/forms/assets/submit-actions-ue.png)


To configure a submit action as an Email for your form submission:

1. Open your Adaptive Form in **Editor**.
1. Select your **[!UICONTROL Adaptive Form Block]**. 
1. Click the properties ![properties](/help/forms/assets/Smock_Properties_18_N.svg) icon.
1. Select the **[!UICONTROL Send email]** option from the **[!UICONTROL Submit Action]** drop-down list. 
1. Once you select the send email option, you can configure the following properties as shown in the image below.
        
<table>
  <thead>
    <tr>
      <th>Image</th>
      <th>Property</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
    <td rowspan="7"><img src="/help/forms/assets/email-config-ue.png" alt="Email Configuration"></td> 
    <td><b>From</td>
    <td>Specify the email address of the sender.</td>
    </tr>
    <tr>
      <td><b>To</td>
      <td>Specify the primary recipients of the email, multiple email addresses can be added, separated by commas.</td>
    </tr>
    <tr>
      <td><b>CC</td>
      <td>Specify the recipients who should receive a carbon copy (CC) of the email.</td>
    </tr>
    <tr>
      <td><b>BCC</td>
      <td>Specify the recipients who should receive a blind carbon copy (BCC) of the email.</td>
    </tr>
    <tr>
      <td><b>Subject</td>
      <td>Specify the subject line of the email.</td>
    </tr>
    <tr>
      <td><b>Use External Template</td>
      <td>Enables the use of an external email template for formatting the email content. Provide the URL or path to the external template to integrate a pre-designed email template hosted in your AEM Assets folder.</td>
    </tr>
    <tr>
      <td><b>Include Attachment</td>
      <td>Specifies whether the submitted form data should include an attachment submitted through the form in the email. Supported attachment formats are PDF, XML, and JSON.</td>
    </tr>
  </tbody>
</table>






<!--
        
        * **From**: The email address of the sender.
        * **To**: Specify the primary recipients of the email, multiple email addresses can be added, separated by commas.
        * **CC**: Specify the recipients who should receive a carbon copy (CC) of the email.
        * **BCC**: Specify the recipients who should receive a blind carbon copy (BCC) of the email.
        * **Subject**: Specify the subject line of the email.
        * **Use External Template**: Enables the use of an external email template for formatting the email content. Provide the URL or path to the External template path to integrate a pre-designed email template hosted in your AEM Assets folder.
        * **Include Attachment**: Specifies whether the submitted form data should include an attachment submitted through the form in the email.

    ![Screenshot of the Universal Editor email configuration panel showing fields for From, To, CC, BCC, Subject, and options for external templates and attachments](/help/forms/assets/email-config-ue.png)

-->

## Show a custom thank you message on Adaptive Form submission {#submit-action-message-ue}

On Submit option helps you to configure a Submit Action message on Adaptive Form submission, To configure a Submit Action message for your form:

1. Open your Adaptive Form in **Editor**.
1. Select your **[!UICONTROL Adaptive Form Block]**. 
1. Click the properties ![properties](/help/forms/assets/Smock_Properties_18_N.svg) icon. 
1. On click, you see the following option:
    * **[!UICONTROL On Submit]**: On Submit helps you to customize a message to be shown when a form is submitted. By default, a custom message "Thank you for submitting the form" is displayed to the user when a form is successfully submitted. 
    You can also customize the Thank You message on form submission, by selecting the option to **[!UICONTROL Show message]**, and add/edit your message in the Rich Text **Editor**.


## See also

{{universal-editor-see-also}}

