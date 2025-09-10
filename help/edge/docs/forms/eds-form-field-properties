---
title: Mastering Adaptive Forms Block Field Properties
description: Craft powerful forms faster using spreadsheets & Adaptive Forms Block Field Properties! This guide lists all the properties supported by EDS Forms Block. 
feature: Edge Delivery Services
---

# Adaptive Forms Block Field Properties

This document summarizes how JSON schema maps to rendered HTML in `blocks/form/form.js`, focusing on how fields are identified and rendered, common patterns, and field-specific differences.

## How Fields (`fieldType`) Are Identified?

Each field in the JSON schema has a `fieldType` property that determines how it is rendered. The `fieldType` can be:

- **A special type**  
  Examples: `drop-down`, `radio-group`, `checkbox-group`, `panel`, `plain-text`, `image`, `heading`, etc.  
- **A valid HTML input type**  
  Examples: `text`, `number`, `email`, `date`, `password`, `tel`, `range`, `file`, etc.  
- **A type with a `-input` suffix**  
  Examples: `text-input`, `number-input`, etc. (normalized to the base type such as `text`, `number`).

If the `fieldType` matches a special type, a **custom renderer** is used. Otherwise, it is treated as a **default input type**.

See the sections below for the [full HTML structure and properties](#common-html-structure) for each field type.

## Common Properties Used by Fields

Below are the properties used by most fields:

- `id`: Specifies the element ID and supports accessibility.
- `name`: Defines the `name` attribute for input, select, or fieldset elements.
- `label.value`, `label.richText`, `label.visible`: Specifies the label/legend text, HTML content, and visibility.
- `value`: Represents the current value of the field.
- `required`: Adds the `required` attribute or validation data.
- `readOnly`, `enabled`: Controls whether the field is editable or disabled.
- `description`: Displays help text below the field.
- `tooltip`: Sets the `title` attribute for inputs.
- `constraintMessages`: Provides custom error messages as data attributes.

## Common HTML Structure

Most fields are rendered inside a wrapper that includes a label and optional help text. The following snippet demonstrates the structure:

```html
<div class="<fieldType>-wrapper field-wrapper field-<name>" data-id="<id>">
<label for="<id>" class="field-label">Label</label>
<!-- Field-specific input/element here -->
<div class="field-description" id="<id>-description">Description or error
message</div>
</div>
```

For groups (radio/checkbox) and panels, a `<fieldset>` with a `<legend>` is used instead of a `<div>/<label>`. The help text <div> is only present if description is set.

## Error Message Display

Error messages are displayed in the same `.field-description` element used for help text, which is updated dynamically.

**When a field is invalid**:

- The wrapper (e.g., `.field-wrapper`) is assigned the class `.field-invalid`.
- The `.field-description` content is replaced with the corresponding error message.

**When the field becomes valid**:

- The `.field-invalid` class is removed.
- The `.field-description` is restored to the original help text (if available) or removed if none exists.

Custom error messages can be defined using the `constraintMessages` property in the JSON.  
These are added as `data-<constraint>ErrorMessage` attributes on the wrapper (for example, `data-requiredErrorMessage`).

## Default Input Types (HTML Input or `*-input`)

If `fieldType` is not a special type, it is treated as a standard HTML input type or as `<type>-input`, for example, `text`, `number`, `email`, `date`, `text-input`, `number-input`.

- The suffix `-input` is stripped, and the base type is used as the input's `type` attribute.
- These types are handled by default in `renderField()`.
Common default input types are `text`, `number`, `email`, `date`, `password`, `tel`, `range`, `file`, etc.  They also accept `text-input`, `number-input`, etc., which are normalized to the base type.

## Constraints for Default Input Types

Constraints are added as attributes on the input element based on JSON properties.

| JSON Property | HTML Attribute | Applies To |
|--------------|---------------|------------|
| maxLength    | maxlength     | text, email, password, tel |
| minLength    | minlength     | text, email, password, tel |
| pattern      | pattern       | text, email, password, tel |
| maximum      | max           | number, range, date |
| minimum      | min           | number, range, date |
| step         | step          | number, range, date |
| accept       | accept        | file |
| multiple     | multiple      | file |
| maxOccur     | data-max      | panel |
| minOccur     | data-min      | panel |

> [!NOTE]
>
> `multiple` is a boolean property. If true, the `multiple` attribute is added.

These attributes are set automatically by the form renderer based on the field's JSON definition.

## Example: HTML Structure with Constraints

The following example demonstrates how a number field is rendered with validation constraints and error- handling attributes.



```html
<div class="number-wrapper field-wrapper field-age" data-id="age"
data-required="true"
data-minimumErrorMessage="Too small" data-maximumErrorMessage="Too large">
<label for="age" class="field-label">Age</label>
<input type="number"
id="age" name="age"
value="30" required min="18"
max="99" step="1"
placeholder="Enter your age" />
<div class="field-description" id="age-description"> Description or error message
</div>
</div>

```

Each part of the HTML structure plays a role in data binding, validation, and displaying help or error messages.

## Field-Specific Properties and Their HTML Structures

### Drop-down

**Extra Properties:**

- `enum` / `enumNames`: Define the option values and their display labels for the drop-down.
- `type`: Enables multiple selection if set to `array`.
- `placeholder`: Adds a disabled placeholder option to guide users before selection.

Example:

```html
<div class="drop-down-wrapper field-wrapper field-<name>" data-id="<id>"
data-required="true"
data-requiredErrorMessage="This field is required">
<label for="<id>" class="field-label">Label</label>
<select id="<id>" name="<name>" required title="Tooltip" multiple>
<option disabled selected value="">Placeholder</option>
<option value="opt1">Option 1</option>
<option value="opt2">Option 2</option>
</select>
<div class="field-description" id="<id>-description"> Description or error message
</div>
</div>
```

### Plain Text

**Extra Properties**:

- `richText`: If true, renders HTML in the paragraph.

Example:

```html
<div class="plain-text-wrapper field-wrapper field-<name>" data-id="<id>">
<label for="<id>" class="field-label">Label</label>
<p>Text or <a href="..." target="_blank">link</a></p>
</div>
```

### Checkbox

**Extra Properties**:

- `enum`: Defines the values for the checked and unchecked states of the checkbox.
- `properties.variant / properties.alignment`: Specifies the visual style and alignment for switch-style checkboxes.

Example:

```html
<div class="checkbox-wrapper field-wrapper field-<name>" data-id="<id>"
data-required="true"
data-requiredErrorMessage="Please check this box">
<label for="<id>" class="field-label">Label</label>
<input type="checkbox"
id="<id>"
name="<name>" value="on"
required
data-unchecked-value="off" />
<div class="field-description" id="<id>-description"> Description or error message
</div>
</div>
```

### Button

**Extra Properties**:

- `buttonType`: Specifies the button's behavior by setting its type (button, submit, or reset).

Example:

```html
<div class="button-wrapper field-wrapper field-<name>" data-id="<id>">
<button id="<id>" name="<name>" type="submit" class="button"> Label
</button>
</div>
```

### Multiline Input

**Extra Properties**:

- `minLength`: Specifies the minimum number of characters allowed in a text or textarea input.   
- `maxLength`: Specifies the maximum number of characters allowed in a text or textarea input.   
- `pattern`: Defines a regular expression that the input value must match to be considered valid.   
- `placeholder`: Displays placeholder text inside the input or textarea until a value is entered.

Example:

```html
<div class="multiline-wrapper field-wrapper field-<name>" data-id="<id>"
data-minLengthErrorMessage="Too short" data-maxLengthErrorMessage="Too long">
<label for="<id>" class="field-label">Label</label>
<textarea id="<id>"
name="<name>" required
minlength="2"
maxlength="100"
pattern="[A-Za-z]+"
placeholder="Type here..."></textarea>
<div class="field-description" id="<id>-description"> Description or error message
</div>
</div>
```

### Panel

**Extra Properties**:

- `repeatable`: Specifies if the panel can be dynamically repeated.
- `minOccur`: Sets the minimum number of panel instances required.   maxOccur: Sets the maximum number of panel instances allowed.   
- `properties.variant`: Defines the visual style or variant of the panel.
- `properties.colspan`: Specifies how many columns the panel spans in a grid layout.
- `index`: Indicates the panel's position within its parent container.
- `fieldset`: Groups related fields under a `<fieldset>` element with a legend or label.

Example:

```html

<fieldset class="panel-wrapper field-wrapper field-<name>" data-id="<id>"
name="<name>"
data-repeatable="true" data-index="0">
<legend class="field-label">Label</legend>
<!-- Nested fields here -->
<button type="button" class="add">Add</button>
<button type="button" class="remove">Remove</button>
<div class="field-description" id="<id>-description"> Description or error message
</div>
</fieldset>
```

### Radio

**Extra Properties**:

- `enum`: Defines the set of allowed values for the radio field, used as the value attribute for each radio button option.

Example:

```html

<div class="radio-wrapper field-wrapper field-<name>" data-id="<id>"
data-required="true">
<label for="<id>" class="field-label">Label</label>
<input type="radio" id="<id>" name="<name>" value="opt1" required />
<div class="field-description" id="<id>-description"> Description or error message
</div>
</div>
```

### Radio Group

**Extra Properties**:

- `enum`: Defines the list of option values for the radio group, used as each radio button's value.
- `enumNames`: Provides display labels for the radio buttons, matching the order of enum.

Example:

```html
<fieldset class="radio-group-wrapper field-wrapper field-<name>" data-id="<id>"
data-required="true">
<legend class="field-label">Label</legend>
<div>
<input type="radio" id="<id>-0" name="<name>" value="opt1" required />
<label for="<id>-0">Option 1</label>
</div>
<div>
<input type="radio" id="<id>-1" name="<name>" value="opt2" />
<label for="<id>-1">Option 2</label>
</div>
<div class="field-description" id="<id>-description"> Description or error message
</div>
</fieldset>
```

### **Checkbox Group**

**Extra Properties**:

- `enum`: Defines the list of option values for the checkbox group, used as each checkbox's value.
- `enumNames`: Provides display labels for the checkboxes, matching the order of enum.
- `minItems`: Sets the minimum number of checkboxes that must be selected for validity.
- `maxItems`: Sets the maximum number of checkboxes that can be selected before triggering an error.

Example:

```html
<fieldset class="checkbox-group-wrapper field-wrapper field-<name>" data-id="<id>"
data-required="true" data-minItems="1"
data-maxItems="3">
<legend class="field-label">Label</legend>
<div>
<input type="checkbox" id="<id>-0" name="<name>" value="opt1" required />
<label for="<id>-0">Option 1</label>
</div>
<div>
<input type="checkbox" id="<id>-1" name="<name>" value="opt2" />
<label for="<id>-1">Option 2</label>
</div>
<div class="field-description" id="<id>-description"> Description or error message
</div>
</fieldset>
```
 
### Image

**Extra Properties**:

- `value / properties['fd:repoPath']`: Defines the image source path or repository path for rendering the image.
- `altText`: Provides alternative text for the image (alt attribute) to improve accessibility.

Example:

```html
<div class="image-wrapper field-wrapper field-<name>" data-id="<id>">
<picture>
<img src="..." alt="..." />
<!-- Optimized sources -->
</picture>
</div>
```

### Heading

**Extra Properties**:
   
- `value`: Specifies the text content to be displayed inside the heading element (e.g., `<h2>`).

Example:

```html
<div class="heading-wrapper field-wrapper field-<name>" data-id="<id>">
<h2 id="<id>">Heading Text</h2>
</div>
```

For more details, see the implementation in `blocks/form/form.js` and `blocks/form/util.js`.


<!--Each form field is represented as a dedicated row in the spreadsheet, analogous to fields in a database table. The column headers act as labels for the various properties supported by the form field block.

Think of your form as a table in a spreadsheet, where each line represents a different question or piece of information you want to collect. The table headings tell you what kind of answers you can expect for each section.

The below table lists all the properties that are supported by the Adaptive Forms Block.

**Master Your Forms with These Adaptive Forms Block Field Properties:**

This table details all the properties you can use to customize your Adaptive Forms Block fields:

| Property | Description | Example |
|---|---|---|
| **Type** | [HTML input type](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types) (text, email, number, etc.), [textarea](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea), [select](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select), [fieldset](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset) | `text`, `email`, `radio`, `select` |
| **Name** | This defines the unique identifier for submitted data (e.g., 'email' for an email address field).  Choose a clear and unique name for each field, as the name serves as internal field identifier used for data mapping during submission. | `user_name`, `email_address` |
| **Label** | User-friendly field label | `"Full Name"`, `"Choose your country"` |
| **Value** | Default value displayed | `"John Doe"`, `"United States"` |
| **Placeholder** | Hint text within the field | `"Enter your email address"` |
| **Description** | Help text for users | `"Please enter a valid email address"` |
| **Visible** | Show/hide the field initially | `true`, `false` |
| **Mandatory** | Require a value from the user | `true`, `false` |
| **Min/Max** | Set minimum/maximum values (number, date, text length) | `18` (age), `2025-12-31` (date) |
| **Accept** | Allowed file types for file upload | `"image/jpeg,image/png"` |
| **Multiple** | Allow multiple file selections | `true`, `false` |
| **Options** | Comma-separated list for dropdown menus | `"Option 1, Option 2, Option 3"` |
| **Checked** | Default-selected radio button/checkbox | `true`, `false` |
| **Fieldset** | Group fields together | Fieldset name (e.g., `"Personal Information"`) |-->

