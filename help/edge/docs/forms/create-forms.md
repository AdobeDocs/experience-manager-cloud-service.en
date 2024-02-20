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

* You have a Github account. 
* You have access to Google Sheets or Microsoft SharePoint.
* You understand the basics of Git, HTML, CSS, and JavaScript.
* You have Node and NPM installed for local development.

## Before you start

* Set up and clone your an Edge Delivery Service (EDS) project. See [developer tutorial](https://www.aem.live/developer/tutorial) for details. 
* Clone the [Forms Block repository](https://github.com/adobe/afb). It includes the Form block which is necessary to render the form.

![Getting Started with Edge Delivery Forms](/help/edge/assets/getting-started-with-eds-forms.png)

## Add the Form block to your Edge Delivery Service (EDS) project {#add-forms-block-to-an-eds-project}

AEM Forms Edge Delivery includes a Form block to help you easily create forms to capture and store captured data. To include the Form block to your Edge Delivery Service project:  

1. Navigate to your Edge Delivery Service (EDS) project folder on your local development environment. 


    ```Shell 

    cd [EDS Project folder]

    ```

1. Create a folder named `form` under the EDS project directory. For example, under the directory for the EDS project named `Portal`, create a folder named `form`. 

    ```Shell 

    mkdir form

    ```


1. Add the [Forms Block](https://github.com/adobe/afb/tree/main/blocks/form) files to the 'form' folder. 

    ```shell

    cp -R <source:path of the form block> <destination: path of the form folder created in the previous step>

    For example

    cp -R Documents/afb/blocks/form Documents/portal/blocks/

    ```

1. Check-in the 'form' folder and underlying files to your Edge Delivery Service project on GitHub. 

    ```Shell 

    git add .
    git commit -m "Added form block"
    git push origin

    ```

    You are now ready to render an EDS form. 

    >[!NOTE] 
    >
    > * If your pull request/eds project build fails and you encounter an error related to importing the `franklin-lib.js` file, update the import statement to reference the `aem.js` file instead of the `franklin-lib.js` file.
    > * If you encounter any linting errors, feel free to disregard them. To bypass the linting checks, navigate to the package.json file and update the "lint" script from `"lint": "npm run lint:js && npm run lint:css"` to `"lint": "echo 'skipping linting for now'"`. Then, commit the changes to the package.json file.

## Create a form using Microsoft Excel or Google Sheet {#create-a-form-for-an-eds-project}

Allowing website developers to create forms and choose what information to collect from website visitors can be helpful. Instead of complex processes, authors can easily set up a form using a spreadsheet. They need to add the right column headers, and then use a form block to display it on the website without any hassle. To create a form: 

1. Create a Microsoft Excel Workbook or Google Sheet anywhere under your AEM Edge Delivery project directory on Microsoft SharePoint or Google Drive.

1. Make sure the AEM user (for example `helix@adobe.com`) configured for your project has editing permissions for the sheet.

1. Open the workbook that you have created and change the name of the default sheet to "shared-default". 

    ![rename default sheet to "shared-default"](/help/edge/assets/rename-sheet-to-helix-default.png)

1. Copy the contents of the [contact us spreadsheet](https://docs.google.com/spreadsheets/d/12jvYjo1a3GOV30IqPY6_7YaCQtUmzWpFhoiOHDcjB28/edit?usp=drive_link) to your own spreadsheet. 

    ![contact us spreadsheet](/help/edge/assets/contact-us-form-spreadsheet.png)

1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview and publish the sheet. 

    On previewing and publishing, the browser opens new tabs that display the sheet's contents in JSON format. Make sure to take note of the live URL, as it is necessary for rendering the form later on.

    The format of the URL is:

    ```shell

    https://<branch>--<repository>--<owner>.hlx.live/<form>.json

    For example, https://main--portal--wkndforms.hlx.live/contact-us.json

    ```

## Preview the form using your Edge Delivery Service (EDS) page {#add-a-form-to-your-eds-page}

Till now, you have enabled the form block for your EDS project and prepared the structure of the form. Now, to include the form to your EDS page and render it:

1. Go to your AEM Edge Delivery project directory on Microsoft SharePoint or Google Drive.

1. To add the form to a page, open the corresponding the doc file. For example, open the index file.

1. Navigate to the desired location within the document where you want to add the form.

1. Add a block named 'Form' to the file, similar to the one displayed below. 

    ![](/help/edge/assets/form-block-in-sites-page-example.png)

    In the second row, include the URL you noted down in the previous section, as a hyperlink. 

1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview and publish the page. The form is rendered. 

    For example, here is the form based on the [contact us spreadsheet](https://docs.google.com/spreadsheets/d/12jvYjo1a3GOV30IqPY6_7YaCQtUmzWpFhoiOHDcjB28/edit?usp=drive_link): 


    ![contact us (EDS form)](/help/edge/assets/eds-form.png)

    The form block renders the form but it not ready to accept the data yet. On clicking the submit button, you experience an error similar to the following: 

    ![error on form submission](/help/edge/assets/form-error.png)

   [Prepare your sheet to accept data](/help/edge/docs/forms/submit-forms.md). You can submit the data to sheet post preparing it to accept data. 


## See more

* [Create and preview a form](/help/edge/docs/forms/create-forms.md)
* [Enable form to send data](/help/edge/docs/forms/submit-forms.md)
* [Publish a form to sites page](/help/edge/docs/forms/publish-eds-forms.md)
* [Add validations to form fields](/help/edge/docs/forms/validate-forms.md)
* [Change themes and style of form](/help/edge/docs/forms/style-theme-forms.md)