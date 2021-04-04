---
title: Configure RTE to create accessible web pages and sites.
description: Learn to configure Rich Text Editor to create accessible sites in [!DNL Adobe Experience Manager].
contentOwner: AG
exl-id: 54050fc9-0348-4033-8e2b-b3897588cb62
---
# Configure RTE to create accessible sites {#configure-rte-accessible-sites}

[!DNL Adobe Experience Manager] supports standard accessibility features, such as alternate text for images, and extra features that can be accessed when creating content. Content authors use these features with components that use the rich text editor (RTE). The features includes adding alt-text, structural information through headings and paragraph elements, and so on.

For an understanding of typical configurations of RTE, see [configure RTE](rich-text-editor.md) and [configure RTE plug-ins for specific functionality](configure-rich-text-editor-plug-ins.md).

Use the RTE plug-ins configuration to configure and customize the accessibility-related features. For example, use `paraformat` to add extra block level semantic elements, including extending the number of heading levels supported beyond the basic `H1`, `H2` and `H3` provided by default. The rich text editing is possible using many components from the authoring user interface. The commonly used components are text, image, download, and so on.

The RTE functionality can be made available in many components. The primary component is the `Text` component.

For the `Text` component in [!DNL Experience Manager], the following screenshot displays the rich text editor with a range of plug-ins enabled, including `paraformat`:

  ![RTE Text component in full-screen-mode](assets/rte-toolbar-full-screen-mode.png)

## Configure the plug-in features {#configuring-the-plugin-features}

For instructions to configure RTE, see [configure the Rich Text Editor](rich-text-editor.md) page. The article covers:

