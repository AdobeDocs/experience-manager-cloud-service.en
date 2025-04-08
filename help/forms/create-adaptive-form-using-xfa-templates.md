---
title: How to create an Adaptive Form based on Core Components using XFA form templates?
description: Learn how to create an Adaptive Form using [!DNL Experience Manager Forms] using XFA form templates or XDP files.
feature: Adaptive Forms, Core Components
role: User, Developer
level: Beginner
exl-id: f3c9b798-8b20-4674-9b96-a3a0b143d947
---
# Create an Adaptive Form (Core Components) based on XFA Form templates

<span class="preview"> The feature is available under early adopter program. You can write to aem-forms-ea@adobe.com from your official email id to join the early adopter program and request access to the capability. </span>

AEM as a Cloud Service provides users with the option to create Adaptive Forms based on Core Components using XFA (XML Forms Architecture) form templates or `*.XDP` (XML Data Package) files. This feature allows users to save time by migrating fields from XFA form template or XDP files files directly into Adaptive Forms. 

You can repurpose your XFA form template or XDP files form templates to create Adaptive Forms based on Core Components. To repurpose, upload and associate an XFA form template or XDP files with an Adaptive Form. The elements of the XFA form template or XDP files become available for use in the content finder during Adaptive Form authoring. From the Content Finder, you can drag and drop the form template elements onto the form.

## Adavantages of creating forms based on XFA Form templates or XDP files

Few of the advantages of creating forms based on XFA form templates or XDP files are:

* **Time savings**: You can quickly reuse existing XFA form templates (XDP files) without needing to recreate the form structure, saving time and effort during the authoring process.
* **Effortless migration**: If you already have XFA form templates in use, this option provides an easy migration path to Adaptive Forms, allowing you to take advantage of the benefits of modern AEM Core Components without losing existing form data and logic.
* **Improved user experience**: Adaptive Forms are more responsive and customizable than XFA forms. By transitioning to Adaptive Forms, you can ensure a more user-friendly experience across different devices and screen sizes.
* **Enhanced integration**: Adaptive Forms integrate better with other features, such as workflows, data binding, and form submissions, enabling smoother workflows and better overall form management.

## Pre-requisites

You require the following to create an Adaptive Form based on Core Components using XFA form templates or XDP files:

* [Enable Adaptive Forms Core Components for your environment](enable-adaptive-forms-core-components.md).
* Familiarity with the following areas is recommended:
    * Creating an adaptive form
    * XFA (XML Forms Architecture)

## How to create an Adaptive Form using an XFA Form templates or XDP files?

Perform the following steps to create an Adaptive Form using XFA or XDP form templates:

1. Log in to your [!DNL Experience Manager Forms] author instance. 
1.  Enter your credentials on the Experience Manager login page. After you are logged in, in the upper-left corner, select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.

    ![Forms and Documents](/help/forms/assets/create-fdm.png)

1. Select **[!UICONTROL Create]**  &gt; **[!UICONTROL Adaptive Forms]**. 
  
    ![Create Adaptive Form](/help/forms/assets/create-af.png)

    The Form creation wizard opens. 
1. In the **Source** tab, select a template based on Core Components.

     ![Select template](/help/forms/assets/select-template.png)

    When you select a template, a theme and submit action specified in the template are auto-selected, and the **[!UICONTROL Create]** button is enabled.

     ![Select theme](/help/forms/assets/select-form-theme.png)

1.  Select **[!UICONTROL Create]**. A dialog to specify title, name, and location to save the Adaptive Form appears. 
1. Specify its title, name and location.
1. Select **[!UICONTROL Create]**.
    ![Provide name and title](/help/forms/assets/create-form.png)        

    An Adaptive Form is created and opens in the Adaptive Forms editor. The editor displays the contents available in the template.
1.  Select ![Page information](/help/forms/assets/Smock_Properties_18_N.svg) > **[!UICONTROL Open Properties]**. 

    ![Open properties](/help/forms/assets/form-properties.png)

    The Form Properties page opens. 
1.  Go to the **[!UICONTROL Form Model]** tab and choose **Form Templates**. 
1. Select the .xdp file from the dropdown list.

    ![Select XDP file](/help/forms/assets/select-xdp-file.png)

    A warning dialog box appaers on screen. Click **OK** to proceed further.

    ![Warning Dialog](/help/forms/assets/fdm-warning.png)

1.  Select **[!UICONTROL Save & Close]** to save the properties.

    >[!NOTE]
    >
    > After selecting **Form Templates** in the Form **Model** tab, it cannot be changed.


An Adaptive Form is created and opens in the Adaptive Forms editor. The editor displays the contents available in the template.  Based on the type of Adaptive Form, the form elements present in the associated XFA form template are displayed in the **[!UICONTROL Data Model Objects]** tab of the **[!UICONTROL Content Browser]** in the sidebar. You can also drag-drop these elements to build your Adaptive Form.

>[!NOTE]
>
> You can disable scripts for XDP form fields using the panel toolbar of the added field. Create logics for the added fields using the [Visual Rule Editor](/help/forms/rule-editor-core-components.md).   

## See also

{{see-also}}
* [Add dynamic behavior to forms using the rule editor](/help/forms/rule-editor-core-components.md)
