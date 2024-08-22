---
title: How to use Google reCAPTCHA in an AEM Adaptive Form?
description: Enhance form security with Google reCAPTCHA service effortlessly. Step-by-step guide inside!
topic-tags: Adaptive Forms, author
keywords: Google reCAPTCHA service, Adaptive Forms, CAPTCHA challenge, Bot prevention, Core Components, Form submission security, Form spam prevention
feature: Adaptive Forms, Core Components
exl-id: d116f979-efb6-4fac-8202-89afd1037b2c
role: User, Developer
---
# Use Google reCAPTCHA in an AEM Adaptive Form based on Core Components {#using-reCAPTCHA-in-adaptive-forms}

| Applies to | Article link |
| -------- | ---------------------------- |
|  Adaptive Form based on Core Components   | This article  |
|  Adaptive Form based on Foundation Components | [Click here](/help/forms/captcha-adaptive-forms.md) |

CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) is a program commonly used in online transactions to distinguish between humans and automated programs or bots. It poses a challenge and evaluates user response to determine if it's a human or a bot interacting with the site. It prevents the user to proceed if the test fails and helps make online transactions secure by keeping bots from posting spam or malicious purposes. 

AEM Forms as a Cloud Service supports the following CAPTCHA solutions: 

* [Google reCAPTCHA](#connect-your-aem-forms-environment-with-recaptcha-service-by-google)
* [Cloudflare Turnstile](/help/forms/integrate-adaptive-forms-turnstile-core-components.md)
* [hCaptcha](/help/forms/integrate-adaptive-forms-hcaptcha-core-components.md)  


## Connect your AEM Forms environment with reCAPTCHA service by Google {#connect-your-forms-environment-with-recaptcha-service-by-google}

Form authors can use the reCAPTCHA service by Google to implement reCAPTCHA in Adaptive Forms. It offers advance CAPTCHA capabilities to protect your site. For more information on how reCAPTCHA works, see [Google reCAPTCHA](https://developers.google.com/recaptcha/). [!DNL AEM Forms] as a [!DNL Cloud Service] supports Google reCAPTCHA v2 in Adaptive Forms. You can use it to present a CAPTCHA challenge on form submission. To connect your AEM Forms environment with reCAPTCHA service by Google 

1. Obtain [reCAPTCHA API key pair](https://www.google.com/recaptcha/admin) from Google. It includes a **site key** and a **secret key**.

    ![Create Google reCAPTCHA configuration of Google's website to obtain reCAPTCHA Keys](/help/forms/assets/google-captcha.gif)
1. Create Configuration Container on your AEM Forms as a Cloud Service environment. A Configuration Container holds Cloud Configurations used to connect AEM to external services. To create and configure a Configuration Container to connect your AEM Forms environment with reCAPTCHA service by Google:   
    1. Open your AEM Forms as a Cloud Service instance. 
    1. Go to **[!UICONTROL Tools > General > Configuration Browser]**. In the Configuration Browser, you can: 
    1. Select an existing folder or create a folder. You can create a folder and enable the Cloud Configurations option for it or Enable the Cloud Configurations option for an existing folder: 

        * To create a folder and enable the Cloud Configurations option for it: 
            1. In the Configuration Browser, click **[!UICONTROL Create]**. 
            1. In the Create Configuration dialog, specify name, title, and select the **[!UICONTROL Cloud Configurations]** option. 
            1. Click **[!UICONTROL Create]**
        * To enable the Cloud Configurations option for an existing folder: 
            1. In the Configuration Browser, select the folder and select **[!UICONTROL Properties]**.
            1. In the Configuration Properties dialog, enable **[!UICONTROL Cloud Configurations]**.
            1. Select **[!UICONTROL Save & Close]** to save the configuration and exit the dialog.

1. Configure the Cloud Service: 
    1. On your AEM author instance, go to ![tools-1](assets/tools-1.png) &gt; **[!UICONTROL Cloud Services]** and select **[!UICONTROL reCAPTCHA]**.
    1. Select a Configuration Container, created or updated in previous section. Select **[!UICONTROL Create]**.
    1. Specify **[!UICONTROL Title]**, **[!UICONTROL Name]**, **[!UICONTROL Site Key]**, and **[!UICONTROL Secret Key]** for reCAPTCHA service (Obtained in Step 1). Select **[!UICONTROL Create]**.

    ![Configure the Cloud Service to connect your AEM Forms environment with reCAPTCHA service by Google](/help/forms/assets/captcha-configuration.gif)
    
   Once the reCAPTCHA service is configured, it is available for use in an Adaptive Form. For more information, see [using Google reCAPTCHA in an Adaptive Form](#using-reCAPTCHA).

## Use Google reCAPTCHA in an Adaptive Form {#using-reCAPTCHA}

To use reCAPTCHA in Adaptive Forms:

1. Open your AEM Forms as a Cloud Service instance. 
1. Go to **[!UICONTROL Forms]** > **[!UICONTROL Forms and Documents]**.  
1. Select an Adaptive Forms and select **[!UICONTROL Properties]**. For the **[!UICONTROL Configuration Container]** option, select the Configuration Container that contains the Cloud Configuration that connects AEM Forms with reCAPTCHA service by Google and select **[!UICONTROL Save & Close]**. 

    If you do not have such a Configuration Container, see section [Connect your AEM Forms environment with reCAPTCHA service by Google](#connect-your-forms-environment-with-recaptcha-service-by-google) to learn how to create such a Configuration Container.

    ![Select Configuration Container](/help/forms/assets/captcha-properties.png)

1. Select an Adaptive Forms and select **[!UICONTROL Edit]**. The Adaptive Form opens in Adaptive Forms Editor. 
1. From the component browser, drag-drop the **[!UICONTROL Adaptive Form reCAPTCHA]** component onto the Adaptive Form. 

     Google reCAPTCHA validation is time-sensitive and expires in about a couple of minutes. Therefore, Adobe recommends placing the **[!UICONTROL Adaptive Form reCAPTCHA]** component just before the **[!UICONTROL Submit]** button.

1. Select the **[!UICONTROL Adaptive Form reCAPTCHA]** component and select the properties ![Properties icon](assets/configure-icon.svg) icon. It opens the properties dialog. Specify the following mandatory properties: 
    * **[!UICONTROL Name]:** You can identify a form component easily with its unique name both in the form and in the rule editor, but the name must not contain spaces or special characters. 
    * **[!UICONTROL CAPTCHA Configuration]:** Select a Cloud Configuration configured to present the Google reCAPTCHA dialog for the form. You can have multiple Cloud Configurations in your environment for similar purpose. So, choose the service carefully. If no service is listed, see [Connect your AEM Forms environment with reCAPTCHA service by Google](#connect-your-forms-environment-with-recaptcha-service-by-google) to learn how to create a Cloud Service that connects your AEM Forms environment with reCAPTCHA service by Google.  
    * **Captcha Size:** You can select the display size of Google reCAPTCHA challenge dialog. Use the **[!UICONTROL Compact]** option to display a small sized and the **[!UICONTROL Normal]** option to display a relatively large-size Google reCAPTCHA challenge dialog.

1. Select **[!UICONTROL Done]**. 

    Now, the **protected by reCAPTCHA** is displayed on your Adaptive Form. It is displayed on all the Adaptive Forms which are configured to use the Google reCAPTCHA service. 
    
    Now, only legitimate forms, in which the form filler successfully clears the challenge posed by the Google reCAPTCHA service, are allowed for submission.
    ![Google protected by reCAPTCHA badge](/help/forms/assets/google-recaptcha-v2.png)

<!--
### Show or hide CAPTCHA component based on rules {#show-hide-captcha}

You can select to show or hide the CAPTCHA component based on rules that you apply on a component in an Adaptive Form. Select the component, select ![edit rules](assets/edit-rules-icon.svg), and select **[!UICONTROL Create]** to create a rule. For more information on creating rules, see [Rule Editor](rule-editor.md).

For example, the CAPTCHA component must display in an Adaptive Form only if the Currency Value field in the form has a value of more than 25000.

Select the **[!UICONTROL Currency Value]** field in the form and create the following rules:

![Show or hide rules](assets/rules-show-hide-captcha.png)

   >[!NOTE]
   >
   > When you select a reCAPTCHA v2 configuration and the size is set to [!UICONTROL Invisible], the show/hide option remains disabled.

   -->

## Frequently Asked Questions

**Q: Can I use more than one Captcha component in an Adaptive Form?**
**Ans:** Using more than one Captcha component in an Adaptive Form is not supported. Also, it is not recommended to use Captcha component in a fragment or a panel marked for lazy loading.

## See Also {#see-also}

{{see-also}}