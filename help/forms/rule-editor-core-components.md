---
title: How to use the rule editor to add rules to form fields to add dynamic behavior and build complex logic to an adaptive form based on core components?
description: Adaptive Forms rule editor allows you to add dynamic behavior and build complex logic into forms without coding or scripting.
feature: Adaptive Forms, Core Components
role: User, Developer
level: Beginner, Intermediate
exl-id: 1292f729-c6eb-4e1b-b84c-c66c89dc53ae
---

# Introduction to Rule Editor for Adaptive Form based on Core Components

| Version | Article link |
| -------- | ---------------------------- |
| AEM as a Cloud Service (Core Components)    | This article         |
| AEM as a Cloud Service (Foundation Components)    | [Click here](/help/forms/rule-editor.md)       |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-advanced-authoring/rule-editor.html)                  |

In an Adaptive Form based on Core Components, the rule editor feature empowers both business users and developers to write rules for Adaptive Form objects. These rules define actions to trigger on form objects based on preset conditions, user inputs, and user actions on the form. This capability helps to further streamline the form-filling experience, ensuring both accuracy and speed.

The rule editor provides an intuitive and simplified user interface for writing rules. It offers a visual editor that caters to all users, allowing them to create and manage rules without needing extensive technical knowledge. This visual approach makes it easier for users to understand and implement the desired logic within their forms.

Some of the key actions that you can perform on Adaptive Form objects using rules are:

* Show or hide an object
* Enable or disable an object
* Set a value for an object
* Validate the value of an object
* Execute functions to compute the value of an object
* Invoke a Form Data Model (FDM) service and perform an operation
* Set property of an object

<!-- Rule editor replaces the scripting capabilities in [!DNL Experience Manager 6.1 Forms] and earlier releases. However, your existing scripts are preserved in the new rule editor. For more information about working with existing scripts in the rule editor, see [Impact of rule editor on existing scripts](rule-editor.md#p-impact-of-rule-editor-on-existing-scripts-p). -->

Users added to the `forms-power-users` group can create scripts and edit existing ones. Users in the [!DNL forms-users] group can use the scripts but not create or edit scripts.

Refer to the [Difference between the Foundation Rule Editor and the Core Component Rule Editor](/help/forms/rule-editor-core-components-difference-tables.md) article for a detailed comparison. 

<!--
## Difference between Rule editor in Core Components and Rule Editor in Foundation Components

{{rule-editor-diff}}

>[!NOTE]
>
> To see how to create and use custom functions in detail, refer to [Custom functions in Adaptive Forms (Core Components)](/help/forms/create-and-use-custom-functions.md) article.

-->

## Understanding a rule {#understanding-a-rule}

A rule is a combination of actions and conditions. In rule editor, actions include activities such as hide, show, enable, disable, or compute the value of an object in a form. Conditions are Boolean expressions that are evaluated by performing checks and operations on the state, value, or property of a form object. Actions are performed based on the value ( `True` or `False`) returned by evaluating a condition.

The rule editor provides a set of predefined rule types, such as When, Show, Hide, Enable, Disable, Set Value Of, and Validate to help you write rules. Each rule type lets you define conditions and actions in a rule. The document further explains each rule type in detail.

A rule typically follows one of the following constructs:

**Condition-Action** In this construct, a rule first defines a condition followed by an action to trigger. The construct is comparable to the if-then statement in programming languages.

In rule editor, the **When** rule type enforces the condition-action construct.

**Action-Condition** In this construct, a rule first defines an action to trigger followed by conditions for evaluation. Another variation of this construct is action-condition-alternate action, which also defines an alternate action to trigger if the condition returns False.

The Show, Hide, Enable, Disable, Set Value Of, and Validate rule types in the rule editor enforce the action-condition rule construct. By default, the alternate action for Show is Hide and for Enable is Disable, and the opposite way. You cannot change the default alternate action.

>[!NOTE]
>
>The available rule types, including conditions and actions that you define in the rule editor, also depend on the type of form object on which you are creating a rule. The rule editor displays only valid rule types and options for writing condition and action statements for a particular form object type. For example, you do not see Validate and Set Value Of types for a panel object.

For more information about rule types available in the rule editor, see [Available rule types in rule editor](rule-editor.md#p-available-rule-types-in-rule-editor-p).

### Guidelines for choosing a rule construct {#guidelines-for-choosing-a-rule-construct}

While you can achieve most of the use cases by using any rule construct, here are some guidelines to choose one construct over another. For more information about the available rules in rule editor, see [Available rule types in rule editor](rule-editor.md#p-available-rule-types-in-rule-editor-p).

* A typical rule of the thumb when creating a rule is to think about it in the context of the object on which you are writing a rule. Consider that you want to hide or show the field B based on the value a user specifies in the field A. In this case, you are evaluating a condition on field A, and based on the value it returns, you are triggering an action on field B.

  Therefore, if you are writing a rule on field B (the object on which you are evaluating a condition), use the condition-action construct or the When rule type. Similarly, use the action-condition construct or Show or Hide rule type on field A.

* At times, you must perform multiple actions based on one condition. In such cases, it is recommended to use the condition-action construct. In this construct, you can evaluate a condition once and specify multiple action statements.

  For example, to hide fields B, C, and D based on the condition that checks for the value a user specifies in field A, write one rule with condition-action construct or When rule type on field A and specify actions to control the visibility of fields B, C, and D. Otherwise, you need three separate rules on fields B, C, and D, where each rule checks the condition and shows or hides the respective field. In this example, it is more efficient to write the When rule type on one object rather than the Show or Hide rule type on three objects.

* To trigger an action based on multiple conditions, it is recommended to use an action-condition construct. For example, to show and hide field A by evaluating conditions on fields B, C, and D, use the Show or Hide rule type on field A.
* Use condition-action or action condition construct if the rule contains one action for one condition.
* If a rule checks for a condition and performs an action immediately on providing a value in a field or exiting a field, it is recommended to write a rule with a condition-action construct or the When rule type on the field on which the condition is evaluated.
* The condition in the When rule is evaluated when a user changes the value of the object on which the When rule is applied. However, if you want the action to trigger when the value changes on the server side, like for prepopulating the value, it is recommended to write a When rule that triggers the action when the field is initialized.
* When writing rules for drop-downs, radio buttons, or check boxes objects, the options or values of these form objects in the form are pre-populated in the rule editor.

To understand how to use the user interface for writing and managing rules in a Rule Editor,  refer to the [Rule Editor User Interface for Adaptive Forms based on Core Components](/help/forms/rule-editor-core-components-user-interface.md) article.

## See Also

{{see-also-rule-editor}}