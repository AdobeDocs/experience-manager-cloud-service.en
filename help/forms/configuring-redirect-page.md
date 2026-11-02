---
title: How to Configure a Redirect Page?
description: Learn how users can be redirected to a webpage that form authors can configure while creating the form.
feature: Adaptive Forms, Foundation Components
role: User, Developer
level: Intermediate
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: e4dc01d2-7c89-4bd8-af0a-1d2df4676a9a
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
---
# Configuring redirect page {#configuring-redirect-page}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/configuring-redirect-page.html)                  |
| AEM as a Cloud Service     | This article         |

Form authors can configure a page for each form, to which the form users are redirected after submitting a form.

1. In the edit mode, select a component, then click ![field-level](assets/select_parent_icon.svg) &gt; **[!UICONTROL Adaptive Form Container]**, and then click ![cmppr](assets/configure-icon.svg).

1. In the sidebar, click **[!UICONTROL Submission]**.  

1. Provide the URL of the redirect page under **[!UICONTROL Redirect URL/Path]** in the **[!UICONTROL Submission]** section.  
1. Optionally, under Submit Action, for the Submit to REST endpoint action, you can configure the parameter to be passed to the redirect page.

   ![Redirect page configuration](assets/redirect-url.png)

   Redirect page configuration

Form authors can use the following parameters that are passed to the Thank you page. For all the available Submit Actions, `status` and `owner` parameters are passed. Besides these two parameters, some additional parameters are passed for the following Submit Actions:

* **[!UICONTROL Submit to REST endpoint]**: Parameters added for in-field to parameter mapping are passed. `status` and `owner` parameters are not passed in this Submit Action. For more information, see [Configuring the Submit to REST endpoint Submit Action](configuring-submit-actions.md).

>[!MORELIKETHIS]
>
>* [Configure a Redirect Page or thank you message](/help/forms/configure-redirect-page-or-thank-you-message.md)
