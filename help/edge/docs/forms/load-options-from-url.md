---
title: Load Dropdown List Options from URL
description: The dropdown list options are included in a distinct spreadsheet and then imported into the primary spreadsheet via the provided URL.
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
exl-id: 5b0bc1b6-6e33-41f3-b7c1-4d997787b6cd
---
# Load dropdown list options from URL 

In Edge Delivery Services forms, users have the option to select a value from a predefined set of options. Form authors use the `select` element, which provides a list of choices. 
For example, the `enquiry` form features a drop-down menu for selecting countries, offering users a range of predefined countries to choose from. You can see this list comprises a long list of countries separated by commas.

![Drop-down options](/help/forms/assets/drop-down-options.png)

Managing long lists of options for dropdown menus can be cumbersome when directly adding them into the sheet containing the form's definition. Creating a separate sheet to store these dropdown options can simplify and streamline the process. This sheet acts as a centralized repository for all dropdown options, arranged in a structured format. Each option is listed in its own row, facilitating easier management and updates.

Let us explore improving the form authoring process by loading the options list from another spreadsheet via a URL. 

By the end of this article, you learn to:

* [Define options in a separate spreadsheet ](#define-options)
* [Add URL to load drop-down list options](#add-url)

## Define options in a separate sheet {#define-options}

Create a sheet with two columns:`Option` and `Value`, to define the options:

1. Go to your AEM Project folder on Microsoft® SharePoint or Google Drive folder. 
2. Add a sheet named `shared-country` in Microsoft® SharePoint Site or within your Google Drive folder and add the following:
   
    * **Option**: Represents the display values of options in the drop-down menu.
    * **Value**: Represents the submitted value when a user selects the option.

    >[!NOTE]
    >
    > If the value and option for a drop-down option are same, the spreadsheet can contain only the **Option** column.

   Let's add new sheet, [shared-country](/help/forms/assets/enquiry-options.xlsx) for the options displayed in the `Destination` drop-down list in the `enquiry` form.

    Refer to the illustration below, depicting the `shared-country` spreadsheet:

   ![Drop-down for country](/help/forms/assets/drop-down-country-options.png)
3. Preview and publish the `shared-country` sheet using [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content). 
  
   Refer to the URL which showcases the `shared-country` sheet:
   https://main--wefinance--wkndforms.hlx.live/enquiry.json?sheet=country  

>[!NOTE]
>
> `?sheet=country` is a query parameter appended to the URL. This parameter indicates the JSON filtered based on the `shared-country` sheet. It redirects to the JSON file containing information related to different countries.

## Add URL to load drop-down list options{#add-url}

The `Options` property of a `select` field accepts a URL. The URL returns a JSON array used as options for the `Destination` drop-down list. To add the URL to load drop-down list options:

1. Go to your AEM Project folder on Microsoft® SharePoint or Google Drive and open your spreadsheet. You can also create new spreadsheet for a form.
1. Copy the URL of `shared-country` sheet and paste it in the `Options` column for the `Destination` field.

     ![Enquiry spreadsheet](/help/forms/assets/drop-down-enquiry.png)

1. Preview and publish the sheet using [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content).


   ![Drop-down for country](/help/forms/assets/load-dropdown-options-form.png)

You can refer to the [enquiry spreadsheet](/help/forms/assets/enquiry-options.xlsx) to add the URL to load drop-down list options.

After integrating the URL into the form definition to load drop-down list options, the options for the `Destination` drop-down start appearing from the URL.

Refer to the URL below, which displays the `enquiry` form displaying the options saved in the separate sheet:

https://main--wefinance--wkndforms.hlx.live/enquiry-form 

## See also

{{see-more-forms-eds}}
