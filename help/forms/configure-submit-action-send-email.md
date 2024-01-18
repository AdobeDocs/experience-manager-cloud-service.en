---
Title: How to send an email on submission of an Adaptive Form?
Description: Explore the process to set up email notifications when submitting an Adaptive Form.
keywords: how to send an email for an adpative form, Email Submit Action, Adaptive Form Email, Form Submission Email, Send Email Guide
feature: Adaptive Forms, Core Components
---

# Configure the Send Email submit action for an Adaptive Form

The **[!UICONTROL Send Email]** Submit Action enables you to create an email. To send an email to one or more recipients upon successful submission of the form, you can utilize the Send Email Submit Action. This action enables you to create an email that includes form data in a predefined format. For instance, consider the following template where customer name, shipping address, state name, and ZIP code are retrieved from the submitted form data:


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

> [!NOTE]
>
> * It is crucial for all form fields to have unique element names, even if they are placed on different panels within an Adaptive Form.
> * When using AEM as a Cloud Service, outbound email requires encryption. By default, outbound email functionality is disabled. To activate it, submit a support ticket to Request Access.

AEM as a Cloud Service offers various out of the box submit actions for handling form submissions. You can learn more about these options in the [Adaptive Form Submit Action](/help/forms/configure-submit-actions-core-components.md) article.

## Advantages

Here are advantages of configuring an Adaptive Form with Send Email submit action:

* It enables quick communication as form data is directly sent to designated email reciepients.
* It helps in streamlining the workflow by directly integrating form submissions into email notifications.
* It helps organizations customize the email content, thus making it suitable for specific communication needs.

## Configure send email submit action {#steps-to-configure-send-email-submit-action}

To set up Adaptive Form send email configuration, perform the following steps:

1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens. 
1. Click the  **[!UICONTROL Submission]** tab. 
1. From the **[!UICONTROL Submit Action]** drop-down list, select **[!UICONTROL Send email]**.
1. Configure the **[!UICONTROL Action Configuration]** for the **[!UICONTROL Send email]** option.

    ![Action configuration of Send Email](/help/forms/assets/send-email-action-configuration.gif)

    1. Specify sender's email id in the **[!UICONTROL From]** textbox.
    1. Add the email id of the recipient in the **[!UICONTROL To]** textbox. You can add multiple recipients by clicking the **[!UICONTROL Add]** button. 
    1. [Optional] Add the recipient for CC and BCC by clicking the **[!UICONTROL Add]** button. 
    1. Specify a subject line in the **[!UICONTROL Subject]** textbox.
    1. You can either provide an external email template or create your own custom email template.
    To specify the path to the external email template, use **[!UICONTROL External Template Path]** and click **[!UICONTROL Choose]**. 
    Or add a custom email template for the form submission in the **[!UICONTROL Email Template]** textbox.
    
        ```
        Sample Email Template for Job Application:
        
        From: [Recipient's Email ID]
        To: [Sender's Email ID]
        Subject: Application for [Job Title] - [Your Full Name]
        Dear [Hiring Manager's Name],
        I hope this email finds you well. I am writing to express my interest in the [Job Title] position, as advertised on your company's [where you found the job posting].

        Enclosed, please find my resume for your review. I would welcome the opportunity to further discuss how my experiences and skills make me a suitable candidate for this role.
        I look forward to the possibility of an interview.
        Best regards,

        [Your Full Name]
        [Your Contact Information]
        [LinkedIn Profile or any relevant links]
        ```

    1. [Optional] The **[!UICONTROL Send Email]** Submit Action provides the option to include attachments and a [Document of Record (DoR)](generate-document-of-record-core-components.md) with the email. 
    

1. Click **[!UICONTROL Done]**.


## Best Practices {#best-practices}

* It is recommended to keep the email content clear and concise. Users should understand the purpose of the email and any actions they need to take.
* It is crucial for all form fields to have unique element names, even if they are placed on different panels within an Adaptive Form.
* When using AEM as a Cloud Service, outbound email requires encryption. By default, outbound email functionality is disabled. To activate it, submit a support ticket to [Request Access](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/development-guidelines.html?lang=en#sending-email). 


## Related Articles

{{af-submit-action}}


