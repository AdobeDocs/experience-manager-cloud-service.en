---
title: Adding Page Annotations
description: Many components directly related to content allow you to add an annotation
exl-id: a9cb9745-8140-4795-a5f9-fb3a1a299bd8
---
# Adding Page Annotations {#adding-page-annotations}

Adding content to the pages of your website is often subject to discussions prior to it actually being published. To aid this, many components directly related to content (as opposed, for example, to layout) allow you to add an annotation.

An annotation places a colored sketch or sticky-note on the page. The annotation allows you (or other users) to leave comments and/or questions for other authors/reviewers.

>[!NOTE]
>
>Don't forget that [comments](/help/sites-cloud/authoring/getting-started/basic-handling.md#timeline) are also available for providing feedback on a page.

## Annotations {#annotations}

A special [mode](/help/sites-cloud/authoring/fundamentals/environment-tools.md#page-modes) is used for creating and viewing annotations.

>[!CAUTION]
>
>Deleting a resource (e.g. component) deletes all the annotations and sketches attached to that resource irrespective of their position on the page as a whole.

>[!NOTE]
>
>Depending on your requirements you can also develop a workflow to send notifications when annotations are added, updated, or deleted.

### Annotating a Component {#annotating-a-component}

The Annotate mode allows you to create, edit, move or delete annotations on your content:

1. You can enter Annotate mode using the icon in the toolbar (top right) when editing a page:

   ![Annotation button](/help/sites-cloud/authoring/assets/annotations.png)

   You can now view any existing annotations.

   >[!NOTE]
   >
   >To exit Annotation mode tap/click the Annotate icon (x symbol) at the right of the top toolbar.

1. Click/tap the Add Annotation icon (plus symbol at the left of the toolbar) to start adding annotations.

   >[!NOTE]
   >
   >To stop adding annotations (and return to viewing) tap/click the Cancel icon (x symbol in a white circle) at the left of the top toolbar.

1. Click/tap the required component (components that can be annotated will be highlighted with a blue border) to add the annotation and open the dialog:

   ![Adding an Annotation](/help/sites-cloud/authoring/assets/annotation-adding.png)

   Here you can use the appropriate field and/or icon to:

    * Enter the annotation text.
    * Create a sketch (lines and shapes) to highlight an area of the component.

      ![Annotation Sketch button](/help/sites-cloud/authoring/assets/annotation-sketch.png)

      The cursor will change to a crosshair when you are creating a sketch. You can draw multiple distinct lines. The sketch line reflects the annotation color and can be either an arrow, circle, or oval.

    * Choose/change the color:

      ![Annotation color swatch button](/help/sites-cloud/authoring/assets/annotation-color-swatch.png)

    * Delete the annotation.

      ![Annotation delete button](/help/sites-cloud/authoring/assets/annotation-delete.png)

1. You can close the annotation dialog by clicking/tapping outside the dialog. A truncated view (the first word) of the annotation, together with any sketches, is shown:

   ![Annotation sketches](/help/sites-cloud/authoring/assets/annotation-sketches.png)

1. After you have finished editing a specific annotation, you can:

    * Click/tap the text marker to open the annotation. Once open you can view the full text, make changes or delete the annotation.

        * Sketches cannot be deleted independently of the annotation.

    * Reposition the text marker.
    * Click/tap on a sketch line to select that sketch and drag it to the desired position.
    * Move, or copy, a component

        * Any related annotations and their sketches will also be moved or copied and their position in relation to the paragraph will remain the same.

1. To exit Annotation mode, and return to the mode previously used, tap/click the Annotate icon (x symbol) at the right of the top toolbar.

>[!NOTE]
>
>Annotations can not be added to a page that has been locked by another user.

>[!NOTE]
>
>The definition of an individual component type determines whether adding an annotation is possible (or not) on instances of that component.

## Annotation Indicator {#annotation-indicator}

Annotations do not appear in Edit mode, but the badge at the top right of the toolbar shows how many annotations exist for the current page. The badge replaces the default Annotations icon, but still functions as a quick link that toggles to/from the Annotate mode:

![Annotation indicator](/help/sites-cloud/authoring/assets/annotation-indicator.png)

## Annotating Other Resources {#annotating-other-resources}

Besides components, you can annotate a variety of resources:

* Annotating assets [Annotating assets](/help/assets/manage-digital-assets.md#annotating)
* Annotating video assets [Annotating video assets](/help/assets/manage-video-assets.md#annotate-video-assets)
