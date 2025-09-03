---
title: Show a custom thank you message after form submission
description: Learn how to configure thank you pages and redirection for Forms Block to optimize user experience and streamline user journeys.
feature: Edge Delivery Services
exl-id: e6c66b22-dc52-49e3-a920-059adb5be22f
role: Admin, Architect, Developer
---
# Show a custom thank you message after form submission

After a user submits a form, it is crucial to provide a seamless experience through a thank you message. It not only confirms successful submission but also enhance user satisfaction and guide them further in their journey.

- **Thank you message**: A thank you message is a cornerstone of user experience, offering reassurance and conveying important information while reinforcing brand identity. It serves as a direct acknowledgment of the user's action, fostering a sense of completion and satisfaction.

- **Redirect**: A redirect plays a pivotal role in steering users towards relevant destinations, optimizing engagement, and ultimately boosting conversion rates. By seamlessly guiding users to the next step in their journey, a redirect ensures a smooth navigation experience. For example, redirecting user to the payments page after collecting initial details. 

The default behavior of Adaptive Forms Block is to display the following thank you message on submission. The message is displayed on the top of the form on successful form submission. 

![default thank you message](/help/edge/assets/thank-you-message.png)

However, you have the flexibility to tailor this experience to meet your specific needs. Options include:

- Show a custom thank you message after form submission
- Redirect users to another page post-submission for further action

>[!NOTE]
>
> You can refer to the following [enquiry spreadsheet](/help/edge/docs/forms/assets/enquiry.xlsx) to customize the thank you message according to your requirements.

## Configure a custom thank you message

In case you wish to show a personalized thank you message upon successful form submission, you can configure your spreadsheet to display it.

Follow the below steps to configure a custom thank you message for your Adaptive Forms Block:

1. Go to your Edge Deliver project folder on Microsoft SharePoint or Google Workspace and open your spreadsheet. 
1. Add a customized thank you message in the `value` column for the `submit` field type in the spreadsheet. 

    ![Customized Thankyou message](/help/edge/docs/forms/assets/thankyou-custommessage.png)

    For example, add `Submission Successful!` message in the `value` column for the `submit` field type.

1. Preview and publish the sheet using [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content). 

    ![Customized Thankyou message](/help/edge/docs/forms/assets/customized-thank-you-message.png)

## Redirect users to another page post-submission

Redirecting a user to another page after form submission can enhance user experience by providing relevant information, confirming actions, and guiding users towards desired outcomes. For example, 

- after a user completes a purchase form, they are redirected to a payment page to complete the transaction securely. 
- upon submitting a registration form for an event or webinar, users are redirected to a confirmation page displaying event details, such as date, time, and location.

Follow the below steps to redirect users to another page:

1. Go to your Edge Deliver project folder on Microsoft SharePoint or Google Workspace and open your spreadsheet.  
1. Paste the URL in the `value` column for the `submit` field type in the spreadsheet to redirect user on successful form submission. 
   To redirect the page to a different page, use the [Edge Delivery Documentation](https://www.aem.live/docs/) page URL. 

    ![Thankyou redirect URL](/help/edge/docs/forms/assets/thankyou-redirecturl.png)

1. Preview and publish the sheet using [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content). 

    ![Redirect Thankyou message](/help/edge/docs/forms/assets/thankyou-redirectpage.gif)

You can also create new document file and add its preview URL in the `value` column for the `submit` field type.

After a user submits a form, it is important to provide a clear thank you message. It confirms the submission is successful and improves user satisfaction.

