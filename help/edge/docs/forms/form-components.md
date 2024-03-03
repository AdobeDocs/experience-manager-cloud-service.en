---
title: Form Components and Properties
description: This document provides an overview of the form components and their properties available in AEM Forms Edge Delivery Service.
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
---

# Form Components and Properties: AEM Forms Edge Delivery Service

AEM Forms Edge Delivery Service allows you to create user-friendly and interactive forms using various components. These components cater to different types of data collection and can be easily customized to fit your specific needs. 


![A sample spreadsheet with some components and properties](/help/edge/assets/sample-form-in-spreadsheet.png)

The Adaptive Form Block generates a [uniform HTML structure](/help/edge/docs/forms/style-theme-forms.md) for all field types and containers (panels) ensuring the consistency. This consistent structure makes it easier to [style a form](/help/edge/docs/forms/style-theme-forms.md).

## Available components

Here's an overview of the available components:

### Input Fields

- All the valid HTML5 [input types](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types) and [textarea](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea). For example, button, checkbox, color, date, datetime-local, email, file, hidden, image, month, number, password, radio, range, reset, submit, tel, text, time, url, and week. 

### Selection Controls

- [Checkbox groups](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox): For selecting multiple options.
- [Radio groups](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/radio): For selecting a single option from a group.
- [Dropdown menus](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select): To display a menu of options. For example, drop-down box. 

### Containers

- Panels/Containers: To group related form elements together for better organization. It is a combination of the [fieldset](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset) and [legend](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend). 






## Components properties

Each form component comes with various properties that allow you to control its behavior and appearance. Here the properties supported by Adaptive Form Block components:


| Property     | Applicable Components        | Details                                                              |
|--------------|------------------------------|----------------------------------------------------------------------|
| Type         | All                          | Specifies the type of the component. This property determines the behavior and appearance of the input field. For example, for text inputs, the type may be "text," "email" for email inputs, "password" for password inputs. Adaptive Form block supports  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types">all valid HTML5 input types</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea">textarea</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select">select</a>, and <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset">fieldset</a> as type.|
| Type         | All                          | Specifies the type of the component. This property determines the behavior and appearance of the input field. For example, for text inputs, the type may be "text," "email" for email inputs, "password" for password inputs. Adaptive Form block supports  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types">all valid HTML5 input types</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea">textarea</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select">select</a>, and <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset">fieldset</a> as type.|
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



<!--

## Supported HTML 5 input types in Adaptive Form Block

