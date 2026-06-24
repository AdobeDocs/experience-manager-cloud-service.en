---
title: Versioning and Commenting in Interactive Communication Editor
description: Versioning and Commenting in Interactive Communication Editor in AEM Forms allow organizations to create dynamic, data-driven documents for personalized customer communication.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
exl-id: ca9917c0-d8bb-4381-afab-7ab888d992e8
---
# Versioning and Commenting in Interactive Communication Editor


Interactive Communications allow organizations to create dynamic, data-driven documents for personalized customer communication. To support better collaboration, governance, and controlled publishing workflows, the Interactive Communication Editor provides versioning, reviewing, and commenting capabilities.

These features help authors manage multiple iterations of an Interactive Communication, capture reviewer feedback, revert to earlier versions, and maintain a clear audit trail throughout the content lifecycle.

## Interactive Communication Versioning

Versioning in the Interactive Communication Editor lets authors:

- Create multiple versions of an Interactive Communication

- Save incremental changes with meaningful labels and comments

- Revert to any previous version

- Compare differences visually

- Maintain clean governance for review, approval, and release cycles

This ensures that authors can experiment, iterate, and refine Interactive Communication designs while preserving full historical context.

## Create a Version of an Interactive Communication

Use versioning when you want to preserve the current state of an Interactive Communication before making updates.

To create a new version:

1. Navigate to **Forms & Documents** and select the interactive communication you want to version.

1. In the upper-left corner of the asset view, select the rail toggle, then choose **Timeline** from the panel options.

   ![Create version 1](/help/forms/interactive-communication/assets/create-version1.png)

1. The **Timeline** panel opens on the left and displays the activity history for the selected interactive communication, including annotations and previous versions.

   For example, after a review cycle, the timeline may show annotations such as **update address** and **Update Car Model** alongside other activity entries.

   ![Create version 2](/help/forms/interactive-communication/assets/create-version2.png)

1. At the bottom of the **Timeline** panel, click **Save as Version**.

1. In the **Create new version** dialog, enter a version label and an optional comment describing the purpose or changes in this version.

   For example, enter **Includes new bank logo** as the version comment.

   ![Create version 3](/help/forms/interactive-communication/assets/create-version3.png)

1. Click **Create**.

   The new version entry appears in the timeline and a success message confirms the version was created.

   ![Create version 4](/help/forms/interactive-communication/assets/create-version4.png)

A new version entry is added to the version list, capturing your current Interactive Communication state.

## Update a Version

Each time you modify and save the Interactive Communication, you can create a new version to capture the updated state.

To add a new version after editing:

1. Open **Forms & Documents** and select the interactive communication.

1. Open the **Timeline** panel from the left rail.

1. Follow the steps in [Create a Version of an Interactive Communication](#create-a-version-of-an-interactive-communication) to save the current state with a new label and comment.

This helps teams track progress and ensures transparency in the lifecycle.

## Revert to a Previous Version

If an Interactive Communication needs to return to an earlier configuration:

1. Navigate to **Forms & Documents** and select the interactive communication.

1. Open the **Timeline** panel from the left rail.

1. In the timeline, select the version you want to restore. For example, select **Bank Interactive Communication V1** with the comment **Includes new bank logo**.

   ![Revert version 1](/help/forms/interactive-communication/assets/create-version5.png)

1. Click **Revert to this Version**.

   A success message confirms the interactive communication was restored to the selected version. The timeline records a **Page restored** entry.

   ![Revert version 2](/help/forms/interactive-communication/assets/create-version6.png)

The Interactive Communication is restored to the selected version, allowing authors to undo unwanted changes or recover from errors.

## Compare Two Versions

You can compare any two versions of an Interactive Communication side by side as PDF previews, making it easy to spot layout and static content differences without opening each version individually.

For step-by-step instructions, see [Compare Interactive Communication Versions](/help/forms/interactive-communication/howto/compare-interactive-communication-versions.md).

## Add Comments to an Interactive Communication

Commenting enables reviewers and authors to add general notes directly from the **Timeline** panel in **Forms & Documents**.

To add a comment:

1. Navigate to **Forms & Documents** and select the interactive communication.

1. Open the **Timeline** panel from the left rail.

1. Enter your note in the **Comment** field at the bottom of the **Timeline** panel and save it.

   Comments appear in the timeline alongside annotations, version entries, and other activity. For example, after a review cycle, the timeline may list annotations such as **update address** and **Update Car Model** above general comments and version history.

For positioned, component-level review feedback — where a reviewer pins a comment to a specific field or section on the canvas — use the Annotations feature instead. See [Review and Annotate an Interactive Communication](/help/forms/interactive-communication/howto/review-and-annotate-interactive-communication.md).

## See also

- [Compare Interactive Communication Versions](/help/forms/interactive-communication/howto/compare-interactive-communication-versions.md)
- [Review and Annotate an Interactive Communication](/help/forms/interactive-communication/howto/review-and-annotate-interactive-communication.md)
- [Create an Interactive Communication](/help/forms/interactive-communication/create-interactive-communication.md)

