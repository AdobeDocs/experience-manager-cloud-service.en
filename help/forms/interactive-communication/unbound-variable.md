---
title: Unbound Variable Component in Interactive Communication Editor
description: The Unbound Variable component in the Interactive Communication Editor lets you display computed, scripted, or independently set values with full formatting control.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: unbound-variable-ic-editor
---

# Unbound Variable Component in Interactive Communication Editor

[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

## 1. Introduction

The **Unbound Variable** component in the Interactive Communication (IC) editor lets you place a field whose value is not tied to any external data model or schema node. Instead, the value is supplied through scripting, rule-based computation, or a static default, making this component the right choice whenever you need a calculated or intermediate display value that does not come directly from a bound data source.

Because an Unbound Variable is not connected to a Form Data Model, it gives you full authoring control over the value at design time and runtime. You can use it to display computed totals, dynamically generated reference numbers, intermediate formula results, or any other value that your rules engine produces.

The component supports all four data types **Text**, **Numeric**, **Date**, and **Date/Time** and the active data type determines which display pattern syntax and picture clause symbols apply.

## 2. Display Pattern

You can assign a **display pattern** to an Unbound Variable field from the **Properties** panel, using the same display pattern controls available for Text Box, Numeric Field, Date Field, and Date/Time Field components. This allows formatted presentation of computed or referenced values in the canvas preview and in generated output.

The configured pattern is immediately reflected in the canvas preview and is preserved across save and reload cycles.

### Configure a display pattern

1. Select the Unbound Variable component on the design canvas.
2. Open the **Properties** panel.
3. In the **Display Pattern** section, choose a predefined pattern or enter a custom picture clause.
4. Preview the formatted value on the canvas.

### Choosing the right pattern

Because an Unbound Variable can hold any data type, the picture clause syntax you use must match the field's configured data type:

| Field data type | Pattern syntax | Example output | Reference |
|-----------------|----------------|----------------|-----------|
| Text | `text{…}` | (555) 123-4567 | [Text Box — Display Pattern](/help/forms/interactive-communication/text-box.md#2-display-pattern) |
| Numeric | `num{…}` | $1,234.21 | [Numeric Field — Display Pattern](/help/forms/interactive-communication/numeric-field.md#2-display-pattern) |
| Date | `date{…}` | 01/04/2007 | [Date Field — Display Pattern](/help/forms/interactive-communication/date-field.md#2-display-pattern) |
| Date/Time | `date{…} time{…}` | 04/01/2007 14:30 | [Date/Time Field — Display Pattern](/help/forms/interactive-communication/date-time-field.md#2-display-pattern) |

>[!NOTE]
>
> If the field's data type is Date or Date/Time, the underlying value must conform to **ISO 8601** format (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`). Values that do not follow this format are displayed as-is, without the display pattern applied.

## 3. Properties

The Unbound Variable component shares a common property set with other field components, with one key distinction: it has no external data binding options because, by definition, its value is unbound from any data source.

3.1 Basic Field

- **Name:** A unique identifier for the variable. Used to reference it in rules, scripts, and expressions within the IC.

- **Data Type:** Specifies the type of value this variable holds **Text**, **Numeric**, **Date**, or **Date/Time**. The selected data type determines which display pattern syntax applies and how the value is validated.

- **Caption:** The label displayed alongside the field on the canvas (for example, "Computed Total" or "Reference Number").

- **Value:** The default or computed value displayed in the field. In most cases this is set programmatically using the Rule Editor or a script, rather than typed manually.

- **Reserve:** A fallback value displayed when no computed value is available, useful for print-only or read-only output where a blank field is unacceptable.

- **Appearance:** A visual style preset (None, Solid Box, or Underline) for the field container.

3.2 Typography

Controls how the displayed value is styled:

- **Font Variation:** Choose the font family, weight (Regular, Bold), and style (Italic) to match the surrounding content.

- **Font Size:** Typically set to 10 pt by default; adjust to maintain visual consistency with the rest of the communication.

3.3 Position

Defines the component's placement on the canvas:

- **X and Y coordinates:** Set the exact horizontal and vertical position.

- **Width and Height:** Specify dimensions in millimeters to align with adjacent elements.

3.4 Margin

Defines spacing around the component boundary:

- Top (Up)

- Bottom (Down)

- Left

- Right

3.5 Appearance

Styles the field container:

- **Fill:** Background color of the field.

- **Stroke:** Border around the field, with the following options:

  - **Width:** Border thickness.

  - **Style:** Solid, dashed, or dotted.

  - **Edge:** Rounded or sharp corners.

3.6 Presence

Controls visibility at runtime:

- **Visible:** The field is shown and occupies layout space.

- **Hidden (keeps space):** The field is invisible but its layout space is preserved, useful when toggling visibility dynamically using the Rule Editor.

## 4. Usage

Use an Unbound Variable when the value you want to display is:

- **Computed by a rule or script** — for example, a running total, a tax calculation, or a discount amount derived from other field values.

- **Generated programmatically** — for example, a reference number or tracking code assigned at runtime by backend logic.

- **Not available in the data model** — for example, an intermediate result that is meaningful on-screen but does not exist as a schema field.

- **Conditionally visible** — display a computed message or value only when specific conditions are met, using the Rule Editor to set visibility and value together.

You can place an Unbound Variable inside subforms, layout containers, or directly on the design canvas. Combine it with the Rule Editor to write expressions that compute its value based on other bound fields in the IC.

## 5. Best Practices

- **Set a meaningful Reserve value** so that print output and read-only previews never show a blank field when the computed value is unavailable.

- **Match the data type to the output** — if you are computing a currency amount, set the data type to Numeric and apply a numeric display pattern; if computing a date, set it to Date and ensure ISO 8601 input.

- **Use a clear Caption** — since the value is computed and not directly recognizable from a label, a descriptive caption (for example, "Subtotal (computed)") prevents confusion for both reviewers and end users.

- **Avoid overusing Unbound Variables for data that belongs in the model** — if a value could reasonably be added to the Form Data Model, prefer binding a standard field. Reserve Unbound Variables for values that are genuinely transient or derivational.

- **Document your expressions** — add a comment in the Rule Editor describing what each Unbound Variable computes, so the logic remains maintainable when the IC is edited later.

## See also

- [Text Box Component](/help/forms/interactive-communication/text-box.md) — display pattern syntax for text values
- [Numeric Field Component](/help/forms/interactive-communication/numeric-field.md) — display pattern syntax for numeric and currency values
- [Date Field Component](/help/forms/interactive-communication/date-field.md) — display pattern syntax for dates
- [Date/Time Field Component](/help/forms/interactive-communication/date-time-field.md) — display pattern syntax for combined date and time values
- [Use the Rule Editor in Interactive Communication Editor](/help/forms/interactive-communication/use-the-rule-editor.md) — write expressions to compute and assign values to Unbound Variables
- [Configure Data Binding in Interactive Communication Editor](/help/forms/interactive-communication/configure-data-binding.md)
