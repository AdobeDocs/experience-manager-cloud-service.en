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

- [Create a repeatable section in a form](#add-repeatable-sections-to-a-form)
- [Set minimum or maximum number of repetitions in a form](#set-minimum-or-maximum-number-of-repetitions-for-a-repeatable-section)

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
    
    - set the `min` property to specify the minimum number of times the section can be repeated.

    - set the `max` property to specify the maximum number of times the section can be repeated.

    ![Set the min and max property to specify the number of times the section can be repeated](/help/edge/assets/repeatable-section-set-min-max.png)

1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview and publish the sheet. 

    On adding a repeatable section, users find an intuitive **Delete** icon, making it easier to remove repeatable sections. Once added, these sections cannot be decreased to fewer instances than specified by the `min` property. This ensures adherence to the minimum requirement set for the form's completion.


