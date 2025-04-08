---
title: What are the enhancements to the Invoke service VRE for forms based on Core Components?
description: Enhancements to the Invoke service for the rule editor
feature: Adaptive Forms, Core Components
role: User, Developer
level: Beginner, Intermediate
keywords: invoke service enhancements in VRE, populating drop-down options using invoke service, Set repeatable panel using output of invoke service, Set panel using output of invoke service, Use output parameter of invoke service to validate other field.
exl-id: 2ff64a01-acd8-42f2-aae3-baa605948cdd
---
# Using Invoke Service in the Visual Rule Editor for forms based on Core Components

<span class="preview"> This is a pre-release feature and accessible through our [pre-release channel](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/prerelease.html#new-features). </span>

The Visual Rule Editor in an Adaptive Form supports the **Invoke Service** feature, which allows you to select a service from the list of Form Data Models (FDM) configured for your instance. You can map form fields directly to the input parameters of the service. To map form fields to the output parameters, use the event payload option for the specified Form Data Model service. Additionally, the Visual rule editor allows you to create rules for success and failure handlers for **Invoke Service** operations based on its output responses. Success handlers manage the successful execution of the **Invoke Service** operation, while failure handlers address any errors that occur.

### Advantages of using the Invoke Service in the form's rule editor

Here are few advantages of using Invoke Service operation in the rule editor of an Adaotive Form:

* **Streamlined integration**: Visual Rule Editor simplifies the process of integrating external services or APIs into your Adaptive Forms. By using the **Invoke Service**, you can easily connect forms to various data sources and services without the need for complex coding, making form integration more efficient.

* **Dynamic response handling**: You can manage success and error responses based on the output responses of the **Invoke Service**, allowing forms to react dynamically to different scenarios. It ensures forms handle various conditions appropriately, improving flexibility and control.

* **Enhanced user interaction**: Using the **Invoke Service** in the rule editor enables real-time validation within your forms, providing a better user experience. It also ensures that data is accurately validated on the server side, reducing errors and improving form reliability.

## Invoke Service handlers for success and failure responses

>[!NOTE]
>
> You can use the **Invoke Service** success and failure handlers only for forms based on core components. Forms based on foundation components do not support **Invoke Service** success and failure handlers.

Visual rule editor allows you to create rules for success and failure handlers for **Invoke Service** operations based on its output responses. Below image depicts the **Invoke Service** in Visual rule editor for an Adaptive Form:

![Invoke service handlers](/help/forms/assets/invoke-service-rule-editor.png)

To add success or failure handler, click **[!UICONTROL Add Success Handler]** or **[!UICONTROL Add Failure Handler]**, respectively. 

When you click **[!UICONTROL Add Success Handler]**, the **[!UICONTROL Invoke Service Success Handler]** rule editor appears, allowing you to specify rules or logic to manage the **Invoke Service** output response when the operation is successful. You can specify rules even without defining conditions; however, you can add conditions for the success handler by clicking the **[!UICONTROL Add Condition]** option. 

![Invoke service success hadler](/help/forms/assets/invoke-service-success-handler.png)

You can add multiple rules to handle successful responses for the **Invoke Service** operation:

![Multiple success handler](/help/forms/assets/invoke-service-multiple-success-handlers.png){width=50%, height=50%}

Similarly, you can add rules to handle the **Invoke Service** output response when the operation is not successful. The image below displays the **[!UICONTROL Invoke Service Failure Handler]** rule editor:

![Invoke service failure hadler](/help/forms/assets/invoke-service-failue-handler.png)

You can also add multiple rules to handle unsuccessful responses from the **Invoke Service** operation.

The **Enable Error Validation on Server** feature allows validations added by the author while designing an Adaptive Form to run on the server also.

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
| **Populate dropdown options using output of Invoke Service**  | Populates dropdown options dynamically based on data retrieved from the Invoke Service output. [Click here](#use-case-1-populate-dropdown-values-using-the-output-of-invoke-service), to see the implementation.         |
| **Set repeatable panel using output of Invoke Service**  | Configures a repeatable panel by using data from the Invoke Service output, allowing for dynamic panels. [Click here](#use-case-2-set-repeatable-panel-using-output-of-invoke-service), to see the implementation.   |
| **Set panel using output of Invoke Service**             | Sets the content or visibility of a panel using specific values from the Invoke Service output. [Click here](#use-case-3-set-panel-using-output-of-invoke-service), to see the implementation.          |
| **Use output parameter of Invoke Service to validate other fields** | Uses specific output parameters from the Invoke Service to validate the form fields. [Click here](#use-case-4-use-output-parameter-of-invoke-service-to-validate-other-fields), to see the implementation.  |

Create a `Get Information` form that retrieves values based on the input entered in the `Pet ID` text box. The screenshot below shows the form used in these use cases:

![Get information form](/help/forms/assets/get-information-form.png)

**Form Fields**

Add the following fields to the form:  
* **Enter Pet ID**: Textbox  
* **Select Photo URLs**: Dropdown  
* **Tags**: Panel  
  * Name: Textbox  
  * ID: Textbox  
* **Category**: Panel  
  * Name: Textbox  
* **Submit**: Submit button  

>[!NOTE]
>
> In the **Bind Reference** field in the **Properties** dialog of the form fields, select ![foldersearch_18](assets/folder-search-icon.svg) and navigate to select the binary property you added in the Form Data Model (FDM).

**Configuring panels**  

Set the panels as repetitive with the following constraints:  
* Minimum value: 1  
* Maximum value: 4  

You can adjust the values of the repetitive panels to suit your requirements.  

**Data source** 

In this example, the [Swagger Petstore](https://petstore.swagger.io/) API is used to configure a data source. The [Form Data Model](/help/forms/create-form-data-models.md) is configured for the [getPetById](https://petstore.swagger.io/#/pet/getPetById) service, which retrieves pet details based on the entered ID.  

Let's post the following JSON using the [addPet](https://petstore.swagger.io/#/pet/addPet) service in the [Swagger Petstore](https://petstore.swagger.io/) API:

```
{
        "id": 101,
        "category": {
            "id": 1,
            "name": "Labrador"
        },
        "name": "Lisa",
        "photoUrls": [
            "https://example.com/photos/lisa1.jpg",
            "https://example.com/photos/lisa2.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "vaccinated"
            },
            {
                "id": 2,
                "name": "friendly"
            },
            {
                "id": 3,
                "name": "house-trained"
            }
        ],
        "status": "available"
    }

```


Rules and logic are implemented using the **Invoke Service** action in the rule editor on the `Pet ID` textbox to demonstrate the mentioned use cases.  

Let's now explore the implementation of each use case in detail.

### Use Case 1: Populate dropdown values using the output of Invoke Service  

This use case demonstrates how to populate dropdown options dynamically based on the output of an `Invoke Service`.  

#### Implementation  

To achieve this, create a rule on the `Pet ID` text box to invoke the `getPetById` service. In the rule, set the `enum` property of the `photo-url` dropdown to `photoUrls` in **[!UICONTROL Add Success Handler]**.  

![Set drop-down value](/help/forms/assets/set-dropdownoption.png)  

#### Output  

Enter `101` in the `Pet ID` text box to dynamically populate the dropdown options based on the entered value.  

![Result](/help/forms/assets/output1.png)  

### Use Case 2: Set repeatable panel using output of Invoke Service  

This use case demonstrates how to populate repeatable panels dynamically based on the output of an **Invoke Service**.  

#### Considerations  

* Ensure the name of the repeatable panel matches the parameter of the **Invoke Service** for which you want to set the panel.  
* The panel repeats for the number of values returned by the corresponding **Invoke Service** field.  

#### Implementation  

Create a rule on the `Pet ID` text box to invoke the `getPetById` service. In **[!UICONTROL Add Success Handler]**, add another success handler response. Set the value of the `tags` panel to `tags` in the rule.  

![Create rule for repeatable panel](/help/forms/assets/create-rule-repeatable-panel.png)  

#### Output  

Enter `101` in the `Pet ID` text box to populate the repeatable panel dynamically based on the input value.  

![Output](/help/forms/assets/output2.png)  

### Use Case 3: Set panel using output of Invoke Service  

This use case demonstrates how to dynamically set the value of a panel based on the output of an **Invoke Service**.  

#### Considerations  

* Ensure the name of the panel matches the parameter of the **Invoke Service** for which you want to set the panel.  
* The panel repeats for the number of values returned by the corresponding Invoke Service field.  

#### Implementation  

Create a rule on the `Pet ID` text box to invoke the `getPetById` service. In **[!UICONTROL Add Success Handler]**, add another success handler response. Set the value of the `categoryname` text box to `category.name` in the rule.  

![Create rule for repeatable panel](/help/forms/assets/set-panel-values.png)  

#### Output  

Enter `101` in the `Pet ID` text box to populate the panel dynamically based on the input value.  

![Output](/help/forms/assets/output3.png)  

### Use Case 4: Use output parameter of Invoke Service to validate other fields  

This use case demonstrates how to use the output of an **Invoke Service** to dynamically validate other form fields.  

#### Implementation  

Create a rule on the `Pet ID` text box to invoke the `getPetById` service. In **[!UICONTROL Add Failure Handler]**, add a failure handler response. Hide the **Submit** button if an incorrect `Pet ID` is entered.  

![Failure Handler](/help/forms/assets/create-rule-failure-handler.png)  

#### Output  

Enter `102` in the `Pet ID` text box, and the **Submit** button is hidden. 

![Output](/help/forms/assets/output4.png)  

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
