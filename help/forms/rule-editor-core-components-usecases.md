---
title: This article outlines various use cases for a rule editor in an Adaptive Form based on core components.
description: The article outlines various use cases for a rule editor in an Adaptive Form based on core components.
feature: Adaptive Forms, Core Components
role: User, Developer
level: Beginner, Intermediate
exl-id: 8191e113-f768-4b1e-a191-e3c722f19054
---
# Different use cases of Rule Editor

The article provides detailed examples of a Rule Editor for an Adaptive Form based on core components, providing insights into its proper implementation for different scenarios. The rule editor allows developers to define and manage the logic controlling the behavior of forms. 
Now, let us discuss the different implementations for a rule editor.


## Navigating among panels using button 

The rule editor allows you to add navigation buttons to your panel layouts, such as Horizontal Tabs, Vertical Tabs, Accordions, or Wizard. These buttons enhance the user experience by simplifying transitions among different panels in a form, shifting focus to the selected panel.

Imagine you are interacting with the profile settings section of an application, where navigation is facilitated by buttons rather than tabs. Upon entering the profile settings from the main dashboard, you encounter a series of panels dedicated to different aspects of their profile: **Personal Information**, **Account Security**, and **Notification Preferences**.

Each panel contains relevant fields and options for updating specific information. Navigation buttons, such as `Next` and `Back`, are prominently placed allow you to move between these panels. Click `Next` to advance the user to the **Account Security** panel and click `Back` to return to the **Personal Information** panel. This method of navigation ensures a seamless transition between sections without losing context, providing a smooth and intuitive user experience. The use of navigation buttons simplifies the process of managing profile settings, making the interaction more organized and user-friendly.

You can use the `Navigate among the panels` rule to create navigation rules for buttons that allow switching between different panels.  Select the `Shift focus to the next item` attribute to move the focus to the next panel in the layout.

![Next panel rule](/help/forms/assets/rule-editor-navigate-in-panel-next.png){width=50%}

When the `Next` button is clicked, focus moves to the subsequent panel in the layout.

![Navigate in panel using Next button](/help/forms/assets/navigate-in-panel.gif)

Similarly, you can create a rule for the `Previous` button to shift focus to the preceding panel.

![Previous panel rule](/help/forms/assets/rule-editor-navigate-in-panel-previous.png){width=50%}

## Streamline complex calculations in repeatable panels with functions

The rule editor allows you to use out-of-the-box functions like Sum, Min, Max, and Join directly on fields within repeatable panels. You can also pass a repeatable panel field value to the function that accepts number array, string array, boolean array etc. This unlocks powerful automation, allowing you to implement complex business logic without custom code.

Imagine a form with a repeatable panel, where each panel instance collects information about the declared value of assets. 

![Repeatable form](/help/forms/assets/ootb-function-support-repeatable-panel-form.png)

You can use the `Sum` function to automatically calculate the total assets value across all panels, eliminating the need for manual calculations and reducing the potential for errors. 

![Support for repeatable panel fields in OOTB functions](/help/forms/assets/ootb-function-support-repeatable-panel.png)

When you fill out a form, adding instances to declare the asset values, the `Calculate Asset Value` button computes the total sum of all declared asset values and displays the result in the total in `assetvalue` textbox.

![Support for repeatable panel fields in OOTB functions](/help/forms/assets/ootb-function-support-repeatable-panel-form-preview.png)

>[!NOTE]
>
> In case the value of the repeatable panel field is passed to a function that does not accept an array, the field value from the last instance of the repeatable panel is passed to the function.

