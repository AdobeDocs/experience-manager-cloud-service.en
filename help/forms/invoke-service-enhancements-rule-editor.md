---
title: What are the enhancements to the Invoke service VRE for forms based on Core Components?  
description: Enhancements to the Invoke service for the rule editor
feature: Adaptive Forms, Core Components
role: User, Developer
level: Beginner, Intermediate
keywords: invoke service enhancements in VRE, populating drop-down options using invoke service, Set repeatable panel using output of invoke service, Set panel using output of invoke service, Use output parameter of invoke service to validate other field.
---

# Using Invoke Service in the Visual Rule Editor

Visual Rule Editor in an Adaptive Form supports the **Invoke Service** operation. This operation allows you to select a service from the list of Form Data Models (FDM) configured for your instance. You can map objects to input and output parameters using the event payload option for the specified FDM service. Additionally, the Visual rule editor allows you to create rules for success and failure handlers for **Invoke Service** operations based on its output responses. Success handlers manage the successful execution of the **Invoke Service** operation, while failure handlers address any errors that occur.

### Advantages of using the Invoke Service in the form's rule editor

Here are few advantages of using Invoke Service operation in the rule editor of an Adaotive Form:

* **Streamlined integration**: Visual Rule Editor simplifies the process of integrating external services or APIs into your Adaptive Forms. By using the **Invoke Service**, you can easily connect forms to various data sources and services without the need for complex coding, making form integration more efficient.

* **Dynamic response handling**: You can manage success and error responses based on the output responses of the **Invoke Service**, allowing forms to react dynamically to different scenarios. It ensures forms handle various conditions appropriately, improving flexibility and control.

* **Enhanced user interaction**: Using the **Invoke Service** in the rule editor enables real-time validation within your forms, providing a better user experience. It also ensures that data is accurately validated on the server side, reducing errors and improving form reliability.

## Invoke Service handlers for success and failure responses

Visual rule editor allows you to create rules for success and failure handlers for **Invoke Service** operations based on its output responses. Below image depicts the **Invoke Service** in Visual rule editor for an Adaptive Form:

![Invoke service handlers](/help/forms/assets/invoke-service-rule-editor.png)

To add success or failure handler, click **[!UICONTROL Add Success Handler]** or **[!UICONTROL Add Failure Handler]**, respectively. When you click **[!UICONTROL Add Success Handler]**, the **[!UICONTROL Invoke Service Success Handler]** rule editor appears, allowing you to specify rules or logic to manage the **Invoke Service** output response when the operation is successful. You can specify rules even without defining conditions; however, you can add conditions for the success handler by clicking the **[!UICONTROL Add Condition]** option. The **Enable Error Validation on Server** feature allows validations added by the author while designing an Adaptive Form to run on the server also.

![Invoke service success hadler](/help/forms/assets/invoke-service-success-handler.png)

You can add multiple rules to handle successful responses for the **Invoke Service** operation:

![Multiple success handler](/help/forms/assets/invoke-service-multiple-success-handlers.png){width=50%, height=50%}

Similarly, you can add rules to handle the **Invoke Service** output response when the operation is not successful. The image below displays the **[!UICONTROL Invoke Service Failure Handler]** rule editor:

![Invoke service failure hadler](/help/forms/assets/invoke-service-failue-handler.png)

## Prerequisites for using the Invoke Service in the rule editor

Below are the prerequisites you must satisfy before using **Invoke Service** in the rule editor:

* Make sure you have configured a data source. For instructions on configuring a data source, [click here](/help/forms/configure-data-sources.md).
* Create a Form Data Model using the configured data source. For guidance on creating a Form Data Model, [click here](/help/forms/create-form-data-models.md).
* Ensure that Core Components are enabled for your environment. For detailed instructions on how to enable Core Components for your environment, [click here](/help/forms/enable-adaptive-forms-core-components.md).

## Exploring Invoke Service through different use cases

The Visual rule editor’s **Invoke Service** allows you to perform several useful operations. You can use it to populate dropdown options, set repeatable or simple panels, and validate form fields, all based on the output response of the **Invoke Service**. Thus, enhancing the flexibility and interactivity of your forms.

The table below describes a few scenarios in which the **Invoke Service** can be used:

| **Use Case**                                             | **Description**                                                                                          |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Populate dropdown options using output of Invoke Service**  | Populates dropdown options dynamically based on data retrieved from the Invoke Service output. [Click here](#use-case-1), to see the implementation.         |
| **Set repeatable panel using output of Invoke Service**  | Configures a repeatable panel by using data from the Invoke Service output, allowing for dynamic panels. [Click here](#use-case-2), to see the implementation.   |
| **Set panel using output of Invoke Service**             | Sets the content or visibility of a panel using specific values from the Invoke Service output. [Click here](#use-case-3), to see the implementation.          |
| **Use output parameter of Invoke Service to validate other fields** | Uses specific output parameters from the Invoke Service to validate the form fields. [Click here](#use-case-4), to see the implementation.  |

In our examples, the [Swagger Petstore](https://petstore.swagger.io/) is used to configure a data source. The Form Data Model is set up for the [getPetById](https://petstore.swagger.io/#/pet/getPetById) service, which retrieves pet information based on the entered ID. Rules and logic are created using the **Invoke Service** in the rule editor to demonstrate the above-mentioned use cases.

Let's now explore the implementation of each use case in detail.

### Use Case 1: Populate dropdown options using output of Invoke Service

#### Consideration

#### Implementation

### Use Case 2: Set repeatable panel using output of Invoke Service

#### Consideration

#### Implementation

### Use Case 3: Set panel using output of Invoke Service

#### Consideration

#### Implementation

### Use Case 4: Use output parameter of Invoke Service to validate other fields

#### Consideration

#### Implementation

## Frequently asked questions

**Q: What happens if I have created a rule using the Invoke Service and then upgrade to the latest version of the core components?**

**A:** When you upgrade to the latest version of the core components, the **Invoke Service** rule automatically updates to the latest user interface, as it is backward compatible.

**Q: Can I add multiple rules to handle successful or failure responses for the Invoke Service operation?**

**A:** Yes, you can add multiple rules to handle successful or failure responses for the **Invoke Service** operation.

## Related articles

* [Configure data sources](configure-data-sources.md)
* [Create form data model (FDM)](create-form-data-models.md)
* [Work with form data model (FDM)](work-with-form-data-model.md)
* [Use form data model (FDM)](using-form-data-model.md)


## Additional resources

{{see-also-rule-editor}}

