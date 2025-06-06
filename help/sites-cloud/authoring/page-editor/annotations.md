---
title: Adding Page Annotations
description: Use annotation mode to leave annotations and sketches on pages as you would use sticky notes to assist your content review process
exl-id: a9cb9745-8140-4795-a5f9-fb3a1a299bd8
solution: Experience Manager Sites
feature: Authoring
role: User
---
# Adding Page Annotations {#adding-page-annotations}

Creating content for your digital experience often requires discussion and feedback prior to publication. To aid this feedback process, AEM lets you add annotations to your content.

An annotation places a simple sketch or note (think real-world sticky-note) on the page. The annotation lets you leave comments or questions for other authors and reviewers.

>[!TIP]
>
>Don't forget that [comments](/help/sites-cloud/authoring/basic-handling.md#timeline) are also available for providing feedback on a page.

A special [mode](/help/sites-cloud/authoring/page-editor/introduction.md#mode-selector) is used for creating and viewing annotations.

>[!TIP]
>
>Depending on your requirements you can also develop a [workflow](/help/sites-cloud/authoring/workflows/overview.md) to send notifications when annotations are added, updated, or deleted.

## Annotation Indicator {#annotation-indicator}

Annotations do not appear in Edit mode, but the badge at the top right of the toolbar shows how many annotations exist for the current page. The badge replaces the default Annotations icon, but still functions as a quick link that toggles to/from the Annotate mode:

![Annotation indicator](/help/sites-cloud/authoring/assets/annotation-indicator.png)

## Annotate Mode {#annotate-mode}

Annotations are only visible in Annotate mode.

1. You enter Annotate mode using the icon in the toolbar (top right) when editing a page:

   ![Annotation button](/help/sites-cloud/authoring/assets/annotations.png)

   You can now view any existing annotations.

   ![Annotation examples](/help/sites-cloud/authoring/assets/annotation-sketches.png)

1. Select the annotation to open the annotation dialog and view its details.

   ![Annotation details](/help/sites-cloud/authoring/assets/annotation-adding.png)

1. To exit Annotate mode, and return to the mode previously used, select the x button at the right of the top toolbar.

## Adding and Editing Annotations {#annotating-a-component}

In addition to viewing the annotations, Annotate mode lets you create, edit, move, or delete annotations on your content

1. [Start Annotate mode](#annotate-mode) on the page.

1. Select the Add Annotation icon (plus symbol at the left of the toolbar) to start adding annotations.

1. Select the required component (components that can be annotated are highlighted with a blue border) to add the annotation and open the dialog:

   ![Adding an Annotation](/help/sites-cloud/authoring/assets/annotation-adding.png)

   Here you can use the appropriate field and/or icon to:

    * Enter the annotation text.
    * Create a sketch (lines and shapes) to highlight an area of the component.

      ![Annotation Sketch button](/help/sites-cloud/authoring/assets/annotation-sketch.png)

      The cursor will change to a crosshair when you are creating a sketch. You can draw multiple distinct lines. The sketch line reflects the annotation color and can be either an arrow, circle, or oval.

    * Choose or change the color:

      ![Annotation color swatch button](/help/sites-cloud/authoring/assets/annotation-color-swatch.png)

1. You can close the annotation dialog by clicking or tapping outside the dialog. A truncated view of the annotation, together with any sketches, is shown:

   ![Annotation sketches](/help/sites-cloud/authoring/assets/annotation-sketches.png)

1. After you have finished editing a specific annotation, you can:

    * Select the text marker to open the annotation. Once open you can view the full text, make changes, or [delete the annotation](#deleting-annotations).
    * Reposition the text marker.
    * Select a sketch line to select that sketch and drag it to the desired position.
    * Move or copy a component
        * Any related annotations and their sketches will also be moved or copied but their position in relation to the paragraph will remain the same.


>[!NOTE]
>
>Annotations cannot be added to a page that has been locked by another user.

>[!NOTE]
>
>The definition of an individual component type determines whether adding an annotation is possible (or not) on instances of that component.

## Deleting Annotation and Sketches {#deleting-annotations}

Annotations and their associated sketches can be deleted.

1. [Start Annotate mode](#annotate-mode) on the page.

1. Select the text marker to open the annotation.

1. Select the Delete icon.

   ![Delete annotation](/help/sites-cloud/authoring/assets/annotation-delete.png)

1. The annotation and all associated sketches are deleted.

>[!NOTE]
>
>Deleting a component deletes all the annotations and sketches attached to that resource irrespective of their positions on the page as a whole.

## Deleting Sketches Only {#deleting-sketches}

You can delete only specific sketches instead of the entire annotation with all associated sketches.

1. [Start Annotate mode](#annotate-mode) on the page.

1. Select the sketch. AEM highlights it with a darker blue box.

   ![Select sketch for deletion](/help/sites-cloud/authoring/assets/annotation-sketch-delete.png)

1. Press the Delete key on your keyboard.

1. The sketch is deleted, but the annotation remains.

## Annotating Other Resources {#annotating-other-resources}

Besides components, you can annotate a variety of resources:

* Annotating assets [Annotating assets](/help/assets/manage-digital-assets.md#annotating)
* Annotating video assets [Annotating video assets](/help/assets/manage-video-assets.md#annotate-video-assets)
