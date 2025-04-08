---
title: How to use CAPTCHA in Adaptive Forms?
description: Learn to configure or Google reCAPTCHA service for an Adaptive Form.
uuid: 0e11e98a-12ac-484c-b77f-88ebdf0f40e5
contentOwner: vishgupt
products: SG_EXPERIENCEMANAGER/6.5/FORMS
topic-tags: adaptive_forms, author
feature: Adaptive Forms, Foundation Components
role: User, Developer
exl-id: 3fdbe5a3-5c3c-474d-b701-e0182da4191a
---
# Use reCAPTCHA in Adaptive Forms {#using-reCAPTCHA-in-adaptive-forms}

>[!NOTE]
>
> Adobe recommends using the modern and extensible data capture [Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html) for [creating new Adaptive Forms](/help/forms/creating-adaptive-form-core-components.md) or [adding Adaptive Forms to AEM Sites pages](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md). These components represent a significant advancement in Adaptive Forms creation, ensuring impressive user experiences. This article describes older approach to author Adaptive Forms using foundation components.


| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/captcha-adaptive-forms.html)                  |
| AEM as a Cloud Service     | This article        |
| Applies to | Adaptive Form based on Foundation Components. <br> For Adaptive Form based on Core Components, [Click here](/help/forms/captcha-adaptive-forms-core-components.md).  |


CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) is a program commonly used in online transactions to distinguish between humans and automated programs or bots. It poses a challenge and evaluates user response to determine if it's a human or a bot interacting with the site. It prevents the user to proceed if the test fails and helps make online transactions secure by keeping bots from posting spam or malicious purposes.

AEM Forms as a Cloud Service supports the following CAPTCHA solutions: 

