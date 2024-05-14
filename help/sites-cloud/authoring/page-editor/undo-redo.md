---
title: Undo and Redo Limitations
description: Learn about the limitations of the undo and redo options in the AEM page editor.
exl-id: 87773f47-5116-4966-9ba4-5deedb7c4fa6
---
# Undo and Redo Limitations {#undo-redo}

AEM stores a history of actions that you perform and the sequence in which you performed them so that you can undo multiple actions in the order that you performed them and redo them to re-apply one or more of the actions if necessary.

If an element on the content page is selected (such as a text component), then the undo and redo command applies to the selected item.

The behavior of the undo and redo commands is similar to that in other software. Use the commands to restore the recent state of your web page as you make decisions about content. For example, if you move a text paragraph to a different location on the page, you can use the undo command to move the paragraph back. If you then decide that the previous position was better, use the redo command to "undo the undo".

For example, you can:

* Redo actions as long as you have not made a page edit since you used undo.
* Undo a maximum of 20 edit actions (default setting).
* Also use [Keyboard shortcuts](/help/sites-cloud/authoring/sites-console/keyboard-shortcuts.md) for undo and redo.

You can use undo and redo for the following types of page changes:

* Adding, editing, removing, and moving paragraphs
* In-place editing of paragraph content
* Copying, cutting, and pasting items within a page

>[!NOTE]
>
>* Special permissions are required to undo and redo changes to files and images.
>* The history of changes to files and images lasts for a minimum of ten hours. Beyond this time however, the undo of the changes is not guaranteed. Your administrator can change the default time of ten hours.
>* Your system administrator can configure various aspects of the Undo/Redo features according to the requirements for your instance.
