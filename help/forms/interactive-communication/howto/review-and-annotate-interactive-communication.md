---
title: Review and Annotate an Interactive Communication
description: Learn how reviewers can pin feedback directly to components on the IC canvas and how authors can track and resolve that feedback without leaving the Interactive Communication Editor.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: review-annotate-interactive-communication
---

# Review and Annotate an Interactive Communication

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

## Introduction

Reviewing an Interactive Communication (IC) typically means sharing screenshots, composing emails, or holding side conversations, none of which can be tied back to the exact field or section being discussed. Annotations solve this by giving reviewers a dedicated, read-only view of the IC where they can click any component and leave a comment pinned to that exact spot on the canvas.

All reviewers share the same annotation view, so feedback is visible to everyone in one place. Annotations exist only during the authoring and review process, they never appear on published or customer-facing output.

| Who | Benefit |
|-----|---------|
| **Reviewer** | Give precise, in-context feedback without editing the IC or risking accidental changes. |
| **Author (IC designer / owner)** | Receive actionable feedback tied to specific components, with a clear way to track and close each review item. |

## Before you begin

Reviewers and authors must each be assigned to the appropriate out-of-the-box reviewer and author groups before they can access the annotation canvas or the resolve workflow.

>[!NOTE]
>
> Confirm the exact group names for your environment with your AEM administrator before assigning access.

## Leave an annotation

*Perform these steps as a reviewer.*

1. Open the IC in the read-only annotation view.

1. To attach a comment to a specific component, click that component on the canvas. To leave a general comment not tied to a component, drag the comment cursor to any open area of the canvas.

1. Enter your feedback in the comment box and save it.

   The comment appears as an open annotation pin at the location you selected. All other reviewers can see it immediately.

1. Repeat for each component or area that needs feedback.

## View and resolve annotations

*Perform these steps as an author.*

1. Open the IC in the Interactive Communication Editor.

1. Select a component that shows reviewer annotation pins.

1. Open the **Properties** panel. All annotations attached to that component are listed there.

1. Review each comment, then make the necessary changes to the design.

1. Once you have addressed a comment, mark it as **Resolved**.

   A resolved annotation pin changes from open to closed (grey), distinguishing completed review items from those still outstanding. The resolved comment remains visible in the history so the full review trail is preserved.

## Current limitations

- Reviewers and authors must be assigned to the appropriate out-of-the-box groups. Custom group configurations are not supported.

- If you reduce the size of a component after an annotation has been placed on it, the pin remains at the original position rather than moving with the component boundary.

- Annotations on fragments within a document are not supported.

- Annotations on the **Table** component are not yet supported.

## Frequently asked questions

**How do I attach a comment to a specific field rather than a general area?**
Click directly on the component in the annotation canvas. The pin is attached to that component and appears to all reviewers in the same annotation view.

**How does an author know which components have open annotations?**
Annotation pins are visible directly on the canvas in the IC Editor. Selecting a component shows all its attached comments in the Properties panel.

**Do annotations appear in the published PDF output?**
No. Annotations are part of the authoring and review workflow only. They are never included in published or customer-facing output.

**What is the difference between an annotation and a comment?**
An annotation is a positioned pin tied to a specific component on the canvas, visible in the read-only annotation view. A comment is a general note attached to the IC as a whole, added from the Comments panel in the editor. See [Versioning and Commenting](/help/forms/interactive-communication/versioning-and-commenting-in-interactive-communication-editor.md) for details on comments.

## See also

- [Create an Interactive Communication](/help/forms/interactive-communication/create-interactive-communication.md)
- [Template Lock in Interactive Communication Editor](/help/forms/interactive-communication/enable-template-lock.md)
- [Versioning and Commenting in Interactive Communication Editor](/help/forms/interactive-communication/versioning-and-commenting-in-interactive-communication-editor.md)
