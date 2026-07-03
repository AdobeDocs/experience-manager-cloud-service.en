---
title: Review and Annotate an Interactive Communication
description: Learn how reviewers can pin feedback directly to components on the interactive communication canvas and how authors can track and resolve that feedback without leaving the Interactive Communication Editor.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms."
exl-id: review-annotate-interactive-communication
---

# Review and Annotate an Interactive Communication

Reviewing an interactive communication typically means sharing screenshots, composing emails, or holding side conversations, none of which can be tied back to the exact field or section being discussed. Annotations solve this by giving reviewers a dedicated, read-only view of the interactive communication where they can click any component and leave a comment pinned to that exact spot on the canvas.

All reviewers share the same annotation view, so feedback is visible to everyone in one place. Annotations exist only during the authoring and review process, they never appear on published or customer-facing output.

| Who | Benefit |
|-----|---------|
| **Reviewer** | Give precise, in-context feedback without editing the interactive communication or risking accidental changes. |
| **Author (interactive communication designer / owner)** | Receive actionable feedback tied to specific components, with a clear way to track and close each review item. |

## Before you begin

Reviewers and authors must each be assigned to the appropriate out-of-the-box reviewer and author groups before they can access the annotation canvas or the resolve workflow.

>[!NOTE]
>
> Confirm the exact group names for your environment with your AEM administrator before assigning access.

## Add an annotation

Perform these steps as a reviewer.

1. Navigate to **Forms & Documents** and select the interactive communication you want to review and click **Annotate** in the toolbar.

   ![Annotate 1](/help/forms/interactive-communication/assets/add-annotate1.png)

   The read-only **Annotations View** opens with the interactive communication displayed on the canvas.

   ![Annotate 2](/help/forms/interactive-communication/assets/add-annotate2.png)

1. To attach a comment to a specific component, click that component on the canvas.

   ![Annotate 3](/help/forms/interactive-communication/assets/add-annotate3.png)

1. Enter your feedback in the comment box, then click the blue post button to save the comment.

   ![Annotate 4](/help/forms/interactive-communication/assets/add-annotate4.png)

1. Repeat steps 2 and 3 for each component that needs feedback.

   For example, click the bank address block and add **Update Address**, then click the **Make and Model** cell in the Vehicle Details table and add **Update Car Model**.

1. When you have finished adding comments, click **Submit Feedback**.

   ![Annotate 5](/help/forms/interactive-communication/assets/add-annotate5.png)

   A success message confirms your feedback was submitted. Each comment appears as an annotation pin at the location you selected, and all other reviewers can see it immediately.

## Review the annotations

Perform these steps as an author.

1. Navigate to **Forms & Documents**, select the interactive communication, and click **Edit** to open it in the Interactive Communication Editor.

   ![Resolve 1](/help/forms/interactive-communication/assets/add-annotate6.png)

1. Select a component that shows a reviewer annotation pin.

   For example, select the bank address block. In the **Properties** panel, expand the **Comments** section to view the attached annotation. The reviewer comment **update address** appears here.

   ![Resolve 2](/help/forms/interactive-communication/assets/add-annotate7.png)

1. Review each comment and make the necessary changes to the design.

   For example, update the bank address text as requested by the reviewer.

   ![Resolve 3](/help/forms/interactive-communication/assets/add-annotate8.png)

1. Once you have addressed a comment, click **Resolve** in the **Comments** section.

1. Repeat steps 2 through 4 for each remaining annotation.

   For example, select the **Make and Model** cell in the Vehicle Details table, update the value to **Creta SX(O)** as requested in the **Update Car Model** comment, and mark it as **Resolved**.

   ![Resolve 4](/help/forms/interactive-communication/assets/add-annotate9.png)

1. Click **Save**.

   ![Resolve 5](/help/forms/interactive-communication/assets/add-annotate10.png)

   A resolved annotation pin changes from open to closed (grey), distinguishing completed review items from those still outstanding. The resolved comment remains visible in the history so the full review trail is preserved.

## Considerations

- Reviewers and authors must be assigned to the appropriate out-of-the-box groups. Custom group configurations are not supported.

- If you reduce the size of a component after an annotation has been placed on it, the pin remains at the original position rather than moving with the component boundary.

- Annotations on fragments within a document are not supported.

- Annotations on the **Table** component are not yet supported.

## Frequently asked questions

**How do I attach a comment to a specific field rather than a general area?**
Click directly on the component in the annotation canvas. The pin is attached to that component and appears to all reviewers in the same annotation view.

**How does an author know which components have open annotations?**
Annotation pins are visible directly on the canvas in the Interactive Communication Editor. Selecting a component shows all its attached comments in the Properties panel.

**Do annotations appear in the published PDF output?**
No. Annotations are part of the authoring and review workflow only. They are never included in published or customer-facing output.

**What is the difference between an annotation and a comment?**
An annotation is a positioned pin tied to a specific component on the canvas, visible in the read-only annotation view. A comment is a general note attached to the interactive communication as a whole, added from the Comments panel in the editor. See [Versioning and Commenting](/help/forms/interactive-communication/versioning-and-commenting-in-interactive-communication-editor.md) for details on comments.

## See also

- [Create an Interactive Communication](/help/forms/interactive-communication/create-interactive-communication.md)
- [Template Lock in Interactive Communication Editor](/help/forms/interactive-communication/enable-template-lock.md)
- [Versioning and Commenting in Interactive Communication Editor](/help/forms/interactive-communication/versioning-and-commenting-in-interactive-communication-editor.md)

