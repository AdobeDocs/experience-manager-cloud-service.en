---
title: Use reCAPTCHA with Edge Delivery Services for AEM Forms as a Cloud Service
description: Use Google reCAPTCHA in an form for Edge Delivery Services for AEM Forms
feature: Edge Delivery Services
keywords: reCAPTCHA in forms, Using reCAPTCHA in Universal Editor, Add reCAPTCHA in forms
role: Admin, Architect, Developer
hide: yes
hidefromtoc: yes
exl-id: 1f28bd13-133f-487e-8b01-334be7c08a3f
---
# Use reCAPTCHA in WYSIWYG Authoring

CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) is a popular tool used to protect websites from fraudulent activities, spam, and misuse. 

For example, consider a form that calculates the tax based on additional deductions and the tax rate. In such cases, there is a risk of malicious users exploiting the form for purposes like sending phishing emails or flooding it with irrelevant or harmful content using spambots. Integrating CAPTCHA offers added security by verifying that submissions are from genuine users, effectively minimizing spam entries.

![Google recaptcha](/help/edge/docs/forms/universal-editor/assets/google-recaptcha.png)

In Edge Delivery Services Forms, the Form Block allows you to [connect Google reCAPTCHA with forms](#connect-forms-with-recaptcha-service-by-google) using the **Captcha(Invisible)** component to distinguish between humans and bots. This functionality helps authors protect their forms from spam and misuse.

## Connect Forms with reCAPTCHA Service by Google

You can author Edge Delivery Services Forms to implement the reCAPTCHA service provided by Google. Depending on your needs, you may configure one of the following reCAPTCHA services for your Edge Delivery Services Forms:

* [reCAPTCHA Enterprise](#configure-recaptcha-enterprise)
* [reCAPTCHA](#configure-recaptcha)

>[!NOTE]
>
> For more information on how reCAPTCHA works, see [Google reCAPTCHA](https://developers.google.com/recaptcha/). 

### Configure reCAPTCHA Enterprise

reCAPTCHA Enterprise is a premium, enterprise-grade fraud detection and prevention service offered by Google. It builds on the foundation of reCAPTCHA (score-based) but provides additional features, scalability, and customization to meet the complex needs of businesses.

#### Before You Start

Before configuring Google reCAPTCHA Enterprise for Edge Delivery Services Forms, ensure you have completed the following steps:

1. Create or select a [Google Cloud project](https://cloud.google.com/recaptcha/docs/prepare-environment#before-you-begin) and retrieve the [Project ID](https://support.google.com/googleapi/answer/7014113?hl=en#:~:text=To%20locate%20your%20project%20ID,a%20member%20of%20are%20displayed).

1. [Enable the reCAPTCHA Enterprise API](https://cloud.google.com/recaptcha/docs/prepare-environment#enable-api) for your Google Cloud project and [create an API key](https://console.cloud.google.com/apis/credentials).

1. Create a [site key for your Google Cloud project](https://console.cloud.google.com/security/recaptcha) and copy the site key.

Once you have these credentials, you can proceed with configuring reCAPTCHA Enterprise for your forms:

1. [Create Cloud Configuration Container](#1-create-cloud-configuration-container)
1. [Create the cloud service configuration for reCAPTCHA Enterprise](#2-create-the-cloud-service-configuration-for-recaptcha-enterprise)

#### 1. Create Cloud Configuration Container

To create the cloud configuration container, perform the following steps:

1. Login to your author instance.
1. Go to **[!UICONTROL Tools]** ![tools-1](/help/forms/assets/tools-1.png) > **[!UICONTROL General]** > **[!UICONTROL Configuration Browser]**.

    ![Cloud configuration container](/help/edge/docs/forms/universal-editor/assets/recaptcha-general-configuration.png)

1. In the **[!UICONTROL Configuration Browser]**, navigate to your form and select **[!UICONTROL Properties]**.

    ![Cloud configuration properties](/help/edge/docs/forms/universal-editor/assets/general-configuration-properties.png)
   
1. In the **[!UICONTROL Configuration Properties]** dialog, enable **[!UICONTROL Cloud Configurations]**.

1. Select **[!UICONTROL Save & Close]** to save the configuration and exit the dialog.

    ![Enable Cloud configuration properties](/help/edge/docs/forms/universal-editor/assets/enable-cloud-configurations.png)
`
    After creating the cloud configuration container, publish it.

    ![Publish Cloud Configuration](/help/edge/docs/forms/universal-editor/assets/publish-cloud-configuration.png)

#### 2. Create the cloud service configuration for reCAPTCHA Enterprise

To create the cloud service configuration for reCAPTCHA Enterprise, perform the following steps:

1. Login to your author instance.
1. Navigate to  **[!UICONTROL Tools]** ![tools-1](/help/forms/assets/tools-1.png) &gt; **[!UICONTROL Cloud Services]** > **[!UICONTROL reCAPTCHA]**. 

    ![Recaptcha Cloud Configuration](/help/edge/docs/forms/universal-editor/assets/recaptcha-cloud-configuration.png)

   The **Configurations** dialog opens. 

1. Navigate to your form and select **[!UICONTROL Create]**. 
   
    ![Captcha configuration](/help/edge/docs/forms/universal-editor/assets/create-captcha-confguration.png)

   The **[!UICONTROL Create reCAPTCHA Configuration]** dialog opens.

    ![reCaptcha Enterprise](/help/edge/docs/forms/universal-editor/assets/recaptcha-enterprise.png)

1. Select version as [!DNL ReCAPTCHA Enterprise] and specify Title, Name, Project ID, Site Key, and API key.
   
   >[!NOTE]
   >
   > You can obtain the Project ID, Site Key, and API key from the [Before You Start ](#before-you-start) section for reCAPTCHA Enterprise.

1. Select **[!UICONTROL Key type]** as **Score-based site key**.
1. Specify a [threshold score in the range 0 to 1](https://cloud.google.com/recaptcha/docs/interpret-assessment-website#interpret_scores). Scores greater than or equal to the threshold scores identify human interaction, otherwise considered as bot interaction.
1. Select **[!UICONTROL Create]** to create the cloud service configuration.

    After creating the reCAPTCHA cloud configuration, publish it.

    ![Publish Recaptcha configuration](/help/edge/docs/forms/universal-editor/assets/publisg-recaptcha-configuration.png)

You can now create or edit a form and add the reCAPTCHA component using the WYSIWYG based authoring. For detailed instructions on integrating Google reCAPTCHA into your form, refer to [Use reCAPTCHA in Your Form](#use-recaptcha-in-your-form). 

## Configure reCAPTCHA 

reCAPTCHA is a free service offered by Google that helps websites detect and prevent abusive traffic, including bots and spam. It supports a score-based version that operates in the background and assigns a risk score (ranging from 0.0 to 1.0) to each user interaction. Scores greater than or equal to the threshold scores identify human interaction, otherwise considered as bot interaction.

#### Before You Begin

Before configuring Google reCAPTCHA for Edge Delivery Services Forms, retrieve the [reCAPTCHA API key pair from the Google Console](https://www.google.com/recaptcha/admin). The pair includes a Site key and a Secret key.

>[!NOTE]
>
> * Edge Delivery Services Forms only supports **reCAPTCHA Score based** version.

Once you have the API key pair, you can proceed with configuring reCAPTCHA for your forms:

1. [Create Cloud Configuration Container](#1-create-cloud-configuration-container-1)
1. [Create the cloud service configuration for reCAPTCHA](#2-create-the-cloud-service-configuration-for-recaptcha)

#### 1. Create Cloud Configuration Container 

To create the cloud configuration container, perform the following steps:

1. Login to your author instance.
1. Go to **[!UICONTROL Tools]** ![tools-1](/help/forms/assets/tools-1.png) > **[!UICONTROL General]** > **[!UICONTROL Configuration Browser]**.

    ![Cloud configuration container](/help/edge/docs/forms/universal-editor/assets/recaptcha-general-configuration.png)

1. In the **[!UICONTROL Configuration Browser]**, navigate to your form and select **[!UICONTROL Properties]**.

    ![Cloud configuration properties](/help/edge/docs/forms/universal-editor/assets/general-configuration-properties.png)
   
1. In the **[!UICONTROL Configuration Properties]** dialog, enable **[!UICONTROL Cloud Configurations]**.

1. Select **[!UICONTROL Save & Close]** to save the configuration and exit the dialog.

    ![Enable Cloud configuration properties](/help/edge/docs/forms/universal-editor/assets/enable-cloud-configurations.png)

    After creating the cloud configuration container, publish it.

    ![Publish Cloud Configuration](/help/edge/docs/forms/universal-editor/assets/publish-cloud-configuration.png)

#### 2. Create the cloud service configuration for reCAPTCHA

To create the cloud service configuration for reCAPTCHA, perform the following steps:

1. Login to your author instance.
1. Navigate to  **[!UICONTROL Tools]** ![tools-1](/help/forms/assets/tools-1.png) &gt; **[!UICONTROL Cloud Services]** > **[!UICONTROL reCAPTCHA]**. 

    ![Recaptcha Cloud Configuration](/help/edge/docs/forms/universal-editor/assets/recaptcha-cloud-configuration.png)

   The **Configurations** dialog opens. 

1. Navigate to your form and select **[!UICONTROL Create]**. 
   
    ![Captcha configuration](/help/edge/docs/forms/universal-editor/assets/create-captcha-confguration.png)

   The **[!UICONTROL Create reCAPTCHA Configuration]** dialog opens.

    ![reCaptcha Enterprise](/help/edge/docs/forms/universal-editor/assets/recaptcha.png)

1. Select version as [!DNL ReCAPTCHA v2] and specify Title and Name.
1. Specify the Site Key and Secret Key.
   
   >[!NOTE]
   >
   > You can obtain the Site Key and Secret key from the [Before You Begin](#before-you-begin) section for reCAPTCHA.

1. Select **[!UICONTROL Create]** to create the cloud service configuration.

    After creating the reCAPTCHA cloud configuration, publish it.

    ![Publish Recaptcha configuration](/help/edge/docs/forms/universal-editor/assets/publisg-recaptcha-configuration.png)

You can now create and edit a form and add the reCAPTCHA component using the WYSIWYG based authoring. For detailed instructions on integrating Google reCAPTCHA into your form, refer to [Use reCAPTCHA in Your Form](#use-recaptcha-in-your-form). 

### Use reCAPTCHA in Your Form

To author a form and add the reCAPTCHA (Invisible) component, perform the following steps:

1. Open a form in Universal Editor for editing.
1. Navigate to the added Adaptive Form section in the Content tree.
1. Click the **[!UICONTROL Add]** icon and add the **[!UICONTROL Captcha (Invisble)]** component from the **Adaptive Form Components** list. 

    ![Add reCaptcha component](/help/edge/docs/forms/universal-editor/assets/add-recaptcha-component.png)

     You can also drag and drop the required Adaptive Forms component, as the Universal Editor offers an intuitive drag-and-drop feature.

1. Click **Publish** to publish the form again after adding the **[!UICONTROL Captcha (Invisble)]** component.

    ![republish form](/help/edge/docs/forms/universal-editor/assets/publish-form.png)

You can now view the form with reCAPTCHA service at the following URL:
    `https://<branch>--<repo>--<owner>.aem.live/content/forms/af/<form-name`.

![Form with reCAPTCHA](/help/edge/docs/forms/universal-editor/assets/form-with-recaptcha.png)

## Frequently Asked Questions

* **What happens if a user does not create a reCAPTCHA cloud configuration?**
    
    **A**: If a user does not create a reCAPTCHA cloud configuration, the AEM server searches for the reCAPTCHA cloud configuration in the Global Configuration Container. If no configuration exists in the Global Configuration Container, the AEM server throws an error.

* **What happens if a user creates multiple reCAPTCHA cloud configurations?**
    **A**: If a user creates more than one reCAPTCHA cloud configurations, the system automatically selects the first created reCAPTCHA configuration.

* **Why are modifications or changes not visible at the published URL?**
    If modifications or changes are not visible at the published URL, ensure that the form is republished to apply the updates.

* **Which reCAPTCHA service does Edge Delivery Services Forms support?**
    **A**: Edge Delivery Services Forms supports only score-based reCAPTCHA service provided by Google.


## See also

{{see-more-forms-eds}}
