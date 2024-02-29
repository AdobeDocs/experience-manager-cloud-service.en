---
title: Getting Started with AEM Forms Edge Delivery Service. Create a form. 
description: Craft perfect forms, fast! ⚡ AEM Forms Edge Delivery doc-based authoring = blazing speed & SEO-friendly forms for happier users & search engines.
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
---

# Create a form for a Edge Delivery Service (EDS) Site

In today's digital age, creating user-friendly forms is essential for any organization. AEM Forms Edge Delivery's lets you create forms using familiar tools like Word or Google Docs. 

These forms submit data directly to a Microsoft Excel or Google Sheets file, enabling you to use vibrant ecosystem and robust APIs of Google Sheets, Microsoft Excel, and Microsoft Sharepoint to easily process submitted data or to initiate an existing business workflow.

AEM Forms Edge Delivery provides a Form block to help you easily create forms to capture and store captured data. You can include the Form block in your AEM EDS project to start creating a form. Let's start: 


## Prerequisites

Before you start, ensure that you have completed the following steps:

* Set up Edge Delivery Service (EDS) GitHub project using AEM boilerplate and clone the corresponding GitHub repository on your local machine. See [developer tutorial](https://www.aem.live/developer/tutorial) for details. In this document, the local folder of your Edge Delivery Service (EDS) project is referred as `[EDS Project repository]` . 
* Clone the [Forms Block repository](https://github.com/adobe/afb) on your local machine. It contains the code to render the form on an EDS webpage. In this document, the local folder of your Forms Block repository is referred as `[Forms Block repository]`. 
* Ensure that you have access to Google Sheets or Microsoft SharePoint. To set up Microsoft SharePoint as your content source, see [How to use Sharepoint](https://www.aem.live/docs/setup-customer-sharepoint)



## Create a form

+++ Step 1: Add the Form block to your Edge Delivery Service (EDS) project.

The Form block empowers users to create forms for an Edge Delivery Service Site. However, this block isn't included in the default AEM boilerplate (used to create an Edge Delivery Service project). To seamlessly integrate the Form block into your Edge Delivery Service project:

1. **Locate the Form Block Repository:** Access the [Forms Block repository]/blocks folder on your local machine and copy the `form` folder.
1. **Paste the Form Block into your EDS Project:**
Navigate to the [EDS Project repository]/blocks/ folder on your local machine and paste the form folder.
1. **Commit Changes to GitHub:** Check in the form folder and its underlying files to your Edge Delivery Service project on GitHub.

After completing these steps, the Form block is successfully integrated into your Edge Delivery Service(EDS) project repository on GitHub. 
 

**Troubleshooting GitHub build issues**

Ensure a smooth GitHub build process by addressing potential issues:

* **Resolve Module Path Error:**
    If you encounter the error "Unable to resolve path to module "'../../scripts/lib-franklin.js'", navigate to the [EDS Project]/blocks/forms/form.js file. Update the import statement by replacing the lib-franklin.js file with the aem.js file.

* **Handle Linting Errors:**
    Should you come across any linting errors, you can bypass them. Open the [EDS Project]/package.json file and modify the "lint" script from "lint": "npm run lint:js && npm run lint:css" to "lint": "echo 'skipping linting for now'". Save the file and commit the changes to your GitHub project.

    

+++

+++ Step 2: Author a form using Microsoft Excel or Google Sheet.

Instead of navigating through complex processes, crafting a form can be effortlessly achieved using a spreadsheet. You can start by adding the rows and column headers to a spreadsheet, where each row represents a form field, while each column header defines the properties of the corresponding field.

For instance, consider the following spreadsheet where rows outline fields for a `enquiry` form and column headers define their properties:

![Enquiry spreadsheet](/help/edge/assets/enquiry-form-spreadsheet.png)

To proceed with form creation:

1. Access your AEM Edge Delivery project folder on Microsoft SharePoint or Google Drive. 

1. Create a Microsoft Excel Workbook or Google Sheet anywhere within your AEM Edge Delivery project directory. For example, create a spreadsheet named `enquiry` on AEM Edge Delivery project directory on Google Drive. 

1. Ensure that the sheet is shared with the appropriate AEM user (for example `helix@adobe.com`) [as per the configurations specified for your project](https://www.aem.live/docs/setup-customer-sharepoint). Grant the user editing permission for the sheet. 

1. Open the created spreadsheet and rename the default sheet to "shared-default". 

    ![rename default sheet to "shared-default"](/help/edge/assets/rename-sheet-to-shared-default.png)

1. To add the form fields, insert rows and column headers into the 'shared-default' sheet. Each row should represent a form field, with column headers defining the corresponding field [properties](/help/edge/docs/forms/eds-form-field-properties).

    For a swift start, consider copying the contents of the [Enquiry spreadsheet](https://docs.google.com/spreadsheets/d/196lukD028RDK_evBelkOonPxC7w0l_IiJ-Yx3DvMfNk/edit#gid=0) into your spreadsheet. After copying the content, save your spreadsheet. 

    >[!VIDEO](https://video.tv.adobe.com/v/3427468?quality=12&learn=on)


1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview the sheet. 

    ![Use AEM Sidekick to preview the sheet](/help/edge/assets/preview-form.png)

    Upon previewing and publishing, new browser tabs display the sheet's contents in JSON format. Ensure to capture the preview URL, as this is required for rendering the form in next section. The URL format is as follows:


    ```JSON

        https://<branch>--<repository>--<owner>.hlx.live/<form>.json
       
    ```

    * `<branch>` refers to the branch of your GitHub repository. 
    * `<repository>` denotes your GitHub repository. 
    * `<owner>` refers to username of your GitHub account that hosts your GitHub repository.

    For example, if your project's repository is named "portal", it's located under the account "wkndforms", and you're using the "main" branch, the URL look like the following:

    `https://main--portal--wkndforms.hlx.page/enquiry.json`


+++

+++ Step 3: Preview the form using your Edge Delivery Service (EDS) page.


Till now, you have added the form block to your EDS project and prepared the structure of the form. Now, to preview the form:

1. **Access Your Project Directory:** Open your Microsoft SharePoint or Google Drive account and navigate to your AEM Edge Delivery project directory..

1. **Embed the Form into a Document:** Open a document file (For example, index file) to embed the form. Alternatively, you can create a new document.

1. **Navigate to the Desired Location:** Move to the desired location within the document where you intend to add the form.

1. **Add the Form Block:** Insert a block named 'Form' into the file, as illustrated below:

    | Form  |
    |---|
    | [https://main--portal--wkndforms.hlx.live/enquiry.json ](https://main--portal--wkndforms.hlx.live/enquiry.json)  |

    This block serves as a placeholder where the form is embedded. In the second row of the block, add the preview URL of your `<form>.json` file as a hyperlink. 
    
     >[!IMPORTANT]
     >
     >
     > Ensure that the URL is formatted as a hyperlink rather than being displayed as plain text.


1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview the document. The page now displays the form. For example, here is the form based on the [enquiry spreadsheet](https://docs.google.com/spreadsheets/d/196lukD028RDK_evBelkOonPxC7w0l_IiJ-Yx3DvMfNk/edit#gid=0): 


    [![A sample EDS form](/help/edge/assets/eds-form.png)](https://main--portal--wkndforms.hlx.live/)

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