The Adaptive Form Block supports a range of HTML 5 input types, and it also seamlessly renders forms created with AEM core components.
Here is the table which outlines how core components correspond to their HTML-5 input types in Edge Delivery:
<table>
 <tbody>
  <tr>
   <td><b>Core Components</b> </td>
   <td><b>HTML 5 input type</b> </td>
   <td><b>Details</b></td>
  </tr>
  <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/form-container.html">Form Container</a></td>
   <td><a href ="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#form">form </td>
   <td> Create a form to capture user inputs.
   </td>
  </tr>
  <tr>
   <td><a herf="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/text-input.html">Text Input</a></td>
   <td><a href ="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/text">text</a></td>
   <td> Defines a single-line text input field. </td>
  </tr>
  <tr>
   <td><a href = "https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/number-input.html">Number Input</a></td>
   <td><a href = "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/number">number</a></td>
   <td>Lets user  enter a number input. You can also add built-in validation to reject non-numerical inputs. Lets user  enter a number input. You can also add built-in validation to reject non-numerical inputs. Initially, the input field is displayed as a number input. If a user applies a display pattern, it changes to text to allow the author to apply number formatting, since HTML 5 lacks support for display patterns. However, when the user clicks it, it returns to typing numbers.</td>
  </tr>
  <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/date-picker.html">Date Picker</a></td>
   <td><a href = "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date">date </a></td>
   <td> Create an input field for entering a date. You have the option to input the date either through a text box, which validates the entry, or through a dedicated date picker interface. Initially, the native date input field is displayed. If a user applies a display pattern, it changes to text to allow the user to apply formatting, since HTML 5 lacks support for display patterns. However, when the user clicks it, it returns to typing a date.</td>
  </tr>
  <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/file-attachment.html">File Attachment</a></td>
   <td><a href ="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file">file</a></td>
   <td> Allows user to choose one or more files from the device storage. It supports enhanced file input validations, such as accepted file types, file size restrictions, and minimum/maximum file selection limits. </td>
  </tr>
  <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/drop-down.html"> Dropdown List</a></td>
   <td><a href ="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select">select</a></td>
   <td> Allows users to select one or more options from a list of predefined options. The options can be of type String, Number, or Boolean.</td>
  </tr>
  <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/checkbox-group.html">Checkbox Group</a></td>
   <td><a href ="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox">multiple checkbox</a></td>
   <td> Allow users to select one or more options from a list. Multiple checkboxes are generated with identical names, each corresponding to an item in the enum. </td>
  </tr>
  <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/radio-button.html">Radio Button Group</td>
   <td><a href ="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/radio">multiple radio</a></td>
   <td> Allows a user to select one option from a group of related options. Multiple radio buttons are generated with identical names, each corresponding to an item in the enum.</td>
  </tr>
  <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/button.html">Button</td>
   <td><a href ="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/button">button</a></td>
   <td>A UI element that allows users to trigger an action when clicked. </td>
  </tr>
  <tr>
   <td><a href =""https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel-container.html">Panel</a></td>
   <td><a href ="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset">fieldset with legend</a></td>
   <td> Group sections within a form, where a nested *legend* element adds a caption for the form.</td>
  </tr>
   <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard.html">Wizard</a></td>
   <td><a href ="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset">fieldset</a></td>
   <td>Groups related sections within a form. It also controls the arrangement, supporting display options for positioning them at the top or at the left side. </td>
  </tr>
    <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/text.html">Text</a></td>
   <td><a href ="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p">p</a></td>
   <td>A p tag marks a paragraph. In visual content, paragraphs are chunks of text separated by blank lines or an indented first line</td>
  </tr>
     <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/submit-button.html">Submit button</td>
   <td><a href ="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/submit">submit</a></td>
   <td> A UI element that enables users to submit a form to the server upon clicking. If a user adds a submit rule to a button, it functions as the submit button. </td>
  </tr>
     <tr>
   <td><a href = "https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/reset-button.html">Reset button</a></td>
   <td><a href ="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/reset">reset</a></td>
   <td>A UI element that resets a form upon clicking. If a user adds a reset rule to a button, it functions as the reset button. </td>
  </tr>
    <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/email-input.html">Email Input</td>
   <td><a href ="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email">email</a></td>
   <td> Allows the user to enter and edit an email address. If the user adds the multiple attributes, a list of email addresses can be added or edited.</td>
  </tr>
   <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/telephone-input.html">Telephone Input</a></td>
   <td><a href ="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/tel">tel</a></td>
   <td>Allows user to enter and edit a telephone number.</td>
  </tr>
   <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/header.html">Header</td>
   <td><a href = "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header"> header</a></td>
   <td>It includes introductory content, typically a group of introductory or navigational aids. It is supported outside Form container. </td>
  </tr>
  <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/footer.html">Footer</td>
   <td><a href = "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer">footer</a></td>
   <td> Contains information such as copyright data or links to related documents. It is supported outside Form container.</td>
  </tr>
  <tr>
   <td><a href = "https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion.html">Accordion<a></td>
   <td><i>Not yet supported in Adaptive Form Block</i></td>
   <td> Allows user to create expandable and collapsible sections in a form. </td>
  </tr>
  <tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/horizontal-tabs.html">Horizontal tabs</a></td>
   <td><i>Not yet supported in Adaptive Form Block</i></td>
   <td>Organizes multiple sections of a form into separate tabs which are displayed horizontally.</td>
  </tr>
  <tr>
   <td><a href = "https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/image.html">Image</a></td>
   <td><i>Not yet supported in Adaptive Form Block</i></td>
   <td> Allows user to include images in a form.</td>
  </tr><tr>
   <td><a href ="https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/title.html">Title</a></td>
   <td><i>Not yet supported in Adaptive Form Block</i></td>
   <td> Refers to the text that appears at the top of the form. </td>
  </tr>
  <tr>
   <td><a href = "https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/submit-button.html">Switch</td>
   <td><i>Not yet supported in Adaptive Form Block</i></td>
   <td> A two-state toggle that allows user to select between two states such as enabling or disabling a feature, setting, or functionality.</td>
  </tr>
 </tbody>
</table> -->

## See more

- [Create and preview a form](/help/edge/docs/forms/create-forms.md)
- [Enable form to send data](/help/edge/docs/forms/submit-forms.md)
- [Publish a form to sites page](/help/edge/docs/forms/publish-forms.md)
- [Add validations to form fields](/help/edge/docs/forms/validate-forms.md)
- [Change themes and style of form](/help/edge/docs/forms/style-theme-forms.md)
