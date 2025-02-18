---
title: Extending the Universal Editor
description: Learn about the different options to extend the capabilities of Universal Editor to support the needs of your content authors.
feature: Developing
role: Admin, Architect, Developer
---

# Extending the Universal Editor {#extending}

Learn about the different options to extend the capabilities of Universal Editor to support the needs of your content authors.

>[!TIP]
>
>The Universal Editor also offers several [customization options,](/help/implementing/universal-editor/customizing.md) allowing you to better meet your project needs.

## Extensions {#extensions}

As an Adobe Experience Cloud service, the Universal Editor's UI can be extended using the App Builder and Experience Manager. Adobe offers many ready-made extensions that you can use for your project.

* **[AEM Product Picker for Universal Editor](https://developer.adobe.com/uix/docs/extension-manager/extension-developed-by-adobe/ue-product-picker/)**: Integrate Adobe Commerce data by selecting or removing product data from the editor.
* **[Universal Editor Content Drafts](https://developer.adobe.com/uix/docs/extension-manager/extension-developed-by-adobe/universal-editor-content-drafts/)**: Create, edit, and manage multiple drafts of content.
* **[Configurable Asset Picker](https://developer.adobe.com/uix/docs/extension-manager/extension-developed-by-adobe/configurable-asset-picker/)**: Enable asset selection from repositories other than the one used by the edited page.
* **Forms Rule Editor**: Add dynamic behavior to AEM Forms fields visually, without coding.
* **[Export Content Fragments to Adobe Target](https://developer.adobe.com/uix/docs/extension-manager/extension-developed-by-adobe/exporting-content-fragment-to-adobe-target/)**: Export Content Fragments, created in Adobe Experience Manager as a Cloud Service to Adobe Target to be used as offers in Target activities, to test and personalize experiences at scale.
* **[Content Fragment Workflows](https://developer.adobe.com/uix/docs/extension-manager/extension-developed-by-adobe/content-fragments-workflows/)**: Initiate an AEM workflow for selected content fragments.

## Extending the UI {#extending-ui}

The Universal Editor's UI extensions are JavaScript applications built with Adobe App Builder. Using these same tools, you can also add your own buttons and actions to the header menu and properties panel as well as create your own events for the Universal Editor.

If you would like to explore the possibilities of creating your own extensions, please see the following resources:

1. [UI Extensibility](https://developer.adobe.com/uix/docs/) - This is the developer documentation for UI extension.
1. [UI Extensibility Guides](https://developer.adobe.com/uix/docs/guides/) - Step-by-step instructions on how to develop your own extension
1. [The Universal Editor UI Extension Points](https://developer.adobe.com/uix/docs/services/aem-universal-editor/) - Universal Editor-specific extension point documentation

>[!TIP]
>
>If you prefer learning by example, please see the [AEM UI extensibility tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/developing/extensibility/ui/overview). Though it focuses on extending the Content Fragment console, the concepts for implementing a UI extension in the Universal Editor are the same.

[Using Extension Manager in AEM Sites](https://developer.adobe.com/uix/docs/extension-manager/), you can enable or disable your extensions on a per-instance basis, access Adobe's first-party extensions including those for the Universal Editor, and much more.

## Extension Points {#extension-points}

In addition to UI extensibility, the Universal Editor offers many other flexible extension points to enable seamless integration of custom business requirements.

* **[Blocks](/help/edge/developer/block-collection.md)**: In simple JSON format, projects can adjust the blocks and UE features available for content creation.
* **3rd-Party Storage**: The Universal Editor can federate the editing of content from different sources, even when they are displayed on the same page.
* **Custom Buttons**: Implement specific actions for general contexts or particular content types. 
* **[Custom User Interface](#extending-ui)**: Extensions can display necessary UI in side-panels or modal dialogs.
* **Custom Data Types**: Create input methods tailored to your requirements or enable authors to reference content from proprietary backends, like a product picker.
* **[Events](/help/implementing/universal-editor/events.md)**: Extensions receive events about the author's actions and selections on the page to respond appropriately.
