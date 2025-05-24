---
title: Translate and localize an Edge Delivery Services for AEM Forms
description: Translate and localize an Edge Delivery Services for AEM Forms
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
exl-id: 8a0c826f-8acc-4a00-bd84-7b0df9a82457
role: Admin, Architect, Developer
---

# Translate and localize an Edge Delivery Services for AEM Forms

In Edge Delivery Services, form translation involves converting form content from one language to another with a focus on accuracy, clarity, and consistency. Translated or localized forms enable broader audience reach across different geographical locations, thus enhancing user experience and facilitating better communication across diverse language preferences. 


By the end of the article, you learn to:

* [Translate forms within Google Drive](#translate-form-google-drive)
* [Translate forms within SharePoint Site](#translate-form-sharepoint)

## Translate forms within Google Drive {#translate-form-google-drive}

The `GOOGLETRANSLATE` function at Google sheets translates forms by tapping into built-in translation tool, changing text from one language to another directly within a Google sheet. To translate forms within Google Drive:

1. Go to your AEM Project folder on Google Drive and open your Google sheet. 
2. Rename the existing sheet (`shared-default`) to `shared-en`.
3. Add a sheet named `shared-default`. The `shared-default` sheet contains the content for localization to a specific language.
4. Add the  localized content in the `shared-default` sheet using the `GOOGLETRANSLATE` function. 
   You can use a formula to translate the content of cell D2 from the `shared-en` sheet into French within the `shared-default` sheet. Here is the formula to use:
   `=GOOGLETRANSLATE('shared-en'!D2,"en","fr")`

    ![Enquiry Translate spreadsheet](/help/forms/assets/translate-enquiry-spreadsheet.png)

5. Preview and publish the sheet using [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content). 

You can refer to the [spreadsheet](/help/forms/assets/enquirytranslate.xlsx) containing the form definition for an `enquiry` form translated from English to French language.

![Enquiry Translated Form](/help/forms/assets/translate-form-french.png)

Refer to the URL below, where you can view the form with its French language translation:
https://main--portal--wkndforms.hlx.live/enquirytranslate

## Translate forms within SharePoint Site{#translate-form-sharepoint}

To translate the forms on the Microsoft&reg; SharePoint site, you need to manually change the labels of the fields using any translation service. To translate the forms within SharePoint Site:

1. Go to your AEM Project folder on Microsoft&reg; SharePoint and open your spreadsheet. 
2. Rename the existing sheet (`shared-default`) to `shared-en`.
3. Add a sheet named `shared-default`. The `shared-default` sheet contains the content for localization to a specific language.
4. Add the  localized content in the `shared-default` sheet manually. 
    
      ![Enquiry Translate spreadsheet](/help/forms/assets/translate-enquiry-sp-spreadsheet.png)

5. Preview and publish the sheet using [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content). 

Refer to the [spreadsheet](/help/forms/assets/enquirytranslate-sp.xlsx) containing the form definition for an `enquiry` form translated from English to French language.

![Enquiry Translated Form](/help/forms/assets/translate-form-french.png)

Refer to the URL below, where you can view the form with its French language translation:
https://main--wefinance--wkndforms.hlx.live/enquirytranslate 

## Known issues {#known-issues}

* The labels of the form get translated to the specified localized language in the `shared-default` sheet, but the error messages are displayed in the default language of the browser.

    ![Error message](/help/forms/assets/translate-error-message.png)

* When you open the calendar, the calendar drop-down is displayed in the default language of the browser.

    ![Error message](/help/forms/assets/translate-calender-display.png)


## Frequently asked questions {#faq}

**Q**: How can I type input in the specified localized language in a form?

**A**: To input text in a specific localized language, adjust the keyboard settings on your device. Refer to the following links for instructions on how to do it:

  * [Set up your Mac to take input in another language](https://support.apple.com/en-in/guide/mac-help/mchlp1406/mac)
  * [Set up your Windows to take input in another language](https://support.microsoft.com/en-us/windows/manage-the-input-and-display-language-settings-in-windows-12a10cb4-8626-9b77-0ccb-5013e0c7c7a2#:~:text=Select%20the%20Start%20%3E%20Settings%20%3E%20Time,you%20want%2C%20then%20select%20Options)
  * [Set up your Android or iPhones/iPads to take input in another language](https://support.google.com/gboard/answer/7068494?hl=en&co=GENIE.Platform%3DAndroid)


**Q**: How can I retrieve a list of locales used in the `GOOGLETRANSLATE` function?

**A**: You can refer to the [official documentation of Google](https://cloud.google.com/translate/docs/languages) for a comprehensive list of locales used in the GOOGLETRANSLATE.

## See also

{{see-more-forms-eds}}

