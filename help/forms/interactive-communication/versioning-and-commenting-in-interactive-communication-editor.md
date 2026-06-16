---
title: Versioning and Commenting in Interactive Communication Editor
description: Versioning and Commenting in Interactive Communication Editor in AEM Forms allow organizations to create dynamic, data-driven documents for personalized customer communication.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
exl-id: ca9917c0-d8bb-4381-afab-7ab888d992e8
---
# Versioning and Commenting in Interactive Communication Editor


Interactive Communications (IC) allow organizations to create dynamic, data-driven documents for personalized customer communication. To support better collaboration, governance, and controlled publishing workflows, the Interactive Communication Editor provides versioning, reviewing, and commenting capabilities.

These features help authors manage multiple iterations of an IC, capture reviewer feedback, revert to earlier versions, and maintain a clear audit trail throughout the content lifecycle.

## Interactive Communication Versioning

Versioning in the Interactive Communication Editor lets authors:

- Create multiple versions of an IC

- Save incremental changes with meaningful labels and comments

- Revert to any previous version

- Compare differences visually

- Maintain clean governance for review, approval, and release cycles

This ensures that authors can experiment, iterate, and refine IC designs while preserving full historical context.

## Create a Version of an Interactive Communication

Use versioning when you want to preserve the current state of an IC before making updates.

To create a new version:

1. Open AEM and navigate to Forms → Forms & Documents.

1. Select the Interactive Communication you want to version.

1. From the left panel, choose Versions.

1. In the action menu (three dots), select Save as Version.

1. Enter a version label and an optional comment describing the purpose or changes in this version.

1. Save the version.

A new version entry is added to the version list, capturing your current IC state.

## Update a Version

Each time you modify and save the Interactive Communication, you can create a new version to capture the updated state.

To add a new version after editing:

1. Open the IC in the editor and make your updates.

1. Follow the steps in Create a Version of an Interactive Communication.

1. Add a label and comment explaining what has changed.

This helps teams track progress and ensures transparency in the lifecycle.

## Revert to a Previous Version

If an IC needs to return to an earlier configuration:

1. Open Forms & Documents and select the IC.

1. Go to the Versions panel.

1. Select the earlier version you want to restore.

1. Click Revert to this Version.

The IC will be restored to the selected version, allowing authors to undo unwanted changes or recover from errors.

## Compare Two Versions

You can compare any two versions of an Interactive Communication side by side as PDF previews, making it easy to spot layout and static content differences without opening each version individually.

>[!NOTE]
>
> This comparison covers layout and static content only. Dynamic field values are not included.

To compare two versions:

1. Navigate to **Forms > Forms & Documents** in AEM.

1. Select the Interactive Communication you want to compare.

1. Click **Compare Version** from the action toolbar.

1. Choose the version to compare from the version selector.

1. A new tab opens with the selected version and the current version displayed side by side as PDF previews.

**Current limitations:**

- **Large text blocks:** If a paragraph has been rewritten or rearranged, both pages render identically to their source PDF — there is no visual cue that text content has changed.
- **Dynamic data:** Dynamic field values are not rendered in the comparison view. Only static layout and content differences are visible.

For step-by-step instructions, see [Compare Interactive Communication Versions](/help/forms/interactive-communication/howto/compare-interactive-communication-versions.md).

## Add Comments to an Interactive Communication

Commenting enables reviewers and authors to add general notes directly inside the Interactive Communication Editor using the Comments panel.

>[!NOTE]
>
> **Comments vs. Annotations:** The Comments panel supports general notes attached to the IC as a whole. For positioned, component-level review feedback — where a reviewer pins a comment to a specific field or section on the canvas — use the Annotations feature instead. See [Review and Annotate an Interactive Communication](/help/forms/interactive-communication/howto/review-and-annotate-interactive-communication.md).

To add a comment:

1. Select the Interactive Communication in Forms & Documents.

1. Navigate to the Comments panel.

1. Enter your feedback or notes and click **Add Comment**.

Comments help streamline workflows between authors, reviewers, and stakeholders.

>[!NOTE]
>
> When using commenting inside Interactive Communications, the standalone "Review and Approval" workflow for forms is automatically disabled.

Together, these tools give teams:

- Structured content governance

- Simplified collaboration

- Traceable change history

- Easy rollback and comparison

Use them to maintain controlled authoring, meet compliance requirements, and iterate confidently throughout the lifecycle of customer communications.

## See also

- [Compare Interactive Communication Versions](/help/forms/interactive-communication/howto/compare-interactive-communication-versions.md)
- [Review and Annotate an Interactive Communication](/help/forms/interactive-communication/howto/review-and-annotate-interactive-communication.md)
- [Create an Interactive Communication](/help/forms/interactive-communication/create-interactive-communication.md)
