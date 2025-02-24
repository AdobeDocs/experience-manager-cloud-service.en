---
title: How to use the rule editor to apply rules to form fields, enabling dynamic behavior and complex logic for forms created with WYSIWYG authoring?
description: The rule editor in Universal Editor allows you to add dynamic behavior and build complex logic into forms without coding or scripting.
feature: Edge Delivery Services
role: Admin, Architect, Developer
hide: yes
hidefromtoc: yes
exl-id: 846f56e1-3a98-4a69-b4f7-40ec99ceb348
---

# Introduction to Rule Editor in WYSIWYG Authoring

You can add dynamic form behaviour using the Rule Editor, which allows you to create rules. These rules enable conditional field visibility, automate calculations based on user input, and improve the overall user experience. By streamlining the form-filling process, the Rule Editor helps ensure both accuracy and efficiency.

The Rule Editor offers an intuitive visual interface for creating and managing rules. Its user-friendly approach makes it accessible to all users, even those without extensive technical expertise, allowing them to implement logic effortlessly within their forms.

## Understanding a rule

Rules are instructions that guide users on what actions to perform under specific conditions.

* **Condition**: A condition is a check or rule that evaluates whether something is true or false. It answers the question: "Does this meet the requirement?"

* **Action**: An action is what happens when the condition is true. It is the task or behavior triggered based on the evaluation of the condition.

A rule typically follows one of the following constructs:

* **Condition-Action**: Check a condition first, then perform an action. In the rule editor, the `When` rule type enforces the `condition-action` construct.
* **Action-Condition**: Perform an action first, then check a condition. The `Set Value Of`, and `Validate` rule types in the rule editor enforce the `action-condition` construct.
* **Action-Condition-Alternate Action**: Perform an action, check a condition, and then either perform the main action or an alternate action based on the condition. For example, by default, the alternate action for `Show` is `Hide`, and for `Enable` it is `Disable`.

For example, a condition might check if a user has entered a certain value in a field, and the action could be to show or hide a field.
* **Condition**: Check if the income is greater than $50,000.
* **Action**: If the condition is true, show the `Additional Deduction` field; otherwise, perform the alternate action: hide the `Additional Deduction` field.

