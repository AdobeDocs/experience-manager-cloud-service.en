---
title: Load Dropdown List Options from a URL or another sheet for Edge Delivery Services for AEM Forms as a Cloud Service
description: The dropdown list options are included in a distinct spreadsheet and then imported into the primary spreadsheet via the provided URL.
feature: Edge Delivery Services
exl-id: 5b0bc1b6-6e33-41f3-b7c1-4d997787b6cd
role: Admin, Architect, Developer
---

# Options from a URL or another sheet for Edge Delivery Services for AEM Forms as a Cloud Service 

Forms often include dropdown menus for users to select from predefined options. These options are typically defined within the form itself, but managing long lists can be cumbersome. This guide outlines how to improve form authoring by loading dropdown options from a separate spreadsheet via a URL.


Benefits of loading a dropdown options from a separate spreadsheet are: 

* Simplified Management: Maintain dropdown options in a centralized location for easier updates and additions.
* Improved Efficiency: Eliminate the need to manually add long option lists within the form definition.

![Drop-down options](/help/forms/assets/drop-down-options.png)


By the end of this article, you learn to:

* [Define options in a separate spreadsheet ](#define-options)
* [Add URL to load drop-down list options](#add-url)

## Define options in a separate sheet {#define-options}

Defining Options in a Separate Spreadsheet

1. Create a Spreadsheet:
   1. Locate your AEM project folder in Microsoft&reg; SharePoint or Google Drive.
   1. Add a new sheet. For example, "shared-country".
1. Define Option Columns:
   Add two columns: "Option" and "Value".
   * "Option" defines the text displayed in the dropdown menu.
   * "Value" defines the submitted value when a user selects the option.

   >[!NOTE]
   >
   >If both option and value are identical, only the "Option" column is required.

1. Populate the Spreadsheet:
   Enter your country options in the "Option" column (and "Value" column if necessary).
   
   Refer to the example below for structure.

   ![Drop-down for country](/help/forms/assets/drop-down-country-options.png)

1. Preview and publish the `shared-country` sheet using [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content).

   For example, if your project's repository is named "wefinance", it's located under the account owner "wkndform", and you're using the "main" branch, the URL which showcases the `shared-country` sheet:
   `https://main--wefinance--wkndform.aem.live/enquiry.json?sheet=country` 
   <!--(https://main--wefinance--wkndform.aem.live/enquiry.json?sheet=country)  -->

>[!NOTE]
>
> `?sheet=country` is a query parameter appended to the URL. This parameter indicates the JSON filtered based on the `shared-country` sheet. It redirects to the JSON file containing information related to different countries.

## Add URL to load drop-down list options{#add-url}

The `Options` property of a `select` field accepts a URL. The URL returns a JSON array used as options for the `Destination` drop-down list. To add the URL to load drop-down list options:

1. Go to your AEM Project folder on Microsoft&reg; SharePoint or Google Drive and open your spreadsheet. You can also create new spreadsheet for a form.
1. Copy the URL of `shared-country` sheet and paste it in the `Options` column for the `Destination` field.

     ![Enquiry spreadsheet](/help/forms/assets/drop-down-enquiry.png)

1. Preview and publish the sheet using [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content).


   ![Drop-down for country](/help/forms/assets/load-dropdown-options-form.png)

You can refer to the [enquiry spreadsheet](/help/edge/assets/enquiry.xlsx) to add the URL to load drop-down list options.

After integrating the URL into the form definition to load drop-down list options, the options for the `Destination` drop-down start appearing from the URL.

For example, if your project's repository is named "wefinance", it's located under the account owner "wkndform", and you're using the "main" branch, the below URL displays the `enquiry` form displaying the options saved in the separate sheet:

`https://main--wefinance--wkndform.aem.live/enquiry-form`
<!--(https://main--wefinance--wkndform.aem.live/enquiry-form) 
-->

## See also

{{see-more-forms-eds}}

   