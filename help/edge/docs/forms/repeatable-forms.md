---
title: Add repeatable sections to a form
description: Add repeatable sections to an EDS form
feature: Edge Delivery Services
exl-id: 062d5a88-48ca-421f-bf0d-1483e3cfee28
role: Admin, Architect, Developer
---
# Add repeatable sections to a form

Adaptive Forms Block provides the capability to add or make a section or a component of a form repeatable. This allows users to enter information multiple times for the same type of data, making it easier to collect information like work experience or educational background.

For example, consider a form used to collect information about a person's work experience. You may have a repeatable section for capturing details of each previous job. The repeatable section would typically contain fields such as company name, job title, dates of employment, and job responsibilities. The user can add multiple instances of the repeatable section to enter information about each job they have held.

By the end of this article, you learn to:

* [Create a repeatable section in a form](#add-repeatable-sections-to-a-form)
* [Set minimum or maximum number of repetitions in a form](#set-minimum-or-maximum-number-of-repetitions-for-a-repeatable-section)

## Create a repeatable section

Creating a repeatable section in a form offers users the ability to input multiple instances of the same set of data, allowing for the efficient collection of repetitive information. To create a repeatable section in a form: 

1. Go to your Edge Deliver project folder on Microsoft SharePoint or Google Workspace and open your spreadsheet. 

1. Add a form field with the `type` property set to `fieldset` 
1. Specify `Name` of the field. The name property is used to create a repeatable section.
1. Enable repeatability by setting `repeatable` to `true`.
1. Specify a descriptive `label` for the field. It serves as the heading for the repeatable section. 

    Refer to the image below for an illustration of an employment history section within a job application form. 

    ![](/help/edge/assets/repeatable-section-example-job-application-form.png)

1. For each field you want to include in the section, set its `Fieldset` property to the same name you chose in step 3.

    For instance, designate `experience` in the Fieldset property of all relevant fields to be included in the `employment history` section.

    ![example of a repeatable section field and its properties](/help/edge/assets/repeatable-section--mention-fieldset-name-example-job-application-form.png)

1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview and publish the sheet. The repeatable section is added to form. 

    Underneath the repeatable section, users find an intuitive **Add** button, facilitating the addition of multiple sections with ease.

    ![repeatable section, Add button, to add multiple sections ](/help/edge/assets/repeatable-section-example.png)


## Setting Minimum and Maximum Repetitions

In form design, it's beneficial to set minimum and maximum repetitions for repeatable sections. By doing so, you establish control and consistency while guiding users effectively. To set minimum or maximum number of repetitions:

1. Go to your Edge Deliver project folder on Microsoft SharePoint or Google Workspace and open your spreadsheet.

1. For a field of `type` `fieldset` and `repeatable` property set to `true`:
    
    * set the `min` property to specify the minimum number of times the section can be repeated.

    * set the `max` property to specify the maximum number of times the section can be repeated.

    ![Set the min and max property to specify the number of times the section can be repeated](/help/edge/assets/repeatable-section-set-min-max.png)

1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview and publish the sheet. 

    On adding a repeatable section, users find an intuitive **Delete** icon, making it easier to remove repeatable sections. Once added, these sections cannot be decreased to fewer instances than specified by the `min` property. This ensures adherence to the minimum requirement set for the form's completion.

<!--

For example, consider a form used to collect information from users applying for a loan. . You may have a repeatable section for capturing details of each co-applicant. The repeatable section would typically contain fields such as co-co-applicant

The form allows users to provide personal information, including details of the co-applicants. Users can enter details for co-applicants, with this section being repeatable.

![Repeatable sections in forms](/help/forms/assets/eds-repeatable.png)

## Prerequisites

The [Adaptive Forms Block is enabled](/help/edge/docs/forms/create-forms.md) for your Edge Delivery Services project. 

## Add a repeatable section to a form 

Let's take an example of a loan application form. The form enables users to submit personal information. You can include co-applicant details using repeatable sections, with the option to add a minimum and maximum of three co-applicant sections.

"_You can use a Microsoft Excel file on your SharePoint Site or Google Sheet file on Google Drive to develop a form. Examples in this document are based on a [Microsoft Excel file on your SharePoint Site](https://www.aem.live/docs/setup-customer-SharePoint)._" 


To add repeatable sections in Edge Delivery:

1. [Author a form using Microsoft Excel](#author-form)
2. [Preview and publish the form](#preview-form)

### Author a form using Microsoft Excel {#author-form}

1. Go to your Edge Deliver project folder on Microsoft SharePoint or Google Workspace and open your spreadsheet. For example, open an a spreadsheet named `loan-application.xlsx`.

1. Add a new columns labeled `Repeatable` to the sheet contaning your form fields. By default, the `shared-default` sheet contains the form fields.  

1. Add new columns labeled as `Repeatable`, `Min`, and `Max` in your Microsoft Excel file.
1. Specify the value for the `Repeatable` column as `True` for the fieldset that you want to make repeatable.
1. Specify the values for the `Min` and `Max` columns. The `Min` value represents the minimum number of occurrences for which the panel repeats, while the `Max` value represents the maximum number of occurrences for which the panel repeats.
1. Save your Microsoft Excel file.
     
>[!NOTE]
>
> Here is the [Loan application](/help/forms/assets/loan-application.xlsx) excel sheet for your reference. 

### Preview/Publish the form using your Edge Delivery Service

1. Open or create new document file in a Microsft SharePoint Site to embed the Excel sheet  in it using a `Form Block`. For example, open the `index` file and add a `Form Block`.
2. Open the command prompt, navigate to your AEM Edge Delivery project directory on your local machine, and execute the command as `aem up`.

The form is accessible at `https://localhost:3000`, where clicking the `Add` button adds new repeatable section for entering co-applicant details. You can also delete the repeatable section by clicking the `Delete` button. 

>[!NOTE]
>
> If you encounter a "Page Not Found" error while accessing your form at localhost, add the directory name of the Microsoft SharePoint Site in front of the URL where your form is located. For example, `http://localhost:3000/<dir-name>/`

-->


## See also

{{see-more-forms-eds}}
