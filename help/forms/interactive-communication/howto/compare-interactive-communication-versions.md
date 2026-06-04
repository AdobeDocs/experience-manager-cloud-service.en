---
title: Compare Interactive Communication Versions
description: Learn how to open two versions of an Interactive Communication side by side as PDF previews to inspect layout and content differences before publishing.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: compare-interactive-communication-versions
---

# Compare Interactive Communication Versions

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

## Introduction

When an Interactive Communication goes through multiple rounds of editing, it can be difficult to know exactly what changed between two saved states. You can open any two versions side by side as PDF previews, making it straightforward to spot layout shifts, component additions or removals, and static content changes, without having to open each version individually or compare screenshots manually.

| Who | Benefit |
|-----|---------|
| **Author (IC designer / owner)** | Verify that edits between review cycles produced the expected changes before publishing. |
| **Content reviewer** | Confirm that author revisions addressed feedback from a previous version without introducing new issues. |

>[!NOTE]
>
> This comparison covers **layout and static content only**. Dynamic field values populated at runtime are not rendered in the comparison view.

## Before you begin

Make sure you have saved at least two versions of the Interactive Communication you want to compare. To create a version, open the IC, navigate to the **Versions** panel, and select **Save as Version**. See [Create Versions and Add Comments](/help/forms/interactive-communication/versioning-and-commenting-in-interactive-communication-editor.md) for step-by-step instructions.

## Compare two versions

1. Navigate to **Forms > Forms & Documents** in AEM.

1. Locate and select the Interactive Communication you want to compare.

1. Click **Compare Version** from the action toolbar.

1. In the version selector, choose the version you want to compare against the current version.

1. A new tab opens with both versions displayed side by side as PDF previews, the version you selected on one side and the current version on the other.

   Scroll through both previews to inspect layout and content differences page by page.

## Current limitations

- **Large text blocks:** If a paragraph or block of text has been rewritten or rearranged, both pages render identically to their source PDF. There is no inline text-diff, the comparison is visual only, and changed text is not flagged.

- **Dynamic data:** Dynamic field values are not included in the comparison. Only the static layout and content of each version are visible.

## Frequently asked questions

**How many versions can I compare at a time?**
You can compare two versions at a time — the version you select and the current version. They open side by side in a new tab.

**Can I compare a version with a version other than the current one?**
The version selector always compares against the current version. To compare two non-current versions, temporarily revert to the older version, then use Compare Version again.

**Is it possible to download or export the comparison view?**
No. The side-by-side comparison is a visual review tool only — it is not exportable from the editor.

## See also

- [Create Versions and Add Comments](/help/forms/interactive-communication/versioning-and-commenting-in-interactive-communication-editor.md)
- [Review and Annotate an Interactive Communication](/help/forms/interactive-communication/howto/review-and-annotate-interactive-communication.md)
- [Create an Interactive Communication](/help/forms/interactive-communication/create-interactive-communication.md)
