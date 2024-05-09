---
title: How can we translate a Core Components based Adaptive Form?
description: Learn to create a Form Data Model (FDM) in AEM Forms, test the model with sample data and services, and configure various option for a model.
feature: Adaptive Forms, Core Components
exl-id: ad46bf0f-e6ec-4c52-9695-5768a9968e16
---
# Use machine translation or human translation to translate a Core Components based Adaptive Form {#using-aem-translation-workflow-to-localize-adaptive-forms-and-document-of-record}

Localized forms help you serve a wider audience across geographies. Adobe Experience Manager translation workflow helps you localize Adaptive Forms and their documents of record . You can use **machine translation** or **human translators** to localize an Adaptive Form.

## Translate an Adaptive Form and document of record using machine translation {#localizing-an-adaptive-form-and-document-of-record-using-machine-translation}

The machine translation service immediately translates your content in Adaptive Form and [Document of Record](/help/forms/generate-document-of-record-core-components.md). AEM Forms as a Cloud Service is pre-configured to use a trial version of Microsoft Translator for machine translation. Perform the following steps to enable machine translation for your Adaptive Forms and Document of Record:

1. On the AEM Forms UI, select a form, and select the **[!UICONTROL Add Dictionary]** option.
1. In the Add Dictionary to Translation Project screen, for the **[!UICONTROL Project]** option 

   * To create a translation project, select the **[!UICONTROL Create a new translation project]** option and in the **Project Title** field, specify the title. For example, `Government Reference Site - German locale.`
   * To add a new dictionary to an existing translation project, select the **[!UICONTROL Add to an existing translation project]** option and select an **[!UICONTROL Existing translation project]**. 
1. In the **Target Languages** field, specify a locale (For example, `German(de)`). You can specify multiple locales. The form is translated to all the locales specified in the **Target Languages** field. Click **Done**.
1. In the Dictionary Added dialog box, click **Open Projects**. 
1. In the Projects screen, click the created project. For example, click the **Government Reference Site - German locale** tile.
1. On the **Translation Job** tile, click the ![aem62forms_downarrow](assets/aem62forms_downarrow.png) icon, and click **Start**. The status of the tile changes to Draft. On completion of the translation, the status changes to **Approved**. Refresh the page after a few minutes and verify the status.

      ![Start Translation](/help/forms/assets/adaptive-forms-core-components-start-translation.png)
1. After the status changes to **Approved** on the **Translation Job** tile, click the ![aem62forms_downarrow](assets/aem62forms_downarrow.png) icon, and click **Complete**.

1. To preview the localized form, on the AEM Forms UI, select the localized form. Click **[!UICONTROL Preview]** >**[!UICONTROL Preview as HTML]**. Reopen the form after adding the `afAcceptLang=<locale code>` to the URL off the form. For example, add `afAcceptLang=de`to open German version of the form. 


   >[!NOTE]
   >
   >* Before opening the localized version of form in the browser window, ensure that the locale of the browser is set to match the locale of the form. For example, if the form is translated to German(de) language then set the locale of the browser to German(de).
   >* Adaptive form components do not support right to left (RTL) languages. For example, Hebrew.

<!-- 
   Along with the Adaptive form, the auto-generated document of record is also localized.

   For more information on Document of Record settings and configuration, see:

   [Document of Record Template](/help/forms/using/generate-document-of-record-for-non-xfa-based-adaptive-forms.md#p-document-of-record-template-configuration-p)

   [Document of Record settings](/help/forms/using/generate-document-of-record-for-non-xfa-based-adaptive-forms.md#p-document-of-record-settings-p)

1. [Customize the branding information of the document of record](/help/forms/using/generate-document-of-record-for-non-xfa-based-adaptive-forms.md) and ensure that the browser locale is set to the same language to which you have localized the Adaptive Form using machine language. The browser locale helps localize the branding information in the document of record.
1. To view the localized document of record, select Generate Preview. The document of record PDF is generated and opened in a new tab in your browser.

-->

## Localizing an adaptive form and its document of record using Human Translation {#localizing-an-adaptive-form-and-its-document-of-record-using-human-translation}

In Human translation the content is sent to a translation provider and translated by professional translators. When complete, the translated content is returned and imported into AEM. When your translation provider is integrated with AEM, content is automatically sent between AEM and the translation provider.

For translation, a dictionary containing files in XLIFF format is shared with the professional translators. The dictionary includes a separate XLIFF file for each locale. Each XLIFF file contains text that is displayed to the end users and placeholders for the corresponding localized text.

Perform the following steps to localize a form and its document of record using Human Translators:

1. On the AEM Forms UI, select a form, and select the **[!UICONTROL Add Dictionary]** option.
1. In the Add Dictionary to Translation Project screen, for the **[!UICONTROL Project]** option 

   * To create a translation project, select the **[!UICONTROL Create a new translation project]** option and in the **Project Title** field, specify the title. For example, `Government Reference Site - German locale.`
   * To add a new dictionary to an existing translation project, select the **[!UICONTROL Add to an existing translation project]** option and select an **[!UICONTROL Existing translation project]**. 
1. In the **Target Languages** field, specify a locale (For example, `German(de)`). You can specify multiple locales. The form is translated to all the locales specified in the **Target Languages** field. Click **Done**.
1. In the Dictionary Added dialog box, click **Open Projects**. 
1. In the Projects screen, click the created project. For example, click the **Government Reference Site - German locale** tile. 
1. At the bottom of the **Summary** tile, click the **ellipses**. The Translation Project Properties screen opens.
1. Open the **[!UICONTROL Advanced]** tab  at the top of the **Translation Project Properties** screen. For the **[!UICONTROL Translation field]**, select **[!UICONTROL Human Translation]**. Click **Save & Close** at the top of the screen.
1. On the **Translation Job** tile, click the ![aem62forms_downarrow](assets/aem62forms_downarrow.png) icon, and click **Export**. On the Export dialog, click the Download Exported File option. It downloads a .zip file. 
   ![Export translation file](/help/forms/assets/adaptive-forms-core-components-start-translation-export.png)
1. Extract the downloaded .zip file. The extracted folder has two files:
   * translation_export_summary.xml
   * [form-fields-file].xml.
1. Open the [form-fields-file].xml for editing. Add the localized strings and messages for form fields. Save and close the file.
1. Zip the files the translation_export_summary.xml and [form-fields-file].xml.
1. On the **Translation Job** tile, click the ![aem62forms_downarrow](assets/aem62forms_downarrow.png) icon, and click **Import**. Select the archive containing [form-fields-file].xml. with localized strings and messages for form fields.

   ![Import translation file](/help/forms/assets/adaptive-forms-core-components-start-translation-import.png)

1. To preview the localized form, on the AEM Forms UI, select the localized form. Click **[!UICONTROL Preview]** >**[!UICONTROL Preview as HTML]**. Reopen the form after adding the `afAcceptLang=<locale code>` to the URL off the form. For example, add `afAcceptLang=de`to open German version of the form.

## See Also {#see-also}

{{see-also}}