---
title: Merge and Split Table Cells in Interactive Communication Editor
description: Learn how to combine adjacent table cells into a single cell and split a merged cell back into multiple columns to create flexible table layouts in the Interactive Communication Editor.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: merge-split-table-cells-ic-editor
---

# Merge and Split Table Cells in Interactive Communication Editor


## Introduction

Standard table grids are uniform by default every row has the same number of equally sized cells. Many real-world layouts require more flexibility: a spanning header above multiple columns, a summary row that occupies the full table width, or grouped cells that visually tie related data together. You can merge adjacent cells in a row to achieve these layouts, and split any previously merged cell back into individual columns whenever you need to revise the structure.

| Who | Benefit |
|-----|---------|
| **Author (IC designer / layout designer)** | Build invoices, schedules, and comparison tables with spanning headers or grouped cells without leaving the IC editor. |

## Merge cells

1. In the IC Editor, click the first cell you want to include in the merge.

1. Hold **Shift** and click the last cell in the range to select all consecutive cells within the same row.

1. Right-click the selection and choose **Merge Cells** from the context menu.

   The selected cells are combined into a single merged cell. Content and formatting from the first cell in the selection are preserved; content from subsequent cells is discarded.

**What to keep in mind:**

- You can only merge cells that are consecutive and within the same row. Selecting cells across multiple rows is not supported.
- Only the first cell's content and formatting are retained after the merge.

## Split a merged cell

1. Right-click the merged cell you want to split.

1. Select **Split Cell** from the context menu.

1. In the split dialog, enter the number of columns to split the cell into.

   The **Max Columns** value shown in the dialog represents the maximum you can split into — equal to the number of cells that were originally merged. For example, if three cells were merged, Max Columns is 3.

   | Split value | Result |
   |-------------|--------|
   | 3 | Cell splits back into 3 individual cells |
   | 2 | Cell splits into 2 cells |
   | 1 | Cell remains as a single cell (no change) |

1. Click **OK** to apply.

   The table structure updates automatically. Any value between 1 and the Max Columns value is valid.

## Current limitation

Merging cells that span multiple rows is not fully supported and may produce unexpected results. Perform merge operations only on consecutive cells within the same row.

## Frequently asked questions

**Can I merge cells across rows as well as columns?**
No. Only consecutive cells within the same row can be merged. Cross-row (row-spanning) merges are not fully supported and may produce unexpected results.

**What happens to the content of cells I merge?**
Content and formatting from the first cell in the selection are preserved. Content from the remaining cells is discarded when the merge is applied.

**How do I know the maximum number of columns I can split a merged cell into?**
The split dialog shows the **Max Columns** value, which equals the number of cells that were originally merged to create the cell.

## See also

- [Table Component in Interactive Communication Editor](/help/forms/interactive-communication/table.md)
- [Create Dynamic Table in Interactive Communication Editor](/help/forms/interactive-communication/dynamic-table-in-interactive-communication-editor.md)
- [Create an Interactive Communication](/help/forms/interactive-communication/create-interactive-communication.md)
