---
title: How to customize auto-generated Document of Record template for Adaptive Forms?
description: Learn how to download, customize, and re-upload the auto-generated Document of Record (DoR) template for Adaptive Forms using Adobe Forms Designer.
feature: Adaptive Forms, Core Components, Foundation Components
role: User, Developer
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: 2416add3-0b9d-4a8d-a84d-d65c0762d8e8
---
# Customize the auto-generated Document of Record template

<span class="preview"> This article applies to both **Core Components** and **Foundation Components** based Adaptive Forms.</span>

When you auto-generate a Document of Record (DoR) for an Adaptive Form, AEM Forms creates a default template based on the form structure. You can customize this auto-generated template to match your organization's branding and layout requirements.

The customization workflow involves three steps:

1. Download the auto-generated DoR template from Forms Manager.
1. Modify the template using Adobe Forms Designer.
1. Re-upload the customized template to AEM Forms and configure it as a custom template.

## Prerequisites {#prerequisites}

Before you start, ensure you have the following:

* Access to AEM Forms Manager with permissions to download and upload templates.
* Adobe Forms Designer installed on your local machine.
* An Adaptive Form with **[!UICONTROL Generate Document of Record]** enabled.

## Step 1: Download the auto-generated DoR template {#download-auto-generated-dor-template}

To download the auto-generated DoR template (XDP file) for your Adaptive Form:

1. Log in to your AEM Forms author instance.
1. Navigate to **[!UICONTROL Forms]** > **[!UICONTROL Forms and Documents]**.
1. Select the Adaptive Form for which you want to download the DoR template.
1. Open the properties of the selected Adaptive Form.
1. In the properties panel, select the **[!UICONTROL Download Document of Record]** option to download the auto-generated DoR template (XDP file).
1. Save the downloaded XDP file to your local machine.


## Step 2: Customize the template using Adobe Forms Designer {#customize-template-using-designer}

Open the downloaded XDP template in Adobe Forms Designer and modify it to suit your organization's needs.

1. Open the downloaded XDP file in **Adobe Forms Designer**.
1. Customize the template as required. Examples of customizations include:

   * **Multiple master pages**: Add additional master pages to define different layouts for specific pages of the Document of Record. For example, use a distinct first page with a company letterhead and subsequent pages with a simpler layout.
   * **Font colors and font families**: Change the font color, size, and family to align with your corporate brand guidelines.
   * **Custom elements**: Add elements such as company logos, headers, footers, and disclaimer text to establish a consistent brand identity.
   * **Page layout and styling**: Adjust margins, spacing, and the overall page structure to improve readability.
   * **Field styling and positioning**: Modify the appearance and position of form fields to match your preferred layout.

1. Save the customized XDP template.

>[!NOTE]
>
> Do not remove or modify any scripts present in the template. Modifying scripts can affect the data binding and Document of Record generation.

## Step 3: Re-upload the customized template to AEM {#reupload-customized-template}

After you customize the template, upload it to AEM Forms and configure the Adaptive Form to use it.

1. Upload the customized XDP template to your AEM Forms instance:
   * Navigate to **[!UICONTROL Forms]** > **[!UICONTROL Forms and Documents]**.
   * Select **[!UICONTROL Create]** > **[!UICONTROL File Upload]** and upload the customized XDP file.

Then configure the form to use the custom template. The steps differ depending on whether your form is based on Core Components or Foundation Components.

>[!BEGINTABS]

>[!TAB Core Components]

For Adaptive Forms based on Core Components:

1. Open the Adaptive Form in the editor for which you want to apply the custom template.
1. In the content tree, select the **[!UICONTROL Guide Container]** (root panel).
1. Open **[!UICONTROL Properties]** and click the **[!UICONTROL Document of Record]** (DoR) icon to open Document of Record properties.
1. In the **[!UICONTROL Basic]** tab, open the **[!UICONTROL Template]** dropdown and select **[!UICONTROL Custom]**.
1. Browse and select the uploaded customized XDP template.
1. Select the checkmark to save.

   ![Document of Record properties - Template set to Custom (Core Components)](/help/forms/assets/submission-pdf-dor-custom-template.png)

>[!TAB Foundation Components]

For Adaptive Forms based on Foundation Components:

1. Open the Adaptive Form in the editor for which you want to apply the custom template.
1. Select the root panel (form container).
1. Open **[!UICONTROL Document of Record Properties]** (from the properties panel or the DoR tab).
1. In the **[!UICONTROL Basic]** tab, open the **[!UICONTROL Template]** dropdown and select **[!UICONTROL Custom]**.
1. Browse and select the uploaded customized XDP template.
1. Select **[!UICONTROL Done]** to save.

   ![Document of Record properties - Template set to Custom (Foundation Components)](/help/forms/assets/dor-custom-template-foundation-components.png)

>[!ENDTABS]

The Adaptive Form now uses the customized template when generating the Document of Record.

## Verify the customized template {#verify-customized-template}

To confirm that the customized template is applied correctly:

1. Submit a test entry for the Adaptive Form.
1. Generate the Document of Record.
1. Verify that the generated PDF reflects your customizations, including logos, fonts, layout changes, and other branding elements.

## Troubleshooting {#troubleshooting}

| Issue | Resolution |
|---|---|
| The customized template does not upload. | Ensure the XDP file is valid and not corrupted. Verify that you have the required permissions to upload files to AEM Forms. |
| Customizations do not appear in the generated Document of Record. | Confirm that you selected the correct customized template in the **[!UICONTROL Document of Record Template Configuration]** section of the form properties. |
| Layout or formatting issues in the generated PDF. | Verify that the customizations in Adobe Forms Designer follow the [base template conventions](/help/forms/generate-document-of-record-core-components.md#base-template-conventions). Ensure all elements are properly positioned within the template structure. |

## See Also {#see-also}

* [Generate Document of Record for Adaptive Forms (Core Components)](/help/forms/generate-document-of-record-core-components.md)
* [Generate Document of Record for Adaptive Forms (Foundation Components)](/help/forms/generate-document-of-record-for-non-xfa-based-adaptive-forms.md)
* [Base template of a Document of Record](/help/forms/generate-document-of-record-core-components.md#base-template-of-a-document-of-record)
* [Customize the branding information in Document of Record](/help/forms/generate-document-of-record-core-components.md#customize-the-branding-information-in-document-of-record)
