---
title: Enable Adobe Analytics for an Adaptive Form using Experience Cloud Setup Automation
description: Experience Cloud Setup Automation helps to connect Adobe Analytics to an Adaptive Form. It helps in tracking and analyzing user interaction with an Adaptive Form, offering insights into visitor interactions and engagement.
---

# Enable Adobe Analytics for an Adaptive Form using Experience Cloud Setup Automation {#integrate-adobe-analytics-to-aem-forms-with-experience-cloud-setup-automation}

Experience Cloud Setup Automation helps to connect Adobe Analytics to Adaptive Forms which aids in tracking and analyzing user interaction with your forms and offering insights into visitor interactions and engagement. Experience Cloud Setup Automation also helps monitoring form performance which involves assessing metrics like completion times and drop-off points. This analysis helps optimize forms for better user experience while distinguishing user behavior based on login status, for example, anonymous users, to identify general trends and patterns.

## Advantages of integrating Adobe Analytics with Adaptive Forms {#advantages-of-integrating-adobe-analytics-with-aem-forms}

* **Insights into end-user behavior**: Adobe Analytics helps to get insights about end-user behavior,  reveals user actions, drop-offs, and completion rates, enabling a deeper understanding of how individuals engage with forms.
* **Enabling non-technical business users to gain insights**: Adobe Analytics through its easy to use interface empowers even non-technical users to access and interpret form usage data, fostering data-driven decisions for enhancing enrollment experiences.
* **Optimizing data capture experience based on usage**: Organizations easily identify pain points in data capture, leading to targeted improvements that enhance form usability and increase successful submissions.

## Scope of Adaptive Forms usage metrics {#scope-of-adaptive-forms-usage-metrics}

Adobe Analytics offers a comprehensive array of Adaptive Forms performance metrics designed to provide valuable insights into form usage. These metrics are:

* **Form renditions, Form submissions, Validation errors, and Unique visitors**, allowing you to assess the usage and effectiveness of your forms.

* **Visitor insights** which encompass visit and submission frequencies, and unique visitor counts, offering a comprehensive view of your form audience.

* **Device type** data which informs you about the devices users employ to access your forms.

* **Geographical breakdown** reveals the regional distribution of your form users.

* **Traffic sources** and **Popular forms** metrics which consist of the top referring domains and most-visited forms, help you understand where your traffic originates and which forms are the most popular.

* **User activity on top forms** provides insights into field visits, form renditions, validation errors, abandoned forms, and form submissions, allowing you to analyze user behavior.

* **Timeline for time spent on forms** which offers a timeline-based view of user engagement with your forms.

* **Areas requiring visitor assistance** metrics which include help views, validation error instances, and field visit frequencies, highlighting where users may need assistance in filling out forms.

![Analytics Report](assets/analytics-report.png)


For a detailed information about each metric, visit [Viewing and Understanding AEM Forms Analytics Reports](/help/forms/view-understand-aem-forms-analytics-reports.md)

## Prerequisites {#prerequisites}

<!--
Analytics, Data Collection (Formerly Adobe Launch), and Experience Manager (experience.adobe.com)
-->

Experience Cloud Setup Automation in Adobe Experience Manager Forms requires an **Adobe Analytics license**, **Data Collection (Formerly Adobe Launch)** to manage tracking scripts, and integration with the **Experience Platform Launch (API)** for streamlined data aggregation and insights generation.

If you have an active license for Experience Cloud Setup Automation, Adobe Analytics, and Experience Platform Launch API, you should verify their availability within your developer console.

To verify the aforementioned licenses is available, visit the developer console and search your project with the project id, for example, as shown in the image as `AEM-p53584-e979139` and ensure that you have Experience Cloud Setup Automation, Adobe Analytics, and Experience Platform Launch API.

![Prerequiste Forms Analytics Integration](assets/analytics-aem.png)

<!-- 
>[!NOTE]
> If you have an active licenses for Experience Cloud Setup Automation, Adobe Analytics, and Experience Platform Launch API, you should verify their availability within your developer console.
-->

