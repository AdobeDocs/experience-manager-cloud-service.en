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

* You have a GitHub account. 
* You have access to Google Sheets or Microsoft SharePoint.
* You understand the basics of Git, HTML, CSS, and JavaScript.
* You have Node and NPM installed for local development.

## Before you start

* Set up and clone your Edge Delivery Service (EDS) project. See [developer tutorial](https://www.aem.live/developer/tutorial) for details. 
* Clone the [Forms Block repository](https://github.com/adobe/afb). It includes the Form block which is necessary to render the form.

![Getting Started with Edge Delivery Forms](/help/edge/assets/getting-started-with-eds-forms.png)

## Add the Form block to your Edge Delivery Service (EDS) project {#add-forms-block-to-an-eds-project}

AEM Forms Edge Delivery includes a Form block to help you easily create forms to capture and store captured data. To include the Form block to your Edge Delivery Service project:  

1. Navigate to the `blocks` folder in your Edge Delivery Service (EDS) project folder on your local development environment. 


    ```Shell 

    cd [EDS Project folder]/blocks

    ```

1. Create a folder named `form` under the `blocks` directory. For example, under the directory for the EDS project named `Portal`, create a folder named `form`. 

    ```Shell 

    mkdir form

    ```


1. Add the [Forms Block](https://github.com/adobe/afb/tree/main/blocks/form) files to the 'form' folder. 

    ```shell

    cp -R <source:path of the form block> <destination: path of the form folder created in the previous step>

    ```

    **For example,**


    ```shell

    cp -R ../../afb/blocks/form ../../fantastic-computing-machine/blocks 


    ```

    

1. Check in the 'form' folder and underlying files to your Edge Delivery Service project on GitHub. 

    ```Shell 

    cd ..
    git add .
    git commit -m "Added form block"
    git push origin

    ```

    The Form block is added to your EDS project. You can now create a form and add it to your site. 

    >[!NOTE] 
    >
    > * If you encounter an error "Unable to resolve path to module "'../../scripts/lib-franklin.js'", open the `[EDS Project]/blocks/forms/form.js` file. In the import statement, replace the `franklin-lib.js` file with the `aem.js` file.
    > * If you encounter any linting errors, feel free to disregard them. To bypass the linting checks, open the `[EDS Project]\package.json` file and update the "lint" script from `"lint": "npm run lint:js && npm run lint:css"` to `"lint": "echo 'skipping linting for now'"`. Save the file and commit it to your GitHub project.

## Create a form using Microsoft Excel or Google Sheet {#create-a-form-for-an-eds-project}

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

     

## Preview the form using your Edge Delivery Service (EDS) page {#add-a-form-to-your-eds-page}

Till now, you have enabled the form block for your EDS project and prepared the structure of the form. Now, to preview the form:

1. Go to your AEM Edge Delivery project directory on Microsoft SharePoint or Google Drive.

1. Create or open a doc file to host the form. For example, open the index file.

1. Navigate to the desired location within the document where you want to add the form.

1. Add a block named 'Form' to the file, similar to the one displayed below. 

    ![](/help/edge/assets/form-block-in-sites-page-example.png)

    In the second row, include the URL you noted down in the previous section, as a hyperlink. You can use the preview URL (.page URL) or publish URL (.live). The preview URL can be used while building or testing the form and publish URL for production. 

    >[!IMPORTANT]
    >
    >
    > Ensure that the URL is not mentioned as a plain-text. It should be added as a hyperlink. 

1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview the page. The page now displays the form. For example, here is the form based on the [contact us spreadsheet](https://docs.google.com/spreadsheets/d/12jvYjo1a3GOV30IqPY6_7YaCQtUmzWpFhoiOHDcjB28/edit?usp=drive_link): 


    ![A sample EDS form](/help/edge/assets/eds-form.png)

    Now, fill the form and click the submit button, you experience an error, similar to the following, because the spreadsheet is not set to accept the data yet. 

    ![error on form submission](/help/edge/assets/form-error.png)


   The next step is to [prepare your spreadsheet to accept data](/help/edge/docs/forms/submit-forms.md). 



## See more

* [Form Field Properties](/help/edge/docs/forms/eds-form-field-properties)
* [Create and preview a form](/help/edge/docs/forms/create-forms.md)
* [Enable form to send data](/help/edge/docs/forms/submit-forms.md)
* [Publish a form to sites page](/help/edge/docs/forms/publish-eds-forms.md)
* [Add validations to form fields](/help/edge/docs/forms/validate-forms.md)
* [Change themes and style of form](/help/edge/docs/forms/style-theme-forms.md)
