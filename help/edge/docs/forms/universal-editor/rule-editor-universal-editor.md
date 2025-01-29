---
title: How to use the rule editor to apply rules to form fields, enabling dynamic behavior and complex logic for forms created with WYSIWYG authoring?
description: The rule editor in Universal Editor allows you to add dynamic behavior and build complex logic into forms without coding or scripting.
feature: Edge Delivery Services
role: Admin, Architect, Developer
---

# Use rules to add dynamic behavior to forms 

You can add dynamic form behaviour using the Rule Editor, which allows you to create rules. These rules enable conditional field visibility, automate calculations based on user input, and improve the overall user experience. By streamlining the form-filling process, the Rule Editor helps ensure both accuracy and efficiency.

The Rule Editor offers an intuitive visual interface for creating and managing rules. Its user-friendly approach makes it accessible to all users, even those without extensive technical expertise, allowing them to implement logic effortlessly within their forms.

Some of the key actions that you can perform on form objects using rules are:

* Show or hide an object
* Enable or disable an object
* Set a value for an object
* Validate the value of an object
* Execute functions to compute the value of an object
* Invoke a Form Data Model (FDM) service and perform an operation
* Set property of an object

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

For detailed step-by-step instructions, see the [show/hide field based on a condition]()

## How to enable Rule Editor extension?

To enable the Rule Editor extension for your environment, send an email from your official address to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) with your request.

After the Rule Editor extension is enabled for your environment, the ![edit-rules](/help/forms/assets/edit-rules-icon.svg) icon appears in the upper-right corner of the editor.

![Universal Editor rule editor](/help/edge/docs/forms/assets/universal-editor-rule-editor.png)

Select the form object for which you want to write a rule, and click the ![edit-rules](/help/forms/assets/edit-rules-icon.svg) icon. The Rule Editor user interface appears.

![Rule Editor user interface](/help/edge/docs/forms/assets/rule-editor-for-field.png)

Now, you can start writing rules or business logic for the selected form field by using the [available rule types in the Rule Editor](#available-rule-types-in-rule-editor).

## Understanding Rule Editor User Interface

The visual editor of the rule editor opens when you click click the ![edit-rules](/help/forms/assets/edit-rules-icon.svg) icon:

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
      <td>1. Component-rule display</td>
      <td>Displays the title of the form object through which you launched the rule editor and the rule type currently selected.</td>
    </tr>
    <tr>
      <td>2. Form objects and functions</td>
      <td>The <b>Forms Objects</b> tab shows a hierarchical view of all objects contained in the form. The <b>Functions</b> tab includes a set of built-in functions.</td>
    </tr>
    <tr>
      <td>3. Form objects and functions toggle</td>
      <td>The toggle button, when tapped, toggles the form objects and functions pane.</td>
    </tr>
    <tr>
      <td>4. Visual rule editor</td>
      <td>The visual rule editor is the area in the visual editor mode of the rule editor user interface where you write rules.</td>
    </tr>
    <tr>
      <td>5. Done and cancel buttons</td>
      <td>The <b>Done</b> button is used to save a rule. The <b>Cancel</b> button discards any changes that you made to a rule and closes the rule editor.</td>
    </tr>
  </tbody>
</table>

Any existing rules on a form object are listed when you select the object. You can view the title and a preview the rule summary on the visual rule editor. Furthermore, you can change the order of rules, edit rules, enable/disbale rules or delete rules.

![show the available rules of form object]()

## Available rule types in Rule Editor

The rule editor provides a set of predefined rule types that you can use to write rules, as displayed in below table:

<table border="1">
  <thead>
    <tr>
      <th></th>
      <th>Rule Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7"><img src="/help/edge/docs/forms/assets/rule-types.png" alt="Available Rule Types in rule Editor" style="width: 100%;"></td>
      <td>Set Value of</td>
      <td>Sets the value of a form object depending on whether the specified condition is satisfied.</td>
    </tr>
    <tr>
      <td>Clear Value Of</td>
      <td>Clears the value of the specified object.</td>
    </tr>
    <tr>
      <td>Hide/Show</td>
      <td>Hides or shows a form object based on whether a condition is satisfied or not.</td>
    </tr>
    <tr>
      <td>Enable/Disable</td>
      <td>Enables or disables a form object based on whether a condition is satisfied or not.</td>
    </tr>
    <tr>
      <td>Validate</td>
      <td>Validates the form or specified object.</td>
    </tr>
    <tr>
      <td>When</td>
      <td>Follows the `condition-action-alternate` action rule construct, or `condition-action` rule construct. It specifies a condition for evaluation followed by an action to trigger if the condition is satisfied.</td>
    </tr>
    <tr>
      <td>Format</td>
      <td> Formats a form object using a function or regular expression (regex).</td>
    </tr>
  </tbody>
</table>

