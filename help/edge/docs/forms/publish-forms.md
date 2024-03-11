---
title: Publish an AEM Forms Edge Delivery Services Form
description: Publish an AEM Forms Edge Delivery Services Form
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
exl-id: dcb16da1-dcc2-4529-8859-0716e727b54d
---
# Publish your form

Once you are ready to share your form with your customers for data collection or submission, you can simply publish it, making the form readily available for your customers to use.

![Document-based authoring ecosystem](/help/edge/assets/document-based-authoring-workflow-publish-form.png)

## Pre-requisites

* The [Adaptive Forms Block is enabled for your EDS project on GitHub](/help/edge/docs/forms/create-forms.md).
* Your form is full tested and ready to use. 
* Your [spreadsheet is configured](/help/edge/docs/forms/submit-forms.md) to accept data.

## Publish your form  

+++ 1. Publish your spreadsheet

1. Open your Microsoft SharePoint or Google Drive account and navigate to your AEM Edge Delivery project directory.

1. Open the spreadsheet that has your form. For example, the `enquiry` form Microsoft Excel workbook. 

1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview the sheet. 

    ![Use AEM Sidekick to preview the sheet](/help/edge/assets/preview-form.png)

    Upon successful completion of the preview operation, the spreadsheet content undergoes conversion into JSON format. The preview page then presents this content in a structured table format. For instance, the accompanying image illustrates the content of an 'enquiry' form.

    ![Forms Preview JSON Format](/help/edge/assets/forms-preview-json-format.png)

1. Use AEM Sidekick to publish the sheet. Ensure to capture the publish URL, as this is required for rendering the form in the next section. The URL format is as follows:


    ```JSON

        https://<branch>--<repository>--<owner>.hlx.live/<form>.json
       
    ```

    * `<branch>` refers to the branch of your GitHub repository. 
    * `<repository>` denotes your GitHub repository. 
    * `<owner>` refers to username of your GitHub account that hosts your GitHub repository.

    For example, if your project's repository is named "portal", it's located under the account "wkndforms", and you're using the "main" branch, the URL look like the following:

    `https://main--portal--wkndforms.hlx.page/enquiry.json`

+++

+++ 2. Add the form to your webpage

Add the `<form>.json` to a webpage to facilitate customer interaction, enabling form fillers to effortlessly fill out and submit the form.


To add the form to your webpage:

1. Access your Microsoft SharePoint or Google Drive account and navigate to your `[AEM Edge Delivery project directory]`.

1. Open a document file where you intend to embed the form. For instance, you can open the `index.docx` file, or alternatively, create a new document.
 
1. Identify the desired section within the document where you want to insert the form, and navigate to it accordingly.

1. Add a block named 'Form' to the file, similar to the example provided below:

    | Form  |
    |---|
    | [https://main--portal--wkndforms.hlx.live/enquiry.json ](https://main--portal--wkndforms.hlx.live/enquiry.json)  |

    This block serves as a placeholder where the form is embedded. In the second row of the block, add the URL of your `<form>.json` file as a hyperlink. 
    
     >[!IMPORTANT]
     >
     >
     > Ensure that the URL is formatted as a hyperlink rather than being displayed as plain text.
    
    Use the preview URL (.page URL) for developmental or testing purposes, or the publish URL (.live) for production. Here's are examples with preview and publish URL: 

    **Preview URL**
    | Form  |
    |---|
    | [https://main--portal--wkndforms.hlx.page/enquiry.json ](https://main--portal--wkndforms.hlx.page/enquiry.json)  |


     **Publish URL**
    | Form  |
    |---|
    | [https://main--portal--wkndforms.hlx.live/enquiry.json ](https://main--portal--wkndforms.hlx.live/enquiry.json)  |

1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview the webpage. The page now displays the form. For example, here is the form based on the [enquiry spreadsheet](https://docs.google.com/spreadsheets/d/196lukD028RDK_evBelkOonPxC7w0l_IiJ-Yx3DvMfNk/edit#gid=0): 


    [![A sample EDS form](/help/edge/assets/eds-form.png)](https://main--portal--wkndforms.hlx.live/)

1. Use AEM Sidekick to publish the form. Now, your customers can fill out the form and submit it. 

+++ 
    
## Troubleshooting 

+++ Unable to submit data to form

If you encounter an error resembling the following message, it indicates that the spreadsheet is not configured to [accept the submitted](/help/edge/docs/forms/submit-forms.md) data yet.

![error on form submission](/help/edge/assets/form-error.png)

+++




## See more