* [Google reCAPTCHA](#configure-recaptcha-service-by-google)
* [Cloudflare Turnstile](/help/forms/integrate-adaptive-forms-turnstile.md)
* [hCaptcha](/help/forms/integrate-adaptive-forms-hcaptcha.md)   

## Configure reCAPTCHA service by Google {#google-reCAPTCHA}

Form authors can use the reCAPTCHA service by Google to implement reCAPTCHA in Adaptive Forms. It offers advance CAPTCHA capabilities to protect your site. For more information on how reCAPTCHA works, see [Google reCAPTCHA](https://developers.google.com/recaptcha/). AEM Forms supports [!DNL reCAPTCHA v2] and [!DNL reCAPTCHA Enterprise]. Any other version is not supported. Also notice, reCAPTCHA in Adaptive Forms is not supported in offline mode on [!DNL AEM Forms] app. Based on your requirement you can configure reCAPTCHA service to enable:

![reCAPTCHA](/help/forms/assets/recaptcha_new.png)

* [reCAPTCHA Enterprise in AEM Forms](#steps-to-implement-reCAPTCHA-enterprise-in-forms)
* [reCAPTCHA v2 in AEM Forms](#steps-to-implement-reCAPTCHA-v2-in-forms)


### Configure reCAPTCHA Enterprise  {#steps-to-implement-reCAPTCHA-enterprise-in-forms}

1. Create or select a [Google Cloud project](https://cloud.google.com/recaptcha-enterprise/docs/set-up-non-google-cloud-environments-api-keys#before-you-begin) and enable [reCAPTCHA Enterprise API](https://cloud.google.com/recaptcha-enterprise/docs/set-up-non-google-cloud-environments-api-keys#enable-the-recaptcha-enterprise-api). 
1. Obtain the [Project ID](https://support.google.com/googleapi/answer/7014113?hl=en#:~:text=To%20locate%20your%20project%20ID,a%20member%20of%20are%20displayed) and create an [API key](https://cloud.google.com/recaptcha-enterprise/docs/set-up-non-google-cloud-environments-api-keys#create_an_api_key) and a [site key for websites](https://cloud.google.com/recaptcha-enterprise/docs/create-key#create-key).
1. Create configuration container for cloud services.

    1. Go to **[!UICONTROL Tools > General > Configuration Browser]**.
    1. Select a folder or create a folder, and enable the folder for cloud configurations using following steps:
        1. In the Configuration Browser, select the folder and select **[!UICONTROL Properties]**.
        1. In the Configuration Properties dialog, enable **[!UICONTROL Cloud Configurations]**.
        1. Select **[!UICONTROL Save & Close]** to save the configuration and exit the dialog.

1. Configure the cloud service for [!DNL reCAPTCHA Enterprise].

    1. On your Experience Manager author instance, go to ![tools-1](assets/tools-1.png) &gt; **[!UICONTROL Cloud Services]**.
    1. Select **[!UICONTROL reCAPTCHA]**. The Configurations page opens. Select the configuration container that you created and select **[!UICONTROL Create]**.
    1. Select version as [!DNL reCAPTCHA Enterprise] and specify Name, Project ID, Site Key, and API key (Obtained in Step 2) for reCAPTCHA Enterprise service.
    1. Select key type, the key type should be same as the site key that you configured in the [Google Cloud project](https://cloud.google.com/recaptcha-enterprise/docs/set-up-non-google-cloud-environments-api-keys#before-you-begin), for example, **Checkbox site key** or **Score-based site key**.
    1. Specify a [threshold score in the range 0 to 1](https://cloud.google.com/recaptcha-enterprise/docs/interpret-assessment#interpret_scores). Scores greater than or equal to the threshold scores identify human interaction, otherwise considered bot interaction.
    1. Select **[!UICONTROL Create]** to create the cloud service configuration.

<!--
    1. In the Edit Component dialog, specify the name, project ID, site key, API key (obtained in steps 2 and 3), select the key type, and enter the threshold score. Select **[!UICONTROL Save Settings]** and then select **[!UICONTROL OK]** to complete the configuration.
-->

Once the reCAPTCHA Enterprise service is enabled, it is available for use in adaptive forms. See [using CAPTCHA in adaptive forms](#using-reCAPTCHA).

<!--
![reCAPTCHA Enterprise](/help/forms/assets/recaptcha1-enterprise.png)
-->

### Configure Google reCAPTCHA v2 {#steps-to-implement-reCAPTCHA-v2-in-forms}

1. Obtain [reCAPTCHA API key pair](https://www.google.com/recaptcha/admin) from Google. It includes a **site key** and a **secret key**.
1. Create configuration container for cloud services. 
    1. Go to **[!UICONTROL Tools > General > Configuration Browser]**.
    1. Select a folder or create a folder, and enable the folder for cloud configurations using following steps:
        1. In the Configuration Browser, select the folder and select **[!UICONTROL Properties]**.
        1. In the Configuration Properties dialog, enable **[!UICONTROL Cloud Configurations]**.
        1. Select **[!UICONTROL Save & Close]** to save the configuration and exit the dialog.

1. Configure the cloud service for reCAPTCHA v2.

    1. On your AEM author instance, go to ![tools-1](assets/tools-1.png) &gt; **Cloud Services**.
    1. Select **[!UICONTROL reCAPTCHA]**. The Configurations page opens. Select the configuration container that you created and select **[!UICONTROL Create]**.
    1. Select version as [!DNL reCAPTCHA v2] , specify Name, Site key, and Secret Key for reCAPTCHA service (Obtained in Step 1) and select **[!UICONTROL Create]** to create the cloud service configuration.
    1. In the Edit Component dialog, specify the site and secret keys obtained in step 1. Select **[!UICONTROL Save Settings]** and then select **OK** to complete the configuration.

   Once the reCAPTCHA service is configured, it is available for use in adaptive forms. For more information, see [using CAPTCHA in adaptive forms](#using-reCAPTCHA).

<!--![reCAPTCHA v2](/help/forms/assets/recaptcha-v2.png)-->


## Use Google reCAPTCHA in adaptive forms {#using-reCAPTCHA}

To use Google reCAPTCHA in an adaptive form:

1. Open an adaptive form in edit mode.

   >[!NOTE]
   >
   >Ensure that the configuration container selected when creating the adaptive form contains the reCAPTCHA cloud service. You can also edit adaptive form properties to change the configuration container associated with the form.

1. From the component browser, drag-drop the **Captcha** component onto the adaptive form.

   >[!NOTE]
   >
   >* Using more than one Captcha component in an adaptive form is not supported. Also, it is not recommended to use CAPTCHA in a panel marked for lazy loading or in a fragment.
   >* reCaptcha is time-sensitive and expires in about a couple of minutes. Therefore, it is recommended to place the Captcha component just before the Submit button in the adaptive form.

1. Select the Captcha component that you added and select ![cmppr](assets/cmppr.png) to edit its properties.
1. Specify a title for the CAPTCHA widget. The default value is **Captcha**. Select **Hide title** if you do not want title to appear.
1. From the **Captcha service** drop-down, select **reCAPTCHA** to enable reCAPTCHA service if you configured it as described in [reCAPTCHA service by Google](#google-reCAPTCHA).
1. Select a configuration from the Settings drop-down for **reCAPTCHA Enterprise** or **reCAPTCHA v2** 
    1. If you select **reCAPTCHA Enterprise** version, the key type can be of **checkbox** or **score based**, It is based on your selection when you configure [site key for websites](https://cloud.google.com/recaptcha-enterprise/docs/create-key#create-key):

    >[!NOTE] 
    >
    >* In the cloud configuration with **key type** as **checkbox**, the customized error message appears as an inline message if the captcha validation fails.
    >* In the cloud configuration with **key type** as **score based**,  the customized error message shows as a pop-up message if the captcha validation fails.

      1. You can select size as **[!UICONTROL Normal]** and **[!UICONTROL Compact]**.
      1. You can select a **[!UICONTROL Bind Reference]**, In **[!UICONTROL Bind Reference]** the data submitted is a bound data, otherwise it is unbound data. Below are XML examples of unbound data and bound data (with bind reference as SSN) respectively, when a form is submitted.

    ```xml

            <?xml version="1.0" encoding="UTF-8" standalone="no"?>
            <afData>
            <afUnboundData>
                <data>
                    <captcha16820607953761>
                        <captchaType>reCaptchaEnterprise</captchaType>
                        <captchaScore>0.9</captchaScore>
                    </captcha16820607953761>
                </data>
            </afUnboundData>
            <afBoundData>
                <Root
                    xmlns:xfa="http://www.xfa.org/schema/xfa-data/1.0/"
                    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                    <PersonalDetails>
                        <SSN>371237912</SSN>
                        <FirstName>Sarah </FirstName>
                        <LastName>Smith</LastName>
                    </PersonalDetails>
                    <OtherInfo>
                        <City>California</City>
                        <Address>54 Residency</Address>
                        <State>USA</State>
                        <Zip>123112</Zip>
                    </OtherInfo>
                </Root>
            </afBoundData>
            <afSubmissionInfo>
                <stateOverrides/>
                <signers/>
                <afPath>/content/dam/formsanddocuments/captcha-form</afPath>
                <afSubmissionTime>20230608034928</afSubmissionTime>
            </afSubmissionInfo>
            </afData>

    ```
        
    ```xml

            <?xml version="1.0" encoding="UTF-8" standalone="no"?>
            <afData>
            <afUnboundData>
                <data/>
            </afUnboundData>
            <afBoundData>
                <Root
                    xmlns:xfa="http://www.xfa.org/schema/xfa-data/1.0/"
                    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                    <PersonalDetails>
                        <SSN>
                            <captchaType>reCaptchaEnterprise</captchaType>
                            <captchaScore>0.9</captchaScore>
                        </SSN>
                        <FirstName>Sarah</FirstName>
                        <LastName>Smith</LastName>
                    </PersonalDetails>
                    <OtherInfo>
                        <City>California</City>
                        <Address>54 Residency</Address>
                        <State>USA</State>
                        <Zip>123112</Zip>
                    </OtherInfo>
                </Root>
            </afBoundData>
            <afSubmissionInfo>
                <stateOverrides/>
                <signers/>
                <afPath>/content/dam/formsanddocuments/captcha-form</afPath>
                <afSubmissionTime>20230608035111</afSubmissionTime>
            </afSubmissionInfo>
            </afData>
    ```
    
    If you select **reCAPTCHA v2** version:
      1. You can select the size as **[!UICONTROL Normal]** or **[!UICONTROL Compact]** for the reCAPTCHA widget. 
      1. You can select the **[!UICONTROL Invisible]** option to show the CAPTCHA challenge only in the case of a suspicious activity.

    The reCAPTCHA service is enabled on the adaptive form. You can preview the form and see the CAPTCHA working. The **protected by reCAPTCHA** badge, displayed below, is displayed on the protected forms.
    ![Google protected by reCAPTCHA badge](/help/forms/assets/google-recaptcha-v2.png)

1. Save the properties.

>[!NOTE]
> 
> Do not select **[!UICONTROL Default]** from the Captcha service drop-down as the default AEM CAPTCHA service is deprecated.

>[!VIDEO](https://video.tv.adobe.com/v/3422641/recaptcha-google-adaptive-forms/?quality=12&learn=on)

### Show or hide CAPTCHA component based on rules {#show-hide-captcha}

You can select to show or hide the CAPTCHA component based on rules that you apply on a component in an Adaptive Form. Select the component, select ![edit rules](assets/edit-rules-icon.svg), and select **[!UICONTROL Create]** to create a rule. For more information on creating rules, see [Rule Editor](rule-editor.md).

For example, the CAPTCHA component must display in an Adaptive Form only if the Currency Value field in the form has a value of more than 25000.

Select the **[!UICONTROL Currency Value]** field in the form and create the following rules:

![Show or hide rules](assets/rules-show-hide-captcha.png)

   >[!NOTE]
   >
   > When you select a reCAPTCHA v2 configuration and the size is set to [!UICONTROL Invisible], the show/hide option remains disabled.

### Validate CAPTCHA {#validate-captcha}

You can validate CAPTCHA in an Adaptive Form either when you submit the form or base the CAPTCHA validation on user actions and conditions.

#### Validate CAPTCHA on form submission {#validation-form-submission}

To validate a CAPTCHA automatically when you submit an Adaptive Form:

1. Select the CAPTCHA component and select ![cmppr](assets/configure-icon.svg) to view the component properties.
1. In the **[!UICONTROL Validate CAPTCHA]** section, select **[!UICONTROL Validate CAPTCHA at form submission]**.
1. Select ![Done](assets/save_icon.svg) to save the component properties.

#### Validate CAPTCHA on user actions and conditions {#validate-captcha-user-action}

To validate a CAPTCHA based on conditions and user actions:

1. Select the CAPTCHA component and select ![cmppr](assets/configure-icon.svg) to view the component properties.
1. In the **[!UICONTROL Validate CAPTCHA]** section, select **[!UICONTROL Validate CAPTCHA on a user action]**.
1. Select ![Done](assets/save_icon.svg) to save the component properties.

[!DNL Experience Manager Forms] provides `ValidateCAPTCHA` API to validate CAPTCHA using pre-defined conditions. You can invoke the API using a custom Submit Action or by defining rules on components in an Adaptive Form.

The following is an example of a `ValidateCAPTCHA` API to validate CAPTCHA using pre-defined conditions:

```javascript
if (slingRequest.getParameter("numericbox1614079614831").length() >= 5) {
     GuideCaptchaValidatorProvider apiProvider = sling.getService(GuideCaptchaValidatorProvider.class);
        String formPath = slingRequest.getResource().getPath();
        String captchaData = slingRequest.getParameter(GuideConstants.GUIDE_CAPTCHA_DATA);
        if (!apiProvider.validateCAPTCHA(formPath, captchaData).isCaptchaValid()){
            response.setStatus(400);
            return;
        }
    }
```

The example signifies that the `ValidateCAPTCHA` API validates the CAPTCHA in the form only if number of digits in the numeric box specified by the user while filling the form is greater than 5.

**Option 1: Use [!DNL Experience Manager Forms] ValidateCAPTCHA API to validate CAPTCHA using a custom Submit Action**

Perform the following steps to use the `ValidateCAPTCHA` API to validate CAPTCHA using a custom Submit Action:

1. Add the script that includes the `ValidateCAPTCHA` API to custom Submit Action. For more on custom Submit Actions, see [Create a custom Submit Action for Adaptive Forms](custom-submit-action-form.md).
1. Select the name of the custom Submit Action from the **[!UICONTROL Submit Action]** drop-down list in **[!UICONTROL Submission]** properties of an Adaptive Form.
1. Select **[!UICONTROL Submit]**. The CAPTCHA gets validated based on the conditions defined in `ValidateCAPTCHA` API of the custom Submit Action.

**Option 2: Use [!DNL Experience Manager Forms] ValidateCAPTCHA API to validate CAPTCHA on a user action before submitting the form**

You can also invoke `ValidateCAPTCHA` API by applying rules on a component in an Adaptive Form.

For example, you add a **[!UICONTROL Validate CAPTCHA]** button in an Adaptive Form and create a rule to invoke a service on the click of a button.

The following figure illustrates how you can invoke a service on the click of a **[!UICONTROL Validate CAPTCHA]** button:

![Validate CAPTCHA](assets/captcha-validation1.gif)

You can invoke the custom servlet that includes `ValidateCAPTCHA` API using the rule editor and enable or disable the submit button of the Adaptive Form based on the validation result.

Similarly, you can use rule editor to include a custom method to validate CAPTCHA in an Adaptive Form.

<!--

### Add custom CAPTCHA services {#add-custom-captcha-service}

[!DNL Experience Manager Forms] provides reCAPTCHA as the CAPTCHA service. However, you can add a custom service to display in the **[!UICONTROL CAPTCHA Service]** drop-down list.  

The following is a sample implementation of the interface to add additional CAPTCHA service to your Adaptive Form:

```javascript
package com.adobe.aemds.guide.service;

import org.osgi.annotation.versioning.ConsumerType;

/**
 * An interface to provide captcha validation at server side in Adaptive Form
 * This interface can be used to provide custom implementation for different captcha services.
 */
@ConsumerType
public interface GuideCaptchaValidator {
    /**
     * This method should define the actual validation logic of the captcha
     * @param captchaPropertyNodePath path to the node with CAPTCHA configurations inside form container
     * @param userResponseToken  The user response token provided by the CAPTCHA from client-side
     *
     * @return  {@link GuideCaptchaValidationResult} validation result of the captcha
     */
     GuideCaptchaValidationResult validateCaptcha(String captchaPropertyNodePath, String userResponseToken);

    /**
     * Returns the name of the captcha validator. This should be unique among the different implementations
     * @return  name of the captcha validator
     */
     String getCaptchaValidatorName();
}
```

`captchaPropertyNodePath` refers to the resource path of the CAPTCHA component in the Sling repository. Use this property to include details specific to the CAPTCHA component. For example, `captchaPropertyNodePath` includes information for the reCAPTCHA cloud configuration configured on the CAPTCHA component. The cloud configuration information provides **[!UICONTROL Site Key]** and **[!UICONTROL Secret Key]** settings for implementing the reCAPTCHA service.

`userResponseToken` refers to the `g_recaptcha_response` that gets generated after solving a CAPTCHA in a form. -->

### Edit reCAPTCHA service domain {#reCAPTCHA-service-domain}

reCAPTCHA service uses `https://www.recaptcha.net/` as the default domain. You can modify the settings to set `https://www.google.com/` or any custom domain name for loading, rendering, and validating the reCAPTCHA service.

Set the **[!UICONTROL af.cloudservices.recaptcha.domain]** property of the **[!UICONTROL Adaptive Form and Interactive Communication Web Channel Configuration]** configuration to specify `https://www.google.com/` or any other custom domain name. The following JSON file displays a sample:

```json
{
  "af.cloudservices.recaptcha.domain": "https://www.google.com/"
}
```

To set values of a configuration, [Generate OSGi Configurations using the AEM SDK](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/configuring-osgi.html?lang=en#generating-osgi-configurations-using-the-aem-sdk-quickstart), and [deploy the configuration](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/deploy-code.html?lang=en#deployment-process) to your Cloud Service instance.

## See Also {#see-also}

{{see-also}}

<!--

>[!MORELIKETHIS]
>
>* [Reference Themes, Templates, and Form Data models for Adaptive Forms](/help/forms/reference-themes-templates-data-models.md)

-->
