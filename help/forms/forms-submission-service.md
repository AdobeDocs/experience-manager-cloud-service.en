---
Title: How to use forms submission service for submitting forms?
Description: Learn how to use forms submission service for submitting forms.
Keywords: Use form submission service, Submit form using form submission service 
feature: Edge Delivery Services
Role: User, Developer
---

# Forms Submission service

Forms Submission service allows you to store data from the form submissions in any spreadsheet, such as OneDrive, SharePoint, or Google Sheets, allowing you to easily access and manage form data within your preferred spreadsheet platform.

![Forms submission service](/help/forms/assets/form-submission-service.png)

## Advantages to use Forms Submission service

A few advantages of using the Forms Submission Service with spreadsheets are:

* **Direct integration**: You can configure forms to submit data directly to a specified spreadsheet, eliminating the need for manual data transfer. 
* **Data structure**: When setting up the submission, you can map form fields to corresponding spreadsheet columns for organized data storage. 
* **Access control**: You can leverage existing permissions to control who can access and modify submitted form data, depending on the chosen spreadsheet service. 

## Pre-requisites

Below are the prerequisites for using the Forms Submission service:

* Make sure your AEM Project has the latest Adaptive Form Block.  
* Ensure you have an AEM Forms add-on license.
* Ensure that your Git repository is added to the allowlist to use the Forms Submission Service. Fill out the [form](https://main--afb--adobe.hlx.page/docs/docbased/submit#feature-enablement-request) to request for Forms Submission Service.  
* Ensure that your spreadsheet has edit access granted to the `forms@adobe.com` account.  
  
## Configure Forms Submission service 

![Workflow for forms submission service](/help/forms/assets/forms-submission-service-workflow.png)

### 1. Create a form using a form definition

Create new AEM project configured with the Adaptive Forms Block. Refer to the [Getting Started - Developer Tutorial]([/help/forms/](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/build-forms/getting-started-edge-delivery-services-forms/tutorial)) article to learn how to create a new AEM project.
Next, author a form using Google Sheets or Microsoft Excel. To learn how to create a form using a form definition in Microsoft Excel or Google Sheets, [click here](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/build-forms/getting-started-edge-delivery-services-forms/create-forms).

The below screenshot displays the form definition used to create form:

![Form Definition](/help/forms/assets/form-submission-definition.png)

### 2. Enable the spreadsheet to accept data.

Once you have created and previewed the form, enable the corresponding spreadsheet to start receiving data. You can [manually enable the spreadsheet to accept data](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/build-forms/getting-started-edge-delivery-services-forms/submit-forms#manually-enable-the-spreadsheet-to-accept-data).

![Incoming sheet](/help/forms/assets/form-submission-incoming-sheet.png)

### 3. Share the spreadsheet and generate a link.

To share the spreadsheet to the `forms@adobe.com` account and generate a link, perform the folllowing steps:

1. In Excel or Google Sheets, click the **Share** button on the top-right corner.
1. Add the `forms@adobe.com` account and 
click the eye icon, select **Edit** access, and click **Send**.

    ![Share incoming sheet](/help/forms/assets/form-submission-share-incoming.png)

1. To copy the spreadsheet link, click the **Share** button on the top-right corner and select **Copy Link**.

    ![Copy link of incoming sheet](/help/forms/assets/form-submission-copy-link.png)

### 4. Link the spreadsheet in the form definition

To configure the Forms Submission service with the Google Sheets or Microsoft Excel, perform the following steps:

1. Open the spreadsheet which contains the form definition.
1. In the row corresponding to the **Submit** field, paste the copied spreadsheet link into the **Action** column.

    ![Link a spreadsheet](/help/forms/assets/form-submission-sheet-linking.png)

1. Preview and publish the sheet using the [AEM Sidekick](https://www.aem.live/docs/sidekick) with updated Form Submission service.

>[!NOTE]
>
> You can refer to the [spreadsheet](/help/forms/assets/spreadsheet.xlsx) to use the Forms Submission service.

## See also

{{see-more-forms-eds}}