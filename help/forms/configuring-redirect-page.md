---
title: How to Configure a Redirect Page?
description: Learn how users can be redirected to a webpage that form authors can configure while creating the form.
feature: Adaptive Forms
role: User
level: Intermediate
exl-id: e4dc01d2-7c89-4bd8-af0a-1d2df4676a9a
---
# Configuring redirect page {#configuring-redirect-page}

Form authors can configure a page for each form, to which the form users are redirected after submitting a form.

1. In the edit mode, select a component, then click ![field-level](assets/select_parent_icon.svg) &gt; **[!UICONTROL Adaptive Form Container]**, and then click ![cmppr](assets/configure-icon.svg).

1. In the sidebar, click **[!UICONTROL Submission]**.  

1. Provide the URL of the redirect page under **[!UICONTROL Redirect URL/Path]** in the **[!UICONTROL Submission]** section.  
1. Optionally, under Submit Action, for the Submit to REST endpoint action, you can configure the parameter to be passed to the redirect page.

   ![Redirect page configuration](assets/redirect-url.png)

   Redirect page configuration

Form authors can use the following parameters that are passed to the Thank you page. For all the available Submit Actions, `status` and `owner` parameters are passed. Besides these two parameters, some additional parameters are passed for the following Submit Actions:

* **[!UICONTROL Submit to REST endpoint]**: Parameters added for in-field to parameter mapping are passed. `status` and `owner` parameters are not passed in this Submit Action. For more information, see [Configuring the Submit to REST endpoint Submit Action](configuring-submit-actions.md).
