---
title: Publish an AEM Forms Edge Delivery Services Form
description: Publish an AEM Forms Edge Delivery Services Form
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
---

# Publish your form

Once you are ready to share your form with your customers for data collection or submission, you can simply publish it, making the form readily available for your customers to use.

## Pre-requisites

* The [Form block is enabled for your EDS project on Github](/help/edge/docs/forms/create-forms.md).
* Your form is full tested and ready to use. 
* Your [spreadsheet is configured](/help/edge/docs/forms/submit-forms.md) to accept data.

## Publish your form    

To publish the form:

1. Access your Microsoft SharePoint or Google Drive account and navigate to your `[AEM Edge Delivery project directory]`.

1. Open a document file where you intend to embed the form. For instance, you can open the index file, or alternatively, create a new document.
 
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

1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview the page. The page now displays the form. For example, here is the form based on the [enquiry spreadsheet](https://docs.google.com/spreadsheets/d/196lukD028RDK_evBelkOonPxC7w0l_IiJ-Yx3DvMfNk/edit#gid=0): 


    [![A sample EDS form](/help/edge/assets/eds-form.png)](https://main--portal--wkndforms.hlx.live/)

    Now, your customers can fill out the form and submit it. 
    
## Troubleshooting 

+++ Unable to submit data to form

If you encounter an error resembling the following message, it indicates that the spreadsheet is not configured to accept the submitted data yet.

![error on form submission](/help/edge/assets/form-error.png)

+++


## See more

* [Create and preview a form](/help/edge/docs/forms/create-forms.md)
* [Enable form to send data](/help/edge/docs/forms/submit-forms.md)
* [Publish a form to sites page](/help/edge/docs/forms/publish-eds-forms.md)
* [Add validations to form fields](/help/edge/docs/forms/validate-forms.md)
* [Change themes and style of form](/help/edge/docs/forms/style-theme-forms.md)