---
title: Add a table to an Adaptive Form (Core Components)
description: Learn to add and configure the Table component in Adaptive Forms based on Core Components. Create structured rows and columns, merge table row cells, enable sorting, set column widths, and add repeatable rows.
feature: Adaptive Forms, Core Components
keywords: table component, adaptive form table, core components table, merge cells, column sorting, repeatable rows
role: User, Developer
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: f4a8c2e1-9b3d-4a7f-8c6e-1d2f3a4b5c6d
---
# Add a table to an Adaptive Form (Core Components) {#tables-in-adaptive-forms-core-components}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5 (Core Components) | [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-core-components/create-an-adaptive-form-core-components.html) |
| AEM as a Cloud Service (Foundation Components) | [Click here](/help/forms/adaptive-forms-tables.md) |
| AEM as a Cloud Service (Core Components) | This article |

Using tables is an effective way to present complex, structured data in Adaptive Forms. Government and financial services forms often require tabular layouts for numeric data, line items, and multi-column inputs.

The **Adaptive Form Table** Core Component lets you author responsive tables with configurable rows and columns, merge and split table row cells, enable column sorting, set proportional column widths, and add or remove rows at runtime. This article describes how to use the Table component in Adaptive Forms based on Core Components.

>[!NOTE]
>
> This article applies to Adaptive Forms based on **Core Components**. If you author forms with Foundation Components, see [Add a table to an adaptive form (Foundation Components)](/help/forms/adaptive-forms-tables.md).

## Key capabilities {#key-capabilities}

The Table Core Component supports the following capabilities:

