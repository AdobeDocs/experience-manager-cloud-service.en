---
title: Integrate Adobe Analytics to AEM Forms with Experience Cloud Setup Automation
description: Experience Cloud Setup Automation helps to connect Adobe Analytics to AEM Forms. It helps in tracking and analyzing user interaction with AEM Forms, offering insights into visitor interactions and engagement.
---

# Integrate Adobe Analytics to AEM Forms with Experience Cloud Setup Automation {#integrate-adobe-analytics-to-aem-forms-with-experience-cloud-setup-automation}

Experience Cloud Setup Automation helps to connect Adobe Analytics to AEM Forms, Adobe Analytics aids in tracking and analyzing user interaction with AEM Forms, offering insights into visitor interactions and engagement. Experience Cloud Setup Automation also helps monitoring form performance which involves assessing metrics like completion times and drop-off points. This analysis helps optimize forms for better user experience while distinguishing user behavior based on login status, for example, anonymous users, to identify general trends and patterns.

## Advantages of integrating Adobe Analytics with AEM Forms {#advantages-of-integrating-adobe-analytics-with-aem-forms}

* **Insights into end-user behavior**: Adobe Analytics helps to get insights about end-user behavior,  reveals user actions, drop-offs, and completion rates, enabling a deeper understanding of how individuals engage with forms.
* **Enabling non-technical business users to gain insights**: Adobe Analytics through its easy to use interface empowers even non-technical users to access and interpret form usage data, fostering data-driven decisions for enhancing enrollment experiences.
* **Optimizing data capture experience based on usage**: Organizations can identify pain points in data capture, leading to targeted improvements that enhance form usability and increase successful submissions.

## Scope of Adaptive Forms usage metrics {scope-of-adaptive-forms-usage-metrics}

Adobe Analytics offers a comprehensive array of Adaptive Forms performance metrics designed to provide valuable insights into form usage. These metrics encompass:

* **Form renditions, Form Submissions, Validation Errors, and Unique Visitors**, allowing you to assess the usage and effectiveness of your forms.

* **Visitor Insights** which encompass visit and submission frequencies, and unique visitor counts, offering a comprehensive view of your form audience.

* **Device Type** data which informs you about the devices users employ to access your forms.

* **Geographical Breakdown** that reveals the regional distribution of your form users.

* **Traffic Sources** and **Popular Forms** metrics which consist of the top referring domains and most-visited forms, helping you understand where your traffic originates and which forms are the most popular.

* **User Activity on Top Forms** that provides insights into field visits, form renditions, validation errors, abandoned forms, and form submissions, allowing you to analyze user behavior.

* **Timeline for Time Spent on Forms** which offers a timeline-based view of user engagement with your forms.

* **Areas Requiring Visitor Assistance** metrics which include help views, validation error instances, and field visit frequencies, highlighting where users may need assistance in filling out forms.

![Analytics Report](assets/analytics-report.png)


For a detailed information about each metric, visit [Viewing and Understanding AEM Forms Analytics Reports](https://experienceleague.adobe.com/docs/experience-manager-65/forms/integrate-aem-forms-with-experience-cloud-solutions/view-understand-aem-forms-analytics-reports.html)

## Prerequisites {#prerequisites}

Experience Cloud Setup Automation in Adobe Experience Manager Forms requires an Adobe Analytics license, Data Collection (Formerly Adobe Launch) to manage tracking scripts, and integration with the Experience Platform Launch API for streamlined data aggregation and insights generation.

<!-- 

When you have access to the above applications, you can visit the developer console and search your project with the program id and author id of your AEM instance, and ensure that you have Experience Cloud Setup Automation, Adobe Analytics, and Experience Platform Launch API are included in the corresponding AEM developer console as shown in the image below.

![Prerequiste Forms Analytics Integration](assets/analytics-aem.png)

-->

>[!NOTE]
> If you an active license for Experience Cloud Setup Automation, Adobe Analytics, and Experience Platform Launch API, you must ensure it is available in your developer console. For more information about your available integrations, see [troubleshooting AEM Forms with Analytics Integration]().

## Configure Adobe Analytics {#configure-adobe-analytics}

Perform the below listed steps to enable and configure Adobe Analytics for your Adaptive Forms:

* [Enable Adobe Analytics for Adaptive Forms based on Foundation Components](#integrate-adobe-analytics-with-aem-forms-for-foundation-component)
* [Enable Adobe Analytics for Adaptive Forms based on Core Components](#integrate-adobe-analytics-with-aem-forms-for-core-components)

### Integrate Adobe Analytics with AEM Forms for Foundation Component {#integrate-adobe-analytics-with-aem-forms-for-foundation-component}

1. On your AEM instance, Go to **[Forms]** >> **[Forms and Document]** and select your Form.
1. Create a configuration container for cloud services:
    1. Go to **[!UICONTROL Tools > General > Configuration Browser]**.
    1. Select or create a Configuration Container, and enable the folder for **[!UICONTROL Cloud Configurations]**.
    1. Tap **[!UICONTROL Save & Close]** to save the configuration and exit the dialog.
1. Select your **[!UICONTROL Form]** >> **[!UICONTROL Properties]**, In the **[!UICONTROL Configuration Container]**, select the configuration container that you created or selected in the **[!UICONTROL Configuration Browser]** in Step 2.
1. Select the Task Panel on the Left Rail and click **Setup Analytics** and **Activate Adobe Analytics**.
1. Provide the name that you prefer for the report suite, Click **[!UICONTROL Next]** and **[!UICONTROL Save]**.
1. Once you save the project, the setup runs for sometime till installation and integration of Adobe Analytics with your AEM Forms, you can also check the **integration status**.

    >[!NOTE] 
    >
    >If your installation does not set up in sometime, retry. If the issue still persists, you can connect to the Support team.

* Navigate to your form, and you see that Adobe Analytics is integrated to your form as shown in the image.

![Integrated AEM Analytics](assets/analytics-aem-integrated.png)

### Integrate Adobe Analytics with AEM Forms for Core Components {#integrate-adobe-analytics-with-aem-forms-for-core-components}

1. On your AEM instance, Go to **[!UICONTROL Forms]** >> **[!UICONTROL Forms and Document]** and select your Form.
1. Select the Task Panel on the Left and click **Setup Analytics** and **Activate Adobe Analytics**.
1. Provide the name that you prefer for the report suite, Click **[!UICONTROL Next]** and **[!UICONTROL Save]**.
1. Once you save the project, the setup runs for sometime till installation and integration of Adobe Analytics with your AEM Forms, you can also check the **integration status** while installation.

    >[!NOTE] 
    >
    >If your installation does not set up in sometime, retry. If the issue still persists, you can connect to the Support team.

1. Navigate to your form, and you see that Adobe Analytics is integrated to your form.