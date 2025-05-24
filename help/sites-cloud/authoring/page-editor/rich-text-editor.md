---
title: Use the Rich Text Editor in [!DNL Adobe Experience Manager] to author content.
description: Use the [!DNL Experience Manager] Rich Text Editor to author content.
exl-id: 15c175f8-11de-4475-87a9-920219a4c004
solution: Experience Manager Sites
feature: Authoring
role: User
---
# Use the Rich Text Editor to author content {#use-rich-text-editor-to-author-content}

The Rich Text Editor (RTE) is a basic building block to add textual content to [!DNL Adobe Experience Manager]. Also, many other components that allow authoring are based on RTE. Experience Manager developers can customize RTE and administrators configure RTE for use by authors.

## In-place editing {#in-place-editing}

Selecting a text-based component with a single click to reveal the [component toolbar](/help/sites-cloud/authoring/page-editor/editor-side-panel.md#components-browser).

![The component toolbar](/help/sites-cloud/authoring/assets/editing-component-toolbar.png)

Clicking again or initially selecting the component with a slow double-click opens in-place editing. The editing mode contains a toolbar. You can edit the content and make basic formatting changes.

![In place editing with the RTE](/help/sites-cloud/authoring/assets/rte-in-place-editing.png)

Typically, the toolbar provides the following options:

* **Format**: Emphasize text as bold or italic or underline the text.
* **Lists**: Create bulleted or numbered lists and set the indentation.
* **Hyperlink**: Create links.
* **Unlink**: Remove hyperlink.
* **Full Screen**: Open the editor in full-screen mode.
* **Close**: Stop editing.
* **Save**: Save changes.

## Full-screen editing {#full-screen-editing}

For text-based components, click the full-screen mode ![RTE full screen button](/help/sites-cloud/authoring/assets/editing-full-screen.png) from the [toolbar](/help/sites-cloud/authoring/page-editor/editor-side-panel.md#components-browser) to open the rich text editor and hides the rest of the page content.

Full screen mode displays all the configured options that you can use for authoring. The availability of options [depends on the configuration](/help/implementing/developing/extending/rich-text-editor.md).

![RTE in full screen mode](/help/sites-cloud/authoring/assets/rte-full-screen.png)

Further rich text editor options include:

* **Anchor**: Create an anchor in the text that you can later link to or create a reference to.
* **Align Text Left**.
* **Center Text**.
* **Align Text Right**.

Click minimize to close the full-screen mode.

>[!TIP]
>
>Copying nested lists from [!DNL Microsoft Word] into the RTE can give inconsistent results. Instead, paste as text and do manual adjustment.

>[!MORELIKETHIS]
>
>* [Configure rich text editors](/help/implementing/developing/extending/rich-text-editor.md)
