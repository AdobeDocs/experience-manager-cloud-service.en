---
title: Translate and localize an AEM Forms Edge Delivery ServicesForm
description: Translate and localize an AEM Forms Edge Delivery ServicesForm
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
exl-id: 8a0c826f-8acc-4a00-bd84-7b0df9a82457
---

# Translate and localize an AEM Forms Edge Delivery ServicesForm

In Edge Delivery systems, form translation involves converting form content from one language to another with a focus on accuracy, clarity, and consistency. Translated or localized forms enable broader audience reach across different geographical locations, thereby enhancing user experience and facilitating better communication across diverse language preferences. 


By the end of the article, you learn to:

* [Translate forms within Google Drive](#translate-form-google-drive)
* [Translate forms within SharePoint Site](#translate-form-sharepoint)

## Translate forms within Google Drive {#translate-form-google-drive}

The `GOOGLETRANSLATE` function in Google sheets translates forms by tapping into built-in translation tool, changing text from one language to another directly within a Google sheet. To translate forms within Google Drive:

1. Go to your AEM Project folder on Google Drive and open your Google sheet. You can also create new sheet for a form.
1. Add new sheet to your existing Google sheet. 
1. Rename the existing sheet (`shared-default`) to `shared-en` and create a new sheet named `shared-default`. The `shared-default` sheet contains the content for localization to a specific language.
1. Add the  localized content in `shared-default` using the `GOOGLETRANSLATE` function. 
   You can use a formula to translate the content of cell D2 from the `shared-en` sheet into French within the `shared-default` sheet. Here is the formula to use:
   `=GOOGLETRANSLATE('shared-en'!D2,"en","fr")`

    ![Enquiry Translate spreadsheet](/help/forms/assets/translate-enquiry-spreadsheet.png)

1. Preview and publish the sheet using [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content). 

You can refer to the [spreadsheet](/help/forms/assets/enquirytranslate.xlsx) containing the form definition for an `enquiry` form translated from English to French language.

![Enquiry Translated Form](/help/forms/assets/translate-form-french.png)

Refer to the URL below, where you can view the form with its French language translation:
https://main--portal--wkndforms.hlx.live/enquirytranslate 

## Translate forms within SharePoint Site{#translate-form-sharepoint}

To translate the forms on the Microsoft® SharePoint site, you need to manually change the labels of the fields using any translation service. To translate the forms within SharePoint Site:

1. Go to your AEM Project folder on Microsoft® SharePoint and open your spreadsheet. You can also create new spreadsheet for a form.
1. Add new sheet to your existing Google spreadsheet. 
1. Rename the existing sheet (`shared-default`) to `shared-en` and create a new sheet named `shared-default`. The `shared-default` sheet contains the content for localization to a specific language.
1. Add the  localized content in `shared-default` manually. 
    
      ![Enquiry Translate spreadsheet](/help/forms/assets/translate-enquiry-sp-spreadsheet.png)

1. Preview and publish the sheet using [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content). 

Refer to the [spreadsheet](/help/forms/assets/enquirytranslate.xlsx) containing the form definition for an `enquiry` form translated from English to French language.

![Enquiry Translated Form](/help/forms/assets/translate-form-french.png)

Refer to the URL below, where you can view the form with its French language translation:
https://main--wefinance--wkndforms.hlx.live/enquirytranslate

## Known issues {#known-issues}

* The labels of the form get translated to the specified localized language in the `shared-default` sheet, but the error messages are displayed in the default language of the browser.

    ![Error message](/help/forms/assets/translate-error-message.png)

* When you open the calendar, the calendar drop-down is displayed in the default language of the browser.

    ![Error message](/help/forms/assets/translate-calender-display.png)


## See also

{{see-more-forms-eds}}

