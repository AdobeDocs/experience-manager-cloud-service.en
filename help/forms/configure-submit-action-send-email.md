---
Title: How to send an email on submission of an Adaptive Form?
Description: Explore the process to set up email notifications when submitting an Adaptive Form.
keywords: how to send an email for an adpative form, Email Submit Action, Adaptive Form Email, Form Submission Email, Send Email Guide
feature: Adaptive Forms, Core Components
exl-id: 70386e57-345b-4edb-97f1-3fd52ea9ff4f
---
# Configure the Send Email submit action for an Adaptive Form

The **[!UICONTROL Send Email]** Submit Action enables you to send an email to one or more recipients upon successful submission of the form. This Submit Action enables you to create an email that can include form data in a predefined format. For instance, consider the following template where customer name, shipping address, state name, and ZIP code are retrieved from the submitted form data:


     ```
     Hi ${customer_Name},
 
     The following is set as your deafult shipping address:
     ${customer_Name},
     ${customer_Shipping_Address},
     ${customer_State},
     ${customer_ZIPCode}
 
     Regards,
     WKND 
 
     ```


## Advantages

Some advantages of configuring an Adaptive Form with Send Email submit action are:

* It enables quick communication as form data is directly sent to designated email reciepients.
* It helps in streamlining the workflow by directly integrating form submissions into email notifications.
* It helps organizations customize the email content, thus making it suitable for specific communication needs.

## Configure send email submit action {#steps-to-configure-send-email-submit-action}

To configure the Submit Action:

1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens. 
1. Click the  **[!UICONTROL Submission]** tab. 
1. From the **[!UICONTROL Submit Action]** drop-down list, select **[!UICONTROL Send email]**.

    ![Action configuration of Send Email](/help/forms/assets/send-email-action-configuration.gif)
1. Specify sender's email id in the **[!UICONTROL From]** textbox.
1. Add the email id of the recipient in the **[!UICONTROL To]** textbox. You can add multiple recipients by clicking the **[!UICONTROL Add]** button. 
1. [Optional] Add the recipient for CC and BCC by clicking the **[!UICONTROL Add]** button. 
1. Specify a subject line in the **[!UICONTROL Subject]** textbox.
1. Add an email template to configure send email submit action.
    * You can specify the path to the external email template saved in your AEM assets by using the **[!UICONTROL External Template Path]** option.
    * You can also add a custom email template for the form submission in the **[!UICONTROL Email Template]** textbox.
1. [Optional] The **[!UICONTROL Send Email]** Submit Action provides the option to include attachments and a [Document of Record (DoR)](generate-document-of-record-core-components.md) with the email. 
1. Click **[!UICONTROL Done]**.

## Best Practices {#best-practices}

* It is recommended to keep the email content clear and concise. Users should understand the purpose of the email and any actions they need to take.
* It is recommended for all form fields to have unique element names, even if they are placed on different panels within an Adaptive Form.
* When using AEM as a Cloud Service, outbound email requires encryption. By default, outbound email functionality is disabled. To activate it, submit a support ticket to [request access](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/development-guidelines.html?lang=en#sending-email). 


## Related Articles

{{af-submit-action}}
