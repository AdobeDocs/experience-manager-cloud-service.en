---
title: How to configure a Submit Action to send an email for an Adaptive Form?
description: An Adaptive Form provides a Submit Action to send an email. 
keywords: how to configure send an email submit action for an adpative form
feature: Adaptive Forms, Core Components
---

# Configure Send Email submit action

To send an email to one or more recipients upon successful submission of the form, you can use the **[!UICONTROL Send Email]** Submit Action. 

This action enables you to create an email that includes form data in a predefined format. For instance, consider the following template where customer name, shipping address, state name, and ZIP code are retrieved from the submitted form data:

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

## Steps to configure send email submit action {#steps-to-configure-send-email-submit-action}

1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens. 
1. Click the  **[!UICONTROL Submission]** tab. 
1. From the **[!UICONTROL Submit Action]** drop-down list, select **[!UICONTROL Send email]** .
1. Configure the **[!UICONTROL Action Configuration]** for the **[!UICONTROL Send email]** option.


    1. Specify email id in the **[!UICONTROL From]** textbox.
    1. Add the email id of the recipient in the **[!UICONTROL To]** textbox. You can add multiple recipients by clicking the **[!UICONTROL Add]** button. 
    1. [Optional] Add the recipents for CC and BCC by clicking the **[!UICONTROL Add]** button. 
    1. Specify the proper and clear subject line in the **[!UICONTROL Subject]** textbox.
    1. You can either provide the external template path or you can add your own emaol template in the **![!UICONTROL Email Template]** textbox.
    1. [Optional] The **[!UICONTROL Send Email]** Submit Action provides the option to include attachments and a Document of Record (DoR) with the email. 
    To enable the [!UICONTROL Attach Document of Record] option, refer to the documentation on [configure the Adaptive Form to generate a Document of Record (DoR)](generate-document-of-record-core-components.md). You can enable this option from the Adaptive Form properties.

1. Click **[!UICONTROL Done]**


>[!NOTE]
>
> * It is crucial for all form fields to have unique element names, even if they are placed on different panels within an Adaptive Form.
> * When using AEM as a Cloud Service, outbound email requires encryption. By default, outbound email functionality is disabled. To activate it, submit a support ticket to [Request Access](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/development-guidelines.html?lang=en#sending-email). 


## Best Practices {#best-practices}

1. If the form submission involves sensitive information, ensure that the email communication is secure.
1. It is recommended to keep the email content clear and concise. Users should understand the purpose of the email and any actions they need to take.
