---
description: This tutorial includes instructions to make a section of a form repeatable
title: Repeatable sections in Edge Delivery Services
feature: Edge Delivery Services
---

# Repeatable sections in Edge Delivery

A repeatable section is a component of a form that is duplicated or replicated multiple times to gather information for multiple occurrences of the same data. 

For example, consider a form used to collect information from users applying for a loan. The form allows users to provide personal information, including details of the co-loaners. Users can enter details for co-applicants, with this section being repeatable.

![Repeatable sections in forms](/help/forms/assets/eds-repeatable.png)

## Prerequisites

Set up Edge Delivery Service (EDS) GitHub project using AEM boilerplate and clone the corresponding GitHub repository on your local machine. See [developer tutorial](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/edge-delivery/build/tutorial.html) for details. 

## Repeatable sections in Edge Delivery

Let's take an example of a loan application form. The form enables users to submit personal information. You can include co-applicant details using repeatable sections, with the option to add a minimum and maximum of three co-applicant sections.

>[!NOTE]
>
> * You can author a Microsoft Excel on your SharePoint Site or Google Drive to make the fieldsets repeatable in a form. 
> * In this case, we are taking example of a Micrsoft SharePoint. To make your SharePoint folder as the content source, follow the steps as explained in [How to use Sharepoint](https://www.aem.live/docs/setup-customer-sharepoint).


To add repeatable sections in Edge Delivery:

1. [Author a form using Microsoft Excel](#author-form)
2. [Preview and publish the form](#preview-form)

### Author a form using Microsoft Excel {#author-form}

1. Go to your Microsoft SharePoint account and open or create AEM Edge Delivery project directory.
2. Open an existing Microsoft Excel file or create new. 
   In this example, we are using an Excel sheet named `loan-application.xlsx` created in Microsoft SharePoint Site.
3. Add new columns labeled as `Repeatable`, `Min`, and `Max` in your Microsoft Excel file.
4. Specify the value for the `Repeatable` column as `True` for the fieldset that you want to make repeatable.
5. Specify the values for the `Min` and `Max` columns. The `Min` value represents the minimum number of occurrences for which the panel repeats, while the `Max` value represents the maximum number of occurrences for which the panel repeats.
6. Save your Microsoft Excel file.
     
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