* [Plug-ins and their features](rich-text-editor.md#aboutplugins)
* [Configuration locations](rich-text-editor.md#understand-the-configuration-paths-and-locations)
* [Activate a plug-in and configure the features property](rich-text-editor.md#enable-rte-functionalities-by-activating-plug-ins)
* [Configure other functionalities of the RTE](rich-text-editor.md#enable-rte-functionalities-by-activating-plug-ins)

To activate a few or all features for a plug-in, configure the plug-in within the appropriate `rtePlugins` sub-branch in CRXDE Lite.

![CRXDE Lite showing an example rtePlugin](assets/example-rteplugin-crxde-lite.png)

### Example to specify paragraph formats available in RTE selection field {#example-specifying-paragraph-formats-available-in-rte-selection-field}

New semantic block formats are made available for selection.

1. Depending on your RTE, determine and navigate to the [configuration location](rich-text-editor.md#understand-the-configuration-paths-and-locations).
1. [Enable the paragraphs selection field](rich-text-editor.md) by [activating the plug-in](rich-text-editor.md#enable-rte-functionalities-by-activating-plug-ins).
1. [Specify the formats you want to have available in the paragraphs selection field](rich-text-editor.md).
1. The paragraph formats are then available to the content author from the selection fields in the RTE.

With structural elements available in the RTE via the paragraph format options, [!DNL Experience Manager] provides a good basis for the development of accessible content. Content authors cannot use the RTE to format font size or colors or other related attributes, preventing the creation of inline formatting. Instead, the authors can select the appropriate structural elements, such as headings and use global styles chosen from the Styles option to ensure clean markup and greater options for users who browse with their own style sheets and correctly structured content.

## Use of the Source Edit feature {#use-of-the-source-edit-feature}

In some cases, content authors will find it necessary to examine and adjust the HTML source code created using the RTE. For example, a piece of content created within the RTE may require more markup to ensure compliance with WCAG 2.0. This can be done with the [source edit](rich-text-editor.md#aboutplugins) option of the RTE. You can specify the [`sourceedit` feature on the `misctools` plug-in](rich-text-editor.md#aboutplugins).

>[!CAUTION]
>
>Use the `sourceedit` feature carefully. Any typing errors and the unsupported features can introduce issues.

<!--
TBD ENGREVIEW: Is this only applicable to Classic UI? 

## Adding Support for further HTML Elements and Attributes {#adding-support-for-additional-html-elements-and-attributes}

To further extend the accessibility features of [!DNL Experience Manager], it is possible to extend the existing components based on the RTE (such as the `Text` and `Table` components) with extra elements and attributes.

The following procedure illustrates how to extend the `Table` component with a `Caption` element that provides information about a data table to assistive technology users:

### Example: Add a caption to a table properties dialog {#example-adding-the-caption-to-the-table-properties-dialog}

In the constructor of the `TablePropertiesDialog`, add an extra text input field that is used for editing the caption. Set the `itemId` to `caption` (the DOM attribute’s name) to automatically handle its content.

In a `Table`, set the attribute to the DOM element or or remove it from the DOM element. The dialog in the `config` object passed the value. Set or remove the DOM attributes using the corresponding `CQ.form.rte.Common` methods (`com` is a shortcut for `CQ.form.rte.Common`). Using `CQ.form.rte.Common` methods avoids common pitfalls with browser implementations.

>[!NOTE]
>
>This procedure is only suitable for the classic UI.

### Step-by-step instructions {#step-by-step-instructions}

1. Start CRXDE Lite. For example: [http://localhost:4502/crx/de/](http://localhost:4502/crx/de/)

1. Copy `/libs/cq/ui/widgets/source/widgets/form/rte/commands/Table.js` to `/apps/cq/ui/widgets/source/widgets/form/rte/commands/Table.js`. Create intermediate folders if those do not exist.

1. Copy `/libs/cq/ui/widgets/source/widgets/form/rte/plugins/TablePropertiesDialog.js` to `/apps/cq/ui/widgets/source/widgets/form/rte/plugins/TablePropertiesDialog.js`.

1. Open `/apps/cq/ui/widgets/source/widgets/form/rte/plugins/TablePropertiesDialog.js` file to edit.

1. In the `constructor` method, before the mention of `var dialogRef = this;`, add the following code:

   ```javascript
   editItems.push({
       "itemId": "caption",
       "name": "caption",
       "xtype": "textfield",
       "fieldLabel": CQ.I18n.getMessage("Caption"),
       "value": (this.table && this.table.caption ? this.table.caption.textContent : "")
   });
   ```

1. Open `/apps/cq/ui/widgets/source/widgets/form/rte/commands/Table.js` file.

1. Add the following code at the end of the `transferConfigToTable` method:

   ```javascript
   /**
    * Adds Caption Element
   */
   var captionElement;
   if (dom.firstChild && dom.firstChild.tagName.toLowerCase() == "caption")
   {
      captionElement = dom.firstChild;
   }
   if (config.caption)
   {
       var captionTextNode = document.createTextNode(config.caption)
       if (captionElement)
       {
          dom.replaceNode(captionElement.firstChild,captionTextNode);
       } else
       {
           captionElement = document.createElement("caption");
           captionElement.appendChild(captionTextNode);
           if (dom.childNodes.length>0)
           {
              dom.insertBefore(captionElement, dom.firstChild);
           } else
           {
              dom.appendChild(captionElement);
           }
       }
   } else if (captionElement)
   {
     dom.removeChild(captionElement);
   }
   ```

1. To save your changes, click **[!UICONTROL Save All]**.

## Best practices and limitations {#best-practices-limitations-tips}

* A plain text field is not the only type of input allowed for the value of the caption element. You can use any ExtJS widget, that provides the caption’s value through its `getValue()` method.
* To add editing capabilities for more elements and attributes, ensure that:

  * The `itemId` property for each corresponding field is set to the name of the appropriate DOM attribute (`TablePropertiesDialog`).
  * The attribute is set and/or removed on the DOM element explicitly (`Table`).
-->

>[!MORELIKETHIS]
>
>* [A quick guide to WCAG standards](/help/onboarding/accessibility/quick-guide-wcag.md)
>* [How to create accessible content in Experience Manager](/help/sites-cloud/authoring/fundamentals/accessible-content.md)
