---
title: Adaptive Form Block components and their properties
description: This document provides an overview of the form components and their properties available in Edge Delivery Services for AEM Forms.
feature: Edge Delivery Services
exl-id: 7d087d41-9313-482a-a905-8955b0999781
role: Admin, Architect, Developer
---
# Adaptive Form Block components and their properties

Edge Delivery Services for AEM Forms allows you to create user-friendly and interactive forms using various components. These components cater to different types of data collection and can be easily customized to fit your specific needs. 


![A sample spreadsheet with some components and properties](/help/edge/assets/sample-form-in-spreadsheet.png)

The Adaptive Forms Block generates a [uniform HTML structure](/help/edge/docs/forms/style-theme-forms.md) for all field types and containers (panels) ensuring the consistency. This consistent structure makes it easier to [style a form](/help/edge/docs/forms/style-theme-forms.md).

## Available components

Here's an overview of the available components:

### Input Fields

* All the valid HTML5 [input types](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types) and [textarea](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea). For example, button, checkbox, color, date, datetime-local, email, file, hidden, image, month, number, password, radio, range, reset, submit, tel, text, time, url, and week. 

### Selection Controls

* [Checkbox groups](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox): For selecting multiple options.
* [Radio groups](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/radio): For selecting a single option from a group.
* [Dropdown menus](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select): To display a menu of options. For example, drop-down box. 

### Containers

* Panels/Containers: To group related form elements together for better organization. It is a combination of the [fieldset](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset) and [legend](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend). 


## Components properties

Each form component comes with various properties that allow you to control its behavior and appearance. Here the properties supported by Adaptive Forms Block components:


| Property     | Applicable Components        | Details                                                              |
|--------------|------------------------------|----------------------------------------------------------------------|
| Type         | All                          | Specifies the type of the component. This property determines the behavior and appearance of the input field. For example, for text inputs, the type may be "text," "email" for email inputs, "password" for password inputs. Adaptive Forms Block supports  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types">all valid HTML5 input types</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea">textarea</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select">select</a>, and <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset">fieldset</a> as type.|
| Name         | All                          | Identifies the component for form submission. The name attribute is used when the form data is submitted to the server, associating the user input with a specific field. |
| Label        | All                          | Provides contextual information to users. The label is the text displayed next to the component, giving users guidance on what information to input. |
| Value        | Text, Password, Email, Number, Range, Date and its variants (datetime-local, month, week, time), Checkbox, Radio, Hidden, Submit, Button               | Specifies the initial value of the component. For text inputs, textarea, and select elements, this is the default text or option displayed. For radio and checkbox components, this is the value/data submitted when they are selected. The value attribute is optional but should be considered mandatory for checkbox and radio inputs. |
| Placeholder  | Text, Tel, Email, Password, Date (and its variants like month, week, time, datetime-local), Number, Range  | Offers hints for expected input. The placeholder attribute provides a brief hint that describes the expected value of the input field. It disappears once the user starts typing. |
| Description  | All                          | Provides additional information about the component and serves as help text. The description field allows for further explanation of the purpose or instructions for filling out the component. It aids users in understanding the context of the input field. |
| Visible      | All                          | Controls initial visibility. The visible attribute is a boolean property that determines whether the component is initially visible or hidden when the form loads. If set to true, the field is shown; otherwise, it is hidden. |
| Mandatory    | Text, Tel, Email, Password, Date and its variants (datetime-local, month, week, time), Number, Checkbox, Radio, File, Select (dropdown), Textarea                      | Indicates whether the field must be filled out before submission. The mandatory attribute is a boolean property used to specify whether the user must provide input for the field before submitting the form. |
| Min          | Date (and its variants like month, week, time, datetime-local), Number, Range  | Specifies the minimum allowed value. The min attribute sets the minimum value that the user can input into the field. For example, for number inputs, it defines the lowest acceptable number. |
| Max          | Date (and its variants like month, week, time, datetime-local), Number, Range            | Specifies the maximum allowed value. The max attribute sets the maximum value that the user can input into the field. For example, for date inputs, it defines the highest acceptable date. |
| Accept       | File             | Defines the allowed file types. The accept attribute is a comma-separated list of unique file type specifiers that restricts the types of files that users can select in a file input field. |
| Multiple     | File     | Allows multiple selections. The multiple attribute is a boolean property used with file input fields. When set to true, it enables users to select more than one files. |
| Options      | Dropdown                     | Specifies choices for dropdown menus. The options property is a comma-separated list of choices for dropdown menus, defining the selectable options displayed to the user. |
| Checked      | Checkbox, Radio              | Determines if the field is selected by default. The checked attribute is a boolean property used with checkbox and radio inputs. When set to true, it indicates that the field is selected by default when the form loads. |
| Fieldset     | All                          | Groups fields to create visually distinct sections within a form. The fieldset element groups related fields within a form, visually separating them to improve organization and user experience. </br> To organize a set of fields within a fieldset, simply use the `fieldset` property and specify its name attribute. In the example below, we demonstrate how radio buttons are encapsulated within a single fieldset for better organization. ![Fieldset example](/help/edge/assets/fieldset-example.png) |
| Repeatable  | All                          | A Boolean property for `fieldset` indicating that a particular fieldset can be repeated for specified `Min` and `Max` number of times. The `Min` property should set to 1 or greater, don't set the `Min` property to 0. |
| Visible Expression  | All                          | A visible expression refers to a spreadsheet formula, denoted by the '=' tag, used for controlling the visibility of a field. In this formula, only the value property of other fields can be employed, allowing straightforward management of field visibility within the system.|
| Value Expression  | All                          | A value expression refers to a spreadsheet formula, denoted by the '=' tag, used for controlling the value of a field. In this formula, only the value property of other fields can be employed, allowing straightforward management of field value within the system. |


## See also

{{see-more-forms-eds}}
