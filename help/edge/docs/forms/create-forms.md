---
title: Getting Started with AEM Forms Edge Delivery Service
description: Craft perfect forms, fast! ⚡ AEM Forms Edge Delivery doc-based authoring = blazing speed & SEO-friendly forms for happier users & search engines.
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
---

# Create a form on AEM Forms Edge Delivery Service

In today's digital age, creating user-friendly forms is essential for any organization. AEM Forms Edge Delivery's lets you create forms using familiar tools like Word or Google Docs. 

These forms submit data directly to a Microsoft Excel or Google Sheets file, enabling you to use vibrant ecosystem and robust APIs of Google Sheets, Microsoft Excel, and Microsoft Sharepoint to easily process submitted data or to initiate an existing business workflow.


## Prerequisites

Before you start, ensure that you have completed the following steps:

* Set up and clone your Edge Delivery Service (EDS) project. See [developer tutorial](https://www.aem.live/developer/tutorial) for details. The local folder of your Edge Delivery Service (EDS) project is reffered as `[EDS Project repository]` in this document. 
* Clone the [Forms Block repository](https://github.com/adobe/afb). It contains the code to render the form on an EDS webpage. The local folder of your Forms Block repository is reffered as `[Forms Block repository]` in this document. 
* Ensure that you have access to Google Sheets or Microsoft SharePoint.


## Create a form

+++ Step 1: Add the Form block to your Edge Delivery Service (EDS) project.

AEM Forms Edge Delivery includes a Form block to help you easily create forms to capture and store captured data. To include the Form block to your Edge Delivery Service project: 

1. Navigate to `[Forms Block repository]/blocks` and copy the `forms` folder.

1. Navigate to `[EDS Project repository]/blocks/` and paste the `forms` folder. 

    >[!VIDEO](https://video.tv.adobe.com/v/3427487?quality=12&learn=on)  

1. Check in the `form` folder and underlying files to your Edge Delivery Service project on GitHub. 

    The Form block is added to your EDS project repository on Github. Ensure that the Github build does not fails:

    * If you encounter an error "Unable to resolve path to module "'../../scripts/lib-franklin.js'", open the `[EDS Project]/blocks/forms/form.js` file. In the import statement, replace the `lib-franklin.js` file with the `aem.js` file.
    
    * If you encounter any linting errors, feel free to disregard them. To bypass the linting checks, open the `[EDS Project]\package.json` file and update the "lint" script from `"lint": "npm run lint:js && npm run lint:css"` to `"lint": "echo 'skipping linting for now'"`. Save the file and commit it to your GitHub project.

You can now create a form and add it to your site. 

+++

+++ Step 2: Author a form using Microsoft Excel or Google Sheet.

Instead of complex processes, you can easily create a form using a spreadsheet. You can start by adding the rows and column headers to a spreadsheet, where each row defines a form field and each column header defines the properties of the corresponding form fields.

For example, in the following spreadsheet, rows define the fields for a `contact us` form and column header defines properties of the corresponding fields. 

![contact us spreadsheet](/help/edge/assets/contact-us-form-spreadsheet.png)

To create a form: 

1. Open your AEM Edge Delivery project folder on Microsoft SharePoint or Google Drive.  

1. Create a Microsoft Excel Workbook or Google Sheet anywhere under your AEM Edge Delivery project directory. For example, create a spreadsheet named `contact-us` on AEM Edge Delivery project directory on Google Drive. 

1. Make sure that the sheet is shared with AEM user (for example `helix@adobe.com`) [configured for your project](https://www.aem.live/docs/setup-customer-sharepoint) and user has editing permissions for the sheet. 

1. Open the spreadsheet that you have created and change the name of the default sheet to "shared-default". 

    ![rename default sheet to "shared-default"](/help/edge/assets/rename-sheet-to-shared-default.png)

1. To add the fields of the form, add the rows and column headers to the `shared-default` sheet, where each row defines a form field and each column header defines the [properties](/help/edge/docs/forms/eds-form-field-properties)) of the corresponding form fields. 

    To start quickly, you can copy the contents of the [contact us spreadsheet](https://docs.google.com/spreadsheets/d/12jvYjo1a3GOV30IqPY6_7YaCQtUmzWpFhoiOHDcjB28/edit?usp=drive_link) to your spreadsheet.

    >[!VIDEO](https://video.tv.adobe.com/v/3427468?quality=12&learn=on)

1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview and publish the sheet. 

    ![Use AEM Sidekick to preview and publish the sheet](/help/edge/assets/preview-form.png)

    On previewing and publishing, the browser opens new tabs that display the sheet's contents in JSON format. Make sure to take note of the live URL, as it is necessary for rendering the form later on.

    The format of the URL is:

    ```JSON

    https://<branch>--<repository>--<owner>.hlx.live/<form>.json

    For example, https://main--portal--wkndforms.hlx.live/contact-us.json

    ```

+++

+++ Step 3: Preview the form using your Edge Delivery Service (EDS) page.


Till now, you have added the form block to your EDS project and prepared the structure of the form. Now, to preview the form:

1. Go to your Microsoft SharePoint or Google Drive account and open your AEM Edge Delivery project directory.

1. Open a doc file to embed the form to it. For example, open the index file. You can also create a new doc file. 

1. Navigate to the desired location within the document where you want to add the form.

1. Add a block named 'Form' to the file, similar to the one displayed below. 

    ![](/help/edge/assets/form-block-in-sites-page-example.png)

    In the second row, include the URL you recorded in the preceding section as a hyperlink. Use the preview URL (.page URL) for developmental or testing purposes, or the publish URL (.live) for production.

    >[!IMPORTANT]
    >
    >
    > Ensure that the URL is hyperlinked rather than presented as plain text.


1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview the page. The page now displays the form. 

    For example, here is the form based on the [contact us spreadsheet](https://docs.google.com/spreadsheets/d/12jvYjo1a3GOV30IqPY6_7YaCQtUmzWpFhoiOHDcjB28/edit?usp=drive_link): 


    ![A sample EDS form](/help/edge/assets/eds-form.png)

    Now, fill the form and click the submit button, you experience an error, similar to the following, because the spreadsheet is not set to accept the data yet. 

    ![error on form submission](/help/edge/assets/form-error.png)

+++


## Next step

[Prepare your spreadsheet](/help/edge/docs/forms/submit-forms.md) to begin accepting data upon form submission.



## See more

* [Form Field Properties](/help/edge/docs/forms/eds-form-field-properties)
* [Create and preview a form](/help/edge/docs/forms/create-forms.md)
* [Enable form to send data](/help/edge/docs/forms/submit-forms.md)
* [Publish a form to sites page](/help/edge/docs/forms/publish-eds-forms.md)
* [Add validations to form fields](/help/edge/docs/forms/validate-forms.md)
* [Change themes and style of form](/help/edge/docs/forms/style-theme-forms.md)
