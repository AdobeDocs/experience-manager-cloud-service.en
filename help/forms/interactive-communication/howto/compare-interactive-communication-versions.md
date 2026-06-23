---
title: Compare Interactive Communication Versions
description: Learn how to open two versions of an Interactive Communication side by side as PDF previews to inspect layout and content differences before publishing.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms."
exl-id: compare-interactive-communication-versions
---

# Compare Interactive Communication Versions

When an Interactive Communication goes through multiple rounds of editing, it can be difficult to know exactly what changed between two saved states. You can open any two versions side by side as PDF previews, making it straightforward to spot layout shifts, component additions or removals, and static content changes, without having to open each version individually or compare screenshots manually.

| Who | Benefit |
|-----|---------|
| **Author (interactive communication designer / owner)** | Verify that edits between review cycles produced the expected changes before publishing. |
| **Content reviewer** | Confirm that author revisions addressed feedback from a previous version without introducing new issues. |

>[!NOTE]
>
> This comparison covers **layout and static content only**. Dynamic field values populated at runtime are not rendered in the comparison view.

## Before you begin

Make sure you have saved at least one version of the Interactive Communication you want to compare against the current design. 

To create a version, open **Forms & Documents**, select the interactive communication, open the **Timeline** panel from the left rail, and click **Save as Version**. See [Versioning and Commenting in Interactive Communication Editor](/help/forms/interactive-communication/versioning-and-commenting-in-interactive-communication-editor.md) for step-by-step instructions.

After saving the version, update the Interactive Communication in the editor so the current design differs from the saved version. You need both a saved version and a modified current state before you can compare them.

## Update the Interactive Communication

After creating a version, open the interactive communication in the Interactive Communication Editor and make your design updates.

For example, after saving **Bank Interactive Communication Version 1**, you might update the bank logo, revise the loan details, and change vehicle information in the table:

- Replace the text-based bank header with a bank logo image
- Update loan details such as the application reference number, approved loan amount, loan tenure, and EMI start date
- Update the **Make and Model** value and dealer name in the Vehicle Details table

![Updated Interactive Communication](/help/forms/interactive-communication/assets/compare-ic1.png)

Click **Save** when you finish editing. The current design is now ready to compare against the saved version.

## Compare two versions

1. Navigate to **Forms & Documents** and select the interactive communication you want to compare.

1. Open the **Timeline** panel from the left rail.

1. In the timeline, locate the saved version you want to compare. For example, select **Bank Interactive Communication Version 1** with the comment **This version includes new bank logo and updated details**.

1. Click **Compare to Current**.

   ![Compare to Current](/help/forms/interactive-communication/assets/compare-ic2.png)

   A new tab opens with both versions displayed side by side as PDF previews. The saved version appears on the left and the current version appears on the right.

   ![Side-by-side comparison](/help/forms/interactive-communication/assets/comapre-ic3.png)

   Scroll through both previews to inspect layout and content differences page by page. For example, the comparison highlights changes to the bank logo, loan details, and vehicle information such as the car model and dealer name.

## Considerations

- **Large text blocks:** If a paragraph or block of text has been rewritten or rearranged, both pages render identically to their source PDF. There is no inline text-diff, the comparison is visual only, and changed text is not flagged.

- **Dynamic data:** Dynamic field values are not included in the comparison. Only the static layout and content of each version are visible.

## Frequently asked questions

**How many versions can I compare at a time?**
You can compare two versions at a time — the version you select and the current version. They open side by side in a new tab.

**Can I compare a version with a version other than the current one?**
The version selector always compares against the current version. To compare two non-current versions, temporarily revert to the older version, then use **Compare to Current** again.

**Is it possible to download or export the comparison view?**
No. The side-by-side comparison is a visual review tool only — it is not exportable from the editor.

## See also

- [Versioning and Commenting in Interactive Communication Editor](/help/forms/interactive-communication/versioning-and-commenting-in-interactive-communication-editor.md)
- [Review and Annotate an Interactive Communication](/help/forms/interactive-communication/howto/review-and-annotate-interactive-communication.md)
- [Create an Interactive Communication](/help/forms/interactive-communication/create-interactive-communication.md)
