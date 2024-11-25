---
title: Intoduction to scope objects in custom functions
description: Form supports scope objects in custom functions which is passed as a last argument to functions when rule is executed.
keywords: scope objects in custom functions, global objects, field objects.
feature: Adaptive Forms, Core Components
role: User, Developer
exl-id: 248c75a5-6335-41d2-aa0a-28a20a710f88
---
# Scope object in custom functions

In Adaptive Forms, a scope object is passed as the last argument to functions when a rule is executed. It can be used to read form/field properties and modify the form from within the functions. The scope object contains a read-only proxy object for the form, the triggered event, and the target field. Form and field properties can be accessed using the scope object by appending `$`, for example, `scope.form.$id` and `scope.field.$id`, respectively.

## Form modification functions using scope object

Scope object has following functions for form modification:

| Function        | Syntax| Description| Code sample|
|-----------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------|
| **setProperty** | `setProperty(any $element, any $payload)`| Sets a property of the `$element` using the `$payload`.|[Click here](/help/forms/custom-function-core-components-use-cases.md#show-a-panel-using-the-setproperty-rule) to view the example.   |
| **validate**    | `validate([any $element])`| Runs validation on `$element`. If no element is provided, it validates the entire form. | [Click here](/help/forms/custom-function-core-components-use-cases.md#validate-the-field) to view the example.     |
| **reset**| `reset([any $element])`| Resets the `$element`. If no element is provided, it resets the entire form. | [Click here](/help/forms/custom-function-core-components-use-cases.md#reset-a-panel) to view the example.     |
| **importData**  | `importData(any $payload)` | Imports data into the form, replacing any existing form data.|  [Click here](/help/forms/custom-function-core-components-use-cases.md#pre-fill-the-field-with-a-value-when-the-form-loads) to view the example.    |
| **exportData**  | `exportData()`| Returns the form's data.| [Click here](/help/forms/custom-function-core-components-use-cases.md#submit-altered-data-to-the-server) to view the example.     |
| **submitForm**   | `submitForm(any $data [, boolean $validate_form = true, string $submit_as = 'multipart/form-data'])`  | Triggers a form submission. The `$data` parameter specifies what to submit, and `$submit_as` defines the content type (defaults to 'multipart/form-data'). The optional `$validate_form` determines if the form should be validated (default: true). Upon success, `submitSuccess` is fired; on failure, `submitError` is fired.|  [Click here](/help/forms/custom-function-core-components-use-cases.md#submit-altered-data-to-the-server) to view the example.    |
| **setFocus** | `setFocus(any $element [, FocusOption $focusOption])`| Sets focus to the `$element`, which can be a panel or field. If no element is provided, focus is set to the field that triggered the rule. The optional `$focusOption` parameter (of enum type `FocusOption`) specifies whether to focus on the 'nextItem' or 'previousItem' relative to `$element`. If a panel is specified, navigation is restricted to that panel; with a field, navigation happens in the parent panel. |  [Click here](/help/forms/custom-function-core-components-use-cases.md#set-focus-on-the-specific-field) to view the example.    |
| **dispatchEvent**| `dispatchEvent(any $element, string $eventName [, any $payload])`| Dispatches an event of type `$eventName` on the element specified by `$element`. If no element is provided, the event is dispatched on the form. The optional `$payload` is made available to expressions handling the event.|   [Click here](/help/forms/custom-function-core-components-use-cases.md#add-or-delete-repeatable-panel-using-the-dispatchevent-property) to view the example.   |
| **markFieldAsInvalid** | `markFieldAsInvalid(string $fieldIdentifier, string $validationMessage [, any $option = {useId: true}])`       | Marks the field identified by `$fieldIdentifier` as invalid and sets the validation message to `$validationMessage`. The optional `$option` parameter specifies if `$fieldIdentifier` is interpreted as `id`, `name`, or `dataRef`. The default value is `{useId: true}`, and supported values include `{useId: true}`, `{useDataRef: true}`, and `{useQualifiedName: true}`. |  [Click here](/help/forms/custom-function-core-components-use-cases.md#to-display-a-custom-message-at-the-field-level-and-marking-the-field-as-invalid) to view the example.  |

## See Also

{{see-also-rule-editor}}