For detailed step-by-step instructions, see the [add a conditional rule](#2-add-a-conditional-rule).

## How to enable Rule Editor extension?

In Universal Editor, the Rule Editor extension is not enabled by default. To enable the Rule Editor extension write to us at [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) from your official email id.

After the Rule Editor extension is enabled for your environment, the ![edit-rules](/help/forms/assets/edit-rules-icon.svg) icon appears in the upper-right corner of the editor.

![Universal Editor rule editor](/help/edge/docs/forms/assets/universal-editor-rule-editor.png)

Select the form component for which you want to write a rule, and click the ![edit-rules](/help/forms/assets/edit-rules-icon.svg) icon. The Rule Editor user interface appears.

![Rule Editor user interface](/help/edge/docs/forms/assets/rule-editor-for-field.png)

In this article, `form object` and `form component` are used interchangeably.

Now, you can start writing rules or business logic for the selected form field by using the [available rule types in the Rule Editor](#available-rule-types-in-rule-editor).

## Understanding Rule Editor User Interface

The editor of the Rule Editor opens when you click the ![edit-rules](/help/forms/assets/edit-rules-icon.svg) icon:

![Rule Editor user Interface](/help/edge/docs/forms/assets/rule-editor-interface.png)

<table border="1">
  <thead>
    <tr>
      <th>Component of Rule Editor</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1. Title</td>
      <td>Displays the title of the form component and the selected rule type. For example, 'Enter Gross Salary' is a text box component for which the 'When' rule type is selected. </td>
    </tr>
    <tr>
      <td>2. Form objects and functions</td>
      <td>The <b>Forms Objects</b> tab shows a hierarchical view of all components contained in the form. The <b>Functions</b> tab includes a set of built-in functions in the rule editor.</td>
    </tr>
    <tr>
      <td>3. Form objects and functions toggle</td>
      <td>The toggle button alternately shows or hides the form objects and functions pane. </td>
    </tr>
    <tr>
      <td>4. Visual Rule Editor</td>
      <td>The visual Rule Editor is the interface where you can create rules for the form components.</td>
    </tr>
    <tr>
      <td>5. Done and cancel buttons</td>
      <td>The <b>Done</b> button is used to save a rule. The <b>Cancel</b> button discards any changes that you made to a rule and closes the Rule Editor.</td>
    </tr>
  </tbody>
</table>

Any existing rules on a form component are listed when you select the component. You can view the title and a preview the rule summary on the Rule Editor. Furthermore, you can change the order of rules, edit rules, enable/disbale rules or delete rules.

![show the available rules of form object](/help/edge/docs/forms/assets/rule-editor15.png)

## Available rule types

The Rule Editor provides a set of predefined rule types that you can use to write rules, as displayed in below table:

<table border="1">
  <thead>
    <tr>
      <th>Rule Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Set Value of</td>
      <td>Sets the value of a form component depending on whether the specified condition is satisfied or not.</td>
    </tr>
    <tr>
      <td>Clear Value Of</td>
      <td>Clears the value of the specified form component.</td>
    </tr>
    <tr>
      <td>Hide/Show</td>
      <td>Hides or shows a form component based on whether a condition is satisfied or not.</td>
    </tr>
    <tr>
      <td>Enable/Disable</td>
      <td>Enables or disables a form component based on whether a condition is satisfied or not.</td>
    </tr>
    <tr>
      <td>Validate</td>
      <td>Checks the form component based on a condition and displays an error if the condition is not met. </td>
    </tr>
    <tr>
      <td>When</td>
      <td>It specifies a condition for evaluation followed by an action to trigger if the condition is satisfied. It follows the <i>condition-action-alternate</i> action rule construct or <i>condition-action</i> rule construct. </td>
    </tr>
    <tr>
      <td>Format</td>
      <td> Modifies the display value of the form component using the given expression when its value changes.</td>
    </tr>
    <tr>
      <td>Invoke Service</td>
      <td>Invokes a service configured using external APIs, Form Data Model or RESTful web services.</td>
    </tr>
    <tr>
      <td>Set Property</td>
      <td>Sets the value of a property of the specified form component based on a condition.</td>
    </tr>
    <tr>
      <td>Set Focus</td>
      <td>Sets focus on the specified form component.</td>
    </tr>
    <tr>
      <td>Save Form</td>
      <td>It allows user to save the form as a draft using the Drafts & Submissions Forms Portal component. </td>
    </tr>
    <tr>
      <td>Submit Form</td>
      <td>Submits the form.</td>
    </tr>
    <tr>
      <td>Reset Form</td>
      <td>Resets the form.</td>
    </tr>
    <tr>
      <td>Add/Remove Instance</td>
      <td>Adds or removes an instance of the specified repeatable panel or table row.</td>
    </tr>
    <tr>
      <td>Navigate To</td>
      <td>Navigates to other Adaptive Forms, other assets such as images or document fragments, or an external URL.</td>
    </tr>
    <tr>
      <td>Dispatch Event</td>
      <td>Triggers specific actions based on predefined conditions or events.</td>
    </tr>
    <tr>
      <td>Navigate Among the Panels</td>
      <td>Allows you to shift focus among different panels in a form.</td>
    </tr>
  </tbody>
</table>


Now, let's explore how to [write rules in the Rule Editor](#write-rules).

## Write Rules

To understand how to write rules in Visual Rule Editor, let’s consider an simple example of a tax calculation form: 

![Rule Editor example](/help/edge/docs/forms/assets/rule-editor-1.png)

In the form described above, the user enters the gross salary. Based on this input, conditional field is displayed and the payable tax is calculated. 

**Form Fields:**
* Gross Salary (user input)
* Additional Deduction (conditional field)
* Taxable Income (calculated field)
* Tax Payable (calculated field)

**Conditional Rule:**
  * Condition: Gross Salary > 50,000
  * Action: Show the Additional Deduction field

**Calculation Rules:**

* Taxable Income = Gross Salary - Additional Deduction (if applicable)
* Tax Payable = Taxable Income * Tax Rate (for simplicity, assume a fixed rate of 10%)

To write rules, perform the following steps:

### 1. Author a form

  To author a form in Universal Editor:

   1. Open a form in Universal Editor for editing.
   1. Add the following form components:
      * Tax Calculation Form (Title)
      * Gross Salary (Number Input)
      * Additional Deduction (Number Input)
      * Taxable Income (Number Input)
      * Tax Payable (Number Input)
      * Submit (Submit Button)
   1. Hide the `Additional Deduction` form field, by opening its `Properties`.
   
      ![Rule Editor example](/help/edge/docs/forms/assets/rule-editor2.png)

### 2. Add a conditional rule for a form field

  Once you have authored the form, write the first rule to show the `Additional Deduction` field only if the gross salary exceeds $50,000. To add a conditional rule:

  1. Open a form in Universal Editor for editing and select the **[!UICONTROL Gross Salary]** field in the content tree and select ![edit-rules](/help/forms/assets/edit-rules-icon.svg). Alternatively, you can select **[!UICONTROL Gross Salary]** field directly from the **[!UICONTROL Forms Object]** pane.
    ![Rule Editor example1](/help/edge/docs/forms/assets/rule-editor3.png)
  The visual Rule Editor interface appears.
  1. Click **[!UICONTROL Create]** to create rules.
   ![Rule Editor example2](/help/edge/docs/forms/assets/rule-editor4.png)
  By default, the `Set Value Of` rule type is selected. While you cannot change or modify the selected object, you can use the rule drop-down to select another rule type.  
  ![Rule Editor example3](/help/edge/docs/forms/assets/rule-editor5.png)
  1. Open the rule type drop-down list and select **[!UICONTROL When]** rule type.
  ![Rule Editor example4](/help/edge/docs/forms/assets/rule-editor6.png)
  1. Select **[!UICONTROL Select State]** drop-down and select **[!UICONTROL is greater than]**. The **[!UICONTROL Enter a Number]** field appears.
  ![Rule Editor example5](/help/edge/docs/forms/assets/rule-editor7.png)
  1. Enter `50000` in the **[!UICONTROL Enter a Number]** field in the rule.
  ![Rule Editor example6](/help/edge/docs/forms/assets/rule-editor8.png)
  You have defined the condition as `When Gross Salary is greater than 50000`. Next, define the action to perform if this condition is `True`.
  1. In the `Then` statement, select **[!UICONTROL Show]** from the **[!UICONTROL Select Action]** drop-down.
  ![Rule Editor example7](/help/edge/docs/forms/assets/rule-editor9.png)
  1. Drag-drop the **[!UICONTROL Additional Deduction]** field from the Form Objects tab on the **[!UICONTROL Drop object or select here]** field. Alternatively, select the **[!UICONTROL Drop object or select here]** field and select the **[!UICONTROL Additional Deduction]** field from the pop-up menu, which lists all form objects in the form.
  ![Rule Editor example8](/help/edge/docs/forms/assets/rule-editor10.png)
  1. Click **[!UICONTROL Add Else Section]** to add another condition for the **[!UICONTROL Gross Salary]** field, in case you enter salary less than `50000`.
  ![Rule Editor example9](/help/edge/docs/forms/assets/rule-editor11.png)
  1. Select **[!UICONTROL Hide]** from the **[!UICONTROL Select Action]** drop-down in the `Else` statement.
  ![Rule Editor example10](/help/edge/docs/forms/assets/rule-editor12.png)
  1. Drag-drop the **[!UICONTROL Additional Deduction]** field from the Form Objects tab on the **[!UICONTROL Drop object or select here]** field. Alternatively, select the **[!UICONTROL Drop object or select here]** field and select the **[!UICONTROL Additional Deduction]** field from the pop-up menu, which lists all form objects in the form.
  ![Rule Editor example11](/help/edge/docs/forms/assets/rule-editor13.png)
  1. Select **[!UICONTROL Done]** to save the rule.
  The rule appears as follows in the Rule Editor.
  ![Rule Editor example12](/help/edge/docs/forms/assets/rule-editor14.png)

  >[!NOTE]
  >
  > Alternatively, you can write a Show rule on the Additional Deduction field, instead of a When rule on the Gross Salary field, to implement the same behavior.

### 3. Add calculation rules for the form fields

  Next, write a rule to compute the `Taxable Income`, which is the difference between `Gross Salary` and `Additional Deduction` (if applicable). To add calculation rule on the **[!UICONTROL Taxable Income]** field, perform the following steps:
  
  1. In authoring mode, select the **[!UICONTROL Taxable Income]** field and select ![edit-rules](/help/forms/assets/edit-rules-icon.svg) icon. Alternatively, you can select **[!UICONTROL Taxable Income]** field directly from the **[!UICONTROL Forms Object]** pane.
  1. Next, select **[!UICONTROL Create]** to create the rule.
    ![Rule Editor example13](/help/edge/docs/forms/assets/rule-editor16.png)
  1. Select **[!UICONTROL Select Option]** and select **[!UICONTROL Mathematical Expression]**. A field to write mathematical expression opens.
    ![Rule Editor example14](/help/edge/docs/forms/assets/rule-editor17.png)

  1. In the mathematical expression field:
  
      * Select or drag-drop from the Forms Object tab the **[!UICONTROL Gross Salary]** field in the first **[!UICONTROL Drop object or select here]** field.
  
      * Select **[!UICONTROL Minus]** from the **[!UICONTROL Select Operator]** field.
  
      * Select or drag-drop from the Forms Object tab the **[!UICONTROL Additional Deduction]** field in the other **[!UICONTROL Drop object or select here]** field.
      ![Rule Editor example15](/help/edge/docs/forms/assets/rule-editor18.png)

  1. Select **[!UICONTROL Done]** to save the rule.  
      
      Now, add a rule for the `Tax Payable ` field, which is determined by multiplying the taxable income by the tax rate. For simplicity, assume a fixed tax rate of `10%`.

  1. In authoring mode, select the **[!UICONTROL Tax Payable]** field and select ![edit-rules](/help/forms/assets/edit-rules-icon.svg) icon. Next, select **[!UICONTROL Create]** to create rules.
  ![Rule Editor example16](/help/edge/docs/forms/assets/rule-editor19.png)
  1. Select **[!UICONTROL Select Option]** and select **[!UICONTROL Mathematical Expression]**. A field to write mathematical expression opens.
  ![Rule Editor example17](/help/edge/docs/forms/assets/rule-editor20.png)
  1. In the mathematical expression field:
  
      * Select or drag-drop from the Forms Object tab the **[!UICONTROL Taxable Income]** field in the first **[!UICONTROL Drop object or select here]** field.
  
      * Select **[!UICONTROL Multiplied by]** from the **[!UICONTROL Select Operator]** field.
  
      * Select **Number** from the  **[!UICONTROL Select Option]** field  and enter the value as `10` in the **[!UICONTROL Enter a Number]** field.
      ![Rule Editor example18](/help/edge/docs/forms/assets/rule-editor21.png)
  1. Next, select in the highlighted area around the expression field and select **[!UICONTROL Extend Expression]**.
    ![Rule Editor example19](/help/edge/docs/forms/assets/rule-editor22.png)
  1. In the extended expression field, select **[!UICONTROL divided by]** from the **[!UICONTROL Select Operator]** field and **[!UICONTROL Number]** from the **[!UICONTROL Select Option]** field. Then, specify `100` in the number field.
    ![Rule Editor example20](/help/edge/docs/forms/assets/rule-editor23.png)
  1. Select **[!UICONTROL Done]** to save the rule. 

### 4. Preview a form

Now, when you preview the form and enter the **Gross Salary** as `60,000`, the **Additional Deduction** field appears, and the **Taxable Income** and **Tax Payable** are calculated accordingly.

![Preview a form](/help/edge/docs/forms/assets/rule-editor-form.png)

Apart from the out-of-the-box functions like Sum, Average that are listed under Functions Output, you can [write custom functions](#create-a-custom-function) to implement complex business logics.

## Custom Function in Rule Editor

Edge Delivery Services Forms supports custom functions, that allows users to define JavaScript functions for implementing complex business rules. The custom functions extend the capabilities of forms by facilitating manipulation and processing of entered data to meet specified requirements. 

### Create a custom function

To create a custom functions, edit the `../[blocks]/form/functions.js` file. The creation process generally involves the following steps:

* **Function Declaration**: Define the function name and its parameters (the inputs that it accepts).
* **Logic Implementation**: Write the code that outlines the specific calculations or manipulations performed by the function.
* **Function Export**: Make the function accessible within your rules by exporting it from the relevant file.


This example demonstrates two custom functions as`getFullName` and `days`:  

```JavaScript

/**
 * Get Full Name
 * @name getFullName Concats first name and last name
 * @param {string} firstname in Stringformat
 * @param {string} lastname in Stringformat
 * @return {string}
 */
function getFullName(firstname, lastname) {
  return `${firstname} ${lastname}`.trim();
}

/**
 * Calculate the number of days between two dates.
 * @param {*} endDate
 * @param {*} startDate
 * @name days Calculates the numebr of days between two dates
 * @returns {number} returns the number of days between two dates
 */
function days(endDate, startDate) {
  const start = typeof startDate === 'string' ? new Date(startDate) : startDate;
  const end = typeof endDate === 'string' ? new Date(endDate) : endDate;

  // return zero if dates are valid
  if (Number.isNaN(start.getTime()) || Number.isNaN(end.getTime())) {
    return 0;
  }

  const diffInMs = Math.abs(end.getTime() - start.getTime());
  return Math.floor(diffInMs / (1000 * 60 * 60 * 24));
}

// eslint-disable-next-line import/prefer-default-export
export { getFullName, days };

```
![Adding custom Function](/help/edge/docs/forms/assets/create-custom-function.png)

### Use a Custom Function in Rule Editor

To use the custom function in the Rule Editor:

1. **Add the Function**: Include your custom function in the`../[blocks]/form/functions.js` file. Remember to add it to the `export` statement within the file.
1. **Deploy the File**: Deploy the updated `functions.js` file to your GitHub project and verify a successful build.
1. **Function Usage**: Access the function within your form's Rule Editor by selecting the `Function Output` option in the **[!UICONTROL Select Action]** field.

    ![Custom Function in Rule Editor](/help/edge/docs/forms/assets/custom-function-rule-editor.png)

1. **Preview the form**: Preview your form with the newly implemented function.  

## Additional Information

>[!NOTE]
>
> In Universal Editor, static and dynamic imports are not supported in custom function scripts. You need to add the complete code in the `../[blocks]/form/functions.js` file.

This article provides limited information on the Rule Editor available in the Universal Editor. To learn more about the Rule Editor and custom functions, refer to the following articles:

{{see-also-rule-editor}}

## See also

{{universal-editor-see-also}}