This is just one example! Explore the available [functions](#b-form-objects-and-functions-br) to simplify workflows and enhance data accuracy within your forms.

## Nested expressions {#nestedexpressions}

Rule editor lets you use multiple AND and OR operators to create nested rules. You can mix multiple AND and OR operators in the rules.

The following is an example of a nested rule that displays a message to the user about eligibility for a child's custody when the required conditions are met.

![Complex expression](assets/complexexpression.png)

You can also drag-and-drop conditions within a rule to edit it. Select and hover over the handle ( ![handle](assets/drag-handle.svg)) before a condition. Once the pointer turns into the hand symbol as shown below, drag and drop the condition anywhere within the rule. The rule structure changes.

![Drag-and-drop](assets/drag-and-drop.png)

## Date expression conditions {#dateexpression}

Rule editor lets you use date comparisons to create conditions.

The following is an example condition that displays a static text object if the mortgage on the house is already taken, which the user signifies by filling up the date field.

When the date of mortgage of the property as filled in by the user is in the past, the Adaptive Form displays a note about the income calculation. The following rule compares the date filled in by the user with the current date and if the date filled in by the user is earlier than the current date, the form displays the text message (named Income).

![Date expression condition](assets/dateexpressioncondition.png)

When filled date is earlier than the current date, the form displays the text message (Income) as following:

![Date expression condition met](assets/dateexpressionconditionmet.png)

## Number comparison conditions {#number-comparison-conditions}

Rule editor lets you create conditions that compare two numbers.

Following is an example condition that displays a static text object if the number of months an applicant is staying at current address is less than 36.

![Number comparison condition](assets/numbercomparisoncondition.png)

When the user signifies living at the present residential address for less than 36 months, the form displays a notification that more proof of residence can be requested.

![More proof requested](assets/additionalproofrequested.png)

<!-- ## Impact of rule editor on existing scripts {#impact-of-rule-editor-on-existing-scripts}

In [!DNL Experience Manager Forms] versions prior to [!DNL Experience Manager 6.1 Forms] feature pack 1, form authors and developers used to write expressions in the Scripts tab of the Edit component dialog to add dynamic behavior to Adaptive Forms. The Scripts tab is now replaced by the rule editor.

Any scripts or expressions that you must have written in the Scripts tab are available in the rule editor. While you cannot view or edit them in visual editor, if you are a part of the forms-power-users group you can edit scripts in code editor. -->

### Invoke Form Data Model service {#invoke}

Consider a web service `GetInterestRates` that takes loan amount, tenure, and applicant's credit score as input and returns a loan plan including EMI amount and rate of interest. You create a Form Data Model (FDM) using the web service as a data source. You add data model objects and a `get` service to the form model. The service appears in the Services tab of the form data model (FDM). Then, create an Adaptive Form that includes fields from data model objects to capture user inputs for loan amount, tenure, and credit score. Add a button that triggers the web service to fetch plan details. The output is populated in appropriate fields.

The following rule shows how you configure the Invoke service action to accomplish the example scenario.

![Example-invoke-services](assets/example-invoke-services.png)

>[!NOTE]
>
>If the input is of array type, the fields that support arrays are visible under the Output drop-down section.

### Triggering multiple actions using the When rule {#triggering-multiple-actions-using-the-when-rule}

In a loan application form, you want to capture whether the loan applicant is an existing customer or not. Based on the information, user provides, the customer ID field should show or hide. Also, you want to set focus on the customer ID field if the user is an existing customer. The loan application form has the following components:

* A radio button, **[!UICONTROL Are you an existing Geometrixx customer?]**, which provides [!UICONTROL Yes] and [!UICONTROL No] options. The value for Yes is **0** and No is **1**.

* A text field, **[!UICONTROL Geometrixx customer ID]**, to specify the customer ID.

When you write a When rule on the radio button to implement this behavior, the rule appears as follows in the visual rule editor.  

![When-rule-example](assets/when-rule-example.png)

In the example rule, the statement in the When section is the condition, which when returns True, executes the actions specified in the Then section.

<!-- The rule appears as follows in the code editor.

![when-rule-example-code](assets/when-rule-example-code.png) 

Rule in the code editor -->

### Using a function output in a rule {#using-a-function-output-in-a-rule}

In a purchase order form, you have the following table, in which users fill in their orders. In this table:

* The first row is repeatable, so users can order multiple products and specify different quantities. Its element name is `Row1`.
* The title of the cell in the Product Quantity column of the repeatable row is Quantity. The element name for this cell is `productquantity`.
* The second row in the table is non-repeatable and the title of the cell in the Product Quantity column in this row is Total Quantity.

![Example-function-table](assets/example-function-table.png)

**A.** Row1 **B.** Quantity **C.** Total Quantity

Now, you want to add specified quantities in the Product Quantity column for all products and display the sum in the Total Quantity cell. You can achieve this sum by writing a Set Value Of rule on the Total Quantity cell as shown below.

![Example-function-output](assets/example-function-output.png)

### Validating a field value using expression {#validating-a-field-value-using-expression}

In the purchase order form explained in the previous example, you want to restrict the user from ordering more than one quantity of any product that is priced more that 10000. To do this validation, you can write a Validate rule as shown below.

![Example-validate](assets/example-validate.png)

## See Also

{{see-also-rule-editor}}