<!-- For more information about your available integrations, see [troubleshooting Adaptive Forms with Analytics Integration](https://experienceleague.adobe.com/docs/experience-manager-65/forms/integrate-aem-forms-with-experience-cloud-solutions/view-understand-aem-forms-analytics-reports.html)
-->

## Configure Adobe Analytics {#configure-adobe-analytics}

Perform the below listed steps to enable and configure Adobe Analytics for your Adaptive Forms:

* [Enable Adobe Analytics for Adaptive Forms based on Foundation Components](#integrate-adobe-analytics-with-aem-forms-for-foundation-component)
* [Enable Adobe Analytics for Adaptive Forms based on Core Components](#integrate-adobe-analytics-with-aem-forms-for-core-components)

### Enable Adobe Analytics with Adaptive Forms for Foundation Component {#integrate-adobe-analytics-with-aem-forms-for-foundation-component}

1. Create a configuration container for cloud services:
    1. Go to **[!UICONTROL Tools > General > Configuration Browser]**.
    1. Select or create a Configuration Container, and enable the folder for **[!UICONTROL Cloud Configurations]**.
    1. Tap **[!UICONTROL Save & Close]** to save the configuration and exit the dialog.
1. On your AEM instance, Go to **[Forms]** >> **[Forms and Document]**.
1. Select your **[!UICONTROL Form]** >> **[!UICONTROL Properties]**, In the **[!UICONTROL Configuration Container]**, select the configuration container that you created or selected in the **[!UICONTROL Configuration Browser]** in Step 1.
1. Select the Task Panel on the Left Rail and click **Setup Analytics** and **Activate Adobe Analytics**.
1. Provide the name that you prefer for the report suite, Click **[!UICONTROL Next]** and **[!UICONTROL Save]**.
1. Once you save the project, the setup runs for some time till the  integration of Adobe Analytics with your Adaptive Form, You can also check the **integration status**.

    >[!NOTE] 
    >
    >If your setup takes longer than 15 minutes, retry the integration steps.

1. On your AEM instance, Go to **[!UICONTROL Forms]** >> **[Forms and Document]** and select your **[!UICONTROL Form]**, you see that Adobe Analytics is integrated to your form as shown in the image below.
1. Now you can view your [Adaptive Form Adobe Analytics report](#view-adobe-analytics-report).

![Integrated AEM Analytics](assets/analytics-aem-integrated.png)

### Enable Adobe Analytics with Adaptive Forms for Core Components {#integrate-adobe-analytics-with-aem-forms-for-core-components}

1. On your AEM instance, Go to **[!UICONTROL Forms]** >> **[!UICONTROL Forms and Document]** and select your **[!UICONTROL Form]**.
1. Select the Task Panel on the Left and click **Setup Analytics** and **Activate Adobe Analytics**.
1. Provide the name that you prefer for the report suite, Click **[!UICONTROL Next]** and **[!UICONTROL Save]**.
1. Once you save the project, the setup runs for some time till the  integration of Adobe Analytics with your Adaptive Form, You can also check the **integration status**.

    >[!NOTE] 
    >
    >If your setup takes longer than 15 minutes, retry the integration steps.

1. On your AEM instance, Go to **[!UICONTROL Forms]** >> **[!UICONTROL Forms and Document]** and select your **[!UICONTROL Form]**, you see that Adobe Analytics is integrated to your form.
1. Now you can view your [Adaptive Form Adobe Analytics report](#view-adobe-analytics-report).

## View Adaptive Forms Adobe Analytics report {#view-adobe-analytics-report}

1. On your AEM instance, Go to **[!UICONTROL Forms]** >> **[!UICONTROL Forms and Document]**.
1. Select your form, you see that Adobe Analytics is integrated as shown on the left, to the Forms activated for Adobe Analytics.

    ![View Report](assets/activ-aa.png)

1. Click **Adobe Analytics** to view your report and analyze performance data.
 