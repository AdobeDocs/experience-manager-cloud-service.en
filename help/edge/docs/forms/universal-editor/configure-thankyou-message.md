---
title: "How to Configure a Redirect Page or Thank you message"
description: "Learn how users can be displayed a thank you message or redirected to a webpage that form authors can configure while creating the form."
feature: Adaptive Forms, Edge Delivery Services
role: User
level: Intermediate
---
# Configure Redirect or Thank You Message

In forms created using the Universal Editor, form authors can configure what happens after a user submits a form. You can either display a thank you message or redirect the user to a specific webpage by using the Submission tab in the Edit Form Properties extension.

You can configure the  Thankyou message or Rediect URLs for forms created in the Universal Editor using the **Submission** tab of the **AEM Form Properties** extension.

## Prerequisites

You can configure the submit action for forms created in the Universal Editor using the **Submission** tab of the **Edit Form Properties** extension.

![Form properties icon](/help/forms/assets/ue-form-properties-icon.png)

![Universal Editor Form Properties](/help/forms/assets/ue-form-properties.png)

>[!NOTE]
>
>* If you do not see the **Form Properties** icon in your Universal Editor interface, enable the **Edit Form Properties** extension in the Extension Manager. 
>* Refer to the [Extension Manager Feature Highlights](https://developer.adobe.com/uix/docs/extension-manager/feature-highlights/#enablingdisabling-extensions) article to learn how to enable or disable extensions in the Universal Editor.

## How to Configure Redirect or Thank You Message?

On submission of a form, you can redirect the user to another webpage or show a message. 

To configure the redirect page or thank you message: 

1. Open the Adaptive Form for editing.
1. Open the Content Tree and select the **[!UICONTROL Guide Container]**. 
1. Click the Adaptive Form Container properties ![Adaptive Form Container properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box to configure Data Models opens. 
1. Open the **[!UICONTROL Submission]** tab. Options to configure a redirect page or a message are displayed: 

    ![Submission dialog of Guide Contaner to configure a redirect page or a message](/help/forms/assets/adaptive-forms-core-components-redirect-page-or-thank-you-message.png)

**Configure Redirect URLs**

* To configure a Redirect URL, for on Submit option, select the **[!UICONTROL Redirect to URL option]**, and provide an absolute address or a Redirect URL or relative path of an AEM Sites page. 

![redirect](/help/edge/docs/forms/universal-editor/assets/redirect-ue.png)

**Configure Thankyou message**

* To configure a custom or thank you message, select the **[!UICONTROL Show Message]** option, and provide a message in the Message content box. It is a rich text box, you can use the full screen option to view all the available rich text items. 

![thankyou](/help/edge/docs/forms/universal-editor/assets/thankyou-ue.png)

Form authors can configure a page for each form, to which the form users are redirected after submitting a form.