* Structured row and column authoring with header and body rows
* Column and row headers with accessibility semantics
* Repeatable rows with add and remove actions at runtime
* Column sorting with ascending and descending order
* Disable sorting on individual columns for accessibility compliance
* Proportional column widths 
* Merge and split table row cells
* Replace default text box cells with other Adaptive Form components
* Bind table data to a form data model
* Calculations in table rows using the [Rule Editor](/help/forms/rule-editor-core-components.md)
* Table rendering in [Submission PDF (Document of Record)](/help/forms/generate-document-of-record-core-components.md#tables)

## Comparison with Foundation Component Table {#comparison-with-foundation-component-table}

If you already use the [Foundation Component Table](/help/forms/adaptive-forms-tables.md), most table authoring operations work the same way—adding rows and columns, merging and splitting table row cells, setting column widths, enabling sorting, and adding repeatable rows.

The Core Component Table adds or improves the following compared to the Foundation Component Table:

| Capability | Foundation Component Table | Core Component Table |
| --- | --- | --- |
| Disable sorting on a specific column | Not supported | Supported (accessibility compliance) |
| Calculations in table rows | JavaScript expressions | [Visual Rule Editor](/help/forms/rule-editor-core-components.md) with functions such as Sum, Min, Max, and Average |
| Form data binding | XSD complex types, XDP tables | JSON Schema and Form Data Model bind references |
| Submission PDF (Document of Record) | [Foundation Components guide](/help/forms/generate-document-of-record-for-non-xfa-based-adaptive-forms.md) | [Core Components guide](/help/forms/generate-document-of-record-core-components.md#tables) |
| Component properties | Documented in authoring dialogs | Documented in [Adaptive Forms Core Components documentation](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html) |

## Table structure {#table-structure}

When you add a Table component to an Adaptive Form, the **Content** browser displays the following hierarchy:

* **Table** — the root table container
  * **Header Row** — contains one header cell per column (for example, Column 1, Column 2, Column 3)
  * **Row 1**, **Row 2**, and additional rows — each row contains body cells

Each header cell and body cell is an individual Adaptive Form component. Header cells use the **Text** component by default. Body cells use the **Text Box** component by default.

## Create a table {#create-a-table}

1. Open an Adaptive Form based on Core Components for editing.
1. In the **Components** browser, locate the **Table** component.
1. Drag the **Table** component onto the form canvas.

For table component properties, see the [Adaptive Forms Core Components documentation](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html).

## About header and body cells {#about-header-and-body-cells}

### Edit header labels

Header cells are **Text** components. To change a column header label:

1. Select the header cell in the table.
1. In the toolbar, select **Edit**.
1. Update the header label.
1. Click **Done**.

### Replace body cell components

Body cells are **Text Box** components by default. You can replace a body cell with another Adaptive Form component, such as a **Number Input**, **Date Picker**, or **Drop-down list**:

1. Select the body cell you want to replace.
1. In the toolbar, select **Replace**.
1. Select the component you want to use in the cell, such as **Number Input**.

>[!NOTE]
>
>You can use different component types in different cells within the same row.

## Add or delete a column {#add-or-delete-a-column}

To add or delete a column:

1. Select a header cell in the column you want to modify.
1. In the toolbar, select **Add Column** or **Delete Column**.

When you add a column, a new header cell and corresponding body cells are added to each row. When you delete a column, the header cell and all body cells in that column are removed.

>[!NOTE]
>
> You cannot delete the header row from the table.

## Add, delete, or move a row {#add-delete-move-rows}

To add, delete, or move a row:

1. Select the row where you want to add, delete, or move a row.
1. In the toolbar, select one of the following actions:
   * **Move Up** — moves the selected row up.
   * **Move Down** — moves the selected row down.
   * **Add Row** — adds a row below the selected row.
   * **Delete Row** — deletes the selected row.

## Merge and split table row cells {#merge-and-split-cells}

You can merge adjacent table row cells in the same row to create a single cell that spans multiple columns.

To merge table row cells:

1. Press and hold **Command** (macOS) or **Control** (Windows) and select the adjacent table row cells you want to merge.
1. In the toolbar, select **Merge Cells**.

To split a merged table row cell:

1. Select the merged cell.
1. In the toolbar, select **Split Cell**.

Merged table row cells are useful for labels, subheadings, or fields that span multiple columns within a row.

>[!NOTE]
>
> Row span and header cells that span multiple columns are not supported. See [Limitations](#limitations).

## Set column width {#set-column-width}

You can set proportional column widths using comma-separated values in the table configuration dialog.

1. Select the **Table** component.
1. In the toolbar, select **Configure**.
1. In the **Column Width** field, enter a comma-separated list of values.
1. Click **Done**.

For example, for a table that includes three columns, specifying `2,4,6` as the value in the **Column Width** field sets the width of columns as 2/12 for the first column, 4/12 for the second column, and 6/12 for the third column. 2/12 as the width for the first column refers to one-sixth of the table width. Similarly, 4/12 sets the second column width as one-third of the table width and 6/12 sets the third column width as half of the table width.

>[!NOTE]
>
> The values represent relative proportions, not fixed pixel widths.

## Sort columns {#sort-columns}

You can sort table data by column in ascending or descending order at runtime.

Sorting applies to columns that contain static text, data model properties, or a combination of both. The body cells in a sortable column must contain one of the following components: **Number Input**, **Date Input**, **Date Picker**, **Text**, or **Text Box**.

### Enable sorting on the table

1. Select the **Table** component.
1. In the toolbar, select **Configure**.
1. Select **Enable Sorting**.
1. Click **Done**.
1. Switch to **Preview** mode.

>[!NOTE]
>
> Sorting is enabled by default.

In **Preview** mode, sorting icons appear in the column headers. Click a column header to sort values in ascending or descending order.

### Disable sorting on a specific column

The Core Component Table supports disabling sorting on individual columns. This helps meet accessibility requirements when certain columns should not be sortable.

To disable sorting on a column:

1. Enable sorting on the table.
1. Select the header cell for the column where sorting should be disabled.
1. Disable sorting for that column.

Columns with sorting disabled do not display sorting controls at runtime.

## Add or delete rows dynamically {#add-or-delete-rows-dynamically}

Tables support adding and deleting rows at runtime when a row is configured as repeatable.

1. Select the table row you want to make repeatable.
1. In the toolbar, select **Configure**.
1. Select the **Repeat Panel** tab.
1. Turn on **Make row repeatable**.
1. Specify **Minimum repetitions** and **Maximum repetitions** to control how many row instances a user can add or remove.
1. Click **Done**.
1. Switch to **Preview** mode.

At runtime or in **Preview** mode, users see **Add** and **Delete** buttons to add or remove row instances.

For more information about repeatable behavior, see [Create forms with repeatable sections (Core Components)](/help/forms/create-forms-repeatable-sections.md).

For accessibility guidance when authoring tables, see [Create accessible complex tables in HTML5 forms](/help/forms/accessible-tables.md).

## Use calculations in a table {#use-calculations-in-a-table}

Use the [Rule Editor for Adaptive Forms based on Core Components](/help/forms/rule-editor-core-components.md) to perform calculations in table rows, such as column totals or aggregated values.

The Rule Editor provides out-of-the-box functions such as **Sum**, **Min**, **Max**, and **Average** that you can apply to fields within table rows and repeatable panels. For examples, see [Examples for a Rule Editor for an Adaptive Form Based on Core Components](/help/forms/rule-editor-core-components-usecases.md).

## Include tables in Submission PDF {#include-tables-in-submission-pdf}

Adaptive Form table components such as header rows and body rows map to corresponding components in the generated Submission PDF (Document of Record). You can configure how tables appear in the Submission PDF using table and panel layout settings.

For more information, see:

* [Tables in Submission PDF](/help/forms/generate-document-of-record-core-components.md#tables)
* [Table and column layouts for panels in Submission PDF](/help/forms/generate-document-of-record-core-components.md#table-and-column-layouts-for-panels-in-document-of-record)

## Limitations {#limitations}

Keep the following limitations in mind when authoring tables with Core Components:

* **Row span is not supported.** You can merge table row cells horizontally within a row, but not vertically across rows.
* **Header cells cannot span multiple columns.**
* **Responsive mobile layouts** such as collapsible columns and headers-on-left layouts available in Foundation Components are planned for a future release of the Core Component Table.
* **Theme Editor support** for the Table component is planned for a future release. Use Adaptive Form themes until Theme Editor support is available.
* Each body cell in a default table has a predefined element name. If you add multiple tables to a form, rename default body cell element names to keep them unique and avoid data loss on submission.

## See Also {#see-also}

* [Create an Adaptive Form (Core Components)](/help/forms/creating-adaptive-form-core-components.md)
* [Add a table to an adaptive form (Foundation Components)](/help/forms/adaptive-forms-tables.md)
* [Introduction to Rule Editor for Adaptive Forms based on Core Components](/help/forms/rule-editor-core-components.md)
* [Generate Submission PDF for Adaptive Forms (Core Components)](/help/forms/generate-document-of-record-core-components.md)
* [Create forms with repeatable sections (Core Components)](/help/forms/create-forms-repeatable-sections.md)
