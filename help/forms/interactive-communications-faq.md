---
title: Frequently asked questions — Interactive Communications
description: Frequently asked questions about Interactive Communications in AEM Forms as a Cloud Service, covering display patterns, annotations, version compare, and more.
feature: Interactive Communication
role: User, Developer, Admin
exl-id: 4cc1bff3-edfb-4826-b914-2a2231b703f9
---
# Frequently asked questions — Interactive Communications

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

## General

**Q: Can I import an existing XDP into the Interactive Communications editor?**
Yes, you can import an existing XDP and use it as a starting point. Any unsupported features are highlighted during the import process.

**Q: Is the Interactive Communications editor available for on-premise deployments?**
No, the editor is only available for Forms as a Cloud Service deployments.

## Display Patterns

**Q: What is a display pattern and how is it different from data binding?**
A display pattern controls how a field value is *presented* to users in the canvas preview and in generated output — for example, formatting a number as currency ($1,234.21) or a text string as a phone number ((555) 123-4567). The underlying stored value is unchanged. Data binding, by contrast, controls *where* the field value comes from — connecting the field to a data model or schema element.

**Q: Which field types support display patterns?**
Display patterns are supported on Text Box, Numeric Field, Date Field, Date/Time Field, and Unbound Variable components. Each field type uses XFA picture clause syntax appropriate to its data type.

**Q: My date display pattern is not working — the field shows the raw value instead of the formatted output. What is wrong?**
Date and Date/Time fields require the underlying value to conform to **ISO 8601** format. For Date fields, provide values in `YYYY-MM-DD` format (for example, `2007-04-01`). For Date/Time fields, use `YYYY-MM-DDTHH:MM` format (for example, `2007-04-01T14:30`). Values that do not follow ISO 8601 are displayed as-is, without the display pattern applied.

**Q: Can I define a custom pattern that is not in the predefined list?**
Yes. You can enter a custom **XFA picture clause** directly in the Display Pattern field in the Properties panel. Refer to the picture clause symbols for each field type in the respective component reference pages.

## Review and Annotations

**Q: What is the difference between Comments and Annotations in Interactive Communications?**
**Comments** are general notes added to an IC from the Comments panel — they are attached to the document as a whole, not to specific components. **Annotations** are positioned, component-level review pins: a reviewer opens a read-only annotation canvas, clicks any component on the design, and leaves a comment pinned to that exact spot. All reviewers share the same annotation view. Authors can then mark each annotation as Resolved from within the IC Editor.

**Q: Can a reviewer accidentally edit the IC while leaving annotations?**
No. The annotation canvas is a dedicated read-only view. Reviewers can only add or view comment pins — they cannot modify any component in the IC.

**Q: What happens to an annotation after it is marked Resolved?**
Resolved annotations remain visible for history purposes but appear as closed (grey) pins, visually distinguishing them from open (active) feedback items. This allows teams to track review progress without losing the audit trail.

**Q: Are annotations supported on all components?**
Not yet. Annotations on Fragment parts of a document and on the Table component are not currently supported. Annotations on other components are fully supported.

## Version Compare

**Q: What can I see when I compare two versions?**
Both versions open side by side as PDF previews, so you can visually inspect layout and static content differences. Dynamic field values are not included — only the rendered layout and static text are compared.

**Q: How do I start a version comparison?**
Navigate to **Forms > Forms & Documents**, select the IC, click **Compare Version** from the action toolbar, and choose the version to compare. A new tab opens with both versions displayed side by side.

**Q: Can I see specific text changes within a paragraph when comparing versions?**
No. If a paragraph has been rewritten or rearranged, both pages render identically to their source PDF. There is no inline text-diff — the comparison is visual only.

## Tables

**Q: Can I merge cells in a table?**
Yes. Select two or more consecutive cells within the same row, right-click, and choose **Merge Cells**. Only consecutive cells within the same row can be merged. Cross-row merges are not fully supported. See [Merge and Split Table Cells](/help/forms/interactive-communication/howto/merge-and-split-table-cells.md).

**Q: Can I undo a cell merge?**
Yes. Right-click the merged cell, select **Split Cell**, and specify the number of columns to split into (up to the original number of merged cells).

## Master Page

**Q: How do I make a component appear on every page of an Interactive Communication?**
Move the component to the master page. Right-click an eligible component on a design page and select **Move to > Master page**. The component is removed from the design page and placed on the master page at the same visual position, so it appears consistently across all pages that share that master page. See [Move a Component to the Master Page](/help/forms/interactive-communication/howto/move-component-to-master-page.md).

**Q: Which component types cannot be moved to the master page?**
The following types are not eligible for the Move to Master Page action: Content Areas, Page Areas, Page Sets, Fragments, Subform, Table Rows, Table Cells, and Radio Buttons. Components with a content lock or layout lock applied are also ineligible.

