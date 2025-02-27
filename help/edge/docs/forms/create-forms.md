---
title: Getting Started with Edge Delivery Services for AEM Forms. Create a form.
description: Craft perfect forms, fast! ⚡ AEM Forms Edge Delivery doc-based authoring = blazing speed & SEO-friendly forms for happier users & search engines.
feature: Edge Delivery Services
exl-id: 0cf881a2-3784-45eb-afe8-3435e5e95cf4
role: Admin, Architect, Developer
---
# Create a form using Adaptive Forms Block

>[!VIDEO](https://video.tv.adobe.com/v/3427881?quality=12&learn=on)

AEM Forms Edge Delivery provides a block, known as Adaptive Forms Block, to help you easily create forms to capture and store captured data. You can [create a new AEM project pre-configured with Adaptive Forms Block](/help/edge/docs/forms/tutorial.md#create-a-new-aem-project-pre-configured-with-adaptive-forms-block) or [add the Adaptive Forms Block to an existing AEM project](/help/edge/docs/forms/tutorial.md#add-adaptive-forms-block-to-your-existing-aem-project).  

These forms submit data directly to a Microsoft Excel or Google Sheets file, enabling you to use vibrant ecosystem and robust APIs of Google Sheets, Microsoft Excel, and Microsoft SharePoint to easily process submitted data or to initiate an existing business workflow.

![Document-based Authoring ecosystem](/help/edge/assets/document-based-authoring-workflow-create-form.png)


## Prerequisites

Before you start, ensure that you have completed the following steps:

* Set up an [AEM project using AEM Forms boilerplate](/help/edge/docs/forms/tutorial.md#create-a-new-aem-project-pre-configured-with-adaptive-forms-block) [added Adaptive Forms Block to your existing AEM Project](/help/edge/docs/forms/tutorial.md#add-adaptive-forms-block-to-your-existing-aem-project) and clone the corresponding GitHub repository on your local machine. 
<!--In this document, the local folder of your Edge Delivery Services (EDS) project is referred as `[EDS Project repository]`.  -->
* Ensure that you have access to Google Sheets or Microsoft SharePoint. To set up Microsoft SharePoint as your content source, see [How to use SharePoint](https://www.aem.live/docs/setup-customer-sharepoint).



## Create a form

<!--
+++ Step 1: Add the Adaptive Forms Block to your Edge Delivery Services (EDS) project.

The Adaptive  empowers users to create forms for an Edge Delivery Service Site. However, this block isn't included in the default AEM boilerplate (used to create an Edge Delivery Services project). To seamlessly integrate the Adaptive Forms Block into your Edge Delivery Services project:

1. **Clone the Adaptive Forms Block repository**: Clone the [Adaptive Forms Block repository](https://github.com/adobe-rnd/form-block) on your local machine. It contains the code to render the form on an EDS webpage. In this document, the local folder of your Forms Block repository is referred as `[Adaptive Forms Block repository]`.
2. **Locate the Adaptive Forms Block Repository:** Access the [Adaptive Forms Block repository]/blocks/src folder and copy its content. 

3. on your local machine and copy the `form` folder. 
4. **Paste the Adaptive Forms Block's code into your EDS Project:**
Navigate to the [EDS Project repository]/blocks/ folder on your local machine and create a 'form' folder. Paste the `[Adaptive Forms Block repository]/blocks/src content`, copied in perevious step to the `[EDS Project repository]/blocks/form` folder.
1. **Commit Changes to GitHub:** Check in the `[EDS Project repository]/blocks/form` folder and its underlying files to your Edge Delivery Services project on GitHub.

After completing these steps, the Adaptive Forms Block is successfully added to your Edge Delivery Services (EDS) project repository on GitHub. You can now create and add forms to a EDS Sites page.
 

**Troubleshooting GitHub build issues**

Ensure a smooth GitHub build process by addressing potential issues:

* **Resolve Module Path Error:**
    If you encounter the error "Unable to resolve path to module "'../../scripts/lib-franklin.js'", navigate to the [EDS Project]/blocks/forms/form.js file. Update the import statement by replacing the lib-franklin.js file with the aem.js file.

* **Handle Linting Errors:**
    Should you come across any linting errors, you can bypass them. Open the [EDS Project]/package.json file and modify the "lint" script from "lint": "npm run lint:js && npm run lint:css" to "lint": "echo 'skipping linting for now'". Save the file and commit the changes to your GitHub project. -->

+++ Step 1: Author a form using Microsoft Excel or Google Sheet.

Instead of navigating through complex processes, crafting a form can be effortlessly achieved using a spreadsheet. You can define the rows and columns that will make up the form structure. Each row represents an individual [form field](/help/edge/docs/forms/form-components.md#available-components) and the column headers define the corresponding [field properties](/help/edge/docs/forms/form-components.md#components-properties).  

For instance, consider the following spreadsheet where rows outline fields for a [enquiry](/help/edge/assets/enquiry.xlsx) spreadsheet and column headers define their properties:

![Enquiry spreadsheet](/help/edge/assets/enquiry-form-spreadsheet.png)

To proceed with form creation:

1. Access your AEM Edge Delivery project folder on Microsoft SharePoint or Google Drive. 

1. Create a Microsoft Excel Workbook or Google Sheet anywhere within your AEM Edge Delivery project directory. For example, create a spreadsheet named `enquiry` on AEM Edge Delivery project directory on Google Drive. 

   <!-- ![Sample Content on Google Drive](/help/edge/assets/upload-sample-files-to-your-content-folder.png)-->

1. Ensure that the sheet is shared with the appropriate AEM user (for example `forms@adobe.com`) [as per the configurations specified for your project](https://www.aem.live/docs/setup-customer-sharepoint). Grant the user editing permission for the sheet. 

1. Open the created spreadsheet and rename the default sheet to "shared-aem". 

    ![rename default sheet to "shared-default"](/help/edge/assets/rename-sheet-to-shared-default.png)

1. To add the form fields, insert rows and column headers into the 'shared-aem' sheet. Each row should represent a [form field](/help/edge/docs/forms/form-components.md#available-components), with column headers defining the corresponding field [properties](/help/edge/docs/forms/form-components.md#components-properties).


    For a swift start, consider copying the contents of the [Enquiry spreadsheet](/help/edge/assets/enquiry.xlsx) into your spreadsheet. After copying the content, save your spreadsheet. 

    >[!VIDEO](https://video.tv.adobe.com/v/3427468?quality=12&learn=on)


1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview the sheet. 

    ![Use AEM Sidekick to preview the sheet](/help/edge/assets/preview-form.png)

    Upon previewing, new browser tabs display the sheet's contents in JSON format. Ensure to capture the preview URL, as this is required for rendering the form in next the section. The URL format is as follows:


    ```JSON

        https://<branch>--<repository>--<owner>.aem.live/<form-path>/<form-file-name>.json
       
    ```

    * `<branch>` refers to the branch of your GitHub repository. 
    * `<repository>` denotes your GitHub repository. 
    * `<owner>` refers to username of your GitHub account that hosts your GitHub repository.

    For example, if your project's repository is named "wefinance", it's located under the account "wkndform", and you're using the "main" branch, the URL look like the following:

`https://main--wefinance--wkndform.aem.page/enquiry.json`
<!--(https://main--wefinance--wkndform.aem.page/enquiry.json)-->


+++

+++ Step 2: Preview the form using your Edge Delivery Services page.


Till now, you have prepared the structure of the form. Now, to preview the form:

1. Open your Microsoft SharePoint or Google Drive account and navigate to your AEM Edge Delivery project directory.



1. Open a document file (For example, index file) to embed the form. Alternatively, you can [create a new document](/help/edge/assets/enquiry-form.docx).

1. Move to the desired location within the document where you intend to add the form.

1. To create a form block to render the form. Select Insert > Table, and create a one column, two row table. Name the table "Form" and paste the preview URL in the second row. Make sure the URL is formatted as a hyperlink, not plain text, as illustrated below:

    | Form  |
    |---|
    | `https://main--wefinance--wkndform.aem.live/enquiry.json` |


    ![Add Adaptive Forms Block to your webpage](/help/edge/assets/enquiry-doc-to-embed-form.png)

    This block serves as a placeholder where the form is embedded. In the second row of the block, add the preview URL of your `<form>.json` file as a hyperlink. 
    
     >[!IMPORTANT]
     >
     >
     > Ensure that the URL is formatted as a hyperlink rather than being displayed as plain text.


1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview the document. The page now displays the form. For example, here is the form based on the [enquiry spreadsheet](/help/edge/assets/enquiry-form.docx): 


    [![A sample EDS form](/help/edge/assets/updated-form.png)](https://main--wefinance--wkndform.aem.page/enquiry-form)

    Now, fill the form and click the submit button, you experience an error, similar to the following, because the spreadsheet is not set to accept the data yet. 

    ![error on form submission](/help/edge/assets/form-error.png)

+++


## Next step

[Prepare your spreadsheet](/help/edge/docs/forms/submit-forms.md) to begin accepting data upon form submission.


## See also

{{see-more-forms-eds}}
