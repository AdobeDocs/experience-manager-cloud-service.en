---
title: Integrate Adobe Analytics to AEM Forms with Experience Cloud Setup Automation
description: Experience Cloud Setup Automation helps to connect Adobe Analytics to AEM Forms. It helps in tracking and analyzing user interaction with AEM Forms, offering insights into visitor interactions and engagement.
---

# Integrate Adobe Analytics to AEM Forms with Experience Cloud Setup Automation {#integrate-adobe-analytics-to-aem-forms-with-experience-cloud-setup-automation}

Experience Cloud Setup Automation helps to connect Adobe Analytics to AEM Forms, Adobe Analytics aids in tracking and analyzing user interaction with AEM Forms, offering insights into visitor interactions and engagement. Experience Cloud Setup Automation also helps monitoring form performance which involves assessing metrics like completion times and drop-off points. This analysis helps optimize forms for better user experience while distinguishing user behavior based on login status, for example, anonymous users, to identify general trends and patterns.

## Advantages of integrating Adobe Analytics with AEM Forms{#advantages-of-integrating-adobe-analytics-with-aem-forms}

* **Insights into end-user behavior**: Adobe Analytics helps to get insights about end-user behavior,  reveals user actions, drop-offs, and completion rates, enabling a deeper understanding of how individuals engage with forms.
* **Enabling non-technical business users to gain insights**: Adobe Analytics empowers even non-technical users to access and interpret form usage data, fostering data-driven decisions for enhancing form experience for user satisfaction.
* **Optimizing data capture experience based on usage**: Organizations can identify pain points in data capture, leading to targeted improvements that enhance form usability and increase successful submissions.

## Prerequisites {#prerequisites}

Experience Cloud Setup Automation in Adobe Experience Manager Forms requires an Adobe Analytics license, Data Collection (Formerly Adobe Launch) to manage tracking scripts, and integration with the Experience Platform Launch API for streamlined data aggregation and insights generation.

When you have access to the above applications, you can visit the developer console and search your project with the program id and author id of your AEM instance, and ensure that you have Experience Cloud Setup Automation, Adobe Analytics, and Experience Platform Launch API are included in the corresponding AEM developer console as shown in the image below.

![Prerequiste Forms Analytics Integration](assets/analytics-aem.png)

## Configure Adobe Analytics {#configure-adobe-analytics}

Adobe Analytics is scalable, comprehensive, and easy to integrate and to use in AEM Adaptive Forms, Based on your AEM Forms version, you configure and integrate:

* [Adobe Analytics for Foundation Components](#integrate-adobe-analytics-with-aem-forms-for-foundation-component)
* [Adobe Analytics for Core Components](#integrate-adobe-analytics-with-aem-forms-for-core-components)

### Integrate Adobe Analytics with AEM Forms for Foundation Component {#integrate-adobe-analytics-with-aem-forms-for-foundation-component}

1. On your AEM instance, Go to **[Forms]** >> **[Forms and Document]** and select you Form. 
1. Create a configuration container for cloud services:
    1. Go to **[!UICONTROL Tools > General > Configuration Browser]**.
    1. Select a folder or create a folder, and enable the folder for **[!UICONTROL Cloud Configurations]**.
    1. Tap **[!UICONTROL Save & Close]** to save the configuration and exit the dialog.
1. Select **[Forms]** >> **[Properties]**.
1. Select the folder that you created in **[Configuration Browser]** in the **[Configuration Container]** section.
1. Select the Task Panel on the Left Rail and click **Setup Analytics** and **Activate Adobe Analytics**.
1. Provide the name that you prefer for the report suite, Click **[!UICONTROL Next]** and **[!UICONTROL Save]**.
1. Once you save the project, the setup runs for sometime till installation and integration of Fast Track Analytics with your AEM Forms, you can also check the **integration status**.

    >[!NOTE] 
    >
    >If your installation does not set up in sometime, retry. If the issue still persists, you can connect to the Support team.

* Navigate to your form, and you see that Adobe Analytics is integrated to your form as shown in the image.

![Integrated AEM Analytics](assets/analytics-aem-integrated.png)

### Integrate Adobe Analytics with AEM Forms for Core Components {#integrate-adobe-analytics-with-aem-forms-for-core-components}

1. On your AEM instance, Go to **[Forms]** >> **[Forms and Document]** and select you Form. 
1. Select the Task Panel on the Left and click **Setup Analytics** and **Activate Adobe Analytics**.
1. Provide the name that you prefer for the report suite, Click **[!UICONTROL Next]** and **[!UICONTROL Save]**.
1. Once you save the project, the setup runs for sometime till installation and integration of Fast Track Analytics with your AEM Forms, you can also check the integration status.

    >[!NOTE] 
    >
    >If your installation does not set up in sometime, retry. If the issue still persists, you can connect to the Analytics Support team.

1. Navigate to your form, and you see that Adobe Analytics is integrated to your form.