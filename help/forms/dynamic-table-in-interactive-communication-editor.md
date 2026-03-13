# Dynamic Tables in Interactive Communication Editor

## Overview

The Interactive Communication Editor provides a Dynamic Table
feature that allows authors to create data-driven tables whose content is populated automatically at runtime from structured data sources.

Unlike static tables where rows must be manually created, dynamic tables automatically expand or contract based on the records returned from a bound JSON data model. This makes them useful for scenarios such as billing statements, transaction histories, product lists, or policy schedules.

This article explains how to insert and configure a dynamic table, bind it to a JSON data source, manage multi-page table flow, and validate row counts.

## Prerequisites

Before creating a dynamic table, ensure the following:

- An Interactive Communication document is created and opened in
    the editor.
- A JSON data model (Form Data Model or sample JSON file) is
    available and referenced by the communication.
- The Print or Web channel layout is configured.
- The layout contains sufficient space to render the expected number
    of rows.

## Key Capabilities

- **JSON data binding per column:** Bind each table column to a specific field in a JSON array.

- **Flowed content for multi-page layout:** Allows the table to grow dynamically and continue across multiple pages.

- **Allow page break within content:** Enables row-level page splitting when the table reaches the end of a page.

- **Minimum row count validation:** Enforces a lower bound on the number of rows rendered.

- **Maximum row count validation:** Limits the total number of rows rendered from the data source.

- **Initial row count control:** Sets the default number of rows displayed during design-time preview.

## Insert a Dynamic Table

1. Open the **Interactive Communication Editor** and select the
    required channel (Print or Web).
2. Select the **editable layout area** where the table should appear.
3. From the **Components panel**, drag the **Table component** to the
    canvas.
4. Specify the **number of columns and initial rows** in the dialog box
    and click **OK**.

>[!NOTE] 
>
> Columns can be added or removed later, but defining them
> correctly during insertion simplifies data binding.

## Bind the Table to JSON Data

To bind the dynamic table to a data source:

1. Select the table and open the **Properties panel**.
2. Under **Data Binding**, click **Bind to Data Model**.
3. In the data model browser, locate the **repeatable data array** in the JSON schema.
4. Select the array node and click **Bind** so the table renders one
row for each data record.

### Bind Column Fields

1. Select a **body cell** in the table (not the header).
2. Click the **Bind icon** in the Data Binding section.
3. Select the corresponding field from the data model.
4. Repeat the process for each column.

## Enable Multi-Page Flow

Dynamic tables may exceed the space of a single page. To allow the table
to continue across pages, place it inside a **Flowed Content**
container.



### Configure Flowed Content

1. Select the **Table Object**.
2. In Properties, set Content Type to **Flowed**.
3. Place or move the table inside this flowed container.
4. Use **Preview mode** to confirm that the table continues onto the
    next page.

>[!NOTE] 
>
> If the document contains repeating headers or footers, ensure the flowed area is positioned between them.

## 5. Allow Page Breaks Within the Table

To allow the table itself to split across pages:

1. Select the **table** in the canvas.
2. Open the **Properties panel**.
3. Locate **Allow Page Break Within Content**.
4. Enable the toggle and save the configuration.

When enabled, the rendering engine automatically inserts a page break
when the table reaches the bottom of the page. The **table header row is
repeated** at the top of the next page.

### Configure Row Validation

1. Select the table and open **Properties**.
2. Navigate to **Validation or Row Settings**.
3. Configure **Minimum Rows**, **Maximum Rows**, and **Initial Rows**.
4. Save the configuration and preview the communication.

>[!NOTE]
>
> Setting **Initial Rows** to around **3--5** provides a more realistic layout preview before runtime data is applied.

The Dynamic Table feature in the Interactive Communication Editor enables authors to create flexible, data-driven tables without writing custom code. By binding the table to a data array, enabling Flowed Content, allowing page breaks, and configuring row validation, authors can produce structured communications that adapt smoothly to varying volumes of data while maintaining a consistent layout.
